# Review Checklist

## Correctness

- Changed behavior matches requirements.
- Edge cases and failure paths are handled.
- Backward compatibility is preserved or migration is explicit.

## Tests

- Changed behavior has coverage.
- Critical failure path has coverage or documented residual risk.
- Test commands are reported.

## Security and Data

- Auth and permission checks still hold.
- Secrets and PII are not leaked.
- Inputs are validated.
- Migrations are safe and reversible enough for the context.

## Operations

- Performance risk is understood.
- Observability and error handling are adequate.
- Docs and runbooks match the change.
