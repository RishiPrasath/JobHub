"""Evidence-first HTTP Company Research Service.

This is deliberately a small experiment, not a production crawler. It resolves a
company through the registry service, discovers public source pages through the
local SearXNG instance, and records what could and could not be retrieved.

It does not log in, bypass challenges, follow arbitrary user URLs, infer an
employer score, or ask an LLM to fill gaps in the evidence.
"""
import ipaddress
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import pagefetch, websearch


PORT = int(os.environ.get("COMPANY_RESEARCH_PORT", "8091"))
REGISTRY_URL = os.environ.get("JOBHUB_REGISTRY_URL", "http://registry:8090").rstrip("/")
SEARCH_URL = os.environ.get("SEARXNG_URL", "http://searxng:8080").rstrip("/")
REGISTRY_TIMEOUT_SECONDS = float(os.environ.get("COMPANY_RESEARCH_REGISTRY_TIMEOUT_SECONDS", "8"))
SEARCH_TIMEOUT_SECONDS = float(os.environ.get("COMPANY_RESEARCH_SEARCH_TIMEOUT_SECONDS", "8"))
MAX_BODY_BYTES = int(os.environ.get("COMPANY_RESEARCH_MAX_BODY_BYTES", "300000"))
MAX_NAME_CHARS = 200
MAX_JOB_TITLE_CHARS = 200
MAX_JOB_TEXT_CHARS = 50000
MAX_JOB_URL_CHARS = 1000
MAX_QUERIES = int(os.environ.get("COMPANY_RESEARCH_MAX_QUERIES", "6"))
MAX_RESULTS_PER_QUERY = int(os.environ.get("COMPANY_RESEARCH_MAX_RESULTS", "5"))
MAX_FETCHES = int(os.environ.get("COMPANY_RESEARCH_MAX_FETCHES", "10"))
MAX_UNAVAILABLE_BEFORE_BREAKER = int(os.environ.get("COMPANY_RESEARCH_MAX_UNAVAILABLE", "2"))
USER_AGENT = "JobHubCompanyResearch/0.1 (evidence experiment)"

_EMAIL = re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b")
_PHONE = re.compile(r"(?<!\d)(?:\+?65[\s-]?)?[689]\d{3}[\s-]?\d{4}(?!\d)")
_LONG_HANDLE = re.compile(r"(?<!\w)u/[A-Za-z0-9_-]{3,}(?!\w)")

SOURCE_DOMAINS = (
    ("glassdoor", ("glassdoor.",)),
    ("indeed", ("indeed.",)),
    ("jobstreet", ("jobstreet.",)),
    ("blind", ("teamblind.com",)),
    ("fishbowl", ("fishbowlapp.com",)),
    ("comparably", ("comparably.com",)),
    ("reddit", ("reddit.com",)),
    ("mycareersfuture", ("mycareersfuture.gov.sg",)),
    ("official_or_other", ()),
)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def redact(value):
    """Reduce accidental PII retention in previews and logs."""
    value = _EMAIL.sub("[email redacted]", value or "")
    value = _PHONE.sub("[phone redacted]", value)
    value = _LONG_HANDLE.sub("[handle redacted]", value)
    return value


def source_class(url):
    host = urllib.parse.urlparse(url).netloc.lower().removeprefix("www.")
    for name, domains in SOURCE_DOMAINS:
        if any(domain in host for domain in domains):
            return name
    return "official_or_other"


def _public_http_url(url):
    try:
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            return False
        host = parsed.hostname.lower().rstrip(".")
        if host in ("localhost", "0.0.0.0", "::1") or host.endswith(".local"):
            return False
        try:
            address = ipaddress.ip_address(host)
            if address.is_private or address.is_loopback or address.is_link_local:
                return False
        except ValueError:
            pass
        return True
    except ValueError:
        return False


def query_plan(company_name, job_title=None):
    name = company_name.strip().replace('"', "")
    title = (job_title or "").strip().replace('"', "")
    queries = [
        (f'"{name}" Glassdoor reviews Singapore', "structured employer reviews"),
        (f'"{name}" Indeed reviews Singapore', "structured employer reviews"),
        (f'"{name}" JobStreet reviews Singapore', "local employer reviews"),
        (f'"{name}" workplace culture workload management Singapore', "lived experience"),
        (f'"{name}" layoffs interview experience Singapore', "job security and candidate experience"),
    ]
    if title:
        queries.append((f'"{name}" "{title}" employee experience Singapore', "role-relevant experience"))
    return [{"query": q, "purpose": purpose} for q, purpose in queries[:MAX_QUERIES]]


