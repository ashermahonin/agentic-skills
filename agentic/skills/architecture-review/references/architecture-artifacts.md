# Architecture Artifacts

Create only artifacts that help decisions, implementation, or review.

## Core Views

- `14-system-context.md`: users, external systems, trust boundary.
- `15-container-view.md`: deployable units and data stores.
- `16-component-view.md`: internal components only when ownership or risk requires it.
- `17-runtime-scenarios.md`: critical happy paths and failure paths.
- `18-deployment-view.md`: environments, scaling, network, secrets, operations.

## Contracts

- `19-data-model.md`: ownership, shape, migrations, retention.
- `20-api-contracts.md`: request/response/events/errors/versioning.
- `21-crosscutting-concepts.md`: auth, observability, errors, retries, safety.

## ADRs

Write an ADR when the decision is expensive to reverse, affects multiple teams, changes data/contracts, or changes operational risk.
