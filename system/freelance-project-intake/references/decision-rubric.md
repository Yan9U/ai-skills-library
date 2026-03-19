# Decision Rubric

Use this rubric when deciding whether the project can be completed by the agent and supporting agents.

## Assumption Stress-Test

Before issuing any verdict, challenge the brief across these five categories. Surface each assumption explicitly in the intake summary; do not silently fill in gaps.

1. **Scope boundaries** - What is explicitly excluded? Are there related features the client might assume are included?
2. **Delivery format** - Is the output a file, an API, a deployed service, or documentation? Each has very different effort and access requirements.
3. **Quality / performance bar** - What does "good" mean numerically? For example: accuracy threshold, response time, or file size limit.
4. **Hidden dependencies** - Are there third-party APIs, data licenses, platform accounts, or external services required that the client has not mentioned?
5. **Revision expectations** - How many rounds of revision are expected, and over what calendar timeline?

Proceed to the feasibility verdict only after at least three concrete facts are established: deliverable, target environment, and one success criterion.

## Verdict Levels

### Agent-ready

Use this when:

- The deliverable is clear.
- Required data, files, APIs, or code access are available.
- The work can be done with normal software tools and without specialized physical hardware.
- Acceptance criteria are concrete and testable. Example of concrete: "accuracy > 90% on held-out test set, measured with provided script." Example of vague: "the model should work well." Vague criteria push the verdict toward Blocked.

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

#### Codebase Risk

Activates when the project requires extending an existing client codebase. Answer these four diagnostic questions before finalizing the verdict:

1. Is the code modular, or is it a monolith with tangled dependencies?
2. Does it have any tests or assertions that can catch regressions?
3. Is there inline documentation or a README explaining intent?
4. Is it version-controlled (git or equivalent)?

Risk mapping:
- All yes -> standard timeline; no adjustment needed
- Mixed (2 to 3 yes) -> add 20 to 30 percent time buffer; flag as `Agent-ready with user actions`
- Mostly no (0 to 1 yes) -> recommend a paid discovery phase to assess the codebase before quoting full scope; do not commit to a fixed price

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
