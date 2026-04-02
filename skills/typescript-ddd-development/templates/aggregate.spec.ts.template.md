# Aggregate Test Template

Use this template when generating tests for an aggregate root.

```ts
import { describe, expect, it } from 'vitest';
import { {AggregateName} } from './{aggregate-name}';

describe('{AggregateName}', () => {
    it('should create a valid aggregate', () => {
        const aggregate = {AggregateName}.create({validId}, {validProps});

        expect(aggregate).toBeInstanceOf({AggregateName});
        expect(aggregate.id).toBe({validId});
    });

    it('should throw on invalid creation input', () => {
        expect(() => {AggregateName}.create({validId}, {invalidProps})).toThrow(
            '{InvalidErrorMessage}'
        );
    });

    it('should apply a valid aggregate behavior', () => {
        const aggregate = {AggregateName}.create({validId}, {initialProps});

        aggregate.{behaviorName}({validArgument});

        expect(aggregate.{getterName}).toEqual({expectedValue});
    });

    it('should reject an invalid aggregate transition', () => {
        const aggregate = {AggregateName}.create({validId}, {initialProps});

        expect(() => aggregate.{behaviorName}({invalidArgument})).toThrow(
            '{TransitionErrorMessage}'
        );
    });

    it('should preserve aggregate invariants after mutation', () => {
        const aggregate = {AggregateName}.create({validId}, {initialProps});

        aggregate.{behaviorName}({validArgument});

        expect({invariantExpectation}).toBe(true);
    });

    it('should compare equal when identities are equal', () => {
        const left = {AggregateName}.from({sameId}, {propsA});
        const right = {AggregateName}.from({sameId}, {propsB});

        expect(left.equals(right)).toBe(true);
    });

    it('should compare different when identities are different', () => {
        const left = {AggregateName}.from({idA}, {props});
        const right = {AggregateName}.from({idB}, {props});

        expect(left.equals(right)).toBe(false);
    });
});
```
