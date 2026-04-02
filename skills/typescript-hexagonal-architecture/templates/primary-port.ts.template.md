# Primary Port TypeScript Template

```ts
export interface {PrimaryPortName}Request {
    {requestField}: {RequestFieldType};
}

export interface {PrimaryPortName}Response {
    {responseField}: {ResponseFieldType};
}

export interface {PrimaryPortName} {
    execute(request: {PrimaryPortName}Request): Promise<{PrimaryPortName}Response>;
}
```

## Notes

- Place under `src/core/ports/primary`.
- Keep the contract small and framework-agnostic.
