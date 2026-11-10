"""E21 simulated pilot: keyword auto-coder and summary tables.

Frozen before the pilot ran (see protocol/FROZEN.md). Coding scheme: protocol/coding_scheme.md.
The auto-coder is deliberately crude; the specialist's manual reading (data/manual_codes.json) is the
primary coding and every disagreement is listed. Nothing here computes a pass/fail verdict.

Usage (from repo root):
  python 04_experiments/E21-interview-preparation-need/harness/code_answers.py auto
  python 04_experiments/E21-interview-preparation-need/harness/code_answers.py summary
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
RUN = HERE / "runs" / "2026-11-10-run-001" / "outputs"
DATA = HERE / "data"


def rx(p, t):
    return re.search(p, t, flags=re.I) is not None


TYPES = {
    "behavioural": r"behaviou?ral|tell me about a time|\bSTAR\b|conflict|weakness|strengths?\b|situational",
    "role_technical": r"technical|case study|hands-on|practical test|software|role-specific|skills? test|trade test|machine|equipment",
    "switch_story": r"\bswitch|career change|changing careers|transition|why (are you|did you) (leav|chang)|why this field",
    "assessment_format": r"assessment|psychometric|aptitude|online test|one-way|video interview|trial shift|group exercise|written test|\btest\b",
    "process_unknown": r"who (was|would be|will be) (interview|in the)|how many rounds|panel|did(n't| not) know (the|what) (process|format)|format",
}
CUE = (r"not ready|wasn'?t ready|unprepared|didn'?t expect|did not expect|blank|froze|couldn'?t answer|could not answer|"
       r"no idea|caught off|stumped|struggled|hardest|surpris|unfamiliar|didn'?t know|did not know|hadn'?t prepared|not prepared")


def auto_code(a: dict) -> dict:
    q = {k: (a.get(k) or "") for k in ("q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q8n")}
    for k in q:
        if not isinstance(q[k], str):
            q[k] = json.dumps(q[k])
    prep = q["q2"]
    m = []
    for name, pat in [("friends_family", r"friend|family|parent|spouse|husband|wife|sibling|brother|sister|cousin|colleague"),
                      ("videos", r"youtube|video|tiktok"),
                      ("articles", r"article|blog|website|google|reddit|glassdoor|forum|online search"),
                      ("ai_assistant", r"chatgpt|\bgpt\b|gemini|copilot|claude|ai assistant|\bAI\b"),
                      ("mock_tool", r"mock interview|practice tool|interview app|simulator|interview practice"),
                      ("coach_agency", r"coach|agency|recruiter|career cent|workshop|course|mentor"),
                      ("own_notes", r"notes|rehears|practis|practic|wrote|jotted|list of")]:
        if rx(pat, prep):
            m.append(name)
    nothing = rx(r"did(n't| not) (really )?prepare|no prep|nothing|wing(ed)? it|just (went|turned up|showed up)|never prepare", prep)
    if nothing and len(m) <= 1:
        m = ["none"]
    if not m:
        m = ["none"]
    specific = rx(r"research|job (description|posting|ad)|company (website|page)|about the company|looked up|tailor|read the posting|the posting", prep)
    pfr = "none" if m == ["none"] else ("specific" if specific else "generic")
    if rx(r"\$\s?\d|\bpaid\b|subscription|\bfee\b|bought|\bcost me", prep) and not rx(r"did(n't| not) pay|no cost|all free|\bfree\b", prep):
        cost = "paid"
    elif rx(r"\bfree\b|did(n't| not) pay|no cost|didn'?t spend|nothing", prep):
        cost = "free"
    else:
        cost = "unstated"
    gtext = q["q3"] + " " + q["q4"] + " " + q["q5"]
    types = [t for t, p in TYPES.items() if rx(p, gtext)]
    gap = "yes" if (types and rx(CUE, gtext)) else "no"
    ttext = prep + " " + q["q5"] + " " + q["q6"]
    if m == ["none"]:
        sat = "no_tools"
    else:
        neg = rx(r"not enough|too generic|generic|didn'?t help|did not help|useless|too general|didn'?t cover|didn'?t fit|disappoint|clunky|unhelpful|shallow|didn'?t match", ttext)
        pos = rx(r"helpful|worked well|good enough|satisfied|\bfine\b|useful|enough for me|did the job", ttext)
        sat = "partial" if (neg and pos) else "dissatisfied" if neg else "satisfied" if pos else "partial"
    unmet = "yes" if gap == "yes" and sat in ("partial", "dissatisfied", "no_tools") else "no"
    q6 = q["q6"].strip()
    neg6 = rx(r"^\W*(no\b|never|not yet|haven'?t|have not|i haven'?t|nope)", q6[:60])
    tried = "no" if (neg6 or not rx(r"mock|practice|simulat|tried|used", q6)) else "yes"
    if tried == "no":
        outc = "na"
    else:
        outc = ("stopped" if rx(r"stopped|quit|gave up|abandon|didn'?t continue|lost interest|too (generic|robotic|awkward)|boring", q6)
                else "continued" if rx(r"still use|kept|continue|regularly|carried on", q6) else "stopped")
    q8 = q["q8"].strip()
    if rx(r"^\W*(no\b|not really|probably not|nope|i wouldn'?t|i would not)", q8[:50]):
        use = "no"
    elif rx(r"not sure|unsure|don'?t know|maybe|might", q8[:80]):
        use = "unsure"
    elif rx(r"\bif\b|as long as|only if|provided|unless|depends|but\b", q8):
        use = "conditional" if rx(r"yes|would|sure|definitely|i'?d", q8[:120]) else "unsure"
    elif rx(r"yes|would|definitely|sure|absolutely|i'?d|sounds", q8):
        use = "yes"
    else:
        use = "unsure"
    q8n = q["q8n"]
    neu = ("named_tool_or_practice" if rx(r"practice|mock|rehears|simulat|\btool\b|\bapp\b|\bAI\b|chatgpt", q8n)
           else "other_help" if rx(r"feedback|tips|checklist|coach|friend|template|advice|someone|guide", q8n) else "nothing")
    q7 = q["q7"]
    vv = rx(r"record|voice|video|camera|face|audio|hear|mic", q7)
    st = rx(r"stor|saved|where|data|delet|privacy|share|employer|leak|hack|retain|safe", q7)
    nc = rx(r"don'?t mind|do not mind|fine with|no concern|not bothered|doesn'?t bother|no problem", q7)
    rec = "both" if (vv and st) else "voice_video" if vv else "storage" if st else "none" if nc else "unstated"
    if nc and rec in ("voice_video", "storage", "both") and not rx(r"worr|concern|uncomfortable|nervous|don'?t like|hate|creepy|weird|private", q7):
        rec = "none"
    stories = []
    if rx(TYPES["behavioural"] + r"|who (was|would be|will be) interview|interviewers", gtext):
        stories.append("S-23")
    if rx(TYPES["switch_story"], gtext):
        stories.append("S-24")
    if rx(TYPES["assessment_format"], gtext):
        stories.append("S-25")
    return {"prep_for_role": pfr, "prep_methods": m, "prep_cost": cost, "gap_named": gap, "gap_type": types or ["none"],
            "tool_satisfaction": sat, "gap_unmet": unmet, "tried_ai_mock": tried, "ai_mock_outcome": outc,
            "would_use_posting_tool": use, "would_use_neutral": neu, "recording_concern": rec,
            "story_raised": stories or ["none"]}


def load_answers() -> dict:
    return json.loads((RUN / "answers.json").read_text(encoding="utf-8"))


def pct(n, d):
    return f"{n}/{d} ({100 * n / d:.0f}%)" if d else "n/a"


def figures(codes: dict) -> dict:
    n = len(codes)

    def c(f):
        return sum(1 for v in codes.values() if f(v))

    return {
        "n": n,
        "prep_specific": pct(c(lambda v: v["prep_for_role"] == "specific"), n),
        "prep_none": pct(c(lambda v: v["prep_for_role"] == "none"), n),
        "gap_named": pct(c(lambda v: v["gap_named"] == "yes"), n),
        "gap_unmet": pct(c(lambda v: v["gap_unmet"] == "yes"), n),
        "tried_ai_mock": pct(c(lambda v: v["tried_ai_mock"] == "yes"), n),
        "ai_continued": c(lambda v: v["ai_mock_outcome"] == "continued"),
        "ai_stopped": c(lambda v: v["ai_mock_outcome"] == "stopped"),
        "use_posting_tool_strict_yes": pct(c(lambda v: v["would_use_posting_tool"] == "yes"), n),
        "use_posting_tool_loose_yes_or_conditional": pct(c(lambda v: v["would_use_posting_tool"] in ("yes", "conditional")), n),
        "neutral_wants_practice_or_tool": pct(c(lambda v: v.get("would_use_neutral") == "named_tool_or_practice"), n),
        "recording_concern": dict(Counter(v["recording_concern"] for v in codes.values())),
        "tool_satisfaction": dict(Counter(v["tool_satisfaction"] for v in codes.values())),
        "stories_raised": dict(Counter(s for v in codes.values() for s in v["story_raised"])),
        "gap_types": dict(Counter(s for v in codes.values() for s in v["gap_type"])),
        "methods": dict(Counter(s for v in codes.values() for s in v["prep_methods"])),
    }


SCALARS = ["prep_for_role", "prep_cost", "gap_named", "tool_satisfaction", "gap_unmet", "tried_ai_mock",
           "ai_mock_outcome", "would_use_posting_tool", "would_use_neutral", "recording_concern"]


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "auto"
    answers = load_answers()
    auto = {pid: auto_code(a) for pid, a in answers.items()}
    DATA.mkdir(exist_ok=True)
    (DATA / "auto_codes.json").write_text(json.dumps(auto, indent=1), encoding="utf-8")
    if cmd == "auto":
        print(json.dumps(figures(auto), indent=1))
        return
    manual = json.loads((DATA / "manual_codes.json").read_text(encoding="utf-8"))
    manual = {k: v for k, v in manual.items() if not k.startswith("_")}
    out = {"simulated": True, "label": "SIMULATED PILOT. Not evidence about job seekers. No verdict computed.",
           "figures_manual": figures(manual), "figures_auto": figures(auto)}
    dis = []
    agree = tot = 0
    for pid, mc in manual.items():
        for f in SCALARS:
            tot += 1
            if mc.get(f) == auto[pid].get(f):
                agree += 1
            else:
                dis.append({"persona": pid, "field": f, "manual": mc.get(f), "auto": auto[pid].get(f)})
    out["auto_vs_manual_scalar_agreement"] = pct(agree, tot)
    out["disagreements"] = dis
    (DATA / "coded_summary.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(json.dumps(out["figures_manual"], indent=1))
    print("auto vs manual agreement:", out["auto_vs_manual_scalar_agreement"], "disagreements:", len(dis))


if __name__ == "__main__":
    main()
