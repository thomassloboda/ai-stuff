# Use Case Test Template

```ts
import { describe, expect, it } from 'vitest';
import { {UseCaseName} } from './{use-case-name}';

describe('{UseCaseName}', () => {
    it('should execute the use case successfully', async () => {
        const dependency = {
            {dependencyMethod}: async () => ({expectedDependencyResult}),
        };

        const useCase = new {UseCaseName}(dependency as never);

        const result = await useCase.execute({requestFixture});

        expect(result).toEqual({expectedResponse});
    });
});
```

## Notes

- Add failure-path tests.
- Verify branching and port interactions when relevant.
