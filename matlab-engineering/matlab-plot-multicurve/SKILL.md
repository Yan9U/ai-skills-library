---
name: matlab-plot-multicurve
description: Use when creating MATLAB plots with multiple curves, groups, subplots, or comparative overlays that need consistent styling and readable legends.
---

# MATLAB Plot Multicurve

## Purpose

Compare multiple signals or experiment groups clearly in one MATLAB visualization workflow.

## When to use

- Overlaying several curves on one axis
- Comparing baseline and treatment runs
- Building subplot-based result panels
- Plotting parameter sweeps or controller responses

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before exporting.

## Workflow

1. Decide whether the comparison belongs on one axis or separate subplots.
2. Fix a consistent color and line-style mapping before plotting.
3. Keep x-axis scaling and units aligned across comparable panels.
4. Place legends where they do not cover data.
5. Export a figure and, if needed, a summary table.

## Always

- Use display names for legend entries.
- Keep shared axes comparable.
- Do not mix too many traces on one axis without a reason.
- Use `tiledlayout` for multi-panel figures.
- Explain the comparison, not just the raw data.

## Example code

```matlab
tiledlayout(2,1);
nexttile
plot(t, y1, 'DisplayName', 'Baseline'); hold on
plot(t, y2, 'DisplayName', 'Controller A');
legend('Location', 'best'); grid on
```
