---
name: observability-troubleshooting
description: Use this skill to investigate incidents and service issues through logs, metrics, traces, dashboards, and other observability signals.
---

# Purpose

This skill helps analyze monitoring and runtime signals to narrow incidents quickly.

It applies to:
- logs
- traces
- metrics
- dashboards
- alerts
- latency regressions
- throughput drops
- error spikes

# Principles

Always:
- start from concrete signals
- correlate signals across sources when possible
- distinguish observations from hypotheses
- identify the likely impacted service, route, dependency, or release window
- suggest the smallest next diagnostic step when uncertainty remains

Avoid:
- jumping straight from a single alert to a code fix
- treating correlation as proof without caveats
- ignoring recent deploys, config changes, or dependency incidents

# Recommended troubleshooting flow

1. Identify the triggering signal.
2. Establish timeframe and blast radius.
3. Identify affected service, route, or dependency.
4. Correlate logs, traces, and metrics.
5. Compare before and after relevant changes.
6. Form and rank hypotheses.
7. Suggest code areas or infrastructure areas to inspect next.

# Output guidance

Prefer this structure:
- Signal summary
- Observations
- Hypotheses
- Evidence
- Suggested next checks
- Likely ownership / code area
