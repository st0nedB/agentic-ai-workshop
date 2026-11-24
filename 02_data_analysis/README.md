# Task 02 — Data analysis: ISAC UAV measurement data

## Workshop exercise

The organizer will supply one `.h5` measurement file in `02_data_analysis/data/`. Participants do not need to download or decrypt the dataset during the workshop.

Inspect the HDF5 groups, datasets, shapes and metadata. Define an Agent Contract, review a proposed analysis plan, and apply a visualization skill. Produce two interpretable plots, the generating code, and a short interpretation in `results/`. Preserve the input file and verify units and assumptions against the available documentation.

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
