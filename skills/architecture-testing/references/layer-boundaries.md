# Layer Boundaries Reference

## Goal

Keep responsibilities clear across domain, ports, application, and infrastructure.

## Expected ownership

### Domain
Contains:
- entities
- value objects
- aggregates
- domain errors
- pure domain logic

Must not contain:
- ORM code
- HTTP DTOs
- transport logic
- logging SDK usage
- infrastructure clients

### Ports
Contains:
- primary ports for inbound contracts
- secondary ports for outbound contracts

Must not contain:
- concrete infrastructure implementations
- business workflow orchestration that belongs to use cases

### Application
Contains:
- use cases
- domain-service orchestration when needed

Must not contain:
- low-level infrastructure details
- transport controller responsibilities

### Infrastructure
Contains:
- adapter implementations
- persistence details
- REST adapters
- third-party integrations
- in-memory implementations used for testing or local execution

Must not contain:
- core business rules that belong in domain or application
