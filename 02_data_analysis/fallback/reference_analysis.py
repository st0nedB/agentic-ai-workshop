#!/usr/bin/env python3
"""Reference workflow for Exercise 3, using only the synthetic dataset."""
import argparse
from pathlib import Path
import h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def analyze(source, output):
    with h5py.File(source, "r") as handle:
        if not handle.attrs.get("synthetic", False):
            raise ValueError("This reference script expects the synthetic fallback.")
        group = handle["measurement"]
        time = group["time_s"][:]
        amplitude = group["amplitude_v"][:]
        fs = float(group.attrs["sample_rate_hz"])
    if amplitude.shape != (len(time), 2) or not np.allclose(np.diff(time), 1 / fs):
        raise ValueError("Unexpected synthetic dataset dimensions or sample spacing")
    output.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots()
    for channel in range(2):
        ax.plot(time, amplitude[:, channel], label=f"Channel {channel + 1}")
    ax.set(xlabel="Time (s)", ylabel="Amplitude (V)")
    ax.legend()
    fig.savefig(output / "time_series.png", dpi=150, bbox_inches="tight")
    plt.close(fig)

    centered = amplitude - amplitude.mean(axis=0)
    frequency = np.fft.rfftfreq(len(time), d=1 / fs)
    spectrum = 2 * np.abs(np.fft.rfft(centered, axis=0)) / len(time)
    spectrum[0] /= 2
    if len(time) % 2 == 0:
        spectrum[-1] /= 2
    fig, ax = plt.subplots()
    for channel in range(2):
        ax.plot(frequency, spectrum[:, channel], label=f"Channel {channel + 1}")
    ax.set(xlabel="Frequency (Hz)", ylabel="Single-sided amplitude (V)")
    ax.legend()
    fig.savefig(output / "spectrum.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    peaks = frequency[np.argmax(spectrum, axis=0)]
    (output / "RESULTS.md").write_text(
        f"# Synthetic reference analysis\n\nInput: {source.name}\n\n"
        f"Spectral peaks: {peaks[0]:.1f} Hz and {peaks[1]:.1f} Hz.\n"
        "Uniform sampling, two channels, rectangular FFT window; synthetic data only.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data/synthetic.h5")
    parser.add_argument("--output", type=Path, default=ROOT / "results/reference")
    args = parser.parse_args()
    analyze(args.input, args.output)
