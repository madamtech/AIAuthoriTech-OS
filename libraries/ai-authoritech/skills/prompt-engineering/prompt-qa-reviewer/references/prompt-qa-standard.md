# Prompt QA Standard

## Review domains

| Domain | Evidence expected |
|---|---|
| Identity | Stable IDs, exact versions, provenance, hashes or immutable references |
| Contract | Task, non-goals, authority, precedence, uncertainty, completion |
| Context | Typed variables, trust, sensitivity, freshness, delimiters, budgets |
| Output and tools | Schema, failure state, least privilege, side effects, verification |
| Tests | Traceability, representative splits, leakage controls, raw results |
| Safety and privacy | Injection, prohibited action, data handling, escalation evidence |
| Portability | Adapter parity, limitations, fallbacks, re-evaluation triggers |
| Operations | Ownership, monitoring, incidents, rollout, rollback, deprecation |

## Severity

- **Critical:** Enables unauthorized or harmful action; exposes protected data;
  corrupts evidence integrity; falsely reports completion; or lacks a viable
  rollback for a material release. Block approval.
- **High:** Breaks a required behavior, supported segment, mandatory schema, or
  material adapter; or leaves a major risk untested. Block approval unless the
  affected capability is removed from scope.
- **Medium:** Degrades reliability, maintainability, observability, or coverage
  without violating a hard gate. Require a dated remediation condition.
- **Low:** Minor clarity, consistency, or documentation defect with limited effect.

## Verdict rules

Approve only when all required artifacts are version-aligned, hard gates pass,
test evidence supports the complete approval boundary, and operational controls
match the risk. Approve with conditions only for non-blocking defects with owners,
deadlines, monitoring, and a limited approval boundary. Reject when a blocking
defect is confirmed. Use inconclusive when evidence identity, coverage, sample
size, grader reliability, or reproducibility cannot support a decision.

Every defect must cite inspectable evidence and define the minimum retest surface.
Every closed defect must link the corrected version and fresh evidence. Preserve
superseded findings for audit history.
