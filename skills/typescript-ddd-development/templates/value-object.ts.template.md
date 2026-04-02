# Value Object TypeScript Template

Use this template when generating a value object in TypeScript.

Adapt:
- class name
- primitive or fields type
- validation rules
- normalization rules
- default generation behavior in `create`
- error types if the project uses dedicated domain errors

## Single primitive value object template

```ts
export class {ValueObjectName} {
    private constructor(
        public readonly value: {PrimitiveType}
    ) {}

    static create(): {ValueObjectName} {
        return new {ValueObjectName}({defaultValue});
    }

    static from(value: {PrimitiveType}): {ValueObjectName} {
        const normalizedValue = {ValueObjectName}.normalize(value);
        {ValueObjectName}.validate(normalizedValue);

        return new {ValueObjectName}(normalizedValue);
    }

    private static normalize(value: {PrimitiveType}): {PrimitiveType} {
        return value;
    }

    private static validate(value: {PrimitiveType}): void {
        if ({invalidCondition}) {
            throw new Error('{InvalidErrorMessage}');
        }
    }

    public toString(): string {
        return String(this.value);
    }

    public equals(other: {ValueObjectName}): boolean {
        return this.value === other.value;
    }

    public toJSON(): {PrimitiveType} {
        return this.value;
    }
}
```

## Notes

- Keep the constructor private.
- Use `create` only when the domain can generate a valid default or derived value.
- Use `from` for external input.
- Keep `normalize` only when needed. If no normalization is needed, it may return the value unchanged.
- `toJSON` is optional and should be included only if serialization is useful.
- Replace generic `Error` with a dedicated domain error if the project uses one.
