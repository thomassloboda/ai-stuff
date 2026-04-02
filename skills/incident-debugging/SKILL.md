---
name: incident-debugging
description: Use this skill to debug incidents methodically, from symptom collection through root cause analysis, fix validation, and regression protection.
---

# Purpose

This skill structures debugging work for production or local incidents.

It applies to:
- failing tests
- runtime errors
- incident investigations
- unexpected behavior regressions
- integration failures

# Workflow

1. Capture the observed symptom precisely.
2. Reproduce when possible.
3. Narrow the fault domain.
4. Separate facts from hypotheses.
5. Validate the most plausible root cause.
6. Implement the smallest reliable fix.
7. Add or update a regression test when possible.
8. Verify the fix.

# Principles

Always:
- prefer root cause over symptom masking
- keep a clear chain from observation to conclusion
- challenge assumptions quickly
- document what was reproduced and what was not
- verify the fix with relevant checks

Avoid:
- broad blind changes
- stopping after finding a suspicious area without validation
- declaring success without verification

# Output guidance

Prefer this structure:
- Symptom
- Reproduction
- Root cause
- Fix
- Validation
- Remaining uncertainty
