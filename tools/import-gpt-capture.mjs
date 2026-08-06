import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const enhancement = "libraries/ai-authoritech/skills/image-generation/gpt-visual-intelligence-enhancement/SKILL.md";
const ignoredFileLabels = new Set(["File", "PDF", "Text", "Spreadsheet", "Presentation"]);

function slugify(value) {
  return value.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase()
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "untitled";
}

function slugFor(capture) {
  const base = slugify(capture.name);
  const indexed = `${base}-${String(capture.index).padStart(3, "0")}`;
  if (capture.name === "Untitled") return indexed;

  const existingPath = path.join(repoRoot, "gpts", "manifests", base, "manifest.json");
  if (!fs.existsSync(existingPath)) return base;

  const expectedId = `AA-GPT-${String(capture.index).padStart(6, "0")}`;
  const existing = JSON.parse(fs.readFileSync(existingPath, "utf8"));
  return existing.gpt_id === expectedId ? base : indexed;
}

function visualApplicable(capture) {
  const text = `${capture.name} ${capture.description || ""} ${capture.instructions || ""}`.toLowerCase();
  return (capture.capabilities || []).includes("Image Generation") || /visual|design|brand|thumbnail|product imagery|image edit|3d|graphic|poster|cover|photo|stationery|cinematic|video|avatar|portrait|airbrush|coloring/.test(text);
}

export function importCaptures(captures) {
  const capturedAt = new Date().toISOString();
  for (const capture of captures) {
    const dir = path.join(repoRoot, "gpts", "manifests", slugFor(capture));
    fs.mkdirSync(dir, { recursive: true });
    const knowledge = [...new Set(capture.knowledge_files || [])].filter(x => x && !ignoredFileLabels.has(x));
    const authoritative = Boolean(capture.authoritative);
    const manifest = {
      gpt_id: `AA-GPT-${String(capture.index).padStart(6, "0")}`,
      name: capture.name,
      owner: "Tanika Crawford",
      status: authoritative ? "captured" : "discovered-unverified",
      purpose: capture.description || "Purpose requires review because the Builder description was unreadable.",
      business: "Tanika Crawford / business mapping needs review",
      runtime: {
        platform: "chatgpt-custom-gpt",
        deployment_location: capture.sharing_status || null,
        live_gpt_url: capture.visible_url || null
      },
      configuration: {
        description: capture.description || null,
        instructions: capture.instructions || null,
        conversation_starters: capture.conversation_starters || [],
        capabilities: [...new Set(capture.capabilities || [])],
        knowledge_files: knowledge.map(name => ({ name, repository_reference: null, verification_status: "verified" })),
        actions: [...new Set(capture.apps_actions || [])].map(name => ({ name, type: "visible app or action", schema_reference: null, verification_status: "unverified" }))
      },
      skills: { required: [], optional: [], default_enhancements: visualApplicable(capture) ? [enhancement] : [] },
      evaluation: {
        profile: null,
        required_tests: ["primary-purpose-preservation", "instruction-compliance", "knowledge-grounding", "tool-selection", "visual-lock-preservation-when-applicable"],
        last_result: "not-tested"
      },
      provenance: {
        capture_method: "builder-copy",
        captured_at: capturedAt,
        verified_by: authoritative ? "Codex browser audit of visible Builder fields" : null,
        evidence: [
          `Visible Builder capture attempted ${capturedAt}`,
          `Sharing/publishing status: ${capture.sharing_status || "needs-review"}`,
          ...(capture.needs_review || []).map(x => `needs-review: ${x}`)
        ]
      },
      version: "1.0.0",
      change_log: [authoritative ? "1.0.0 - Initial visible Builder configuration capture." : "1.0.0 - Partial Builder capture; manual review required."]
    };
    fs.writeFileSync(path.join(dir, "manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`);
    fs.writeFileSync(path.join(dir, "CHANGELOG.md"), `# Changelog\n\n## 1.0.0 - ${capturedAt.slice(0, 10)}\n\n- ${authoritative ? "Captured all visible Builder fields." : "Recorded partial Builder data; manual review is required."}\n- Sharing/publishing status: \`${capture.sharing_status || "needs-review"}\`.\n${visualApplicable(capture) ? "- Mapped the GPT Visual Intelligence Enhancement.\n" : ""}${(capture.needs_review || []).map(x => `- Needs review: ${x}\n`).join("")}`);
  }
  return captures.length;
}
