# Repository Analysis Reference

## Goal

Read an unknown repository and extract enough information to understand how developers actually work in it.

## Signals to inspect

Inspect, when present:
- top-level folder layout
- manifest and lock files
- build and task files
- CI/CD workflows
- test files and coverage config
- lint and formatting config
- code structure and imports
- README, CONTRIBUTING, and project docs
- deployment, container, and infrastructure files
- observability and monitoring config

## Strong evidence vs weak evidence

Treat as strong evidence:
- scripts actually defined in manifests
- config files used by tooling
- import patterns in code
- test file placement
- CI workflow commands
- architecture tests or lint rules

Treat as weaker evidence:
- a dependency present but unused
- a folder name without supporting imports or scripts
- outdated documentation that conflicts with code

## Deliverables

Produce findings that are:
- concise
- explicit about confidence
- grounded in files and code patterns
- useful for generating project-specific guidance
