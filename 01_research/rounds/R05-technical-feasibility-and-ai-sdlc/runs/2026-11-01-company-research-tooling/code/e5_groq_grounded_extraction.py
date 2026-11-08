"""E5: Groq gpt-oss-120b, naive quotes (A) vs numbered-excerpt citations with code-side quote verification (B)."""
import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path
RUN = Path(__file__).resolve().parents[1]
ROOT = RUN.parents[4]
for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip())
MODEL = "openai/gpt-oss-120b"
URL = os.environ["GROQ_BASE_URL"].rstrip("/") + "/chat/completions"
QUESTIONS = {
 "what_company_does": "What does the organisation do, sell or provide?",
 "markets_locations": "Which markets, customers or locations does it say it serves?",
 "employer_type": "Is it a direct employer or a recruitment/staffing agency? (answer one of: direct_employer, recruitment_agency, not_stated)",
 "hiring_information": "Does the page give careers, hiring or application information?",
 "contact_or_address": "Does the page state a contact route or physical address?",
}
def norm(s): return re.sub(r"\W+", " ", s.lower()).strip()
def excerpts(text, cap=6000):
    parts, total = [], 0
    for ln in re.split(r"\n+|(?<=[.!?])\s+", text):
        ln = ln.strip()
        if len(ln) < 25: continue
        if total + len(ln) > cap: break
        parts.append(ln[:400]); total += len(ln)
    return parts
def schema(cited):
    ans = {"type": "object", "additionalProperties": False, "required": ["answer", "status", "quote"] + (["excerpt_id"] if cited else []),
           "properties": {"answer": {"type": "string"}, "status": {"type": "string", "enum": ["supported", "not_found"]}, "quote": {"type": "string"}}}
    if cited: ans["properties"]["excerpt_id"] = {"type": "integer"}
    return {"type": "json_schema", "json_schema": {"name": "research", "strict": True, "schema": {
        "type": "object", "additionalProperties": False, "required": list(QUESTIONS), "properties": {k: ans for k in QUESTIONS}}}}
def call(messages, cited):
    body = {"model": MODEL, "messages": messages, "temperature": 0, "max_tokens": 2500, "reasoning_effort": "low", "response_format": schema(cited)}
    for attempt in range(6):
        t0 = time.time()
        req = urllib.request.Request(URL, json.dumps(body).encode(), {"Authorization": "Bearer " + os.environ["GROQ_API_KEY"], "Content-Type": "application/json", "User-Agent": "JobHub-research/0.1"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                d = json.load(r); return d, round(time.time() - t0, 1)
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:300]
            if e.code == 429:
                wait = float(e.headers.get("retry-after", 20)) + 2; print("   429, wait", wait, flush=True); time.sleep(wait); continue
            return {"error": f"{e.code} {msg}"}, round(time.time() - t0, 1)
    return {"error": "gave_up_429"}, 0
def run():
    pages = sorted((RUN / "outputs/pages").glob("P*_plain.txt"))
    out = []
    qtext = "\n".join(f"- {k}: {v}" for k, v in QUESTIONS.items())
    for pf in pages:
        pid = pf.name[:3]; text = pf.read_text(encoding="utf-8"); ex = excerpts(text); page_n = norm(" ".join(ex))
        for mode in ("A_naive", "B_cited"):
            cited = mode == "B_cited"
            if cited:
                body = "\n".join(f"[{i}] {e}" for i, e in enumerate(ex, 1))
                sys_p = "Answer using ONLY the numbered excerpts. For each question give a short answer, the excerpt_id, and a verbatim quote copied from that excerpt. If the excerpts do not answer it, status=not_found, excerpt_id=0, quote=''. Never use outside knowledge."
            else:
                body = "\n".join(ex)
                sys_p = "Answer using ONLY the page text. For each question give a short answer and a verbatim supporting quote. If the page text does not answer it, status=not_found and quote=''. Never use outside knowledge."
            d, secs = call([{"role": "system", "content": sys_p}, {"role": "user", "content": f"Questions:\n{qtext}\n\nPAGE TEXT:\n{body}"}], cited)
            rec = {"id": pid, "mode": mode, "seconds": secs, "excerpts": len(ex)}
            if "error" in d: rec["error"] = d["error"]
            else:
                rec["usage"] = d.get("usage", {}).get("total_tokens")
                try:
                    j = json.loads(d["choices"][0]["message"]["content"]); rec["valid_json"] = True; rec["answers"] = {}
                    for k, a in j.items():
                        q = norm(a.get("quote", "")); sup = a["status"] == "supported"
                        quote_ok = bool(q) and q in page_n
                        if cited and quote_ok:
                            eid = a.get("excerpt_id", 0); quote_ok = 1 <= eid <= len(ex) and q in norm(ex[eid - 1])
                        rec["answers"][k] = {"status": a["status"], "answer": a["answer"][:160], "quote": a.get("quote", "")[:160], "quote_verified": quote_ok if sup else None}
                except Exception as e:
                    rec["valid_json"] = False; rec["parse_error"] = str(e)[:100]
            out.append(rec); print(pid, mode, secs, rec.get("usage"), {k: v["quote_verified"] for k, v in rec.get("answers", {}).items()}, rec.get("error", ""), flush=True)
            (RUN / "outputs/e5_groq_extraction.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
            time.sleep(8)
run()
