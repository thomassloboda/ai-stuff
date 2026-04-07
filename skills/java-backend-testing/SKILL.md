---
name: java-backend-testing
description: Use this skill to choose the right test seam and write effective Java backend tests, balancing unit, slice, integration, and contract-level verification without defaulting blindly to one style.
---

# Purpose

This skill helps choose and write the right kind of backend test in a Java codebase.

It is intended for:
- domain and service logic
- Spring or Jakarta web endpoints
- persistence behavior
- messaging adapters
- external gateway clients
- security and validation behavior

When the repository uses Spring heavily, also apply `spring-testing-patterns` for concrete Spring testing patterns after the seam is selected.

When realistic infrastructure behavior is the main risk, also apply `testcontainers-patterns`.

# Core principle

Use the lowest credible test level that proves the behavior.

Do not default blindly to:
- pure unit tests for everything
- full Spring Boot tests for everything
- Testcontainers for everything

The right level depends on what is changing.

# Test seam selection

## Prefer unit tests when the change is mainly:
- domain logic
- policy or rule evaluation
- mapping-free application orchestration
- service behavior that can be exercised behind interfaces

Typical tools:
- JUnit
- AssertJ
- Mockito only when mocking collaborators is clearer than using fakes

## Prefer slice tests when the change is mainly:
- controller behavior -> `@WebMvcTest`
- persistence behavior -> `@DataJpaTest`
- JSON or request/response contract behavior
- validation or serialization at a specific boundary

Slice tests are often the best compromise between confidence and speed.

## Prefer broader integration tests when the change is mainly:
- real database behavior
- transactional boundaries
- messaging integration
- application wiring across several layers
- configuration that matters to correctness

Use realistic infrastructure only where it adds confidence that lower seams cannot provide.

## Prefer contract-oriented tests when the change is mainly:
- HTTP status and payload guarantees
- validation failures
- authorization rules
- external client behavior at the adapter boundary

# Heuristics by layer

## Domain and application core

Prefer:
- fast JUnit tests
- clear business assertions
- minimal framework involvement

Avoid:
- full Spring context when the behavior is pure business logic
- over-mocking internal logic instead of exercising real collaborators where simple fakes exist

## Web layer

Prefer:
- `@WebMvcTest` or equivalent focused controller tests
- assertions on status, payload, validation, and security-relevant behavior

Avoid:
- booting the entire app for every endpoint test unless the wiring itself is the subject

## Persistence and infrastructure

Prefer:
- `@DataJpaTest` for repository behavior
- Testcontainers when SQL dialect, schema behavior, or infrastructure realism matters
- focused adapter-level tests for messaging or external clients

Avoid:
- mocking the database interaction layer so heavily that repository behavior is no longer being tested

# Command guidance

Choose the narrowest command that proves the phase:
- targeted test class first
- then package or broader suite only when needed

Typical examples:
- `./gradlew test --tests com.example.SomeTest`
- `./mvnw -Dtest=SomeTest test`
- `./gradlew integrationTest --tests com.example.SomeIntegrationTest`

Follow project conventions if they already exist.

# Test writing principles

Always:
- name tests by observable behavior
- keep setup focused
- assert meaningful outputs, side effects, or boundary contracts
- cover failure paths when they matter to behavior
- use realistic fixtures where they improve clarity

Avoid:
- asserting private method behavior
- broad boot tests where a slice test would be enough
- excessive Mockito-driven tests that mostly mirror the implementation

# TDD guidance

When used with `tdd-red-green-refactor`:
- choose the seam before RED
- prefer unit or slice tests unless the change truly requires broader integration
- make the RED failure specific and behavior-focused
- keep GREEN minimal
- use REFACTOR to improve naming, extraction, duplication, and boundary clarity

# Output expectations

After applying this skill, report:
- chosen test seam
- why that seam is appropriate
- expected test location pattern
- preferred verification command
- key assertions the test should focus on
