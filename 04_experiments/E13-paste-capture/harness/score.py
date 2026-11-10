"""Score a run against the frozen gold labels. Reads outputs, writes results.json and results.md next to them.

Usage: python harness/score.py [run_dir]
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

EXP = Path(__file__).resolve().parent.parent
run_dir = EXP / (sys.argv[1] if len(sys.argv) > 1 else "runs/2026-11-10-run-001")
out = run_dir / "outputs"
gold = {g["id"]: g for g in json.loads((EXP / "data/gold_labels.json").read_text(encoding="utf-8"))["items"]}
FIELDS = ["title", "employer", "pay", "duties", "closing"]
c30 = [i for i, g in gold.items() if g["set"] == "complete30"]
p10 = [i for i, g in gold.items() if g["set"] == "partial10"]


def pct(a, b):
    return round(100 * a / b, 1) if b else None


def load(name):
    p = out / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def score_system(label, an):
    """an: id -> analysis dict with fields{}, partial_flag."""
    r = {"system": label}
    c30 = [i for i in globals()["c30"] if i in an]   # a system may have been run on a subset
    p10 = [i for i in globals()["p10"] if i in an]
    r["ids_scored"] = {"complete": len(c30), "partial": len(p10)}
    gold_complete = [i for i in c30 if all(gold[i]["fields"][f] != "missing" for f in FIELDS)]
    pred_complete = [i for i in c30 if all(an[i]["fields"][f] != "missing" for f in FIELDS)]
    r["gold_complete"] = {"n": len(gold_complete), "of": len(c30), "pct": pct(len(gold_complete), len(c30))}
    r["predicted_complete"] = {"n": len(pred_complete), "of": len(c30), "pct": pct(len(pred_complete), len(c30))}
    r["complete_agreement"] = {"n": sum((i in gold_complete) == (i in pred_complete) for i in c30), "of": len(c30)}
    # per-field 3-class accuracy and errors
    pf, errs = {}, []
    for f in FIELDS:
        ok = sum(an[i]["fields"][f] == gold[i]["fields"][f] for i in c30)
        pf[f] = {"correct": ok, "of": len(c30), "pct": pct(ok, len(c30))}
        for i in c30:
            if an[i]["fields"][f] != gold[i]["fields"][f]:
                errs.append({"id": i, "board": gold[i]["board"], "field": f, "gold": gold[i]["fields"][f], "got": an[i]["fields"][f],
                             "value": (an[i].get("values") or {}).get(f)})
    r["field_accuracy"], r["field_errors"] = pf, errs
    # partial detection
    flagged = [i for i in p10 if an[i]["partial_flag"]]
    r["partial_detection"] = {"flagged": len(flagged), "of": len(p10), "pct": pct(len(flagged), len(p10)),
                              "missed": [i for i in p10 if i not in flagged],
                              "by_type": {t: {"flagged": sum(an[i]["partial_flag"] for i in p10 if gold[i]["partial_type"] == t),
                                              "of": sum(1 for i in p10 if gold[i]["partial_type"] == t)}
                                          for t in ("cut_off", "no_body", "cards_nav")}}
    ff = [i for i in c30 if an[i]["partial_flag"]]
    r["false_flags"] = {"n": len(ff), "of": len(c30), "ids": ff, "reasons": {i: an[i]["partial_reasons"] for i in ff}}
    return r


def breakdown():
    """Gold missing fields by board and by job type (what the pastes lack, not what the system says)."""
    by_board, by_type = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: defaultdict(int))
    n_board, n_type, comp_board, comp_type = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
    for i in c30:
        g = gold[i]
        n_board[g["board"]] += 1
        n_type[g["job_type"]] += 1
        full = True
        for f in FIELDS:
            if g["fields"][f] == "missing":
                by_board[g["board"]][f] += 1
                by_type[g["job_type"]][f] += 1
                full = False
        if full:
            comp_board[g["board"]] += 1
            comp_type[g["job_type"]] += 1
    tot = defaultdict(int)
    for i in c30:
        for f in FIELDS:
            tot[f] += gold[i]["fields"][f] == "missing"
    return {"by_board": {b: {"n": n_board[b], "complete": comp_board[b], "pct_complete": pct(comp_board[b], n_board[b]), "missing": dict(by_board[b])} for b in n_board},
            "by_job_type": {t: {"n": n_type[t], "complete": comp_type[t], "pct_complete": pct(comp_type[t], n_type[t]), "missing": dict(by_type[t])} for t in n_type},
            "gold_missing_by_field": dict(tot)}


def board_scores(an):
    c30 = [i for i in globals()["c30"] if i in an]
    p10 = [i for i in globals()["p10"] if i in an]
    """System accuracy by board: per-field correct, complete-agreement, partial flags (false flags / detections)."""
    res = {}
    for b in sorted({gold[i]["board"] for i in gold}):
        ids30 = [i for i in c30 if gold[i]["board"] == b]
        ids10 = [i for i in p10 if gold[i]["board"] == b]
        res[b] = {"n30": len(ids30), "n10": len(ids10),
                  "field_correct": {f: f"{sum(an[i]['fields'][f] == gold[i]['fields'][f] for i in ids30)}/{len(ids30)}" for f in FIELDS},
                  "false_flags": sum(an[i]["partial_flag"] for i in ids30), "partials_flagged": f"{sum(an[i]['partial_flag'] for i in ids10)}/{len(ids10)}"}
    return res


results = {"run": str(run_dir.name), "breakdown_gold": breakdown()}
det = load("analysis.json")
results["version"] = det["version"]
results["deterministic"] = score_system("deterministic snapshot step", det["items"])
results["deterministic"]["by_board"] = board_scores(det["items"])

llm = load("llm_analysis.json")
if llm:
    results["llm_model"] = llm.get("model")
    results["llm"] = score_system("LLM check (" + str(llm.get("model")) + ")", llm["items"])
    results["llm"]["by_board"] = board_scores(llm["items"])
    union = {}
    for i in gold:
        if i not in llm["items"]:
            continue
        a, b = det["items"][i], llm["items"][i]
        union[i] = {"fields": a["fields"], "partial_flag": a["partial_flag"] or b["partial_flag"], "partial_reasons": a["partial_reasons"] + b["partial_reasons"]}
    results["union_partial_flag"] = score_system("union of partial flags (deterministic OR LLM)", union)
    results["union_partial_flag"].pop("field_accuracy"); results["union_partial_flag"].pop("field_errors")

# stale
rule, e2e = load("stale_rule_results.json"), load("stale_e2e_results.json")
rule_ok, e2e_ok = sum(r["ok"] for r in rule), sum(r["ok"] for r in e2e)
repaste_ok = all(r["message_has_repaste_prompt"] for r in rule)
results["stale"] = {"rule_table": {"ok": rule_ok, "of": len(rule), "failures": [r for r in rule if not r["ok"]]},
                    "end_to_end": {"ok": e2e_ok, "of": len(e2e), "failures": [r for r in e2e if not r["ok"]],
                                   "failing_snapshots": sorted({r["id"] for r in e2e if not r["ok"]})},
                    "combined": {"ok": rule_ok + e2e_ok, "of": len(rule) + len(e2e)},
                    "notice_includes_repaste_prompt": repaste_ok,
                    "closing_date_extraction": {"correct": sum((det["items"][i]["closing_date_iso"] or None) == gold[i]["closing_date_iso"] for i in c30), "of": len(c30)}}
integ = load("integrity.json")
results["integrity"] = {"restore_equals_original": sum(x["restore_equals_original"] for x in integ), "stored_equals_original": sum(x["stored_equals_original"] for x in integ),
                        "of": len(integ), "with_crlf": sum(x["has_crlf"] for x in integ), "with_nbsp": sum(x["has_nbsp"] for x in integ),
                        "with_zero_width": sum(x["has_zero_width"] for x in integ)}

# verdicts (primary system = deterministic)
d = results["deterministic"]
gc, pd_, ffn = d["gold_complete"]["pct"], d["partial_detection"]["pct"], d["false_flags"]["n"]
st = results["stale"]
integ_ok = results["integrity"]["restore_equals_original"] == results["integrity"]["of"] and results["integrity"]["stored_equals_original"] == results["integrity"]["of"]
v = {}
v["T1 >=80% of 30 pastes contain all minimum fields"] = ("pass" if gc >= 80 else "fail" if gc < 50 else "inconclusive", f"{d['gold_complete']['n']}/30 = {gc}% (gold labels)")
v["T2 >=90% of 10 partial pastes flagged"] = ("pass" if pd_ >= 90 else "fail" if pd_ < 70 else "inconclusive", f"{d['partial_detection']['flagged']}/10 = {pd_}%")
v["T3 <=2 false flags on 30 complete pastes"] = ("pass" if ffn <= 2 else "fail", f"{ffn}/30")
v["T4 stale rule correct on 100% of test snapshots"] = ("pass" if st["combined"]["ok"] == st["combined"]["of"] else "fail", f"rule table {rule_ok}/{len(rule)}; end to end {e2e_ok}/{len(e2e)}; combined {st['combined']['ok']}/{st['combined']['of']}")
v["T5 100% of snapshots restore to original"] = ("pass" if integ_ok else "fail", f"{results['integrity']['restore_equals_original']}/{results['integrity']['of']}")
fail_rule = gc < 50 or pd_ < 70
pass_all = gc >= 80 and pd_ >= 90 and ffn <= 2 and st["combined"]["ok"] == st["combined"]["of"] and integ_ok
results["verdicts"] = v
results["overall_part_a"] = "fail" if fail_rule else ("pass" if pass_all else "inconclusive")
(out / "results.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")

# markdown summary
L = [f"# Scored results ({run_dir.name})", "", f"Snapshot step: {results['version']}", "", "## Verdicts", "", "| Threshold | Observed | Verdict |", "|---|---|---|"]
for k, (vd, obs) in v.items():
    L.append(f"| {k} | {obs} | {vd} |")
L += ["", f"Part A overall: {results['overall_part_a']}", "", "## Completeness of the 30 pastes (gold labels) by board", "", "| Board | n | all fields | % | missing fields |", "|---|---|---|---|---|"]
for b, x in results["breakdown_gold"]["by_board"].items():
    L.append(f"| {b} | {x['n']} | {x['complete']} | {x['pct_complete']} | {x['missing']} |")
L += ["", "By job type:", "", "| Job type | n | all fields | % | missing fields |", "|---|---|---|---|---|"]
for b, x in results["breakdown_gold"]["by_job_type"].items():
    L.append(f"| {b} | {x['n']} | {x['complete']} | {x['pct_complete']} | {x['missing']} |")
L += ["", f"Gold-missing by field (of 30): {results['breakdown_gold']['gold_missing_by_field']}", ""]
for key in ("deterministic", "llm"):
    if key not in results:
        continue
    s = results[key]
    L += [f"## System: {s['system']}", "",
          f"- pastes scored: {s['ids_scored']['complete']} complete-set, {s['ids_scored']['partial']} partial-set",
          f"- predicted complete: {s['predicted_complete']['n']}/{s['predicted_complete']['of']}; gold complete {s['gold_complete']['n']}/{s['gold_complete']['of']}; agreement on complete/incomplete {s['complete_agreement']['n']}/{s['complete_agreement']['of']}",
          f"- partial pastes flagged {s['partial_detection']['flagged']}/{s['partial_detection']['of']} (missed: {s['partial_detection']['missed']}); by type {s['partial_detection']['by_type']}",
          f"- false flags on complete pastes {s['false_flags']['n']}/{s['false_flags']['of']}: {s['false_flags']['reasons']}", "",
          "Field accuracy (3-class state) on the 30:", "", "| Field | correct | % |", "|---|---|---|"]
    for f, x in s["field_accuracy"].items():
        L.append(f"| {f} | {x['correct']}/{x['of']} | {x['pct']} |")
    L += ["", "Field errors:", ""]
    for e in s["field_errors"]:
        L.append(f"- {e['id']} ({e['board']}) {e['field']}: gold {e['gold']}, got {e['got']}, value {e['value']!r}")
    L += ["", "By board:", "", "| Board | n30 | field correct | false flags | partials flagged |", "|---|---|---|---|---|"]
    for b, x in s["by_board"].items():
        L.append(f"| {b} | {x['n30']} | {x['field_correct']} | {x['false_flags']} | {x['partials_flagged']} |")
    L.append("")
if "union_partial_flag" in results:
    u = results["union_partial_flag"]
    L += ["## Variant: union of partial flags", "", f"- partial flagged {u['partial_detection']['flagged']}/{u['partial_detection']['of']} (missed {u['partial_detection']['missed']}); false flags {u['false_flags']['n']}/{u['false_flags']['of']} {u['false_flags']['ids']}", ""]
L += ["## Stale rule", "", f"- rule table: {rule_ok}/{len(rule)}; failures: {[r['id'] for r in st['rule_table']['failures']]}",
      f"- end to end: {e2e_ok}/{len(e2e)}; failing snapshots: {st['end_to_end']['failing_snapshots']}",
      f"- closing date extraction correct on {st['closing_date_extraction']['correct']}/30",
      f"- notice includes re-paste prompt: {repaste_ok}", "", "## Integrity", "", f"{results['integrity']}"]
(out / "results.md").write_text("\n".join(L), encoding="utf-8")
print("\n".join(L))
