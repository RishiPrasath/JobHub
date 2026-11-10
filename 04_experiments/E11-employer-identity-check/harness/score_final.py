"""Final scoring of run1 and run2 against the frozen gold, under protocol/interpretation.md. Writes runs/2026-11-10-run-001/analysis_summary.json.
Usage: python harness/score_final.py   (from the experiment folder). Does not touch raw outputs."""
import json
from collections import Counter, defaultdict
from pathlib import Path

R = Path(__file__).resolve().parents[1]
O = R / "runs/2026-11-10-run-001/outputs"
G = {x["id"]: x for x in json.load(open(R / "data/ground_truth.json", encoding="utf-8"))["items"]}
EXISTS = {"exists_and_consistent", "exists_limited_evidence", "web_evidence_only"}
BRAND = {"brand_legal_entity_unconfirmed"}


def load(run):
    return {i: json.load(open(O / run / (i + ".json"), encoding="utf-8")) for i in G}


def uen(r):
    return (r["registry"].get("entity") or {}).get("uen")


def cls(g, r):
    h, u, t = r["headline"], uen(r), g["truth_type"]
    named = h in EXISTS or h in BRAND
    if t == "entity":
        if h in EXISTS and u == g["truth_uen"]:
            return "correct"
        if h in EXISTS:
            return "wrong_accepted"
        return "unresolved_brand" if h in BRAND else "wrong_refusal"
    if t == "unknown":
        return "unknown_accept" if named else "unknown_refusal"
    if t == "not_disclosed":
        return "wrong_accepted" if named else "correct"          # naming any company for a hidden-employer posting is wrong
    return "wrong_accepted" if named else "correct"             # not_real: caught == not accepted


runs = {r: load(r) for r in ("run1", "run2")}
out = {}
for name, res in runs.items():
    c = {i: cls(G[i], res[i]) for i in G}
    known = [i for i in G if G[i]["truth_type"] != "unknown"]
    strat = defaultdict(Counter)
    for i in G:
        strat[G[i]["stratum"]][c[i]] += 1
    hid = [i for i in G if G[i]["stratum"] == "hidden"]
    out[name] = dict(
        classes=dict(Counter(c.values())),
        by_stratum={k: dict(v) for k, v in strat.items()},
        known_n=len(known), known_correct=sum(c[i] == "correct" for i in known),
        correct_rate_known=round(sum(c[i] == "correct" for i in known) / len(known), 3),
        wrong_accepted=sum(v == "wrong_accepted" for v in c.values()),
        wrong_accepted_ids=[i for i, v in c.items() if v == "wrong_accepted"],
        lookalikes_not_confirmed=sum(c[i] == "correct" for i in G if G[i]["stratum"] == "lookalike"),
        hidden_no_company=sum(c[i] == "correct" for i in hid),
        hidden_anonymous=sum(c[i] == "correct" for i in ("H01", "H02", "H03")),
        hidden_agency=sum(c[i] == "correct" for i in ("H04", "H05", "H06")),
        entity_items=sum(G[i]["truth_type"] == "entity" for i in G),
        entity_correct=sum(c[i] == "correct" and G[i]["truth_type"] == "entity" for i in G),
        accepted_entity_precision=None,
        seconds_sum=round(sum(r["seconds"] for r in res.values()), 1),
        seconds_mean=round(sum(r["seconds"] for r in res.values()) / len(res), 1),
        briefs_written=sum(1 for r in res.values() if r["brief"]),
        summary_unavailable=sum(any("summary_unavailable" in d for d in r["degraded"]) for r in res.values()),
        searches=sum(len(r["web"]["queries"]) for r in res.values()),
        pages_read=sum(len(r["web"]["pages"]) for r in res.values()),
        rows={i: dict(employer=G[i]["employer"], stratum=G[i]["stratum"], truth=G[i]["truth_type"], truth_uen=G[i].get("truth_uen"),
                      headline=res[i]["headline"], uen=uen(res[i]), cls=c[i], seconds=res[i]["seconds"]) for i in G})
    acc = [i for i in G if G[i]["truth_type"] == "entity" and res[i]["headline"] in EXISTS]
    out[name]["accepted_entity_precision"] = "%d/%d" % (sum(uen(res[i]) == G[i]["truth_uen"] for i in acc), len(acc))
a, b = runs["run1"], runs["run2"]
out["stability"] = dict(
    same_headline=sum(a[i]["headline"] == b[i]["headline"] for i in G),
    same_accepted_uen_or_refusal=sum(uen(a[i]) == uen(b[i]) and (a[i]["headline"] in EXISTS) == (b[i]["headline"] in EXISTS) for i in G),
    same_class=sum(cls(G[i], a[i]) == cls(G[i], b[i]) for i in G), n=len(G),
    differing_headlines={i: [a[i]["headline"], b[i]["headline"]] for i in G if a[i]["headline"] != b[i]["headline"]})
(R / "runs/2026-11-10-run-001/analysis_summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
for k in ("run1", "run2"):
    o = out[k]
    print(k, {x: o[x] for x in ("classes", "known_correct", "known_n", "correct_rate_known", "wrong_accepted", "wrong_accepted_ids", "lookalikes_not_confirmed", "hidden_no_company", "hidden_anonymous", "hidden_agency", "entity_correct", "entity_items", "accepted_entity_precision", "seconds_mean", "briefs_written", "summary_unavailable", "searches", "pages_read")})
    print("   ", o["by_stratum"])
print(out["stability"])
