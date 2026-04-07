# Prompts V2

This repository keeps one focused responsibility per skill and a small set of orchestration-oriented agents.

## Core V2 rules

- every agent must answer in the user's language
- every agent must keep working until the task is either completed or concretely blocked
- skills stay orthogonal and composable rather than being merged into one giant prompt
- when `agent/runSubagent` is available, delegation is allowed but must stay bounded and reviewable

## Separation of concerns

- `typescript-ddd-development` defines what the domain model should be
- `typescript-hexagonal-architecture` defines where artifacts belong and which dependencies are allowed
- agents orchestrate work and decide when to combine skills

Keeping DDD and Hexagonal Architecture separate is intentional in V2.

## TDD workflow

The repository can also use a generic TDD workflow:
- `tdd-red-green-refactor` defines the workflow and phase gates
- stack-specific testing skills define the right seam and test style

For example:
- `typescript-backend-testing` explains how to choose between unit, integration, and API-level tests in a TypeScript backend
- `flutter-testing` explains how to choose between unit, widget, and integration tests in Flutter
- `java-backend-testing` explains how to choose between unit, slice, and integration tests in Java backends

The workflow should stay generic.
What varies by stack is the testing strategy, not the Red-Green-Refactor cycle itself.

When a stricter execution model is helpful, `ts-beast-tdd-orchestrator` can coordinate the three dedicated phase agents explicitly.

## Language policy

Every agent should include an explicit instruction equivalent to:

```md
Always use the user's language.
```

This must be stated directly in the agent prompt, not only assumed implicitly.

## Delegation policy

Agents that declare `agent/runSubagent` should include an explicit delegation policy.

Recommended policy:
- keep ownership of the main task and final synthesis
- delegate only bounded subtasks
- prefer parallel evidence gathering, isolated drafting work, or side investigations
- do not delegate the immediate next blocking step when local execution is faster
- validate and integrate subagent output before replying

## Linter expectations

The prompt linter checks at least:
- frontmatter presence and required keys
- missing referenced skills
- explicit user-language directive in every agent
- explicit delegation policy for agents that declare `agent/runSubagent`
- stale tool aliases that no longer match the declared tool surface

Run it with:

```bash
python3 scripts/prompt_lint.py
```
