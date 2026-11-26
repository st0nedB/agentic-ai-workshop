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
test "$(find 01_file_organization/working -type f | wc -l)" -eq 45
test -d 03_sandboxing/runtime/working/.git
test -f 03_sandboxing/runtime/private_repo/id_ed25519
bash 03_sandboxing/run.sh verify
python3 03_sandboxing/test_lab.py
# Verify the real measurement dataset, including Git LFS hydration.
python3 - <<'PY'
from pathlib import Path
import h5py

root = Path("02_data_analysis/dataset")
for name in ("channel.h5", "target.h5"):
    path = root / name
    assert path.is_file(), f"Missing dataset file: {path}"
    assert h5py.is_hdf5(path), f"Invalid HDF5 file (check Git LFS checkout): {path}"
    with h5py.File(path, "r") as data:
        datasets = []
        data.visititems(lambda name, obj: datasets.append(name)
                        if isinstance(obj, h5py.Dataset) and obj.size else None)
        assert datasets, f"No nonempty datasets in {path}"
    print(f"Verified {path}")

video = root / ".example" / "ddmap.mp4"
assert video.is_file(), f"Missing example video: {video}"
with video.open("rb") as stream:
    header = stream.read(32)
assert header[4:8] == b"ftyp", f"Invalid MP4 file (check Git LFS checkout): {video}"
PY
python3 - <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, "01_file_organization")
from verify import inventory, compare
root = Path("01_file_organization/working")
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
