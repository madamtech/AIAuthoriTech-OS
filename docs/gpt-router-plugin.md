# AIAuthoriTech GPT Router Plugin

The `ai-authoritech-os` plugin makes the 93 captured Custom GPT configurations reusable in supported ChatGPT and Codex skill surfaces without turning every GPT into a separate top-level skill.

## Invocation

- ChatGPT skill surface: `@ai-authoritech-gpt-router`
- Codex: `$ai-authoritech-gpt-router`
- Exact selection: `Use AA-GPT-000089 for this request.`
- Name selection: `Use High Fashion OIL IDG for this request.`
- Purpose selection: `Choose the best registered GPT for a 3D-print vendor display.`

Duplicate names must be selected by registry ID. The router never guesses between duplicate `i-PRO Sales Intelligence` or `Untitled` records.

## Included workflows

- `ai-authoritech-gpt-router`: selects the configuration.
- `apply-gpt-configuration`: executes with the selected manifest.
- `check-gpt-skill-compatibility`: evaluates a proposed pairing before deployment.
- `run-gpt-skill-pilot`: runs controlled before-and-after tests.
- `gpt-visual-intelligence-enhancement`: adds the existing evaluation-led visual layer when mapped and applicable.

## Source of truth

The repository manifests remain authoritative. Run the plugin sync script after manifest or registry changes:

```powershell
node .agents/plugins/plugins/ai-authoritech-os/scripts/sync-gpt-library.mjs
```

The plugin contains a distributable snapshot so routing works outside the repository. It does not modify live Custom GPTs. Live updates require a compatible decision, a passing pilot, and explicit deployment authorization.
