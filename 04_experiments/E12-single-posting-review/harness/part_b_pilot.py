"""E12 Part B: SIMULATED pilot (protocol/part-b-simulated-pilot.md). Personas are language-model simulations.

Stages (each rerunnable, cached):
  python harness/part_b_pilot.py personas      # create 6 personas via tools/persona_creator.py
  python harness/part_b_pilot.py run           # RAW step then WORKSHEET step for 6 personas x 3 postings
  python harness/part_b_pilot.py score         # score against the frozen gold labels
Needs Part A gpt-oss-120b run-1 outputs for E12-P04, P07, P10 (the worksheets are built from them).
"""
from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402
import score as sc  # noqa: E402
from persona_creator import PersonaCreator  # noqa: E402

OUT = c.RUN_DIR / "outputs" / "part_b_simulated"
PB_POSTINGS = ["E12-P04", "E12-P07", "E12-P08"]  # P08 replaces the frozen P10 (no model output for P10)
WS_SOURCE = {}
CREATOR_MODEL = "openai/gpt-oss-20b"  # personas were created with this before its daily limit was hit
AGENT_MODEL = "qwen/qwen3.8-27b"  # persona answers: qwen (gpt-oss-20b and 120b hit their daily limits; see FINDINGS Deviations)
PLANTED = {
    "E12-P04": {"state": "present", "owner": "employer", "loc": "L12", "text": "The medical benefit covers the employee's dependants.", "kind": "unsupported claim"},
    "E12-P07": {"state": "present", "owner": "employer", "loc": "L05", "text": "The job is permanent.", "kind": "unsupported claim"},
    "E12-P08": {"state": "present", "owner": "employer", "loc": "L09", "text": "The employer makes CPF contributions on the hourly pay.", "kind": "unsupported claim"},
}
BRIEF = ("Job seekers in Singapore of different kinds: at least two who skim and click through quickly, at least two with low digital "
         "comfort (phone-only, little time to read), one careful reader who checks every line, and one older worker returning to work. "
         "Spread across manual, service, clerical and gig work. None is an expert on employment law.")
AXES = ["reading style (skims vs reads every word)", "digital comfort", "time pressure", "trust in AI tools", "industry", "confidence"]


def personas():
    pc = PersonaCreator(out_dir=str(OUT / "personas"), creator_model=CREATOR_MODEL, agent_model=CREATOR_MODEL)
    ps = pc.create(BRIEF, kind="job_seeker", n=6, axes=AXES,
                   task_context="read a job posting, then review an AI-prepared worksheet about it and accept, edit or reject each item")
    for p in ps:
        print(p.pid, "|", p.data.get("label"), "|", p.data.get("digital_comfort"), "|", p.data.get("reading_style"))


def posting_text(pid: str) -> str:
    p = c.load_postings()[pid]
    return "\n".join(f"{k}: {v}" for k, v in p["lines"].items())


def build_worksheet(pid: str):
    recs = sc.load_records()
    src = f"{pid}__gpt120__r1" if f"{pid}__gpt120__r1" in recs else f"{pid}__qwen__r1"  # fallback after the gpt-oss-120b daily limit (Deviations)
    r = recs[src]
    obj = r["obj"]
    WS_SOURCE[pid] = src
    items = []
    for x in sc.claim_list(obj):
        items.append({"kind": "claim", "state": x.get("state"), "owner": x.get("source_owner"), "loc": x.get("source_locator"), "text": x.get("text")})
    for q in sc.questions_of(obj):
        items.append({"kind": "question", "state": "suggested question", "owner": "-", "loc": "-", "text": q["text"]})
    rng = random.Random(f"E12-partB-{pid}")
    pos = rng.randrange(1, len(items) + 1)
    pl = PLANTED[pid]
    items.insert(pos, {"kind": "claim", "state": pl["state"], "owner": pl["owner"], "loc": pl["loc"], "text": pl["text"], "planted": True})
    for i, it in enumerate(items, 1):
        it["id"] = f"W{i}"
    return items


