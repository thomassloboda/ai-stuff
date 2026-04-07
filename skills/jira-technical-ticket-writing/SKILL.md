---
name: jira-technical-ticket-writing
description: Use this skill to draft technical Jira tickets in a Markdown artifact before creating or updating issues in Jira, so scope, wording, and dependencies are reviewed in a stable written form first.
---

# Purpose

This skill helps prepare high-quality Jira tickets by drafting them in Markdown before any Jira write action happens.

It is intended for:
- technical implementation tickets
- migration backlog items
- refactor tasks
- bugfix tickets
- architecture enforcement tasks
- decomposing an approved plan into Jira-ready items

# Core principle

Write first, create second.

Before creating or updating Jira issues, produce a Markdown draft that captures the exact wording, scope, dependencies, and done criteria for each ticket.

This draft becomes the reviewable source of truth for the Jira-writing step.

# Why this skill exists

Drafting in Markdown first helps:
- validate scope before strong Jira actions
- keep a durable review artifact in the repository or workspace
- reduce vague or inconsistent ticket descriptions
- separate planning quality from tool execution
- make batch ticket creation more deterministic

# When to use this skill

Use this skill when:
- the user asks to create Jira tickets from a plan
- a migration backlog needs ticket-ready items
- a technical analysis must be converted into actionable Jira issues
- an agent is about to create or update several Jira issues
- ticket wording needs to be reviewed or shared before Jira writes happen

# Required workflow

Follow this sequence:

1. Read the approved plan or source material.
2. Draft the tickets in a Markdown file.
3. Validate the draft for scope, granularity, and dependencies.
4. Only then create or update Jira issues from that draft.

Do not skip the Markdown drafting step unless the user explicitly asks for direct Jira creation without a draft.

# Draft file expectations

The Markdown draft should be explicit and operational.

Use one section per ticket and include:
- title
- technical objective
- current problem
- target state
- in scope
- out of scope
- dependencies
- done criteria
- effort

When useful, also include:
- epic key
- components
- labels
- linked ticket references

Prefer a filename such as:
- `jira-ticket-draft.md`
- `migration-ticket-draft.md`
- `docs/jira/<topic>-tickets.md`

Follow existing project conventions if they already define a drafting location.

# Ticket writing principles

Each drafted ticket should be:
- small
- technically coherent
- independently understandable
- suitable for a small pull request
- explicit about boundaries
- actionable without hidden context

Avoid:
- vague titles
- mixing unrelated technical goals
- missing done criteria
- overloading one ticket with an entire epic worth of work
- inventing business context not present in the plan

# Recommended Markdown structure

Use this structure when possible:

```md
# Jira Ticket Draft

## Ticket 1

### Title
Introduce CustomerRepositoryPort

### Technical objective
Describe the technical move in one or two sentences.

### Current problem
Describe the coupling, gap, or missing abstraction.

### Target state
Describe the expected architecture or behavior after the change.

### In scope
- Item 1
- Item 2

### Out of scope
- Item 1

### Dependencies
- None

### Done criteria
- Criterion 1
- Criterion 2

### Effort
S
```

# Validation checklist

Before Jira creation, verify that:
- each ticket maps to one technical objective
- dependencies are explicit
- done criteria are testable or observable
- wording matches the approved plan
- scope boundaries are clear
- the draft is complete enough to create Jira issues without improvisation

# Jira creation handoff

When handing the draft to a Jira-writing agent or tool:
- preserve the ticket titles exactly unless a project convention requires adaptation
- preserve scope boundaries
- preserve dependencies and epic linkage
- reuse known project components, versions, and fields only when confidence is high

# Output expectations

After using this skill, report:
- the Markdown draft file path
- whether Jira issues were only drafted or also created
- the number of tickets prepared
- important assumptions or unresolved ambiguities
