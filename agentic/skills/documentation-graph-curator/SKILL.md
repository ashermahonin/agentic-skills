---
name: documentation-graph-curator
description: "Maintain project documentation and Obsidian-first knowledge graph using Markdown notes, wikilinks, ADRs, artifact indexes, Mermaid diagrams as visual layer, change logs, and graph hygiene. Use when syncing docs after code changes, creating a project vault skeleton, updating project memory, linking requirements to architecture and tasks, cleaning stale notes, or making sure agents can navigate the project without confusion."
---

# Documentation Graph Curator

## Role

Keep the second brain useful instead of decorative. Make notes navigable, current, linked, and small enough for agents to use quickly.

## Start By

- Identify which project artifacts changed or should change.
- Check that Markdown wikilinks connect requirements, architecture, tasks, ADRs, risks, and services.
- Separate source-of-truth notes from visual diagrams.
- Find stale or orphaned notes that would confuse future agents.

## Procedure

1. Update the smallest set of notes that preserve project truth.
2. Use wikilinks for graph structure; use Mermaid only to visualize relationships already represented in notes.
3. Keep each note focused on one artifact or decision.
4. Record decisions as ADRs when they are expensive to reverse.
5. Update change log, risk register, and task links when work closes or shifts.
6. Avoid machine-specific absolute paths in tracked docs.

## Principal-Level Defaults

- Follow `../../routing/principal-operating-model.md` before moving from analysis to implementation.
- Use Context7 MCP for current library, framework, platform, API, CLI, and configuration documentation whenever the task depends on external technology behavior.
- Keep a decision trace: facts, assumptions, options considered, tradeoffs, selected path, validation evidence, and rollback or follow-up.
- Escalate irreversible, security-sensitive, data-migration, production, or cross-boundary choices before write-heavy work.

## Output Artifacts

- Updated project notes
- Wikilink graph hygiene summary
- ADR or decision updates
- Change log entry
- Stale note or missing artifact list

## Quality Bar

- A future agent should find the right next artifact in one or two clicks.
- Do not let diagrams become the only place a relationship exists.
- Do not store full RAG-scale memory in small orientation notes.
- Keep docs portable and project-relative.

## Handoff

Hand off updated notes, missing links, stale docs, and next maintenance actions.

## References

- `references/obsidian-linking.md`: Use this for Obsidian graph hygiene.
