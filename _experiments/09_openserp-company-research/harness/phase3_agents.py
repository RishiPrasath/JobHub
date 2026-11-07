"""Phase 3: persona sub-agents researching an employer through OpenSERP.

Each agent (one thread) does: write queries (LLM) -> search (OpenSERP) -> pick pages -> read pages (OpenSERP /extract)
-> write a cited company brief (LLM) -> verify every quote against its source text in code.
Search and page reads run in parallel across agents (the service rate-limits itself); LLM calls go through one
token-budgeted queue so the free-tier limit is respected.

Usage: python phase3_agents.py [persona_id ...]     (no arguments = all personas)
Writes /outputs/phase3/<persona_id>/ and /outputs/phase3/summary.json."""
import concurrent.futures as cf
import json, os, re, sys, threading, time, urllib.error, urllib.parse, urllib.request

BASE = os.environ.get("OPENSERP_URL", "http://openserp:7000")
GROQ_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_URL = (os.environ.get("GROQ_BASE_URL") or "https://api.groq.com/openai/v1").rstrip("/") + "/chat/completions"
MODEL = os.environ.get("GROQ_MODEL") or "openai/gpt-oss-120b"
TPM = int(os.environ.get("LLM_TPM_BUDGET", "6500"))          # tokens per minute we allow ourselves on the free tier
OUT = "/outputs/phase3"
ENGINES = "duckduckgo,bing"                                   # tried in order for each query (mode=any)
MAX_QUERIES, MAX_PAGES, PER_DOMAIN, PAGE_CHARS = 6, 8, 2, 3200

PERSONAS = [
    # id, who, company, role, what we know independently (never shown to the agent)
    {"id": "p1-software", "who": "software engineer", "company": "Grab Holdings", "role": "Backend Engineer", "truth": "real, well known"},
    {"id": "p2-nurse", "who": "registered nurse", "company": "Raffles Medical Group", "role": "Staff Nurse", "truth": "real, well known"},
    {"id": "p3-warehouse", "who": "warehouse and logistics worker", "company": "Ninja Van Singapore", "role": "Warehouse Associate", "truth": "real, well known"},
    {"id": "p4-marketing", "who": "marketing professional", "company": "Lazada Singapore", "role": "Digital Marketing Executive", "truth": "real, well known"},
    {"id": "p5-finance", "who": "finance and accounting professional", "company": "KPMG Singapore", "role": "Audit Associate", "truth": "real, well known"},
    {"id": "p6-obscure-real", "who": "customer service professional", "company": "Avanguarde Pte. Ltd.", "role": "Customer Service Executive", "truth": "real but tiny: live in the company registry, almost no web footprint"},
    {"id": "p7-fictitious", "who": "operations manager", "company": "Zzqxv Qwlmt Holdings Pte Ltd", "role": "Operations Manager", "truth": "fictitious: no such entity"},
    {"id": "p8-lookalike", "who": "customer service officer", "company": "DBS Bank Singapore Recruitment Pte Ltd", "role": "Customer Service Officer", "truth": "lookalike of a real bank: no such registered entity"},
]

BLOCK = re.compile(r"captcha|verify you are human|prove your humanity|not for bots|complete the challenge|access denied|just a moment|enable javascript|unusual traffic|sign in to continue|join now to see|log in to (see|continue)|checking your browser|are you a robot|403 forbidden", re.I)
DATA_URI = re.compile(r"\(data:[^)]{40,}\)")                   # inline images inflate length; a Reddit challenge page was 98% image data
GENERIC = {"pte", "ltd", "limited", "singapore", "holdings", "group", "the", "and", "of", "company", "inc", "llc", "bank"}


def name_tokens(company):
    return [w for w in re.findall(r"[a-z0-9]{3,}", company.lower()) if w not in GENERIC]
STATS = {"search_calls": 0, "search_ok": 0, "search_empty": 0, "search_fail": 0, "pages_tried": 0, "pages_ok": 0, "pages_thin": 0,
         "pages_blocked": 0, "pages_error": 0, "pages_irrelevant": 0, "llm_calls": 0, "llm_tokens": 0, "llm_429": 0}
stats_lock = threading.Lock()


def bump(**kw):
    with stats_lock:
        for k, v in kw.items():
            STATS[k] += v


# ---------------------------------------------------------------- LLM (token-budgeted, one at a time)
llm_lock = threading.Lock()
llm_window = []                                               # (time, tokens) used in the last 60 s


