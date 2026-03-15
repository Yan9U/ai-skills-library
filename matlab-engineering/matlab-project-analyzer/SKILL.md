---
name: matlab-project-analyzer
description: Use when analyzing an existing MATLAB or Simulink project to identify entry points, dependencies, toolbox needs, data flow, file structure, and execution order.
---

# MATLAB Project Analyzer

## Purpose

Map an unfamiliar MATLAB project before editing or extending it.

## When to use

- First contact with a MATLAB codebase
- Reverse engineering project structure
- Locating entry points and startup scripts
- Detecting toolbox or Simulink dependencies
- Planning safe code changes

Read [../references/matlab-mcp-guardrails.md](../references/matlab-mcp-guardrails.md) first.

## Workflow

1. List `.m`, `.mlx`, `.mat`, and `.slx` assets.
2. Identify entry points such as `main.m`, `startup.m`, scripts, tests, and top-level models.
3. Detect toolbox-sensitive APIs before proposing changes.
4. Trace data inputs, outputs, and generated artifacts.
5. Summarize the run path, dependencies, and main risk areas.

## Always

- Distinguish scripts from functions and classes.
- Look for `addpath`, `genpath`, `load`, `readtable`, and `sim`.
- Note required working directories and relative paths.
- Call out generated files and side effects.
- Prefer a concise dependency map over a long file-by-file dump.

## Example code

```matlab
root = pwd;
disp(what(root));
files = dir(fullfile(root, '**', '*.m'));
disp({files.name}.');
```
