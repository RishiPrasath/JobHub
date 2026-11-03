"""ACRA registry as a self-provisioning service. Nothing is baked into the image or the repo.

On start it compares the registry's published release with the copy in $JOBHUB_DATA. With no copy (first
provision) or an older copy it downloads everything, builds a new index beside the old one, checks it, and only
then switches over. After that it re-checks every ACRA_CHECK_HOURS and refreshes when a new release appears.

The server process only answers requests. Downloading and indexing run in a separate low-priority worker
process, so a refresh cannot slow lookups, and a worker that dies (out of memory, killed, network) cannot take
the server down. A failed refresh leaves the working copy serving. Downloads resume after a failure.

    GET /health   200 once an index is usable, 503 while the first one is being built
    GET /status   release dates, entity count, age, phase and progress, last error, request counters
    GET /resolve?name=...&uen=...&hint=...
"""
import json, os, shutil, signal, sqlite3, subprocess, sys, threading, time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import acra

try:
    import fcntl
except ImportError:          # Windows hosts: no cross-process lock, the container is the supported way to run this
    fcntl = None

CHECK_HOURS = float(os.environ.get("ACRA_CHECK_HOURS", "24"))
RETRY_MINUTES = float(os.environ.get("ACRA_RETRY_MINUTES", "30"))
MAX_AGE_DAYS = float(os.environ.get("ACRA_MAX_AGE_DAYS", "45"))        # warn when the copy is older than this
MIN_ROWS = int(os.environ.get("ACRA_MIN_ROWS", "1000000"))             # refuse an index smaller than this
SHRINK_LIMIT = 0.9                                                      # new index must keep 90% of the old row count
MAX_CONCURRENT = int(os.environ.get("ACRA_MAX_CONCURRENT", "16"))       # simultaneous lookups; more get a 503
MIN_FREE_GB = float(os.environ.get("ACRA_MIN_FREE_GB", "1.5"))          # a refresh needs about this much free space beyond the live copies
WORKER_TIMEOUT_MIN = float(os.environ.get("ACRA_WORKER_TIMEOUT_MIN", "90"))

_state = {"phase": "starting", "last_check": None, "last_error": None, "worker_pid": None}
_stats = {"requests": 0, "ok": 0, "client_errors": 0, "server_errors": 0, "busy": 0, "timeouts": 0, "ms_total": 0.0, "ms_max": 0.0}
_stats_lock = threading.Lock()
_slots = threading.BoundedSemaphore(MAX_CONCURRENT)
_stop = threading.Event()


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _pointer(data):
    return Path(data) / "registry.json"


def _progress_file(data):
    return Path(data) / "registry" / "progress.json"


