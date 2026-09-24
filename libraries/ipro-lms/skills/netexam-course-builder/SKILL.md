---
name: netexam-course-builder
description: Translate an approved course blueprint and source content into a NetExam course build specification covering objects, files, settings, enrollment, completion, visibility, certificates, reporting, and QA. Use before configuring or releasing NetExam learning content. Use when asked to (1) build netexam course, (2) refine netexam course, (3) validate netexam course, or (4) standardize netexam course.
---

# NetExam Course Builder

Use the [operating standard](references/netexam-course-standard.md) and [working template](assets/netexam-course-build-template.md).

Create a traceable build plan and release package for a NetExam course.

## Procedure

1. Confirm approved objectives, source files, audience, owners, version, languages, prerequisites, completion evidence, and release date.
2. Inventory course objects, modules, SCORM or media packages, assessments, resources, certificates, and related certifications.
3. Define titles, descriptions, metadata, categories, branch visibility, enrollment rules, due dates, credits, and completion settings.
4. Map content versions and replacement behavior, including transcript and reporting impacts.
5. Define accessibility, browser, launch, tracking, and mobile acceptance criteria.
6. Build functional, completion, failure, resume, visibility, reporting, and regression test cases.
7. Plan approvals, publication, communications, monitoring, and rollback.

## Output Contract

Provide a course object inventory, field/configuration matrix, content map, audience rules, version plan, test evidence requirements, release checklist, and unresolved risks.

## Guardrails

- Do not alter approved learning content silently.
- Verify NetExam behavior in the applicable environment.
- Preserve historical completion and reporting requirements.
- Keep secure links, learner data, and credentials out of examples.

## Recovery

If source content, completion rules, audience visibility, object dependencies, test evidence, or production approval is missing, keep the course in a nonproduction state. Document the gap and require controlled validation.
