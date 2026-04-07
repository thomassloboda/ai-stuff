---
name: spring-testing-patterns
description: Use this skill to apply practical Spring testing patterns for controllers, services, repositories, security, and infrastructure seams with the right balance between slice tests, integration tests, and realistic fixtures.
---

# Purpose

This skill provides concrete testing patterns for Spring-based Java backends.

It is intended for:
- Spring MVC controllers
- request validation
- security behavior
- JPA repositories
- service orchestration
- transactional behavior
- Spring wiring that matters to correctness

# Relationship to other skills

Use `java-backend-testing` to choose the right seam.

Use this skill once the seam is known and the codebase uses Spring patterns.

When the selected Spring test really needs real infrastructure behavior, also apply `testcontainers-patterns`.

# Default patterns

## Controller boundary

Prefer `@WebMvcTest` when testing:
- request routing
- status codes
- request validation
- serialization and deserialization
- controller-level security behavior

Typical tools:
- `MockMvc`
- `ObjectMapper`
- focused mocked collaborators only at the controller boundary

Prefer assertions on:
- HTTP status
- response payload
- validation errors
- headers when meaningful

Avoid:
- booting the full application when controller slice coverage is enough
- asserting incidental JSON formatting details that do not matter to the contract

# Service and application logic

Prefer plain JUnit tests for:
- orchestration logic
- business decisions
- branching behavior
- collaboration with ports or interfaces

Use Spring context only when framework wiring itself is part of the behavior under test.

Avoid:
- wrapping every service test in Spring Boot
- overusing Mockito where a simple fake would make intent clearer

# Persistence

Prefer `@DataJpaTest` when testing:
- custom queries
- mapping behavior
- constraints
- transactional repository behavior

Prefer Testcontainers when:
- database-specific behavior matters
- SQL dialect differences matter
- schema migrations or realistic infra behavior are part of the risk

Avoid:
- mocking repositories while pretending to test persistence behavior
- using full application boot just to verify one repository query

# Security

Prefer focused tests for:
- authorization rules
- authentication-dependent controller behavior
- role-based or claim-based access decisions

Typical patterns:
- request-level tests with `MockMvc`
- explicit authenticated and unauthenticated cases
- explicit forbidden and allowed paths

Avoid:
- assuming security works because the happy path is covered
- mixing too many concerns into one security test

# Full integration

Prefer `@SpringBootTest` only when:
- several layers must be proven together
- configuration wiring is central to the behavior
- lower-level seams cannot credibly prove the requirement

Use it sparingly.

When used:
- keep the scenario focused
- combine with realistic fixtures
- avoid turning each test into an end-to-end system test

# Test data guidance

Prefer:
- builders or fixture helpers
- readable defaults
- explicit overrides for the behavior under test

Avoid:
- giant inline setup blocks repeated across tests
- obscure fixture factories that hide what matters

# TDD guidance

When used with `tdd-red-green-refactor`:
- choose `@WebMvcTest` for controller contracts before reaching for `@SpringBootTest`
- choose plain JUnit for domain and service logic before reaching for Spring slices
- choose `@DataJpaTest` for repository behavior before broader boot tests
- choose Testcontainers when persistence realism is the real risk, not by habit

# Output expectations

After applying this skill, report:
- Spring testing pattern selected
- why it is appropriate here
- preferred annotations or tools
- the most important assertions to write first
