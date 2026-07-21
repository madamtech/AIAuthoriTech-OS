# Agent QA Standard

## Evaluation domains

| Domain | Minimum evidence |
|---|---|
| Requirements and architecture | Traceability from approved requirements and controls to tests |
| Instructions | Precedence, scope, ambiguity, conflict, refusal, and injection behavior |
| Knowledge and memory | Retrieval relevance, grounding, citation, freshness, access, retention, and isolation |
| Tools | Schema validation, least privilege, authorization, effect verification, idempotency, and failure handling |
| Workflows and state | Transitions, checkpoints, handoffs, retries, compensation, concurrency, recovery, and completion |
| Permissions and approvals | Role enforcement, approval binding, rejection, expiry, amendment, and unavailable-reviewer behavior |
| Safety, security, and privacy | Misuse, leakage, injection, privilege escalation, unsafe action, and cross-user contamination |
| Output quality | Accuracy, completeness, usability, accessibility, and uncertainty communication |
| Reliability and efficiency | Repeatability, availability assumptions, latency, token use, tool cost, and budget enforcement |
| Operations | Logs, traces, alerts, incident response, rollback, support ownership, change control, and retirement |

Test representative combinations when controls interact. A tool test alone does not
prove the workflow safely authorizes or verifies that tool's external effect.

## Evidence grades

1. **Direct:** Observed result from the identified release candidate in a controlled
   or production-like test.
2. **Corroborated:** Direct evidence supported by logs, traces, or verified external
   state.
3. **Indirect:** Configuration, documentation, prior-version results, or owner
   attestation without current behavioral verification.
4. **Unavailable:** No usable evidence. Treat the requirement as untested.

Prefer corroborated evidence for consequential behavior.

## Severity

- **Critical:** Unauthorized or unsafe consequential action, sensitive-data
  exposure, security-control bypass, irreversible corruption, or credible severe
  harm.
- **High:** Core task failure, approval failure, fabricated completion, systematic
  ungrounded behavior, unrecoverable workflow failure, or material policy breach.
- **Medium:** Material quality, reliability, performance, cost, or operational
  problem with a workable control or workaround.
- **Low:** Localized defect with limited impact that does not compromise a release
  gate.

Rate severity from impact and credible exposure, not frequency alone. An
intermittent critical failure remains critical.

## Release gates

A release-candidate verdict requires all of the following:

- No unresolved critical or high-severity defect.
- Every mandatory requirement and control has a passing representative test.
- Safety, authority, approval, and external-effect tests use corroborated evidence.
- Regression metrics meet approved thresholds and budgets.
- Known limitations are documented and reflected in user or operator controls.
- Monitoring, incident response, rollback, and accountable ownership are ready.
- The tested fingerprint matches the proposed release artifact and configuration.

High-risk systems also require production-like evaluation, adversarial coverage,
human-review sampling, and accountable signoff. Never infer readiness from a
weighted average when a mandatory gate fails.

## Test record

For every scenario record:

- ID, requirement, risk, environment, and test data class
- Preconditions and authorization context
- Input, expected outcome, and expected external effect
- Observed output, tool calls, logs, state, and verified external effect
- Repetitions and variance
- Pass, fail, inconclusive, skipped, or blocked status
- Defect reference, severity, owner, and retest requirement

Redact secrets and sensitive data while preserving enough evidence to reproduce
the behavior safely.
