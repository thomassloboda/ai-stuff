---
name: flutter-testing
description: Use this skill to choose the right test seam and write effective Flutter tests, balancing unit, widget, integration, and platform-boundary verification without defaulting blindly to one style.
---

# Purpose

This skill helps choose and write the right kind of test in a Flutter codebase.

It is intended for:
- pure Dart domain or utility logic
- state management behavior
- widget rendering and interactions
- navigation flows
- repository and gateway adapters
- plugin or platform-channel boundaries

When the chosen seam is a widget test, also apply `flutter-widget-testing-patterns` for concrete widget testing patterns.

When the chosen seam is an integration test, also apply `flutter-integration-testing-patterns` for concrete integration testing patterns.

# Core principle

Use the lowest credible test level that proves the behavior.

Do not default blindly to:
- unit tests for everything
- widget tests for everything
- `integration_test` for everything

The right level depends on what is changing.

# Test seam selection

## Prefer unit tests when the change is mainly:
- pure Dart logic
- value parsing or formatting
- domain rules
- state transitions that do not need the widget tree
- small services that can be exercised without Flutter bindings

## Prefer widget tests when the change is mainly:
- rendering
- user interaction with one screen or component
- view-model and UI wiring
- navigation intent that can be exercised inside the test harness
- state-driven UI transitions

## Prefer integration tests when the change is mainly:
- full user journeys across several screens
- router configuration that matters end to end
- platform integration that lower-level seams cannot credibly prove
- lifecycle behavior that requires a near-real app environment

## Prefer targeted boundary tests when the change is mainly:
- plugin wrappers
- platform channels
- external SDK integration
- persistence or HTTP adapters

These often combine focused unit or widget tests with a smaller number of broader integration checks.

# Heuristics by layer

## Pure Dart / domain / application logic

Prefer:
- fast unit tests
- explicit failure-path coverage
- deterministic assertions

Avoid:
- spinning up widgets when the widget tree adds no confidence
- mocking so much that the real logic disappears

## Presentation and interaction

Prefer:
- widget tests for user-visible behavior
- assertions on visible state, semantics, navigation intent, and interaction outcomes

Avoid:
- asserting internal widget implementation details
- relying on brittle tree shape when user-facing behavior is what matters

## Integration and platform boundaries

Prefer:
- a small number of integration tests for true cross-boundary risk
- focused tests around plugin wrappers or platform adapters

Avoid:
- pushing every behavior into `integration_test`
- using broad end-to-end tests as a substitute for clear lower-level coverage

# Command guidance

Choose the narrowest command that proves the phase:
- targeted file or target first
- then broader suite only when needed

Typical examples:
- `flutter test test/path/to/file_test.dart`
- `dart test test/path/to/file_test.dart`
- `flutter test integration_test/path/to/file_test.dart`

Follow project conventions if they already exist.

# Test writing principles

Always:
- name tests by behavior
- keep Arrange / Act / Assert obvious
- assert visible outcomes, state transitions, or contract behavior
- keep test setup readable
- prefer deterministic timing and explicit pumping

Avoid:
- fragile assertions on incidental widget structure
- giant integration flows covering too many concerns
- excessive mocking of Flutter or state management internals

# TDD guidance

When used with `tdd-red-green-refactor`:
- choose the seam before RED
- prefer unit or widget tests unless the behavior genuinely requires broader integration
- make the RED failure specific
- keep GREEN minimal
- let REFACTOR improve naming, extraction, duplication, or widget/service boundaries

# Output expectations

After applying this skill, report:
- chosen test seam
- why that seam is appropriate
- expected test location pattern
- preferred verification command
- key assertions the test should focus on
