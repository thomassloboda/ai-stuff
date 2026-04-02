# Value Object Test Template

Use this template when generating tests for a primitive-based value object.

```ts
import { describe, expect, it } from 'vitest';
import { {ValueObjectName} } from './{value-object-name}';

describe('{ValueObjectName}', () => {
    it('should create a valid instance from valid input', () => {
        const result = {ValueObjectName}.from({validInput});

        expect(result).toBeInstanceOf({ValueObjectName});
        expect(result.value).toBe({expectedStoredValue});
    });

    it('should throw on invalid input', () => {
        expect(() => {ValueObjectName}.from({invalidInput})).toThrow(
            '{InvalidErrorMessage}'
        );
    });

    it('should return its string representation', () => {
        const result = {ValueObjectName}.from({validInput});

        expect(result.toString()).toBe(String({expectedStoredValue}));
    });

    it('should compare equal when values are equal', () => {
        const left = {ValueObjectName}.from({equalInputA});
        const right = {ValueObjectName}.from({equalInputB});

        expect(left.equals(right)).toBe(true);
    });

    it('should compare different when values are different', () => {
        const left = {ValueObjectName}.from({validInputA});
        const right = {ValueObjectName}.from({validInputB});

        expect(left.equals(right)).toBe(false);
    });

    it('should serialize to its primitive value', () => {
        const result = {ValueObjectName}.from({validInput});

        expect(result.toJSON()).toBe({expectedStoredValue});
    });
});
```

## Notes

- Add one invalid test per validation rule when relevant.
- Add boundary tests when min/max constraints exist.
- Add normalization tests when normalization exists.
- Omit `toJSON` tests if the value object does not expose `toJSON`.
