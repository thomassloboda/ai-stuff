---
name: git-conventional-commit-writing
description: Use this skill to analyze the current worktree and propose clean commit messages following Conventional Commits and the project ticket convention `type(scope-optional): [PROJ-123] short description`.
---

# Purpose

This skill helps analyze a git worktree and propose one or more commit messages that follow:
- Conventional Commits
- the project ticket convention extracted from branch names
- concise and readable commit summaries
- optional long descriptions when they add value

It is intended for:
- proposing a commit message for the current worktree
- proposing multiple commit messages when the worktree mixes several intentions
- extracting project ticket information from the branch name
- selecting an appropriate conventional commit type
- selecting an optional scope
- drafting a useful body when needed

# Commit convention

The expected subject format is:

```text
type(scope-optional): [PROJ-123] short description
```

The expected body format is:

```text
[PROJ-123] longer description first line

Additional context when useful.
```

Rules:
- `scope` is optional
- `[PROJ-123]` is included only when a ticket can be extracted confidently
- the subject must be short, imperative, and must not end with a period
- if a body is present and a ticket exists, the first body line must repeat the ticket
- do not invent a ticket when none can be extracted confidently

# Required analysis

Before proposing a commit message, inspect:
- current branch name
- staged changes when relevant
- unstaged changes when relevant
- changed files
- overall worktree intent

Prefer staged changes when the user is preparing an actual commit.
If nothing is staged, analyze the full worktree and state that assumption.

# Reference routing

Use these references together:
- `references/conventional-commit-rules.md`
- `references/branch-ticket-extraction.md`
- `references/worktree-analysis.md`

Use this template when producing the final output:
- `templates/commit-message.template.md`

# Decision rules

## Commit type selection

Select the type from the dominant intention of the change.

Common mappings:
- `feat` for a new user-visible or domain-visible capability
- `fix` for a bug fix or incorrect behavior correction
- `refactor` for structural improvement without intended functional change
- `test` for test-only changes
- `docs` for documentation-only changes
- `chore` for maintenance or housekeeping changes
- `build` for build tooling, dependencies, packaging, or scripts
- `ci` for pipeline or CI-only changes
- `perf` for performance-focused changes

Do not default to `chore` too quickly. Prefer the most meaningful type.

## Scope selection

Choose a scope only when there is a clear dominant module, bounded area, or technical surface.

Possible scopes may come from:
- the dominant folder
- the main domain concept
- the main adapter or infrastructure target
- the main use case or feature area

If no scope is clearly dominant, omit it.

## Ticket extraction

Try to extract a ticket from the branch name.
Use the extracted ticket in the subject and, when a body exists, repeat it on the first body line.

If no ticket can be extracted confidently:
- omit the ticket entirely
- do not invent a placeholder
- do not block the proposal

## Single commit vs multiple commits

If the worktree appears cohesive, propose one commit message.
If the worktree mixes multiple unrelated intentions, explicitly say so and propose a split into multiple commits.

Examples of mixed intentions:
- bug fix plus unrelated refactor
- feature addition plus mass formatting
- domain change plus separate CI cleanup
- test changes for unrelated modules bundled together

# Output expectations

When proposing a commit message, always report:
- whether the proposal is based on staged changes or the full worktree
- extracted ticket, if any
- selected type
- selected scope, if any
- proposed subject
- proposed body, if useful
- whether the worktree should ideally be split into multiple commits

# Anti-pattern checks

Before finalizing, check that the proposed message does not:
- use an incorrect or vague type without justification
- force a scope when none is clear
- invent a ticket
- produce an overly long subject
- describe implementation trivia instead of intent
- mix multiple unrelated changes into one message without warning
