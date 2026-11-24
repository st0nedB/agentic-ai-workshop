#!/usr/bin/env python3
"""Find the smallest ISAC UAV scenario and download its original HDF5 files.

Requires Python 3.12+, OpenSSL, access to the TU Ilmenau data server,
and the official dataset decryption password. No password is saved.
"""
import argparse
import concurrent.futures
import getpass
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request

SOURCE = "https://raw.githubusercontent.com/EMS-TU-Ilmenau/isac-uav-dataset/main/scenarios.checksum"
SERVER = "https://resdata.tu-ilmenau.de/public/ei/ems/isac-uav-dataset/"
RECEIVERS = ("VGH0", "VGH1", "VGH2")
HERE = Path(__file__).resolve().parent


def load_checksums():
    with urllib.request.urlopen(SOURCE, timeout=30) as response:
        lines = response.read().decode("utf-8").splitlines()
    return dict(line.split(maxsplit=1)[::-1] for line in lines if line.strip())


def archive_size(url):
    """Read remote Content-Length without downloading the file."""
    try:
        with urllib.request.urlopen(
            urllib.request.Request(url, method="HEAD"), timeout=30
        ) as response:
            length = response.headers.get("Content-Length")
            if length is not None:
                return int(length)
    except Exception:
        pass
    with urllib.request.urlopen(
        urllib.request.Request(url, headers={"Range": "bytes=0-0"}), timeout=30
    ) as response:
        content_range = response.headers.get("Content-Range")
        if content_range and "/" in content_range:
            return int(content_range.rsplit("/", 1)[1])
        length = response.headers.get("Content-Length")
        if length and response.status == 200:
            return int(length)
    raise RuntimeError("Server does not publish a usable archive size: " + url)


def find_smallest_scenario(checksums):
    scenarios = sorted({
        name.removesuffix("_channel.h5").rsplit("_", 1)[0]
        for name in checksums
        if name.endswith("_channel.h5")
    })
    tasks = {
        (scenario, rx): f"{SERVER}{scenario}_{rx}.tar.bz2.encrypted"
        for scenario in scenarios
        for rx in RECEIVERS
    }
    results = {}
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(archive_size, url): key for key, url in tasks.items()}
        for future in concurrent.futures.as_completed(futures):
            key = futures[future]
            try:
                results[key] = future.result()
            except Exception as exc:
                failures.append((key, str(exc)))
    if failures:
        sample = "; ".join(f"{s}/{r}: {message}" for (s, r), message in failures[:3])
        raise RuntimeError(
            f"Cannot determine the global minimum: {len(failures)} of "
            f"{len(tasks)} archive sizes unavailable. {sample}"
        )
    ranking = sorted(
        (sum(results[(scenario, rx)] for rx in RECEIVERS), scenario)
        for scenario in scenarios
    )
    return ranking[0], len(ranking)


def copy_and_hash(source, destination):
    digest = hashlib.sha256()
    with open(destination, "wb") as target:
        while chunk := source.read(8 * 1024 * 1024):
            target.write(chunk)
            digest.update(chunk)
    return digest.hexdigest()


def download_scenario(scenario, checksums, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    password = getpass.getpass("Official ISAC UAV dataset password: ")
    if not password:
        raise RuntimeError("Password required.")
    for rx in RECEIVERS:
        stem = f"{scenario}_{rx}"
        expected = [f"{stem}_channel.h5", f"{stem}_target.h5"]
        if any(name not in checksums for name in expected):
            raise RuntimeError(f"No checksum available for {stem}")
        if all(
            (output_dir / name).exists()
            and hash_file(output_dir / name) == checksums[name]
            for name in expected
        ):
            print(f"{stem}: already verified")
            continue
        print(f"Downloading {stem}...")
        with tempfile.TemporaryDirectory(prefix=".isac-", dir=output_dir) as tmp:
            tmp = Path(tmp)
            encrypted = tmp / "source.encrypted"
            decrypted = tmp / "source.tar.bz2"
            url = f"{SERVER}{stem}.tar.bz2.encrypted"
            with urllib.request.urlopen(url, timeout=120) as response, open(encrypted, "wb") as file:
                shutil.copyfileobj(response, file, 8 * 1024 * 1024)
            proc = subprocess.run(
                ["openssl", "enc", "-d", "-aes256", "-pbkdf2",
                 "-pass", "stdin", "-in", str(encrypted), "-out", str(decrypted)],
                input=password + "\n",
                capture_output=True, text=True,
            )
            if proc.returncode:
                raise RuntimeError(f"Decryption failed for {stem}: {proc.stderr.strip()}")
            with tarfile.open(decrypted, "r:bz2") as archive:
                for filename in expected:
                    member = archive.extractfile(filename)
                    if member is None:
                        raise RuntimeError(f"Missing file in archive: {filename}")
                    temporary = tmp / filename
                    actual = copy_and_hash(member, temporary)
                    if actual != checksums[filename]:
                        raise RuntimeError(f"SHA-256 mismatch for {filename}")
                    os.replace(temporary, output_dir / filename)
            print(f"{stem}: verified")
    print(f"Ready: {output_dir}")


def hash_file(path):
    with open(path, "rb") as file:
        digest = hashlib.sha256()
        while chunk := file.read(8 * 1024 * 1024):
            digest.update(chunk)
        return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", help="Override automatic smallest-scenario selection")
    parser.add_argument("--dry-run", action="store_true", help="Check sizes only; do not download")
    parser.add_argument("--output", type=Path, default=HERE / "data")
    args = parser.parse_args()
    checksums = load_checksums()
    if args.scenario:
        scenario = args.scenario
    else:
        (size, scenario), count = find_smallest_scenario(checksums)
        print(f"Smallest of {count} scenarios: {scenario} "
              f"(three encrypted receiver archives, {size / 1024**3:.2f} GiB)")
    if args.dry_run:
        return
    download_scenario(scenario, checksums, args.output)


if __name__ == "__main__":
    main()
