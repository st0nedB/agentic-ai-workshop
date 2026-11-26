# Faulty measurement analysis

This small, entirely synthetic sensor recording should be processed by `analyze.py`.

## Expected outputs

After repair, running `python3 analyze.py` should generate:

- `results/summary.txt`: count, mean, minimum, and maximum amplitude.
- `results/signal.svg`: amplitude versus time, with labeled axes.

Diagnose the failure before making changes.

Use the safety instructions in `AGENTS.md`.
