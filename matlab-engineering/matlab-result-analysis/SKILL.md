---
name: matlab-result-analysis
description: Use when analyzing MATLAB experiment outputs, comparing runs, computing summary metrics, or producing compact result tables and figures from saved artifacts.
---

# MATLAB Result Analysis

## Purpose

Turn raw MATLAB outputs into metrics, comparisons, and decision-ready summaries.

## When to use

- Comparing experiment or simulation runs
- Computing summary statistics and performance metrics
- Converting raw arrays into tables and plots
- Writing concise result summaries from MATLAB outputs

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before saving summaries.

## Workflow

1. Load raw outputs and align them by scenario or run ID.
2. Compute the metrics that matter to the task.
3. Build tables first, then plots from those tables.
4. Highlight the baseline and the best or worst cases explicitly.
5. Save raw summaries and a human-readable comparison figure.

## Always

- Keep metric definitions explicit.
- Separate preprocessing from metric computation.
- Preserve raw data alongside aggregated summaries.
- Mark failed or incomplete runs clearly.
- Avoid overclaiming from a single metric.

## Example code

```matlab
summaryTbl = table(run_id, rmse, overshoot, settle_time);
writetable(summaryTbl, 'output/matlab/summary.csv');
```
