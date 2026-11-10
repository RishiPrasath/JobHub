"""POST HOC analyses (labelled as such in FINDINGS.md). Not part of the pre-registered scoring.
 A. lenient parse of the free-text outputs (requirement items that the model emitted as JSON strings)
 B. pay errors split into straddle cases (gold rule u) and the rest
 C. omissions split: credential gold x answered u (cautious) vs other omissions
 D. direction-tolerant reading: m accepted where gold is c
 E. error attribution for the structured method (extraction vs code)
"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import score as S
C = S.C
out = {}

# A. lenient parse
orig = C.parse_free_one
def lenient(d):
    if isinstance(d, dict) and isinstance(d.get("requirements"), list):
        fixed = []
        for r in d["requirements"]:
            if isinstance(r, str):
                m = re.search(r"\{.*\}", r, re.S)
                try:
                    r = json.loads(m.group(0)) if m else None
                except Exception:
                    r = None
            if isinstance(r, dict):
                fixed.append(r)
        d = {**d, "requirements": fixed}
    return orig(d)

def free_single(parser):
    C.parse_free_one = parser
    res, raws, use = S.collect("free", "single", 1)
    rows = [S.score_one(pid, prof, res.get((pid, prof)), raws.get((pid, prof))) for pid in S.PIDS for prof in S.PROFS if (pid, prof) in res]
    return rows

strict = free_single(orig)
len_rows = free_single(lenient)
C.parse_free_one = orig
nstr = 0
for prof in S.PROFS:
    for pid in S.PIDS:
        try:
            r, rec = C.free_results(prof, [pid], 1)
        except Exception:
            continue
        d = C.clean(rec["content"])
        if isinstance(d, dict) and any(isinstance(x, str) for x in (d.get("requirements") or [])):
            nstr += 1
out["A_free_outputs_with_string_requirement_items"] = nstr
out["A_strict"] = S.rates(S.aggregate(strict))
out["A_lenient"] = S.rates(S.aggregate(len_rows))

# B pay split
def pay_split(rows):
    st = oth = 0
    det = []
    for r in rows:
        c = r["cells"]["pay"]
        if c["hard_error"]:
            straddle = r["pid"] in ("S02", "S08", "S09", "S10", "S11") and c["gold"] == "u"
            det.append((r["prof"], r["pid"], c["gold"], c["sys"], "straddle" if straddle else "other"))
            st += straddle
            oth += not straddle
    return dict(straddle=st, other=oth, detail=det)
out["B_free_pay_errors"] = pay_split(len_rows)
sr = [json.loads(l) for l in open(S.OUT / "cells.jsonl")]
srows = [x for x in sr if x["method"] == "struct" and x["mode"] == "single"]
out["B_struct_pay_errors"] = pay_split(srows)

# C omissions split
def om_split(rows):
    cred_x_u = other = 0
    cmp_cred = cmp_other = 0
    for r in rows:
        a = b = False
        for k, c in r["cells"].items():
            if c["omitted"]:
                b = True
        for d in r["reqs"]:
            if d["omitted"]:
                if d["kind"] == "credential" and d["gold"] == "x" and d.get("sys") in ("u", None):
                    a = True
                else:
                    b = True
        cmp_cred += a and not b
        cmp_other += b
    return dict(comparisons=len(rows), only_credential_x_answered_u_or_missing=cmp_cred, other_omission=cmp_other,
                other_omission_pct=S.pct(cmp_other, len(rows)))
out["C_free"] = om_split(len_rows)
out["C_struct"] = om_split(srows)

# D direction tolerant
def tol(rows):
    n = unsup = 0
    for r in rows:
        for d in r["reqs"]:
            if d["matched"]:
                n += 1
                s = d.get("sys")
                bad = (s in ("m", "x") and s not in d["accept"] and not (s == "m" and d["gold"] == "c")) or (s == "c" and d["gold"] == "u" and "c" not in d["accept"])
                unsup += bad
        n += len(r["extras"])
        unsup += sum(e["unsupported"] for e in r["extras"])
    return dict(items=n, unsupported=unsup, pct=S.pct(unsup, n))
out["D_free_lenient_parse_m_accepted_for_c"] = tol(len_rows)
out["D_struct_m_accepted_for_c"] = tol(srows)

# E struct attribution: list every hard error / unsupported with the extraction facts
errs = []
for r in srows:
    for k, c in r["cells"].items():
        if c["hard_error"]:
            errs.append(("hard", r["prof"], r["pid"], k, c["gold"], c["sys"]))
    for d in r["reqs"]:
        if d["unsupported"]:
            errs.append(("req", r["prof"], r["pid"], d["id"], d["gold"], d["sys"]))
    if r["rtw"]["false_flag"]:
        errs.append(("rtw_false_flag", r["prof"], r["pid"], "rtw", r["rtw"]["gold"], r["rtw"]["sys"]))
out["E_struct_errors"] = errs
# extraction-level audits: how many extractions have a non-verbatim excerpt dropped
dropped = 0
tot = 0
ex_out = {}
for pid in S.PIDS:
    try:
        ex, rec = C.extraction([pid], 1)
    except Exception:
        continue
    e = ex[pid]
    reqs, d = C.ex_requirements(e, C.PBY[pid]["text"])
    n_all = len((e or {}).get("requirements") or [])
    ex_out[pid] = dict(reqs_extracted=n_all, reqs_kept=len(reqs), dropped=d, gold_reqs=len(C.GOLD[pid]["requirements"]))
    dropped += d
    tot += n_all
out["E_extraction_requirement_excerpt_audit"] = ex_out
out["E_dropped_total"] = [dropped, tot]
(S.OUT / "posthoc.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
