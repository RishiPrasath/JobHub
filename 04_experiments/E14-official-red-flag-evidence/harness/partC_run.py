"""Part C simulated pilot. Run from the repo root:  python 04_experiments/E14-official-red-flag-evidence/harness/partC_run.py
Personas are simulations (tools/persona_creator.py). Results are labelled simulated and satisfy no Part C threshold.
"""
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "tools"))
from persona_creator import PersonaCreator  # noqa: E402
from llm_client import parse_json  # noqa: E402

E14 = REPO / "04_experiments/E14-official-red-flag-evidence"
OUT = E14 / "runs/2026-11-10-run-001/outputs/partC"
stim = json.loads((E14 / "data/partC_stimuli.json").read_text(encoding="utf-8"))["stimuli"]

pc = PersonaCreator(out_dir=str(OUT / "personas"), creator_model="openai/gpt-oss-120b", agent_model="openai/gpt-oss-20b")
agents = pc.spawn_on_demand(
    "job seekers in Singapore with mixed digital comfort, time pressure and trust in online tools; include a cautious one, "
    "a hurried one, a sceptical one, a low-digital-skill one",
    kind="job_seeker", n=6,
    task_context="read six short employer-check results and say what each means about the employer and what they would do next")

results = []
for i, a in enumerate(agents):
    order = [stim[(i + k) % len(stim)] for k in range(len(stim))]
    body = "\n\n".join(f"[{s['id']}]\n{s['text']}" for s in order)
    task = ("You are using a job-search tool. It showed you these six employer-check results, in this order. "
            "These are invented examples. For EACH id, say in your own words what it means about the employer, and what you would do next. "
            "Reply with JSON only: {\"S1\": {\"meaning\": \"...\", \"next\": \"...\"}, ... \"S6\": {...}}. Keep each field under 40 words.\n\n" + body)
    json_mode_failed = False
    try:
        r = a.ask(task, json_mode=True, max_tokens=1400, tag=f"partC-{a.persona.pid}")
    except Exception as e:  # the API rejected malformed JSON in json mode (seen for one persona); retry once without json mode
        json_mode_failed = True
        r = a.ask(task, json_mode=False, max_tokens=1400, tag=f"partC-nojson-{a.persona.pid}")
    results.append({"persona_id": a.persona.pid, "order": [s["id"] for s in order], "simulated": True,
                    "json_mode_failed": json_mode_failed,
                    "raw": r["content"], "parsed": parse_json(r["content"]),
                    "usage": {k: r.get(k) for k in ("prompt_tokens", "completion_tokens", "total_tokens") if k in r}})
(OUT / "answers.json").write_text(json.dumps({"label": "SIMULATED - personas are language-model simulations, not participants",
                                              "agent_model": "openai/gpt-oss-20b", "results": results},
                                             ensure_ascii=False, indent=1), encoding="utf-8")
print("done", len(results), "personas;", sum(1 for r in results if r["parsed"]), "parsed")
