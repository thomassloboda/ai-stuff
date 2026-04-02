# Domain Error TypeScript Template

Use this template when generating a domain error.

Adapt:
- error name
- message
- optional structured context
- base class usage if the project already has one

## Simple template

```ts
export class {DomainErrorName} extends Error {
    constructor() {
        super('{ErrorMessage}');
        this.name = '{DomainErrorName}';
    }
}
```

## Template with structured context

```ts
export interface {DomainErrorName}Context {
    {contextFieldName}: {ContextFieldType};
}

export class {DomainErrorName} extends Error {
    constructor(
        public readonly context: {DomainErrorName}Context
    ) {
        super('{ErrorMessage}');
        this.name = '{DomainErrorName}';
    }
}
```

## Notes

- Prefer explicit business-oriented names.
- Keep the error small and intention-revealing.
- Add structured context only when it materially improves domain clarity or testing.
- Reuse a shared domain base class if the project already has one.
