---
name: code-review
description: Use this skill to perform high-signal code review on diffs or pull requests, focusing on correctness, design, architecture, tests, maintainability, and optional Sonar-style quality concerns.
---

# Purpose

This skill helps review code changes thoroughly.

It applies to:
- local diffs
- pull requests
- heavy refactors
- architecture-sensitive changes
- domain changes
- changes with test or quality implications

# Review goals

Look for:
- correctness issues
- regression risks
- missing or weak tests
- architecture violations
- dependency direction problems
- unclear naming or API design
- maintainability concerns
- hidden complexity
- Sonar-style quality concerns when applicable

# Severity model

Classify findings using this scale:
- Blocking: likely bug, regression, unsafe architecture issue, or missing essential test coverage
- Important: maintainability or design issue that should likely be fixed before merge
- Suggestion: improvement that is helpful but not required
- Question: genuine ambiguity that should be clarified

# Sonar-style concerns

When relevant, inspect for:
- duplicated logic
- overly complex conditionals
- long methods with mixed responsibilities
- weak error handling
- nullability blind spots
- confusing nesting
- dead code or unused branches
- low-signal logging
- missing failure-path tests
- inconsistent naming

Use Sonar-style reasoning as a complement, not as a substitute for domain and architecture judgment.

# Review principles

Always:
- read enough surrounding code to understand context
- explain why a finding matters
- prefer specific recommendations over generic remarks
- distinguish actual issues from stylistic preferences
- mention positive signals when they are meaningful

Avoid:
- nitpicking already automated style rules
- speculative criticism with no code evidence
- repeating the same issue several times

# Skill interplay

Use `typescript-ddd-development` when reviewing domain modeling.
Use `typescript-hexagonal-architecture` when reviewing boundaries, ports, adapters, and dependency direction.
Use this skill for the review method itself.
