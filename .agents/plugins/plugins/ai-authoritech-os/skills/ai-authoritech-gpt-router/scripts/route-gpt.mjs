import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const skillRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const referenceRoot = path.join(skillRoot, "references");
const registry = JSON.parse(fs.readFileSync(path.join(referenceRoot, "gpts.json"), "utf8"));
const entries = [...(registry.authoritative_gpts || []), ...(registry.discovered_gpts || [])];

const args = process.argv.slice(2);
const queryIndex = args.indexOf("--query");
const query = queryIndex >= 0 ? args[queryIndex + 1]?.trim() : null;

function manifestPath(entry) {
  return path.join(referenceRoot, "manifests", `${entry.gpt_id}.json`);
}

function result(entry, match, confidence) {
  return { status: "selected", match, confidence, gpt_id: entry.gpt_id, name: entry.name, live_gpt_url: entry.live_gpt_url, manifest_path: manifestPath(entry) };
}

if (args.includes("--list")) {
  console.log(JSON.stringify({ total: entries.length, gpts: entries.map(entry => ({ gpt_id: entry.gpt_id, name: entry.name })) }, null, 2));
  process.exit(0);
}

if (!query) {
  console.error("Usage: node route-gpt.mjs --query <name, ID, or task> | --list");
  process.exit(2);
}

const normalized = query.toLowerCase();
const byId = entries.find(entry => entry.gpt_id.toLowerCase() === normalized);
if (byId) {
  console.log(JSON.stringify(result(byId, "exact-id", 1), null, 2));
  process.exit(0);
}

const exactNames = entries.filter(entry => entry.name.toLowerCase() === normalized);
if (exactNames.length === 1) {
  console.log(JSON.stringify(result(exactNames[0], "exact-name", 0.99), null, 2));
  process.exit(0);
}
if (exactNames.length > 1) {
  console.log(JSON.stringify({ status: "ambiguous", query, candidates: exactNames.map(entry => ({ gpt_id: entry.gpt_id, name: entry.name, manifest_path: manifestPath(entry) })) }, null, 2));
  process.exit(3);
}

const tokens = [...new Set(normalized.match(/[a-z0-9]+/g) || [])].filter(token => token.length > 2);
const scored = entries.map(entry => {
  const manifest = JSON.parse(fs.readFileSync(manifestPath(entry), "utf8"));
  const haystack = `${entry.name} ${manifest.purpose || ""} ${manifest.configuration?.description || ""}`.toLowerCase();
  const matched = tokens.filter(token => haystack.includes(token));
  const nameBonus = normalized.includes(entry.name.toLowerCase()) || entry.name.toLowerCase().includes(normalized) ? 0.35 : 0;
  const score = Math.min(0.95, nameBonus + (tokens.length ? matched.length / tokens.length * 0.65 : 0));
  return { entry, score, matched };
}).filter(item => item.score > 0).sort((a, b) => b.score - a.score || a.entry.gpt_id.localeCompare(b.entry.gpt_id));

if (!scored.length) {
  console.log(JSON.stringify({ status: "not-found", query, confidence: 0 }, null, 2));
  process.exit(4);
}

const top = scored[0];
const tied = scored.filter(item => Math.abs(item.score - top.score) < 0.05);
if (tied.length > 1) {
  console.log(JSON.stringify({ status: "ambiguous", query, confidence: top.score, candidates: tied.slice(0, 5).map(item => ({ gpt_id: item.entry.gpt_id, name: item.entry.name, score: item.score, matched_terms: item.matched, manifest_path: manifestPath(item.entry) })) }, null, 2));
  process.exit(3);
}

console.log(JSON.stringify({ ...result(top.entry, "purpose", top.score), matched_terms: top.matched }, null, 2));
