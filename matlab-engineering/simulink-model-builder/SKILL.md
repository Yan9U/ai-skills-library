---
name: simulink-model-builder
description: Use when creating Simulink models programmatically with MATLAB APIs such as new_system, add_block, add_line, set_param, save_system, and open_system.
---

# Simulink Model Builder

## Purpose

Create Simulink models programmatically so model generation is reproducible and patchable.

## When to use

- Building system models
- Control-system block diagrams
- Power, signal, or mechanical model scaffolding
- Reproducible model generation from code

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) before using Simulink APIs.

## Workflow

1. Confirm that Simulink is installed.
2. Create the model with `new_system`.
3. Add blocks with clear names and parameter values.
4. Connect them using `add_line`.
5. Open and save the finished model.

## Always

- Call `open_system` before final review.
- Name blocks clearly and consistently.
- Set key parameters explicitly with `set_param`.
- Save with `save_system`.
- Keep geometry readable so the generated model is inspectable.

## Example code

```matlab
mdl = 'demo_model';
new_system(mdl);
open_system(mdl);
add_block('simulink/Sources/Step', [mdl '/Step']);
add_block('simulink/Sinks/Scope', [mdl '/Scope']);
add_line(mdl, 'Step/1', 'Scope/1');
save_system(mdl);
```
