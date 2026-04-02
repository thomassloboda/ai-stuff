---
name: typescript-hexagonal-architecture
description: Use this skill to design, generate, and maintain TypeScript code that respects a strict hexagonal architecture with explicit dependency rules, barrel files, and systematic testing.
---

# Purpose

This skill helps design and implement TypeScript code following a strict hexagonal architecture.

It is intended for:
- application use cases
- domain services at the application layer
- primary and secondary ports
- infrastructure adapters
- persistence adapters
- REST adapters
- in-memory adapters
- architecture-aware tests
- barrel-file based module exposition

This skill focuses on placement, dependency direction, adapter boundaries, port contracts, module exposition, and test discipline.

It should work especially well together with `typescript-ddd-development` when the project also follows tactical DDD.

# Target structure

Unless the user explicitly asks otherwise, use this structure:

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

Follow the existing project structure if it already differs, but state the deviation explicitly.

# Core principles

Always:
- place code in the correct layer before thinking about implementation details
- keep dependency direction explicit and one-way
- keep business rules out of infrastructure code
- define contracts in ports and implement them in adapters
- expose modules through barrel files
- generate or update tests for every created or modified artifact
- prefer simple, readable module boundaries over clever abstractions
- respect existing project conventions when they are already established

Avoid:
- leaking framework, transport, persistence, or SDK concerns into the core domain
- letting infrastructure dictate domain shape
- placing use-case orchestration in controllers or persistence adapters
- placing domain logic in REST handlers, repositories, or messaging adapters
- bypassing ports to call infrastructure directly from application code
- skipping tests for “simple” files
- bypassing barrel files with unnecessary deep imports

# Layer responsibilities

## `src/core/domain`

This layer contains pure domain building blocks.

It may contain:
- aggregates
- entities
- value objects
- domain errors

It should:
- model business concepts and invariants
- remain independent from application and infrastructure concerns
- avoid persistence, HTTP, messaging, framework, and SDK code

Use `typescript-ddd-development` for modeling artifacts in this layer.

## `src/core/ports`

This layer contains explicit contracts between the core and the outside world.

### `src/core/ports/primary`

Primary ports define how the outside world can drive the application.

Typical examples:
- use case interfaces
- command handlers contracts
- query handlers contracts

### `src/core/ports/secondary`

Secondary ports define what the application needs from the outside world.

Typical examples:
- repositories
- event buses
- clocks
- id generators
- third-party gateways

Ports should:
- be framework-agnostic
- use domain or application concepts, not infrastructure DTOs
- remain small and intention-revealing

## `src/application`

This layer orchestrates business flows.

### `src/application/use-cases`

Use cases:
- coordinate domain objects and ports
- enforce application flow
- do not contain infrastructure details
- do not replace domain behavior with procedural business logic

### `src/application/domain-services`

Use this folder only for domain-oriented coordination that does not naturally belong inside a single aggregate, entity, or value object and that is still part of application-layer orchestration in this architecture.

Keep these services focused and explicit.

## `src/infrastructure`

This layer contains technical implementations.

It may contain:
- in-memory adapters
- persistence adapters
- REST adapters
- third-party integrations

Infrastructure code may depend on application, ports, and domain. The reverse must not happen.

# Dependency rules

The dependency direction should be:
- `core/domain` -> depends only on `core/domain`
- `core/ports` -> may depend on `core/domain`
- `application` -> may depend on `core/domain` and `core/ports`
- `infrastructure` -> may depend on `application`, `core/ports`, and `core/domain`

Never allow:
- `core/domain` importing from `application`
- `core/domain` importing from `infrastructure`
- `core/ports` importing from `infrastructure`
- `application` importing concrete infrastructure implementations

If a use case needs external behavior, depend on a secondary port.
If the outside world needs to trigger a use case, go through a primary port or directly through the use-case public API according to project convention.

# Artifact routing

Use this skill to determine where an artifact belongs before generating it.

## Place in `src/core/domain/*`
- aggregates
- entities
- value objects
- domain errors

## Place in `src/core/ports/primary/*`
- primary input contracts
- use-case entry interfaces when the project uses them

## Place in `src/core/ports/secondary/*`
- repository contracts
- gateway contracts
- publisher contracts
- external service contracts
- time, id, or randomness abstractions when needed

## Place in `src/application/use-cases/*`
- command use cases
- query use cases
- workflow orchestration classes

## Place in `src/application/domain-services/*`
- coordination logic that is domain-oriented but does not fit naturally inside a single domain type in this architecture

## Place in `src/infrastructure/in-memory/*`
- in-memory repositories
- test doubles used as concrete adapters
- local non-persistent adapter implementations

## Place in `src/infrastructure/persistence/sqlite/*`
- SQLite repositories
- SQLite mappers
- SQLite persistence-specific helpers

## Place in `src/infrastructure/persistence/mongodb/*`
- MongoDB repositories
- MongoDB mappers
- MongoDB persistence-specific helpers

## Place in `src/infrastructure/persistence/kafka/*`
- Kafka producers and consumers when modeled as persistence or event-stream adapters in this project structure

## Place in `src/infrastructure/rest/*`
- HTTP controllers
- REST request/response mapping
- route-level adapters

## Place in `src/infrastructure/thirds/*`
- third-party SDK adapters
- external API gateways
- external service implementations

# Barrel files

Barrel files are required by default.

Use `index.ts` files to expose public modules at each meaningful folder level.

Always:
- create or update `index.ts` when adding an exposable artifact
- keep exports explicit and readable
- align barrel file granularity with the folder structure

Avoid:
- deep imports across the codebase when a barrel file exists
- wildcard re-export chains so deep that module ownership becomes unclear

# Testing policy

Everything created or modified must be tested at the appropriate level.

At minimum:
- domain artifacts must have unit tests
- use cases must have unit tests
- adapters must have tests appropriate to their responsibility
- regressions should add or update a test proving the fix
- barrel files should be updated and validated whenever module exposition changes

Prefer colocated `*.spec.ts` files unless the project already uses another convention.

Apply the DDD testing reference as well when the artifact touches domain logic.

# Template usage

Use templates as accelerators, not rigid recipes.

When using templates:
- adapt them to the requested artifact
- remove unused methods rather than filling placeholders mechanically
- preserve project conventions when already present
- keep the final implementation as small as possible while respecting the architecture

Recommended templates:
- `templates/use-case.ts.template.md`
- `templates/use-case.spec.ts.template.md`
- `templates/primary-port.ts.template.md`
- `templates/secondary-port.ts.template.md`
- `templates/in-memory-adapter.ts.template.md`
- `templates/repository-adapter.ts.template.md`
- `templates/rest-adapter.ts.template.md`
- `templates/index.ts.template.md`
- `templates/architecture-spec.ts.template.md`

# Output expectations

After generating or modifying code, always report:
- created or modified file paths
- selected layer and why
- dependency constraints respected
- ports introduced or reused
- adapters introduced or reused
- barrel files created or updated
- tests added or updated
- any deviation from the default structure
- any assumption or uncertainty

# Anti-pattern checks

Before finalizing, check that the code does not:
- place business logic in infrastructure adapters
- let application code depend on concrete infrastructure classes
- leak HTTP, ORM, SDK, or persistence types into core domain code
- bypass ports to access infrastructure directly
- expose modules without updating barrel files
- add untested artifacts
- mix unrelated responsibilities inside one adapter
- create architecture that contradicts the declared folder structure
