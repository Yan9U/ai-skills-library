---
name: pid-controller-design
description: Use when designing, tuning, or validating PID controllers in MATLAB for continuous or discrete systems, including saturation and anti-windup considerations.
---

# PID Controller Design

## Purpose

Design practical PID controllers in MATLAB with explicit tuning logic and closed-loop validation.

## When to use

- Classical PID tuning
- Setpoint tracking and disturbance rejection
- Continuous or discrete controller design
- Anti-windup and actuator saturation handling

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using `pid`, `pidtune`, or related toolbox APIs.

## Workflow

1. Define the plant, control objective, and constraints.
2. Decide on P, PI, PID, or filtered PID structure.
3. Tune gains with a method that matches the plant knowledge level.
4. Simulate step tracking, disturbance rejection, and saturation scenarios.
5. Report overshoot, settling time, steady-state error, and robustness notes.

## Always

- Specify sample time for digital controllers.
- Include actuator limits if they matter.
- Treat derivative action carefully in noisy systems.
- Add anti-windup when integral action can saturate.
- Validate against at least one non-nominal case.

## Example code

```matlab
C = pid(1.2, 0.8, 0.05);
T = feedback(C * G, 1);
step(T); grid on
```
