"""Groq structured extraction: the model cites a numbered excerpt, code rejects any quote not found in it."""
import json, os, re, time, urllib.error, urllib.request

MODEL = os.environ.get("GROQ_MODEL") or "openai/gpt-oss-120b"
QUESTIONS = {
    "what_company_does": "What does the organisation do, sell or provide?",
    "markets_locations": "Which markets, customers or locations does it say it serves?",
    "employer_type": "Is it a direct employer or a recruitment/staffing agency? (direct_employer, recruitment_agency, not_stated)",
    "hiring_information": "Does the page give careers, hiring or application information?",
    "contact_or_address": "Does the page state a contact route or physical address?",
}


def _norm(s):
    return re.sub(r"\W+", " ", s.lower()).strip()


def excerpts(text, cap=6000):
    out, total = [], 0
    for ln in re.split(r"\n+|(?<=[.!?])\s+", text):
        ln = ln.strip()
        if len(ln) < 25:
            continue
        if total + len(ln) > cap:
            break
        out.append(ln[:400])
        total += len(ln)
    return out


def _schema():
    a = {"type": "object", "additionalProperties": False, "required": ["answer", "status", "excerpt_id", "quote"],
         "properties": {"answer": {"type": "string"}, "status": {"type": "string", "enum": ["supported", "not_found"]},
                        "excerpt_id": {"type": "integer"}, "quote": {"type": "string"}}}
    return {"type": "json_schema", "json_schema": {"name": "research", "strict": True, "schema": {
        "type": "object", "additionalProperties": False, "required": list(QUESTIONS), "properties": {k: a for k in QUESTIONS}}}}


def extract(text, api_key=None, base_url=None):
    api_key = api_key or os.environ["GROQ_API_KEY"]
    url = (base_url or os.environ.get("GROQ_BASE_URL") or "https://api.groq.com/openai/v1").rstrip("/") + "/chat/completions"
    ex = excerpts(text)
    system = ("Answer using ONLY the numbered excerpts. For each question give a short answer, the excerpt_id, and a verbatim quote "
              "copied from that excerpt. If the excerpts do not answer it: status=not_found, excerpt_id=0, quote=''. Never use outside knowledge.")
    user = ("Questions:\n" + "\n".join("- %s: %s" % kv for kv in QUESTIONS.items())
            + "\n\nEXCERPTS:\n" + "\n".join("[%d] %s" % (i, e) for i, e in enumerate(ex, 1)))
    body = {"model": MODEL, "temperature": 0, "max_tokens": 2500, "reasoning_effort": "low", "response_format": _schema(),
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
    for _ in range(5):
        req = urllib.request.Request(url, json.dumps(body).encode(), {
            "Authorization": "Bearer " + api_key, "Content-Type": "application/json", "User-Agent": "JobHubResearchBot/0.1"})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=90))
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(float(e.headers.get("retry-after", 20)) + 2)
                continue
            return {"error": str(e.code)}
    else:
        return {"error": "rate_limited"}
    j = json.loads(d["choices"][0]["message"]["content"])
    answers = {}
    for k, a in j.items():
        status, why = a["status"], None
        if status == "supported":
            eid, q = a.get("excerpt_id", 0), _norm(a.get("quote", ""))
            if not (1 <= eid <= len(ex)) or not q or q not in _norm(ex[eid - 1]):
                status, why = "rejected_unverified_quote", "quote not found in cited excerpt"
        answers[k] = {"status": status, "answer": a["answer"] if status == "supported" else "",
                      "excerpt_id": a.get("excerpt_id"), "quote": a.get("quote", ""), "why": why}
    return {"excerpts": len(ex), "tokens": d.get("usage", {}).get("total_tokens"), "answers": answers}
