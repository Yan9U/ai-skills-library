---
name: matlab-optimization
description: Use when solving MATLAB optimization problems such as unconstrained, constrained, nonlinear, or toolbox-assisted design optimization with explicit objectives and constraints.
---

# MATLAB Optimization

## Purpose

Formulate and solve optimization problems in MATLAB with clear objectives, constraints, and validation logic.

## When to use

- Objective minimization or maximization
- Constrained design optimization
- Nonlinear calibration problems
- Solver comparison and robustness checks

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using Optimization Toolbox solvers.

## Workflow

1. Define variables, objective, constraints, and scales.
2. Pick the narrowest solver that matches the problem.
3. Provide initial guesses and bounds explicitly.
4. Inspect convergence, feasibility, and local-minimum risk.
5. Re-evaluate the final solution in the original model.

## Always

- Keep objective and constraints in separate functions when complexity grows.
- Normalize variables when scales differ widely.
- Record solver settings and random seeds.
- Fall back to `fminsearch` when advanced solvers are unavailable.
- Report both optimum value and decision variables.

## Example code

```matlab
obj = @(x) (x(1)-2)^2 + (x(2)+1)^2;
x0 = [0; 0];
x_hat = fminsearch(obj, x0);
```
