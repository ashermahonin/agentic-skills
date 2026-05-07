# Obsidian Linking Rules

Markdown wikilinks are the graph source of truth. Mermaid diagrams are useful visuals, but Mermaid links do not count as Obsidian graph links.

## Required Link Families

Every project note should link to the relevant items from these families when applicable:

- Parent artifact or home note
- Requirements and quality scenarios
- ADRs or decision index
- Epics, stories, tasks, dependency graph, and parallelization plan
- Risks and rollback notes
- Services, owners, and language profiles

## Note Shape

- Keep one artifact per note.
- Keep file names stable and numbered when order matters.
- Use frontmatter for status, owner, service, language, and risk.
- Keep full deep context in RAG/Graphify when notes would become too large.

## Hygiene Checks

- No empty `[[]]` placeholders.
- No machine-specific absolute paths in tracked docs.
- No orphaned critical artifact.
- No diagram-only relationship.
