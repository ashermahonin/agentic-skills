---
name: analyze-codebase
description: "Analyze an existing repository in read-only mode to reconstruct current behavior, architecture, dependency clusters, build and test health, hotspots, tech debt, ownership boundaries, integration points, and current-vs-target gaps. Use for existing-product improvement, migration planning, code archaeology, risky refactors, unfamiliar repositories, or artifacts `80-current-state-scan.md` through `85-migration-plan.md` before writing code."
---

# Analyze Codebase

## Role

Slow the impulse to edit until the system has been understood. Produce an evidence-backed map of what exists, how it behaves, and where change would be risky.

## Start By

- Read the repo orientation files and build/test commands.
- List languages, frameworks, services, data stores, queues, and deployment pieces.
- Find entrypoints, critical flows, and ownership boundaries.
- Identify generated, vendored, or external code that should not be rewritten casually.

## Procedure

1. Map top-level directories to responsibilities.
2. Trace the most important runtime flows from entrypoint to persistence or external boundary.
3. Check build, test, lint, and local run instructions without changing source files.
4. Identify hotspots: high-change files, large modules, unclear boundaries, test gaps, risky dependencies, and fragile contracts.
5. Compare current architecture to the requested target and write migration risks before proposing edits.
6. Stay read-only unless the user explicitly moves the work into implementation.

## Output Artifacts

- Current-state scan
- Codebase map
- Hotspots and tech-debt list
- Current architecture summary
- Target gap notes
- Migration plan inputs

## Quality Bar

- Back claims with file paths, commands, or observed behavior.
- Do not infer architecture from folder names alone.
- Separate actual current behavior from desired target behavior.
- Call out unknowns instead of smoothing them over.

## Handoff

Hand off evidence, high-risk files, safe write boundaries, and validation commands to architecture or decomposition.

## References

- `references/scan-checklist.md`: Use this checklist when scanning an existing repository.
