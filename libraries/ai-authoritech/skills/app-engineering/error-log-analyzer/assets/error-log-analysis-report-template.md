# Error Log Analysis Report

## 1. Question and Scope

- Analysis question:
- Time window and time zones:
- Systems, environments, versions, and cohorts:
- Impact and urgency:
- Read-only authority and query limits:

## 2. Source and Quality Inventory

| Source | Producer/collector/store | Time quality | Sampling/loss/retention | Known gaps | Quality |
|---|---|---|---|---|---|

## 3. Redaction and Normalization

- Removed or transformed fields:
- Surrogate identifiers:
- Canonical schema:
- Clock offsets, drift, ingestion delay, and ordering limits:

## 4. Baseline

| Measure | Current | Comparator | Denominator | Change | Segments | Limitation |
|---|---:|---:|---|---:|---|---|

## 5. Event Signatures

| ID | Signature | Unique operations/count | First/last | Affected cohorts | Baseline change | Confidence |
|---|---|---|---|---|---|---|

## 6. Correlated Timeline

| Time | Event/signature | Service/state | Correlation key | Strength | Evidence | Gap/conflict |
|---|---|---|---|---|---|---|

## 7. Failure Structure

- Trigger or entry event:
- Primary failure:
- Downstream symptoms:
- Retries or duplicate reporting:
- Recovery or terminal outcome:
- Missing spans and conflicting evidence:

## 8. Working-versus-Failing Cohorts

| Dimension | Working | Failing | Difference | Confidence |
|---|---|---|---|---|

## 9. Ranked Findings

| Rank | Finding type | Evidence | Outcome/extent | Alternatives | Confidence | Next query/test |
|---:|---|---|---|---|---|---|

Types: observed, associated, anomalous, or hypothesis.

## 10. Observability Gaps

| Gap | Investigation impact | Recommended instrument/change | Owner | Priority |
|---|---|---|---|---|

## 11. Follow-Up

- Exact bounded queries or evidence requests:
- Safety, cost, and access constraints:
- Escalations and owners:
- Open questions:
