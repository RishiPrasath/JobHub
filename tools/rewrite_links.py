"""Rewrite repo paths after the reorg, using tools/path-map.csv.

Usage: python tools/rewrite_links.py

Markdown links are recomputed in every .md file. Root-relative plain-text paths
are replaced only in living documents and compose files: frozen decks and raw
outputs are left as they were (see tools/path-map.csv and tag pre-reorg).
"""
import csv, os, posixpath, re, subprocess, urllib.parse
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)
PAIRS = list(csv.DictReader(open('tools/path-map.csv', encoding='utf-8')))
PAIRS = sorted(((r['old'], r['new']) for r in PAIRS), key=lambda x: -len(x[0]))
FROZEN = ('01_research/decks/00_', '01_research/decks/01_')

def to_new(p):
    for o, n in PAIRS:
        if p == o:
            return n
        if p.startswith(o + '/'):
            return n + p[len(o):]
    return p

def tracked():
    out = subprocess.run(['git', 'ls-files', '-z'], capture_output=True, text=True, encoding='utf-8').stdout
    return [x for x in out.split('\0') if x]

OLD_FILES = subprocess.run(['git', 'ls-tree', '-r', '--name-only', '-z', 'pre-reorg'], capture_output=True, text=True, encoding='utf-8').stdout.split('\0')
INVERSE = {to_new(o): o for o in OLD_FILES if o}
LINK = re.compile(r'(\]\()(<?)([^)\s>]+)(>?)((?:\s+"[^"]*")?\))')
BARE = re.compile(r'(?<![\w./%-])(' + '|'.join(re.escape(o) for o, _ in PAIRS if '/' in o or o.startswith(('_', '0'))) + r')(?=[/`\s:,;)"\']|$)', re.M)

def fix_links(text, new_path):
    old_path = INVERSE.get(new_path)
    if not old_path:
        return text, 0
    count = 0
    def sub(m):
        nonlocal count
        raw = m.group(3)
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', raw) or raw.startswith(('#', '/')):
            return m.group(0)
        path, frag = (raw.split('#', 1) + [None])[:2]
        if not path:
            return m.group(0)
        slash = path.endswith('/')
        target = posixpath.normpath(posixpath.join(posixpath.dirname(old_path), urllib.parse.unquote(path)))
        if target.startswith('..'):
            return m.group(0)
        rel = posixpath.relpath(to_new(target), posixpath.dirname(new_path) or '.')
        out = urllib.parse.quote(rel, safe="/-_.~()&+,=!'") + ('/' if slash and not rel.endswith('/') else '')
        if frag is not None:
            out += '#' + frag
        if out == raw:
            return m.group(0)
        count += 1
        return f'{m.group(1)}{m.group(2)}{out}{m.group(4)}{m.group(5)}'
    return LINK.sub(sub, text), count

def fix_bare(text):
    table = dict(PAIRS)
    return BARE.subn(lambda m: table[m.group(1)], text)

links = bare = 0
for f in tracked():
    is_md = f.endswith('.md')
    is_compose = f.endswith('docker-compose.yml')
    if not (is_md or is_compose) or not os.path.exists(f):
        continue
    with open(f, encoding='utf-8', newline='') as h:
        t = o = h.read()
    if is_md:
        t, n = fix_links(t, f)
        links += n
    if is_compose or not (f.startswith(FROZEN) or '/outputs/' in f):
        t, n = fix_bare(t)
        bare += n
    if t != o:
        with open(f, 'w', encoding='utf-8', newline='') as h:
            h.write(t)
print('links rewritten', links, 'plain paths rewritten', bare)
