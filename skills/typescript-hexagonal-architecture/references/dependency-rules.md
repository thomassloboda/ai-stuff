# Dependency Rules Reference

## Purpose

This reference defines allowed dependency directions in the hexagonal architecture.

## Allowed dependency directions

Use the following rules:
- `src/core/domain` may depend only on itself
- `src/core/ports` may depend on `src/core/domain`
- `src/application` may depend on `src/core/domain` and `src/core/ports`
- `src/infrastructure` may depend on `src/application`, `src/core/ports`, and `src/core/domain`

## Forbidden dependency directions

Never allow:
- `src/core/domain` -> `src/application`
- `src/core/domain` -> `src/infrastructure`
- `src/core/ports` -> `src/infrastructure`
- `src/application` -> concrete infrastructure adapters

If an application service or use case requires outside behavior, introduce or reuse a secondary port.

If an outside adapter needs to trigger application behavior, connect it to the application through a primary port or through the public use-case API according to project convention.

## Port usage rules

Primary ports define how the outside world enters the application.

Secondary ports define what the application expects from the outside world.

Do not:
- inject concrete repositories directly into domain classes
- import REST DTOs into core domain types
- make ports depend on infrastructure implementation details

## Verification guidance

Before finalizing code, verify that:
- application code depends on abstractions rather than concrete adapters
- domain code is free from infrastructure imports
- ports remain small and framework-agnostic
- adapter code is kept at the edges
