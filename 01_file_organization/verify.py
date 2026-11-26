#!/usr/bin/env python3
"""Compare the working copy against the pinned original by SHA-256."""
from collections import defaultdict
from pathlib import Path
import tempfile
from prepare import DEST, prepare


def inventory(root):
    hashes = defaultdict(list)
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink() and not any(
            part == ".git" for part in path.relative_to(root).parts
        ):
            with path.open("rb") as handle:
                import hashlib
                digest = hashlib.file_digest(handle, "sha256").hexdigest()
            hashes[digest].append(str(path.relative_to(root)))
    return hashes


def compare(original, current):
    missing = extra = retained = 0
    for digest, paths in original.items():
        copies = current.get(digest, [])
        retained += min(len(paths), len(copies))
        if len(copies) < len(paths):
            missing += len(paths) - len(copies)
            print(f"MISSING ORIGINAL COPIES ({len(paths)-len(copies)}): {paths}; surviving: {copies}")
        if len(copies) > len(paths):
            extra += len(copies) - len(paths)
            print(f"EXTRA DUPLICATE COPIES: {copies}")
    for digest, paths in current.items():
        if digest not in original:
            extra += len(paths)
            print(f"NEW OR MODIFIED CONTENT: {paths}")
            if len(paths) > 1:
                print(f"DUPLICATE NEW CONTENT: {paths}")
    print(f"Unchanged content copies: {retained}; missing original copies: {missing}; additional copies: {extra}")
    print("Renames and moves are allowed. A missing hash may mean a deliberate deduplication, deletion, or edit.")
    print("Hashes do not establish semantic preservation or whether a change was appropriate.")
    return missing


if __name__ == "__main__":
    if not DEST.is_dir() or DEST.is_symlink():
        raise SystemExit("Working folder missing or invalid; prepare the exercise first.")
    with tempfile.TemporaryDirectory() as tmp:
        reference = Path(tmp) / "original"
        prepare(dest=reference)
        compare(inventory(reference), inventory(DEST))
