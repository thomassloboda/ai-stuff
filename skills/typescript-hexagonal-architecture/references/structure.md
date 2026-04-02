# Structure Reference

## Purpose

This reference defines the default folder structure for the TypeScript hexagonal architecture used in this project.

## Target structure

```md
src
+- application
|  +- domain-services
|  +- use-cases
+- core
|  +- domain
|  |  +- aggregates
|  |  +- domain-error
|  |  +- entities
|  |  +- value-objects
|  +- ports
|     +- primary
|     +- secondary
+- infrastructure
|  +- in-memory
|  +- persistence
|  |  +- sqlite
|  |  +- mongodb
|  |  +- kafka
|  +- rest
|  +- thirds
```

## Placement rules

### `src/core/domain`

Place here:
- aggregates
- entities
- value objects
- domain errors

This folder must remain free from infrastructure and application concerns.

### `src/core/ports/primary`

Place here:
- primary input contracts
- interfaces that define how the outside world can trigger application behavior

### `src/core/ports/secondary`

Place here:
- repository interfaces
- gateway interfaces
- publisher interfaces
- contracts for external capabilities required by the application

### `src/application/use-cases`

Place here:
- application orchestration classes
- command/query use cases
- workflows that coordinate domain and ports

### `src/application/domain-services`

Place here:
- explicit application-layer domain coordination that does not fit inside one domain type in this architecture

Do not place generic helpers here.

### `src/infrastructure/in-memory`

Place here:
- in-memory adapters
- local testing adapters
- fake repositories when they are concrete infrastructure implementations

### `src/infrastructure/persistence/sqlite`

Place here:
- SQLite-specific repositories
- SQLite mappers
- SQLite persistence helpers

### `src/infrastructure/persistence/mongodb`

Place here:
- MongoDB-specific repositories
- MongoDB mappers
- MongoDB persistence helpers

### `src/infrastructure/persistence/kafka`

Place here:
- Kafka-based adapters when they belong to this project's persistence or event-stream infrastructure convention

### `src/infrastructure/rest`

Place here:
- REST controllers
- request/response mappers
- route-facing adapters

### `src/infrastructure/thirds`

Place here:
- third-party SDK adapters
- external API clients
- concrete implementations for external services

## Folder-local conventions

Every meaningful artifact folder should usually contain:
- implementation file
- spec file
- `index.ts`

Prefer colocated tests and barrel files unless the project already uses another convention.

## Reporting

When creating code, state clearly:
- where each file was placed
- why that layer was selected
- whether the default structure was followed or adapted
