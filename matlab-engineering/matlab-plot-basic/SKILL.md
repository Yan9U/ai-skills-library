---
name: matlab-plot-basic
description: Use when creating basic MATLAB figures such as line, scatter, bar, histogram, or image plots with clear labels, units, and reproducible exports.
---

# MATLAB Plot Basic

## Purpose

Produce clean baseline MATLAB figures for inspection, debugging, or routine reporting.

## When to use

- Single-curve line plots
- Scatter or bar charts
- Histograms and images
- Fast exploratory visualization
- Small dashboards with one figure

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before exporting.

## Workflow

1. Decide figure type from data shape and intent.
2. Plot the minimum necessary elements first.
3. Add axis labels, units, title, and grid.
4. Export to a stable path with an explicit filename.
5. Re-check readability at the final size.

## Always

- Label axes with units.
- Use `figure`, `clf`, and explicit handles in repeatable scripts.
- Avoid legends when a single trace is obvious.
- Keep colors and markers consistent with the data type.
- Save the figure if it matters downstream.

## Example code

```matlab
fig = figure;
plot(t, y, 'LineWidth', 1.5);
grid on
xlabel('Time (s)');
ylabel('Amplitude');
saveas(fig, 'output/matlab/basic_plot.png');
```
