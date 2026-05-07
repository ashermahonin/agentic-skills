---
name: user-journey-mapper
description: "Map user journeys, story maps, interaction flows, alternate paths, failure paths, release slices, and scenario-to-task links before decomposition. Use when a product workflow, UX flow, story map, persona path, acceptance scenario, or `09-user-story-map.md` and `10-user-journeys.md` artifact must be clarified before epics, stories, tasks, or parallel implementation are assigned."
---

# User Journey Mapper

## Role

Turn product intent and architecture constraints into concrete user journeys that can be decomposed safely. Keep the work practical: who acts, what triggers the flow, what happens next, what fails, and which release slice should carry the value first.

## Start By

- Identify the primary user, operator, or external actor.
- Collect product scope, requirements, domain findings, and architecture constraints.
- Name the main journey, alternate journeys, and failure journeys.
- Check whether `09-user-story-map.md` and `10-user-journeys.md` already exist and should be updated.

## Procedure

1. Build a story map using activities, steps, details, and release slices.
2. Write user journeys with trigger, main flow, alternate flow, failure flow, and expected outcome.
3. Connect each journey to requirements, quality scenarios, risks, and architecture constraints.
4. Mark unclear interactions that need user clarification before decomposition.
5. Identify which journeys are MVP, later phase, or explicitly out of scope.
6. Hand off only journeys that are concrete enough to become epics, stories, tasks, and validation scenarios.

## Output Artifacts

- User story map
- User journey list
- Alternate and failure flow notes
- Release slicing notes
- Journey-to-requirement links
- Decomposition handoff notes

## Quality Bar

- Do not describe generic personas without a concrete action path.
- Do not create tasks until the journey has trigger, outcome, and acceptance signal.
- Keep failure paths visible, especially permissions, empty states, integration failures, and recovery.
- Link journeys to requirements and risks so Obsidian Graph remains useful.

## Handoff

Hand off journey IDs, release slices, acceptance signals, risks, and unresolved interaction questions to `decompose-work`.

## References

- `references/story-map-format.md`: Use this when writing story maps and user journeys.
