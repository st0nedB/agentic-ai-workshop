# Exercise 2 — Analyze measurement data

**Block 2 · 30 minutes · Group work**

## Objective

Direct an AI agent through an unfamiliar scientific analysis: supply context, define success, review a plan, apply a visualization skill and verify the results. Choose your own analysis objective; there is no prescribed signal processing method or reference solution.

## Inputs

The [dataset documentation](dataset/README.md) describes a real ISAC UAV measurement. The repository contains these Git LFS files:

- `dataset/channel.h5` — measured channel data.
- `dataset/target.h5` — target data.
- `dataset/.example/ddmap.mp4` — example delay-Doppler visualization, for optional inspiration only.

Use one or both HDF5 files as appropriate to your objective. You do not need to reproduce the example video. If the files are missing or are Git LFS pointer files, run `git lfs pull --include="02_data_analysis/dataset/**"` from the repository root.

## Assignment

Open your configured agent from the exercise directory:

```bash
cd "$(git rev-parse --show-toplevel)"
cd 02_data_analysis
opencode  # or: codex
```

1. **Inspect and specify (7 min):** Ask the agent to inspect the HDF5 structure, shapes, attributes and documentation. Choose a feasible analysis objective and define an Agent Contract with goal, inputs, boundaries and definition of done. Treat the original measurement files as read-only; write all generated work to `results/`. Save the contract in `results/CONTRACT.md`.
2. **Plan and review (6 min):** Ask for a plan without editing the dataset or implementing the analysis yet. Review the proposed transformations, axes, units, assumptions and checks. Approve or revise the plan before execution.
3. **Apply a skill and execute (12 min):** Inspect the [Scientific Visualization Skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md). Determine how to use it with your chosen agent. Review third-party instructions and scripts before installing or running them. Have the agent execute the approved plan, producing reproducible code and two meaningful visualizations.
4. **Verify (5 min):** Inspect the plots and code. Check whether the results are physically plausible, axes and units are correct, and assumptions are supported by the dataset documentation. Do not invent missing metadata. Record limitations and the command required to reproduce the results.

## Deliverables and success criteria

Save the following in `results/`:

- `CONTRACT.md` — agreed objective, inputs, boundaries and success criteria.
- Analysis code with a reproducible execution command.
- Two meaningful, interpretable visualizations with appropriate labels and units.
- `RESULTS.md` — interpretation, assumptions, verification checks, limitations and any incomplete work.

Success means the outputs address your chosen objective, the original files remain unchanged, and another participant can understand and reproduce the implemented analysis.

Keep the analysis code for [Exercise 3](EXERCISE-3.md), even if you do not finish all deliverables.
