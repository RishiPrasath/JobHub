"""E17 Part A scoring against the frozen gold labels. Usage: python score.py [RUN_DIR]
Definitions: protocol/thresholds.md (operational definitions 1-8). Writes RUN_DIR/outputs/score.json.
Calls that failed (for example the Groq daily token limit) are NOT scored; they are counted as unscored and bounds are reported
(lower bound: every unscored posting a miss; upper bound: every unscored posting a hit)."""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

E = Path(__file__).resolve().parents[1]
rundir = Path(sys.argv[1]) if len(sys.argv) > 1 else E / "runs/2026-11-10-run-001"
gold = {g["id"]: g for g in json.loads((E / "data/gold.json").read_text(encoding="utf-8"))}
sl = json.loads((rundir / "outputs/shortlists.json").read_text(encoding="utf-8"))
ALL = list(gold)


def load(model, run):
    """Union of the final and rebuilt-from-cache result files; only parse_ok results with a valid verdict are kept."""
    slug = re.sub(r"[^A-Za-z0-9]+", "-", model).strip("-")
    out = {}
    for name in (f"matcher__{slug}__run{run}__partial.json", f"matcher__{slug}__run{run}.json"):
        p = rundir / "outputs" / name
        if p.exists():
            for r in json.loads(p.read_text(encoding="utf-8"))["results"]:
                if r.get("parse_ok") and r.get("verdict") in ("match", "none"):
                    out[r["id"]] = r
    return out


def pct(a, b):
    return round(100 * a / b, 1) if b else None


def real(g):
    return [c for c in g["accept"] if c != "NONE"]


def score(res):
    ids = [i for i in ALL if i in res]
    hit, hit_code, top1 = {}, {}, {}
    fam = defaultdict(lambda: [0, 0])
    stratum = defaultdict(lambda: [0, 0])
    sen_list, sen3 = [], 0
    true_nm = [i for i in ids if gold[i]["true_no_match"]]
    code_posts = [i for i in ids if real(gold[i]) and not gold[i]["none_acceptable"]]
    for i in ids:
        g, r = gold[i], res[i]
        t3 = r["top3"]
        a = bool(set(t3) & set(real(g)))
        b = g["none_acceptable"] and r["verdict"] == "none"
        hit[i], hit_code[i] = a or b, a
        top1[i] = bool(t3) and t3[0] in real(g)
        for d, k in ((fam, g["family"]), (stratum, g["stratum"])):
            d[k][0] += hit[i]
            d[k][1] += 1
        bad = set(g["too_senior"]) | set(g["too_junior"])
        if t3 and t3[0] in bad and r["verdict"] == "match":
            sen_list.append((i, g["title"][:40], t3[0], "senior" if t3[0] in g["too_senior"] else "junior"))
        if set(t3) & bad:
            sen3 += 1
    cw = [i for i in true_nm if res[i]["verdict"] == "match" and res[i]["confidence"] in ("high", "medium")]
    cwh = [i for i in true_nm if res[i]["verdict"] == "match" and res[i]["confidence"] == "high"]
    n = len(ids)
    unscored = [i for i in ALL if i not in res]
    unscored_nm = [i for i in unscored if gold[i]["true_no_match"]]
    nh = sum(hit.values())
    return {
        "n_scored": n, "n_unscored": len(unscored), "unscored_ids": unscored,
        "top3_hit_overall": {"hits": nh, "pct_of_scored": pct(nh, n), "lower_bound_pct_of_100": pct(nh, 100),
                             "upper_bound_pct_of_100": pct(nh + len(unscored), 100)},
        "top3_recall_gold_code_postings": [sum(hit_code[i] for i in code_posts), len(code_posts), pct(sum(hit_code[i] for i in code_posts), len(code_posts))],
        "top1_gold_code_postings": [sum(top1[i] for i in code_posts), len(code_posts), pct(sum(top1[i] for i in code_posts), len(code_posts))],
        "true_no_match_scored": len(true_nm), "true_no_match_unscored": len(unscored_nm),
        "no_match_flagged_none": [sum(res[i]["verdict"] == "none" for i in true_nm), len(true_nm)],
        "confident_wrong_match_medium_or_high": [len(cw), len(true_nm), cw],
        "confident_wrong_match_high_only": [len(cwh), len(true_nm)],
        "no_match_handled_correctly": {"pct_of_scored": pct(len(true_nm) - len(cw), len(true_nm)),
                                       "lower_bound_of_20": pct(len(true_nm) - len(cw), 20),
                                       "upper_bound_of_20": pct(len(true_nm) - len(cw) + len(unscored_nm), 20)},
        "false_none_on_gold_code_postings": [sum(res[i]["verdict"] == "none" for i in code_posts), len(code_posts)],
        "seniority_errors_top1": len(sen_list), "seniority_errors_any_of_top3": sen3, "seniority_error_list": sen_list,
        "by_family_hit": {f: [v[0], v[1], pct(v[0], v[1])] for f, v in sorted(fam.items())},
        "by_stratum_hit": {k: [v[0], v[1], pct(v[0], v[1])] for k, v in stratum.items()},
        "misses": [(i, gold[i]["title"][:45], gold[i]["accept"], res[i]["top3"], res[i]["verdict"], res[i]["confidence"]) for i in ids if not hit[i]],
    }


