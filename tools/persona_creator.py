"""Persona Creator: builds simulated personas on the fly and spawns them as sub-agents.

Role definition: agents/roles/19_persona-creator.md. Read it before use.

What it does
  1. `PersonaCreator.create(...)` turns a brief into N diverse, fictional personas (job seekers,
     employers, recruiters, career coaches, regulators, advisers, ...), saved as JSON.
  2. `PersonaCreator.spawn(persona)` turns one persona into a sub-agent that can be given tasks.
  3. `PersonaCreator.panel(...)` creates personas and runs the same task past all of them.
  4. `PersonaCreator.spawn_on_demand(...)` is the "whenever needed" entry point: describe the kind of
     person an experiment needs and get working sub-agents back.

What it must not be used for: personas are simulations by a language model. They are NOT users, they
cannot supply need evidence (N3/N4) or behaviour evidence (T4), and a result from them must always be
labelled "simulated". They are for finding problems in a test design, stress-testing outputs from
different viewpoints, and producing realistic inputs. They never replace the real participants in a
plan.

CLI
  python tools/persona_creator.py create --kind job_seeker --n 6 --brief "mid-career switchers in logistics" --out DIR
  python tools/persona_creator.py ask --personas DIR/personas.json --task "How would you check this offer?"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from llm_client import DEFAULT_MODELS, chat, parse_json  # noqa: E402

KINDS = {
    "job_seeker": "a person looking for work in Singapore",
    "career_switcher": "a mid-career person changing field",
    "early_career": "a recent graduate or first-time job seeker",
    "foreign_professional": "a non-resident professional seeking work in Singapore",
    "low_wage_worker": "a person in a manual, service or gig role",
    "employer": "a hiring manager or business owner who writes postings and makes offers",
    "recruiter": "an agency or in-house recruiter",
    "career_coach": "a career coach or counsellor who advises job seekers",
    "hr_professional": "an HR or employment-practice professional",
    "regulator_adviser": "someone with knowledge of Singapore employment guidance and enforcement",
    "scammer_adversary": "an adversary who writes deceptive postings (used only to stress-test detection fixtures)",
    "accessibility_user": "a job seeker who uses assistive technology or has limited time and attention",
    "other": "any other stakeholder described in the brief",
}

CREATOR_SYSTEM = """You are the Persona Creator for JobHub, a research project on job-search intelligence in Singapore.
You create FICTIONAL simulation personas for testing. Rules:
- Every persona is invented. Never use a real person, a real company's staff, or identifiable details.
- Vary the personas along the requested axes so the set is not clustered. Do not default to one profile.
- Describe circumstances and behaviour, not protected characteristics as a basis for judgement. Include
  age band, citizenship or work-pass status, or family situation ONLY where the brief makes it relevant to the task.
- Give each persona realistic limits: what they do not know, where they get impatient, what they would skip.
- Do not make any persona an expert, enthusiastic or compliant by default.
- Output JSON only."""

CREATOR_USER = """Brief: {brief}
Kind of persona: {kind} ({kind_desc})
Number of personas: {n}
Variation axes (spread the set across these): {axes}
Task context (what the personas will be asked to do; do not answer it): {task_context}

Return JSON: {{"personas": [{{
  "persona_id": "short-slug",
  "kind": "{kind}",
  "label": "6-10 word description",
  "first_name": "fictional first name",
  "background": "2-3 sentences, no identifying detail",
  "situation_now": "what they are doing about work/hiring right now",
  "goals": ["..."],
  "constraints": ["time, money, status, confidence, digital skill ..."],
  "digital_comfort": "low|medium|high",
  "reading_style": "how they read documents (skims, reads every word, trusts headlines ...)",
  "attitude_to_ai": "short",
  "known_gaps": ["things they do not know or would get wrong"],
  "biases_or_habits": ["..."],
  "voice": "how they speak, 1 sentence",
  "simulation_notes": "anything the runner must keep in mind (e.g. would abandon after 3 minutes)"
}}]}}"""

AGENT_SYSTEM = """You are simulating a fictional person for a research test. Stay in character and answer as they would.
Persona:
{persona}

