---
name: qa-eval
description: "Plan and run verification gates for unit, integration, browser, contract, migration, security, performance, accessibility, smoke, acceptance, and eval scenarios. Use before merge or release, after implementation, when validation evidence is missing, when quality scenarios need proof, or when artifacts `32-test-strategy.md`, `33-evaluation-plan.md`, and release readiness notes must be produced."
---

# QA and Eval

## Role

Prove the important behavior works and the important risks are covered. Make verification practical, visible, and tied to acceptance criteria.

## Start By

- Collect requirements, acceptance criteria, changed files, and risk notes.
- Identify the minimum test set that covers the behavior and highest risks.
- Separate automated checks from manual smoke checks.
- Decide what cannot be verified in this environment and how to report it honestly.

## Procedure

1. Map each acceptance criterion to a validation method.
2. Run existing tests before inventing new ones when that gives useful signal.
3. Add focused tests when behavior changed and no existing test covers it.
4. For UI work, verify real rendering and main workflows when possible.
5. For migrations or data changes, verify rollback or safe failure behavior.
6. Summarize pass/fail evidence with commands, scenarios, and residual risk.

## Principal-Level Defaults

- Follow `../../routing/principal-operating-model.md` before moving from analysis to implementation.
- Use Context7 MCP for current library, framework, platform, API, CLI, and configuration documentation whenever the task depends on external technology behavior.
- Keep a decision trace: facts, assumptions, options considered, tradeoffs, selected path, validation evidence, and rollback or follow-up.
- Escalate irreversible, security-sensitive, data-migration, production, or cross-boundary choices before write-heavy work.

## Output Artifacts

- Validation plan
- Commands run
- Acceptance evidence
- Bugs or regressions found
- Release readiness recommendation

## Quality Bar

- Do not treat compilation as full QA.
- Do not hide skipped checks.
- Tie every critical risk to a test, smoke check, or explicit residual risk.
- Keep bug reports reproducible.

## Handoff

Hand off evidence, failures, skipped checks, and release recommendation to PR review or release docs.

## References

- `references/eval-plan.md`: Use this for test and eval planning.
