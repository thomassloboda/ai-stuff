# Architecture Test Template

Use this template when adding a general architecture test file.

```ts
import { describe, it, expect } from 'vitest';

describe('architecture', () => {
  it('should respect the intended layer boundaries', async () => {
    expect(true).toBe(true);
  });
});
```

Adapt the implementation to the repository tooling used for architecture assertions.
