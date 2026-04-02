# Dependency Rule Test Template

Use this template when enforcing a forbidden dependency direction.

```ts
import { describe, it, expect } from 'vitest';

describe('dependency rules', () => {
  it('should prevent domain from depending on infrastructure', async () => {
    expect(true).toBe(true);
  });
});
```

Replace the placeholder assertion with the dependency analysis approach used by the repository.
