---
name: architecture-review
description: "Design or review software architecture using system context, container, component, runtime, deployment, data, API, integration, crosscutting concepts, and ADR artifacts. Use before large implementation, service-boundary changes, infrastructure changes, API or data contract changes, migrations, reliability work, security-sensitive design, or architecture artifacts `14-system-context.md` through `22-adr-index.md`."
---

# Architecture Review

## Role

Turn requirements and current-state evidence into a system shape that can be implemented, tested, operated, and changed. Prefer clarity and tradeoffs over ornamental diagrams.

## Start By

- Gather requirements, quality scenarios, current-state evidence, and constraints.
- Name the architecture decision that matters most.
- Identify boundaries: user/system, service/service, data/API, sync/async, build/runtime, trust zones.
- Decide what must be documented as an ADR.

## Procedure

1. Draft the system context first, then containers, then components only where detail changes decisions.
2. Map runtime scenarios for critical user and failure paths.
3. Define data ownership, API contracts, integration contracts, and deployment assumptions.
4. Review crosscutting concerns: auth, secrets, observability, errors, retries, rate limits, privacy, migration, rollback, and operations.
5. Write tradeoffs explicitly, including what is intentionally not solved.
6. Refuse implementation handoff until risky decisions have owners and validation paths.

## Principal-Level Defaults

- Follow `../../routing/principal-operating-model.md` before moving from analysis to implementation.
- Use Context7 MCP for current library, framework, platform, API, CLI, and configuration documentation whenever the task depends on external technology behavior.
- Keep a decision trace: facts, assumptions, options considered, tradeoffs, selected path, validation evidence, and rollback or follow-up.
- Escalate irreversible, security-sensitive, data-migration, production, or cross-boundary choices before write-heavy work.

## Output Artifacts

- System context
- Container and component views
- Runtime scenarios
- Deployment view
- Data model and API contracts
- ADR candidates or decisions

## Quality Bar

- Architecture must answer how the system changes safely, not only how it works when happy.
- Do not draw a component unless it affects ownership, contract, or risk.
- Call out irreversible or expensive decisions.
- Tie architecture back to requirements and quality scenarios.

## Handoff

Hand off boundaries, contracts, ADRs, validation expectations, and unresolved risks to decomposition.

## References

- `references/architecture-artifacts.md`: Use this to decide which architecture artifacts are required.
