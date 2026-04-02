# Value Objects Reference

## Definition

A value object is defined by:
- the value it carries
- the business invariants it protects
- equality by value
- absence of conceptual identity

A value object should generally be immutable.

Examples:
- Email
- Money
- Currency
- Slug
- PhoneNumber
- Percentage
- DateRange

## Modeling rules

Every value object should:
- model a true value object, not an entity
- be immutable
- not expose its constructor publicly
- encapsulate one primitive value or a small immutable set of values
- keep stored data private and readonly
- validate input in every public factory
- throw explicit domain errors on invalid input
- implement equality based on canonical value
- avoid public mutation methods
- avoid framework-specific concerns

## Shape

A value object may wrap:
- a single primitive value
- multiple related fields when the concept is still identity-free and value-defined

Examples:
- single primitive: `Email`, `Slug`, `CurrencyCode`
- multiple fields: `Money`, `DateRange`, `GeoPoint`

When wrapping a single primitive, exposing a `value` getter is acceptable when it improves clarity.

When wrapping multiple fields, prefer named getters.

## Constructor and factories

The constructor should not be public.

Use:
- `create` for new domain-safe creation
- `from` for external or semi-trusted input when needed

### `create`

`create` should:
- accept domain-relevant input
- enforce all invariants
- return a valid value object
- reject invalid input explicitly

### `from`

`from` should:
- be used when external input parsing or reconstruction is needed
- validate input
- apply canonicalization when required by the domain
- reject ambiguous or invalid formats explicitly

Do not add `from` if the user does not need it.

## Validation

Validation should be:
- explicit
- local to the value object
- easy to read
- tested thoroughly

Possible validations include:
- required value
- empty or blank value rejection
- min and max length
- numeric bounds
- format constraints
- allowed characters
- precision and scale
- ordering constraints between fields
- domain-specific structural rules

Do not rely on external framework validators in the domain layer unless the user explicitly requests it.

## Normalization and canonicalization

Normalization is allowed only when there is a clear domain reason.

Possible examples:
- trimming surrounding spaces
- lowercasing an email local policy when appropriate
- normalizing Unicode
- storing a canonical currency code
- removing display-only formatting characters from phone numbers

If normalization exists:
- make it explicit in code
- keep it unsurprising
- document it in tests
- compare equality on the normalized stored value

Do not hide surprising transformations.

## Equality

Value objects compare by value, not by reference.

If the value object wraps:
- a single primitive, compare the canonical stored primitive
- multiple fields, compare all meaningful canonical fields

If an `equals` method is implemented:
- it should be deterministic
- it should compare only meaningful value state
- it should not depend on object reference

## Public API

A value object may expose:
- `value` for single-primitive wrappers when useful
- named getters for multi-field value objects
- `equals`
- `toString` when a human-readable representation is meaningful
- `toJSON` when serialization is explicitly needed

Do not expose:
- public mutation methods
- setters
- convenience methods unrelated to domain meaning

## String and JSON representation

Implement `toString` only when a meaningful textual representation exists.

Examples:
- `Email#toString()` returning the canonical email string
- `Slug#toString()` returning the slug text

Implement `toJSON` only when serialization is needed.

If either exists:
- ensure it reflects the canonical value representation
- add tests for it

## Testing

Every value object should have unit tests covering:
- valid creation
- invalid inputs
- boundary cases
- normalization behavior
- equality by value
- string representation when `toString` exists
- serialization when `toJSON` exists

Tests should cover every declared invariant.

Examples:
- blank input rejected
- overlong input rejected
- malformed input rejected
- normalized input yields canonical stored value
- equal canonical values compare as equal

## Folder structure

Use:

```md
src
+- core
|   +- domain
|   |   +- value-objects
|   |   |   +- {value_object_name}
|   |   |   |   +- {value_object_name}.ts
|   |   |   |   +- {value_object_name}.spec.ts
|   |   |   |   +- index.ts
```

## Reporting expectations

After creating a value object, report:
- file paths
- wrapped value shape
- implemented invariants
- normalization rules
- public API
- tests added
- assumptions made

## Anti-patterns

Do not:
- model a value object as an entity with identity
- add mutable setters
- compare by reference
- skip validation in public factories
- normalize silently in a surprising way
- wrap a primitive without any domain meaning or invariant unless the user explicitly wants that abstraction
