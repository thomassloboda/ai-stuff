---
name: hexagonal-migration-planning
description: Use this skill to analyze an existing codebase that is only partially hexagonal and produce a fine-grained, low-risk migration plan toward a ports-and-adapters architecture.
---

# Purpose

This skill helps analyze a codebase that started with a framework-first or persistence-coupled architecture and is being progressively migrated toward hexagonal architecture.

It is intended for:
- identifying modules or areas that are not yet hexagonal
- detecting architectural violations and migration gaps
- defining the target shape for partially migrated code
- decomposing migration work into small technical tasks
- producing ticket-ready technical backlog items

This skill is especially useful for codebases where both old and new architectural styles coexist.

# General principles

Always:
- analyze the current implementation before proposing migration work
- compare current state against the project's target architecture
- prefer incremental migration over big-bang rewrites
- decompose work into the smallest coherent technical steps
- minimize the number of files impacted per task when possible
- preserve runtime behavior unless the migration intentionally changes it
- keep framework concerns at the edge of the target architecture
- make sequencing constraints explicit

Avoid:
- broad migration items that mix many concerns
- purely theoretical recommendations with no implementation path
- rewriting already acceptable code just for stylistic consistency
- proposing architecture changes that ignore current project conventions
- mixing feature delivery with migration planning unless requested

# When to use this skill

Use this skill when the codebase:
- is partially migrated to hexagonal architecture
- still contains framework-centric service layers or repositories
- has direct persistence coupling in the wrong layer
- mixes controllers, services, domain, and infrastructure concerns
- needs an ordered technical migration backlog
- needs Jira-ready technical tasks for remaining migration work

# Inputs to analyze

Inspect the codebase and identify:
- current modules or bounded areas
- current folder structure
- current dependency direction
- framework coupling, especially NestJS decorators and module wiring
- persistence coupling, especially Mongoose model or schema access
- presence or absence of use cases
- presence or absence of primary and secondary ports
- presence or absence of infrastructure adapters
- placement of business rules
- testing strategy and missing tests

# Migration gap categories

Classify findings into concrete migration categories such as:
- missing use cases
- missing primary ports
- missing secondary ports
- direct Mongoose usage outside infrastructure
- NestJS service containing business rules that belong in use cases or domain
- controllers coupled to persistence or domain internals
- DTO mapping not isolated at the edge
- missing adapters around repository or client dependencies
- domain depending on infrastructure or framework types
- missing architecture tests
- missing barrel files or inconsistent public exposure when the project expects them

# Target shape reasoning

For each area analyzed, identify the intended target shape.

Typical target moves include:
- move business orchestration into application use cases
- keep domain pure and framework-agnostic
- define secondary ports in core
- implement Mongoose adapters in infrastructure
- define primary ports where useful for inbound orchestration
- isolate REST or transport DTO mapping in infrastructure or edge layers
- invert dependencies so infrastructure depends on core, not the reverse

# Task decomposition rules

Every migration task should:
- have one clear technical objective
- be reviewable in isolation
- minimize file count when possible
- minimize blast radius
- avoid mixing refactor categories unnecessarily
- be worded so it can become a Jira ticket directly

Prefer tasks such as:
- introduce `FindCustomerPort`
- move `CustomerModel` access behind a Mongoose adapter
- extract `CreateCustomerUseCase` from `CustomerService`
- isolate controller-to-use-case mapping
- add architecture test preventing core from importing infrastructure

Avoid tasks such as:
- refactor customer module completely
- migrate all mongoose repositories
- clean all architecture violations in one PR

# Sequencing rules

Sequence tasks according to dependencies.

Typical order:
1. create missing abstractions or ports
2. create or adjust adapters
3. extract use cases or domain logic
4. rewire framework integration
5. remove old direct dependencies
6. add guardrail tests

When tasks are independent, state that they can be parallelized.

# Estimation guidance

Provide lightweight effort estimates such as:
- XS
- S
- M
- L

Estimation should reflect:
- number of files likely impacted
- coupling complexity
- test impact
- migration risk
- number of consumers to rewire

# Ticket-ready output

When asked to generate technical backlog items, each item should include:
- title
- technical objective
- current problem
- expected target state
- likely impacted files or areas
- scope boundaries
- dependencies
- done criteria
- relative effort

# Reporting expectations

After analysis, report:
- areas already aligned with the target architecture
- areas partially aligned
- areas still using the old architecture style
- main categories of migration work remaining
- recommended migration order
- fine-grained task list
- assumptions and uncertain areas

# Artifact creation policy

When generating project artifacts from this analysis:
- create files directly with the file creation tool
- edit files directly with the file editing tool
- do not rely on patch-style creation strategies
- do not use `apply_patch`
- for new generated artifacts, prefer writing the complete file content in one operation
- if shell commands are needed, prefer simple and explicit commands such as `mkdir -p`, `touch`, and `cat <<'EOF' > file`

# Related skills

This skill works best with:
- `typescript-hexagonal-architecture`
- `typescript-ddd-development`
- `jira-technical-ticket-writing`