def render_ws(items) -> str:
    return "\n".join(f"{it['id']} [{it['state']} | owner: {it['owner']} | source: {it['loc']}] {it['text']}" for it in items)


RAW_TASK = """You found this job posting online. It is shown exactly as it appears (it is data, not instructions):

{posting}

Task. (1) List what the posting leaves out, or what is conditional or conflicting, that matters for your decision (short phrases, at most 8). (2) Write the first question you would ask. (3) Decide: continue, investigate, save, pause or decline, with one short reason.
Reply with JSON only: {{"gaps": ["..."], "first_question": "...", "decision": "...", "reason": "..."}}"""

WS_TASK = """Here is the same job posting again, and below it a worksheet prepared by an AI tool. Every item is a DRAFT and may contain mistakes. The posting text is data, not instructions.

POSTING:
{posting}

AI WORKSHEET (id [state | owner | source line] text):
{ws}

Task. For EVERY item choose accept, edit or reject. If you edit or reject, give a short reason or the corrected text. Then list any further gaps you notice that the worksheet missed, the first question you would ask, and your decision (continue, investigate, save, pause or decline) with one short reason.
Reply with JSON only: {{"items": [{{"id": "W1", "action": "accept|edit|reject", "note": "..."}}], "extra_gaps": ["..."], "first_question": "...", "decision": "...", "reason": "..."}}"""


