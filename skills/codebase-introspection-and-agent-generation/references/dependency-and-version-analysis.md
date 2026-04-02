# Dependency and Version Analysis Reference

## Goal

Detect the important dependencies used by the repository and highlight version-sensitive decisions.

## What to capture

Capture:
- package manager
- runtime or language version when available
- framework versions
- ORM or persistence tooling
- test framework versions
- lint, format, static analysis, and coverage tooling
- observability tooling
- build and deployment tooling

## Rules

- Prefer lock files or resolved dependency data when available.
- If exact versions are not easy to determine, state that clearly.
- Verify framework behavior with docs when implementation details could differ by version.
- Do not list every dependency. Focus on the ones that shape architecture, development flow, testing, quality, and runtime behavior.
