#!/usr/bin/env python3
"""Load the CC BY 4.0 fictional workshop archive into a local working folder.

Source and attribution: see QUELLEN_UND_LIZENZ.md.
Uses only the Python standard library.
"""
from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import shutil
import tempfile
from urllib.request import Request, urlopen
from zipfile import ZipFile

SOURCE_REPO = "techczech/agents-for-reproducibility"
SOURCE_COMMIT = "8d9c85f491d7dcf9295f712298100662f62e37cb"
SOURCE_PARTS = ("sample-files", "messy-research-archive")
SOURCE_URL = f"https://codeload.github.com/{SOURCE_REPO}/zip/{SOURCE_COMMIT}"
EXPECTED_FILE_COUNT = 45
EXPECTED_TOTAL_BYTES = 16_256_497
ROOT = Path(__file__).resolve().parent
DEST = ROOT / "arbeitsordner"


def prepare(reset: bool = False) -> None:
    if DEST.exists():
        if not reset:
            print(f"Arbeitsordner vorhanden, keine Änderungen: {DEST}")
            return
        if DEST.is_symlink():
            raise RuntimeError("Arbeitsordner ist ein Symlink; Abbruch aus Sicherheitsgründen.")
        shutil.rmtree(DEST)
        print("Vorhandene Arbeitskopie gelöscht (--reset).")

    with tempfile.TemporaryDirectory(prefix=".ausgangsdaten-", dir=ROOT) as tmp:
        temp_root = Path(tmp)
        archive_file = temp_root / "original.zip"
        print(f"Lade 45 fiktive Beispieldateien herunter: {SOURCE_REPO}@{SOURCE_COMMIT[:12]}")
        request = Request(SOURCE_URL, headers={"User-Agent": "agentic-ai-workshop"})
        with urlopen(request, timeout=120) as response, archive_file.open("wb") as output:
            shutil.copyfileobj(response, output)

        extracted = temp_root / "extracted"
        extracted.mkdir()
        with ZipFile(archive_file) as archive:
            selected = []
            for item in archive.infolist():
                parts = PurePosixPath(item.filename).parts
                # GitHub snapshot ZIP has one repository root directory.
                if len(parts) < 4 or tuple(parts[1:3]) != SOURCE_PARTS or item.is_dir():
                    continue
                relative_parts = parts[3:]
                if any(part in (".", "..") for part in relative_parts):
                    raise RuntimeError("Unsicherer Dateipfad im Archiv.")
                # Never extract symlinks.
                if (item.external_attr >> 16) & 0o170000 == 0o120000:
                    raise RuntimeError("Unerwarteter Symlink im Quelldatensatz.")
                selected.append((item, Path(*relative_parts)))

            count = len(selected)
            total_bytes = sum(item.file_size for item, _ in selected)
            if count != EXPECTED_FILE_COUNT or total_bytes != EXPECTED_TOTAL_BYTES:
                raise RuntimeError(
                    f"Quelldatensatz unerwartet verändert: {count} Dateien, "
                    f"{total_bytes} Bytes (erwartet: {EXPECTED_FILE_COUNT}, "
                    f"{EXPECTED_TOTAL_BYTES})."
                )

            for item, relative in selected:
                destination = extracted / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(item) as source, destination.open("wb") as target:
                    shutil.copyfileobj(source, target)

        shutil.move(str(extracted), str(DEST))
    print(f"Fertig: {EXPECTED_FILE_COUNT} Dateien in {DEST}")
    print("Quelle und CC-BY-4.0-Hinweis: 01_dateichaos/QUELLEN_UND_LIZENZ.md")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Vorhandenen Arbeitsordner mit ALLEN Änderungen löschen und neu herunterladen.",
    )
    args = parser.parse_args()
    prepare(reset=args.reset)