def llm(system, user, schema, name, max_tokens=2200):
    """One strict-JSON call. Waits for token budget, retries on 429 using the server's retry-after."""
    body = {"model": MODEL, "temperature": 0, "max_tokens": max_tokens, "reasoning_effort": "low",
            "response_format": {"type": "json_schema", "json_schema": {"name": name, "strict": True, "schema": schema}},
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
    est = int((len(system) + len(user)) / 3.2) + max_tokens // 2
    with llm_lock:
        for attempt in range(6):
            now = time.time()
            llm_window[:] = [(t, n) for t, n in llm_window if now - t < 60]
            used = sum(n for _, n in llm_window)
            if used + est > TPM and llm_window:
                time.sleep(max(1.0, 61 - (now - llm_window[0][0])))
                continue
            req = urllib.request.Request(GROQ_URL, json.dumps(body).encode(), {
                "Authorization": "Bearer " + GROQ_KEY, "Content-Type": "application/json", "User-Agent": "JobHubResearchExperiment/0.1"})
            try:
                d = json.load(urllib.request.urlopen(req, timeout=120))
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    bump(llm_429=1)
                    time.sleep(float(e.headers.get("retry-after", 20)) + 2)
                    continue
                raise RuntimeError("LLM HTTP %s: %s" % (e.code, e.read()[:200].decode("utf-8", "replace")))
            tokens = d.get("usage", {}).get("total_tokens", est)
            llm_window.append((time.time(), tokens))
            bump(llm_calls=1, llm_tokens=tokens)
            return json.loads(d["choices"][0]["message"]["content"]), tokens
    raise RuntimeError("LLM budget wait exceeded")


# ---------------------------------------------------------------- OpenSERP
def http_get(path, timeout=150):
    t = time.time()
    try:
        with urllib.request.urlopen(BASE + path, timeout=timeout) as r:
            return r.status, r.read(), time.time() - t
    except urllib.error.HTTPError as e:
        return e.code, e.read(), time.time() - t
    except Exception as e:
        return type(e).__name__, str(e).encode(), time.time() - t


def search(q):
    bump(search_calls=1)
    code, body, secs = http_get("/mega/search?" + urllib.parse.urlencode({"text": q, "mode": "any", "engines": ENGINES, "limit": 8}))
    rec = {"query": q, "http": code, "seconds": round(secs, 1), "results": [], "engines_failed": None, "error": None}
    try:
        j = json.loads(body)
    except Exception:
        rec["error"] = body[:200].decode("utf-8", "replace")
        bump(search_fail=1)
        return rec
    if code != 200:
        rec["error"] = {k: j.get(k) for k in ("error", "code", "message") if k in j} or str(j)[:200]
        bump(search_fail=1)
        return rec
    rec["engines_failed"] = j.get("meta", {}).get("engines_failed")
    rec["results"] = [{k: r.get(k) for k in ("rank", "type", "engine", "title", "url", "domain", "snippet")}
                      for r in j.get("results", []) if r.get("type") == "organic"]
    bump(**({"search_ok": 1} if rec["results"] else {"search_empty": 1}))
    return rec


def norm_url(u):
    p = urllib.parse.urlparse(u)
    return (p.netloc.lower().removeprefix("www.") + p.path.rstrip("/")).lower()


def read_page(url, tokens=()):
    bump(pages_tried=1)
    code, body, secs = http_get("/extract?" + urllib.parse.urlencode({"url": url, "mode": "auto"}), timeout=120)
    rec = {"url": url, "http": code, "seconds": round(secs, 1), "status": "error", "chars": 0, "text": "", "note": None}
    try:
        j = json.loads(body)
    except Exception:
        rec["note"] = body[:160].decode("utf-8", "replace")
        bump(pages_error=1)
        return rec
    if code != 200:
        msg = str(j.get("message") or j.get("error") or j)[:160]
        rec["note"] = msg
        rec["status"] = "blocked" if re.search(r"blocked|rate limited|HTTP 40[13]|HTTP 429", msg, re.I) else "error"
        bump(**{"pages_blocked" if rec["status"] == "blocked" else "pages_error": 1})
        return rec
    md = DATA_URI.sub("(data:…)", (j.get("markdown") or j.get("text") or "")).strip()
    title = (j.get("title") or "")[:120]
    rec.update(title=title, chars=len(md), mode_used=(j.get("meta") or {}).get("mode_used"))
    if (BLOCK.search(md[:800]) or BLOCK.search(title)) and len(md) < 2500:
        rec.update(status="blocked", note="challenge or login-wall text (title: %s)" % title[:60])
        bump(pages_blocked=1)
    elif len(md) < 400:
        rec.update(status="thin", note="fewer than 400 characters of real content came back")
        bump(pages_thin=1)
    elif tokens and not any(t in md.lower() for t in tokens):
        rec.update(status="irrelevant", note="the page never mentions the company name (%s)" % ", ".join(tokens))
        bump(pages_irrelevant=1)
    else:
        rec.update(status="ok", text=md)
        bump(pages_ok=1)
    return rec


# ---------------------------------------------------------------- agent
Q_SCHEMA = {"type": "object", "additionalProperties": False, "required": ["queries"],
            "properties": {"queries": {"type": "array", "items": {"type": "string"}}}}
EVIDENCE = {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["source", "quote"],
            "properties": {"source": {"type": "integer"}, "quote": {"type": "string"}}}}
