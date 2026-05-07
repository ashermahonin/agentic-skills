# Agentic SDLC Rules

## Purpose

This repository defines a clean agentic software-development workflow: permanent project rules, reusable skills, and an explicit phase graph.

## Repo Map

- `agentic/`: main system directory for skills, routing, docs, scripts, and Obsidian skeleton.
- `agentic/skills/`: skill folders created according to `skill-creator`.
- `agentic/routing/skills.json`: routing by entrypoint, phase, and permission.
- `.claude/rules/`: Claude-specific rule files.
- `agentic/obsidian/project-skeleton/`: Markdown artifacts for project memory.
- `install.sh`: global or project-local skill installer.
- `DESIGN.md`: documentation design contract for README diagrams and GitHub presentation.
- `agentic/scripts/validate.py`: structural validation.

## Default Workflow

1. Use `sdlc-orchestrator` for complex work.
2. Use `intake-coordinator` before research or coding.
3. Keep planning, research, architecture, decomposition, QA, and review read-only unless the user explicitly asks for edits.
4. Grant write scope only to `service-implementation` after requirements, architecture, ownership, and validation gates are clear.
5. Update documentation and graph links with code changes.

## Definition of Done

- Scope and assumptions are explicit.
- Affected artifacts are updated.
- Tests or validation commands are run or clearly reported as not run.
- Risks, rollback, and follow-up work are documented.
- Installer changes are checked with `./install.sh --dry-run` before real installation.
- GitHub-facing docs keep the root README English-first and put translations in `agentic/docs/`.

## Forbidden Defaults

- Do not jump from a broad request directly to code.
- Do not spawn multiple agents without disjoint ownership and merge order.
- Do not treat Mermaid links as Obsidian graph links.
- Do not write machine-specific absolute paths into tracked docs.
