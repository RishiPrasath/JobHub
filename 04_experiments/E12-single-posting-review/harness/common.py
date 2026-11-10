"""Shared helpers for E12: load postings and gold labels, build the model input, paths.

Rerunnable. No network access here.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

E12 = Path(__file__).resolve().parents[1]
REPO = E12.parents[1]
sys.path.insert(0, str(REPO / "tools"))
sys.path.insert(0, str(E12 / "harness"))

DATA = E12 / "data"
RUN_ID = "2026-11-10-run-001"
RUN_DIR = E12 / "runs" / RUN_ID
RAW_DIR = RUN_DIR / "outputs" / "raw"

PROMPT_PATH = E12 / "harness" / "guarded-role-review-v2.md"  # byte-identical to E08 run 002
USER_PREFIX = "Review exactly this one posting input. Return only the required JSON object.\n\n"  # E08 run_batch.py wording

SECTIONS = ["role_identity", "duties", "qualifications", "work_conditions", "compensation",
            "compensation_rules", "application_process", "employer_context", "contradictions",
            "unknowns", "verification_questions"]

MODELS = {"gpt120": "openai/gpt-oss-120b", "qwen": "qwen/qwen3.8-27b", "oss20": "openai/gpt-oss-20b"}  # oss20 added after the gpt-oss-120b daily limit (see FINDINGS Deviations)
# (model key, run number)
RUNS = [("gpt120", 1), ("gpt120", 2), ("qwen", 1), ("oss20", 1)]
TEMPERATURE = 1.0
import os
MAX_TOKENS = int(os.environ.get('E12_MAX_TOKENS', '4096'))  # 4096 = E08 value; used for every call in run 001 (the env override was not used)
REASONING = "low"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


_HDR = re.compile(r"^=== (E12-P\d+) \| (.*) ===\s*$")


def load_postings() -> dict:
    """Return {posting_id: {id, meta{}, lines{Lnn: text}}} from data/postings/batch-*.txt."""
    out = {}
    for f in sorted((DATA / "postings").glob("batch-*.txt")):
        cur = None
        for raw in f.read_text(encoding="utf-8").splitlines():
            m = _HDR.match(raw)
            if m:
                pid = m.group(1)
                meta = {}
                for part in m.group(2).split(" | "):
                    if "=" in part:
                        k, v = part.split("=", 1)
                        meta[k.strip()] = v.strip()
                cur = {"id": pid, "meta": meta, "lines": {}}
                out[pid] = cur
                continue
            if cur is not None:
                mm = re.match(r"^(L\d\d): (.*)$", raw)
                if mm:
                    cur["lines"][mm.group(1)] = mm.group(2)
    return out


def load_gold() -> dict:
    gold = {}
    for f in sorted((DATA / "gold").glob("gold-*.json")):
        gold.update(json.loads(f.read_text(encoding="utf-8"))["postings"])
    return gold


def build_input(p: dict) -> dict:
    """The fixture object shown to the model. Nothing from meta except the board and ownership."""
    return {
        "posting_id": p["id"],
        "captured_at": "2026-11-10",
        "source": {"name": p["meta"]["board"], "ownership": p["meta"]["ownership"]},
        "evidence": dict(p["lines"]),
    }


def user_message(p: dict) -> str:
    return USER_PREFIX + json.dumps(build_input(p), ensure_ascii=False, indent=2)


def system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


def norm(s: str) -> str:
    s = s.lower()
    for ch in (chr(0x2013), chr(0x2014), chr(0x2011), chr(0x2010)):
        s = s.replace(ch, '-')
    s = s.replace(chr(0x2019), "'").replace(chr(0xa0), ' ')
    s = re.sub(r'(\d)\s+(am|pm)', r'\1\2', s)  # '7 pm' == '7pm' (scorer fix found while checking P09; applied to all outputs)
    s = re.sub(r's\$|\$', '', s)
    s = s.replace(',', '')
    return re.sub(r'\s+', ' ', s).strip()
