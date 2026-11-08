"""Cited company brief from numbered sources, with every quote checked against its source in code."""
import json
import threading
import time
import urllib.error
import urllib.request

from . import config
from .gate import squash

MAX_WAIT_SECONDS = 90          # total time one brief may spend waiting on the model service; longer fails into 'summary unavailable'
_lock = threading.Lock()
_window = []                                   # (time, tokens) in the last 60 s, to stay under the free-tier tokens-per-minute limit

EVIDENCE = {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["source", "quote"],
                                        "properties": {"source": {"type": "integer"}, "quote": {"type": "string"}}}}
CLAIM = {"type": "object", "additionalProperties": False, "required": ["claim", "evidence"],
         "properties": {"claim": {"type": "string"}, "evidence": EVIDENCE}}
SCHEMA = {"type": "object", "additionalProperties": False,
          "required": ["validity_status", "validity_reasoning", "key_facts", "positive_signals", "red_flags", "confidence", "could_not_verify"],
          "properties": {
              "validity_status": {"type": "string", "enum": ["appears_real_and_consistent", "appears_real_limited_evidence", "cannot_verify", "inconsistent_or_suspicious"]},
              "validity_reasoning": {"type": "string"},
              "key_facts": {"type": "array", "items": CLAIM}, "positive_signals": {"type": "array", "items": CLAIM},
              "red_flags": {"type": "array", "items": CLAIM},
              "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
              "could_not_verify": {"type": "array", "items": {"type": "string"}}}}

SYSTEM = ("You are a careful analyst writing a company brief for a job seeker. Use ONLY the numbered sources. "
          "Source 0, when present, is the official company registry record. "
          "Every claim needs evidence: the source number and a SHORT verbatim quote (8 to 25 words) copied exactly from that source. "
          "Do not state anything you cannot quote. A source about a similarly named but different company is NOT evidence about this one. "
          "Choose a cautious validity status: 'cannot_verify' when no source clearly describes this specific company; "
          "'appears_real_limited_evidence' when only a few do; 'inconsistent_or_suspicious' when sources conflict or describe a different or lookalike entity; "
          "'appears_real_and_consistent' only when several independent sources agree. List what you could not verify.")


def _llm(system, user, max_tokens=2600):
    body = {"model": config.MODEL, "temperature": 0, "max_tokens": max_tokens, "reasoning_effort": "low",
            "response_format": {"type": "json_schema", "json_schema": {"name": "company_brief", "strict": True, "schema": SCHEMA}},
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
    est = int((len(system) + len(user)) / 3.2) + max_tokens // 2
    started = time.time()
    with _lock:
        for _ in range(6):
            now = time.time()
            if now - started > MAX_WAIT_SECONDS:
                raise RuntimeError("model service busy: waited %d s" % MAX_WAIT_SECONDS)
            _window[:] = [(t, n) for t, n in _window if now - t < 60]
            if _window and sum(n for _, n in _window) + est > config.LLM_TPM:
                time.sleep(max(1.0, 61 - (now - _window[0][0])))
                continue
            req = urllib.request.Request(config.GROQ_URL, json.dumps(body).encode(), {
                "Authorization": "Bearer " + config.GROQ_KEY, "Content-Type": "application/json", "User-Agent": "JobHubCompanyResearch/0.1"})
            try:
                d = json.load(urllib.request.urlopen(req, timeout=120))
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    wait = float(e.headers.get("retry-after", 20)) + 2
                    if time.time() - started + wait > MAX_WAIT_SECONDS:      # a daily limit asks for minutes or hours: fail fast, do not hang
                        raise RuntimeError("model rate limit reached (retry in %d s)" % wait)
                    time.sleep(wait)
                    continue
                raise RuntimeError("model service HTTP %s" % e.code)
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                raise RuntimeError("model service unreachable: %s" % type(e).__name__)
            _window.append((time.time(), d.get("usage", {}).get("total_tokens", est)))
            return json.loads(d["choices"][0]["message"]["content"]), d.get("usage", {}).get("total_tokens")
    raise RuntimeError("model token budget wait exceeded")


def verify(claims, sources):
    """A claim is 'verified' only if one of its quotes appears in the cited source's text."""
    out = []
    for c in claims:
        ev = []
        for e in c["evidence"]:
            s = sources.get(e["source"])
            found = bool(s) and len(squash(e["quote"])) >= 12 and squash(e["quote"]) in squash(s["text"])
            ev.append({"source": e["source"], "url": s["url"] if s else None, "quote": e["quote"], "quote_found_in_source": found})
        out.append({"claim": c["claim"], "evidence": ev, "status": "verified" if any(x["quote_found_in_source"] for x in ev) else "unverified"})
    return out


def write(sources, header, posture=None):
    """sources: {id: {'url','text','kind'}}. Returns (brief dict with verified claims, tokens). Raises RuntimeError on model failure."""
    blocks = []
    for i, s in sources.items():
        label = {"registry": "OFFICIAL REGISTRY RECORD", "page": "PAGE", "snippet_only": "SEARCH SNIPPET ONLY (page not read)"}[s["kind"]]
        blocks.append("[%d] %s %s\n%s" % (i, label, s["url"], s["text"]))
    user = header + "\n\n" + ("\n\n".join(blocks) if blocks else "(no sources)")
    system = SYSTEM + (" " + posture if posture else "")
    brief, tokens = _llm(system, user)
    for k in ("key_facts", "positive_signals", "red_flags"):
        brief[k] = verify(brief[k], sources)
    return brief, tokens
