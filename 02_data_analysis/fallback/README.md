# Synthetic fallback

This independently generated dataset is **not real ISAC or UAV measurement data**. It is a small reproducible two-channel recording with sinusoidal components and additive Gaussian noise.

| HDF5 entry | Shape | Unit or meaning |
|---|---|---|
| /measurement/time_s | (1000,) | Seconds |
| /measurement/amplitude_v | (1000, 2) | Volts; sample × channel |
| /measurement attribute sample_rate_hz | Scalar | 100 Hz |

Generate from the repository root:

```bash
python3 02_data_analysis/fallback/generate.py
```

The generator refuses to overwrite an existing file. For Exercise 3 only, if your own analysis is incomplete, run:

```bash
python3 02_data_analysis/fallback/reference_analysis.py
```

This produces a time series and an amplitude spectrum under `02_data_analysis/results/reference/`. Use the source code as the workflow evidence, not as the solution to Exercise 2. The reference analysis is specific to the synthetic schema.
