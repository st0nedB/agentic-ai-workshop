#!/usr/bin/env python3
"""Local smoke test for the workshop fixtures (does not need Docker)."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent


def check():
    with tempfile.TemporaryDirectory() as directory:
        working = Path(directory) / "working"
        shutil.copytree(ROOT / "fixtures" / "working", working)
        first = subprocess.run(["python3", "analyze.py"], cwd=working,
                               capture_output=True, text=True)
        assert first.returncode != 0, "The intentionally broken analysis should fail"
        assert "voltage_v" in first.stderr, first.stderr

        config_file = working / "config.json"
        config = json.loads(config_file.read_text(encoding="utf-8"))
        config["signal_column"] = "amplitude_v"
        config_file.write_text(json.dumps(config), encoding="utf-8")

        second = subprocess.run(["python3", "analyze.py"], cwd=working,
                                capture_output=True, text=True)
        assert second.returncode == 0, second.stderr
        assert (working / "results" / "summary.txt").is_file()
        assert "<svg" in (working / "results" / "signal.svg").read_text(encoding="utf-8")
        assert len((working / "measurements.csv").read_text().splitlines()) > 10

    dummy = (ROOT / "fixtures" / "private_repo" / "id_ed25519").read_text()
    assert "FAKE" in dummy and "BEGIN OPENSSH PRIVATE KEY" not in dummy
    script = (ROOT / "run.sh").read_text()
    assert "target=/lab/working/.git,readonly" in script
    assert "source=$WORK,target=/lab/working" in script
    assert "source=$PRIVATE" not in script
    print("PASS: broken fixture, repair, outputs, dummy secret, and mount declarations")


if __name__ == "__main__":
    check()
