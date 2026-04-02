# Aggregate TypeScript Template

Use this template when generating an aggregate root in TypeScript.

Adapt:
- aggregate root name
- identity type
- internal members
- invariants
- public behaviors
- transition guards
- domain error types

```ts
export interface {AggregateName}Props {
    {propName}: {PropType};
}

export class {AggregateName} {
    private constructor(
        public readonly id: {IdType},
        private props: {AggregateName}Props
    ) {}

    static create(id: {IdType}, props: {AggregateName}Props): {AggregateName} {
        {AggregateName}.validate(props);

        return new {AggregateName}(id, props);
    }

    static from(id: {IdType}, props: {AggregateName}Props): {AggregateName} {
        {AggregateName}.validate(props);

        return new {AggregateName}(id, props);
    }

    private static validate(props: {AggregateName}Props): void {
        if ({invalidCondition}) {
            throw new Error('{InvalidErrorMessage}');
        }
    }

    get {getterName}(): {PropType} {
        return this.props.{propName};
    }

    public {behaviorName}({argumentName}: {ArgumentType}): void {
        if ({forbiddenCondition}) {
            throw new Error('{TransitionErrorMessage}');
        }

        {mutationLogic}

        this.assertInvariants();
    }

    private assertInvariants(): void {
        if ({aggregateInvariantViolation}) {
            throw new Error('{AggregateInvariantErrorMessage}');
        }
    }

    public equals(other: {AggregateName}): boolean {
        return this.id === other.id;
    }

    public toJSON(): {AggregateName}Props & { id: {IdType} } {
        return {
            id: this.id,
            ...this.props,
        };
    }
}
```

## Notes

- The aggregate root is the only public entry point for aggregate behavior.
- Do not expose internal members for direct uncontrolled mutation.
- Re-check aggregate invariants after each public behavior when relevant.
- `toJSON` is optional.
- Replace primitive ids with dedicated value objects when the project uses them.
