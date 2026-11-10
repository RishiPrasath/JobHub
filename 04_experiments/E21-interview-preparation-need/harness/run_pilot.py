"""E21 simulated pilot runner. Creates 8 simulated job-seeker personas and has them answer the interview guide.

Frozen before running (protocol/FROZEN.md). Rerunnable: every model call is cached under outputs/raw.
Run from the repo root:  python 04_experiments/E21-interview-preparation-need/harness/run_pilot.py
Personas are simulations by a language model. Nothing here is evidence about real job seekers.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "tools"))
from llm_client import parse_json  # noqa: E402
from persona_creator import PersonaCreator  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "runs" / "2026-11-10-run-001" / "outputs"
CREATOR = "openai/gpt-oss-120b"
AGENT = "openai/gpt-oss-20b"

# (kind, n, brief, axes). 8 personas in total; the mix meets the protocol sample rules.
BATCHES = [
    ("career_switcher", 2, "Mid-career people in Singapore who recently switched or are trying to switch field and had at least one job interview in the last 6 months. One moving from an office field to a different office field, one moving from a non-office job into an office job.",
     ["previous field", "years of experience", "trust in AI tools", "how much they prepare"]),
    ("low_wage_worker", 2, "People in Singapore applying for NON-OFFICE roles (for example food service, retail, warehouse, cleaning, security, trades or delivery) who had a job interview in the last 6 months. Interviews may be short, informal, walk-in or a trial shift.",
     ["type of work", "age band", "digital comfort", "how much they prepare"]),
    ("foreign_professional", 1, "A professional from overseas on or seeking a work pass in Singapore who had an interview in the last 6 months, e.g. by video call, with an unfamiliar local hiring style.",
     ["home country style of interviewing", "English fluency", "trust in AI tools"]),
    ("job_seeker", 1, "An older job seeker with LOW digital comfort who mainly uses a phone, had one job interview in the last 6 months, and prefers to ask people rather than use apps.",
     ["digital comfort low", "confidence", "who they ask for help"]),
    ("job_seeker", 1, "A job seeker who NEVER prepares for interviews: they turn up and rely on being themselves, and see preparation as unnecessary or fake. Had an interview in the last 6 months.",
     ["why they do not prepare", "confidence", "how interviews went"]),
    ("early_career", 1, "A recent graduate who prepares heavily, uses AI assistants and mock-interview tools regularly, and had several interviews in the last 6 months. A deliberate counter-view: someone likely satisfied with existing tools.",
     ["AI use", "number of interviews", "confidence"]),
]

CONTEXT = ("You are taking part in a SIMULATED research interview about the most recent job interview you had in the last "
           "6 months. Invent plausible, specific details consistent with your persona (role, process, what you did). Answer in "
           "your own voice, 2 to 5 sentences per question. Do not be more articulate or more positive than your persona.")

Q_MAIN = """{ctx}

Interview questions (answer each):
1. Tell me about the most recent interview you had. What was the role, and what was the process (how many rounds, what format, one interviewer or a panel)?
2. How did you prepare for it? How long did you spend, and what did you use (friends or family, videos, articles, AI assistants, mock-interview tools, a coach or agency, nothing)? Did any of it cost money?
3. What was the hardest part? Were there questions you were not ready for? Tell me about one specific moment.
4. Did anything about the format surprise you?
5. Looking back, what would you have wanted before the interview that you did not have? What stopped you from preparing more?
6. Have you ever used an AI mock interview or a similar practice tool? What was it like? Did you carry on or stop, and why?
7. How do you feel about a practice tool recording your voice or video? How do you feel about where your answers would be stored?

Return JSON only: {{"q1": "...", "q2": "...", "q3": "...", "q4": "...", "q5": "...", "q6": "...", "q7": "..."}}"""

Q_LEAD = """Your earlier answers about your interview and preparation were:
{prev}

Next question: 8. Would you practise inside a tool that knows the job posting and your profile? Why, or why not?
Then: 9. Which of the interviewer's questions, if any, were unclear, or felt like they were nudging you toward an answer?
Answer in your own voice. Return JSON only: {{"q8": "...", "q9": "..."}}"""

Q_NEUT = """Your earlier answers about your interview and preparation were:
{prev}

Next question: 8N. Thinking about your last interview, if you had to get ready for the next one tomorrow, what would you do, and what would you want help with, if anything?
Answer in your own voice, 2 to 4 sentences. Return JSON only: {{"q8n": "..."}}"""


def main():
    pc = PersonaCreator(out_dir=str(OUT / "personas"), creator_model=CREATOR, agent_model=AGENT)
    agents = []
    for kind, n, brief, axes in BATCHES:
        agents += pc.spawn_on_demand(brief, kind=kind, n=n, axes=axes,
                                     task_context="a research interview about how they prepared for their latest job interview")
    answers, usage = {}, {"prompt": 0, "completion": 0, "total": 0, "calls": 0}

    def acc(r):
        u = r.get("usage") or {}
        usage["calls"] += 1
        for k, kk in (("prompt", "prompt_tokens"), ("completion", "completion_tokens"), ("total", "total_tokens")):
            usage[k] += u.get(kk, 0) if not r.get("cached") else 0

    for a in agents:
        pid = a.persona.pid
        r1 = a.ask(Q_MAIN.format(ctx=CONTEXT), json_mode=True, max_tokens=1300, tag=f"{pid}-main")
        acc(r1)
        d1 = parse_json(r1["content"]) or {}
        prev = "\n".join(f"{k}: {d1.get(k, '')}" for k in ("q1", "q2", "q3", "q4", "q5", "q6", "q7"))
        r2 = a.ask(Q_LEAD.format(prev=prev), json_mode=True, max_tokens=500, tag=f"{pid}-q8lead")
        acc(r2)
        r3 = a.ask(Q_NEUT.format(prev=prev), json_mode=True, max_tokens=350, tag=f"{pid}-q8neutral")
        acc(r3)
        d2, d3 = parse_json(r2["content"]) or {}, parse_json(r3["content"]) or {}
        answers[pid] = {**d1, **d2, **d3, "simulated": True, "persona_kind": a.persona.data.get("kind"),
                        "parse_ok": bool(d1 and d2 and d3)}
        print(pid, "parse_ok=", answers[pid]["parse_ok"], flush=True)
    (OUT / "answers.json").write_text(json.dumps(answers, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "usage.json").write_text(json.dumps({"creator_model": CREATOR, "agent_model": AGENT, "uncached_usage": usage,
                                                "note": "cached calls are counted as 0 tokens; creator-call tokens are in outputs/personas/raw"}, indent=1))
    print("usage (agent calls, uncached):", usage)


if __name__ == "__main__":
    main()
