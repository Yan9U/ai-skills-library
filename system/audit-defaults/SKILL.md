---
name: audit-defaults
description: Use when you need to surface all hardcoded assumptions and default values in a project that a customer or end-user may need to change to match their real scenario. Produces a structured "customer-facing defaults" table. Trigger phrases: "list defaults", "what variables should the customer know about", "surface assumptions", "audit parameters", "what does the customer need to change".
---

# Audit Defaults — Customer-Facing Parameter Review

## Purpose

Read the project source and produce a structured list of every hardcoded value, assumed constant, or default setting that influences results. The output is intended to be shared with a customer or end-user so they know what to adjust before running the code.

## When to use

- Before delivering a project to a client, to proactively document what was assumed
- After a client says "the output is not what I expected"
- When onboarding a new user to an existing codebase
- Any time magic numbers or domain constants appear without explanation

## Workflow

1. **Discover entry points** — find the main scripts, config files, or parameter-building functions (e.g. `build_params()`, `config.m`, `settings.py`, `constants.h`).
2. **Read all source files** that define or use hardcoded values.
3. **Categorize each value** into one of three tiers:

   | Tier | Label | Meaning |
   |------|-------|---------|
   | 1 | **Customer must review** | Domain/physical constants the customer almost certainly knows better than us (e.g. laser power, material properties, financial parameters) |
   | 2 | **Customer may want to adjust** | Simulation or algorithm settings with sensible defaults but clear impact on output (e.g. time window, step size, tolerance) |
   | 3 | **Developer internal** | Numerical settings that rarely need changing unless there is a precision problem (e.g. min step size, buffer capacity) |

4. **For each Tier 1 and Tier 2 value**, record:
   - Variable name and file location (file:line)
   - Current default value and unit
   - Plain-language description of what it represents
   - Effect of increasing or decreasing it on the output
   - Any known constraints or valid ranges

5. **Output the result** as a Markdown table (Tier 1 first, then Tier 2), followed by a short prose paragraph summarising the most impactful assumptions.

6. Optionally, if the project is MATLAB, also note which values are in `build_params()` vs. `sim_options` vs. top-level scripts, since those have different change-complexity for the customer.

## Output format

```
## Customer-Facing Parameter Audit

### Tier 1 — Must Review Before Running

| Parameter | File:Line | Default | Unit | What It Is | Effect of Change |
|-----------|-----------|---------|------|------------|-----------------|
| ...       | ...       | ...     | ...  | ...        | ...             |

### Tier 2 — May Want to Adjust

| Parameter | File:Line | Default | Unit | What It Is | Effect of Change |
|-----------|-----------|---------|------|------------|-----------------|
| ...       | ...       | ...     | ...  | ...        | ...             |

### Summary

[2–4 sentences: which parameters matter most, what the customer should confirm first]
```

## Rules

- Do not list variables that are derived from other variables (e.g. `epsilon_l = sqrt(2*P_l/...)`) — only list the root inputs.
- If the project has a config file or struct that aggregates parameters, list them from there rather than from every call site.
- Always include physical units. If units are missing from the code, infer from context or flag as "unit unclear".
- Keep descriptions non-technical. Write as if explaining to a domain expert who is not a programmer.
- Client-facing output should be in Simplified Chinese unless the user specifies otherwise.
