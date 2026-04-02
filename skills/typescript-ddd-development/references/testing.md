# Domain Testing Reference

## Purpose

This reference defines how to test TypeScript domain-layer code generated with DDD principles.

It applies to:
- entities
- value objects
- domain errors
- domain services
- repository interfaces only when contract tests are explicitly requested

The goal is to make domain tests:
- readable
- behavior-focused
- precise
- stable
- aligned with business rules

## General principles

Domain tests should:
- test business behavior, not implementation trivia
- use explicit and intention-revealing test names
- focus on invariants, behaviors, and failures
- remain independent from frameworks and infrastructure
- be easy to read without excessive helper indirection
- prefer a small number of meaningful assertions over broad snapshot-style assertions

Prefer tests that explain domain rules.

Examples:
- `should reject a blank email`
- `should normalize and store email in canonical form`
- `should not cancel a paid invoice`
- `should consider two orders with the same id equal`

## Scope

Test what belongs to the domain layer:
- validation rules
- normalization rules
- equality semantics
- state transitions
- invariant enforcement
- domain-specific behaviors
- explicit domain errors
- serialization behavior only when serialization methods exist

Do not test:
- TypeScript itself
- getters and setters with no logic just for coverage
- framework decorators or adapters in domain tests
- persistence behavior in pure domain unit tests
- incidental private helper methods directly

## File structure

Unless the user asks otherwise, colocate tests with the artifact:

```md
src
+- core
|   +- domain
|   |   +- entities
|   |   |   +- {entity_name}
|   |   |   |   +- {entity_name}.spec.ts
|   |   +- value-objects
|   |   |   +- {value_object_name}
|   |   |   |   +- {value_object_name}.spec.ts
|   |   +- errors
|   |   |   +- {error_name}
|   |   |   |   +- {error_name}.spec.ts  // only if dedicated tests are useful
```

## Test naming

Use test names that state:
- the action or condition
- the expected domain outcome

Prefer:
- `should create a valid email`
- `should reject an email without at sign`
- `should trim surrounding spaces before validation`
- `should prevent transition from paid to cancelled`

Avoid:
- `test email`
- `works correctly`
- `should behave properly`
- `invalid case`

## Value object testing

Every value object test suite should cover, when relevant:
- valid creation
- invalid inputs
- boundary values
- normalization or canonicalization
- equality by value
- `toString` when it exists
- `toJSON` when it exists

### Typical cases

For a primitive-based value object:
- blank input rejected
- malformed input rejected
- minimum valid value accepted
- maximum valid value accepted
- normalization behavior documented
- equal canonical values compare as equal

For a multi-field value object:
- invalid field combinations rejected
- ordering rules enforced
- equality compares meaningful canonical fields

## Entity testing

Every entity test suite should cover, when relevant:
- valid creation
- creation failures
- identity semantics
- invariant enforcement
- valid state transitions
- invalid state transitions
- public domain behaviors
- serialization when `toJSON` exists

### Typical cases

For an entity:
- creation initializes a valid state
- forbidden transitions throw explicit domain errors
- repeated forbidden actions remain rejected
- separate instances with the same identity are equal
- observable state changes after valid behavior calls

## Domain error testing

Test domain errors when:
- they carry meaningful custom behavior
- they expose structured data
- the codebase explicitly tests error classes

Otherwise, testing them indirectly through entities or value objects is often enough.

When tested directly, cover:
- error name
- error message
- optional structured context

## Domain service testing

When testing a domain service:
- focus on domain decisions and orchestration
- mock only the minimum required collaborators
- avoid infrastructure-heavy setup
- verify business outcomes, not call choreography unless it matters to the rule

Use domain services only when behavior does not naturally belong to an entity or value object.

## Equality testing

Equality tests should match the model type.

For value objects:
- equal canonical values should be equal
- different values should not be equal
- equality should not depend on reference identity

For entities:
- same identity should be equal
- different identity should not be equal
- equality should not require full property equality

## Failure assertions

When domain rules fail:
- assert the explicit domain error type when relevant
- assert the failure condition clearly
- assert the message only when messages are part of the project convention

Prefer precise assertions over broad "throws any error" checks.

Good examples:
- rejects with `InvalidEmailError`
- rejects when end date is before start date
- rejects cancellation of a paid invoice

## Boundary testing

Boundary cases should be tested whenever validation involves:
- min or max length
- numeric limits
- inclusive or exclusive boundaries
- date ordering
- allowed character sets
- precision and scale

Prefer testing:
- just below boundary
- exact boundary
- just above boundary

This often gives better coverage than many arbitrary invalid examples.

## Normalization testing

If normalization or canonicalization exists, tests should make it explicit.

Cover:
- accepted unnormalized input
- canonical stored representation
- equality based on canonical value
- surprising transformations should not exist

Examples:
- surrounding spaces trimmed
- casing normalized when domain rules require it
- formatting characters removed only when explicitly intended

## Serialization testing

Test serialization only if methods like `toJSON` exist.

Serialization tests should verify:
- the serialized shape
- the serialized canonical value
- no leaking of hidden internal implementation details

Do not add serialization tests when no serialization API exists.

## Test style

Prefer:
- one behavior per test
- explicit arrange / act / assert structure when it improves readability
- direct construction through public factories
- minimal fixtures
- deterministic inputs

Avoid:
- large shared mutable fixtures
- overuse of test helpers that hide intent
- testing private methods directly
- asserting many unrelated behaviors in one test

## Coverage guidance

Coverage matters, but business coverage matters more than raw percentage.

Aim to cover:
- every declared invariant
- every domain behavior
- every invalid transition
- every normalization rule
- every meaningful equality rule

Do not add meaningless tests only to inflate coverage.

## Reporting expectations

After generating tests, report:
- created test file paths
- covered rules and behaviors
- edge cases included
- normalization cases included, if any
- equality cases included
- any intentionally untested area and why

## Anti-patterns

Do not:
- test implementation details instead of business rules
- duplicate the same case many times with cosmetic differences
- write snapshot tests for simple domain objects without need
- assert broad generic errors when explicit domain errors exist
- generate coverage-only tests with no business value
- mix infrastructure integration concerns into pure domain unit tests
