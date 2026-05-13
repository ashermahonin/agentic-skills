---
name: service-implementation
description: "Implement a specific service, module, feature slice, bug fix, migration step, or bounded-context task after requirements, architecture, contracts, file ownership, validation pack, and documentation expectations are clear. Use for coding work where the agent owns a defined path or component and must preserve surrounding behavior, tests, data safety, and project memory."
---

# Service Implementation

## Role

Do the actual code work without losing the system contract. Implement narrowly, respect existing patterns, and leave evidence that the change behaves correctly.

## Start By

- Read the assigned task, requirements, architecture notes, and write scope.
- Inspect nearby code before choosing patterns.
- Confirm tests or validation commands before editing.
- Check for dirty files and avoid overwriting unrelated user changes.

## Procedure

1. Make the smallest coherent code change that satisfies the task.
2. Use existing helpers, conventions, APIs, and test style before adding new abstractions.
3. Keep migrations, contracts, and backward compatibility explicit.
4. Update or add tests when behavior changes or risk justifies it.
5. Run the validation pack or report why it could not run.
6. Update docs or Obsidian notes when behavior, architecture, commands, or decisions change.

## Principal-Level Defaults

- Follow `../../routing/principal-operating-model.md` before moving from analysis to implementation.
- Use Context7 MCP for current library, framework, platform, API, CLI, and configuration documentation whenever the task depends on external technology behavior.
- Keep a decision trace: facts, assumptions, options considered, tradeoffs, selected path, validation evidence, and rollback or follow-up.
- Escalate irreversible, security-sensitive, data-migration, production, or cross-boundary choices before write-heavy work.

## Output Artifacts

- Changed files summary
- Behavior summary
- Tests and validation evidence
- Docs updated
- Risks or follow-ups

## Quality Bar

- Do not broaden scope silently.
- Do not rewrite working code just to make it prettier.
- Do not hide test failures.
- Prefer boring correctness over cleverness.

## Handoff

Hand off changed files, validation results, residual risk, and docs touched to QA or PR review.

## References

- `references/implementation-contract.md`: Use this as the implementation handoff contract.
