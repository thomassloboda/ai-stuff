# Entity TypeScript Template

Use this template when generating a domain entity in TypeScript.

Adapt:
- identity type
- props
- invariants
- domain behaviors
- transition guards
- error types

```ts
export interface {EntityName}Props {
    {propName}: {PropType};
}

export class {EntityName} {
    private constructor(
        public readonly id: {IdType},
        private props: {EntityName}Props
    ) {}

    static create(id: {IdType}, props: {EntityName}Props): {EntityName} {
        {EntityName}.validate(props);

        return new {EntityName}(id, props);
    }

    static from(id: {IdType}, props: {EntityName}Props): {EntityName} {
        {EntityName}.validate(props);

        return new {EntityName}(id, props);
    }

    private static validate(props: {EntityName}Props): void {
        if ({invalidCondition}) {
            throw new Error('{InvalidErrorMessage}');
        }
    }

    get {getterName}(): {PropType} {
        return this.props.{propName};
    }

    public {behaviorName}({behaviorArgumentName}: {BehaviorArgumentType}): void {
        if ({invalidTransitionCondition}) {
            throw new Error('{TransitionErrorMessage}');
        }

        this.props.{propName} = {nextValueExpression};
    }

    public equals(other: {EntityName}): boolean {
        return this.id === other.id;
    }

    public toJSON(): {EntityName}Props & { id: {IdType} } {
        return {
            id: this.id,
            ...this.props,
        };
    }
}
```

## Notes

- Keep mutation controlled through domain methods only.
- Do not expose props directly.
- `toJSON` is optional.
- Replace primitive ids with a dedicated id value object when the project uses one.
