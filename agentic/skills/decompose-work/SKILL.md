---
name: decompose-work
description: "Break approved product scope and architecture artifacts into epics, user stories, implementation tasks, dependency graph, critical path, ownership map, validation packs, merge order, and parallelization plan. Use after requirements and architecture are approved and before assigning implementation agents, opening parallel work, or writing artifacts `24-epics.md` through `29-agent-role-matrix.md`."
---

# Decompose Work

## Role

Make implementation boring in the best way. Convert a big plan into small, owned, sequenced tasks that can run without stepping on each other.

## Start By

- Confirm requirements and architecture are approved enough to decompose.
- List deliverables and affected modules.
- Identify dependencies, shared files, contracts, and migration order.
- Decide which tasks can run in parallel and which must stay serial.

## Procedure

1. Create epics for coherent slices of value or infrastructure.
2. Break epics into stories and tasks with clear done criteria.
3. Assign each task a write scope, interfaces touched, validation command, and expected docs update.
4. Build the dependency graph and critical path.
5. Define parallel lanes only when file ownership and contracts are disjoint.
6. Write merge order, conflict policy, and fallback if a lane blocks.

## Principal-Level Defaults

- Follow `../../routing/principal-operating-model.md` before moving from analysis to implementation.
- Use Context7 MCP for current library, framework, platform, API, CLI, and configuration documentation whenever the task depends on external technology behavior.
- Keep a decision trace: facts, assumptions, options considered, tradeoffs, selected path, validation evidence, and rollback or follow-up.
- Escalate irreversible, security-sensitive, data-migration, production, or cross-boundary choices before write-heavy work.

## Output Artifacts

- Epics
- Stories
- Tasks
- Dependency graph
- Parallelization plan
- Agent role matrix

## Quality Bar

- A task without validation is not ready.
- A parallel task without ownership boundaries is not parallel-ready.
- Do not split work by agent count; split by coherent boundaries.
- Keep merge order visible.

## Handoff

Hand off each implementation task with scope, files, contracts, validation, docs, dependencies, and merge order.

## References

- `references/parallelization-policy.md`: Use this before running multiple agents or parallel implementation lanes.
