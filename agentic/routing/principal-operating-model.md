# Principal-Level Operating Model

This model raises every skill from task execution to senior engineering judgment. Use it as a lightweight checklist before moving from analysis to implementation, and again before handoff.

## Core Standard

1. **Evidence before confidence.** Separate facts, assumptions, and recommendations. Use current docs, repo evidence, tests, traces, metrics, or user-provided constraints before claiming certainty.
2. **Context7 by default.** Use Context7 MCP for current library, framework, platform, API, CLI, and configuration documentation whenever external technology behavior affects the answer.
3. **Decision trace.** Record the selected path, viable alternatives, tradeoffs, why the chosen option wins, and what would make the decision change.
4. **Risk budget.** Identify blast radius, reversibility, data/security impact, operational impact, migration risk, and user-facing failure modes.
5. **Validation ladder.** Prefer the cheapest useful proof first: static check, unit test, contract test, integration test, browser/smoke test, load or migration rehearsal, then release readiness.
6. **Ownership and handoff.** Name owners, file/module boundaries, dependency order, merge order, validation evidence, docs updated, and follow-up work.
7. **Stop conditions.** Pause for approval before destructive changes, production changes, irreversible migrations, credential/security changes, or architecture decisions with broad impact.

## Principal Review Questions

- What evidence supports the plan, and what is still assumption?
- Which docs were verified through Context7 or another primary source?
- What is the smallest safe slice that proves the approach?
- What breaks if this is wrong, and how do we detect it quickly?
- What rollback, migration, or containment path exists?
- What artifact must future agents read to avoid rediscovering this decision?

## Source-Informed Practices

- [Google SRE](https://sre.google/sre-book/service-level-objectives/) emphasizes user-relevant SLIs/SLOs and error-budget-aware release decisions.
- [DORA capabilities](https://dora.dev/capabilities/) emphasize continuous delivery, test automation, maintainability, cloud infrastructure, and measurable delivery health.
- [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) emphasizes secure development practices integrated into the SDLC, not bolted on after implementation.
- [OpenSSF SLSA](https://slsa.dev/spec/v1.0/) emphasizes supply-chain provenance, tamper resistance, and artifact trust.
- [Context7 MCP](https://github.com/upstash/context7) guidance recommends auto-invocation for code generation, setup, configuration, and library/API documentation.
