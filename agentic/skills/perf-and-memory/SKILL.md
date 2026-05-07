---
name: perf-and-memory
description: "Review or plan performance, memory, allocation, concurrency, caching, latency, throughput, profiling, benchmark, capacity, and language-runtime work. Use when a task mentions speed, memory, scale, load, p95/p99 latency, CPU, heap, allocations, async/concurrency, streaming, database query cost, caching, or artifacts `30-language-profiles.md` and performance-related quality scenarios."
---

# Performance and Memory

## Role

Keep performance work honest. Find the bottleneck with evidence, choose the simplest useful intervention, and make sure the result can be measured again.

## Start By

- Identify the user-visible or system-visible performance problem.
- Choose the metric: latency, throughput, memory, CPU, allocations, query count, startup, bundle size, or cost.
- Find existing benchmarks, traces, logs, or production signals.
- Name the language/runtime constraints that matter.

## Procedure

1. Form a hypothesis and measurement plan before optimizing.
2. Collect baseline evidence or state why baseline cannot be collected.
3. Look for algorithmic issues, I/O bottlenecks, query shape, caching boundaries, concurrency limits, allocation churn, and serialization overhead.
4. Recommend or implement the smallest change likely to move the metric.
5. Re-measure after the change when possible.
6. Record tradeoffs: complexity, correctness risk, cache invalidation, resource cost, and rollback.

## Output Artifacts

- Performance hypothesis
- Baseline and target metric
- Profiling or benchmark plan
- Optimization recommendation
- Validation evidence
- Language profile update

## Quality Bar

- Never optimize an unnamed metric.
- Do not claim improvement without measurement or a clear reason measurement was impossible.
- Treat caching as a correctness and invalidation problem, not a magic speed button.
- Prefer reducing work over hiding work.

## Handoff

Hand off metric, evidence, changed constraints, and regression checks to implementation, QA, or review.

## References

- `references/language-profile-template.md`: Use this for language-specific performance notes.
