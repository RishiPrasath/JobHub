"""SIMULATED Part B pilot: 6 personas (tools/persona_creator.py) react to a full page dump and to a stale notice.
Personas are simulations by a language model. They are not participants and cannot satisfy Part B.
Usage: python harness/run_pilot.py
"""
import json, sys
from pathlib import Path
EXP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXP.parents[1] / "tools"))
from persona_creator import PersonaCreator
from llm_client import parse_json

out = EXP / "runs/2026-11-10-run-001/outputs/personas"
dump = (EXP / "data/pilot/page_dump.txt").read_text(encoding="utf-8")
AGENT_MODEL = "openai/gpt-oss-20b"  # (a brief switch to 120b was abandoned: its daily token limit was exhausted after one persona)
pc = PersonaCreator(out_dir=str(out), agent_model=AGENT_MODEL)
brief = ("job seekers in Singapore who look at jobs on a phone or laptop; mixed digital comfort and patience, including a manual or service "
         "worker, an older career switcher and someone who skims; none of them is keen to do extra work for a tool")
agents = pc.spawn_on_demand(brief, kind="job_seeker", n=6, task_context="copy a job posting from a job site and paste it into a tool",
                            axes=["digital comfort", "device used (phone or laptop)", "patience", "job type sought", "confidence with tools"])

TASK_A = """You are job hunting on the device you normally use. You found a job you like and want to keep it in JobHub, a tool that checks postings.
JobHub shows a box that says "Paste the job posting here". You did Select All and Copy on the job page, and this is exactly what landed in the box:

<<<
{dump}
>>>

Answer as yourself, in JSON only:
{{"would_paste_as_is": true|false,
 "what_you_would_select_and_copy_instead": "plain words: which part, from which line to which line, or 'everything'",
 "how_you_would_do_it_on_your_device": "taps/drags/keys, in a sentence",
 "effort_1_to_5": 1 means very easy and 5 means not worth it,
 "seconds_you_expect_it_to_take": number,
 "problems_you_notice_in_the_pasted_text": "...",
 "would_you_do_this_for_every_job_you_consider": "yes|sometimes|no",
 "why": "..."}}"""

TASK_B = """Nine days ago you pasted a posting into JobHub (Administrative Assistant, Marina Dental Group). Today you open it and see this message above the saved posting.
Message 1: "This copy of the posting may be out of date. Paste the posting again to refresh it."
Message 2: "The closing date on this posting (20 Nov 2026) has passed, so it may no longer be open. Paste the posting again to refresh it."
Answer as yourself, in JSON only:
{{"message_1_means": "...", "message_1_why_it_appeared": "your guess", "what_you_would_do": "...",
 "would_you_rely_on_the_old_copy_meanwhile": "yes|no|unsure",
 "message_2_means": "...", "which_message_is_clearer": "1|2|same", "wording_problem_if_any": "..."}}"""

rows = []
for a in agents:
    ra = a.ask(TASK_A.format(dump=dump), json_mode=True, max_tokens=900, temperature=0.7, tag=f"A-{a.persona.pid}")
    rb = a.ask(TASK_B, json_mode=True, max_tokens=800, temperature=0.7, tag=f"B-{a.persona.pid}")
    rows.append({"persona_id": a.persona.pid, "label": a.persona.data.get("label"), "digital_comfort": a.persona.data.get("digital_comfort"),
                 "simulated": True, "task_a": parse_json(ra["content"]), "task_b": parse_json(rb["content"]),
                 "usage": [ra["usage"].get("total_tokens"), rb["usage"].get("total_tokens"), ]})
    print(a.persona.pid, "done", flush=True)
(out / "pilot_results.json").write_text(json.dumps({"SIMULATED": True, "agent_model": AGENT_MODEL, "note": "Language-model simulations, not participants.", "rows": rows}, indent=1, ensure_ascii=False), encoding="utf-8")
