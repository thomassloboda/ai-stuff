---
name: architecture-testing
description: Use this skill to add, update, or enforce architecture tests for layering, dependency rules, forbidden imports, folder placement, and structural conventions in a TypeScript codebase.
---

# Purpose

This skill helps enforce architectural guardrails in a TypeScript codebase.

It is intended for:
- dependency direction tests
- forbidden import checks
- layer boundary tests
- hexagonal architecture enforcement
- folder placement validation
- barrel-file policy enforcement when relevant
- structural regressions prevention

This skill is especially useful in codebases that follow DDD and hexagonal architecture and want their architecture to remain enforceable over time.

# General principles

Always:
- prefer automated architectural checks over informal expectations when the rule is stable
- enforce the minimum set of rules that meaningfully protect the design
- keep architecture tests readable and intention-revealing
- align architecture rules with the real project structure
- fail loudly on invalid dependency direction
- keep architecture tests focused on structure, not business behavior

Avoid:
- adding architecture tests that do not match the actual repository structure
- making rules so broad that they become noisy or constantly false-positive
- using architecture tests to enforce style trivia that is not structurally important
- duplicating existing lint or build rules unless the extra guardrail adds value

# Main references

Use these references when applying this skill:
- `references/dependency-rules.md`
- `references/layer-boundaries.md`
- `references/barrel-files.md`
- `references/placement-rules.md`
- `references/testing-strategy.md`

Use these templates when appropriate:
- `templates/architecture-test.template.md`
- `templates/dependency-rule-test.template.md`
- `templates/barrel-file-check.template.md`

# Scope of enforcement

This skill should help verify rules such as:
- domain must not depend on infrastructure
- application may depend on domain and ports but not the reverse
- infrastructure may depend inward, never the reverse
- ports live in the expected layer
- adapters live in the expected infrastructure folders
- domain artifacts are placed in the expected domain folders
- barrel files exist where the project requires them

# When to use this skill

Use this skill when:
- architectural drift has appeared or is likely
- a repository is using hexagonal architecture and wants automated enforcement
- a refactor changes layering or file placement
- a code review highlights repeated dependency violations
- the team wants architecture rules to be testable rather than implied

# Output expectations

After using this skill, report:
- which architecture rules were enforced
- which files or tests were added or updated
- which assumptions were made about the repository structure
- which rules were intentionally left unenforced and why
