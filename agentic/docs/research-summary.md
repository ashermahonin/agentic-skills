# Research Note

<p>
  <a href="#русский">Русский</a>
  |
  <a href="#english">English</a>
</p>

## Русский

Эта заметка оставлена только как внутренний контекст для структуры репозитория. Основная документация специально сфокусирована на установке, маршрутах и навыках.

Короткая модель:

1. **Постоянный контекст**: `AGENTS.md`, `CLAUDE.md`, path-scoped правила и проектные ограничения.
2. **Навыки по требованию**: отдельные skills для повторяемых процедур, чтобы не раздувать always-on prompt.
3. **Явный граф оркестрации**: маршруты, checkpoints, approval gates, traceability и синхронизация документации.

Workflow должен быть artifact-driven, а не role-chat-driven. Сложная работа начинается с intake, discovery, requirements, architecture, user journeys и decomposition. Только после этого включаются implementation, verification и docs sync.

Для существующих продуктов первым шагом всегда идёт read-only code archaeology: current state, codebase map, hotspots, current architecture, target architecture и migration plan.

Obsidian является проектной памятью. Markdown notes и wikilinks: источник графа. Mermaid diagrams нужны для визуализации, но не заменяют обычные Obsidian links.

## English

This note is kept only as internal context for the repository structure. The main documentation intentionally focuses on installation, routing, and skills.

Short model:

1. **Permanent context**: `AGENTS.md`, `CLAUDE.md`, path-scoped rules, and project constraints.
2. **On-demand skills**: dedicated skills for repeatable procedures, instead of bloating the always-on prompt.
3. **Explicit orchestration graph**: routes, checkpoints, approval gates, traceability, and documentation sync.

The workflow should be artifact-driven, not role-chat-driven. Complex work starts with intake, discovery, requirements, architecture, user journeys, and decomposition. Implementation, verification, and docs sync come after those gates are clear.

For existing products, the first step is always read-only code archaeology: current state, codebase map, hotspots, current architecture, target architecture, and migration plan.

Obsidian is the project memory. Markdown notes and wikilinks are the graph source of truth. Mermaid diagrams are for visualization and do not replace normal Obsidian links.