def _get_json(url, timeout=10):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.status, json.load(response)


def registry_lookup(company_name, uen=None, job_url=None):
    params = {"name": company_name}
    if uen:
        params["uen"] = uen
    url = REGISTRY_URL + "/resolve?" + urllib.parse.urlencode(params)
    try:
        status, body = _get_json(url, timeout=REGISTRY_TIMEOUT_SECONDS)
        return {"status": "ok" if status == 200 else "unavailable", "url": url, "response": body}
    except urllib.error.HTTPError as exc:
        return {"status": "unavailable", "url": url, "http_status": exc.code, "note": "registry returned an error"}
    except Exception as exc:
        return {"status": "unavailable", "url": url, "note": type(exc).__name__}


def _search_one(item):
    """Use SearXNG directly; do not silently fall back to an unsanctioned engine."""
    old = os.environ.get("SEARXNG_URL")
    os.environ["SEARXNG_URL"] = SEARCH_URL
    try:
        old_timeout = os.environ.get("SEARXNG_TIMEOUT_SECONDS")
        os.environ["SEARXNG_TIMEOUT_SECONDS"] = str(SEARCH_TIMEOUT_SECONDS)
        try:
            return websearch.searxng(item["query"], max_results=MAX_RESULTS_PER_QUERY)
        finally:
            if old_timeout is None:
                os.environ.pop("SEARXNG_TIMEOUT_SECONDS", None)
            else:
                os.environ["SEARXNG_TIMEOUT_SECONDS"] = old_timeout
    finally:
        if old is None:
            os.environ.pop("SEARXNG_URL", None)
        else:
            os.environ["SEARXNG_URL"] = old


def discover(plan):
    results = []
    queries = []
    seen = set()
    unavailable_count = 0
    for item in plan:
        if unavailable_count >= MAX_UNAVAILABLE_BEFORE_BREAKER:
            queries.append({
                "query": item["query"],
                "purpose": item["purpose"],
                "source": "searxng_local",
                "status": "skipped_after_dependency_failure",
                "note": "search dependency circuit breaker opened",
                "result_count": 0,
            })
            continue
        found = _search_one(item)
        if found.get("status") in ("unavailable", "failed"):
            unavailable_count += 1
        else:
            unavailable_count = 0
        queries.append({
            "query": item["query"],
            "purpose": item["purpose"],
            "source": found.get("source"),
            "status": found.get("status"),
            "note": found.get("note"),
            "result_count": len(found.get("results", [])),
        })
        for rank, result in enumerate(found.get("results", []), 1):
            url = result.get("url", "")
            if not _public_http_url(url) or url in seen:
                continue
            seen.add(url)
            results.append({
                "url": url,
                "title": redact((result.get("title") or "")[:300]),
                "snippet": redact((result.get("description") or "")[:1200]),
                "source_class": source_class(url),
                "evidence_kind": "search_lead",
                "query": item["query"],
                "rank": rank,
                "retrieval_status": "not_fetched",
            })
    return queries, results


def fetch_leads(leads):
    fetched = []
    for lead in leads[:MAX_FETCHES]:
        record = dict(lead)
        try:
            page = pagefetch.fetch(lead["url"])
            record["retrieval_status"] = page.get("status", "unknown")
            record["retrieved_at"] = page.get("fetched_at")
            record["robots"] = page.get("robots")
            record["http_status"] = page.get("http")
            record["page_title"] = redact(page.get("title", ""))
            text = redact(page.get("text", ""))
            if text:
                record["content_preview"] = text[:1600]
                record["evidence_kind"] = "retrieved_page"
            if page.get("status") in ("blocked_by_robots",) or str(page.get("status", "")).startswith("blocked_or_failed"):
                record["note"] = "The page could not be retrieved; this is not evidence that the source has no information."
        except Exception as exc:
            record["retrieval_status"] = "failed"
            record["note"] = type(exc).__name__
        fetched.append(record)
    for lead in leads[MAX_FETCHES:]:
        fetched.append({**lead, "retrieval_status": "not_fetched_due_to_bound"})
    return fetched


