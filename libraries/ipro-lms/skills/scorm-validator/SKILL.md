---
name: scorm-validator
description: Validate a SCORM package's structure, manifest, launch behavior, runtime communication, completion, status, score, bookmarking, and LMS compatibility. Use before LMS release or when diagnosing a package that imports but does not track correctly.
---

# SCORM Validator

Separate package defects, content defects, LMS configuration issues, and integration symptoms.

## Workflow

1. Identify SCORM version, authoring tool, package version, target LMS, browsers, and expected completion behavior.
2. Inspect ZIP root structure, `imsmanifest.xml`, resources, launch files, identifiers, dependencies, and referenced paths.
3. Validate launch and runtime API discovery in a safe test environment.
4. Test initialization, status, completion, success, score, suspend data, location, commit, termination, and resume behavior as applicable.
5. Run first attempt, pass, fail, exit/resume, relaunch, completion, and cross-browser scenarios.
6. Compare observed LMS records to expected results and isolate the likely fault domain.

## Output

Provide package metadata, structural findings, runtime event evidence, scenario results, LMS record comparison, defect severity, likely cause, remediation, limitations, and release recommendation.

## Guardrails

- Do not modify the source package unless requested and authorized.
- Never treat successful import as successful tracking.
- Distinguish SCORM 1.2 and 2004 data-model rules.
- Sanitize learner data, URLs, tokens, and proprietary content.

