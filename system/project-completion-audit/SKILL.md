---
name: project-completion-audit
description: Audit whether a project is actually complete after an AI agent believes the work is finished. Reconstruct the full requirement set, list completed work, map each requirement to the relevant code and files, summarize how the implementation satisfies the requirement, capture validation evidence, and identify remaining gaps or risks so a second AI agent can independently verify completion.
---

# Project Completion Audit

Use this skill at the end of a project when the agent needs to produce a rigorous handoff document for an independent completion check.

## Default Stance

- Treat completion claims as untrusted until tied to concrete artifacts.
- Separate confirmed facts from inferred requirements.
- Prefer traceability over narrative. Every important claim should point to code, files, tests, or explicit user requirements.
- Follow the user's conversation language. If the user writes in Chinese, answer in Chinese.
- Write the audit file in Simplified Chinese unless the user explicitly requests another language.

## Workflow

1. Gather the source of truth.
   Inspect the user request, prior requirement documents, relevant project files, test commands, and any delivery notes.
   If a requirement is not explicitly stated anywhere, mark it as `Inferred` and explain the inference source.
2. Reconstruct the requirement baseline.
   Build a complete requirement list, including functional requirements, output or UI expectations, data or integration expectations, operational constraints, and requested deliverables.
   Assign each requirement one status only: `Implemented`, `Partially implemented`, `Missing`, or `Cannot verify`.
3. Inventory completed work.
   Summarize what was built, changed, configured, fixed, or documented.
   Group related work into user-facing capabilities instead of a raw file dump.
4. Create requirement-to-code traceability.
   For every requirement, cite the main implementation files and the relevant commands, tests, or observable outputs.
   Explain briefly how the code satisfies the requirement. If the linkage is weak, say so directly.
5. Capture verification evidence.
   Record which tests, manual checks, builds, or runtime validations were performed.
   If verification was not run, state that clearly and classify the affected requirements as `Cannot verify` unless other strong evidence exists.
6. Identify gaps and residual risk.
   List missing requirements, partial implementations, unverified paths, environment assumptions, and follow-up actions needed for a true completion claim.
7. Save the audit artifact.
   Write the final report to `client_docs/audits/<project-slug>-completion-audit.md`.
   Start from `assets/completion-audit-template.md` and fill it with project-specific content.

## Required Output Structure

The audit report must include these sections in this order:

1. `Project Summary`
   Include project name, audit date, auditor, overall verdict, and the evidence base used.
2. `Requirement Checklist`
   One row per requirement with: ID, requirement, source (`Explicit` or `Inferred`), status, evidence, and notes.
3. `Completed Work`
   Describe the delivered capabilities and key implementation work already present in the codebase.
4. `Implementation Mapping`
   For each requirement, explain how the code implements it and cite the main files.
5. `Validation Evidence`
   List tests, builds, commands, screenshots, or manual checks that support the completion claim.
6. `Gaps And Risks`
   List anything missing, partial, unverified, environment-dependent, or likely to fail in handoff.
7. `Handoff Verdict`
   End with exactly one verdict:
   - `Ready for independent completion check`
   - `Substantially complete but needs clarification`
   - `Not complete`

## Writing Rules

- Use stable requirement IDs such as `R1`, `R2`, `R3`.
- Do not hide uncertainty. Mark inferred or unverified items explicitly.
- Prefer repository paths over vague descriptions.
- Do not claim a requirement is complete without naming the implementing files or evidence.
- If the project has no usable requirement source, say that the audit is reconstruction-based and lower confidence accordingly.

## File Placement

- Save audit reports under `client_docs/audits/`.
- If a project already has an earlier audit file, update it in place unless the user asks for separate versions.

## Resources

- `assets/completion-audit-template.md`: Default Chinese report skeleton for the final audit handoff

## Example Triggers

- "项目做完后，帮我出一份完成度审查文档给另一个 agent 复核。"
- "Use $project-completion-audit to generate a requirements-to-code completion report."
- "I think this feature is done. Produce a full checklist and traceability report for a second AI review."
