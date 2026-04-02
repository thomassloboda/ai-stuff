# Worktree Analysis Reference

## Goal

Analyze the current git worktree to determine:
- whether to base the proposal on staged changes or the full worktree
- the dominant intention of the changes
- the best conventional commit type
- an optional scope
- whether one commit or multiple commits are more appropriate

## Preferred inputs

Prefer inspecting, when available:
- current branch name
- `git status --short`
- `git diff --staged --name-only`
- `git diff --staged`
- `git diff --name-only`
- `git diff`

If staged changes exist, prefer them for the commit proposal.
If nothing is staged, analyze the full worktree and say so explicitly.

## Single vs multiple commit decision

Propose a single commit when the changes are cohesive and support one dominant intention.

Examples:
- adding one value object and its tests
- fixing one bug across related files
- refactoring one module without unrelated changes

Propose multiple commits when the worktree mixes unrelated intentions.

Examples:
- one feature plus unrelated formatting cleanup
- refactor plus separate CI changes
- test changes for unrelated modules mixed together
- documentation updates bundled with infrastructure rewiring

## Type heuristics

Use the dominant change intent.

Examples:
- domain capability added -> `feat`
- incorrect behavior corrected -> `fix`
- internal restructuring without intended behavior change -> `refactor`
- tests only -> `test`
- docs only -> `docs`
- tooling or housekeeping only -> `chore`
- CI pipeline only -> `ci`
- dependency or build system changes -> `build`
- performance-focused change -> `perf`

## Scope heuristics

Choose a scope when a clear dominant area exists, such as:
- a domain concept like `customer`, `order`, `cart`
- a technical surface like `ports`, `mongodb`, `rest`, `sqlite`
- a module or bounded area clearly dominating the diff

Prefer omitting the scope over using a weak or misleading scope.

## Message quality checks

Before finalizing:
- confirm the subject reflects the dominant intention
- keep the subject short and readable
- remove low-level implementation noise
- avoid vague wording such as `update`, `change`, `stuff`, or `misc`
