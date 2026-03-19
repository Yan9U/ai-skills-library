# Output Format

Use this response structure unless the user asks for a different format.

## Language Policy

- Speak to the user in the user's language. Default to Simplified Chinese if the user is writing in Chinese.
- Write client-facing questionnaires, milestone plans, and quotes in Simplified Chinese unless the user requests another language.

## Intake Summary

- Restate the project in plain language.
- Mention the likely deliverable and the main risk.

## Execution Verdict

- State one verdict: `Agent-ready`, `Agent-ready with user actions`, `Blocked pending client information or resources`, or `Decline / no-bid`.
- State whether multi-agent work is useful.

## What Codex Can Do

- List the technical work Codex and supporting agents can handle.

## What You Must Do

- List concrete actions the user must take.

## What The Client Must Provide

- List missing files, data, credentials, constraints, or approvals.

## Client Questions

- If blocked, provide grouped client questions.
- Mention the DOCX path if a questionnaire was generated.

## Milestones And Timeline

- If the scope is clear enough, provide 3 to 5 milestones with time estimates.
- Each milestone must include an "Observable Outcome" field per the Milestone Framing rules in `references/planning-and-pricing.md`.

## Requirements Summary (optional)

Activate this only when: (a) verdict is `Agent-ready` or `Agent-ready with user actions`, and (b) the client has already provided enough information, typically on a second invocation after the questionnaire is returned. Do not produce this section on a first pass with a thin brief.

- **Goal** - One sentence stating the core deliverable
- **User Stories** - 2 to 5 items in "As a [actor], I need [X] so that [Y]" format
- **Acceptance Criteria** - Bullet list of testable assertions
- **Out of Scope** - Explicit list of what is not included

## Quote

- Provide a fixed-price range, hourly range, or discovery quote.
- State the pricing assumptions and the student discount logic.

## Assumptions

- List assumptions that could change the verdict, plan, or quote.
