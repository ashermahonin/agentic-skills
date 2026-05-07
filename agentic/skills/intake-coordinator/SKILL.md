---
name: intake-coordinator
description: "Clarify and scope incoming product or engineering requests before research, architecture, or coding starts. Use when the request is broad, emotionally urgent, ambiguous, risky, multi-phase, missing success criteria, missing constraints, missing non-goals, or likely to create rework if the agent starts implementation too early."
---

# Intake Coordinator

## Role

Turn an unclear request into a working brief without making the user repeat themselves. Preserve urgency, remove fog, and create just enough structure for the next skill to act confidently.

## Start By

- Extract the user goal, desired outcome, deadline pressure, and emotional priority.
- Separate facts from assumptions.
- Identify what can be decided now and what genuinely needs clarification.
- Ask only the smallest number of questions needed to unblock the next phase.

## Procedure

1. Write a one-paragraph brief in plain language.
2. List success criteria as observable outcomes, not slogans.
3. Mark constraints: time, budget, stack, security, data, deployment, design, and ownership.
4. Define non-goals so the task does not quietly expand.
5. Name the next skill and the artifact it should produce.
6. If the request is narrow and safe, hand off quickly instead of over-planning.

## Output Artifacts

- Request brief
- Assumptions and open questions
- Success criteria
- Constraints and non-goals
- Next recommended skill

## Quality Bar

- The brief should feel like the user was understood, not processed.
- Do not invent requirements to avoid asking a necessary question.
- Do not ask questions whose answer can be found in the repo or existing docs.
- Keep the next step concrete.

## Handoff

Hand off a concise brief plus the exact uncertainties the next skill must resolve.

## References

- `references/brief-template.md`: Use this template for `01-request-brief.md` and `02-clarifications.md`.
