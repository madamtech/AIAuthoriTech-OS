---
name: scorm-validator
description: Validate a SCORM package's archive structure, manifest, resources, launch behavior, runtime API communication, completion, success, score, bookmarking, resume, termination, browser behavior, and LMS records. Use before release or when tracking fails. Do not expose proprietary content, modify source without approval, or confuse successful import with valid runtime behavior. Use when asked to (1) create scorm validator, (2) review scorm validator, (3) improve scorm validator, or (4) standardize scorm validator.
---

# SCORM Validator

Use the [SCORM validation standard](references/scorm-validation-standard.md) and [SCORM test record template](assets/scorm-test-record-template.md).

## Procedure

1. Identify SCORM version, authoring tool, package version, target LMS, browsers, and expected completion behavior.
2. Inspect ZIP root structure, `imsmanifest.xml`, resources, launch files, identifiers, dependencies, and referenced paths.
3. Validate launch and runtime API discovery in a safe test environment.
4. Test initialization, status, completion, success, score, suspend data, location, commit, termination, and resume behavior as applicable.
5. Run first attempt, pass, fail, exit/resume, relaunch, completion, and cross-browser scenarios.
6. Compare observed LMS records to expected results and isolate the likely fault domain.

## Output Contract

Provide package metadata, structural findings, runtime event evidence, scenario results, LMS record comparison, defect severity, likely cause, remediation, limitations, and release recommendation.

## Guardrails

- Do not modify the source package unless requested and authorized.
- Never treat successful import as successful tracking.
- Distinguish SCORM 1.2 and 2004 data-model rules.
- Sanitize learner data, URLs, tokens, and proprietary content.

## Recovery

If the package version, expected completion behavior, test environment, runtime evidence, or LMS record access is unavailable, limit the conclusion to the validated layer. Preserve console and runtime evidence, identify the likely fault domain, and do not certify compatibility.
