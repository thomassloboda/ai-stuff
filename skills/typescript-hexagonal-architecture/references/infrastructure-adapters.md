# Infrastructure Adapters Reference

## Definition

Infrastructure adapters are concrete implementations that connect the application to technical systems.

Examples:
- repository implementations
- REST controllers
- SDK-based gateways
- messaging adapters
- in-memory adapters used as concrete test infrastructure

## Placement

Place adapters under the relevant infrastructure folder:
- `src/infrastructure/in-memory`
- `src/infrastructure/persistence/sqlite`
- `src/infrastructure/persistence/mongodb`
- `src/infrastructure/persistence/kafka`
- `src/infrastructure/rest`
- `src/infrastructure/thirds`

## Rules

Adapters should:
- implement primary or secondary ports when relevant
- convert external formats into application or domain concepts
- keep framework and SDK details at the edge
- avoid containing central business logic
- remain focused on integration responsibilities

## Mapping guidance

Adapters may need mapping logic.

Keep mapping:
- explicit
- local to the adapter or its helper module
- separate from domain behavior

Do not leak persistence records, HTTP DTOs, or SDK objects into the core domain unnecessarily.

## Testing

Every adapter should have tests at an appropriate level.

Examples:
- in-memory adapters: unit tests
- repository adapters: integration-style tests or contract-oriented tests when appropriate
- REST adapters: request/response mapping tests
- third-party adapters: focused tests around mapping and interaction boundaries
