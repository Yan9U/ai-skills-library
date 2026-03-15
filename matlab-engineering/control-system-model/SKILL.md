---
name: control-system-model
description: Use when building or analyzing MATLAB control-system models such as transfer functions, state-space systems, linearized plants, and input-output models.
---

# Control System Model

## Purpose

Represent dynamic systems in MATLAB so they can be analyzed, simulated, or controlled.

## When to use

- Transfer-function modeling
- State-space modeling
- Linear time-invariant plant definition
- Input-output naming and time-base setup
- Preparing plants for controller design

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using Control System Toolbox APIs.

## Workflow

1. Define states, inputs, outputs, units, and operating assumptions.
2. Choose transfer-function, state-space, or discrete-time form.
3. Name channels and specify sample time if discrete.
4. Validate poles, zeros, stability, and basic responses.
5. Save the model in a reusable variable or helper function.

## Always

- State linearization assumptions clearly.
- Keep continuous-time and discrete-time models separate.
- Check units and sign conventions.
- Confirm toolbox availability for `tf`, `ss`, `zpk`, or `c2d`.
- Provide a fallback manual model representation if the toolbox is missing.

## Example code

```matlab
s = tf('s');
G = 5 / (s^2 + 2*s + 5);
step(G); grid on
```
