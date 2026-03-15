---
name: simulink-parameter-tuning
description: Use when tuning Simulink model parameters, controller gains, or block variables with scripted objectives, bounds, and repeatable validation scenarios.
---

# Simulink Parameter Tuning

## Purpose

Tune Simulink parameters in a controlled, scriptable way rather than ad hoc manual edits.

## When to use

- Gain tuning in Simulink models
- Scripted objective-based parameter adjustment
- Comparing tuned versus nominal parameter sets
- Preparing reproducible calibration workflows

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using tuning-specific toolboxes.

## Workflow

1. Define tunable parameters, bounds, and nominal values.
2. Create objective metrics from simulation outputs.
3. Use the simplest suitable tuning method.
4. Re-run the tuned model on at least one validation case.
5. Save tuned parameters separately from the base model.

## Always

- Keep tuning objectives measurable.
- Track both parameter values and resulting metrics.
- Confirm whether Simulink Design Optimization or related toolboxes are required.
- Do not overwrite baseline parameters without saving a nominal copy.
- Report where tuning helps and where it degrades behavior.

## Example code

```matlab
Kp = Simulink.Parameter(1.0);
Ki = Simulink.Parameter(0.5);
Kd = Simulink.Parameter(0.05);
```
