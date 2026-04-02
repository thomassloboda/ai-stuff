# Dependency Rules Reference

## Goal

Define and enforce allowed dependency directions between architectural layers.

## Recommended rules for the current project structure

Expected structure:
- `src/core/domain/*`
- `src/core/ports/primary/*`
- `src/core/ports/secondary/*`
- `src/application/domain-services/*`
- `src/application/use-cases/*`
- `src/infrastructure/*`

Allowed directions:
- `core/domain` may depend only on `core/domain`
- `core/ports` may depend on `core/domain`
- `application` may depend on `core/domain` and `core/ports`
- `infrastructure` may depend on `application`, `core/ports`, and `core/domain`

Forbidden directions:
- `core/domain` → `application`
- `core/domain` → `infrastructure`
- `core/ports` → `application`
- `core/ports` → `infrastructure`
- `application` → `infrastructure` only if the repository explicitly allows direct adapter references, otherwise forbid it

## Test intent

Architecture tests should make violations obvious and actionable.

Examples:
- domain importing a Mongo adapter should fail
- application importing a REST controller should fail
- ports importing infrastructure implementations should fail
