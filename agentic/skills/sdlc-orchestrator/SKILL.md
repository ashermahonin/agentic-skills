---
name: sdlc-orchestrator
description: "Orchestrate full software-development lifecycle work from first request to release readiness. Use when the user asks to build a product, improve an existing product, rebuild a messy system, coordinate several skills, choose between greenfield and migration work, or move a broad task through intake, research, requirements, architecture, decomposition, implementation, verification, and documentation gates."
---

# SDLC Orchestrator

## Role

Keep the whole effort coherent. Treat this skill as the traffic controller for the system: pick the entrypoint, sequence the skills, protect read-only phases, and make sure every handoff produces an artifact another agent can trust.

## Start By

- Restate the goal in one plain sentence.
- Classify the work as new product, existing-product improvement, narrow code change, review-only, or documentation sync.
- Name the first missing artifact that blocks safe progress.
- Choose the next skill from `agentic/routing/skills.json` and explain why.

## Procedure

1. Build the phase map before assigning work. Include discovery, requirements, architecture, decomposition, implementation, QA, and documentation only when each phase is actually needed.
2. Keep research, planning, code archaeology, architecture, decomposition, QA, and review read-only until the relevant gate is satisfied.
3. For existing products, route through `analyze-codebase` before target architecture or implementation.
4. For parallel work, require frozen interfaces, disjoint file ownership, dependency order, and merge order before any worker starts writing.
5. Create a visible checkpoint after each phase: what changed, what is known, what is still blocked, and which skill owns the next step.
6. Stop when the next action needs user approval, destructive access, production access, or a lasting architecture decision.

## Output Artifacts

- Entrypoint classification
- Ordered skill route
- Artifact checklist with owners
- Approval gates and stop conditions
- Current phase summary and next handoff

## Quality Bar

- No phase should exist only for ceremony; every phase must reduce risk or clarify execution.
- No implementation should start from a vague goal.
- No parallelism should start without ownership and merge order.
- No documentation sync should be postponed past the end of the task.

## Handoff

Hand off to the next skill with goal, constraints, artifacts already produced, artifacts still missing, and the exact gate that must pass next.

## References

- `references/phase-gates.md`: Use this when deciding whether a phase is ready to advance or must stay read-only.
