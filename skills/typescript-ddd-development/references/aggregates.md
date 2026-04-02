# Aggregates Reference

## Definition

An aggregate is a consistency boundary in the domain model.

It groups one aggregate root and, when needed, other internal entities and value objects that must remain consistent together according to domain rules.

The aggregate root is the only entry point from outside the aggregate boundary.

An aggregate is not:
- a technical object graph
- a persistence convenience grouping
- a random collection of related entities
- a full module or bounded context

Examples:
- `Order` as aggregate root with `OrderLine` items
- `Cart` as aggregate root with `CartItem` items
- `Invoice` as aggregate root with line items and totals
- `Subscription` as aggregate root with plan state and renewal rules

## Purpose

Aggregates should help enforce domain consistency.

They should:
- protect invariants that must hold together
- define clear transactional boundaries
- control access to internal state
- prevent external code from mutating nested entities freely
- make domain behavior explicit

Use an aggregate when multiple domain objects must change together under the control of one root.

## Aggregate root

Every aggregate should have exactly one aggregate root.

The aggregate root should:
- have a stable identity
- expose the public behaviors of the aggregate
- enforce aggregate-wide invariants
- control creation, modification, and removal of internal members
- protect internal entities from uncontrolled external mutation

External code should interact with the aggregate through the root only.

Do not expose internal entities for direct modification.

## Modeling rules

Every aggregate should:
- represent a true consistency boundary
- define one clear root entity
- keep internal state valid after every public operation
- expose intention-revealing domain methods
- enforce invariants at the boundary
- avoid leaking internal mutation control
- avoid infrastructure and framework concerns
- remain as small as the domain allows while still protecting consistency

Do not create aggregates just because objects are related.
Create them when consistency rules require a shared boundary.

## When to use an aggregate

Use an aggregate when:
- one root must control a set of dependent objects
- multiple changes must preserve shared invariants
- external code must not update internal members independently
- the concept has a natural transactional consistency boundary

Typical examples:
- an `Order` controlling its lines, status, and totals
- a `Cart` controlling the items it contains
- a `Project` controlling membership rules
- a `BankAccount` controlling balance-affecting operations

Do not use an aggregate when:
- related objects can evolve independently
- consistency does not need to be immediate
- the boundary would become overly large and hard to maintain
- you are only mirroring database joins

## Boundary rules

The aggregate boundary should be explicit.

Inside the boundary:
- internal entities and value objects may collaborate
- the root coordinates meaningful changes
- all invariants must hold after each public method returns

Outside the boundary:
- no direct mutation of internal members
- no bypass of root rules
- no reaching into nested entities to modify state

If external code needs to trigger a change, add a root behavior for it.

## Invariants

Aggregates exist to protect invariants that span multiple internal objects.

Examples:
- an order cannot contain duplicate lines for the same product if the domain forbids it
- an invoice total must match its lines
- a cart cannot exceed a maximum item count
- a subscription cannot move to a forbidden state
- a project owner cannot be removed if ownership would become undefined

Every public operation should preserve aggregate invariants.

Prefer explicit guard methods and invariant checks when that improves readability.

## Aggregate size

Prefer small aggregates.

A good aggregate:
- protects real consistency rules
- has a narrow public API
- keeps operations understandable
- avoids loading or mutating unrelated data

Avoid large aggregates that:
- include too many unrelated responsibilities
- become difficult to reason about
- require many unrelated collaborators
- create unnecessary contention or complexity

If an aggregate becomes too large, reconsider the consistency boundary.

## Identity and equality

The aggregate root is an entity and should compare by identity.

Internal entities, when they exist, should follow the project entity conventions.
Value objects should follow value-based equality.

Do not compare the aggregate by deep object graph equality.

## Internal entities and value objects

An aggregate may contain:
- internal entities
- value objects
- collections of internal members

The aggregate root should control:
- addition
- removal
- replacement
- state changes
- invariant checks involving those members

