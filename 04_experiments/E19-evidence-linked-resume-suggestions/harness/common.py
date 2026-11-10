"""Shared helpers for the E19 harness: data loading, ledger rendering, text normalisation."""
from __future__ import annotations

import json
import re
from pathlib import Path

EXP = Path(__file__).resolve().parents[1]
DATA = EXP / "data"
RUN = EXP / "runs" / "2026-11-10-run-001"
OUTPUTS = RUN / "outputs"


def load_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def load_postings():
    return {p["id"]: p for p in load_json(DATA / "postings.json")}


def load_profiles():
    return {k: load_json(DATA / f"profile_{k}.json") for k in ("A", "B")}


def load_gold():
    return load_json(DATA / "gold" / "gold_sets.json")


def entry_values(e: dict) -> list[str]:
    out = []
    for k, v in e.items():
        if k in ("id", "type"):
            continue
        if isinstance(v, list):
            out += [str(x) for x in v]
        else:
            out.append(str(v))
    return out


def entry_text(e: dict) -> str:
    return " | ".join(entry_values(e))


def entries_by_id(profile: dict) -> dict:
    return {e["id"]: e for e in profile["entries"]}


def render_entry(e: dict, with_id: bool) -> str:
    t = e["type"]
    pre = f"[{e['id']}] " if with_id else ""
    if t == "work":
        s = (f"WORK: {e['title']} at {e['employer']} ({e['employment_type']}, {e['start']} to {e['end']}). "
             f"Role: {e['description']} Achievements: {'; '.join(e['achievements'])}. Skills used: {', '.join(e['skills_used'])}.")
    elif t == "education":
        s = f"EDUCATION: {e['qualification']}, {e['institution']} ({e['start']} to {e['end']}). Field: {e['field']}."
    elif t == "certification":
        s = f"CERTIFICATION/LICENCE: {e['name']} (issued by {e['issuing_body']}, {e['issued']})."
    elif t == "skill":
        s = f"SKILL: {e['name']}, level {e['level']}." + (f" {e['detail']}." if e.get("detail") else "")
    elif t == "language":
        s = f"LANGUAGES: {e['detail']}."
    elif t == "project":
        s = f"PROJECT: {e['title']} ({e['dates']}, {e['role']}). {e['description']} Skills used: {', '.join(e['skills_used'])}."
    else:
        s = entry_text(e)
    return pre + s


def render_ledger(profile: dict) -> str:
    return "\n".join(render_entry(e, True) for e in profile["entries"])


def render_resume(profile: dict) -> str:
    """Plain resume text in FEAT-016 section order, with no entry IDs."""
    sec = {"work": [], "education": [], "certification": [], "skill": [], "language": [], "project": []}
    for e in profile["entries"]:
        sec[e["type"]].append(render_entry(e, False))
    names = [("work", "EXPERIENCE"), ("education", "EDUCATION"), ("certification", "CERTIFICATIONS"),
             ("skill", "SKILLS"), ("language", "LANGUAGES"), ("project", "PROJECTS")]
    lines = [profile["personal"]["name"], "SUMMARY: " + profile["summary"]]
    for k, label in names:
        if sec[k]:
            lines.append(label)
            lines += ["- " + x for x in sec[k]]
    return "\n".join(lines)


NUMWORDS = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
            "eleven": 11, "twelve": 12, "fifteen": 15, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
            "sixty": 60, "hundred": 100, "dozen": 12}


def numbers_in(text: str) -> set[str]:
    """Numeric tokens in text as strings; number words are mapped to digits. Requirement ids (R1) are ignored."""
    t = re.sub(r"\bR\d+\b", " ", text)
    t = re.sub(r"(?<=\d),(?=\d{3}\b)", "", t)
    nums = set(re.findall(r"\d+(?:\.\d+)?", t))
    for w, n in NUMWORDS.items():
        if re.search(rf"\b{w}\b", t, flags=re.I):
            nums.add(str(n))
    return nums


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower()).strip()


def stem_in(stem_pattern: str, text: str) -> bool:
    return re.search(stem_pattern, text, flags=re.I) is not None
