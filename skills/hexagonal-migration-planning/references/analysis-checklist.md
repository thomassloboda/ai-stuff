# Analysis Checklist

Use this checklist when assessing a partially hexagonal codebase.

## Current-state inspection

Inspect:
- folder structure
- NestJS modules, controllers, providers, and services
- Mongoose schemas, models, repositories, and direct model usage
- application service orchestration
- domain placement and domain purity
- port definitions and adapter implementations
- test locations and test types
- dependency direction between core, application, and infrastructure

## Red flags to detect

Look for:
- direct `@InjectModel()` usage outside infrastructure adapters
- business logic concentrated in NestJS services
- controllers calling persistence directly
- DTOs leaking into use cases or domain
- domain code importing NestJS or Mongoose types
- missing output ports around repositories or clients
- missing use cases where orchestration exists
- infrastructure code placed under core
- weak or missing architecture tests
- large modules that mix transport, orchestration, business rules, and persistence

## Progress classification

For each module or area, classify as:
- already hexagonal
- partially migrated
- not migrated

## Migration readiness questions

Ask:
- what is the intended boundary of the module?
- what belongs to application?
- what belongs to domain?
- what should become a port?
- what should become an adapter?
- what framework dependencies must move outward?
- what persistence dependencies must move outward?
- what tests must be added to keep behavior safe during migration?
