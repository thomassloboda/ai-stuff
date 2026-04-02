# Commit Message Template

Use this template to produce the final proposal.

## Subject

```text
{type}({scope-optional}): [{ticket-optional}] {short-description}
```

Rules:
- omit `({scope})` when no clear scope exists
- omit `[TICKET]` when no ticket can be extracted confidently
- keep the subject short, imperative, and intention-focused
- do not end the subject with a period

## Body

Use a body only when it adds value.

If a ticket exists and a body is present, the first body line must repeat it:

```text
[{ticket}] {long-description-first-line}

{optional-additional-context}
```

## Output format

When proposing a commit message, provide:
- analysis basis: staged changes or full worktree
- extracted ticket
- selected type
- selected scope
- proposed subject
- proposed body, if any
- split recommendation, if relevant
