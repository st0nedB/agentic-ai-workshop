#!/usr/bin/env bash
# Prepare exercises independently; preserve existing participant work.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
failed=0
prepare() {
  local name="$1" script="$2"
  echo "Preparing $name..."
  if ! python3 "$script"; then
    echo "ERROR: $name preparation failed. Retry with: python3 $script" >&2
    failed=1
  fi
}
prepare "Exercise 1" 01_file_organization/prepare.py
prepare "Exercise 4" 03_sandboxing/prepare.py
exit "$failed"
