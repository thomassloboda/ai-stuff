# Entity Test Template

Use this template when generating tests for an entity.

```ts
import { describe, expect, it } from 'vitest';
import { {EntityName} } from './{entity-name}';

describe('{EntityName}', () => {
    it('should create a valid entity', () => {
        const entity = {EntityName}.create({validId}, {validProps});

        expect(entity).toBeInstanceOf({EntityName});
        expect(entity.id).toBe({validId});
    });

    it('should throw on invalid creation input', () => {
        expect(() => {EntityName}.create({validId}, {invalidProps})).toThrow(
            '{InvalidErrorMessage}'
        );
    });

    it('should apply a valid domain behavior', () => {
        const entity = {EntityName}.create({validId}, {initialProps});

        entity.{behaviorName}({behaviorValidArgument});

        expect(entity.{getterName}).toBe({expectedValue});
    });

    it('should reject an invalid state transition', () => {
        const entity = {EntityName}.create({validId}, {initialProps});

        expect(() => entity.{behaviorName}({behaviorInvalidArgument})).toThrow(
            '{TransitionErrorMessage}'
        );
    });

    it('should compare equal when identities are equal', () => {
        const left = {EntityName}.from({sameId}, {propsA});
        const right = {EntityName}.from({sameId}, {propsB});

        expect(left.equals(right)).toBe(true);
    });

    it('should compare different when identities are different', () => {
        const left = {EntityName}.from({idA}, {props});
        const right = {EntityName}.from({idB}, {props});

        expect(left.equals(right)).toBe(false);
    });
});
```
