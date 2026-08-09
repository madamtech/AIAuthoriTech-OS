#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERIC = {
    'a','an','and','or','the','to','for','of','with','from','into','on','in','by','as','at','is','are','be','this','that','it','its',
    'builder','designer','director','manager','reviewer','assistant','specialist','planner','architect','generator','creator','studio','expert',
    'system','production','professional','advanced','master','custom','gpt','ai','use','using','create','creates','creating','support','supports',
    'user','users','output','outputs','work','workflow','workflows','content','complete','ready','help','helps','provide','provides','include','includes'
}

DOMAIN_MARKERS = {
    'IMG': {'image','images','visual','photo','photos','photography','portrait','art','artwork','graphic','graphics','render','mockup','logo','typography','character','style','editorial','product','prompt','prompts'},
    'VIDEO': {'cinematic','film','video','videos','storyboard','storyboards','screenplay','scene','scenes','shot','shots','camera','motion','lighting','story','stories'},
    'BRAND': {'brand','branding','marketing','campaign','campaigns','social','caption','captions','copy','advertising','advertisement','audience','newsletter','launch','sales'},
    'LMS': {'lms','learning','course','courses','certification','certifications','learner','learners','training','scorm','enrollment','enrollments','transcript','exam','exams'},
    'NET': {'netexam','certification','course','exam','reporting','branch','lms'},
    'WDAY': {'workday','learning','assignment','campaign','security','lms'},
    'CRM': {'salesforce','crm','sales','learning','integration'},
    'AGNT': {'agent','agents','assistant','chatbot','gpt','tool','tools','memory','multi-agent','deployment'},
    'CONS': {'consulting','consultant','strategy','roadmap','readiness','assessment','proposal','implementation','roi','governance','client'},
    'FLOW': {'workflow','process','automation','approval','orchestration','metrics','documentation','standardization'},
    'KNOW': {'knowledge','knowledgebase','knowledge-base','research','source','sources','grounding','retrieval'},
    'GOV': {'government','govcon','public','procurement','proposal','compliance','contract','contracting','solicitation'},
    'BEAUTY': {'beauty','skincare','cosmetic','cosmetics','lotion','soap','bath','fragrance','hair','body','formula','formulation'},
    '3D': {'3d','print','printing','printer','filament','stl','3mf','openscad','slicer','bambu','flashforge','ender'},
    'LASER': {'laser','xtool','engrave','engraving','cut','cutting','material'},
}


def tokens(text):
    return [t for t in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)?", (text or '').lower()) if len(t) > 1 and t not in GENERIC]


def ngrams(ts, n=2):
    return {' '.join(ts[i:i+n]) for i in range(max(0, len(ts)-n+1))}


def frontmatter_description(path):
    if not path.is_file():
        return ''
    text = path.read_text(encoding='utf-8')
    match = re.match(r'^---\s*\n(.*?)\n---', text, flags=re.S)
    if not match:
        return ''
    for line in match.group(1).splitlines():
        if line.startswith('description:'):
            return line.split(':',1)[1].strip().strip('"')
    return ''


def load_assets():
    assets = []
    seen = set()
    for path in sorted((ROOT/'catalog').glob('*.json')):
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except Exception:
            continue
        for asset in data.get('assets', []) if isinstance(data, dict) else []:
            if asset.get('asset_type') == 'SKL' and asset.get('sku') not in seen:
                seen.add(asset['sku'])
                skill_path = ROOT / asset['path'] / 'SKILL.md'
                desc = frontmatter_description(skill_path)
                purpose = ''
                if skill_path.is_file():
                    text = skill_path.read_text(encoding='utf-8')
                    pm = re.search(r'## Purpose\s*\n([^\n]+)', text)
                    if pm:
                        purpose = pm.group(1).strip()
                asset = dict(asset)
                asset['_description'] = desc
                asset['_purpose'] = purpose
                assets.append(asset)
    return assets


def load_gpts():
    out = []
    for path in sorted((ROOT/'gpts'/'manifests').glob('*/manifest.json')):
        data = json.loads(path.read_text(encoding='utf-8'))
        if re.match(r'^AA-GPT-\d{6}$', data.get('gpt_id','')):
            data['_path'] = path.relative_to(ROOT).as_posix()
            out.append(data)
    return sorted(out, key=lambda x: x['gpt_id'])


def existing_verified():
    path = ROOT/'catalog'/'gpt-skill-mappings.json'
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    return {m['gpt_id']: m for m in data.get('mappings',[]) if m.get('verification_status') == 'verified'}


def infer_domains(text_tokens):
    tset = set(text_tokens)
    scores = {}
    for domain, markers in DOMAIN_MARKERS.items():
        hit = tset & markers
        if hit:
            scores[domain] = len(hit)
    return scores


def skill_domain(asset):
    lib = asset.get('library','')
    path = asset.get('path','').lower()
    if lib in DOMAIN_MARKERS:
        return lib
    if '3d' in path or 'three-d' in path or 'printing' in path:
        return '3D'
    if 'laser' in path:
        return 'LASER'
    if asset.get('business') == 'LMS':
        return 'LMS'
    return lib