Rules:
- Use only what this person would plausibly know. If they would not know something, say so or guess the way they would.
- Do not be more helpful, careful or articulate than the persona. Skim, skip, misread or get impatient where they would.
- You are a simulation. Never claim to be a real person or to have real experiences you can cite.
- If the task asks for JSON, return JSON only."""


@dataclass
class Persona:
    data: dict

    @property
    def pid(self) -> str:
        return self.data["persona_id"]

    def system_prompt(self) -> str:
        d = self.data
        lines = [f"{k}: {json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v}"
                 for k, v in d.items() if k not in ("persona_id",)]
        return AGENT_SYSTEM.format(persona="\n".join(lines))


@dataclass
class SubAgent:
    persona: Persona
    model: str
    cache_dir: str | None = None
    history: list = field(default_factory=list)

    def ask(self, task: str, *, json_mode: bool = False, max_tokens: int = 700, temperature: float = 0.7,
            tag: str = "", run: int = 1, remember: bool = False) -> dict:
        msgs = [{"role": "system", "content": self.persona.system_prompt()}]
        if remember:
            msgs += self.history
        msgs.append({"role": "user", "content": task})
        r = chat(self.model, msgs, json_mode=json_mode, max_tokens=max_tokens, temperature=temperature,
                 cache_dir=self.cache_dir, tag=tag or f"{self.persona.pid}", run=run,
                 reasoning_effort="low")
        if remember:
            self.history += [{"role": "user", "content": task}, {"role": "assistant", "content": r["content"]}]
        r["simulated"] = True
        r["persona_id"] = self.persona.pid
        return r


class PersonaCreator:
    def __init__(self, out_dir: str | None = None, creator_model: str | None = None,
                 agent_model: str | None = None):
        self.out_dir = Path(out_dir) if out_dir else None
        self.creator_model = creator_model or DEFAULT_MODELS["primary"]
        self.agent_model = agent_model or DEFAULT_MODELS["second"]
        self.cache = str(self.out_dir / "raw") if self.out_dir else None
        self.registry: dict[str, Persona] = {}

    # -- creation ----------------------------------------------------------------------------
    def create(self, brief: str, kind: str = "job_seeker", n: int = 4, axes: list[str] | None = None,
               task_context: str = "not specified", seed: int = 1) -> list[Persona]:
        if kind not in KINDS:
            kind = "other"
        axes = axes or ["experience level", "digital comfort", "time pressure", "trust in AI tools",
                        "industry", "confidence"]
        out: list[Persona] = []
        batch = 4  # keep each call small for the rate limit
        remaining, idx = n, 0
        while remaining > 0:
            k = min(batch, remaining)
            user = CREATOR_USER.format(brief=brief, kind=kind, kind_desc=KINDS[kind], n=k,
                                       axes=", ".join(axes), task_context=task_context)
            if idx:
                user += f"\nAlready created (make these clearly different): {[p.data['label'] for p in out]}"
            r = chat(self.creator_model, [{"role": "system", "content": CREATOR_SYSTEM},
                                          {"role": "user", "content": user}], json_mode=True,
                     max_tokens=2200 if k > 2 else 1400, temperature=0.9, cache_dir=self.cache,
                     tag=f"create-{kind}-{idx}", run=seed, reasoning_effort="low")
            data = parse_json(r["content"]) or {}
            for p in data.get("personas", []):
                if not p.get("persona_id"):
                    continue
                p["persona_id"] = f"{kind}-{len(out)+1:02d}-{p['persona_id']}"[:60]
                p["kind"] = kind
                p["simulated"] = True
                out.append(Persona(p))
            remaining -= k
            idx += 1
        for p in out:
            self.registry[p.pid] = p
        self._save(out, brief, kind)
        return out

    def _save(self, personas: list[Persona], brief: str, kind: str) -> None:
        if not self.out_dir:
            return
        self.out_dir.mkdir(parents=True, exist_ok=True)
        path = self.out_dir / "personas.json"
        existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"personas": []}
        existing["note"] = "Simulated personas created by tools/persona_creator.py. Not real users."
        existing.setdefault("batches", []).append({
            "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "kind": kind, "brief": brief,
            "creator_model": self.creator_model,
            "brief_sha256": hashlib.sha256(brief.encode()).hexdigest()[:12],
        })
        have = {p["persona_id"] for p in existing["personas"]}
        existing["personas"] += [p.data for p in personas if p.pid not in have]
        path.write_text(json.dumps(existing, ensure_ascii=False, indent=1), encoding="utf-8")

    # -- spawning ----------------------------------------------------------------------------
    def spawn(self, persona: Persona | dict, model: str | None = None) -> SubAgent:
        if isinstance(persona, dict):
            persona = Persona(persona)
        return SubAgent(persona, model or self.agent_model, self.cache)

    def spawn_on_demand(self, brief: str, kind: str = "job_seeker", n: int = 4, **kw) -> list[SubAgent]:
        """Describe who the experiment needs; get working sub-agents."""
        return [self.spawn(p) for p in self.create(brief, kind, n, **kw)]

    def panel(self, brief: str, task: str, kind: str = "job_seeker", n: int = 6, json_mode: bool = False,
              max_tokens: int = 700, **kw) -> list[dict]:
        agents = self.spawn_on_demand(brief, kind, n, task_context=task[:200], **kw)
        return [a.ask(task, json_mode=json_mode, max_tokens=max_tokens, tag=f"panel-{a.persona.pid}")
                for a in agents]

    @staticmethod
    def load(path: str) -> list[Persona]:
        return [Persona(p) for p in json.loads(Path(path).read_text(encoding="utf-8"))["personas"]]


def _main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("create")
    c.add_argument("--kind", default="job_seeker", choices=sorted(KINDS))
    c.add_argument("--n", type=int, default=4)
    c.add_argument("--brief", required=True)
    c.add_argument("--out", required=True)
    a = sub.add_parser("ask")
    a.add_argument("--personas", required=True)
    a.add_argument("--task", required=True)
    a.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.cmd == "create":
        pc = PersonaCreator(args.out)
        for p in pc.create(args.brief, args.kind, args.n):
            print(p.pid, "-", p.data.get("label"))
    else:
        pc = PersonaCreator(args.out)
        for p in PersonaCreator.load(args.personas):
            r = pc.spawn(p).ask(args.task)
            print(f"[{p.pid}] {r['content'][:600]}\n")


if __name__ == "__main__":
    _main()
