# Parallelization Policy

Parallel work is allowed only when it lowers time without raising merge or architecture risk.

## Required Before Parallel Agents

- Frozen interface or contract between lanes.
- Disjoint write scopes.
- Shared files named explicitly.
- Dependency order and merge order written down.
- Validation pack per lane.
- Owner for final integration.

## Do Not Parallelize

- Unclear architecture decisions.
- Shared migration files without a single owner.
- Security or data model changes that require one coherent review.
- Tasks where every worker needs to edit the same core file.

## Handoff Shape

- Lane name
- Owned files/directories
- Inputs
- Outputs
- Validation
- Merge order
- Known conflicts