Internal entities should not expose unrestricted public mutation.

When possible, prefer value objects for internal components that do not require identity.

## Constructor and factories

The aggregate root constructor should not be public.

Use:
- `create` for new aggregate creation
- `from` only when reconstruction from external or persisted data is required

### `create`

`create` should:
- initialize the aggregate in a valid state
- enforce root-level invariants
- ensure internal members are also valid
- reject invalid input explicitly

### `from`

`from` should:
- reconstruct the aggregate only when necessary
- validate or revalidate critical invariants unless project conventions explicitly differ
- not silently bypass consistency rules
- make trust assumptions explicit

Do not add `from` without a clear need.

## Public API

The aggregate root should expose domain behaviors, not generic structure mutation.

Prefer methods like:
- `addItem()`
- `removeItem()`
- `changeQuantity()`
- `submit()`
- `cancel()`
- `assignOwner()`
- `renew()`

Avoid:
- exposing mutable arrays directly
- public setters for nested state
- CRUD-shaped methods with no domain meaning
- getters that leak internal mutable references

If collections are exposed:
- expose readonly views
- do not allow external mutation of internal state

## State transitions

When an aggregate has lifecycle states:
- make transitions explicit
- validate them through root behaviors
- throw explicit domain errors for forbidden transitions

Examples:
- a submitted order cannot be modified unless a rule allows it
- a paid invoice cannot be cancelled
- an archived project cannot accept new tasks if forbidden

State transitions should be easy to understand from the public API.

## Consistency and eventual consistency

Use aggregates for rules that require immediate consistency inside one boundary.

Do not force unrelated concepts into one aggregate just to avoid coordination.
If consistency can be eventual:
- keep separate aggregates
- coordinate outside the aggregate boundary when needed

Do not model cross-aggregate workflows as if they were one in-memory object graph.

## Repository guidance

A repository should load and save the aggregate root, not arbitrary internal pieces.

External code should usually:
- retrieve the aggregate root
- invoke root behaviors
- persist the root

Do not create repositories for internal members unless the architecture explicitly requires it.

## Serialization

Implement `toJSON` only when serialization is explicitly needed.

If `toJSON` exists:
- serialize the root's observable state
- avoid exposing hidden implementation details
- keep the serialized shape aligned with domain meaning
- add tests for it

## Testing

Every aggregate test suite should cover, when relevant:
- valid creation
- creation failures
- aggregate-wide invariants
- valid root behaviors
- invalid root behaviors
- valid state transitions
- invalid state transitions
- protection against illegal internal mutation through the public API
- serialization when `toJSON` exists

### Typical cases

Examples:
- adding an item updates the aggregate consistently
- duplicate item insertion is rejected when forbidden
- removing the last owner is rejected when forbidden
- modifying a closed aggregate is rejected
- total or derived state remains consistent after each operation

Tests should verify the aggregate as a consistency boundary, not just isolated property changes.

## File structure

Unless the project uses another convention, use:

```md
src
+- core
|   +- domain
|   |   +- aggregates
|   |   |   +- {aggregate_name}
|   |   |   |   +- {aggregate_name}.ts
|   |   |   |   +- {aggregate_name}.spec.ts
|   |   |   |   +- index.ts
```

If the codebase places aggregate roots under `entities`, follow the existing convention and state it explicitly.

## Reporting expectations

After creating an aggregate, report:
- file paths
- chosen aggregate root
- aggregate boundary
- internal members
- aggregate-wide invariants
- public behaviors
- state transition rules
- tests added
- assumptions made about consistency and lifecycle

## Anti-patterns

Do not:
- call any large entity graph an aggregate without a consistency reason
- expose internal entities for direct uncontrolled mutation
- model database relationships as aggregates by default
- build overly large aggregates with many unrelated responsibilities
- bypass root invariants through public data exposure
- add repositories for internal members by default
- compare aggregates by deep graph equality
- mix infrastructure concerns into aggregate code
