---
name: flutter-widget-testing-patterns
description: Use this skill to apply practical Flutter widget testing patterns for rendering, interaction, state-driven UI, navigation intent, and accessibility-oriented assertions without relying on brittle tree details.
---

# Purpose

This skill provides concrete patterns for Flutter widget tests.

It is intended for:
- screen rendering
- component interactions
- state-driven UI updates
- navigation intent
- semantics and accessibility-oriented assertions
- focused presentation behavior

# Relationship to other skills

Use `flutter-testing` to choose the right seam.

Use this skill once the seam is clearly a widget test.

# Default patterns

## Render through a realistic test harness

Prefer:
- a small `pumpWidget` helper when the project has shared app scaffolding
- wrapping with the required `MaterialApp`, router, localization, or providers
- keeping the test harness stable and reusable

Avoid:
- rebuilding complex boilerplate in every test
- pulling in the entire app when a focused harness is enough

# Assertions

Prefer assertions on:
- visible text
- enabled or disabled state
- user-visible feedback
- semantics and accessibility-relevant labels
- navigation intent or route effects

Avoid:
- asserting incidental widget tree shape
- targeting deep internal structure unless it is the behavior

# Interaction patterns

Prefer:
- `tester.tap`, `enterText`, `drag`, and user-like interactions
- explicit `pump` or `pumpAndSettle` after state changes
- small focused scenarios per test

Avoid:
- giant interaction scripts covering too many concerns
- implicit waiting where explicit pumping would be clearer

# Finders

Prefer:
- `find.text`
- `find.byType` when the type is part of the UI contract
- `find.byKey` when the project uses stable keys intentionally
- semantic or accessibility-oriented finders when available

Avoid:
- depending on brittle positional assumptions
- scattering arbitrary keys just for the tests unless the repo already accepts that pattern

# Navigation and state

For navigation intent:
- assert the visible destination
- assert the router or navigation effect when the harness exposes it clearly

For state-driven UI:
- assert before and after states
- keep the state transition explicit

Avoid:
- hiding several state transitions in one broad test
- testing internal state containers instead of visible outcomes when the widget seam is the right one

# Golden tests

Use golden tests only when:
- visual regression is the primary concern
- the repository already uses them
- the maintenance cost is justified

Do not default to goldens for normal behavior verification.

# Accessibility and semantics

Prefer checking:
- labels
- roles or semantics expectations when exposed
- focus or keyboard-relevant interactions when they matter

Avoid:
- treating accessibility as an afterthought if the widget is interactive

# TDD guidance

When used with `tdd-red-green-refactor`:
- start with a single focused widget behavior
- make RED fail on a visible or semantic outcome
- keep GREEN minimal
- let REFACTOR improve extraction, naming, and harness reuse

# Output expectations

After applying this skill, report:
- widget test pattern selected
- why it is appropriate here
- preferred harness shape
- the most important assertions and interactions to write first
