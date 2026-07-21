---
name: workflow-composer
description: Design governed end-to-end workflows coordinating multiple skills, tools, people, decisions, shared state, validation, approvals, retries, and recovery. Use when asked to compose, orchestrate, or document a multi-stage workflow rather than one cohesive skill.
---

# Workflow Composer

1. Define trigger, terminal outcome, owner, participants, and scope.
2. Confirm every referenced capability exists and accepts the preceding output.
3. Define minimal shared state.
4. For each stage specify executor, inputs, action, outputs, validation, and failure.
5. Add branches only for real decision conditions.
6. Require approval before consequential external actions lacking prior authority.
7. Bound retries and define escalation after exhaustion.
8. Validate handoffs, recovery, authorization, and completion criteria.
9. Assign identity and catalog relationships.

Do not disguise one skill as a workflow, reference nonexistent dependencies, allow
unbounded retries, or treat attempted actions as completed. Preserve evidence
lineage and minimize sensitive state.
