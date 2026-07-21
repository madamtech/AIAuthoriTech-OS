# Prompt-to-App Standard

Use this standard to preserve traceability while progressively converting an idea
into build instructions.

## Statement classification

Assign each extracted statement one state:

- **Confirmed:** supported by approved evidence or an authorized decision.
- **Inferred:** reasonably derived from evidence but not explicitly approved.
- **Assumed:** temporarily selected to continue; state impact and reversal point.
- **Proposed:** a recommendation awaiting a decision.
- **Conflicting:** incompatible evidence or directions exist.
- **Unknown:** material information is absent.

Never promote a statement to confirmed merely because a coding tool implemented it.

## Question and stop rules

Ask or create a decision gate when uncertainty changes:

- the primary user or business outcome;
- data sensitivity, ownership, retention, or location;
- authentication, authorization, payment, regulated activity, or legal claims;
- irreversible migrations or external effects;
- platform reach, native capability, cost, or vendor commitment;
- acceptance conditions or production authority.

Proceed with a labeled assumption when the decision is reversible, isolated, does
not expose sensitive data, and has an explicit review point.

## Canonical packet before adapter

Keep the canonical packet independent of a vendor:

1. outcome, actors, scope, requirements, and acceptance;
2. journeys, states, content, data, access, and integrations;
3. quality attributes and architecture boundaries;
4. vertical slices and verification gates;
5. change, decision, and risk controls.

Put framework syntax, proprietary components, platform deployment steps, and
provider limitations in an adapter. Do not let the adapter become the only record
of product behavior.

## Vertical-slice contract

Every slice must state:

- slice ID, outcome, user, entry state, and verified terminal state;
- included and excluded requirements;
- files, components, entities, endpoints, migrations, and dependencies in scope;
- UI states and accessibility behavior;
- data and authorization rules;
- integration stubs, fixtures, and failure behavior;
- prohibited changes and protected decisions;
- automated and manual acceptance evidence;
- rollback or reset method;
- handoff summary and open decisions.

Prefer a walking skeleton that proves repository, environment, navigation,
authentication boundary, data path, deployment preview, and observability before
adding feature breadth.

## Prompt construction

A bounded coding prompt should:

1. name exactly one slice;
2. link or quote the authoritative requirements;
3. specify the working context and files in scope;
4. distinguish implementation facts from assumptions;
5. describe states, errors, access rules, and data contracts;
6. forbid unrelated refactors, dependency churn, secrets, and production changes;
7. require tests and verification commands;
8. require a changed-file, migration, dependency, test, and limitation summary;
9. stop on ambiguity that crosses a decision gate.

Do not ask a generation system to “finish the app” without a bounded contract.

## Checkpoint evidence

After each slice, verify:

- only intended files, dependencies, configuration, and schemas changed;
- generated migrations are reviewed and recoverable;
- credentials and sensitive data are absent;
- requirements trace to code and tests;
- authorization is enforced outside the UI;
- normal, denied, invalid, empty, loading, error, retry, and recovery states work;
- accessibility and responsive or adaptive behavior have evidence;
- APIs, jobs, webhooks, AI tools, payments, messages, and other external effects
  reconcile against an authoritative source;
- build, static checks, tests, and preview run successfully;
- protected decisions remain unchanged.

Record evidence, deviations, owner, and disposition before opening the next slice.

## Change control

Give every material change a unique ID. Record request, reason, source, affected
requirements, data, access, architecture, UX, tests, cost, schedule, risk,
decision owner, disposition, and version. Update the canonical packet before
issuing replacement prompts.
