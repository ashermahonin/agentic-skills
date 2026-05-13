# Claude Code Routing

@AGENTS.md

## Force Plan Mode

Use plan-first behavior for broad product work, architecture changes, cross-service changes, migrations, unclear scope, or destructive operations.

## Skills

Load skills from `agentic/skills/`. Use `agentic/routing/skills.json` to pick the entrypoint and next skill.

## Context7 MCP

Use Context7 MCP automatically for library/API documentation, code generation, setup, configuration, CLI, platform, or framework questions. If Context7 is unavailable, say so and treat freshness as a risk.

## Principal Bar

Before implementation, apply `agentic/routing/principal-operating-model.md`: evidence before confidence, decision trace, risk budget, validation ladder, rollback, and handoff.

## Rules

- Architecture work: `.claude/rules/architecture.md`
- Testing and eval: `.claude/rules/testing.md`
- Security-sensitive work: `.claude/rules/security.md`
- Performance-sensitive work: `.claude/rules/performance.md`

## Output

For implementation work, report changed files, validation, risks, and docs updated. For planning work, report artifacts produced and gates still blocking execution.
