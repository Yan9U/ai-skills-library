# Planning And Pricing

Use this file after the project is clear enough to scope.

## Default Language

Unless the user explicitly requests English, write milestone plans, timeline summaries, and quote drafts in Simplified Chinese for the client.

## Milestone Structure

Prefer milestone plans with 3 to 5 phases:

1. Discovery and validation
2. Prototype or core implementation
3. Integration and testing
4. Revisions and delivery
5. Optional deployment or handoff support

For each milestone, state:

- Objective
- Inputs required
- Main tasks
- Output or deliverable
- Estimated time
- Blocking dependencies

## Milestone Framing

Every milestone must also include an **Observable Outcome** field: one sentence stating what the client can see, test, or verify at that stage, not just what was built internally.

Additional rules:
- The first milestone should produce something the client can verify within 1 to 3 days of providing feedback. This de-risks early misalignment before significant effort is invested.
- Prefer vertical slices, meaning thin end-to-end functionality that the client can interact with, over horizontal technical phases such as "database layer complete".

Example of a vertical slice milestone: "Client can upload a CSV and see a cleaned preview in the web UI."
Example of a horizontal phase milestone to avoid: "Backend data-cleaning module complete."

## Time Estimation

Estimate a realistic range, not a single perfect number.

Suggested bands:

- Small: 6 to 15 hours
- Medium: 16 to 40 hours
- Large: 41 to 100 hours
- Very large: more than 100 hours

Then apply an uncertainty buffer:

- Low uncertainty: +10% to +15%
- Medium uncertainty: +20% to +30%
- High uncertainty: +35% to +60%

Use higher buffers when the client has vague requirements, poor sample data, unclear hardware, or likely revision churn.

## Student Pricing Model

Start from a reasonable market baseline, then apply a student discount.

### Baseline Hourly Bands

- Routine scripting or cleanup: USD 12 to 20 per hour
- Standard automation or analysis: USD 18 to 30 per hour
- Full-stack, complex integration, or specialized technical work: USD 25 to 45 per hour

If the client uses a different currency, quote in that currency when practical. Otherwise default to USD.

### Discount Rule

Apply a 20% to 35% discount from the baseline quote to reflect student status and lower reliability versus an experienced freelancer.

### Do Not Undercut Below These Floors

- Routine work floor: USD 8 to 12 per hour
- Specialized or urgent work floor: USD 12 to 18 per hour

Never discount below the point where support, debugging, and communication overhead make the work irrational.

## Quote Formats

Use one of these:

- Fixed price for well-scoped work
- Hourly range for uncertain work
- Paid discovery phase when the brief is incomplete

## Quote Output

Every quote should include:

- Recommended quote
- Pricing model
- Assumptions
- What is included
- What is not included
- Risk factors that may change the quote
