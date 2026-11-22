"""Part B simulated comprehension pilot. NOT a participant test. Six AI personas read eight prepared flags.

Cards come from the Part A deterministic results (pack text, unedited): 5 supported flags, 1 ambiguous flag and
2 real false alarms that the deterministic method produced. Persona answers are marked simulated.

Usage: python pilot.py
"""
import json
import os
import sys
import time
from pathlib import Path

EXP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXP.parents[1] / "tools"))
from persona_creator import PersonaCreator  # noqa: E402
from llm_client import parse_json  # noqa: E402

OUT = EXP / "runs" / "2026-11-10-run-001" / "outputs"
PDIR = OUT / "personas"

# (card label, case id, entry id, kind)
PICK = [("1", "C01", "P1-GENDER", "supported"), ("2", "C03", "P1-NATIONALITY", "supported"),
        ("3", "C06", "P3-FEE", "supported"), ("4", "C08", "P4-UNPAID", "supported"),
        ("5", "C09", "P4-DEDUCT", "supported"), ("6", "A06", "P2-APPEARANCE", "ambiguous"),
        ("7", "J02", "P1-GENDER", "false_alarm"), ("8", "E1", "P1-AGE", "false_alarm")]


def build_cards():
    cases = {c["case_id"]: c for c in json.loads((EXP / "data" / "cases.json").read_text(encoding="utf-8"))["cases"]}
    det = json.loads((OUT / "results_deterministic.json").read_text(encoding="utf-8"))
    R = {r["case_id"]: r for r in det["results"]}
    cards = []
    for lab, cid, eid, kind in PICK:
        f = [x for x in R[cid]["flags"] if x["entry_id"] == eid][0]
        src = "; ".join(s["name"] for s in f["sources"]) or "no official source found"
        cards.append({"card": lab, "case_id": cid, "kind": kind, "entry_id": eid,
                      "text": f"Posting extract: \"{cases[cid]['text']}\"\n"
                              f"Wording noted: \"{f['excerpt']}\"\n"
                              f"Why it may matter: {f['why_it_may_matter']}\n"
                              f"What is not established: {f['what_is_not_established']}\n"
                              f"Question you could ask: {f['suggested_question']}\n"
                              f"Source: {src}"})
    return cards


TASK = """A job-checking tool shows you {n} short notes about job postings. Read each note as you normally would, as this person.
For each note, answer:
- reads_as: "worth_asking" (it is something to ask the employer about; nothing is proven), or "discriminating_or_illegal" (it shows the employer is discriminating or acting illegally), or "unsure"
- not_established: in your own words, what the note does NOT show (write "nothing" or "don't know" if that is your honest answer)
- would_drop_posting: "yes" (you would stop and not follow up on this posting), "no" (you would still follow up), or "ask_first" (you would ask the question first and decide after)
- next_step: what you would actually do next, one short sentence

Return JSON only: {{"answers":[{{"card":"<number>","reads_as":"","not_established":"","would_drop_posting":"","next_step":""}}]}}

Notes:
{cards}"""

BRIEF = ("job seekers in Singapore who skim or read carefully, with mixed digital comfort and mixed trust in employers; "
         "include a fresh graduate, a mid-career worker over 50, a foreign professional on a work pass, a shift worker "
         "who needs work soon, one person who distrusts employers and one who trusts them; none is an expert in employment rules")


def main():
    cards = build_cards()
    (OUT / "pilot_cards.json").write_text(json.dumps(cards, ensure_ascii=False, indent=1), encoding="utf-8")
    PM = os.environ.get("PILOT_MODEL", "qwen/qwen3.8-27b")
    pc = PersonaCreator(out_dir=str(PDIR), creator_model=PM, agent_model=PM)
    agents = pc.spawn_on_demand(BRIEF, kind="job_seeker", n=6,
                                axes=["reading style", "trust in employers", "digital comfort", "urgency to find work", "prior experience of unfair treatment"],
                                task_context="read prepared notes from a job-checking tool and say what they mean")
    answers = []
    for i, a in enumerate(agents):
        order = cards if i % 2 == 0 else list(reversed(cards))
        text = "\n\n".join(f"Note {c['card']}:\n{c['text']}" for c in order)
        r = a.ask(TASK.format(n=len(order), cards=text), json_mode=True, max_tokens=1800, tag=f"pilot-{a.persona.pid}")
        data = parse_json(r["content"]) or {}
        answers.append({"persona_id": a.persona.pid, "simulated": True, "order": [c["card"] for c in order],
                        "parsed": data, "raw": r["content"], "usage": r.get("usage"), "finish_reason": r.get("finish_reason")})
        print(a.persona.pid, len((data or {}).get("answers", [])), "answers")
    (OUT / "pilot_answers.json").write_text(json.dumps({
        "label": "SIMULATED comprehension pilot (AI personas). Not a participant test.",
        "agent_model": PM, "creator_model": PM,
        "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "answers": answers}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
