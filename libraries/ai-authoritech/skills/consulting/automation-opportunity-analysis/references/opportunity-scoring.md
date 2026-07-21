# Opportunity scoring

Score supported criteria from 0 to 4.

## Value — 45 points

| Criterion | Weight |
|---|---:|
| Time or capacity released | 10 |
| Error and rework reduction | 8 |
| Customer or employee impact | 8 |
| Financial value or cost avoidance | 8 |
| Risk and control improvement | 6 |
| Strategic alignment and learning value | 5 |

## Feasibility — 35 points

| Criterion | Weight |
|---|---:|
| Process stability and standardization | 8 |
| Data availability and quality | 8 |
| System and integration readiness | 7 |
| Technical suitability | 6 |
| Owner and stakeholder readiness | 6 |

## Delivery confidence — 20 points

| Criterion | Weight |
|---|---:|
| Evidence coverage | 8 |
| Implementation effort predictability | 5 |
| Control, privacy, and security readiness | 5 |
| Measurement readiness | 2 |

Calculate each section as `sum((score / 4) × weight)` and total to 100.

Do not issue a definitive priority below 60% evidence coverage. Report uncertainty
and use score ranges when material inputs are estimated.

## Priority guidance

- 80–100: strong candidate, subject to blockers
- 65–79: viable candidate with prerequisites
- 50–64: investigate, redesign, or foundation first
- below 50: do not prioritize

A score never overrides a blocker. Examples include prohibited processing,
unmitigated safety exposure, unavailable required data, no accountable owner,
unacceptable control loss, or a disputed current-state process.
