---
name: simulink-batch-simulation
description: Use when running many Simulink simulations programmatically with parameter sweeps, scenario grids, SimulationInput objects, or parallel batch execution.
---

# Simulink Batch Simulation

## Purpose

Execute many Simulink runs reliably with structured inputs, saved outputs, and reproducible experiment metadata.

## When to use

- Scenario sweeps
- Parameter-grid studies
- Repeated Monte Carlo simulations in Simulink
- Batch export of simulation outputs

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before saving run artifacts.

## Workflow

1. Define the model and the varying parameters.
2. Create `Simulink.SimulationInput` objects for each run.
3. Run with `sim`, `parsim`, or a controlled loop.
4. Collect outputs into tables or structs with run identifiers.
5. Export both run-level outputs and aggregated summaries.

## Always

- Attach a run ID to every simulation.
- Keep nominal and variant scenarios easy to separate.
- Check whether Parallel Computing Toolbox is available before using `parsim`.
- Save enough metadata to reproduce any interesting run.
- Fail fast on model compilation errors.

## Example code

```matlab
in(1) = Simulink.SimulationInput('my_model');
in(1) = in(1).setVariable('Kp', 1.0);
out = sim(in);
```
