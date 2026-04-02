# Domain Errors Reference

## Definition

A domain error represents an explicit business failure in the domain layer.

It should be used when:
- an input violates a domain invariant
- a state transition is forbidden by business rules
- a domain operation cannot be completed because business conditions are not met

A domain error is not:
- a transport error
- an infrastructure error
- a framework validation artifact
- a generic fallback for any thrown exception

Examples:
- `InvalidEmailError`
- `InvalidMoneyAmountError`
- `CannotCancelPaidInvoiceError`
- `SubscriptionAlreadyExpiredError`

## Purpose

Domain errors should help the code express business rules clearly.

They should:
- make failures explicit
- improve readability
- make tests more precise
- avoid vague `Error` throws with unclear intent
- stay focused on domain meaning

## Modeling rules

Domain errors should:
- live in the domain layer
- use intention-revealing names
- represent real business failures
- be small and explicit
- be framework-agnostic
- be easy to assert in tests

Prefer named domain errors over anonymous `Error` instances when the failure has business meaning.

## Naming conventions

Use names that describe the violated rule or forbidden action.

Prefer:
- `InvalidEmailError`
- `InvalidOrderStatusError`
- `CannotActivateCancelledSubscriptionError`
- `CannotAssignClosedTicketError`

Avoid vague names such as:
- `ValidationError`
- `BusinessError`
- `DomainProblem`
- `SomethingWentWrongError`

A generic base class is acceptable when the codebase needs one, but leaf errors should remain explicit.

## Base class policy

If the project already uses a shared domain base class, reuse it.

Example:
- `DomainError`
- `DomainInvariantError`
- `InvalidStateTransitionError`

If no shared base exists:
- do not invent a complex hierarchy unless the user asks for it
- a simple custom error class per failure is acceptable
- a small common `DomainError` base class is acceptable if it clearly improves consistency

Do not build a deep inheritance tree without a real need.

## Recommended shape

A domain error should usually:
- extend `Error` directly, or extend a small shared domain base class
- set a clear message
- set a stable error name
- optionally carry structured context when genuinely useful

Structured context may be useful for:
- current state
- attempted transition
- invalid value
- violated limit

But avoid turning errors into generic data bags.

## Message conventions

Error messages should:
- be explicit
- describe the business failure
- be readable in logs and tests
- avoid leaking infrastructure details

Prefer:
- `Email must not be blank`
- `Invoice cannot be cancelled after payment`
- `Percentage must be between 0 and 100`

Avoid:
- `Invalid input`
- `Validation failed`
- `Unexpected value`
- low-level parser or framework jargon

## When to create a dedicated domain error

Create a dedicated domain error when:
- the business rule is meaningful on its own
- the same failure may be asserted in tests or handling code
- naming the error improves readability materially

A plain `Error` with a precise message may be acceptable when:
- the project keeps domain errors lightweight
- the failure is highly local
- there is no benefit in naming the class separately

When in doubt, prefer explicit named domain errors for reusable or important domain rules.

## Validation failures vs transition failures

Distinguish clearly between:
- invalid value or invariant failures
- invalid lifecycle or state transition failures

Examples:
- `InvalidEmailError`
- `InvalidDateRangeError`
- `CannotPublishArchivedPostError`
- `CannotCancelPaidInvoiceError`

This distinction improves both code clarity and test intent.

## Placement

Unless the project uses another convention, place domain errors under:

```md
src
+- core
|   +- domain
|   |   +- errors
|   |   |   +- {error_name}
|   |   |   |   +- {error_name}.ts
|   |   |   |   +- index.ts
```

If the codebase prefers feature-local errors, colocate them with the related entity or value object instead.

Examples:
- next to `email.ts` for `InvalidEmailError`
- next to `invoice.ts` for `CannotCancelPaidInvoiceError`

Follow existing project conventions when provided.

## Usage guidance

Use domain errors:
- in entity factories
- in value object factories
- in invariant checks
- in state transition guards
- in domain services when domain rules fail

Do not use domain errors for:
- database connectivity issues
- HTTP transport failures
- serialization library failures
- framework validation adapter concerns

These belong outside the domain layer.

## Public API impact

When a domain artifact can throw a domain error:
- make the failure mode understandable from the method semantics
- use names and tests to document it clearly
- avoid hidden or surprising failure reasons

Do not add checked-style boilerplate patterns unless the user asks for result objects or discriminated unions.

## Testing

Tests for domain errors should cover:
- correct failure type
- correct failure condition
- meaningful message when messages are part of the convention
- optional structured context when present

Prefer assertions such as:
- the exact error class
- the exact business condition that triggers it

Do not write brittle tests over stack traces or engine-specific formatting.

## Anti-patterns

Do not:
- throw generic `Error` everywhere for domain failures
- leak framework validators into the domain model
- create a huge error hierarchy without need
- model infrastructure failures as domain errors
- use vague names with no business meaning
- hide important business rules inside generic messages