runs = {"qwen_r1": load("qwen/qwen3.8-27b", 1), "qwen_r2": load("qwen/qwen3.8-27b", 2), "gptoss20b_r1": load("openai/gpt-oss-20b", 1)}
R = {"coverage": {k: len(v) for k, v in runs.items()}}
for k, v in runs.items():
    if v:
        R[k] = score(v)

a, b, c = runs["qwen_r1"], runs["qwen_r2"], runs["gptoss20b_r1"]
ids = [i for i in ALL if i in a and i in b]
if ids:
    ss = sum(set(a[i]["top3"]) == set(b[i]["top3"]) for i in ids)
    s1 = sum(a[i]["top3"][:1] == b[i]["top3"][:1] for i in ids)
    sv = sum(a[i]["verdict"] == b[i]["verdict"] for i in ids)
    R["stability_qwen_r1_vs_r2"] = {
        "n_overlap": len(ids), "same_top3_set": [ss, pct(ss, len(ids))], "same_top1": [s1, pct(s1, len(ids))],
        "same_verdict": [sv, pct(sv, len(ids))],
        "unstable_ids": [(i, a[i]["top3"], b[i]["top3"]) for i in ids if set(a[i]["top3"]) != set(b[i]["top3"])],
        "families_in_overlap": sorted({gold[i]["family"] for i in ids})}
    R["qwen_r1_on_r2_overlap"] = score({i: a[i] for i in ids})
    R["qwen_r2_on_r2_overlap"] = score({i: b[i] for i in ids})
ids = [i for i in ALL if i in a and i in c]
if ids:
    R["cross_model_qwen_r1_vs_gptoss"] = {
        "n_overlap": len(ids), "same_top3_set": sum(set(a[i]["top3"]) == set(c[i]["top3"]) for i in ids),
        "same_top1": sum(a[i]["top3"][:1] == c[i]["top3"][:1] for i in ids),
        "same_verdict": sum(a[i]["verdict"] == c[i]["verdict"] for i in ids)}
    R["qwen_r1_on_gptoss_overlap"] = score({i: a[i] for i in ids})
    R["gptoss_on_qwen_overlap"] = score({i: c[i] for i in ids})

real_posts = [i for i in ALL if real(gold[i])]
lost = [i for i in real_posts if not ({x["code"] for x in sl[i]} & set(real(gold[i])))]
R["shortlist_loss"] = {"postings_with_real_gold_code": len(real_posts), "gold_absent_from_shortlist": len(lost),
                       "pct": pct(len(lost), len(real_posts)), "lost": [(i, gold[i]["title"], gold[i]["accept"]) for i in lost]}

(rundir / "outputs/score.json").write_text(json.dumps(R, ensure_ascii=False, indent=1, default=list), encoding="utf-8")
for k in ("coverage", "stability_qwen_r1_vs_r2", "cross_model_qwen_r1_vs_gptoss", "shortlist_loss"):
    if k in R:
        print(k, json.dumps(R[k], ensure_ascii=False)[:700])
for k in ("qwen_r1", "qwen_r2", "gptoss20b_r1", "qwen_r1_on_r2_overlap", "qwen_r2_on_r2_overlap", "qwen_r1_on_gptoss_overlap", "gptoss_on_qwen_overlap"):
    if k in R:
        s = R[k]
        print(k, {x: s[x] for x in s if x not in ("by_family_hit", "misses", "seniority_error_list", "by_stratum_hit", "unscored_ids")})
