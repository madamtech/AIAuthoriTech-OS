import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const pluginRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = path.resolve(pluginRoot, "../../../..");
const routerReferences = path.join(pluginRoot, "skills/ai-authoritech-gpt-router/references");
const manifestSource = path.join(repoRoot, "gpts/manifests");

fs.rmSync(path.join(routerReferences, "manifests"), { recursive: true, force: true });
fs.mkdirSync(path.join(routerReferences, "manifests"), { recursive: true });
fs.copyFileSync(path.join(repoRoot, "registries/gpts.json"), path.join(routerReferences, "gpts.json"));

let count = 0;
for (const entry of fs.readdirSync(manifestSource, { withFileTypes: true })) {
  const source = path.join(manifestSource, entry.name, "manifest.json");
  if (!entry.isDirectory() || !fs.existsSync(source)) continue;
  const manifest = JSON.parse(fs.readFileSync(source, "utf8"));
  fs.copyFileSync(source, path.join(routerReferences, "manifests", `${manifest.gpt_id}.json`));
  count += 1;
}

console.log(JSON.stringify({ manifests: count, registry: "skills/ai-authoritech-gpt-router/references/gpts.json" }));
