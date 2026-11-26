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
python3 -c 'import socket; socket.create_connection(("127.0.0.1", 22), timeout=5).close()'
test "$(find 01_dateichaos/arbeitsordner -type f | wc -l)" -eq 45
test -d 03_sandboxing/runtime/working/.git
test -f 03_sandboxing/runtime/private_repo/id_ed25519
bash 03_sandboxing/run.sh verify
