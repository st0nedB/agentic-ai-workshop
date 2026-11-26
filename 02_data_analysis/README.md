# Exercise 2 — Analyze measurement data

**Block 2 · 30 minutes · Group work**

## Input and prerequisites

The organizer will supply one ISAC UAV measurement `.h5` file in `02_data_analysis/data/`. Participants do not need to download or decrypt it during the workshop. NumPy, SciPy, h5py, Matplotlib and pandas are preinstalled.

If the actual file is unavailable, generate a small, explicitly synthetic fallback from the repository root:

```bash
python3 02_data_analysis/fallback/generate.py
```

Use `02_data_analysis/data/synthetic.h5` and its [documented schema](fallback/README.md). It is not a reproduction of the real ISAC dataset.

## Workflow

1. **Inspect (5 min):** Identify the HDF5 groups, datasets, shapes, attributes and available documentation. Do not assume the dimensions or units.
2. **Define an Agent Contract (5 min):** Specify the input, goal, boundaries and definition of done. Record it in `results/AGENT-CONTRACT.md`. Preserve the input.
3. **Plan (5 min):** Ask the agent to propose a processing and visualization workflow without editing files. Review assumptions, units and plot choices before approving.
4. **Execute (10 min):** Inspect the [Scientific Visualization Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) by K-Dense. Find out how to make it available to your agent and use it to execute the approved plan. Save the analysis code and two interpretable plots.
5. **Verify (5 min):** Rerun the code, inspect the plots, check units against the evidence, and record assumptions and limitations.

Start your agent in `02_data_analysis/`. Save all deliverables under `02_data_analysis/results/`:

- Agent Contract and reproducible analysis code.
- Two plots with labeled axes and documented units where known.
- `RESULTS.md` with a short interpretation, input filename, run command, assumptions and checks.

Do not modify the measurement file or invent missing metadata. Compare findings with your group before continuing to [Exercise 3](EXERCISE-3.md).

## Optional dataset acquisition (organizer only)

[Original dataset](https://github.com/EMS-TU-Ilmenau/isac-uav-dataset) · [Documentation](https://ems-tu-ilmenau.github.io/isac-uav-dataset-docs/)

The original measurement data is **not stored on GitHub**. It is distributed as password-encrypted archives by TU Ilmenau. Each scenario contains measurements from three receivers: `VGH0`, `VGH1`, and `VGH2`.

From the repository root:

```bash
python 02_data_analysis/download_smallest.py --dry-run
python 02_data_analysis/download_smallest.py
```

The script determines the smallest complete scenario by comparing the advertised archive sizes, prompts for the official dataset password, downloads and decrypts the three receiver archives, and checks the original SHA-256 hashes. Six `.h5` files are saved in `02_data_analysis/data/`. Neither the password nor the data files are committed to Git.

Requirements: internet access to `resdata.tu-ilmenau.de`, the dataset password, and `openssl`. The automatic size comparison requires the server to expose accurate Content-Length information. If sizes cannot be determined, the script fails rather than guessing. The upstream repository does not provide per-scenario sizes.

License: [CC BY-NC-ND 4.0](https://github.com/EMS-TU-Ilmenau/isac-uav-dataset/blob/main/LICENSE). Please follow the source repository's attribution and access requirements.

> **For the organizer:** This folder contains the downloader, not a bundled scenario. To distribute actual data to participants without individual password entry, the data must be obtained and provisioned separately, in line with the dataset's access conditions and license.
