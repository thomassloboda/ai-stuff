# REST Adapter TypeScript Template

```ts
export class {RestAdapterName} {
    constructor(
        private readonly {useCaseName}: {UseCaseType}
    ) {}

    async handle(request: {RequestType}): Promise<{ResponseType}> {
        const result = await this.{useCaseName}.execute({mappedRequest});

        return {mappedResponse};
    }
}
```

## Notes

- Place under `src/infrastructure/rest`.
- Keep HTTP mapping concerns here.
- Do not place core business rules in the adapter.
