---
name: pull-request-writing
description: Use this skill to prepare clear, high-signal pull request titles and descriptions from a worktree, diff, or set of code changes.
---

# Purpose

This skill helps turn local code changes into a clean pull request package.

It should help produce:
- a PR title
- a summary of what changed
- motivation or context
- risks and caveats
- validations and tests performed
- migration, rollout, or operational notes when relevant
- links or references to tickets when available

# Principles

Always:
- describe what actually changed, not what was intended but not implemented
- keep titles concise and meaningful
- prefer grouped summaries over file-by-file repetition
- explain user-facing, business, architectural, and operational impact when relevant
- mention tests and validations explicitly
- state important risks or unknowns honestly

Avoid:
- low-signal laundry lists of file names without explanation
- vague titles such as "misc updates"
- overclaiming confidence when the work was not fully validated

# Recommended PR structure

Prefer this structure when possible:
- Title
- Why
- What changed
- Risks / caveats
- Validation
- Ticket / references

# Title guidance

A good PR title should:
- describe the main intention of the change
- stay short enough to scan easily
- avoid trailing punctuation
- reflect the dominant change, not every small edit

# Diff analysis guidance

When analyzing a diff:
- identify the dominant intent of the change
- group related modifications together
- distinguish implementation changes from test-only or cleanup-only changes
- note when the worktree mixes unrelated concerns

If the diff mixes multiple concerns, say so explicitly.

# Ticket references

When ticket identifiers are available from the branch name, PR template, or user input:
- include them consistently
- do not invent missing tickets
- clearly distinguish confirmed references from inferred ones

# Validation section

Always include validation when available:
- tests run
- type checks
- lint checks
- manual verification
- observability checks when relevant

If validation was not possible, say so clearly.
