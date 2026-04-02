# Architecture Test Template

Use this template when the project wants an explicit architecture rule test.

```ts
import { describe, expect, it } from 'vitest';

describe('architecture', () => {
    it('should respect declared layer boundaries', () => {
        expect(true).toBe(true);
    });
});
```

## Notes

- Replace the placeholder assertion with a real architecture check when the codebase uses such tests.
- Keep this optional unless the project explicitly wants architecture tests.
