---
name: flutter-integration-testing-patterns
description: Use this skill to apply practical Flutter integration testing patterns for true multi-screen, platform-relevant, or end-to-end flows without overusing broad device-level tests.
---

# Purpose

This skill provides concrete patterns for Flutter integration tests.

It is intended for:
- multi-screen user journeys
- app-level routing and navigation flows
- platform-relevant behavior that widget tests cannot credibly prove
- cross-boundary scenarios spanning several layers

# Relationship to other skills

Use `flutter-testing` to decide whether an integration test is actually justified.

Use this skill only when the seam has already been chosen as integration-level verification.

# When integration tests are justified

Prefer integration tests when:
- the behavior spans several screens
- router and navigation behavior matter end to end
- platform or plugin integration matters
- state restoration or lifecycle behavior matters
- lower-level unit or widget seams would miss the real risk

Do not default to integration tests for:
- isolated widget rendering
- simple interaction within one component
- pure Dart logic
- behavior already well covered by unit or widget tests

# Core principles

Always:
- keep the scenario focused on one meaningful journey
- assert user-visible outcomes
- minimize incidental setup noise
- prefer deterministic app state before starting the journey

Avoid:
- giant kitchen-sink journeys
- fragile timing assumptions
- mixing several business concerns into one long script
- using integration tests as a substitute for missing widget tests

# Common patterns

## Multi-screen journey

Use when validating:
- a user starts on one screen, performs actions, and ends on another
- navigation and state transitions together define the requirement

Prefer:
- explicit start state
- short action sequence
- assertions on the destination and visible outcomes

## Platform or plugin-relevant flow

Use when validating:
- a plugin wrapper is exercised through the app flow
- device or platform interaction matters to correctness

Prefer:
- limiting the scenario to the boundary that matters
- combining lower-level tests with one or two broad integration checks

## Cross-layer behavior

Use when validating:
- presentation, state, navigation, and adapter behavior together
- a real journey where several seams must cooperate

Prefer:
- one journey per requirement
- test names that read like user behavior

# Harness and setup

Prefer:
- consistent app bootstrapping helpers
- deterministic seed state
- explicit cleanup and reset strategy

Avoid:
- duplicating app setup boilerplate in every test
- hidden global state that makes failures hard to interpret

# Assertions

Prefer assertions on:
- visible content
- navigation results
- enabled or disabled state
- semantics or accessibility-relevant behavior when interactive elements matter

Avoid:
- over-asserting internal implementation details
- relying on incidental ordering or timing when the behavior is what matters

# TDD guidance

When used with `tdd-red-green-refactor`:
- choose integration tests only when widget tests are not enough
- make RED fail on a user-visible or journey-level outcome
- keep GREEN focused on the missing behavior
- let REFACTOR improve harness reuse, state setup clarity, and journey readability

# Output expectations

After applying this skill, report:
- why an integration test is justified here
- the user journey to verify
- the preferred harness or setup pattern
- the most important visible assertions to write first
