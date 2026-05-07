---
name: requirements-quality
description: "Convert product scope into functional requirements, nonfunctional requirements, measurable quality scenarios, acceptance criteria, and traceable requirement links. Use before architecture or implementation when FR/NFR lists, reliability, security, observability, performance, maintainability, compatibility, accessibility, data-safety, or artifacts `11-functional-requirements.md` through `13-quality-scenarios.md` are needed."
---

# Requirements Quality

## Role

Make the product promise testable. Turn intent into requirements that architecture, implementation, and QA can verify without mind-reading.

## Start By

- Collect the product scope, domain constraints, competitor implications, and user journeys.
- Mark each requirement as functional, nonfunctional, or quality scenario.
- Tie requirements to user value or system risk.
- Identify what must be measurable before implementation begins.

## Procedure

1. Write functional requirements as system behaviors with actors, triggers, and expected outcomes.
2. Write nonfunctional requirements as quality attributes with measurable targets or observable thresholds.
3. Use quality scenarios for reliability, performance, security, observability, maintainability, and data safety.
4. Connect each requirement to acceptance criteria and validation method.
5. Flag contradictions, missing owners, and requirements that are too vague to test.

## Output Artifacts

- Functional requirements
- Nonfunctional requirements
- Quality scenarios
- Acceptance criteria
- Traceability notes

## Quality Bar

- Every important requirement should be testable.
- Avoid words like fast, secure, scalable, and intuitive unless they are defined.
- Do not bury architecture decisions inside requirements without marking them.
- Keep requirements small enough to assign and validate.

## Handoff

Hand off requirements with IDs or stable names so architecture, tasks, QA, and docs can link back to them.

## References

- `references/quality-scenario-format.md`: Use this format for measurable quality scenarios.
