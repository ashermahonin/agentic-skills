# Existing Codebase Scan Checklist

## Orientation

- Read agent docs, README, build files, and deployment notes.
- Identify languages, package managers, frameworks, services, and databases.

## Structure

- Map top-level directories to responsibilities.
- Mark generated, vendored, legacy, and experimental areas.

## Runtime Flows

- Entry points
- Authentication/authorization path
- Main user workflow
- Persistence and external integration path
- Background jobs or queues

## Health

- Build command
- Test command
- Lint/type command
- Known failures
- Missing coverage around risky areas

## Risk

- Hotspots
- Tight coupling
- Hidden contracts
- Data migration concerns
- Rollback hazards
