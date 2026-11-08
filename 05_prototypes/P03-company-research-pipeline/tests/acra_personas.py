"""Resolve every employer from the persona job-search run and print states per persona.
Run in the container:  python tests/acra_personas.py /runs/2026-11-01-persona-job-search/research/employers.json"""
import collections, json, sys
from pipeline import acra
E = json.load(open(sys.argv[1], encoding="utf-8"))
by = collections.defaultdict(collections.Counter)
for e in E:
    r = acra.resolve("/data/acra.sqlite", e["employer"])
    by[e["persona"]][r["state"]] += 1
    if r["state"] not in ("exact", "exact_by_uen"):
        print(r["state"], "|", e["employer"], "|", r["why"][:100])
for p, c in sorted(by.items()):
    print(f"{p:24}", dict(c))
