"""E1b: match employer names against locally-held ACRA bulk CSVs. Args: csv_dir"""
import csv, json, re, sys
from difflib import SequenceMatcher
from pathlib import Path
RUN = Path(__file__).resolve().parents[1]
STOP = {"pte", "ltd", "limited", "private", "co", "operative", "singapore", "sg", "the", "of", "and", "&"}
def toks(s): return [t for t in re.sub(r"[^a-z0-9 ]", " ", s.lower()).split() if t not in STOP]
postings = json.loads((RUN / "data/postings.json").read_text(encoding="utf-8"))
Q = {p["id"]: toks(p["employer"]) for p in postings}
cands = {pid: [] for pid in Q}
rows = 0
csv.field_size_limit(10**7)
for f in sorted(Path(sys.argv[1]).glob("*.csv")):
    with open(f, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            rows += 1
            names = [r.get("entity_name", "")] + [r.get(f"former_entity_name{i}", "") for i in (1, 2, 3)]
            nt = [(n, toks(n)) for n in names if n]
            for pid, q in Q.items():
                for n, t in nt:
                    if q and set(q) <= set(t):
                        s = SequenceMatcher(None, " ".join(q), " ".join(t)).ratio()
                        cands[pid].append((round(s, 3), r["uen"], r["entity_name"], n if n != r["entity_name"] else "", r["entity_type_description"], r["entity_status_description"], r["registration_incorporation_date"], r["primary_ssic_description"]))
                        break
out = []
for p in postings:
    c = sorted(set(cands[p["id"]]), key=lambda x: (-x[0], x[5] != "Live"))
    live = [x for x in c if x[5].lower().startswith("live")]
    top = c[:5]
    if not c: state = "unresolved"
    elif c[0][0] >= 0.95 and (len(c) == 1 or c[1][0] < 0.9): state = "exact_match"
    elif c[0][0] >= 0.8 and (len(c) == 1 or c[0][0] - c[1][0] >= 0.1): state = "likely_match"
    else: state = "ambiguous"
    out.append({"id": p["id"], "employer": p["employer"], "state": state, "n_candidates": len(c), "n_live": len(live),
                "top": [dict(zip(("score", "uen", "name", "matched_former_name", "type", "status", "incorporated", "ssic"), x)) for x in top]})
    print(p["id"], state, len(c), "|", top[0][2] if top else "-", "|", top[0][5] if top else "")
(RUN / "outputs/e1b_acra_local_match.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print("rows scanned", rows)
