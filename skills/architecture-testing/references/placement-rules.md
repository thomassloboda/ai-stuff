# Placement Rules Reference

## Goal

Validate that files live in the correct architectural location.

## Expected mapping

- entities, value objects, aggregates, and domain errors → `src/core/domain/*`
- primary and secondary ports → `src/core/ports/*`
- use cases → `src/application/use-cases/*`
- domain-services in the application layer → `src/application/domain-services/*`
- in-memory adapters → `src/infrastructure/in-memory/*`
- persistence adapters → `src/infrastructure/persistence/*`
- REST adapters → `src/infrastructure/rest/*`
- third-party integrations → `src/infrastructure/thirds/*`

## Test intent

Placement tests should help detect:
- domain artifacts misplaced in infrastructure
- adapters misplaced in core
- use cases placed under infrastructure
- ports implemented directly in core domain folders
