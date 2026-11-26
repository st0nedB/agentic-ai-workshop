#!/usr/bin/env python3
"""Generate a small, reproducible synthetic sensor recording for Exercise 2."""
import argparse
from pathlib import Path
import h5py
import numpy as np

DEFAULT = Path(__file__).resolve().parents[1] / "data" / "synthetic.h5"


def generate(path):
    rng = np.random.default_rng(42)
    time = np.arange(1000, dtype=np.float64) / 100
    signal = np.column_stack([
        np.sin(2 * np.pi * 3 * time),
        0.6 * np.sin(2 * np.pi * 7 * time + 0.4),
    ]) + rng.normal(0, 0.08, (time.size, 2))
    path.parent.mkdir(parents=True, exist_ok=True)
    with h5py.File(path, "x") as handle:
        handle.attrs["description"] = "Synthetic workshop sensor recording; not real UAV data"
        handle.attrs["synthetic"] = True
        group = handle.create_group("measurement")
        group.attrs["sample_rate_hz"] = 100.0
        group.create_dataset("time_s", data=time).attrs["unit"] = "s"
        dataset = group.create_dataset("amplitude_v", data=signal)
        dataset.attrs["unit"] = "V"
        dataset.attrs["axes"] = "sample, channel"
    print(f"Created {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit(f"Refusing to overwrite {args.output}")
    generate(args.output)
