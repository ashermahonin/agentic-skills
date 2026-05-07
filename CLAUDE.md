# Claude Code Routing

@AGENTS.md

## Force Plan Mode

Use plan-first behavior for broad product work, architecture changes, cross-service changes, migrations, unclear scope, or destructive operations.

## Skills

Load skills from `agentic/skills/`. Use `agentic/routing/skills.json` to pick the entrypoint and next skill.

## Rules

- Architecture work: `.claude/rules/architecture.md`
- Testing and eval: `.claude/rules/testing.md`
- Security-sensitive work: `.claude/rules/security.md`
- Performance-sensitive work: `.claude/rules/performance.md`

## Output

For implementation work, report changed files, validation, risks, and docs updated. For planning work, report artifacts produced and gates still blocking execution.