def _write_json_atomic(path, obj):
    tmp = Path(str(path) + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def remote_release():
    md = json.load(acra._get(acra.META))["data"]["collectionMetadata"]
    return {"updated_at": md["lastUpdatedAt"], "ids": md["childDatasets"], "frequency": md.get("frequency")}


def _usable(db):
    """True when the file opens read-only and has the expected tables."""
    try:
        con = sqlite3.connect("file:%s?mode=ro" % Path(db).as_posix(), uri=True)
        try:
            con.execute("select 1 from ent limit 1").fetchone()
            con.execute("select 1 from fts limit 1").fetchone()
        finally:
            con.close()
        return True
    except Exception:
        return False


def current(data):
    """The live copy as {'db', 'as_of', 'built_at', 'rows'}, or None.
    If the pointer is missing or unreadable, fall back to the newest index file that opens, then to an index
    built by the older CLI flow (as_of unknown, so the next check refreshes it)."""
    data = Path(data)
    try:
        cur = json.loads(_pointer(data).read_text(encoding="utf-8"))
        if (data / cur["db"]).exists():
            return cur
    except Exception:
        pass
    found = sorted((data / "registry").glob("acra-*.sqlite"), key=lambda p: p.stat().st_mtime, reverse=True) if (data / "registry").exists() else []
    for f in found:
        if _usable(f):
            return {"db": "registry/" + f.name, "as_of": None, "built_at": None, "rows": None, "recovered": True}
    legacy = data / "acra.sqlite"
    if legacy.exists():
        return {"db": legacy.name, "as_of": None, "built_at": None, "rows": None}
    return None


def db_path(data):
    cur = current(data)
    return Path(data) / cur["db"] if cur else Path(data) / "acra.sqlite"


def _check(db, rows, previous_rows):
    con = sqlite3.connect(db)
    try:
        n = con.execute("select count(*) from ent").fetchone()[0]
        f = con.execute("select count(*) from fts").fetchone()[0]
        con.execute("select count(*) from fts where fts match ?", ('"pte"',)).fetchone()
        probe = con.execute("select uen,name from ent where status like 'Live%' limit 1").fetchone()
    finally:
        con.close()
    if n != rows or f != rows:
        raise RuntimeError("index row counts disagree: ent=%d fts=%d expected=%d" % (n, f, rows))
    if n < MIN_ROWS:
        raise RuntimeError("index has only %d rows (floor %d)" % (n, MIN_ROWS))
    if previous_rows and n < previous_rows * SHRINK_LIMIT:
        raise RuntimeError("new index shrank from %d to %d rows" % (previous_rows, n))
    if not probe or acra.resolve(db, probe[1])["state"] == "unresolved":   # a lookup must work end to end
        raise RuntimeError("test lookup failed on the new index")
    return n


def refresh(data, force=False):
    """Bring the local copy up to the published release (runs in the worker process, or by hand via the CLI).
    Returns 'up_to_date' or 'refreshed'. Raises on failure, leaving the live copy untouched."""
    data = Path(data)
    work = data / "registry"
    work.mkdir(parents=True, exist_ok=True)
    lock = open(work / ".lock", "w")
    try:
        if fcntl:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)     # one refresh at a time, even across containers on one volume
    except OSError:
        raise RuntimeError("another refresh is already running on this data volume")
    try:
        remote = remote_release()
        cur = current(data)
        if cur and not force and cur["as_of"] == remote["updated_at"]:
            return "up_to_date"
        stamp = remote["updated_at"][:10]
        staging = work / ("staging-" + stamp)                 # kept across failures so a retry resumes
        for old in work.glob("staging-*"):
            if old != staging:
                shutil.rmtree(old, ignore_errors=True)
        for orphan in list(work.glob("*.building")) + list(work.glob("*.tmp")):
            orphan.unlink(missing_ok=True)
        started = _now()
        have = sum(f.stat().st_size for f in staging.glob("*.csv")) if staging.exists() else 0
        free = shutil.disk_usage(data).free + have
        if free < MIN_FREE_GB * 1e9:
            raise RuntimeError("only %.1f GB free on the data volume; a refresh needs about %.1f GB" % (free / 1e9, MIN_FREE_GB))

        def progress(done, total, step="downloading"):
            _write_json_atomic(_progress_file(data), {"step": step, "done": done, "total": total, "started": started, "release": stamp})

        got = acra.download(staging, ids=remote["ids"], on_progress=progress)
        if got != len(remote["ids"]):
            raise RuntimeError("downloaded %d of %d files; will resume" % (got, len(remote["ids"])))
        again = remote_release()["updated_at"]
        if again != remote["updated_at"]:
            shutil.rmtree(staging, ignore_errors=True)
            raise RuntimeError("ACRA published a new release while downloading; starting over")
        progress(len(remote["ids"]), len(remote["ids"]), "indexing")
        db_name = "registry/acra-%s-%d.sqlite" % (stamp, int(time.time()))
        building = data / (db_name + ".building")
        try:
            rows = acra.build_index(staging, building)
            progress(len(remote["ids"]), len(remote["ids"]), "checking")
            _check(building, rows, (cur or {}).get("rows"))
            building.replace(data / db_name)
        except Exception:
            building.unlink(missing_ok=True)
            shutil.rmtree(staging, ignore_errors=True)       # do not resume from files that produced a bad index
            raise
        _write_json_atomic(_pointer(data), {"db": db_name, "as_of": remote["updated_at"], "built_at": _now(), "rows": rows})
        shutil.rmtree(staging, ignore_errors=True)
        (data / "acra.sqlite").unlink(missing_ok=True)       # index from the older CLI flow, now superseded
        keep = {db_name, (cur or {}).get("db")}
        for old in work.glob("acra-*.sqlite"):               # keep the new copy and the one it replaced
            if "registry/" + old.name not in keep:
                old.unlink(missing_ok=True)
        _progress_file(data).unlink(missing_ok=True)
        return "refreshed"
    finally:
        lock.close()


def status(data):
    cur = current(data)
    out = {"phase": _state["phase"], "last_check": _state["last_check"], "last_error": _state["last_error"],
           "check_every_hours": CHECK_HOURS, "registry_as_of": None, "built_at": None, "rows": None,
           "age_days": None, "stale": None}
    if cur:
        out.update(registry_as_of=cur["as_of"], built_at=cur["built_at"], rows=cur["rows"])
        if cur["as_of"]:
            age = (datetime.now(timezone.utc) - datetime.fromisoformat(cur["as_of"])).days
            out.update(age_days=age, stale=age > MAX_AGE_DAYS)
    out["worker_running"] = _state.get("worker_pid") is not None
    if _state["phase"] in ("bootstrapping", "refreshing"):
        try:
            out["progress"] = json.loads(_progress_file(data).read_text(encoding="utf-8"))
        except Exception:
            out["progress"] = None
    with _stats_lock:
        n = _stats["requests"]
        out["requests"] = {**{k: v for k, v in _stats.items() if k not in ("ms_total", "ms_max")},
                           "avg_ms": round(_stats["ms_total"] / n, 1) if n else 0, "max_ms": round(_stats["ms_max"], 1)}
    return out


