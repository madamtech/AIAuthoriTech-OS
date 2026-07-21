# Instruction layer standard

Keep these concerns distinct:

1. **Canonical stable instructions:** purpose, non-goals, authority, precedence,
   behavioral rules, approvals, safety, failure, and output contracts.
2. **Skills and workflows:** reusable procedures loaded when relevant.
3. **Tool contracts:** schemas, permissions, preconditions, effects, verification,
   errors, retry, and compensation.
4. **Knowledge:** sourced domain facts and policies with provenance and freshness.
5. **Runtime context:** current user, task, environment, permissions, and state.
6. **User input:** desired outcome and constraints within higher-priority rules.

## Testable rule pattern

Prefer:

`When <observable condition>, perform <bounded action>; require <evidence or
approval>; otherwise <fallback>.`

Avoid absolute rules that conflict with legitimate recovery, and avoid soft verbs
such as “try,” “generally,” or “ideally” when the behavior must be enforceable.
