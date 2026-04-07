---
name: tdd-red-green-refactor
description: Use this skill to enforce a strict Red-Green-Refactor cycle with isolated agents, explicit phase gates, and proof at each step before implementation proceeds.
---

# Purpose

This skill enforces a real Test-Driven Development workflow for new behavior.

It is intended for:
- new features
- new behavior in existing modules
- behavior changes that deserve regression protection
- implementation work where the safest path is to prove behavior first

It is not the default for:
- pure refactors with no behavior change
- documentation-only changes
- configuration-only changes
- emergencies where reproducing the issue is impossible and a different debugging workflow is needed

# Core idea

Do not let one agent drift across all TDD phases in a single context.

Instead:
- isolate RED, GREEN, and REFACTOR
- require proof before moving to the next phase
- keep the implementation agent focused on the failing test only
- keep the refactor phase explicit rather than optional cleanup

# Mandatory workflow

Every behavior slice must complete this cycle:

1. Select the test seam.
2. RED: write a failing test and verify it fails.
3. GREEN: implement the minimum code and verify the test passes.
4. REFACTOR: improve the code or explicitly report that no refactor is justified.

Do not skip phases.
Do not start the next behavior slice until the current one completes.

# Step 0: Select the test seam

Before RED, decide what test level best captures the behavior.

Use the lowest credible level that still proves the requirement:
- domain rule or pure business logic -> unit test
- application orchestration or use case -> unit or focused integration test
- adapter or repository contract -> integration test
- HTTP contract or route behavior -> integration test
- full end-to-end user journey -> end-to-end test only when lower levels are insufficient

Do not force integration tests everywhere.

When a stack-specific testing skill exists, apply it before writing the test.

For TypeScript backend work, use `typescript-backend-testing`.

# RED phase

Delegate RED to a dedicated test-writer agent.

Input should include:
- the requested behavior
- the selected test seam
- the most relevant test command
- any stack-specific testing guidance

RED is complete only when the agent returns:
- the test file path
- the failure output or failure summary
- a short explanation of what behavior the test verifies

Do not proceed to GREEN unless the test actually fails for the right reason.

# GREEN phase

Delegate GREEN to a dedicated implementer agent.

Input should include:
- the failing test file path
- the requested behavior
- any constraints discovered in RED

GREEN is complete only when the agent returns:
- the files modified
- proof that the targeted test now passes
- a summary of the minimal implementation

The implementer must not add extra behavior beyond what the failing test requires.

# REFACTOR phase

Delegate REFACTOR to a dedicated refactorer agent.

Input should include:
- the test file path
- the modified implementation files
- any relevant project conventions

REFACTOR is complete only when the agent returns one of:
- a list of improvements made plus proof tests still pass
- "No refactoring needed" with a short, concrete reason

Skipping the evaluation step is not allowed.

# Phase gates

Never:
- implement before a failing test exists
- move to GREEN without proof of RED
- move to REFACTOR without proof of GREEN
- silently modify the test in GREEN to avoid fixing the implementation
- hide a skipped refactor behind a vague success statement

# Output expectations

When orchestrating the full cycle, report:
- chosen test seam
- RED result
- GREEN result
- REFACTOR result
- whether the behavior slice is complete

For multiple requested behaviors, complete the full cycle once per behavior slice.

# Generalization guidance

This workflow is intentionally stack-agnostic.

What changes per stack is not the TDD cycle itself, but:
- where tests live
- which test level is preferred
- which commands verify the phase
- which project conventions define a "good" test

Use stack-specific testing skills for that layer of guidance.

# Communication principles

Always:
- use the user's language
- be explicit about phase boundaries
- require proof, not assumptions
- keep each phase narrow and auditable

Avoid:
- blending phases into one implementation pass
- over-engineering the first passing implementation
- forcing one test style on every stack
