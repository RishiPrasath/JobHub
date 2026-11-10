"""E17 Parts B and C: SIMULATED persona pilot. Six fictional job-seeker personas (tools/persona_creator.py) are not participants.
Part B pilot: each persona picks from the matcher's top three (qwen run 1) or 'none of these' on 8 postings.
Part C pilot: each persona reads three pay-range screens with the basis statement and answers what it tells them.
Usage: python persona_pilot.py [RUN_DIR]. Raw responses are cached; reruns repeat no spend."""
import csv
import json
import random
import sys
from pathlib import Path

E = Path(__file__).resolve().parents[1]
REPO = E.parents[1]
sys.path.insert(0, str(REPO / "tools"))
from persona_creator import PersonaCreator  # noqa: E402

rundir = Path(sys.argv[1]) if len(sys.argv) > 1 else E / "runs/2026-11-10-run-001"
out = rundir / "outputs/personas"
import os
MODEL = os.environ.get("PILOT_MODEL", "openai/gpt-oss-20b")  # run-001 used gpt-oss-120b after gpt-oss-20b hit its daily limit

# fixed before any matcher result was read
B_IDS = ["X3-11", "SYN-01", "X3-33", "X3-26", "SYN-08", "X3-04", "X3-16", "X3-21"]  # last two are true no-match. Substituted for SYN-24, SYN-10, SYN-31 because qwen run 1 was stopped before those postings (deviation)
C_SCREENS = [("X3-04", "within the typical range"), ("X3-36", "below the range, junior role"), ("X3-48", "above the range")]

BASIS = ("Where this comes from: Singapore Ministry of Manpower, Occupational Wage Table, reference month June 2025 "
         "(published June 2026). It covers full-time resident employees (citizens and permanent residents) in all industries "
         "and the gross monthly wage excludes bonuses. Advertised pay (what a posting says), offered pay (what you are told "
         "in an offer) and paid pay (what people actually receive) are different things. This range describes what people "
         "in the occupation were paid; it is not a judgement of any employer or of your worth.")


