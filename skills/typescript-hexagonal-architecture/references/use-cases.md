# Use Cases Reference

## Definition

A use case orchestrates application flow.

It coordinates domain objects and ports to achieve one meaningful application action.

Examples:
- create an order
- cancel a subscription
- publish an invoice
- retrieve an account summary

## Placement

Place use cases under:
- `src/application/use-cases`

## Responsibilities

A use case should:
- coordinate the required ports and domain artifacts
- validate application-level flow when needed
- delegate business invariants to domain types whenever possible
- remain focused on one application action
- stay independent from concrete infrastructure implementations

## Avoid

Do not:
- place transport code in use cases
- place SQL, ORM, SDK, or HTTP details in use cases
- move rich domain behavior out of entities, aggregates, or value objects without reason
- make one use case responsible for many unrelated actions

## Testing

Every use case should have tests covering:
- happy path
- failure path
- interaction with required ports
- important application branching

Use in-memory or mocked secondary ports where appropriate.
