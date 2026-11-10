"""SIMULATED pilot of the E20 Part A interview guide and a Part C style reaction, using tools/persona_creator.py.

Everything this script produces is simulated (personas are language-model inventions, not people).
It pilots the instrument and stress-tests the check's output wording. It evaluates no Part A or Part C threshold.

python harness/persona_pilot.py [--out-dir DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(ROOT / "harness"))
from persona_creator import PersonaCreator  # noqa: E402
from render_report import render  # noqa: E402

OUT = ROOT / "runs" / "2026-11-10-run-001" / "outputs" / "personas"
AGENT_MODEL = "qwen/qwen3.8-27b"  # gpt-oss-20b hit its DAILY LIMIT
CREATOR_MODEL = "qwen/qwen3.8-27b"
REPORT_LETTER = "L18"  # L17 was frozen but is outside the reduced sample; L18 chosen before reading any output

PART_A = """This is a simulated interview about the most recent job offer you received in the last 12 months in Singapore. Invent plausible details that fit your background (you are a simulation). Answer each question in at most 40 words, in your own voice. Return JSON with keys q1 to q7.
q1: What did you receive (a spoken offer, an email, a letter, a contract, a handbook), when, and what response deadline were you given?
q2: What did you check in the offer, how, and with whose help?
q3: Was anything different from what was advertised or agreed, or missing? What did you do about it?
q4: What do you wish you had known or asked?
q5: Would you have used a tool that checks an offer letter at that stage? What would have stopped you?
q6: What are you willing to share for research: a redacted letter, only the terms, or nothing? Why?
q7: Which of these six questions was hard to answer, unclear, repetitive, or leading? Say which and why. If none, say none."""

PART_C = """Imagine the offer letter below is similar to the one you received. A tool produced the report that follows it. Read both, then answer in at most 40 words per answer. Return JSON with keys r1 to r6.
r1: What do you notice in the report?
r2: Is there anything in it that you had not noticed or did not know? Say what.
r3: In your own words, what is the report telling you about the employer or the letter? Is it saying the employer did something wrong?
r4: What would you do next, if anything?
r5: Would you use it at your next offer? Why or why not?
r6: What in the report is confusing, too long, or worded badly?

=== LETTER ===
{letter}

=== REPORT ===
{report}"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(OUT))
    ap.add_argument("--results", default=str(ROOT / "runs" / "2026-11-10-run-001" / "outputs" / "parsed" / "qwen_qwen3_8_27b__run1.json"))
    a = ap.parse_args()
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    pc = PersonaCreator(out_dir=str(out), creator_model=CREATOR_MODEL, agent_model=AGENT_MODEL)
    task_ctx = "answer interview questions about a recent job offer and react to a check report on an offer letter"
    plan = [
        ("low_wage_worker", 1, "a manual or shift worker (warehouse, cleaning, maintenance or similar) who received a job offer in the last 12 months"),
        ("job_seeker", 2, "office professionals (finance, IT or operations), one skimming and one careful, each with a job offer in the last 12 months"),
        ("career_switcher", 1, "a mid-career person who recently moved into a new field and received an offer"),
        ("foreign_professional", 2, "non-resident professionals who received an offer from a Singapore employer, one on an Employment Pass application and one already in Singapore"),
    ]
    agents = []
    for kind, n, brief in plan:
        agents += pc.spawn_on_demand(brief, kind=kind, n=n, task_context=task_ctx)
    letter = (ROOT / "data" / "letters" / f"{REPORT_LETTER}.txt").read_text(encoding="utf-8")
    parsed = json.loads(Path(a.results).read_text(encoding="utf-8"))["results"][REPORT_LETTER]["parsed"]
    report = render(parsed)
    (out / "report_shown.txt").write_text(report, encoding="utf-8")
    records = []
    for ag in agents:
        ra = ag.ask(PART_A, json_mode=True, max_tokens=1200, tag=f"{ag.persona.pid}-partA")
        rc = ag.ask(PART_C.format(letter=letter, report=report), json_mode=True, max_tokens=1200, tag=f"{ag.persona.pid}-partC")
        records.append({"persona_id": ag.persona.pid, "kind": ag.persona.data.get("kind"), "label": ag.persona.data.get("label"),
                        "simulated": True, "part_a_raw": ra["content"], "part_c_raw": rc["content"],
                        "usage": {"a": ra.get("usage"), "c": rc.get("usage")}})
        print(ag.persona.pid, "done", flush=True)
    (out / "pilot_answers.json").write_text(json.dumps({"simulated": True, "note": "Answers by simulated personas, not real people.", "records": records}, indent=1, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
