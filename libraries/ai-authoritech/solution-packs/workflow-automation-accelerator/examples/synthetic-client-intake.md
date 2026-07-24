# Controlled Synthetic Client Intake Automation

A fictional consultancy requested automation from an approved intake form to CRM opportunity creation and an internal review task. The design used synthetic systems, excluded client messaging and contracts, required a deterministic idempotency key, and routed ambiguous submissions to a human reviewer.

Controlled cases covered duplicates, malformed fields, expired authorization, CRM timeout, successful write with a lost response, partial task failure, retry exhaustion, reconciliation, and rollback. Duplicate submissions reused the existing opportunity, uncertain writes triggered reconciliation before retry, and incomplete downstream work entered an owned exception queue.

The result was **conditional pass**. Production readiness remained blocked pending live API verification, secrets configuration, load testing, operations approval, and incident-response rehearsal.
