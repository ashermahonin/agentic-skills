# Agentic Skills

<p align="center">
  <strong>Obsidian-first skill routing for Codex, Claude Code, and local agent workflows.</strong>
</p>

<p align="center">
  <a href="agentic/docs/README.ru.md">Русский</a>
  |
  <a href="agentic/docs/README.es.md">Español</a>
  |
  <a href="agentic/docs/README.zh.md">中文</a>
  |
  <a href="agentic/docs/README.md">Docs</a>
  |
  <a href="agentic/routing/README.md">Routing guide</a>
</p>

<p align="center">
  ✨ plan-first · 🧭 explicit routing · 🧩 reusable skills · ✅ validation gates
</p>

---

## Overview

Agentic Skills is a professional SDLC skill pack for AI coding agents. It gives Codex, Claude Code, and local agents a structured route from the first request to a verified change: intake, discovery, requirements, architecture, decomposition, implementation, QA, review, and project-memory sync.

The repository keeps the root clean and places the working system under one main directory: [`agentic/`](agentic/).

## Routing Diagram

![Agentic Skills routing flow](agentic/docs/assets/routing-flow.svg)

## Quick Start

```bash
git clone <repo-url>
cd agentic-skills
./install.sh --global
python3 agentic/scripts/validate.py
```

Install into one local project instead of globally:

```bash
./install.sh --local /path/to/project --target all
```

Preview the installation without changing files:

```bash
./install.sh --global --dry-run
```

## Installer Flags

| Flag | Meaning |
| --- | --- |
| `--global` | Install into user-level skill folders: `~/.codex/skills`, `~/.claude/skills`, `~/.agents/skills`. |
| `--local PATH` | Install into one project: `PATH/.codex/skills`, `PATH/.claude/skills`, `PATH/.agents/skills`. |
| `--target codex` | Install only for Codex. |
| `--target claude` | Install only for Claude Code. |
| `--target agents` | Install only into `.agents/skills`. |
| `--target all` | Install into all supported targets. Default. |
| `--copy` | Copy skill folders instead of creating symlinks. |
| `--force` | Replace an existing real directory. Symlinks are refreshed safely. |
| `--dry-run` | Print planned actions without changing files. |
| `--list` | List available skills. |

Global installation respects environment-specific homes:

| Variable | Used For | Default |
| --- | --- | --- |
| `CODEX_HOME` | Codex global skills. | `$HOME/.codex` |
| `CLAUDE_HOME` | Claude Code global skills. | `$HOME/.claude` |
| `AGENTS_HOME` | Generic agent skills. | `$HOME/.agents` |

## Skills

| Skill | Purpose |
| --- | --- |
| `sdlc-orchestrator` | Classifies the request, selects the route, and controls gates and handoffs. |
| `intake-coordinator` | Turns vague requests into scoped briefs with assumptions, constraints, and success criteria. |
| `research-domain` | Maps domain context, users, terminology, constraints, and product risks. |
| `competitive-analysis` | Compares competitors, substitutes, gaps, positioning, and scope implications. |
| `requirements-quality` | Converts scope into FR, NFR, quality scenarios, and acceptance criteria. |
| `analyze-codebase` | Reconstructs existing architecture, flows, hotspots, and migration gaps in read-only mode. |
| `architecture-review` | Designs or reviews C4, runtime, deployment, data, API, crosscutting, and ADR artifacts. |
| `user-journey-mapper` | Maps user story maps, journeys, alternate flows, failure flows, and release slices before decomposition. |
| `decompose-work` | Breaks approved work into epics, stories, tasks, dependency graph, and parallel lanes. |
| `service-implementation` | Implements bounded tasks after scope, ownership, contracts, and validation are clear. |
| `perf-and-memory` | Handles latency, throughput, memory, CPU, concurrency, caching, and profiling risks. |
| `qa-eval` | Plans and runs tests, acceptance checks, smoke checks, evals, and release readiness gates. |
| `pr-review` | Reviews diffs for regressions, security/data risks, missing tests, and documentation drift. |
| `documentation-graph-curator` | Maintains Obsidian notes, wikilinks, ADRs, diagrams, and project memory. |

## Repository Layout

```text
AGENTS.md                  # always-on rules for agents
CLAUDE.md                  # Claude Code overlay
PLANS.md                   # long-task planning template
DESIGN.md                  # documentation and diagram design contract
install.sh                 # global/local installer
agentic/                   # main system directory
  skills/                  # all skill folders
  routing/                 # machine-readable and human-readable routing
  obsidian/                # project-memory skeleton
  docs/                    # extended documentation and assets
  scripts/                 # validation helper
```

## Validation

```bash
python3 agentic/scripts/validate.py
./install.sh --global --dry-run
```

The validator checks expanded skill structure, GitHub documentation, routing, SVG assets, Obsidian skeleton, and installer health.
