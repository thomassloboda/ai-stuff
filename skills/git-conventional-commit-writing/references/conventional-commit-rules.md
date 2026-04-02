# Conventional Commit Rules Reference

## Expected format

The expected subject format is:

```text
type(scope-optional): [PROJ-123] short description
```

Examples:
- `feat(customer): [CRM-142] introduce email value object`
- `fix(order): [ORD-88] prevent invalid payment state transition`
- `refactor: [PLAT-7] simplify hexagonal port wiring`
- `test(cart): [SHOP-19] cover duplicate item rejection`

When no ticket can be extracted confidently:
- `feat(customer): add email value object`
- `refactor: simplify port registration`

## Subject rules

The subject should:
- use a valid conventional commit type
- include an optional scope only when meaningful
- include the ticket only when confidently extracted
- be imperative
- be concise
- describe intent, not low-level implementation details
- not end with a period

Prefer:
- `feat(customer): [CRM-142] introduce email value object`
- `fix(order): [ORD-88] reject invalid payment confirmation`

Avoid:
- `chore: stuff`
- `fix: changed code`
- `feat(customer): [CRM-142] add email value object and tests and refactor some stuff`

## Body rules

The body is optional.
Use it when the change benefits from extra context.

If a ticket exists and a body is present, the first body line must repeat the ticket:

```text
[CRM-142] Add a dedicated Email value object and wire it into Customer creation.
```

The body should:
- explain why the change exists
- summarize major effects when useful
- stay concise
- avoid repeating the subject verbatim without adding information

## Type guidance

Use:
- `feat` for a new capability or feature
- `fix` for a bug fix
- `refactor` for structural improvement without intended functional change
- `test` for test-only changes
- `docs` for documentation-only changes
- `chore` for maintenance work
- `build` for build and dependency system changes
- `ci` for CI or pipeline changes
- `perf` for performance improvements

Choose the most meaningful type rather than the safest generic type.
