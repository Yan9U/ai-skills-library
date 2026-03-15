---
name: matlab-paper-plot
description: Use when creating publication-style MATLAB figures for papers, theses, or reports with consistent sizing, typography, export settings, and comparison-ready layouts.
---

# MATLAB Paper Plot

## Purpose

Generate publication-ready MATLAB figures with reproducible sizing and export settings.

## When to use

- Paper or thesis figures
- Report figures that must survive PDF export
- Multi-panel comparison plots
- Figures requiring vector export and consistent typography

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before exporting.

## Workflow

1. Set target figure size in inches or centimeters.
2. Choose fonts, line widths, marker sizes, and color palette deliberately.
3. Remove chart junk and keep labels concise.
4. Export to vector format when possible.
5. Re-open the exported file to confirm readability.

## Always

- Use consistent fonts across all figures in the document.
- Prefer white backgrounds unless the publication style says otherwise.
- Keep legends outside dense data regions.
- Use line widths and marker sizes that survive downscaling.
- Export PDF or SVG when possible, PNG only when raster is required.

## Example code

```matlab
fig = figure('Units', 'inches', 'Position', [1 1 3.4 2.4]);
plot(x, y, 'LineWidth', 1.2);
set(gca, 'FontName', 'Times New Roman', 'FontSize', 9);
exportgraphics(fig, 'output/matlab/paper_plot.pdf', 'ContentType', 'vector');
```
