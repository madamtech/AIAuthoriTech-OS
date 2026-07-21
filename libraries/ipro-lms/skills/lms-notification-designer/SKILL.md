---
name: lms-notification-designer
description: Design governed LMS notifications for enrollment, reminders, due dates, completions, expirations, cancellations, failures, and escalations. Use when defining message triggers, audiences, timing, templates, suppression, localization, and delivery validation.
---

# LMS Notification Designer

Create useful communications without duplication, message fatigue, privacy leakage, or ambiguous timing.

## Workflow

1. Identify the learner event, business purpose, owner, audience, channel, urgency, timezone, and desired action.
2. Define trigger conditions, timing, recurrence, stop conditions, suppression, escalation, and exception behavior.
3. Map approved merge fields to authoritative sources and provide fallbacks for missing values.
4. Draft concise subject and body copy with clear action, deadline, support route, accessibility, and localization requirements.
5. Check overlaps with LMS, CRM, calendar, and manual communications.
6. Test eligible and ineligible recipients, date boundaries, completed learners, failed deliveries, duplicates, and privacy.
7. Define monitoring, ownership, change control, and retirement criteria.

## Output

Provide a notification inventory, trigger matrix, audience logic, approved copy, merge-field dictionary, test cases, escalation flow, and monitoring measures.

## Guardrails

- Do not include sensitive learner details unnecessarily.
- State timezone and deadline logic.
- Stop reminders promptly after the qualifying event.
- Require owner approval before enabling production sends.

