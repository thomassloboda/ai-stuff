---
name: codebase-introspection-and-agent-generation
description: Use this skill to inspect an unknown repository, detect its stack and conventions, and generate project-specific onboarding artifacts such as AGENTS.md, PROJECT_CONVENTIONS.md, WORKFLOWS.md, and recommendations for useful skills and agents.
---

# Purpose

This skill helps inspect a codebase regardless of language or framework and turn that inspection into actionable project-specific AI guidance.

It is intended for:
- repository onboarding
- stack detection
- dependency and version analysis
- architecture and convention extraction
- project-specific `AGENTS.md` generation
- project-specific `PROJECT_CONVENTIONS.md` generation
- project-specific `WORKFLOWS.md` generation
- recommendations for useful skills and agents

# General principles

Always:
- inspect the repository before proposing guidance
- prefer repository evidence over assumptions
- separate confirmed findings from inferences
- identify actual project conventions from code, scripts, CI, and folder structure
- verify version-sensitive framework or package assumptions when needed
- recommend the smallest useful set of project-specific artifacts

Avoid:
- forcing generic architecture patterns onto the project
- inventing conventions not reflected in the codebase
- generating too many project-specific agents or skills without clear value
- treating manifest dependencies as proof of actual usage without checking the codebase

# Analysis workflow

## 1. Detect structure
Inspect the top-level structure and identify whether the repository is:
- a single package
- a monorepo
- a service repository
- a library
- a frontend application
- a backend service
- a fullstack application
- an infrastructure or platform repository

## 2. Detect languages and package managers
Look for evidence of languages, runtimes, and package managers.

Examples include:
- TypeScript / JavaScript
- Python
- Go
- Java / Kotlin
- PHP
- Ruby
- Rust
- C#

Examples of package managers and build systems include:
- pnpm, npm, yarn
- poetry, pip
- cargo
- go modules
- maven, gradle
- composer
- bundler

## 3. Detect frameworks and major tooling
Look for frameworks and tooling in manifests, lock files, scripts, and code.

Examples include:
- NestJS, Express, Fastify, Next.js, React, Vue, Angular
- Spring Boot, Micronaut, Quarkus
- FastAPI, Django, Flask
- Laravel, Symfony
- Kafka, RabbitMQ, NATS
- Prisma, TypeORM, Mongoose, Sequelize, Drizzle
- Vitest, Jest, Playwright, Cypress, pytest, JUnit
- ESLint, Prettier, Biome, Ruff, mypy, PHPStan, Sonar, Detekt
- Datadog, Sentry, OpenTelemetry, Prometheus, Grafana

## 4. Detect scripts and workflows
Capture the main scripts and commands used by developers and CI.

Examples:
- build
- test
- lint
- format
- typecheck
- coverage
- e2e
- dev
- migration
- seed
- release

## 5. Infer architecture and conventions
Infer project structure only when supported by evidence.

Possible findings include:
- layered architecture
- hexagonal architecture
- DDD tactical patterns
- modular monolith
- package-by-feature
- ports and adapters
- barrel-file usage
- colocated tests
- naming conventions
- API module boundaries

## 6. Recommend artifacts
Based on the findings, recommend or generate:
- `STACK_ANALYSIS.md`
- `PROJECT_CONVENTIONS.md`
- `AGENTS.md`
- `WORKFLOWS.md`
- `RECOMMENDED_SKILLS_AND_AGENTS.md`

Generate project-specific skills or agents only when a generic setup would not be enough.

# Output artifacts

## `STACK_ANALYSIS.md`
Should summarize:
- detected languages
- detected frameworks
- dependency and version highlights
- test tooling
- quality tooling
- CI/CD tooling
- observability or runtime tooling
- confidence notes

## `PROJECT_CONVENTIONS.md`
Should summarize:
- structure conventions
- naming conventions
- testing conventions
- lint/format/typecheck commands
- architecture conventions
- import or dependency conventions
- commit and PR conventions when detectable

## `AGENTS.md`
Should summarize:
- which agents are recommended for this project
- which skills are recommended for this project
- which commands matter most in this repository
- what architecture or stack rules agents must respect here

## `WORKFLOWS.md`
Should document only the most useful project-local workflows.

Examples:
- ticket to implementation
- bugfix and regression testing
- review and PR preparation
- release or migration workflow
- incident investigation workflow

## `RECOMMENDED_SKILLS_AND_AGENTS.md`
Should distinguish:
- existing generic agents and skills that are already sufficient
- project-specific agents or skills that are genuinely worth creating
- why each recommendation exists

# How to use other skills

When evidence supports it, reference or recommend:
- `typescript-ddd-development`
- `typescript-hexagonal-architecture`
- `pull-request-writing`
- `code-review`
- `incident-debugging`
- `observability-troubleshooting`
- `git-conventional-commit-writing`

Only recommend them when they fit the actual repository.

# Anti-pattern checks

Before finalizing, check that you do not:
- infer architecture from folder names alone without other evidence
- confuse declared dependencies with actual runtime usage
- over-generate project-specific artifacts
- miss the project’s real developer entrypoints and scripts
- erase uncertainty when the repository is mixed or transitional

# Artifact creation policy

When generating project artifacts:
- create files directly with the file creation tool
- edit files directly with the file editing tool
- do not rely on patch-style creation strategies
- do not use `apply_patch`
- for new generated artifacts, prefer writing the complete file content in one operation
- if shell commands are needed, prefer simple and explicit commands such as `mkdir -p`, `touch`, and `cat <<'EOF' > file`