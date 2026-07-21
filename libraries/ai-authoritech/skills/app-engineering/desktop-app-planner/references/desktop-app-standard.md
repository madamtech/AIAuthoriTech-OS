# Desktop Application Standard

Use this standard to make architecture, security, packaging, and lifecycle
decisions explicit.

## Architecture decision

Compare viable approaches against:

- supported operating systems and required native fidelity;
- local files, devices, GPU, background, and offline requirements;
- accessibility and input-method behavior;
- application and runtime footprint;
- UI and application-core isolation;
- web-content and native-bridge exposure;
- team capability, test burden, release independence, and total ownership cost;
- vendor or framework lifecycle and a credible migration path.

Select one approach only after documenting rejected options and the conditions
that would reopen the decision.

## Trust boundaries and privileges

Treat the UI, webview or renderer, application core, local database, plugins,
document parsers, update service, privileged helper, operating system, and remote
services as distinct trust zones.

- Run the normal application as the signed-in OS user.
- Put elevated operations behind the smallest possible helper.
- Authenticate and authorize every privileged request.
- Allow-list commands and validate canonical paths, arguments, ownership, and
  expected state inside the privileged boundary.
- Never pass arbitrary command lines, scripts, environment variables, registry
  edits, service definitions, or filesystem targets to an elevated helper.
- Version IPC contracts and reject unknown messages or callers.
- Sandbox untrusted content and disable capabilities it does not require.

## Local data and files

Identify an authoritative owner for every data class. Use platform-supported
locations for configuration, cache, state, logs, documents, and secrets.

- Use atomic replace and durable checkpoints for important writes.
- Preserve recovery copies until the new state is verified.
- Detect external edits and file locks; never silently choose a winner.
- Version databases and documents. Make migrations restartable and preserve a
  tested recovery path.
- Separate OS users and application accounts. Define behavior for account switch,
  logout, machine transfer, backup, restore, retention, and deletion.
- Store secrets in an OS-backed credential facility when available.

## IPC and local services

For each endpoint or message, define caller identity, authorization, schema,
maximum size, timeout, cancellation, replay behavior, idempotency, rate limit,
version, safe error, and auditable event. Bind local services to the narrowest
interface. Do not assume loopback alone is an authentication boundary.

## Packaging and signing

Maintain a deterministic build, dependency and license inventory, source revision,
build identity, checksums, signing identity, timestamp, and artifact retention.
Protect signing material with restricted automation or hardware-backed storage.

For each operating system, define:

- package and installer format;
- user or machine install scope;
- elevation points and policy;
- signing and notarization requirements;
- file, protocol, menu, tray, service, or startup registration;
- repair, uninstall, residual user data, and managed-deployment behavior.

Test packages from clean machines, not only developer environments.

## Updates

Use signed update metadata and packages. Verify product, publisher, channel,
architecture, version monotonicity, digest, signature, and compatibility before
installation.

Separate download, verification, staging, migration, activation, health check,
and cleanup. Make interrupted updates recoverable. Keep the last known-good
version until the observation window closes. Define rollback limits when data
migrations are not backward compatible.

Support staged rollout, pause, revocation, forced-update exceptions, proxy-aware
downloads, metered-network policy, and enterprise-controlled channels.

## Compatibility and testing

Create a supported matrix across OS version, CPU architecture, hardware tier,
display scale, multiple monitors, locale, input method, assistive technology,
security software, proxy, device, and installation method.

Test at minimum:

- clean install, upgrade, interrupted update, repair, and uninstall;
- first run, multiple instances, sleep, wake, lock, shutdown, and crash recovery;
- files, associations, links, clipboard, notifications, and devices;
- keyboard, screen reader, scaling, contrast, reduced motion, and localization;
- low disk, corrupt state, denied access, offline operation, and synchronization;
- malformed IPC, malicious files, hostile web content, plugin failure, and
  privileged-boundary abuse;
- CPU, memory, GPU, disk, network, energy, start time, and idle activity.

Record real-device evidence for each supported platform family.

## Operational readiness

Define redacted logs, crash capture, update health, version adoption, performance,
resource use, OS-specific defects, installation failures, support bundles,
diagnostic consent, retention, access, incident response, release-channel
ownership, supported-version policy, deprecation, export, and retirement.
