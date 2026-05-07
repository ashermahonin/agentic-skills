# Phase Gates

Use these gates to stop broad work from sliding straight into code. A gate is passed only when the artifact is concrete enough for a different agent to continue without guessing.

## Intake Gate

- Goal is stated in one sentence.
- User, customer, or operator is named.
- Success criteria are measurable or observable.
- Constraints, non-goals, and approval points are visible.

## Discovery Gate

- Domain assumptions are separated from facts.
- Competitors or alternatives are mapped when product direction matters.
- Risks are written into `07-risk-register.md`.

## Architecture Gate

- System boundary, data model, APIs, runtime flows, and deployment concerns are explicit enough to review.
- ADRs exist for decisions that will be expensive to reverse.
- Existing products include current-state evidence, not only target-state intent.

## Decomposition Gate

- Tasks have owners, file scope, dependencies, and validation expectations.
- Parallel work has interface freeze points and merge order.

## Release Gate

- Acceptance criteria are checked.
- Tests, smoke checks, or evals have run, or the reason they did not run is reported.
- Documentation and Obsidian graph links are updated.
