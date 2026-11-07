"""HTTP API. Research takes minutes (the search service is rate-limited), so it is a job: POST starts one, GET polls it.

    POST /research   {"employer", "role"?, "uen"?, "url"?}  -> 202 {"id"} ; a finished identical request in the last hour is returned as 200
    GET  /research/<id>   -> {"state": queued|running|done|failed, "result"?, "text"?}
    GET  /health          -> 200
    GET  /status          -> reachability of the registry, search and reader services, job counts
"""
import json
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from . import config, orchestrator
from .http import Unavailable, call
from .render import render_text

_jobs, _cache = {}, {}
_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=config.JOB_WORKERS)


def _key(req):
    return (" ".join(req["employer"].lower().split()), (req.get("uen") or "").upper(), (req.get("role") or "").lower(), (req.get("url") or ""))


def _run(job_id, req):
    _jobs[job_id]["state"] = "running"
    try:
        res = orchestrator.research(req)
        _jobs[job_id].update(state="done", result=res, text=render_text(res))
        with _lock:
            _cache[_key(req)] = (time.time(), job_id)
    except Exception as e:
        _jobs[job_id].update(state="failed", error="%s: %s" % (type(e).__name__, str(e)[:200]))


def _probe(name, url):
    try:
        code, _ = call("GET", url, timeout=5)
        return {"name": name, "reachable": True, "http": code}
    except Unavailable as e:
        return {"name": name, "reachable": False, "error": str(e)}


def serve(port):
    class H(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        timeout = 15

        def _send(self, code, body, headers=None):
            raw = json.dumps(body, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            for k, v in (headers or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(raw)

        def send_error(self, code, message=None, explain=None):
            try:
                self._send(code, {"error": message or "bad request"})
            except Exception:
                pass

        def log_message(self, *a):
            pass

        def do_GET(self):
            if self.path == "/health":
                return self._send(200, {"ok": True})
            if self.path == "/status":
                states = [j["state"] for j in _jobs.values()]
                return self._send(200, {"services": [_probe("registry", config.REGISTRY_URL + "/health"), _probe("search", config.OPENSERP_URL + "/health"),
                                                      _probe("reader", config.FETCH_URL + "/health")],
                                        "reader_backend": config.READER, "read_policy": config.READ_POLICY,
                                        "jobs": {s: states.count(s) for s in ("queued", "running", "done", "failed")}})
            if self.path.startswith("/research/"):
                j = _jobs.get(self.path.rsplit("/", 1)[1])
                return self._send(200, j) if j else self._send(404, {"error": "no such job"})
            return self._send(404, {"error": "not found"})

        def do_POST(self):
            if self.path != "/research":
                return self._send(404, {"error": "not found"})
            try:
                n = int(self.headers.get("Content-Length", "0"))
                if n > 20000:
                    return self._send(413, {"error": "body too large"})
                req = json.loads(self.rfile.read(n) or b"{}")
            except ValueError:
                return self._send(400, {"error": "body must be JSON"})
            emp = req.get("employer")
            if not isinstance(emp, str) or not emp.strip():
                return self._send(400, {"error": "employer is required"})
            if len(emp) > config.MAX_NAME_CHARS or any(len(str(req.get(k) or "")) > 500 for k in ("role", "uen", "url")):
                return self._send(400, {"error": "a field is too long"})
            k = _key(req)
            with _lock:
                hit = _cache.get(k)
                if hit and time.time() - hit[0] < config.CACHE_SECONDS and hit[1] in _jobs:
                    return self._send(200, {"id": hit[1], "cached": True, **_jobs[hit[1]]})
                jid = uuid.uuid4().hex[:12]
                _jobs[jid] = {"state": "queued", "created": time.time()}
                if len(_jobs) > 500:
                    for old in sorted(_jobs, key=lambda x: _jobs[x]["created"])[:100]:
                        _jobs.pop(old, None)
            _pool.submit(_run, jid, {"employer": emp, "role": req.get("role"), "uen": req.get("uen"), "url": req.get("url")})
            return self._send(202, {"id": jid, "state": "queued"}, {"Location": "/research/" + jid})

        def _no(self):
            self._send(405, {"error": "method not allowed"}, {"Allow": "GET, POST"})

        do_PUT = do_DELETE = do_PATCH = _no

    class Server(ThreadingHTTPServer):
        request_queue_size = 128
        daemon_threads = True

    print("company research flow on :%d (reader=%s, policy=%s)" % (port, config.READER, config.READ_POLICY), flush=True)
    Server(("0.0.0.0", port), H).serve_forever()
