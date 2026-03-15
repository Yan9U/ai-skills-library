# Decision Rubric

Use this rubric when deciding whether the project can be completed by Codex and supporting agents.

## Verdict Levels

### Agent-ready

Use this when:

- The deliverable is clear.
- Required data, files, APIs, or code access are available.
- The work can be done with normal software tools and without specialized physical hardware.
- Acceptance criteria are specific enough to validate.

Typical examples:

- Python automation scripts
- Data cleaning and analysis with provided files
- Small web features in an existing codebase
- MATLAB or Java assignments with complete specifications

### Agent-ready with user actions

Use this when Codex can do the core technical work, but the user must complete external steps.

Common user actions:

- Obtain client credentials, API keys, datasets, sample files, or legal approvals
- Run software on a target machine, device, or intranet environment
- Purchase hosting, domains, licenses, or cloud credits
- Confirm permission to scrape, automate, or process client data
- Test on physical hardware the agent cannot access

### Blocked pending client information or resources

Use this when the project cannot be scoped responsibly yet.

Common blockers:

- Missing input data, sample files, screenshots, or expected outputs
- Unclear deliverables or success criteria
- Unknown runtime environment or deployment target
- Unknown language, version, or toolbox requirements
- Missing hardware, device, or sensor details
- No deadline, budget, or revision expectation

### Decline / no-bid

Use this when the job is too risky, unethical, impossible to validate, or outside a realistic student-freelancer scope.

Common decline reasons:

- Safety-critical or regulated deliverables without proper supervision
- Fraud, cheating, account abuse, or terms-of-service violations
- Unrealistic deadline versus scope
- Production obligations that require around-the-clock operations
- Confidential systems where the client cannot share enough information to work safely

## Multi-Agent Trigger Rules

Consider multiple agents only when at least two of these are true:

- There are distinct research and implementation-planning tracks.
- Separate subsystems can be analyzed independently.
- The task contains both technical work and packaging work, such as code plus documentation plus quote drafting.
- Parallel review materially reduces uncertainty.

Avoid multi-agent work when:

- The task is blocked on missing client information.
- The problem is small enough for one pass.
- The deliverable depends on a single tightly coupled decision path.

## Missing-Input Checklist

Before committing to a quote or plan, verify these areas:

- Business goal and final deliverable
- Input data, sample files, or APIs
- Required tools, languages, libraries, or versions
- Runtime environment and operating system
- Hardware, device, or sensor requirements
- Deployment target, if any
- Acceptance criteria and test cases
- Deadline, revision count, and communication expectations
- Legal, privacy, or compliance constraints
