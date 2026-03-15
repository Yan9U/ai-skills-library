---
name: matlab-debugger
description: Use when debugging MATLAB errors, wrong results, NaN or Inf propagation, indexing problems, path issues, or toolbox-related failures in scripts and functions.
---

# MATLAB Debugger

## Purpose

Diagnose MATLAB failures quickly and fix the smallest correct scope.

## When to use

- Runtime errors
- Dimension mismatch and indexing bugs
- NaN, Inf, or unstable numerical behavior
- Wrong plots or unexpected outputs
- Path, package, or toolbox issues

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before reproducing failures.

## Workflow

1. Reproduce the failure with the smallest input that still breaks.
2. Classify the issue: syntax, runtime, logic, numerical, path, or toolbox.
3. Inspect sizes, classes, and intermediate values near the failure.
4. Patch the root cause instead of layering defensive workarounds.
5. Re-run the failing case and a nearby normal case.

## Always

- Keep the failing example until the fix is validated.
- Print or inspect `size`, `class`, `min`, `max`, and `nnz(isnan(...))` where useful.
- Check row-vector versus column-vector assumptions.
- Confirm whether the issue comes from missing toolboxes or bad paths.
- Run static checks again after the fix.

## Example code

```matlab
assert(isvector(x), 'x must be a vector');
disp(size(x));
disp(class(x));
disp(nnz(isnan(x)));
```
