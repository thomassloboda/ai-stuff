# Ports Reference

## Definition

Ports are explicit contracts between the core of the system and the outside world.

They define what the application exposes to external drivers and what the application requires from external providers.

## Primary ports

Primary ports model incoming interactions.

Place them under:
- `src/core/ports/primary`

Typical examples:
- use-case interfaces
- command handler contracts
- query handler contracts

Primary ports should:
- be small
- be framework-agnostic
- expose application intent clearly
- avoid transport-specific payloads unless the project explicitly chooses otherwise

## Secondary ports

Secondary ports model outgoing dependencies.

Place them under:
- `src/core/ports/secondary`

Typical examples:
- repository contracts
- event publisher contracts
- clock contracts
- id generator contracts
- third-party gateway contracts

Secondary ports should:
- express required capabilities, not technical implementations
- avoid persistence-specific or SDK-specific details
- use domain or application concepts, not infrastructure DTOs

## Design guidance

When designing a port:
- name it after the capability it expresses
- keep it intention-revealing
- keep it small and focused
- avoid large grab-bag interfaces

Prefer:
- `UserRepository`
- `InvoicePublisher`
- `Clock`
- `PaymentGateway`

Avoid:
- `UtilsPort`
- `ExternalServices`
- `GeneralRepository`

## Testing

Ports are often tested indirectly through use cases and adapters.

When explicit contract tests are added, make the contract expectations clear and reusable.
