---
name: typescript-ddd-development
description: Use this skill to design and generate TypeScript domain code following Domain-Driven Design principles, especially entities, value objects, aggregates, domain errors, and their unit tests.
---

# Purpose

This skill helps design and implement domain-layer code in TypeScript using DDD tactical patterns.

It is intended for:
- entities
- value objects
- aggregates and aggregate roots
- domain errors
- repository interfaces
- domain services
- unit tests for domain code

This skill focuses on domain modeling, invariants, lifecycle, behavior, consistency boundaries, and code clarity.

It should avoid infrastructure concerns, framework coupling, transport concerns, and application-layer orchestration unless the user explicitly asks for them or the codebase already mixes them.

# General principles

Always:
- use domain language, not technical placeholder names
- keep the domain layer independent from frameworks and persistence concerns
- make invariants explicit in code
- prefer intention-revealing names
- prefer controlled mutation through domain methods over uncontrolled public setters
- generate unit tests for produced domain code
- keep the public API as small and expressive as possible
- report clearly what was created and which rules were implemented
- prefer existing project conventions over inventing new abstractions
- keep parsing, validation, normalization, state transitions, and behavior explicit

Avoid:
- anemic domain models when meaningful behavior is known
- generic abstractions that are not clearly useful
- introducing base classes unless the codebase already uses them or the user asks for them
- leaking ORM, DTO, HTTP, framework, schema-validation, or persistence concerns into the domain layer
- inventing business rules that were not provided, unless they are obvious structural invariants
- forcing every concept into the same modeling style

# Artifact routing

Use this skill to first determine which tactical DDD artifact is being requested, then apply the relevant reference and template.

## Use `references/entities.md` when the concept:
- has a stable identity
- has lifecycle continuity over time
- is not defined only by the value of its properties
- may evolve through domain behaviors or state transitions

Typical examples:
- User
- Order
- Invoice
- Subscription
- ShoppingCart

Prefer these templates when applicable:
- `templates/entity.ts.template.md`
- `templates/entity.spec.ts.template.md`
- `templates/index.ts.template.md`

## Use `references/value-objects.md` when the concept:
- has no conceptual identity
- is defined by the value it carries
- protects one or more business invariants
- should usually be immutable

Typical examples:
- Email
- Money
- Currency
- Slug
- PhoneNumber
- Title
- Percentage

Prefer these templates when applicable:
- `templates/value-object.ts.template.md`
- `templates/value-object.spec.ts.template.md`
- `templates/index.ts.template.md`

## Use `references/aggregates.md` when the concept:
- defines a consistency boundary
- has one aggregate root controlling internal members
- must protect invariants spanning multiple internal objects
- should prevent direct uncontrolled mutation of internal state from outside

Typical examples:
- Order with OrderLines
- Cart with CartItems
- Invoice with line items and totals
- Subscription with controlled lifecycle state

Prefer these templates when applicable:
- `templates/aggregate.ts.template.md`
- `templates/aggregate.spec.ts.template.md`
- `templates/index.ts.template.md`

## Use `references/domain-errors.md` when:
- invalid input violates domain invariants
- a state transition is forbidden by business rules
- a business operation must fail explicitly in the domain layer

Typical examples:
- `InvalidEmailError`
- `InvalidMoneyAmountError`
- `CannotCancelPaidInvoiceError`
- `CannotActivateCancelledSubscriptionError`

Prefer these templates when applicable:
- `templates/domain-error.ts.template.md`
- `templates/index.ts.template.md`

## Use `references/testing.md` for:
- all generated domain tests
- naming test cases
- choosing edge cases
- verifying invariants, normalization, equality, behaviors, and state transitions

Always apply the testing reference when generating or updating domain code.

# Ambiguity handling

If the requested concept is ambiguous:
- prefer asking for clarification when the ambiguity materially changes the model
- otherwise make the safest modeling choice and state it explicitly

Examples:
- a primitive wrapper with validation is usually a value object
- a concept with identity and lifecycle is usually an entity
- a concept coordinating multiple internal members under shared consistency rules is usually an aggregate
- a named business failure is usually a domain error

# Global coding conventions

Generated code should:
- be written in TypeScript
- use explicit types
- use private constructors for entities and value objects unless the user explicitly asks otherwise
- use static factories when construction must enforce invariants
- throw explicit domain-level errors on invalid input or invalid transitions
- separate parsing, validation, normalization, and behavior clearly
- expose only the minimum necessary public surface
- remain focused on domain responsibilities
- reuse existing project primitives, abstractions, and naming conventions when present

