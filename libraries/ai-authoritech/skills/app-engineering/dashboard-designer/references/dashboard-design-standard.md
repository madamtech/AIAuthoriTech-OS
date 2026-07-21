# Dashboard Design Standard

## Metric contract

Every metric must define:

- stable ID, display name, business question, and decision;
- formula, numerator, denominator, grain, units, precision, and directionality;
- included and excluded records, status rules, and effective dates;
- time zone, calendar, period boundary, comparison, target, and materiality;
- dimensions, permitted filters, privacy suppression, and authorization;
- source of truth, transformations, freshness, latency, lineage, and owner;
- missing, partial, stale, revised, disputed, and unavailable behavior;
- validation, reconciliation, version, approval, and review cadence.

## Visualization selection

| Analytical task | Prefer | Avoid |
|---|---|---|
| Trend over ordered time | Line or aligned bars | Pie charts and unordered categories |
| Category comparison | Sorted bars or table | Decorative area and 3D shapes |
| Part-to-whole | Stacked bars with few parts | Many slices or changing denominators |
| Distribution | Histogram, box plot, percentile table | Averages without spread |
| Relationship | Scatterplot with context | Dual axes that imply a false link |
| Exact lookup | Table or scorecard | Encoding precise values only by position |
| Process conversion | Stage table or funnel with denominators | Funnel shapes without comparable bases |
| Geography | Map only when location is analytically relevant | Maps for ordinary category ranking |

Show units, denominators, date ranges, and freshness near the result.

## States and trust

Distinguish zero, no records, unavailable, unauthorized, suppressed, not
applicable, delayed, partial, stale, estimated, sampled, forecast, and disputed.
Expose last successful refresh, expected cadence, source, and recovery guidance.

## Accessible charts

Provide a concise title that states the question, a text summary of the main
pattern, semantic labels, keyboard access where interactive, visible focus, high-
contrast non-color cues, accessible tooltips, and an equivalent data table or
download. Ensure zoom and reflow do not hide information or actions.

## Dashboard actions

For write actions define authorized actor, resource, command, validation,
confirmation, idempotency, effect, audit, status, failure, retry, reconciliation,
undo or compensation, and escalation. A successful request is not proof the
business effect completed.

## Validation

Reconcile dashboard totals with authoritative sources using controlled fixtures
and production-safe checks. Test time-zone boundaries, daylight saving,
late-arriving data, duplicates, revised events, divide-by-zero, nulls, currency,
rounding, privacy thresholds, role and tenant isolation, filters, exports, cache
invalidation, and schema changes.
