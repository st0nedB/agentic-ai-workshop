#!/usr/bin/env bash
# Compare the same OpenCode agent with direct access and a restricted container.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
WORK="$ROOT/runtime/working"
PRIVATE="$ROOT/runtime/private_repo"
IMAGE="workshop-agent-sandbox:local"
MODE="$([ "$#" -gt 0 ] && echo "$1" || echo help)"

usage() {
  cat <<'TXT'
Usage: bash 03_sandboxing/run.sh prepare|reset|direct|verify|isolated

Use 'direct' to run OpenCode in the Codespace. Use 'isolated' to run
OpenCode inside a restricted Docker container.
For isolated inference, set OPENROUTER_API_KEY in the Codespace shell.
Optional: WORKSHOP_MODEL (default: openrouter/auto).
TXT
}
prepare() { python3 "$ROOT/prepare.py"; }
ensure_prepared() { [ -d "$WORK/.git" ] || prepare; }
ensure_docker() {
  command -v docker >/dev/null && docker info >/dev/null 2>&1 || {
    echo "Docker unavailable. Rebuild the Codespace with Docker-in-Docker." >&2
    exit 1
  }
  local version cached parent_version child_version
  version="$(npm list --global --depth=0 --json @opencode/cli | node -e 'const fs=require("fs"); const p=JSON.parse(fs.readFileSync(0,"utf8")); const v=p.dependencies?.["@opencode/cli"]?.version; if (!v) process.exit(1); console.log(v);')" || {
    echo "Cannot determine installed OpenCode package version." >&2; exit 1;
  }
  cached="$(docker image inspect --format '{{index .Config.Labels "workshop.opencode.version"}}' "$IMAGE" 2>/dev/null || true)"
  if [ "$cached" != "$version" ]; then
    echo "Building the isolated agent image with OpenCode $version..."
    docker build --build-arg "OPENCODE_VERSION=$version" -t "$IMAGE" -f "$ROOT/Dockerfile" "$ROOT"
  fi
  parent_version="$(opencode --version)"
  child_version="$(docker run --rm --network none "$IMAGE" opencode --version)"
  if [ "$parent_version" != "$child_version" ]; then
    echo "OpenCode version mismatch: direct=$parent_version isolated=$child_version" >&2
    exit 1
  fi
  echo "OpenCode version verified in both environments: $parent_version"
}
container_args() {
  local uid gid
  uid="$(id -u)"
  gid="$(id -g)"
  RUN_ARGS=(
    --rm
    --user "$uid:$gid"
    --cap-drop ALL
    --security-opt no-new-privileges
    --pids-limit 128
    --memory 2g
    --cpus 1
    --read-only
    --tmpfs "/tmp:rw,nosuid,nodev,size=128m"
    --tmpfs "/home/node:rw,nosuid,nodev,uid=$uid,gid=$gid,mode=700,size=512m"
    --workdir /lab/working
    --mount "type=bind,source=$WORK,target=/lab/working"
    --mount "type=bind,source=$WORK/.git,target=/lab/working/.git,readonly"
  )
}
case "$MODE" in
  help|--help|-h) usage ;;
  prepare) prepare ;;
  reset) python3 "$ROOT/prepare.py" --reset ;;
  direct)
    ensure_prepared
    command -v opencode >/dev/null || { echo "OpenCode not installed." >&2; exit 1; }
    echo "DIRECT: the agent can access both the working repository and neighboring files."
    cd "$WORK"
    exec opencode
    ;;
  verify)
    ensure_prepared
    ensure_docker
    container_args
    python3 - "$PRIVATE/id_ed25519" "$WORK/.git" <<'PY'
import os, sys
print("DIRECT Codespace:")
print("  Can access dummy secret:", os.access(sys.argv[1], os.R_OK))
print("  Can write Git metadata:", os.access(sys.argv[2], os.W_OK))
PY
    docker run "${RUN_ARGS[@]}" --network none --entrypoint python3 "$IMAGE" -c '
from pathlib import Path
data = Path("/lab/working/measurements.csv")
secret = Path("/lab/private_repo/id_ed25519")
repo = Path("/lab/working/.git")
assert data.is_file(), "data unavailable"
assert (repo / "HEAD").is_file(), "Git metadata unavailable"
assert not secret.exists(), "unexpected secret access"
try:
    (repo / "probe").write_text("demo")
except OSError: pass
else:
    (repo / "probe").unlink()
    raise AssertionError("Git metadata is writable")
out = Path("/lab/working/results")
out.mkdir(exist_ok=True)
test = out / ".write-probe"
test.write_text("demo")
test.unlink()
print("ISOLATED container:")
print("  Measurement data: readable")
print("  Dummy key: inaccessible")
print("  Git history: readable")
print("  Git metadata: read-only")
print("  Results: writable")
'
    ;;
  isolated)
    ensure_prepared
    ensure_docker
    [ -n "${OPENROUTER_API_KEY:-}" ] || {
      echo "OPENROUTER_API_KEY is required in the parent Codespace shell." >&2; exit 1
    }
    IP="$(docker network inspect bridge --format '{{(index .IPAM.Config 0).Gateway}}')"
    [ -n "$IP" ] && [ "$IP" != "<no value>" ] || {
      echo "No Docker bridge IP found." >&2; exit 1
    }
    PORT="${WORKSHOP_GATEWAY_PORT:-8765}"
    MODEL="${WORKSHOP_MODEL:-openrouter/auto}"
    python3 "$ROOT/gateway.py" --bind "$IP" --port "$PORT" --model "$MODEL" &
    GATEWAY_PID=$!
    trap 'kill "$GATEWAY_PID" 2>/dev/null || true' EXIT
    READY=0
    for _ in {1..20}; do
      if curl -fsS --max-time 1 "http://$IP:$PORT/health" >/dev/null 2>&1; then
        READY=1; break
      fi
      kill -0 "$GATEWAY_PID" 2>/dev/null || break
      sleep 0.25
    done
    [ "$READY" = 1 ] || { echo "Internal inference gateway failed." >&2; exit 1; }
    export WORKSHOP_GATEWAY_BASE_URL="http://$IP:$PORT/v1"
    export WORKSHOP_GATEWAY_MODEL="$MODEL"
    OPENCODE_CONFIG_CONTENT="$(python3 - <<'PY'
import json, os
base = os.environ["WORKSHOP_GATEWAY_BASE_URL"]
model = os.environ["WORKSHOP_GATEWAY_MODEL"]
print(json.dumps({
    "$schema": "https://opencode.ai/config.json",
    "provider": {
        "workshop_gateway": {
            "npm": "@opencode/ai/providers/openai-compatible",
            "name": "Workshop inference relay",
            "options": {"baseURL": base, "apiKey": "not-a-secret"},
            "models": {model: {
                "name": "Workshop model",
                "limit": {"context": 128000, "output": 8192}
            }}
        }
    },
    "model": "workshop_gateway/" + model
}))
PY
)"
    export OPENCODE_CONFIG_CONTENT
    container_args
    echo "ISOLATED: working directory mounted read-write, .git mounted read-only."
    echo "Neighboring dummy key excluded. Real model API key stays in the parent."
    docker run -it "${RUN_ARGS[@]}" --network bridge \
      -e OPENCODE_CONFIG_CONTENT -e HOME=/home/node "$IMAGE" opencode
    ;;
  *) usage >&2; exit 2 ;;
esac
