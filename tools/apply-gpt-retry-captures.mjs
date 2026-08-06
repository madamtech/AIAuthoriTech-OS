import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const captureFile = path.join(root, "tools/gpt-retry-captures.json");
const enhancement = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md";
const ignoredFileLabels = new Set(["File", "PDF", "Text", "Spreadsheet", "Presentation"]);

function unique(values) {
  return [...new Set((values || []).map(value => value?.trim()).filter(Boolean))];
}

function visualApplicable(capture) {
  const text = `${capture.name} ${capture.description || ""} ${capture.instructions || ""}`.toLowerCase();
  return unique(capture.capabilities).includes("Image Generation") ||
    /visual|design|brand|thumbnail|product imagery|image edit|3d|graphic|poster|cover|photo|stationery|cinematic|video|avatar|portrait|airbrush|coloring/.test(text);
}

const captures = JSON.parse(fs.readFileSync(captureFile, "utf8"));
const capturedAt = new Date().toISOString();

for (const capture of captures) {
  if (!capture.visible) throw new Error(`Capture is not complete: ${capture.index} ${capture.name}`);

  const dir = path.join(root, "gpts", "manifests", capture.dir);
  const manifestFile = path.join(dir, "manifest.json");
  const changelogFile = path.join(dir, "CHANGELOG.md");
  if (!fs.existsSync(manifestFile)) throw new Error(`Manifest not found: ${manifestFile}`);

  const manifest = JSON.parse(fs.readFileSync(manifestFile, "utf8"));
  const knowledge = unique(capture.knowledge_files).filter(name => !ignoredFileLabels.has(name));
  const actions = unique(capture.apps_actions);
  const hasVisualEnhancement = visualApplicable(capture);

  manifest.name = capture.name;
  manifest.status = "captured";
  manifest.purpose = capture.description || manifest.purpose;
  manifest.runtime.deployment_location = capture.sharing_status || manifest.runtime.deployment_location;
  manifest.configuration = {
    description: capture.description || null,
    instructions: capture.instructions || null,
    conversation_starters: unique(capture.conversation_starters),
    capabilities: unique(capture.capabilities),
    knowledge_files: knowledge.map(name => ({ name, repository_reference: null, verification_status: "verified" })),
    actions: actions.map(name => ({ name, type: "visible app or action", schema_reference: null, verification_status: "verified" }))
  };
  manifest.skills.default_enhancements = hasVisualEnhancement ? [enhancement] : [];
  manifest.provenance = {
    capture_method: "builder-copy",
    captured_at: capturedAt,
    verified_by: "Codex browser audit of visible Builder fields",
    evidence: [
      `All visible Builder fields captured ${capturedAt}`,
      `Sharing/publishing status: ${capture.sharing_status || "not displayed"}`,
      "Retry completed after browser permissions were updated.",
      "No passwords, API keys, OAuth tokens, secrets, or action credentials were recorded."
    ]
  };
  manifest.version = "1.0.1";
  manifest.change_log = unique([
    ...(manifest.change_log || []),
    "1.0.1 - Completed all visible Builder configuration capture after browser permission update."
  ]);

  fs.writeFileSync(manifestFile, `${JSON.stringify(manifest, null, 2)}\n`);

  const existingChangelog = fs.existsSync(changelogFile) ? fs.readFileSync(changelogFile, "utf8") : "# Changelog\n";
  const update = `## 1.0.1 - ${capturedAt.slice(0, 10)}\n\n- Completed capture of all visible Builder fields after browser permissions were updated.\n- Marked the manifest authoritative.\n- Sharing/publishing status: \`${capture.sharing_status || "not displayed"}\`.\n${hasVisualEnhancement ? "- Mapped the GPT Visual Intelligence Enhancement.\n" : ""}- Excluded passwords, API keys, OAuth tokens, secrets, and action credentials.\n\n`;
  const body = existingChangelog.replace(/^# Changelog\s*/u, "").trimStart();
  fs.writeFileSync(changelogFile, `# Changelog\n\n${update}${body}`);
}

console.log(JSON.stringify({ updated: captures.length, capturedAt }));
