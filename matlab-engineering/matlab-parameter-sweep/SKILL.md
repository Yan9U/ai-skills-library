---
name: matlab-parameter-sweep
description: Use when running deterministic MATLAB parameter sweeps, grid searches, or sensitivity studies and collecting outputs into structured tables and plots.
---

# MATLAB Parameter Sweep

## Purpose

Run structured parameter sweeps in MATLAB and keep results reproducible, comparable, and easy to analyze.

## When to use

- One- or two-dimensional sweeps
- Sensitivity studies
- Hyperparameter or controller gain grids
- Design-space exploration

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before exporting sweep outputs.

## Workflow

1. Define sweep variables and their grids.
2. Separate run configuration from the evaluation function.
3. Execute the sweep with stable logging.
4. Store each run's inputs and outputs together.
5. Summarize with tables and comparison plots.

## Always

- Save the parameter grid used for the sweep.
- Keep run order deterministic.
- Label results with parameter names, not just indices.
- Log failures without losing the whole sweep.
- Distinguish exhaustive grids from sampled sweeps.

## Example code

```matlab
Kp_vals = 0.5:0.5:3.0;
for i = 1:numel(Kp_vals)
    results(i).Kp = Kp_vals(i);
    results(i).score = run_case(Kp_vals(i));
end
```
