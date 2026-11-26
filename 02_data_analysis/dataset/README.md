# 0to1_H15_V5_VGH2: reduced channel and delay-Doppler video

Derived from measurement `0to1_H15_V5_VGH2` of the ISAC UAV dataset.

## Files

| File | Content |
|---|---|
| `0to1_H15_V5_VGH2_channel.h5` | Channel reduced to the 0–0.8 µs delay span (52.7 MB, was 995 MB) |
| `0to1_H15_V5_VGH2_target.h5` | Unchanged copy of the original target file |
| `0to1_H15_V5_VGH2_ddmap.mp4` | Delay-Doppler map video with UAV marker |

## Channel reduction

1. Source grid: 1280 frequencies, 3.7100625–3.79 GHz, Δf = 62.5 kHz (B = 80 MHz, 16 µs delay span, 12.5 ns resolution).
2. IFFT over frequency (1280 points) for each of the 96875 snapshots.
3. Keep the first 64 delay bins (0–0.8 µs). Energy beyond 0.8 µs is discarded, not aliased.
4. FFT back over 64 points. New grid: 64 frequencies, 3.7100625–3.7888125 GHz, Δf = 1.25 MHz. Bandwidth and delay resolution are unchanged.
5. All other datasets, attributes and dimension scales are copied unchanged. The HDF5 layout matches the original.

Check: the 64 delay taps agree with the original's first 64 taps to a relative error of 1.2e-8 (float32 rounding).

## Delay-Doppler video

1. Slow-time windows of 256 snapshots (81.92 ms), hop 128 snapshots (50 % overlap). This gives 755 frames.
2. Periodic Hann window over the 64 frequencies. No window over slow time.
3. Delay: IFFT over frequency, zero-padded to 128 points (×2 oversampling, 6.25 ns bins, 0–0.8 µs).
4. Doppler: FFT over slow time, zero-padded to 512 points (×2 oversampling, 6.1 Hz bins, ±1562.5 Hz), then fftshift.
5. Plot |X|² in dB, with a fixed scale of 0 to −60 dB relative to the overall maximum. Colormap: `cmr.torch` from cmasher.
6. Marker: UAV ground-truth delay and Doppler from `TargetParameters`, taken at each window's centre snapshot.
7. Frame rate 755 / 30.996 s ≈ 24.36 fps, so the video is as long as the measurement. Encoded as H.264 (CRF 18).

Zero-padding only interpolates. The resolution stays at 12.5 ns and 12.2 Hz.

## Source dataset, licence and citation

- Repository: <https://github.com/EMS-TU-Ilmenau/isac-uav-dataset>
- Documentation: <https://ems-tu-ilmenau.github.io/isac-uav-dataset-docs/>
- Licence: [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).
  It covers the measurement files, metadata and all other repository contents.
  The files here are adapted material under this licence.
- Cite:
  J. Beuster, C. Andrich, M. Döbereiner, S. Schieler, M. Engelhardt, C. Schneider and R. Thomä,
  "Measurement Testbed for Radar and Emitter Localization of UAV at 3.75 GHz,"
  *2023 17th European Conference on Antennas and Propagation (EuCAP)*, 2023, pp. 1–5,
  doi: [10.23919/EuCAP57121.2023.10133118](https://doi.org/10.23919/EuCAP57121.2023.10133118).
