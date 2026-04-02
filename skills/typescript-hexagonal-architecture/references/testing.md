# Hexagonal Architecture Testing Reference

## Purpose

This reference defines the minimum testing discipline for code generated under the hexagonal architecture.

## Rule

Everything created or modified must be tested at the appropriate level.

Do not leave artifacts untested.

## Minimum expectations by artifact type

### Domain artifacts
- unit tests

### Use cases
- unit tests
- verify happy paths and important failures
- verify interactions with required ports when relevant

### Ports
- usually tested indirectly through use cases and adapters
- explicit contract tests may be added when useful

### In-memory adapters
- unit tests

### Persistence adapters
- adapter-focused tests
- integration or contract-oriented tests when appropriate

### REST adapters
- request/response mapping tests
- controller or handler behavior tests

### Third-party adapters
- boundary and mapping tests
- failure behavior tests when relevant

## Test placement

Prefer colocated `*.spec.ts` files unless the project already uses another convention.

## Regression discipline

When fixing a bug:
- add or update a test that proves the bug is fixed

## Barrel-file changes

When module exposition changes:
- update relevant `index.ts` files
- verify imports through tests or compilation checks when possible
