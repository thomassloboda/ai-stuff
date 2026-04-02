# Repository Adapter TypeScript Template

```ts
export class {Technology}{RepositoryName} implements {RepositoryPortName} {
    constructor(
        private readonly client: {ClientType}
    ) {}

    async {methodName}({argumentName}: {ArgumentType}): Promise<{ReturnType}> {
        const record = await this.client.{clientMethod}({clientArgument});

        return {mappingExpression};
    }
}
```

## Notes

- Place under the correct persistence folder.
- Keep persistence details inside the adapter.
- Map records explicitly.
- Add adapter-level tests.