def validate_request(payload):
    if not isinstance(payload, dict):
        raise ValueError("JSON body must be an object")
    name = str(payload.get("company_name", "")).strip()
    if not name:
        raise ValueError("company_name is required")
    if len(name) > MAX_NAME_CHARS:
        raise ValueError(f"company_name longer than {MAX_NAME_CHARS} characters")
    title = str(payload.get("job_title", "")).strip()
    job_url = str(payload.get("job_url", "")).strip()
    job_text = str(payload.get("job_text", ""))
    if len(title) > MAX_JOB_TITLE_CHARS:
        raise ValueError(f"job_title longer than {MAX_JOB_TITLE_CHARS} characters")
    if len(job_url) > MAX_JOB_URL_CHARS:
        raise ValueError(f"job_url longer than {MAX_JOB_URL_CHARS} characters")
    if job_url:
        parsed_url = urllib.parse.urlparse(job_url)
        if parsed_url.username or parsed_url.password:
            raise ValueError("job_url must not contain credentials")
        if not _public_http_url(job_url):
            raise ValueError("job_url must be a public http or https URL")
    if len(job_text) > MAX_JOB_TEXT_CHARS:
        raise ValueError(f"job_text longer than {MAX_JOB_TEXT_CHARS} characters")
    uen = str(payload.get("uen", "")).strip()
    if len(uen) > 20:
        raise ValueError("uen longer than 20 characters")
    return {"company_name": name, "uen": uen or None, "job_title": title or None,
            "job_url": job_url or None, "job_text": redact(job_text)[:MAX_JOB_TEXT_CHARS] or None}


def run_research(payload):
    request = validate_request(payload)
    identity = registry_lookup(request["company_name"], request["uen"])
    legal_name = request["company_name"]
    if identity.get("status") == "ok":
        chosen = (identity.get("response") or {}).get("chosen") or {}
        legal_name = chosen.get("name") or legal_name
    plan = query_plan(legal_name, request["job_title"])
    query_log, leads = discover(plan)
    evidence = fetch_leads(leads)
    statuses = {}
    for item in evidence:
        statuses[item["source_class"]] = statuses.get(item["source_class"], 0) + 1
    return {
        "service": "company-research-service",
        "experiment_version": "0.1",
        "retrieved_at": now(),
        "request": request,
        "identity": identity,
        "source_discovery": {
            "query_plan": plan,
            "queries": query_log,
            "evidence": evidence,
            "source_counts": statuses,
        },
        "interpretation": {
            "claims": [],
            "scores": [],
            "note": "This experiment returns source-linked evidence and retrieval limits. It does not infer an employer score or decide whether the user should apply.",
        },
        "limitations": [
            "Search snippets are leads, not verified facts.",
            "Review pages may be blocked, login-gated, incomplete, stale, or unrelated to the requested role.",
            "No automatic login, CAPTCHA solving, challenge bypass, or arbitrary user-URL fetching was attempted.",
        ],
    }


def _send(handler, status, body):
    raw = json.dumps(body, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(raw)))
    handler.end_headers()
    handler.wfile.write(raw)


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/health":
            return _send(self, 200, {"ok": True, "service": "company-research-service", "registry_url": REGISTRY_URL, "search_url": SEARCH_URL})
        if parsed.path == "/":
            return _send(self, 200, {"service": "company-research-service", "version": "0.1", "endpoints": {"POST /research": "run an evidence collection experiment", "GET /health": "service health"}})
        return _send(self, 404, {"error": "not found"})

    def do_POST(self):
        if urllib.parse.urlparse(self.path).path != "/research":
            return _send(self, 404, {"error": "not found"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_BODY_BYTES:
                return _send(self, 413, {"error": f"request body must be between 1 and {MAX_BODY_BYTES} bytes"})
            raw = self.rfile.read(length)
            payload = json.loads(raw.decode("utf-8"))
            return _send(self, 200, run_research(payload))
        except ValueError as exc:
            return _send(self, 400, {"error": str(exc)})
        except json.JSONDecodeError:
            return _send(self, 400, {"error": "request body must be valid JSON"})
        except Exception as exc:
            return _send(self, 500, {"error": "research failed", "type": type(exc).__name__})

    def do_PUT(self):
        return _send(self, 405, {"error": "method not allowed"})

    do_DELETE = do_PATCH = do_PUT

    def log_message(self, *_):
        pass


def serve(port=PORT):
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"company research service on :{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    serve()
