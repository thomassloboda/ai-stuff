# Sonar Guidance

Use this reference when review findings overlap with static quality concerns.

Focus on:
- complexity that harms readability or confidence
- duplication that increases maintenance cost
- branches that are not validated by tests
- suspicious null handling or unchecked assumptions
- methods that coordinate too many concerns at once

Do not force tool-specific wording.
Explain the underlying engineering concern in plain language.
