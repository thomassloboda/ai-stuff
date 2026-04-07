---
name: testcontainers-patterns
description: Use this skill to apply practical Testcontainers patterns for Java backend tests when realistic infrastructure behavior matters more than fast isolated slices.
---

# Purpose

This skill provides concrete patterns for using Testcontainers effectively in Java backend tests.

It is intended for:
- repository integration tests
- persistence behavior that depends on the real database
- migration or schema verification
- messaging infrastructure integration
- infrastructure-dependent Spring Boot tests

# Relationship to other skills

Use `java-backend-testing` to decide whether realistic infrastructure is actually needed.

Use `spring-testing-patterns` when the repository is Spring-based and the seam is already known.

Use this skill only when a real containerized dependency adds confidence that lower-level seams cannot provide.

# When Testcontainers is justified

Prefer Testcontainers when:
- SQL dialect behavior matters
- indexes, constraints, or transaction behavior matter
- schema migration behavior matters
- repository behavior depends on real infrastructure semantics
- messaging or broker behavior is important to correctness

Do not use Testcontainers by default for:
- pure service logic
- controller validation
- simple repository tests that a focused slice can prove without real infra
- tests where the infrastructure realism adds little compared with the startup cost

# Core principles

Always:
- keep the test focused on the infrastructure risk being validated
- use the smallest realistic container setup that proves the behavior
- reuse shared setup patterns when the project already has them
- prefer stable container configuration over clever dynamic wiring

Avoid:
- booting several containers for one narrow assertion unless the behavior truly depends on them
- mixing too many behavioral concerns into one container-backed test
- hiding slow broad tests inside suites that developers expect to stay fast

# Common patterns

## Database-backed repository test

Use when validating:
- custom SQL behavior
- JPA mapping behavior
- transaction semantics
- migration compatibility

Prefer:
- one repository concern per test or per small test group
- explicit seed data
- assertions on persisted outcomes

## Full Spring integration with real database

Use when validating:
- several layers together
- real wiring plus real persistence
- behavior that lower slices cannot credibly prove

Prefer:
- one realistic dependency first
- explicit test data setup
- narrow scenario coverage

Avoid:
- turning every service or controller test into a container-backed integration test

## Messaging or external infrastructure

Use when validating:
- broker integration
- consumer or producer behavior
- serialization against real infrastructure expectations

Prefer:
- adapter-focused tests
- contract-level assertions
- realistic but narrow end-to-end scenarios

# Lifecycle patterns

Prefer:
- shared container setup when the repository already standardizes on it
- clear startup and teardown ownership
- deterministic property injection

In Spring-heavy projects, prefer readable property wiring over magic.

# Performance guidance

Always consider:
- whether the same confidence can be achieved with a cheaper seam
- how often the test should run locally
- whether the suite needs separation between fast and infra-backed tests

If the project distinguishes unit, integration, or infrastructure suites, follow that convention.

# TDD guidance

When used with `tdd-red-green-refactor`:
- do not choose Testcontainers unless the requested behavior truly depends on realistic infrastructure
- if chosen, keep RED narrow and meaningful
- keep GREEN focused on the missing behavior, not on broad environment setup
- keep REFACTOR focused on fixture clarity, setup reuse, and test intent

# Output expectations

After applying this skill, report:
- why Testcontainers is justified here
- which dependency should be containerized
- the narrowest realistic test scope
- the key assertions that make the container worthwhile
