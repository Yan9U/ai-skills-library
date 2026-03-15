---
name: control-system-simulation
description: Use when running MATLAB closed-loop control simulations, disturbance studies, time-domain response checks, or controller comparisons with logged performance metrics.
---

# Control System Simulation

## Purpose

Run control-oriented simulations in MATLAB and extract the metrics needed for engineering decisions.

## When to use

- Closed-loop response simulation
- Disturbance and noise rejection studies
- Controller comparison experiments
- Time-domain metrics and tracking error analysis

Read [../references/matlab-output-conventions.md](../references/matlab-output-conventions.md) before exporting results.

## Workflow

1. Define plant, controller, reference, disturbance, and noise signals.
2. Choose `step`, `lsim`, `ode45`, or another solver based on the model form.
3. Log outputs, states, control effort, and constraints.
4. Compute comparison metrics after the run.
5. Save both raw trajectories and summary tables.

## Always

- Keep simulation time and sample time explicit.
- Compare at least one baseline case.
- Log control effort when actuator limits matter.
- Use the same metrics across controller variants.
- Save reproducible outputs for later plotting.

## Example code

```matlab
t = 0:0.01:10;
u = ones(size(t));
y = lsim(T, u, t);
plot(t, y); grid on
```
