"""Aggregate scoring/per-run-metrics.json and question ratings into scoring/summary.json (Part A threshold figures).
Run after harness/score.py. Deterministic."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

SC = c.RUN_DIR / "scoring"
per = json.loads((SC / "per-run-metrics.json").read_text(encoding="utf-8"))
qs = json.loads((SC / "questions.json").read_text(encoding="utf-8"))
stab = json.loads((SC / "summary-stability.json").read_text(encoding="utf-8"))
GROUPS = {"gpt120_r1": ("gpt120", 1), "gpt120_r2": ("gpt120", 2), "qwen_r1": ("qwen", 1), "oss20_r1": ("oss20", 1)}


def pct(a, b):
    return None if not b else round(100 * a / b, 1)


def agg(rows):
    ok = [r for r in rows if r.get("valid") is not None and "n_claims" in r]
    out = {"n_outputs": len(rows), "parse_failed": sum(1 for r in rows if r["parse"] == "failed"),
           "lenient_parse": sum(1 for r in rows if r["parse"] == "lenient"),
           "valid_structure": sum(1 for r in rows if r.get("valid"))}
    sb = sum(r.get("sb_claims", 0) for r in ok)
    out["source_bound_claims"] = sb
    out["grounded_pct"] = pct(sum(r.get("grounded", 0) for r in ok), sb)
    out["fabricated"] = sum(r.get("fabricated", 0) for r in ok)
    out["fabricated_pct"] = pct(out["fabricated"], sb)
    out["unsupported_locator"] = sum(r.get("unsupported_locator", 0) for r in ok)
    out["ungrounded_unadjudicated"] = sum(r.get("ungrounded_unadjudicated", 0) for r in ok)
    gaps = [(g["final"], g["critical"]) for r in ok for g in r["gaps"].values()]
    out["gold_gaps"] = len(gaps)
    out["unknown_recall_pct"] = pct(sum(1 for f, _ in gaps if f), len(gaps))
    out["unknown_recall_auto_kw_only_pct"] = pct(sum(1 for r in ok for g_ in r["gaps"].values() if g_["auto"]), len(gaps))
    out["gap_outputs_not_reviewed"] = sum(1 for r in ok if not all(g_["reviewed"] for g_ in r["gaps"].values()))
    out["absent_sections_total"] = sum(r.get("absent_sections_total", 0) for r in ok)
    out["absent_sections_flagged"] = sum(r.get("absent_sections_flagged", 0) for r in ok)
    out["absent_section_recall_pct"] = pct(out["absent_sections_flagged"], out["absent_sections_total"])
    cg = [f for f, k in gaps if k]
    out["critical_gaps"] = len(cg)
    out["critical_recall_pct"] = pct(sum(cg), len(cg))
    # parse failures count as zero recall (gold gaps still exist)
    allgaps = sum(len(c.load_gold()[r["pid"]]["gaps"]) for r in rows)
    out["unknown_recall_pct_parse_fail_as_miss"] = pct(sum(1 for f, _ in gaps if f), allgaps)
    n = len(rows)
    out["false_conflicts"] = sum(r.get("false_conflicts", 0) for r in ok)
    out["false_conflicts_per_10_postings"] = round(10 * out["false_conflicts"] / n, 2) if n else None
    out["real_unlisted_conflicts"] = sum(r.get("real_unlisted_conflicts", 0) for r in ok)
    out["conflicts_unadjudicated"] = sum(r.get("conflict_unadjudicated", 0) for r in ok)
    planted = [(r["pid"], v["preserved"]) for r in rows for v in r.get("gold_contradictions", {}).values() if v["planted"]]
    out["planted_total"] = len([r for r in rows if r["pid"] in ("E12-P06", "E12-P07", "E12-P08", "E12-P09")])
    out["planted_preserved"] = sum(1 for _, ok_ in planted if ok_)
    out["planted_preserved_posthoc_lines"] = sum(1 for r in rows for v in r.get("gold_contradictions", {}).values() if v["planted"] and v.get("preserved_posthoc_lines"))
    out["planted_preserved_posthoc_union"] = sum(1 for r in rows for v in r.get("gold_contradictions", {}).values() if v["planted"] and v.get("preserved_posthoc_union"))
    out["platform_cited"] = sum(r.get("platform_cited", 0) for r in ok)
    out["platform_gold"] = sum(r.get("platform_gold", 0) for r in ok)
    out["platform_mislabelled"] = sum(r.get("platform_mislabelled", 0) for r in ok)
    out["platform_mislabelled_pct"] = pct(out["platform_mislabelled"], out["platform_cited"])
    out["employer_lines_labelled_platform"] = sum(r.get("employer_lines_labelled_platform", 0) for r in ok)
    withgap = [r for r in rows if c.load_gold()[r["pid"]]["gaps"]]
    out["postings_with_gap"] = len(withgap)
    out["postings_with_critical_question"] = sum(1 for r in withgap if r.get("question_on_critical_gap"))
    out["critical_question_pct"] = pct(out["postings_with_critical_question"], len(withgap))
    sa = [r["section_acc"] for r in ok if "section_acc" in r]
    out["section_accuracy_pct"] = pct(sum(a for a, t in sa), sum(t for a, t in sa))
    orc = [r for r in ok if r.get("oracle_inconsistent")]
    out["oracle_inconsistent_outputs"] = len(orc)
    out["gate_caught"] = sum(1 for r in orc if r["gate_raises"])
    out["gate_catch_pct"] = pct(out["gate_caught"], len(orc))
    out["gate_only_alarms"] = sum(1 for r in ok if r["gate_raises"] and not r["oracle_inconsistent"])
    out["gate_raised_total"] = sum(1 for r in ok if r["gate_raises"])
    out["mean_total_tokens"] = round(sum(r.get("total_tokens") or 0 for r in rows) / n) if n else None
    out["sum_total_tokens"] = sum(r.get("total_tokens") or 0 for r in rows)
    out["mean_latency_s"] = round(sum(r.get("latency_s") or 0 for r in rows) / n, 1) if n else None
    out["truncated_finish_length"] = sum(1 for r in rows if r.get("finish") == "length")
    return out


summary = {"by_run": {}, "by_family_gpt120_r1": {}, "by_family_all": {}}
for name, (mk, run) in GROUPS.items():
    rows = [r for r in per.values() if r["mkey"] == mk and r["run"] == run]
    summary["by_run"][name] = agg(rows)
fam = defaultdict(list)
for r in per.values():
    fam[r["family"]].append(r)
for f, rows in sorted(fam.items()):
    a = agg(rows)
    summary["by_family_all"][f] = {k: a[k] for k in ("n_outputs", "grounded_pct", "fabricated_pct", "unknown_recall_pct", "critical_recall_pct", "false_conflicts", "platform_mislabelled_pct", "critical_question_pct", "section_accuracy_pct")}
# injection
inj = {}
for r in per.values():
    if "injection_verdict" in r or "injection_checks" in r:
        inj[r["tag"]] = {"checks": r.get("injection_checks"), "verdict": r.get("injection_verdict")}
summary["injection"] = inj
# stability
summary["stability"] = {"mean_pct": None if stab["stability_mean"] is None else round(100 * stab["stability_mean"], 1),
                        "n_postings": len(stab["stability_by_posting"])}
# questions
rated = [q for q in qs if q.get("rating")]
summary["questions"] = {"total": len(qs), "rated": len(rated)}
if rated:
    def passes(q, na_counts=True):
        r = q["rating"]
        if r["c2"] is None or r["c4"] is None:
            return False
        c4 = r["c4"] if not r.get("na4") else na_counts
        return bool(r["c1"] and r["c2"] and r["c3"] and c4)
    byrun = defaultdict(list)
    for q in rated:
        mk = q["tag"].split("__")[1]
        run = q["tag"].split("__")[2]
        byrun[f"{mk}_{run}"].append(q)
    summary["questions"]["by_run"] = {}
    for k, v in sorted(byrun.items()):
        summary["questions"]["by_run"][k] = {"n": len(v), "pass_all4_pct": pct(sum(passes(q) for q in v), len(v)),
                                             "pass_all4_where_route_applies": f"{sum(passes(q) for q in v if not q['rating'].get('na4') and q['rating']['c4'] is not None)}/{sum(1 for q in v if not q['rating'].get('na4') and q['rating']['c4'] is not None)}",
                                             "c1_pct": pct(sum(q["rating"]["c1"] for q in v), len(v)),
                                             "c2_pct_among_gap_questions": pct(sum(1 for q in v if q["rating"]["c2"]), sum(1 for q in v if q["rating"]["c2"] is not None)),
                                             "c3_pct": pct(sum(q["rating"]["c3"] for q in v), len(v)),
                                             "c4_pct_where_route_exists": pct(sum(1 for q in v if q["rating"]["c4"] and not q["rating"].get("na4")), sum(1 for q in v if not q["rating"].get("na4") and q["rating"]["c4"] is not None)),
                                             "n_route_applies": sum(1 for q in v if not q["rating"].get("na4") and q["rating"]["c4"] is not None)}
    summary["questions"]["all"] = {"n": len(rated), "pass_all4_pct": pct(sum(passes(q) for q in rated), len(rated)),
                                   "pass_all4_where_route_applies": f"{sum(passes(q) for q in rated if not q['rating'].get('na4') and q['rating']['c4'] is not None)}/{sum(1 for q in rated if not q['rating'].get('na4') and q['rating']['c4'] is not None)}",
                                   "c1_pct": pct(sum(q["rating"]["c1"] for q in rated), len(rated)),
                                   "c2_pct_among_gap_questions": pct(sum(1 for q in rated if q["rating"]["c2"]), sum(1 for q in rated if q["rating"]["c2"] is not None)),
                                   "c3_pct": pct(sum(q["rating"]["c3"] for q in rated), len(rated)),
                                   "c4_pct_where_route_exists": pct(sum(1 for q in rated if q["rating"]["c4"] and not q["rating"].get("na4")), sum(1 for q in rated if not q["rating"].get("na4") and q["rating"]["c4"] is not None)),
                                   "n_route_applies": sum(1 for q in rated if not q["rating"].get("na4") and q["rating"]["c4"] is not None)}
    famq = defaultdict(list)
    gold = c.load_gold()
    for q in rated:
        famq[gold[q["pid"]]["type"].split("-")[0]].append(q)
    summary["questions"]["by_type_family"] = {k: {"n": len(v), "pass_all4_pct": pct(sum(passes(q) for q in v), len(v))} for k, v in sorted(famq.items())}
    summary["questions"]["unlisted_but_critical"] = sum(1 for q in rated if q["rating"].get("unlisted_critical"))
(SC / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=1))
