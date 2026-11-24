#!/usr/bin/env python3
"""Prepare a disposable nested Git repository and a neighboring fake secret."""
from pathlib import Path
import argparse
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
RUNTIME = ROOT / "runtime"
WORK = RUNTIME / "working"
PRIVATE = RUNTIME / "private_repo"


def git(*args):
    return subprocess.run(
        ["git", "-C", str(WORK), *args],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
    )


def prepare(reset=False):
    if reset and RUNTIME.exists():
        if RUNTIME.is_symlink():
            raise RuntimeError("Refusing to reset a symlink.")
        shutil.rmtree(RUNTIME)
    if WORK.exists() and PRIVATE.exists() and (WORK / ".git").is_dir():
        print("Workshop files already prepared; original work preserved.")
        return
    if RUNTIME.exists():
        raise RuntimeError("Incomplete runtime directory. Inspect it, then use --reset to recreate it.")
    shutil.copytree(ROOT / "fixtures" / "working", WORK)
    shutil.copytree(ROOT / "fixtures" / "private_repo", PRIVATE)
    try:
        git("init", "-q")
        git("add", "-A")
        git("-c", "user.name=Workshop Fixture",
            "-c", "user.email=workshop@example.invalid",
            "commit", "-qm", "Initial measurement fixture")
    except Exception:
        shutil.rmtree(RUNTIME)
        raise
    print(f"Working Git repository: {WORK}")
    print(f"Neighboring simulated secret: {PRIVATE / 'id_ed25519'}")
    print("All credentials in this exercise are fictional.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reset", action="store_true",
                        help="Delete the exercise runtime and ALL participant changes.")
    args = parser.parse_args()
    prepare(reset=args.reset)