def _run_worker(data):
    """Run one refresh in a child process at low priority; return (result, error)."""
    cmd = [sys.executable, "-m", "pipeline.cli", "acra-update", "--if-changed"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, preexec_fn=lambda: os.nice(10))
    _state["worker_pid"] = proc.pid
    try:
        out, err = proc.communicate(timeout=WORKER_TIMEOUT_MIN * 60)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.communicate()
        return None, "refresh worker timed out after %d min" % WORKER_TIMEOUT_MIN
    finally:
        _state["worker_pid"] = None
    if proc.returncode == 0:
        return (out.strip().splitlines() or ["ok"])[-1], None
    if proc.returncode in (137, -9):
        return None, "refresh worker was killed (out of memory?)"
    tail = (err.strip().splitlines() or ["exit %s" % proc.returncode])[-1]
    return None, tail[:300]


def _maintain(data):
    """Background loop: provision at start, then check on a schedule. Never exits."""
    backoff = 60
    while not _stop.is_set():
        _state["last_check"] = _now()
        have = current(data) is not None
        _state["phase"] = "refreshing" if have else "bootstrapping"
        result, err = _run_worker(data)
        have = current(data) is not None
        if err:
            _state["last_error"] = err
            _state["phase"] = "ready" if have else "bootstrapping"
            # nothing to serve yet: retry quickly with backoff; otherwise the normal retry interval
            wait = min(backoff, 900) if not have else RETRY_MINUTES * 60
            backoff *= 2
            print("registry check failed, retrying in %d s: %s" % (wait, err), flush=True)
        else:
            _state["last_error"] = None
            _state["phase"] = "ready"
            backoff = 60
            wait = CHECK_HOURS * 3600
            print("registry check:", result, flush=True)
        _stop.wait(wait)


def _bump(key, ms=None):
    with _stats_lock:
        _stats["requests"] += 1
        _stats[key] += 1
        if ms is not None:
            _stats["ms_total"] += ms
            _stats["ms_max"] = max(_stats["ms_max"], ms)


def serve(data, port=8090):
    data = Path(data)
    data.mkdir(parents=True, exist_ok=True)
    worker = threading.Thread(target=_maintain, args=(data,), daemon=True)
    worker.start()

    class H(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        timeout = 15                                   # drop idle or slow clients

        def _send(self, code, body, headers=None):
            raw = json.dumps(body, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            for k, v in (headers or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self):
            t0 = time.time()
            u = urlparse(self.path)
            q = {k: v[0] for k, v in parse_qs(u.query, max_num_fields=20).items()}
            ready = current(data) is not None
            if u.path == "/health":
                return self._send(200 if ready else 503, {"ok": ready, "phase": _state["phase"]})
            if u.path == "/status":
                return self._send(200, status(data))
            if u.path != "/resolve":
                _bump("client_errors")
                return self._send(404, {"error": "not found"})
            name = q.get("name", "")
            if not name.strip() and not q.get("uen"):
                _bump("client_errors")
                return self._send(400, {"error": "name or uen is required"})
            if len(name) > acra.MAX_NAME_CHARS or len(q.get("hint", "")) > acra.MAX_NAME_CHARS or len(q.get("uen", "")) > 20:
                _bump("client_errors")
                return self._send(400, {"error": "name or hint longer than %d characters, or uen longer than 20" % acra.MAX_NAME_CHARS})
            if not ready:
                _bump("server_errors")
                return self._send(503, {"error": "registry is being provisioned", **status(data)}, {"Retry-After": "30"})
            if not _slots.acquire(timeout=2):
                _bump("busy")
                return self._send(503, {"error": "too many lookups in progress"}, {"Retry-After": "1"})
            try:
                res = acra.resolve(db_path(data), name, q.get("uen"), q.get("hint"))
            except acra.LookupTimeout as e:
                _bump("timeouts")
                return self._send(504, {"error": str(e)})
            except Exception as e:
                _bump("server_errors")
                return self._send(500, {"error": "lookup failed: %s" % type(e).__name__})
            finally:
                _slots.release()
            st = status(data)
            _bump("ok", (time.time() - t0) * 1000)
            return self._send(200, {**res, "registry_as_of": st["registry_as_of"], "registry_stale": st["stale"]})

        def _not_allowed(self):
            self._send(405, {"error": "method not allowed"}, {"Allow": "GET"})

        do_POST = do_PUT = do_DELETE = do_PATCH = _not_allowed

        def send_error(self, code, message=None, explain=None):    # malformed requests also get JSON, not an HTML page
            try:
                self._send(code, {"error": message or "bad request"})
            except Exception:
                pass

        def log_message(self, *a):
            pass

    class Server(ThreadingHTTPServer):
        request_queue_size = 256         # the default of 5 makes bursts of new connections wait for a TCP retry (about 1 to 3 s)
        daemon_threads = True

    httpd = Server(("0.0.0.0", port), H)

    def shutdown(*_):
        print("shutting down", flush=True)
        _stop.set()
        pid = _state.get("worker_pid")
        if pid:
            try:
                os.kill(pid, signal.SIGTERM)
            except OSError:
                pass
        threading.Thread(target=httpd.shutdown, daemon=True).start()

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    print("registry service on :%d, data in %s" % (port, data), flush=True)
    httpd.serve_forever()
