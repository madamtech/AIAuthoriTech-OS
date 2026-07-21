---
name: dashboard-designer
description: Create decision-focused dashboard specifications covering audiences, decisions, metric contracts, sources, freshness, targets, comparisons, filters, segments, visual encodings, drill paths, actions, alerts, permissions, accessibility, responsive behavior, data quality, performance, testing, and governance. Use for executive, operational, client, product, analytics, monitoring, or AI dashboards—not to invent metrics, conceal uncertainty, replace source-system reconciliation, or claim a visualized number is correct without validated lineage.
---

# Dashboard Designer

Design from the user's decision backward to verified data and action.

1. Confirm the dashboard outcome, audiences, decisions, actions, review cadence,
   devices, accessibility target, data sensitivity, latency needs, and owners.
2. Separate executive, managerial, operational, analytical, and diagnostic needs.
   Create role-specific views when one screen would mix incompatible decisions,
   detail, permissions, or time horizons.
3. Define each metric with a stable ID, business question, formula, grain, units,
   dimensions, inclusions, exclusions, source, owner, refresh, latency, time zone,
   target, comparison, quality rule, and effective version using
   [references/dashboard-design-standard.md](references/dashboard-design-standard.md).
4. Trace metrics through source systems, transformations, semantic definitions,
   caches, APIs, and display. Define reconciliation and behavior for stale,
   delayed, partial, missing, disputed, revised, or unauthorized data.
5. Establish hierarchy: outcome and exception summary first, drivers next,
   diagnostic detail on demand. Use progressive disclosure instead of placing
   every available metric above the fold.
6. Choose tables, scorecards, lines, bars, distributions, scatterplots, maps,
   funnels, cohorts, timelines, or other encodings based on the analytical task.
   Avoid visual decoration that weakens accurate comparison.
7. Define baseline, target, variance, trend, distribution, denominator, sample
   size, confidence, and materiality where applicable. Explain directionality and
   do not imply causality from correlation.
8. Define filters, segments, date ranges, comparison periods, saved views,
   defaults, cross-filtering, drill-down, drill-through, reset, URL state, export,
   and the effect each selection has on metric meaning.
9. Link exceptions and insights to a responsible action, workflow, owner, evidence,
   and result. Distinguish informational dashboards from control surfaces; require
   authorization, confirmation, idempotency, audit, and reconciliation for writes.
10. Define default, loading, skeleton, empty, zero, partial, stale, delayed,
    unavailable, no-access, error, offline, high-volume, and export states. Never
    render missing data as zero.
11. Specify responsive hierarchy, table behavior, keyboard flow, focus, semantic
    headings, accessible names, contrast, patterns, zoom, reflow, chart summaries,
    data tables, tooltips, status announcements, reduced motion, and print or
    export alternatives.
12. Define permissions at metric, dimension, row, tenant, resource, export, alert,
    and action levels. Prevent restricted values from leaking through totals,
    tooltips, filters, caches, URLs, files, logs, or analytics.
13. Define query budgets, pre-aggregation, pagination, sampling disclosures,
    caching, concurrency, timeouts, cancellation, progressive loading, and
    observability. Preserve definition and freshness metadata with cached results.
14. Test formulas, lineage, edge cases, time boundaries, currencies, units,
    filters, permissions, tenant isolation, stale data, large values, localization,
    accessibility, responsiveness, export parity, performance, and user decisions.
15. Establish metric approval, definition versioning, change communication,
    deprecation, usage analytics, owner review, feedback, and dashboard retirement.
16. Deliver with
    [assets/dashboard-design-template.md](assets/dashboard-design-template.md).

## Rules

- Do not add a metric without a named decision, definition, source, and owner.
- Do not display missing, delayed, suppressed, or inapplicable data as zero.
- Do not truncate axes, aggregate categories, or use area and volume in ways that
  materially distort comparison.
- Do not use color alone for status or encode red and green without accessible
  alternatives.
- Do not expose restricted detail through aggregates, filters, exports, tooltips,
  URLs, or drill paths.
- Do not let a dashboard action bypass authoritative permission and business rules.
- Do not present forecasts, estimates, samples, or AI-generated summaries as
  observed fact.
- Do not call a dashboard successful based on views alone; measure decision and
  action outcomes.

## Handoff

Provide the audience and decision map, metric catalog and lineage, information
hierarchy, visualization rationale, filter and drill contracts, state matrix,
action and alert design, permission model, accessibility and responsive behavior,
performance plan, test and reconciliation plan, governance, risks, assumptions,
and open decisions.