def main():
    posts = {p["id"]: p for p in json.loads((E / "data/postings.json").read_text(encoding="utf-8"))}
    gold = {g["id"]: g for g in json.loads((E / "data/gold.json").read_text(encoding="utf-8"))}
    x3 = {f"X3-{p['id']:02d}": p for p in json.loads(
        (E.parent / "E10-market-value-and-red-flag-experiments/outputs/x3/postings_ids.json").read_text(encoding="utf-8"))}
    mom = {r["ssoc2024"]: r for r in csv.DictReader(open(
        E.parent / "E10-market-value-and-red-flag-experiments/data/mom/occupations_all_industries.csv", encoding="utf-8"))}
    sl = json.loads((rundir / "outputs/shortlists.json").read_text(encoding="utf-8"))
    m1 = {r["id"]: r for r in json.loads((rundir / "outputs/matcher__qwen-qwen3-8-27b__run1__partial.json").read_text(encoding="utf-8"))["results"]}
    titles = {c["code"]: c["title"] for v in sl.values() for c in v}

    pc = PersonaCreator(out_dir=str(out), creator_model=MODEL, agent_model=MODEL)
    agents = pc.spawn_on_demand(
        "six job seekers in Singapore with mixed digital comfort, who skim: include an early-career graduate, a mid-career "
        "switcher, a worker in a manual or service job, a professional with a decade of experience, one sceptical of "
        "AI tools, and one who reads very literally",
        kind="job_seeker", n=6, seed=2, task_context="choose the occupation that matches a posting from a short list, then read a pay range")

    # ---------------- Part B ----------------
    b_screens = {}
    for pid in B_IDS:
        c3 = m1[pid]["top3"][:3]
        b_screens[pid] = c3
    b_rows = []
    for a in agents:
        lines = []
        mapping = {}
        for n, pid in enumerate(B_IDS, 1):
            p = posts[pid]
            opts = list(b_screens[pid])
            random.Random(f"{a.persona.pid}-{pid}").shuffle(opts)
            letters = "ABC"[:len(opts)]
            mapping[pid] = {l: c for l, c in zip(letters, opts)}
            optxt = "; ".join(f"{l}) {titles[c]}" for l, c in zip(letters, opts))
            lines.append(f"{n}. [{pid}] Posting: {p['title']} | {p['seniority']} | {p['employment_type']} | {p['function']}\n"
                         f"   Which occupation best describes this job? {optxt}; D) none of these")
        task = ("You are looking at job postings and a tool suggests which official occupation each one is, so it can show a pay "
                "range. For each posting choose the ONE option that best describes the job, or D if none fits. Answer as you "
                "naturally would, quickly.\n\n" + "\n".join(lines) +
                '\n\nReturn JSON only: {"answers": {"<posting id>": {"pick": "A|B|C|D", "note": "max 12 words"}}, '
                '"if_none_looked_right": "what you would do, max 25 words"}')
        r = a.ask(task, json_mode=True, max_tokens=1500, tag=f"{a.persona.pid}-partB")
        d = json.loads(r["content"]) if r["content"].strip().startswith("{") else {}
        b_rows.append({"persona": a.persona.pid, "mapping": mapping, "answers": d.get("answers", {}), "if_none": d.get("if_none_looked_right"),
                       "raw_ok": bool(d), "simulated": True})
    (out / "partB_answers.json").write_text(json.dumps({"simulated": True, "screens": b_screens, "rows": b_rows}, indent=1, ensure_ascii=False), encoding="utf-8")

    # ---------------- Part C ----------------
    c_screens = []
    for pid, kind in C_SCREENS:
        g = gold[pid]
        code = g["primary"]
        m = mom[code]
        p = x3[pid]
        c_screens.append({"id": pid, "kind": kind, "title": p["title"], "seniority": p["seniority"], "code": code, "occupation": m["occupation"],
                          "adv_min": p["salary_min"], "adv_max": p["salary_max"], "p25": m["gross_p25"], "median": m["gross_median"], "p75": m["gross_p75"]})
    c_rows = []
    for a in agents:
        blocks = []
        for s in c_screens:
            blocks.append(f"[{s['id']}] Posting: {s['title']} ({s['seniority']}). You confirmed the occupation: {s['occupation']}.\n"
                          f"   Advertised pay: ${s['adv_min']:,} to ${s['adv_max']:,} a month.\n"
                          f"   Official range for this occupation (gross monthly): lower quarter ${int(s['p25']):,}, middle ${int(s['median']):,}, upper quarter ${int(s['p75']):,}.\n"
                          f"   {BASIS}")
        task = ("You have confirmed the occupation for each posting below and the tool now shows a pay range. Read each screen as you "
                "naturally would and answer in your own words.\n\n" + "\n\n".join(blocks) +
                '\n\nReturn JSON only: {"screens": {"<posting id>": {"what_it_tells_me": "...", "what_it_does_not_tell_me": "...", '
                '"basis_in_my_own_words": "what the range is based on, as you understood it", "is_this_posting_fair_or_not": "your honest reading", '
                '"next_step": "what you would do"}}, "range_is_what_i_am_worth": "yes|no|unsure"} Each text field max 30 words.')
        r = a.ask(task, json_mode=True, max_tokens=2600, tag=f"{a.persona.pid}-partC")
        try:
            d = json.loads(r["content"])
        except Exception:
            d = {}
        c_rows.append({"persona": a.persona.pid, "screens": d.get("screens", {}), "worth": d.get("range_is_what_i_am_worth"),
                       "raw_ok": bool(d), "simulated": True})
    (out / "partC_answers.json").write_text(json.dumps({"simulated": True, "basis_text": BASIS, "screens": c_screens, "rows": c_rows}, indent=1, ensure_ascii=False), encoding="utf-8")
    print("personas", len(agents), "B ok", sum(r["raw_ok"] for r in b_rows), "C ok", sum(r["raw_ok"] for r in c_rows))


if __name__ == "__main__":
    main()
