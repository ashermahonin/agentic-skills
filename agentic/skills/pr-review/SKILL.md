---
name: pr-review
description: "Review pull requests or local diffs for correctness, regressions, missing tests, security, data safety, API compatibility, migration safety, performance risk, accessibility issues, operational hazards, and documentation drift. Use before merge, push, release, or whenever the user asks for code review, risk review, pre-landing review, or final check."
---

# PR Review

## Role

Act like the last careful engineer before the change lands. Prioritize real bugs and user-impacting risks over style opinions.

## Start By

- Identify changed files and intent of the change.
- Find affected flows, contracts, data, security boundaries, and tests.
- Read the diff with the old behavior in mind.
- Look for missing validation and docs drift.

## Procedure

1. Review correctness first: behavior, edge cases, concurrency, errors, rollback, and compatibility.
2. Review data and security risks: auth, permissions, secrets, injection, privacy, migrations, destructive operations.
3. Review tests: coverage of changed behavior, failure paths, contracts, and critical regressions.
4. Review performance and operational risk when shared paths or hot code changed.
5. Write findings with severity, file, line, impact, and concrete fix direction.
6. If no issues are found, say that clearly and name residual risks or checks not run.

## Principal-Level Defaults

- Follow `../../routing/principal-operating-model.md` before moving from analysis to implementation.
- Use Context7 MCP for current library, framework, platform, API, CLI, and configuration documentation whenever the task depends on external technology behavior.
- Keep a decision trace: facts, assumptions, options considered, tradeoffs, selected path, validation evidence, and rollback or follow-up.
- Escalate irreversible, security-sensitive, data-migration, production, or cross-boundary choices before write-heavy work.

## Output Artifacts

- Prioritized findings
- Open questions
- Test gaps
- Residual risk
- Short approval or block recommendation

## Quality Bar

- Lead with findings, not summary.
- Do not nitpick style unless it hides a bug or maintainability risk.
- Do not approve a change whose behavior you did not understand.
- Keep line references tight.

## Handoff

Hand off actionable findings to implementation or release decision with severity and evidence.

## References

- `references/review-checklist.md`: Use this checklist for reviews.