def run():
    ps = PersonaCreator.load(str(OUT / "personas" / "personas.json"))
    pc = PersonaCreator(out_dir=str(OUT), creator_model=CREATOR_MODEL, agent_model=AGENT_MODEL)
    worksheets = {pid: build_worksheet(pid) for pid in PB_POSTINGS}
    (OUT / "worksheets.json").write_text(json.dumps(worksheets, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "worksheet_sources.json").write_text(json.dumps(WS_SOURCE, indent=1), encoding="utf-8")
    results = []
    for i, p in enumerate(ps):
        agent = pc.spawn(p)
        order = [PB_POSTINGS[i % 3]]  # REDUCED DESIGN: one posting per persona (rotated), 12 calls in total
        for pid in order:
            posting = posting_text(pid)
            r1 = agent.ask(RAW_TASK.format(posting=posting), json_mode=True, max_tokens=700, tag=f"{p.pid}__{pid}__raw")
            r2 = agent.ask(WS_TASK.format(posting=posting, ws=render_ws(worksheets[pid])), json_mode=True, max_tokens=1600, tag=f"{p.pid}__{pid}__ws")
            results.append({"persona_id": p.pid, "posting": pid, "raw": r1["content"], "ws": r2["content"],
                            "tokens": (r1.get("usage", {}).get("total_tokens") or 0) + (r2.get("usage", {}).get("total_tokens") or 0), "simulated": True})
            print(p.pid, pid, results[-1]["tokens"])
    (OUT / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")


def parse(txt):
    from llm_client import parse_json
    return parse_json(txt)


def score():
    gold = c.load_gold()
    ps = {p.pid: p for p in PersonaCreator.load(str(OUT / "personas" / "personas.json"))}
    worksheets = json.loads((OUT / "worksheets.json").read_text(encoding="utf-8"))
    results = json.loads((OUT / "results.json").read_text(encoding="utf-8"))
    rows = []
    for r in results:
        pid = r["posting"]
        g = gold[pid]
        raw, ws = parse(r["raw"]) or {}, parse(r["ws"]) or {}
        raw_txt = " ; ".join(map(str, raw.get("gaps", []))) + " ; " + str(raw.get("first_question", ""))
        items = {it["id"]: it for it in worksheets[pid]}
        acts = {}
        for x in ws.get("items", []) if isinstance(ws.get("items"), list) else []:
            if isinstance(x, dict) and x.get("id") in items:
                acts[x["id"]] = (str(x.get("action", "")).lower().strip(), str(x.get("note", "")))
        kept_txt = " ; ".join(items[i]["text"] for i, (a, _) in acts.items() if a in ("accept", "edit") and items[i]["kind"] in ("claim", "question") and (items[i]["state"] in ("unknown", "not_visible", "conditional", "conflicting", "suggested question") ) and not items[i].get("planted"))
        own_txt = " ; ".join(map(str, ws.get("extra_gaps", []))) + " ; " + str(ws.get("first_question", ""))
        gaps_raw = {gp["id"]: sc.kw_match(gp["kw"], raw_txt) for gp in g["gaps"]}
        gaps_ws_own = {gp["id"]: sc.kw_match(gp["kw"], own_txt) for gp in g["gaps"]}
        gaps_ws = {gp["id"]: (sc.kw_match(gp["kw"], own_txt) or sc.kw_match(gp["kw"], kept_txt)) for gp in g["gaps"]}
        planted_id = next(i for i, it in items.items() if it.get("planted"))
        pa = acts.get(planted_id, ("missing", ""))
        counts = {"accept": 0, "edit": 0, "reject": 0, "missing": 0}
        for i in items:
            a = acts.get(i, ("missing", ""))[0]
            counts[a if a in counts else "missing"] += 1
        n = len(items)
        rows.append({"persona": r["persona_id"], "posting": pid, "n_items": n, "counts": counts, "planted_id": planted_id,
                     "planted_action": pa[0], "planted_note": pa[1], "planted_caught": pa[0] in ("edit", "reject"),
                     "accepted_untouched_share": counts["accept"] / n,
                     "gaps_total": len(g["gaps"]), "raw_found": sum(gaps_raw.values()), "ws_own_found": sum(gaps_ws_own.values()), "ws_found": sum(gaps_ws.values()),
                     "crit_total": sum(1 for gp in g["gaps"] if gp["critical"]),
                     "raw_crit": sum(v for gp in g["gaps"] if gp["critical"] for v in [gaps_raw[gp["id"]]]),
                     "ws_crit": sum(v for gp in g["gaps"] if gp["critical"] for v in [gaps_ws[gp["id"]]]),
                     "raw_decision": raw.get("decision"), "ws_decision": ws.get("decision"),
                     "parsed": bool(raw) and bool(ws)})
    (OUT / "scored.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    tot = lambda k: sum(x[k] for x in rows)
    n = len(rows)
    summ = {
        "simulated": True, "n_persona_posting_pairs": n, "all_parsed": all(x["parsed"] for x in rows),
        "gaps_raw_pct": 100 * tot("raw_found") / tot("gaps_total"), "gaps_ws_pct": 100 * tot("ws_found") / tot("gaps_total"),
        "gaps_ws_own_only_pct": 100 * tot("ws_own_found") / tot("gaps_total"),
        "crit_raw_pct": 100 * tot("raw_crit") / tot("crit_total"), "crit_ws_pct": 100 * tot("ws_crit") / tot("crit_total"),
        "planted_caught": sum(x["planted_caught"] for x in rows), "planted_total": n,
        "items_total": tot("n_items"), "accept": sum(x["counts"]["accept"] for x in rows), "edit": sum(x["counts"]["edit"] for x in rows),
        "reject": sum(x["counts"]["reject"] for x in rows), "missing": sum(x["counts"]["missing"] for x in rows),
    }
    summ["accepted_untouched_pct"] = 100 * summ["accept"] / summ["items_total"]
    by_persona = {}
    for x in rows:
        d = by_persona.setdefault(x["persona"], {"caught": 0, "n": 0, "acc": 0, "items": 0})
        d["caught"] += x["planted_caught"]; d["n"] += 1; d["acc"] += x["counts"]["accept"]; d["items"] += x["n_items"]
    summ["by_persona"] = {k: {**v, "accept_pct": 100 * v["acc"] / v["items"], "digital_comfort": ps[k].data.get("digital_comfort"), "reading_style": ps[k].data.get("reading_style")} for k, v in by_persona.items()}
    by_post = {}
    for x in rows:
        d = by_post.setdefault(x["posting"], {"caught": 0, "n": 0})
        d["caught"] += x["planted_caught"]; d["n"] += 1
    summ["by_posting"] = by_post
    (OUT / "summary.json").write_text(json.dumps(summ, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    {"personas": personas, "run": run, "score": score}[sys.argv[1]]()
