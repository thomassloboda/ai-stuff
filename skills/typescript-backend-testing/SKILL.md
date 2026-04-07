---
name: typescript-backend-testing
description: Use this skill to choose the right test seam and write effective backend tests in TypeScript, balancing unit, integration, and API-level verification without defaulting blindly to one style.
---

# Purpose

This skill helps choose and write the right kind of backend test in a TypeScript codebase.

It is intended for:
- domain logic
- application use cases
- repositories and persistence adapters
- HTTP routes and controllers
- event handlers and message-driven flows
- external gateway adapters

# Core principle

Use the lowest credible test level that proves the behavior.

Do not default blindly to:
- unit tests for everything
- integration tests for everything
- end-to-end tests for everything

The right level depends on what is changing.

# Test seam selection

## Prefer unit tests when the change is mainly:
- pure domain logic
- value object validation
- entity or aggregate behavior
- application orchestration that can be exercised through ports
- mapping-free business rules

## Prefer focused integration tests when the change is mainly:
- repository behavior
- database interaction
- framework wiring that matters to correctness
- adapter behavior
- serialization or deserialization boundaries
- route handling or middleware interactions

## Prefer API-level tests when the change is mainly:
- HTTP status codes
- request validation
- response contracts
- route authorization or authentication behavior
- endpoint-level orchestration

## Prefer broader end-to-end coverage only when:
- the behavior spans several boundaries that cannot be credibly proven lower
- the user journey itself is the main requirement
- lower-level seams would miss integration risk that matters here

# Heuristics by architecture layer

## Domain

For:
- entities
- value objects
- aggregates
- domain errors

Prefer:
- fast unit tests
- explicit invariant coverage
- failure-path assertions

Avoid:
- framework bootstrapping
- real persistence
- mocking the domain heavily

## Application

For:
- use cases
- command handlers
- query handlers
- orchestration services

Prefer:
- unit tests against ports
- in-memory or fake adapters when that keeps the test honest

Add integration coverage only when framework wiring or adapter interaction is central to the behavior.

## Infrastructure

For:
- repositories
- external gateways
- queue consumers or publishers
- HTTP adapters

Prefer:
- focused integration tests at the adapter boundary
- contract-oriented assertions

When persistence matters, use realistic infrastructure or project-standard test doubles rather than brittle mocks of implementation details.

# Command guidance

Choose the narrowest command that proves the phase:
- targeted single-test-file command first
- then broader suite only when needed

Examples vary by repository:
- `pnpm test -- <file>`
- `npm test -- <file>`
- `vitest run <file>`
- `jest <file>`

Follow project conventions if they already exist.

# Test writing principles

Always:
- name tests by behavior, not by implementation mechanics
- make failure reasons obvious
- keep Arrange / Act / Assert easy to read
- assert observable outcomes
- include failure-path coverage when behavior can fail meaningfully

Avoid:
- testing private implementation details
- excessive mocking that removes the real behavior under test
- giant integration tests that verify too many concerns at once
- asserting incidental formatting or structure when behavior is what matters

# TDD guidance

When used with `tdd-red-green-refactor`:
- decide the seam before RED
- make the RED failure specific and meaningful
- keep GREEN minimal
- let REFACTOR improve naming, extraction, duplication, or boundary clarity

# Output expectations

After applying this skill, report:
- chosen test seam
- why that seam is appropriate
- expected test location pattern
- preferred verification command
- key assertions the test should focus on