# Factories conventions

Use factory methods with explicit responsibilities.

## `create`

Use `create` for new domain-safe creation inside the system.

`create` should:
- enforce invariants
- return a valid domain object
- reject invalid input explicitly

Use `create` only when it has clear domain meaning.
Do not generate it mechanically when `from` alone is sufficient.

## `from`

Use `from` for reconstruction from external or semi-trusted data when needed.

`from` should:
- validate or revalidate input unless the user explicitly wants relaxed reconstruction
- not silently bypass invariants
- make normalization explicit when applicable

Do not add `from` unless external parsing or reconstruction is relevant.

## `rehydrate`

Use `rehydrate` only if the project distinguishes persistence reconstruction from external input parsing.

Do not introduce `rehydrate` unless:
- the user asks for it
- or the codebase already uses this convention

# Aggregates guidance

When generating aggregate-related code:
- ensure there is one clear aggregate root
- expose aggregate behavior through the root only
- protect internal members from uncontrolled direct mutation
- enforce aggregate-wide invariants after every public operation
- keep the consistency boundary as small as the domain allows

Do not create an aggregate only because objects are related.
Create one when shared immediate consistency rules justify a boundary.

# Exceptions and failures

When generated code needs domain failures:
- prefer explicit and intention-revealing exceptions
- use domain-specific names when possible
- make failure reasons readable and actionable

Examples:
- `InvalidEmailError`
- `InvalidMoneyAmountError`
- `CannotCancelPaidInvoiceError`

If the codebase already has a shared domain error base class, reuse it.
Otherwise, do not invent a large hierarchy unless the user asks for it.

Apply `references/domain-errors.md` whenever explicit domain failures are part of the generated behavior.

# Testing conventions

Every generated domain artifact should include unit tests unless the user explicitly asks not to generate them.

Tests should:
- cover happy paths
- cover declared invariants
- cover invalid inputs
- cover important boundary cases
- cover equality semantics
- cover behavior and state transitions when relevant
- cover serialization only when serialization methods exist
- document normalization behavior when normalization exists

Prefer focused tests with explicit names over overly abstract test helpers.

Apply `references/testing.md` for all domain tests.

# Output expectations

After generating code, always report:
- created or modified file paths
- modeling choice made, especially entity vs value object vs aggregate when relevant
- implemented invariants
- normalization rules, if any
- public API surface
- behaviors and state transitions, if any
- domain errors introduced or reused
- tests added or updated
- any uncertainty, assumption, or deviation from project conventions

# File structure

Unless the user asks otherwise, use the following domain structure:

```md
src
+- core
|   +- domain
|   |   +- entities
|   |   +- value-objects
|   |   +- aggregates
|   |   +- errors
```

Each artifact should have its own folder with:
- implementation file
- spec file when relevant
- `index.ts`

If the existing codebase uses a different structure, follow it and state the deviation explicitly.

# How to use references

When generating a specific artifact:
- apply this skill’s general principles first
- identify the correct tactical DDD artifact
- apply the relevant reference file
- apply `references/testing.md` for tests
- use the corresponding template when it fits the requested artifact
- if the reference conflicts with existing project conventions provided by the user, follow the project conventions and state the deviation explicitly

# How to use templates

Templates are accelerators, not rigid blueprints.

When using templates:
- adapt them to the requested domain concept
- remove irrelevant methods rather than filling placeholders mechanically
- do not generate `create`, `from`, `toJSON`, `toString`, or `equals` unless they make sense for the artifact
- align the template output with the reference rules and with the existing codebase conventions
- prefer the simplest shape that correctly models the domain concept

# Recommended templates

Use these templates when appropriate:
- `templates/value-object.ts.template.md`
- `templates/value-object.spec.ts.template.md`
- `templates/entity.ts.template.md`
- `templates/entity.spec.ts.template.md`
- `templates/aggregate.ts.template.md`
- `templates/aggregate.spec.ts.template.md`
- `templates/domain-error.ts.template.md`
- `templates/index.ts.template.md`

# Anti-pattern checks

Before finalizing generated code, check that it does not:
- model a value object as an entity
- model an entity as a primitive wrapper
- model a random object graph as an aggregate without a consistency reason
- expose uncontrolled public mutation
- bypass invariants in public factories
- bypass aggregate-root control for internal state changes
- depend on infrastructure libraries in the domain layer
- add unnecessary abstractions
- produce a fake rich model with no meaningful behavior when the concept is purely structural
- generate tests that only inflate coverage without validating domain rules
