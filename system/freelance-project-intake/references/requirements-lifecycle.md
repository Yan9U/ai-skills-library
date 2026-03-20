# Requirements Lifecycle

Use this guide to maintain one living requirements document for each client project.

## File Path

Store the file at:

`client_docs/plans/<project-slug>-requirements.md`

Do not create a fresh requirements file every time the client changes something. Reuse the same file path for the same project.

## First Pass

Create the file as soon as the project can be identified, even if the brief is incomplete.

Initial sections:

1. Project Name
2. Current Status
3. Goal
4. Active Requirements
5. Open Questions
6. Acceptance Criteria
7. Out of Scope
8. Assumptions
9. Change Log

If the brief is still unclear, mark uncertain items explicitly instead of pretending they are confirmed.

## Requirement Reasonableness Check

Before syncing a new or changed client requirement into the active sections, check:

1. **Feasibility** - Can the requested outcome be achieved with the tools, data, access, and time available?
2. **Testability** - Can success be verified with a concrete demo, metric, or acceptance test?
3. **Consistency** - Does the new request conflict with already confirmed requirements, timeline, or delivery format?
4. **Scope proportionality** - Is the requested change proportionate to the current quote, timeline, and project stage?
5. **Dependency realism** - Does the change silently depend on unavailable APIs, hardware, credentials, or client actions?

If the answer is "no" on any major dimension, treat the requirement as not yet reasonable enough to confirm.

## Update Rule

On every later invocation for the same client project:

1. Open the existing requirements document first.
2. Compare the new client message against the active sections.
3. Evaluate whether the change is reasonable enough to confirm.
4. If reasonable, update active sections in place so they reflect the newest confirmed requirement set.
5. If not reasonable, leave the active sections unchanged and record the request as pending clarification or rejected in the change log or open questions.
6. Append a dated change-log entry summarizing what changed or why the request was not accepted as active scope.

Newest confirmed client instruction wins over older wording unless the user explicitly says the old requirement still stands.

## What Counts As A Requirement Change

Treat these as document updates:

- Added or removed features
- Changed priority
- Changed delivery format
- Changed platform, language, or environment
- Changed acceptance criteria
- Changed deadline or milestone expectation
- New data, files, credentials, or external dependencies
- Explicitly declared out-of-scope items

## Change Log Format

Each update should append a short block with:

- Date
- Source of change, for example "client follow-up in chat"
- Reasonableness verdict: reasonable, pending clarification, or not reasonable
- Added
- Changed
- Removed
- Impact on plan, quote, or risk

## Response Rule

When the client proposes a change:

- If reasonable: say it is reasonable, update the living requirements document, and give a brief work plan
- If not reasonable: explain why, do not overwrite the active requirements with it, and suggest a more realistic alternative, smaller phase, or clarification path

## Alignment Rule

The response shown to the user, the milestone plan, and the quote must all stay consistent with the living requirements document.

If the requirements document changes materially:

- Revise the plan if milestones are affected
- Revise the quote if scope or uncertainty changed
- Surface any conflicts or newly invalid assumptions
