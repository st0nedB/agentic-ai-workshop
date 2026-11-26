#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
codex --version
opencode --version
pi --version
python3 --version
node --version
git --version
python3 -c 'import numpy, scipy, h5py, matplotlib, pandas'
python3 -c 'import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt; plt.plot([0, 1]); plt.savefig("/tmp/workshop-smoke.png")'
docker info >/dev/null
# Confirm SSH is installed and actually listening inside the dev container.
command -v sshd >/dev/null || test -x /usr/sbin/sshd
# The Dev Container sshd feature listens on port 2222 by default.
python3 - <<'PY'
import socket
import time

for attempt in range(10):
    try:
        with socket.create_connection(("127.0.0.1", 2222), timeout=2):
            print("SSH server reachable on port 2222")
        break
    except OSError as exc:
        if attempt == 9:
            raise SystemExit(f"SSH server not reachable on port 2222: {exc}")
        time.sleep(1)
PY
test "$(find 01_dateichaos/arbeitsordner -type f | wc -l)" -eq 45
test -d 03_sandboxing/runtime/working/.git
test -f 03_sandboxing/runtime/private_repo/id_ed25519
bash 03_sandboxing/run.sh verify
python3 03_sandboxing/test_lab.py
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
python3 02_data_analysis/fallback/generate.py --output "$tmp/synthetic.h5"
python3 02_data_analysis/fallback/reference_analysis.py --input "$tmp/synthetic.h5" --output "$tmp/results"
test -s "$tmp/results/time_series.png"
test -s "$tmp/results/spectrum.png"
test -s "$tmp/results/RESULTS.md"
python3 - <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, "01_dateichaos")
from verify import inventory, compare
root = Path("01_dateichaos/arbeitsordner")
original = inventory(root)
assert sum(map(len, original.values())) == 45
assert compare(original, original) == 0
sys.path.insert(0, "03_sandboxing")
from save_evidence import save
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    target = save(Path("03_sandboxing/runtime/working"), Path(tmp))
    assert (target / "analyze.py").is_file()
    assert (target / "OBSERVATIONS.md").is_file()
    assert not (target / "id_ed25519").exists()
PY
