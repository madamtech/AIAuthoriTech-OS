import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { importCaptures } from "./import-gpt-capture.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const inventory = JSON.parse(fs.readFileSync(path.join(root, "tools/gpt-inventory.json"), "utf8"));
const manifestRoot = path.join(root, "gpts/manifests");
const statusLabels = new Set(["Only me", "Anyone with a link", "Everyone", "Public"]);

function inventoryCapture(item) {
  const lines = item.summary_lines || [];
  const sharing = [...lines].reverse().find(line => statusLabels.has(line)) || null;
  const description = lines.find(line => !statusLabels.has(line) && !/^\d+\s+Chats?$/i.test(line)) || null;
  return {
    ...item,
    description,
    instructions: null,
    conversation_starters: [],
    knowledge_files: [],
    capabilities: [],
    apps_actions: [],
    sharing_status: sharing,
    authoritative: false,
    needs_review: [
      "Full Builder instructions were not captured",
      "Conversation starters were not captured",
      "Knowledge file names were not captured",
      "Enabled capabilities were not captured",
      "Apps and actions were not captured"
    ]
  };
}

const existingIds = new Set();
for (const entry of fs.readdirSync(manifestRoot, { withFileTypes: true })) {
  const file = path.join(manifestRoot, entry.name, "manifest.json");
  if (entry.isDirectory() && fs.existsSync(file)) existingIds.add(JSON.parse(fs.readFileSync(file, "utf8")).gpt_id);
}
const missing = inventory.filter(item => !existingIds.has(`AA-GPT-${String(item.index).padStart(6, "0")}`));
importCaptures(missing.map(inventoryCapture));

// Reconcile every record to the final inventory so names and public GPT URLs are exact.
for (const item of inventory) {
  const wantedId = `AA-GPT-${String(item.index).padStart(6, "0")}`;
  for (const entry of fs.readdirSync(manifestRoot, { withFileTypes: true })) {
    const file = path.join(manifestRoot, entry.name, "manifest.json");
    if (!entry.isDirectory() || !fs.existsSync(file)) continue;
    const manifest = JSON.parse(fs.readFileSync(file, "utf8"));
    if (manifest.gpt_id !== wantedId) continue;
    manifest.name = item.name;
    manifest.runtime.live_gpt_url = item.visible_url;
    fs.writeFileSync(file, `${JSON.stringify(manifest, null, 2)}\n`);
    break;
  }
}

const manifests = fs.readdirSync(manifestRoot, { withFileTypes: true })
  .filter(entry => entry.isDirectory() && fs.existsSync(path.join(manifestRoot, entry.name, "manifest.json")))
  .map(entry => ({ dir: entry.name, manifest: JSON.parse(fs.readFileSync(path.join(manifestRoot, entry.name, "manifest.json"), "utf8")) }))
  .filter(({ manifest }) => /^AA-GPT-\d{6}$/.test(manifest.gpt_id))
  .sort((a, b) => a.manifest.gpt_id.localeCompare(b.manifest.gpt_id));

const authoritative = manifests.filter(x => x.manifest.status === "captured");
const review = manifests.filter(x => x.manifest.status !== "captured");
const visual = manifests.filter(x => x.manifest.skills.default_enhancements.length);
const knowledgeCount = manifests.reduce((n, x) => n + x.manifest.configuration.knowledge_files.length, 0);
const actionCount = manifests.reduce((n, x) => n + x.manifest.configuration.actions.length, 0);
const entry = ({ dir, manifest }) => ({
  gpt_id: manifest.gpt_id,
  name: manifest.name,
  manifest: `gpts/manifests/${dir}/manifest.json`,
  live_gpt_url: manifest.runtime.live_gpt_url,
  status: manifest.status,
  authoritative: manifest.status === "captured",
  needs_review: manifest.status !== "captured"
});

const registry = {
  registry_version: "2.1.0",
  updated_at: "2026-08-06",
  purpose: "Record verified GPT configurations, discovered GPT references, deployment mappings, and reusable AIAuthoriTech-OS skill dependencies.",
  source_of_truth_policy: "A GPT becomes authoritative only after all visible Builder fields have been captured. Unreadable, inaccessible, or incomplete fields remain needs-review and are never guessed.",
  manifest_schema: "schemas/gpt-manifest.schema.json",
  default_enhancements: [{
    skill: "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md",
    status: "mapped",
    applies_when: "Image generation is enabled or the visible GPT purpose includes visual design, branding, thumbnails, product imagery, editing, 3D references, or marketing graphics."
  }],
  authoritative_gpts: authoritative.map(entry),
  discovered_gpts: review.map(entry),
  inventory_status: {
    state: review.length ? "captured-with-review-items" : "captured",
    total_count: manifests.length,
    authoritative_count: authoritative.length,
    needs_review_count: review.length,
    completeness: review.length ? "partial" : "complete"
  }
};
fs.writeFileSync(path.join(root, "registries/gpts.json"), `${JSON.stringify(registry, null, 2)}\n`);

const reviewLines = review.map(({ manifest }) => `- ${manifest.gpt_id} — ${manifest.name}: incomplete visible Builder capture`).join("\n");
const visualLines = visual.map(({ manifest }) => `- ${manifest.gpt_id} — ${manifest.name}`).join("\n");
const report = `# Custom GPT Capture Report — 2026-08-06

## Summary

- Total GPTs found: **${manifests.length}**
- Fully captured and authoritative: **${authoritative.length}**
- Partially captured / needs-review: **${review.length}**
- Knowledge files identified: **${knowledgeCount}**
- Apps or actions identified: **${actionCount}**
- GPTs receiving Visual Intelligence Enhancement: **${visual.length}**

The audit records only visible Builder information. Passwords, API keys, OAuth tokens, secrets, and action credentials were excluded. A GPT is authoritative only when all visible Builder fields were captured; incomplete records are explicitly marked \`discovered-unverified\` and \`needs-review\`.

## Visual Intelligence Enhancement mappings

${visualLines || "- None"}

## Items requiring manual review

${reviewLines || "- None"}

## Global review note

- Business/domain ownership mappings retain each GPT's visible purpose, but the repository business classification requires owner review.
- No live GPT configuration was modified during this audit.
`;
fs.mkdirSync(path.join(root, "reports"), { recursive: true });
fs.writeFileSync(path.join(root, "reports/gpt-capture-report-2026-08-06.md"), report);
console.log(JSON.stringify({ total: manifests.length, authoritative: authoritative.length, needsReview: review.length, knowledgeCount, actionCount, visualCount: visual.length, added: missing.length }));
