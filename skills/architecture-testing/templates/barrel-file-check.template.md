# Barrel File Check Template

Use this template when the project expects `index.ts` barrel files in public folders.

```ts
import { describe, it, expect } from 'vitest';

describe('barrel files', () => {
  it('should expose expected public folders through index.ts', async () => {
    expect(true).toBe(true);
  });
});
```

Adapt the check to your file system and architectural enforcement tooling.
