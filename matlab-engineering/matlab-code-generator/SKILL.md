---
name: matlab-code-generator
description: Use when generating or refactoring MATLAB scripts, functions, classes, or numerical algorithms that should be validated through MATLAB MCP or MATLAB CLI.
---

# MATLAB Code Generator

## Purpose

Create clear, runnable MATLAB code from specifications, equations, pseudocode, or existing project patterns.

## When to use

- New MATLAB scripts or functions
- Numerical methods and data-processing utilities
- Refactoring script logic into reusable functions
- Adding comments, help text, and stable interfaces

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before execution-heavy work.

## Workflow

1. Infer whether the task needs a script, function, class, or package.
2. Define inputs, outputs, units, and edge-case behavior first.
3. Generate the smallest runnable file set.
4. Prefer vectorized operations and preallocation where it improves clarity or performance.
5. Run MATLAB static checks, then a minimal smoke test.

## Always

- Add a short help header for public functions.
- Keep function signatures stable and explicit.
- Avoid hidden dependencies on workspace variables.
- Use toolbox-specific functions only after confirming availability.
- Return data instead of only printing to the console.

## Example code

```matlab
function y = moving_average(x, window)
%MOVING_AVERAGE Compute a causal moving average.
arguments
    x (:,1) double
    window (1,1) double {mustBeInteger,mustBePositive}
end

k = ones(window, 1) / window;
y = filter(k, 1, x);
end
```