CLAIM = {"type": "object", "additionalProperties": False, "required": ["claim", "evidence"],
         "properties": {"claim": {"type": "string"}, "evidence": EVIDENCE}}
B_SCHEMA = {"type": "object", "additionalProperties": False,
            "required": ["validity_status", "validity_reasoning", "key_facts", "positive_signals", "red_flags",
                         "relevance_for_persona", "confidence", "confidence_reasoning", "could_not_verify"],
            "properties": {
                "validity_status": {"type": "string", "enum": ["appears_real_and_consistent", "appears_real_limited_evidence", "cannot_verify", "inconsistent_or_suspicious"]},
                "validity_reasoning": {"type": "string"},
                "key_facts": {"type": "array", "items": CLAIM}, "positive_signals": {"type": "array", "items": CLAIM},
                "red_flags": {"type": "array", "items": CLAIM}, "relevance_for_persona": {"type": "string"},
                "confidence": {"type": "string", "enum": ["low", "medium", "high"]}, "confidence_reasoning": {"type": "string"},
                "could_not_verify": {"type": "array", "items": {"type": "string"}}}}


def squash(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s or "").lower()).strip()


def verify(claims, sources):
    """A claim is 'verified' only if at least one of its quotes appears in the cited source's text."""
    out = []
    for c in claims:
        ev = []
        for e in c["evidence"]:
            src = sources.get(e["source"])
            ok = bool(src) and len(squash(e["quote"])) >= 12 and squash(e["quote"]) in squash(src["text"])
            ev.append({**e, "url": src["url"] if src else None, "quote_found_in_source": ok})
        out.append({"claim": c["claim"], "evidence": ev, "status": "verified" if any(x["quote_found_in_source"] for x in ev) else "unverified"})
    return out


