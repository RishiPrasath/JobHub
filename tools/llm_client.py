"""Shared, rate-limit-aware client for JobHub experiments (Groq via the OpenAI SDK).

Why this exists: the account is limited to about 8,000 tokens per minute per model, and several
experiments may run at once. All callers share one cross-process limiter, every call is cached on
disk (so reruns do not repeat spend), and every raw request/response is saved for the run record.

Secrets: the key is read from the repo `.env` (git-ignored) or the environment. It is never printed
or written to a cache file.

Usage:
    from llm_client import chat, parse_json
    r = chat("openai/gpt-oss-120b", [{"role": "user", "content": "..."}], json_mode=True,
             cache_dir="04_experiments/EXX/runs/.../outputs/raw", tag="posting-07-run1")
    data = parse_json(r["content"])
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TPM_BUDGET = int(os.environ.get("JOBHUB_TPM_BUDGET", "6500"))  # leave headroom under 8,000
DEFAULT_MODELS = {
    "primary": "openai/gpt-oss-120b",
    "second": "qwen/qwen3.8-27b",
    "small": "openai/gpt-oss-20b",
}


def load_env() -> None:
    p = REPO / ".env"
    if not p.exists():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if v:
                os.environ.setdefault(k, v)


def _client():
    load_env()
    from openai import OpenAI
    return OpenAI(
        api_key=os.environ["GROQ_API_KEY"],
        base_url=os.environ.get("GROQ_BASE_URL", "https://api.groq.com/openai/v1"),
        timeout=float(os.environ.get("GROQ_TIMEOUT_SECONDS", "90")),
        max_retries=0,
    )


# ---- cross-process sliding-window token limiter -------------------------------------------------
_LOCKDIR = Path(tempfile.gettempdir()) / "jobhub_ratelimit"


def _lock_path(model: str) -> Path:
    return _LOCKDIR / (re.sub(r"[^A-Za-z0-9_.-]", "_", model) + ".lock")


def _state_path(model: str) -> Path:
    return _LOCKDIR / (re.sub(r"[^A-Za-z0-9_.-]", "_", model) + ".json")


class _Lock:
    def __init__(self, model: str):
        self.p = _lock_path(model)

    def __enter__(self):
        _LOCKDIR.mkdir(parents=True, exist_ok=True)
        t0 = time.time()
        while True:
            try:
                fd = os.open(str(self.p), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.close(fd)
                return self
            except (FileExistsError, PermissionError):  # Windows raises PermissionError under contention
                try:
                    if time.time() - self.p.stat().st_mtime > 20:  # stale lock
                        self.p.unlink()
                except OSError:
                    pass
                if time.time() - t0 > 120:
                    raise TimeoutError("rate-limit lock timeout")
                time.sleep(0.05)

    def __exit__(self, *a):
        try:
            self.p.unlink()
        except OSError:
            pass


def _reserve(model: str, tokens: int) -> None:
    """Block until `tokens` fit in the 60 s window, then record them."""
    tokens = min(tokens, TPM_BUDGET)
    while True:
        with _Lock(model):
            sp = _state_path(model)
            try:
                events = json.loads(sp.read_text()) if sp.exists() else []
            except Exception:
                events = []
            now = time.time()
            events = [e for e in events if now - e[0] < 60]
            used = sum(e[1] for e in events)
            if used + tokens <= TPM_BUDGET:
                events.append([now, tokens])
                sp.write_text(json.dumps(events))
                return
            wait = max(0.5, 60 - (now - events[0][0]) + 0.2) if events else 1
        time.sleep(min(wait, 10))


def _penalise(model: str, seconds: float) -> None:
    """After a 429, fill the window so every process backs off."""
    with _Lock(model):
        sp = _state_path(model)
        sp.write_text(json.dumps([[time.time() + seconds - 60, TPM_BUDGET]]))


# ---- helpers ------------------------------------------------------------------------------------
def parse_json(text: str):
    """Parse model output as JSON, tolerating code fences and leading prose. Returns None on failure."""
    if text is None:
        return None
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.S)
    try:
        return json.loads(t)
    except Exception:
        pass
    m = re.search(r"\{.*\}|\[.*\]", t, flags=re.S)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            return None
    return None


def _est_tokens(messages, max_tokens: int) -> int:
    chars = sum(len(m["content"]) for m in messages)
    return int(chars / 3.2) + max_tokens


def chat(model: str, messages: list, *, json_mode: bool = False, max_tokens: int = 1500,
         temperature: float = 0.2, reasoning_effort: str | None = None, cache_dir: str | None = None,
         tag: str = "", run: int = 1, retries: int = 8) -> dict:
    """One chat call with limiter, cache and raw-record. Returns dict(content, usage, model, cached, ...)."""
    key = hashlib.sha256(json.dumps([model, messages, json_mode, max_tokens, temperature,
                                      reasoning_effort, run], sort_keys=True).encode()).hexdigest()[:20]
    cpath = None
    if cache_dir:
        d = Path(cache_dir)
        d.mkdir(parents=True, exist_ok=True)
        cpath = d / f"{re.sub(r'[^A-Za-z0-9_.-]', '_', tag or 'call')}__{re.sub(r'[^A-Za-z0-9]', '', model)[:14]}__{key}.json"
        if cpath.exists():
            rec = json.loads(cpath.read_text(encoding="utf-8"))
            rec["cached"] = True
            return rec
    client = _client()
    kwargs = dict(model=model, messages=messages, max_tokens=max_tokens, temperature=temperature)
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    if reasoning_effort and "gpt-oss" in model:
        kwargs["reasoning_effort"] = reasoning_effort
    last_err = None
    for attempt in range(1, retries + 1):
        _reserve(model, _est_tokens(messages, max_tokens))
        t0 = time.time()
        try:
            resp = client.chat.completions.create(**kwargs)
            msg = resp.choices[0].message
            rec = {
                "model": model, "tag": tag, "run": run, "attempt": attempt,
                "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "latency_s": round(time.time() - t0, 2),
                "params": {k: v for k, v in kwargs.items() if k != "messages"},
                "messages": messages,
                "content": msg.content or "",
                "finish_reason": resp.choices[0].finish_reason,
                "usage": resp.usage.model_dump() if resp.usage else {},
                "cached": False,
            }
            if cpath:
                cpath.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
            return rec
        except Exception as e:  # noqa: BLE001
            last_err = e
            name = type(e).__name__
            text = str(e)
            if "429" in text or "rate" in name.lower():
                m = re.search(r"try again in (?:(\d+)m)?(?:([\d.]+)s)?", text)
                wait = 20.0
                if m:
                    wait = (int(m.group(1) or 0) * 60) + float(m.group(2) or 0) + 1
                if "per day" in text.lower() or "TPD" in text:
                    raise RuntimeError(f"DAILY LIMIT: {text[:300]}") from e
                _penalise(model, min(wait, 90))
                time.sleep(min(wait, 90))
                continue
            if any(s in text for s in ("500", "502", "503", "504", "timed out", "Timeout", "Connection")):
                time.sleep(3 * attempt)
                continue
            raise
    raise RuntimeError(f"chat failed after {retries} attempts: {last_err}")


if __name__ == "__main__":
    r = chat(DEFAULT_MODELS["primary"], [{"role": "user", "content": 'Reply with JSON {"ok": true}'}], json_mode=True,
             max_tokens=100)
    print(r["content"], r["usage"])
