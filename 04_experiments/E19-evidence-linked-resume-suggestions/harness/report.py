"""Aggregate scored results into tables (by model, method, run and by case type)."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import OUTPUTS, load_gold  # noqa: E402

GOLD = load_gold()


def pct(a, b):
    return f"{100 * a / b:.1f}% ({a}/{b})" if b else "n/a (0)"


def summarise(scored: dict, method: str, restrict=None):
    sets = {k: v for k, v in scored["sets"].items() if (restrict is None or restrict(k, v))}
    S = {"sets": len(sets), "parse_fail": sum(1 for v in sets.values() if not v["parse_ok"])}
    raw_n = disp_n = 0
    fab = defaultdict(int)
    unsup_disp = unsup_raw = 0
    intent_disp = intent_raw = 0
    mis_disp = mis_raw = 0
    inj_text_sets = inj_raw_sets = 0
    cite_ok = cite_n = 0
    gap_total = gap_primary = gap_strict = 0
    prec_n = prec_ok = 0
    sup_total = sup_covered = 0
    drop_good = good_raw = 0
    bad_raw = bad_dropped = 0
    tokens = lat = 0
    for sid, v in sets.items():
        sg = GOLD["sets"][sid]
        tokens += (v.get("usage") or {}).get("total_tokens", 0)
        lat += v.get("latency_s") or 0
        raw, disp = v["raw_items"], v["displayed"]
        raw_n += len(raw); disp_n += len(disp)
        if v["injection_in_raw"]:
            inj_raw_sets += 1
        gaps = set(v.get("gaps", []))
        if method == "M3":
            for it in disp:
                cite_n += 1
                cite_ok += bool(it["entry_valid"] and it["req_valid"])
                prec_n += 1; prec_ok += bool(it["in_gold"])
                if it["fills_gap"] or not it["entry_valid"]:
                    unsup_disp += 1
            unsup_raw = unsup_disp
            for r, g in sg["requirements"].items():
                tied = [it for it in disp if it["requirement"] == r]
                if g["status"] == "gap":
                    gap_total += 1
                    gap_primary += (r in gaps) and not any(it["fills_gap"] for it in tied)
                    gap_strict += (r in gaps) and not tied
                if g["status"] == "supported":
                    sup_total += 1
                    sup_covered += any(it["in_gold"] for it in tied)
            continue
        injected_here = False
        for it in raw:
            if it["unsupported"]:
                unsup_raw += 1
            intent_raw += it["intent"]; mis_raw += it["misattribution"]
            if method == "M2":
                clean_gold = (not it["unsupported"]) and it["cited_subset_of_gold"] and it["req_status"] in ("supported", "partial")
                if clean_gold:
                    good_raw += 1; drop_good += (not it["displayed"])
                if it["unsupported"]:
                    bad_raw += 1; bad_dropped += (not it["displayed"])
        for it in disp:
            if it["unsupported"]:
                unsup_disp += 1
            for t in it["fabricated"]:
                fab[t] += 1
            intent_disp += it["intent"]; mis_disp += it["misattribution"]
            if it["injection"]:
                injected_here = True
            cite_n += 1
            if method == "M2":
                cite_ok += bool(it["entry_ids_valid"] and it["req_valid"])
                prec_n += 1; prec_ok += bool(it["cited_subset_of_gold"])
            else:
                cite_ok += bool(it["req_valid"])
        inj_text_sets += injected_here
        for r, g in sg["requirements"].items():
            tied = [it for it in disp if it["requirement"] == r]
            if g["status"] == "gap":
                gap_total += 1
                gap_primary += (r in gaps) and not any(it["unsupported"] for it in tied)
                gap_strict += (r in gaps) and not tied
            if g["status"] == "supported":
                sup_total += 1
                if method == "M2":
                    sup_covered += any(it["cited_subset_of_gold"] and not it["unsupported"] for it in tied)
                else:
                    sup_covered += any((not it["unsupported"]) for it in tied)
    S.update({
        "raw_items": raw_n, "displayed_items": disp_n,
        "fabricated_displayed": dict(fab), "fabricated_displayed_total": sum(fab.values()),
        "unsupported_displayed": pct(unsup_disp, disp_n), "unsupported_displayed_n": unsup_disp,
        "unsupported_raw": pct(unsup_raw, raw_n),
        "citation_complete": pct(cite_ok, cite_n),
        "gap_primary": pct(gap_primary, gap_total), "gap_strict": pct(gap_strict, gap_total),
        "intent_displayed": intent_disp, "intent_raw": intent_raw,
        "misattribution_displayed": mis_disp, "misattribution_raw": mis_raw,
        "injection_followed_displayed_sets": inj_text_sets, "injection_in_raw_sets": inj_raw_sets,
        "precision_vs_gold_entries": pct(prec_ok, prec_n) if method != "M1" else "n/a (no citations)",
        "recall_supported_requirements": pct(sup_covered, sup_total),
        "m2_overdrop_of_clean_gold": pct(drop_good, good_raw) if method == "M2" else "n/a",
        "m2_unsupported_caught_by_filter": pct(bad_dropped, bad_raw) if method == "M2" else "n/a",
        "tokens_per_set": round(tokens / max(len(sets), 1)), "seconds_per_set": round(lat / max(len(sets), 1), 1),
        "total_tokens": tokens,
    })
    return S


def stability(a: dict, b: dict, method: str):
    same = 0; jac = []
    for sid in a["sets"]:
        if sid not in b["sets"]:
            continue
        def feats(v):
            if method == "M3":
                ids = {i["entry_id"] for i in v["displayed"]}
                f = 0
            else:
                ids = {e for i in v["displayed"] for e in i["entry_ids"]}
                f = sum(1 for i in v["displayed"] if i["fabricated"])
            return ids, f > 0
        ia, fa = feats(a["sets"][sid]); ib, fb = feats(b["sets"][sid])
        same += (fa == fb)
        jac.append(len(ia & ib) / len(ia | ib) if (ia | ib) else 1.0)
    n = len(jac)
    return {"sets_compared": n, "same_fabrication_status": pct(same, n), "mean_jaccard_entries": round(sum(jac) / n, 3) if n else None}


def main():
    sd = OUTPUTS / "scored"
    files = {p.name: json.loads(p.read_text(encoding="utf-8")) for p in sorted(sd.glob("*.json"))}
    out = {"runs": {}, "by_case_type": {}, "stability": {}}
    lines = []
    for name, sc in files.items():
        m = sc["meta"]["method"]
        out["runs"][name] = summarise(sc, m)
        types = sorted({t for sid in sc["sets"] for t in GOLD["sets"][sid]["case_types"]})
        out["by_case_type"][name] = {t: summarise(sc, m, lambda k, v, t=t: t in v["case_types"]) for t in types}
    keys = defaultdict(dict)
    for name, sc in files.items():
        keys[(sc["meta"]["model"], sc["meta"]["method"])][sc["meta"]["run"]] = sc
    for (model, m), runs in keys.items():
        if 1 in runs and 2 in runs:
            out["stability"][f"{model}__{m}"] = stability(runs[1], runs[2], m)
    (OUTPUTS / "summary.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    cols = ["sets", "parse_fail", "displayed_items", "fabricated_displayed_total", "unsupported_displayed", "unsupported_raw", "citation_complete",
            "gap_primary", "gap_strict", "intent_displayed", "intent_raw", "misattribution_displayed", "injection_followed_displayed_sets",
            "injection_in_raw_sets", "recall_supported_requirements", "precision_vs_gold_entries", "m2_overdrop_of_clean_gold",
            "m2_unsupported_caught_by_filter", "tokens_per_set", "seconds_per_set"]
    lines.append("| run | " + " | ".join(cols) + " |")
    lines.append("|" + "---|" * (len(cols) + 1))
    for name, s in out["runs"].items():
        lines.append("| " + name.replace(".json", "") + " | " + " | ".join(str(s[c]) for c in cols) + " |")
    (OUTPUTS / "tables.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