def run_agent(p):
    t0 = time.time()
    d = f"{OUT}/{p['id']}"
    os.makedirs(d + "/pages", exist_ok=True)
    log = []

    def note(msg):
        log.append(f"[{time.time()-t0:6.1f}s] {msg}")
        print(f"{p['id']:16} {msg}", flush=True)

    res = {"persona": p["id"], "who": p["who"], "company": p["company"], "role": p["role"], "truth_note": p["truth"], "stages": {}}
    try:
        # 1. the agent writes its own queries
        qj, _ = llm("You research employers for a job seeker. Reply with JSON only.",
                    f"Persona: {p['who']} considering the role '{p['role']}' at '{p['company']}' in Singapore.\n"
                    f"Write {MAX_QUERIES} different web search queries that would reveal whether the company is real and what working there is like: "
                    "cover employee reviews, layoffs or restructuring, scam or fraud reports, interview process, salary, lawsuits or regulatory news. "
                    "Every query must contain the company name. Keep each under 12 words.", Q_SCHEMA, "queries", 400)
        queries = [q.strip() for q in qj["queries"] if q.strip()][:MAX_QUERIES]
        note(f"{len(queries)} queries written")
        # 2. search (the service rate-limits; queries are sent one after another per agent)
        searches = []
        for q in queries:
            s = search(q)
            searches.append(s)
            note(f"search {s['http']} {len(s['results'])} organic in {s['seconds']}s via {sorted({r['engine'] for r in s['results']})} :: {q[:50]}")
        json.dump(searches, open(d + "/search_results.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        # 3. choose pages: most often returned, at most PER_DOMAIN per domain
        seen, order = {}, []
        for s in searches:
            for r in s["results"]:
                k = norm_url(r["url"] or "")
                if not k:
                    continue
                if k not in seen:
                    seen[k] = {**r, "hits": 0}
                    order.append(k)
                seen[k]["hits"] += 1
        ranked = sorted(order, key=lambda k: (-seen[k]["hits"], order.index(k)))
        chosen, per = [], {}
        for k in ranked:
            dom = seen[k]["domain"] or k.split("/")[0]
            if per.get(dom, 0) < PER_DOMAIN and len(chosen) < MAX_PAGES:
                chosen.append(seen[k])
                per[dom] = per.get(dom, 0) + 1
        note(f"{len(order)} unique organic URLs, reading {len(chosen)}")
        # 4. read pages
        pages = []
        for r in chosen:
            pg = read_page(r["url"], name_tokens(p["company"]))
            pg.update(search_title=r["title"], snippet=r["snippet"], engine=r["engine"])
            pages.append(pg)
            note(f"page {pg['status']:7} {pg['chars']:6} chars {pg['seconds']:5.1f}s {r['url'][:70]}")
            if pg["text"]:
                open(f"{d}/pages/{len(pages):02d}_{(r['domain'] or 'x')[:30]}.md", "w", encoding="utf-8").write(pg["text"])
            time.sleep(1.5)
        json.dump([{k: v for k, v in x.items() if k != "text"} for x in pages], open(d + "/pages_log.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        # 5. numbered sources: page text where it was read, otherwise only the search snippet (flagged)
        sources, blocks, failed = {}, [], []
        for i, pg in enumerate(pages, 1):
            if pg["status"] == "ok":
                txt = pg["text"][:PAGE_CHARS]
                sources[i] = {"url": pg["url"], "text": txt, "kind": "page"}
                blocks.append(f"[{i}] PAGE {pg['url']}\n{txt}")
            else:
                failed.append({"url": pg["url"], "status": pg["status"], "note": pg["note"]})
                if pg.get("snippet"):
                    sources[i] = {"url": pg["url"], "text": pg["snippet"], "kind": "snippet_only"}
                    blocks.append(f"[{i}] SEARCH SNIPPET ONLY (page could not be read: {pg['status']}) {pg['url']}\n{pg['snippet']}")
        for j, s in enumerate(searches):                    # snippets of results we did not open still carry information
            pass
        # 6. the brief
        sysmsg = ("You are a careful analyst writing a company brief for a job seeker. Use ONLY the numbered sources. "
                  "Every claim needs evidence: the source number and a SHORT verbatim quote (8 to 25 words) copied exactly from that source. "
                  "Do not state anything you cannot quote. If sources are thin, say so and choose a cautious validity status: "
                  "'cannot_verify' when no source clearly describes this specific company; 'appears_real_limited_evidence' when only a few sources do; "
                  "'inconsistent_or_suspicious' when sources conflict or describe a different or lookalike entity; 'appears_real_and_consistent' only when several independent sources agree. "
                  "A search result about a similarly named but different company is NOT evidence about this one. List what you could not verify.")
        user = (f"Persona: {p['who']}. Role considered: {p['role']}. Company named in the job posting: {p['company']} (Singapore).\n\n"
                + ("\n\n".join(blocks) if blocks else "(no sources could be read)"))
        brief, tok = llm(sysmsg, user, B_SCHEMA, "company_brief", 2600)
        for k in ("key_facts", "positive_signals", "red_flags"):
            brief[k] = verify(brief[k], sources)
        brief["sources_used"] = [{"id": i, "url": s["url"], "kind": s["kind"]} for i, s in sources.items()]
        brief["sources_failed_or_blocked"] = failed
        brief["claims_verified"] = sum(1 for k in ("key_facts", "positive_signals", "red_flags") for c in brief[k] if c["status"] == "verified")
        brief["claims_unverified"] = sum(1 for k in ("key_facts", "positive_signals", "red_flags") for c in brief[k] if c["status"] == "unverified")
        json.dump(brief, open(d + "/brief.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        res.update(ok=True, validity=brief["validity_status"], confidence=brief["confidence"],
                   claims_verified=brief["claims_verified"], claims_unverified=brief["claims_unverified"],
                   queries=len(queries), searches_ok=sum(1 for s in searches if s["results"]), unique_urls=len(order),
                   pages_tried=len(pages), pages_ok=sum(1 for x in pages if x["status"] == "ok"),
                   pages_failed=len(failed), llm_tokens_brief=tok)
        note(f"brief: {brief['validity_status']} / {brief['confidence']} ; claims verified {brief['claims_verified']}, unverified {brief['claims_unverified']}")
    except Exception as e:
        res.update(ok=False, error=f"{type(e).__name__}: {str(e)[:300]}")
        note("FAILED " + res["error"])
    res["seconds"] = round(time.time() - t0, 1)
    open(d + "/log.txt", "w", encoding="utf-8").write("\n".join(log))
    json.dump(res, open(d + "/result.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    want = set(sys.argv[1:])
    todo = [p for p in PERSONAS if not want or p["id"] in want]
    os.makedirs(OUT, exist_ok=True)
    if not GROQ_KEY:
        sys.exit("GROQ_API_KEY is not set (put it in the repo-root .env)")
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=len(todo)) as ex:
        results = list(ex.map(run_agent, todo))
    summary = {"model": MODEL, "wall_seconds": round(time.time() - t0, 1), "totals": STATS, "agents": results}
    json.dump(summary, open(f"{OUT}/summary.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps({"wall_seconds": summary["wall_seconds"], "totals": STATS}, indent=1))
