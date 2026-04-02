# Use Case TypeScript Template

Use this template when generating an application use case.

```ts
export interface {UseCaseName}Request {
    {requestField}: {RequestFieldType};
}

export interface {UseCaseName}Response {
    {responseField}: {ResponseFieldType};
}

export class {UseCaseName} {
    constructor(
        private readonly {dependencyName}: {DependencyType}
    ) {}

    async execute(request: {UseCaseName}Request): Promise<{UseCaseName}Response> {
        const {requestField} = request;

        const result = await this.{dependencyName}.{dependencyMethod}({requestField});

        return {
            {responseField}: result,
        };
    }
}
```

## Notes

- Place under `src/application/use-cases`.
- Depend on ports, not concrete infrastructure implementations.
- Keep orchestration explicit and focused.