def score_pair(gpt, asset):
    conf = gpt.get('configuration', {})
    gtext = ' '.join([
        gpt.get('name',''), gpt.get('purpose',''), conf.get('description') or '', conf.get('instructions') or '',
        ' '.join(conf.get('conversation_starters') or [])
    ])
    stext = ' '.join([asset.get('name',''), asset.get('asset_id',''), asset.get('_description',''), asset.get('_purpose','')])
    gt = tokens(gtext)
    st = tokens(stext)
    gs, ss = set(gt), set(st)
    if not gs or not ss:
        return 0.0, []
    overlap = gs & ss
    weighted = sum(1.8 if len(x) >= 8 else 1.0 for x in overlap)
    containment = len(overlap) / max(1, min(len(gs), len(ss)))
    jaccard = len(overlap) / max(1, len(gs | ss))
    bigram_overlap = ngrams(gt) & ngrams(st)
    phrase_bonus = min(3.0, len(bigram_overlap) * 0.45)
    domains = infer_domains(gt)
    domain = skill_domain(asset)
    domain_bonus = min(3.0, domains.get(domain, 0) * 0.7)
    score = (weighted * 0.20) + (containment * 5.0) + (jaccard * 2.0) + phrase_bonus + domain_bonus
    evidence = sorted(overlap, key=lambda x: (-len(x), x))[:12]
    return round(score,4), evidence


def classify(top):
    if not top:
        return 'no-candidate'
    if top[0]['score'] >= 7.0:
        return 'strong-candidate'
    if top[0]['score'] >= 4.5:
        return 'candidate'
    return 'needs-review'


def reconcile():
    assets = load_assets()
    gpts = load_gpts()
    verified = existing_verified()
    rows = []
    for gpt in gpts:
        if gpt['gpt_id'] in verified:
            rows.append({
                'gpt_id': gpt['gpt_id'], 'gpt_name': gpt['name'], 'status': 'verified-mapped',
                'verified_mapping': verified[gpt['gpt_id']], 'candidates': []
            })
            continue
        scored = []
        for asset in assets:
            score, evidence = score_pair(gpt, asset)
            if score > 0:
                scored.append({
                    'skill_sku': asset['sku'], 'skill_name': asset['name'], 'library': asset.get('library'),
                    'score': score, 'evidence_terms': evidence
                })
        scored.sort(key=lambda x: (-x['score'], x['skill_sku']))
        top = scored[:8]
        rows.append({
            'gpt_id': gpt['gpt_id'], 'gpt_name': gpt['name'], 'status': classify(top), 'candidates': top
        })
    counts = Counter(r['status'] for r in rows)
    return {
        'schema_version': '1.0.0',
        'generated_from': 'captured GPT Builder manifests + governed SKILL.md catalog',
        'policy': 'Candidate scores support reconciliation review only. They do not become verified mappings until direct captured configuration evidence is reviewed.',
        'gpt_count': len(gpts), 'skill_count': len(assets), 'status_counts': dict(sorted(counts.items())), 'gpts': rows
    }


def markdown(data):
    lines = [
        '# Full Custom GPT-to-SKILL Reconciliation', '',
        f"GPTs analyzed: **{data['gpt_count']}**", f"Skills analyzed: **{data['skill_count']}**", '',
        '## Status summary', ''
    ]
    for key, value in data['status_counts'].items():
        lines.append(f'- {key}: **{value}**')
    lines.extend(['', '## Reconciliation queue', '', '| GPT | Status | Top candidate skills |', '|---|---|---|'])
    for row in data['gpts']:
        if row['status'] == 'verified-mapped':
            mapping = row['verified_mapping']
            skills = ', '.join(mapping.get('required_skills',[]) + mapping.get('optional_skills',[]))
        else:
            skills = '; '.join(f"{c['skill_sku']} {c['skill_name']} ({c['score']:.2f})" for c in row['candidates'][:4]) or 'None'
        lines.append(f"| {row['gpt_id']} — {row['gpt_name']} | {row['status']} | {skills} |")
    lines.extend(['', '## Verification rule', '', 'Automated similarity is intentionally non-authoritative. Existing verified mappings remain verified; all other rows are a review queue. A candidate may be promoted only when the captured Builder purpose/instructions directly support the SKILL capability.', ''])
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    data = reconcile()
    if args.write:
        out_json = ROOT/'reports'/'gpt-skill-reconciliation-2026-08-08.json'
        out_md = ROOT/'reports'/'gpt-skill-reconciliation-2026-08-08.md'
        out_json.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
        out_md.write_text(markdown(data), encoding='utf-8')
        print(json.dumps({'gpts': data['gpt_count'], 'skills': data['skill_count'], 'status_counts': data['status_counts']}))
    else:
        print(json.dumps(data, indent=2))

if __name__ == '__main__':
    main()
