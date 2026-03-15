---
name: matlab-monte-carlo
description: Use when running MATLAB Monte Carlo studies, uncertainty propagation, repeated random trials, or stochastic robustness analysis with controlled random seeds.
---

# MATLAB Monte Carlo

## Purpose

Run repeatable stochastic studies in MATLAB and summarize uncertainty with stable metrics.

## When to use

- Uncertainty propagation
- Randomized robustness studies
- Noise sensitivity analysis
- Distribution-based outcome estimates

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before saving run artifacts.

## Workflow

1. Define uncertain parameters and their distributions.
2. Fix `rng(seed)` for reproducibility unless the user asks otherwise.
3. Run enough trials to stabilize key metrics.
4. Aggregate mean, variance, quantiles, and failure rates.
5. Save both per-trial outputs and aggregated summaries.

## Always

- State the random seed.
- Separate sampled inputs from simulated outputs.
- Track trial count and stopping assumptions.
- Use confidence intervals or quantiles, not only averages.
- Check for pathological trials and numerical blow-ups.

## Example code

```matlab
rng(42);
N = 1000;
samples = randn(N, 1);
mu = mean(samples);
ci = prctile(samples, [2.5 97.5]);
```
