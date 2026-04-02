# Branch Ticket Extraction Reference

## Goal

Extract a ticket identifier from the current branch name when possible.

Expected ticket shape:

```text
PROJ-123
```

Recommended extraction pattern:

```regex
([A-Z][A-Z0-9]+-\d+)
```

## Supported examples

The following branch names should typically yield a ticket:
- `feat/CRM-142-add-customer-email-vo` -> `CRM-142`
- `fix/ORD-88-handle-payment-error` -> `ORD-88`
- `refactor/PLAT-7-clean-ports` -> `PLAT-7`
- `CRM-142-add-customer-email-vo` -> `CRM-142`
- `feature/SHOP-19-cart-duplicate-check` -> `SHOP-19`

## Rules

- prefer the first confidently matched ticket in the branch name
- preserve the extracted ticket exactly as written
- do not invent or normalize a ticket beyond obvious exact extraction
- if no ticket is present, omit the ticket in the commit message

## Usage in commit message

If a ticket is extracted:
- include it in the subject as `[PROJ-123]`
- if a body exists, repeat it on the first body line

Examples:

```text
feat(customer): [CRM-142] introduce email value object
```

```text
fix(order): [ORD-88] reject invalid payment confirmation

[ORD-88] Prevent confirmation when the payment state is inconsistent.
```
