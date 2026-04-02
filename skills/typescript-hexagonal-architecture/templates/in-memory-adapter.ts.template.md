# In-Memory Adapter TypeScript Template

```ts
export class InMemory{AdapterName} implements {PortName} {
    private readonly items = new Map<string, {StoredType}>();

    async {methodName}({argumentName}: {ArgumentType}): Promise<{ReturnType}> {
        {implementationLogic}
    }
}
```

## Notes

- Place under `src/infrastructure/in-memory`.
- Keep behavior faithful to the port contract.
- Add focused unit tests.
