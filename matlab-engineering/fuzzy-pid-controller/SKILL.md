---
name: fuzzy-pid-controller
description: Use when building MATLAB fuzzy PID controllers, rule bases, or gain-scheduling logic with Fuzzy Logic Toolbox and validating them against standard PID baselines.
---

# Fuzzy PID Controller

## Purpose

Create fuzzy PID or fuzzy gain-scheduled controller logic in MATLAB for nonlinear or heuristic control problems.

## When to use

- Nonlinear plants that are poorly served by fixed PID gains
- Rule-based gain adaptation
- Fuzzy inference around error and error derivative
- Comparing fuzzy PID against baseline PID

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using Fuzzy Logic Toolbox APIs.

## Workflow

1. Confirm Fuzzy Logic Toolbox availability.
2. Define controller inputs such as error and error rate.
3. Choose membership functions and output variables deliberately.
4. Build a compact rule base before expanding complexity.
5. Simulate against a plain PID baseline and summarize tradeoffs.

## Always

- Keep membership ranges tied to physical operating bounds.
- Use interpretable rule names and comments.
- Avoid oversized rule bases without evidence they help.
- State what is fuzzy: gains, control output, or scheduling logic.
- Report where fuzzy control improves and where it does not.

## Example code

```matlab
fis = mamfis('Name', 'fuzzy_pid');
fis = addInput(fis, [-1 1], 'Name', 'e');
fis = addInput(fis, [-1 1], 'Name', 'de');
fis = addOutput(fis, [-1 1], 'Name', 'u');
```
