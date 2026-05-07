# Quality Scenario Format

Use this for nonfunctional requirements that need measurable evidence.

## Scenario

- Quality attribute:
- Source of stimulus:
- Stimulus:
- Environment:
- System response:
- Response measure:
- Validation method:

## Example

- Quality attribute: latency
- Source of stimulus: authenticated user
- Stimulus: opens dashboard with 5,000 items
- Environment: production-like data set
- System response: dashboard renders usable first view
- Response measure: p95 under agreed threshold
- Validation method: benchmark or browser trace
