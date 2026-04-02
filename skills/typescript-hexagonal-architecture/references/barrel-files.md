# Barrel Files Reference

## Purpose

This project uses a barrel-file system by default.

Barrel files improve module exposition, reduce noisy import paths, and make folder-level public APIs explicit.

## Rules

Always:
- create or update `index.ts` for every meaningful exposable folder
- export the intended public API explicitly
- keep barrel files aligned with folder ownership

Prefer:
- imports through barrel files across folder boundaries
- clear folder-level public APIs
- predictable export shapes

Avoid:
- unnecessary deep imports when a barrel file already exists
- massive opaque export chains that hide ownership
- exporting private implementation details just because a barrel file exists

## Typical shapes

Artifact folder:

```ts
export * from './my-artifact';
```

Parent folder:

```ts
export * from './my-artifact';
export * from './my-other-artifact';
```

## Testing and verification

When adding or moving files:
- update the local barrel file
- update the parent barrel file when relevant
- verify imports remain consistent
