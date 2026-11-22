"""E22 scoring: combine Part A (ACRA match) and Part C (domain chain) against truth."""
import json, re
from pathlib import Path
R = Path(__file__).resolve().parents[1] / "runs/2026-11-21-run-001/outputs"
A = json.loads((R / "acra/match_results.json").read_text(encoding="utf-8"))
C = {r["id"]: r for r in json.loads((R / "domain_chain/chain_results.json").read_text(encoding="utf-8"))}
def core(n): return re.sub(r"\b(PTE|LTD|PRIVATE|LIMITED)\b", " ", re.sub(r"[^A-Z0-9 ]", " ", n.upper())).split()
rows = []
for b in A["brands"]:
    c = C[b["id"]]
    chain_uens = sorted({h["uen"] for a in c["acra_links"] for h in a["acra"]})
    tu = b["truth"]["uen"] if b["truth"] else None
    rows.append({"id": b["id"], "brand": b["brand"], "truth_uen": tu, "truth_name": b["truth"] and b["truth"]["entity_name"],
                 "token_hits": b["token_hits"], "live": b["token_hits_live"], "live_companies": b["token_hits_live_companies"],
                 "naive": b["naive_top1"] and b["naive_top1"]["entity_name"], "naive_ok": b["naive_correct"],
                 "naive_co_ok": b["naive_company_correct"], "truth_in_hits": b["truth_in_token_hits"],
                 "chain_uens": chain_uens, "chain_hit": bool(chain_uens),
                 "chain_agrees_truth": any(u in [tu] + b["alt_uens"] for u in chain_uens) if (tu and chain_uens) else None,
                 "chain_sources": [a["source"] for a in c["acra_links"] if a["acra"]],
                 "cert_type": c["cert"].get("type"), "rdap_registered": c["rdap"].get("registered"),
                 "wayback_first": c["wayback"].get("first_capture")})
known = [r for r in rows if r["truth_uen"]]
lk = A["lookalikes"]
# lookalike danger under a suffix-insensitive matcher: does any live entity share the core words?
summary = {
 "brands": len(rows), "truth_known_in_acra": len(known),
 "naive_top1_correct": sum(1 for r in known if r["naive_ok"]),
 "naive_company_top1_correct_posthoc": sum(1 for r in known if r["naive_co_ok"]),
 "truth_in_name_search_results": sum(1 for r in known if r["truth_in_hits"]),
 "median_live_entities_per_brand_token": sorted(r["live"] for r in rows)[len(rows)//2],
 "max_live_entities": max(r["live"] for r in rows),
 "brands_with_over_10_live_entities": sum(1 for r in rows if r["live"] > 10),
 "chain_reaches_acra": sum(1 for r in rows if r["chain_hit"]),
 "chain_agrees_with_site_truth": sum(1 for r in known if r["chain_agrees_truth"]),
 "chain_and_truth_both_present": sum(1 for r in known if r["chain_agrees_truth"] is not None),
 "lookalikes_exact_accepted": sum(1 for l in lk if l["accepted_by_exact_match"]),
 "lookalikes": len(lk),
}
(R / "summary.json").write_text(json.dumps({"summary": summary, "rows": rows}, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(summary, indent=1))
for r in rows: print(r["id"], r["brand"], "| truth", r["truth_name"], "| naive", r["naive"], r["naive_ok"], "| chain", r["chain_uens"], r["chain_sources"], r["chain_agrees_truth"])
