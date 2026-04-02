# Task Decomposition Reference

## Goal

Turn migration findings into very small technical tasks that can usually fit into one focused pull request.

## Rules

Each task should:
- express one technical change only
- have one obvious review focus
- impact as few files as possible
- avoid unrelated cleanup
- preserve behavior unless explicitly stated otherwise

## Good task patterns

Examples:
- introduce a secondary port interface
- implement a Mongoose adapter for one repository
- extract one use case from one Nest service
- move one set of mapping functions to the edge layer
- add one architecture test for one forbidden dependency direction
- replace one direct model access path with one port usage path

## Poor task patterns

Avoid:
- migrate module X to hexagonal architecture
- clean all service responsibilities
- refactor all persistence code
- remove all framework coupling

## Ticket title guidance

Prefer titles such as:
- Extract `CreateOrderUseCase` from `OrderService`
- Introduce `CustomerRepository` secondary port
- Move direct Mongoose access behind `CustomerMongoRepository`
- Isolate REST DTO mapping for customer creation
- Add architecture test forbidding core-to-infrastructure imports

## Scope boundary guidance

Explicitly state what is not in scope for a task.

Examples:
- do not update controllers in this task
- do not remove the old service yet
- do not migrate read paths in this task
- do not modify unrelated repository methods

## Dependency representation

For each task, state:
- prerequisite ticket or task if any
- whether it can be parallelized
- whether it unlocks follow-up work
