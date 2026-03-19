---
name: freelance-project-intake
description: Assess new freelance client requests for a non-technical student, decide whether Codex can complete the work, determine whether multi-agent execution would help, identify missing client inputs, generate a client questionnaire DOCX when requirements are incomplete, draft milestones and time estimates, and propose a student-discount quote. Use when the user describes a new paid project, outsourcing request, coding task, automation job, MATLAB/Java/Python assignment, website build, data task, or any freelance brief that must be evaluated before accepting, scoping, or pricing.
---

# Freelance Project Intake

Use this skill to turn an unclear client brief into an execution decision, a requirements follow-up package, a realistic plan, and a quote.

## Default Stance

- Assume the user is non-technical and may not know how to execute the project.
- Separate four things clearly: what the agent can do, what additional agents can do, what the user must do, and what the client must provide.
- Prefer conservative scoping over optimistic promises.
- Write internal structure and reusable metadata in English.
- Write client-facing documents, questionnaires, milestone plans, and quote drafts in Simplified Chinese unless the user explicitly requests another language.
- Follow the user's conversation language. If the user writes in Chinese, answer in Chinese.

## Workflow

1. Restate AND interrogate the project.
   Restate the likely deliverable, domain, hidden risks, deadline pressure, and assumptions. Then immediately stress-test 3 to 5 assumptions the agent made that the brief did not state explicitly. Use the "Assumption Stress-Test" categories in `references/decision-rubric.md` as a checklist.
   If in an interactive session with the user, pause for confirmation before advancing to the verdict. Do not proceed to a feasibility verdict until at least three concrete facts are established: deliverable, target environment, and one success criterion.
2. Decide execution feasibility.
   Read `references/decision-rubric.md`. If the project involves extending an existing client codebase, apply the "Codebase Risk" subsection as an additional risk factor before issuing the verdict.
3. Produce one verdict:
   - `Agent-ready`
   - `Agent-ready with user actions`
   - `Blocked pending client information or resources`
   - `Decline / no-bid`
4. Decide whether multi-agent work is justified.
   Use parallel agents only when there are cleanly separable workstreams, such as implementation research vs deployment research, data validation vs planning, or frontend vs backend scoping.
5. Identify missing inputs.
   If the brief is incomplete, read `references/questionnaire-guide.md`, build grouped client questions, and save a DOCX questionnaire.
6. Generate the questionnaire DOCX when needed.
   Start from `assets/questionnaire_input_template.json`, fill it with project-specific details, then run:

   ```bash
   python <installed-skill-dir>/scripts/generate_requirements_docx.py \
     --input <path-to-json> \
     --output client_docs/questionnaires/<project-slug>-requirements-questionnaire.docx
   ```
   Use the installed skill directory for the current agent environment, for example `~/.codex/skills/freelance-project-intake` or `~/.claude/skills/freelance-project-intake`.

7. If the scope is clear enough, read `references/planning-and-pricing.md` and produce milestones, time estimates, dependencies, risk notes, and a discounted quote. Each milestone must include an "Observable Outcome" field per the Milestone Framing rules in that file.
8. Produce a Requirements Summary (optional).
   Activate this only when: (a) verdict is `Agent-ready` or `Agent-ready with user actions`, and (b) the client has already provided enough information, typically on a second invocation after the questionnaire is returned. Do not produce this section on a first pass with a thin brief.
   See `references/output-format.md` for the Requirements Summary structure.
9. Follow `references/output-format.md` so every intake assessment is structured the same way.

## Multi-Agent Guidance

- Use additional agents for medium or large projects with at least two independent analysis tracks.
- Prefer `explorer` agents for bounded codebase or environment questions.
- Prefer `worker` agents only when there is concrete production work that can be split by ownership without overlapping write scopes.
- Do not use extra agents for very small jobs, tightly coupled decisions, or cases blocked on missing client information.
- When you use multiple agents, explain the split in one sentence per agent.

## File Placement

- Save client questionnaires under `client_docs/questionnaires/`.
- Save planning files under `client_docs/plans/`.
- Save quote drafts under `client_docs/quotes/`.
- Save actual implementation work under `projects/`.

## Pricing Guardrails

- Quote below a standard freelancer rate, but do not undercut so far that the project becomes irrational.
- Always state the assumptions behind the quote.
- If the scope is still unclear, recommend a small paid discovery phase instead of a full fixed-price commitment.
- Mention risks that may trigger a re-quote, such as weak sample data, hardware access problems, or hidden integration complexity.

## Resources

- `references/decision-rubric.md`: Feasibility rubric and multi-agent decision rules
- `references/questionnaire-guide.md`: How to ask clients for missing information
- `references/planning-and-pricing.md`: Milestone, time, and pricing guidance
- `references/output-format.md`: Response structure
- `assets/questionnaire_input_template.json`: Starter JSON for questionnaire generation
- `scripts/generate_requirements_docx.py`: Build a DOCX questionnaire from JSON

## Example Triggers

- "A client wants a Python scraper and Excel report. Can Codex handle it and what should I ask first?"
- "Someone sent me a MATLAB image-processing brief. Please judge if this can be done and quote it."
- "I received a Java desktop app request. Figure out missing requirements, prepare client questions, and estimate time."
