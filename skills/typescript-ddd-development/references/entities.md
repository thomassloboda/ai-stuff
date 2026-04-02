# Entities Reference

## Definition

A domain entity is defined by:
- a stable identity
- lifecycle continuity over time
- domain rules that may affect its state and behavior

An entity is not defined only by the value of its properties.

Examples:
- User
- Order
- Invoice
- Subscription
- Project

## Modeling rules

Every entity should:
- represent a true domain concept with stable identity
- not expose its constructor publicly
- keep internal state private
- expose readonly getters for observable state
- expose domain behaviors through methods
- protect invariants at creation time and before every state change
- prevent invalid state transitions
- implement equality based on identity
- avoid uncontrolled public mutation
- avoid framework-specific annotations and infrastructure concerns

## Identity

Every entity should have a clear identity model.

Prefer:
- a dedicated id value object when the codebase uses one
- otherwise a clearly typed id field

Equality should be identity-based.
Two entities with the same identity should compare as equal, even if reconstructed separately.

Do not compare entities by full property equality.

## Constructor and factories

The constructor should not be public.

Use:
- `create` for new entity creation inside the domain
- `from` for reconstruction from external or persisted data only when needed

### `create`

`create` should:
- require all necessary input for a valid initial state
- enforce invariants
- initialize the entity in a valid lifecycle state
- throw explicit domain errors when invalid

### `from`

`from` should:
- be used only when reconstruction is needed
- validate the reconstructed state unless a different project convention exists
- not silently bypass invariants
- make trust assumptions explicit

Do not add `from` if the user does not need external reconstruction.

## Behavior

Entities should contain meaningful domain behavior whenever such behavior exists.

Prefer methods like:
- `activate()`
- `rename()`
- `cancel()`
- `markAsPaid()`
- `assignOwner()`

Avoid:
- plain setter-style methods with no business meaning
- exposing mutable state directly
- generating CRUD-shaped classes and calling them DDD entities

## Invariants and transitions

All important invariants should be explicit.

Examples:
- a cancelled subscription cannot be activated without a dedicated business rule
- an invoice already paid cannot be cancelled
- a user cannot be created without a valid identity and required fields

Check invariants:
- at creation time
- before every state transition
- when dependent properties change

Use private assertion helpers when it improves readability.

## Public API

An entity may expose:
- readonly getters
- intention-revealing domain methods
- `equals`
- `toJSON` only when explicitly needed

Do not expose:
- public mutable properties
- generic `setX` methods unless they truly represent domain language
- convenience methods with no business meaning

## Equality

Entities compare by identity.

If an `equals` method is implemented:
- it should return true when identities are equal
- it should ignore reference inequality
- it should not compare every property unless identity itself includes those properties

## Serialization

Implement `toJSON` only when the user or context requires serialization.

If `toJSON` exists:
- it should serialize meaningful observable state
- it should not expose hidden implementation details
- tests should cover it

## Testing

Every entity should have unit tests covering:
- valid creation
- creation failures
- invariant enforcement
- invalid state transitions
- valid state transitions
- identity-based equality
- serialization when `toJSON` exists

Where relevant, tests should show that:
- different instances with the same identity are equal
- invalid transitions throw explicit domain errors
- internal state remains valid after each operation

## Folder structure

Use:

```md
src
+- core
|   +- domain
|   |   +- entities
|   |   |   +- {entity_name}
|   |   |   |   +- {entity_name}.ts
|   |   |   |   +- {entity_name}.spec.ts
|   |   |   |   +- index.ts
```

## Reporting expectations

After creating an entity, report:
- file paths
- entity identity model
- initial invariants
- lifecycle or state transition rules
- public behaviors
- tests added
- assumptions made

## Anti-patterns

Do not:
- model an entity as a primitive wrapper with only a `value`
- expose public setters for all fields
- compare entities by full deep equality
- bypass invariants in `from`
- generate a purely anemic model when real behavior is known
- add persistence or framework code to the domain entity
