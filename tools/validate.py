"""Validate JobHub's decision records and Markdown links.

Usage:
    python tools/validate.py          check, then regenerate the board and matrix
    python tools/validate.py --check  check only; fail if generated files are stale

Exit code 1 means at least one error. Warnings do not fail the run.
"""
import os, posixpath, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
FEATURES = '03_features'
SCOPE_FILE = '06_scope/SCOPE.md'
MATRIX_FILE = 'generated/traceability.md'
BEGIN, END = '<!-- BOARD:BEGIN -->', '<!-- BOARD:END -->'
SCOPES = {'candidate', 'testing', 'in', 'later', 'out'}
RESULTS = {'pass', 'pass-small-sample', 'mixed', 'inconclusive', 'fail', 'none'}
NEED = {f'N{i}': i for i in range(5)}
FEAS = {f'T{i}': i for i in range(5)}
REQUIRED = ['id', 'title', 'type', 'scope', 'need_level', 'feasibility_level', 'result',
            'opportunity', 'needs', 'findings', 'riskiest_assumption', 'decision', 'updated']
errors, warnings = [], []


def tracked():
    out = subprocess.run(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
                         capture_output=True, text=True, encoding='utf-8').stdout
    return [f for f in out.split('\0') if f and os.path.exists(f)]


def read(path):
    with open(path, encoding='utf-8') as h:
        return h.read()


def check_links(files):
    known = set(files)
    dirs = {posixpath.dirname(f) for f in files}
    for d in list(dirs):
        while d:
            d = posixpath.dirname(d)
            dirs.add(d)
    link = re.compile(r'\]\(<?([^)\s>]+)>?(?:\s+"[^"]*")?\)')
    total = 0
    for f in files:
        if not f.endswith('.md') or f == 'REORG_PLAN.md':
            continue
        in_fence = False
        for no, line in enumerate(read(f).splitlines(), 1):
            if line.lstrip().startswith('```'):
                in_fence = not in_fence
            if in_fence:
                continue
            for raw in link.findall(line):
                if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', raw) or raw.startswith(('#', '/')):
                    continue
                path = urllib.parse.unquote(raw.split('#')[0])
                if not path:
                    continue
                total += 1
                target = posixpath.normpath(posixpath.join(posixpath.dirname(f), path))
                if target in known or target in dirs:
                    continue
                if os.path.exists(target) or '.build/' in target:
                    warnings.append(f'{f}:{no}: link target is not tracked: {raw}')
                else:
                    errors.append(f'{f}:{no}: broken link: {raw}')
    return total


def front_matter(path):
    text = read(path)
    m = re.match(r'---\r?\n(.*?)\r?\n---', text, re.S)
    if not m:
        errors.append(f'{path}: no front matter')
        return {}
    data = {}
    for line in m.group(1).splitlines():
        line = re.sub(r'\s+#.*$', '', line).strip()
        if not line or ':' not in line:
            continue
        key, value = line.split(':', 1)
        value = value.strip()
        if value.startswith('[') and value.endswith(']'):
            data[key] = [v.strip().strip('"') for v in value[1:-1].split(',') if v.strip()]
        else:
            data[key] = None if value in ('', 'null') else value.strip('"')
    return data


def register(path, pattern):
    """Return IDs from the first column of Markdown tables in a register."""
    if not os.path.exists(path):
        return []
    ids = []
    for line in read(path).splitlines():
        m = re.match(r'\|\s*(' + pattern + r')\s*\|', line)
        if m:
            ids.append(m.group(1))
    for i in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f'{path}: duplicate ID {i}')
    return ids


def load_features():
    if not os.path.isdir(FEATURES):
        return []
    feats = []
    for name in sorted(os.listdir(FEATURES)):
        if re.match(r'FEAT-\d{3}', name):
            path = f'{FEATURES}/{name}'
            data = front_matter(path)
            data['_path'], data['_name'] = path, name
            feats.append(data)
    return feats


def check_features(feats, findings, needs, opps, asms, decisions):
    seen = set()
    for f in feats:
        p = f['_path']
        for key in REQUIRED:
            if key not in f:
                errors.append(f'{p}: missing field {key}')
        fid = f.get('id') or ''
        if not f['_name'].startswith(fid + '-'):
            errors.append(f'{p}: id {fid} does not match file name')
        if fid in seen:
            errors.append(f'{p}: duplicate id {fid}')
        seen.add(fid)
        if f.get('scope') not in SCOPES:
            errors.append(f'{p}: bad scope {f.get("scope")}')
        if f.get('need_level') not in NEED:
            errors.append(f'{p}: bad need_level {f.get("need_level")}')
        if f.get('feasibility_level') not in FEAS:
            errors.append(f'{p}: bad feasibility_level {f.get("feasibility_level")}')
        if f.get('result') not in RESULTS:
            errors.append(f'{p}: bad result {f.get("result")}')
        for key, known in [('findings', findings), ('needs', needs), ('opportunity', opps)]:
            for ref in f.get(key) or []:
                if ref not in known:
                    errors.append(f'{p}: {key} refers to unknown {ref}')
        asm = f.get('riskiest_assumption')
        if asm and asm not in asms:
            errors.append(f'{p}: unknown assumption {asm}')
        dec = f.get('decision')
        if dec and dec not in decisions:
            errors.append(f'{p}: unknown decision {dec}')
        scope = f.get('scope')
        if scope in ('testing', 'in') and not (f.get('findings') and asm):
            errors.append(f'{p}: scope {scope} needs a finding and a riskiest assumption')
        if scope == 'in':
            if NEED.get(f.get('need_level'), -1) < 3 or FEAS.get(f.get('feasibility_level'), -1) < 2:
                errors.append(f'{p}: scope in needs at least N3 and T2')
            if not dec:
                errors.append(f'{p}: scope in needs a recorded decision')
        if scope == 'out' and not dec:
            errors.append(f'{p}: scope out needs a recorded decision')


