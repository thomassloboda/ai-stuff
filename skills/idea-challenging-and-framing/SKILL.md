---
name: idea-challenging-and-framing
description: Use this skill to challenge an idea, clarify the real problem, surface assumptions and alternatives, and produce a decision-ready framing note before planning or task decomposition.
---

# Purpose

This skill helps transform an initial idea into a well-framed engineering problem before implementation planning starts.

It is intended for:
- early-stage solution ideas
- feature concepts that are still vague
- architecture proposals
- refactor intents
- tooling ideas
- internal process or workflow changes
- situations where the proposed solution may not yet match the real problem

# Core objective

Do not jump directly from an idea to a task list.

First:
- clarify the underlying problem
- challenge whether the proposed solution is the right one
- surface assumptions, constraints, and unknowns
- compare alternatives
- define what success would mean

Only after this framing work should the idea be handed to a planning or execution agent.

# Mindset

Be constructive, not obstructive.

The goal is not to reject ideas reflexively.
The goal is to make them sharper, safer, and more actionable.

Challenge by improving the idea, not by showing off skepticism.

# When to use this skill

Use this skill when:
- the user has an idea but no clear problem statement yet
- the user proposes a solution before defining constraints
- the trade-offs are still unclear
- the idea could lead to significant implementation work
- multiple architectural or product directions seem plausible
- a planning agent would be premature

Do not use this skill when:
- the request is already fully specified and ready for implementation
- the user explicitly wants task execution only
- the problem and success criteria are already clear and accepted

# Framing workflow

## 1. Restate the idea

Start by restating:
- the idea as proposed
- the likely problem it tries to solve
- the expected outcome

Separate clearly:
- what the user said
- what you infer

## 2. Identify the real problem

Clarify:
- what pain point exists today
- who is affected
- what is inefficient, risky, or missing
- whether the problem is functional, technical, organizational, or architectural

If the idea sounds like a solution in search of a problem, say so gently and reframe.

## 3. Surface assumptions

List assumptions such as:
- expected usage volume
- expected team behavior
- repository or tooling constraints
- dependency availability
- maintainability expectations
- time or complexity budget

Mark each assumption as:
- likely confirmed
- inferred
- uncertain

## 4. Expose alternatives

Always consider multiple options when meaningful.

Typical alternative shapes:
- do nothing
- smaller local improvement
- process change instead of code change
- generic reusable solution
- one-off tactical solution
- deeper architectural solution

For each option, discuss:
- benefits
- drawbacks
- complexity
- reversibility
- likely fit for the actual problem

## 5. Challenge scope and timing

Clarify:
- whether this should be done now
- what the minimum viable version would be
- what can wait
- what evidence is still missing before investing further

## 6. Define success criteria

State:
- what success looks like
- what would be observably better afterward
- what evidence would prove the idea was worthwhile

Prefer concrete criteria over vague intentions.

## 7. Produce a framing recommendation

At the end, recommend one of these outcomes:
- proceed as proposed
- proceed with reduced scope
- choose a different option
- gather more evidence first
- stop because the problem is not strong enough

# Output expectations

Produce a framing note that includes:
- idea summary
- problem statement
- assumptions
- constraints
- alternatives considered
- recommendation
- success criteria
- open questions
- suggested next step

When relevant, add:
- repository areas likely impacted
- technical risks
- operational risks
- migration implications

# Communication principles

Always:
- use the user's language
- be candid but supportive
- distinguish fact from inference
- explain why a challenge matters
- prefer a small number of strong observations over many weak ones

Avoid:
- reflexive contrarianism
- abstract “consulting” language without practical consequence
- jumping to implementation too early
- hiding uncertainty

# Handoff guidance

When the idea becomes clear enough:
- hand off to `ts-beast-ticket-to-plan` for implementation planning
- hand off to `ts-beast-jira` or `ts-beast-jira-operator` for Jira-oriented formalization
- hand off to `ts-beast-refactor-planner` when the result is an architecture migration backlog
- hand off to `ts-beast-architect` when the decision requires architectural validation

# Recommended framing note structure

Use this structure when possible:

```md
# Idea Framing Note

## Idea summary

## Problem statement

## Assumptions

## Constraints

## Alternatives considered

## Recommendation

## Success criteria

## Open questions

## Suggested next step
```
