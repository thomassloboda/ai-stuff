# Testing Strategy Reference

## Goal

Choose architecture tests that are strict enough to protect the design without becoming noisy.

## Preferred order

1. add direct architecture tests for dependency direction and forbidden imports
2. add placement checks when file drift is common
3. add barrel-file checks only where they reflect a real public API convention
4. keep tests readable and closely aligned with repository structure

## Useful enforcement styles

- dependency graph assertions
- import-pattern assertions
- folder naming and placement checks
- module public surface checks

## Reporting expectations

When adding architecture tests, explain:
- which rule the test protects
- what kind of regression it prevents
- what a future contributor should do if it fails legitimately