def board(feats):
    rows = ['| Feature | Scope | Need | Feasibility | Result | Next |', '|---|---|---|---|---|---|']
    order = {'in': 0, 'testing': 1, 'candidate': 2, 'later': 3, 'out': 4}
    ranked = sorted(feats, key=lambda f: (order.get(f.get('scope'), 9), -NEED.get(f.get('need_level'), 0),
                                          -FEAS.get(f.get('feasibility_level'), 0), f.get('id', '')))
    for f in ranked:
        link = posixpath.relpath(f['_path'], posixpath.dirname(SCOPE_FILE))
        rows.append(f"| [{f.get('id')} {f.get('title')}]({link}) | {f.get('scope')} | {f.get('need_level')} | "
                    f"{f.get('feasibility_level')} | {f.get('result')} | {f.get('riskiest_assumption') or 'none'} |")
    return '\n'.join(rows)


def matrix(feats, findings):
    out = ['# Traceability matrix', '', 'Generated by `tools/validate.py`. Do not edit by hand.', '',
           '| Feature | Scope | Opportunities | Needs | Findings | Assumption | Decision |',
           '|---|---|---|---|---|---|---|']
    used = set()
    for f in feats:
        used.update(f.get('findings') or [])
        out.append(f"| {f.get('id')} {f.get('title')} | {f.get('scope')} | {', '.join(f.get('opportunity') or [])} | "
                   f"{', '.join(f.get('needs') or [])} | {', '.join(f.get('findings') or [])} | "
                   f"{f.get('riskiest_assumption') or ''} | {f.get('decision') or ''} |")
    orphans = sorted(set(findings) - used)
    out += ['', '## Findings no feature cites yet', '', ', '.join(orphans) if orphans else 'None.', '']
    return '\n'.join(out)


def generated(check_only, feats, findings):
    if not feats:
        return
    text = matrix(feats, findings)
    stale = not os.path.exists(MATRIX_FILE) or read(MATRIX_FILE) != text
    if os.path.exists(SCOPE_FILE):
        scope = read(SCOPE_FILE)
        if BEGIN not in scope or END not in scope:
            errors.append(f'{SCOPE_FILE}: board markers missing')
        else:
            new = re.sub(re.escape(BEGIN) + '.*?' + re.escape(END),
                         lambda _: f'{BEGIN}\n{board(feats)}\n{END}', scope, flags=re.S)
            if new != scope:
                stale = True
                if not check_only:
                    with open(SCOPE_FILE, 'w', encoding='utf-8', newline='\n') as h:
                        h.write(new)
    if check_only:
        if stale:
            errors.append('generated files are stale: run python tools/validate.py')
        return
    os.makedirs(posixpath.dirname(MATRIX_FILE), exist_ok=True)
    with open(MATRIX_FILE, 'w', encoding='utf-8', newline='\n') as h:
        h.write(text)


def main():
    check_only = '--check' in sys.argv
    files = tracked()
    links = check_links(files)
    findings = register('02_analysis/findings.md', r'FND-[A-Z0-9]+-\d+')
    opps = register('02_analysis/opportunities.md', r'OPP-\d{3}')
    asms = register(f'{FEATURES}/assumptions.md', r'ASM-\d{3}')
    needs = set(re.findall(r'\bS-\d{2}\b', read('02_analysis/needs.md'))) if os.path.exists('02_analysis/needs.md') else set()
    decision_dir = '06_scope/decisions'
    decisions = {n[:4] for n in os.listdir(decision_dir) if re.match(r'\d{4}-', n)} if os.path.isdir(decision_dir) else set()
    feats = load_features()
    check_features(feats, set(findings), needs, set(opps), set(asms), decisions)
    generated(check_only, feats, findings)
    for w in warnings[:15]:
        print('WARN ', w)
    if len(warnings) > 15:
        print(f'WARN  and {len(warnings) - 15} more')
    for e in errors:
        print('ERROR', e)
    print(f'{links} links, {len(feats)} features, {len(findings)} findings, {len(errors)} errors, {len(warnings)} warnings')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
