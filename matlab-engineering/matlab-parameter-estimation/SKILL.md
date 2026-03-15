---
name: matlab-parameter-estimation
description: Use when fitting MATLAB models to data for curve fitting, system identification, least-squares estimation, or parameter calibration with residual checks and bounds.
---

# MATLAB Parameter Estimation

## Purpose

Estimate model parameters from data with explicit objective functions, bounds, and fit diagnostics.

## When to use

- Curve fitting
- Calibration of physical model parameters
- Least-squares identification
- Comparing fitted parameter sets
- Residual and uncertainty analysis

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using Optimization Toolbox functions.

## Workflow

1. Define the model, parameter vector, inputs, and measured outputs.
2. Choose an objective function and initial guess.
3. Add bounds or regularization if parameters are physically constrained.
4. Fit on data, then inspect residuals and parameter plausibility.
5. Report fit quality and sensitivity to initial conditions.

## Always

- Separate training and validation data when possible.
- Keep initial guesses explicit.
- State whether Toolbox functions such as `lsqcurvefit` are required.
- Fall back to `fminsearch` when no constrained solver is available.
- Save estimated parameters and fit metrics.

## Example code

```matlab
model = @(p, x) p(1) * exp(-p(2) * x);
obj = @(p) norm(model(p, xdata) - ydata)^2;
p_hat = fminsearch(obj, [1; 0.1]);
```
