# Barrel Files Reference

## Goal

Enforce or preserve the project's barrel-file policy where it is part of the architecture conventions.

## When barrel checks matter

Use barrel enforcement when the project expects:
- `index.ts` files in exposable folders
- imports through public folder boundaries instead of arbitrary deep paths
- stable public APIs for modules or subtrees

## What to verify

Examples:
- a folder under `src/core/domain/value-objects/email/` should expose its public surface through `index.ts`
- a folder under `src/application/use-cases/create-customer/` may expose its public use case entry through `index.ts`
- imports should not bypass a required barrel if the project treats it as the public contract

## Keep it pragmatic

Do not enforce barrel files everywhere mechanically.
Only enforce them where the project structure and conventions explicitly rely on them.
