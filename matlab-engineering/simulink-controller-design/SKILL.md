---
name: simulink-controller-design
description: Use when building controller structures directly in Simulink, including PID blocks, transfer blocks, subsystems, and feedback interconnections.
---

# Simulink Controller Design

## Purpose

Design controller block structures in Simulink so the resulting model is explicit, tunable, and testable.

## When to use

- PID blocks in Simulink
- Controller subsystems
- Reference, plant, and feedback interconnections
- Controller architecture prototyping

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before adding toolbox-dependent controller blocks.

## Workflow

1. Define the controller architecture first.
2. Build source, summing, controller, plant, and sink blocks in that order.
3. Encapsulate repeatable logic into named subsystems.
4. Parameterize gains and sample times explicitly.
5. Simulate and inspect controller signals before finalizing.

## Always

- Keep signal names visible where it improves readability.
- Avoid hidden initialization assumptions.
- Expose tunable parameters at the top level when practical.
- Use subsystems to prevent diagram sprawl.
- Save the model after each major structural change.

## Example code

```matlab
add_block('simulink/Continuous/PID Controller', [mdl '/PID']);
set_param([mdl '/PID'], 'P', '1.0', 'I', '0.5', 'D', '0.05');
```
