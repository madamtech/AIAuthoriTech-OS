---
name: lms-report-analyzer
description: Analyze LMS reports by validating definitions, filters, status semantics, joins, dates, populations, and reconciliation evidence before interpreting trends. Use for completion, enrollment, certification, exam, transcript, adoption, or exception reporting.
---

# LMS Report Analyzer

Produce decisions from LMS data without overstating what the report proves.

## Workflow

1. Clarify the business question, decision owner, population, period, grain, and expected source of truth.
2. Inventory fields, filters, joins, refresh time, timezone, security scope, and export limitations.
3. Define status, completion, overdue, active user, certification, attempt, and score semantics.
4. Check duplicates, missing records, nulls, stale data, version mismatches, and integration latency.
5. Reconcile totals against a trusted control where available.
6. Calculate only metrics supported by the data and separate facts, interpretations, and hypotheses.
7. Prioritize anomalies and recommended follow-up actions.

## Output

Provide question and scope, data dictionary, quality findings, reconciled totals, metrics, segmented observations, anomalies, likely causes, action recommendations, limitations, and reproducible calculation notes.

## Guardrails

- Never equate missing data with zero activity without evidence.
- Protect personal and employment data; report at the least granular level needed.
- State timezone, snapshot date, and filter logic.
- Do not claim causation from descriptive reports alone.

