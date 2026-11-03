"""ACRA registry as a self-provisioning service. Nothing is baked into the image or the repo.

On start it compares the registry's published release with the copy in $JOBHUB_DATA. With no copy (first
provision) or an older copy it downloads everything, builds a new index beside the old one, checks it, and only
then switches over. After that it re-checks every ACRA_CHECK_HOURS and refreshes when a new release appears.
A failed download or a failed check leaves the working copy serving.

    GET /health   200 once an index is usable, 503 while the first one is being built
    GET /status   release dates, entity count, age, state, last error
    GET /resolve?name=...&uen=...&hint=...
"""
import json, os, shutil, sqlite3, threading, time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import acra

CHECK_HOURS = float(os.environ.get("ACRA_CHECK_HOURS", "24"))
RETRY_MINUTES = float(os.environ.get("ACRA_RETRY_MINUTES", "30"))
MAX_AGE_DAYS = float(os.environ.get("ACRA_MAX_AGE_DAYS", "45"))   # warn when the copy is older than this
MIN_ROWS = int(os.environ.get("ACRA_MIN_ROWS", "1000000"))        # refuse an index smaller than this
SHRINK_LIMIT = 0.9                                                 # new index must keep 90% of the old row count

_lock = threading.Lock()          # one refresh at a time
_state = {"phase": "starting", "last_check": None, "last_error": None, "last_refresh_started": None}


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _pointer(data):
    return Path(data) / "registry.json"


def remote_release():
    md = json.load(acra._get(acra.META))["data"]["collectionMetadata"]
    return {"updated_at": md["lastUpdatedAt"], "ids": md["childDatasets"], "frequency": md.get("frequency")}


def current(data):
    """The live copy as {'db', 'as_of', 'built_at', 'rows'}, or None. An index built by the older CLI counts, with as_of unknown."""
    p = _pointer(data)
    if p.exists():
        cur = json.loads(p.read_text(encoding="utf-8"))
        if (Path(data) / cur["db"]).exists():
            return cur
    legacy = Path(data) / "acra.sqlite"
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
    finally:
        con.close()
    if n != rows or f != rows:
        raise RuntimeError("index row counts disagree: ent=%d fts=%d expected=%d" % (n, f, rows))
    if n < MIN_ROWS:
        raise RuntimeError("index has only %d rows (floor %d)" % (n, MIN_ROWS))
    if previous_rows and n < previous_rows * SHRINK_LIMIT:
        raise RuntimeError("new index shrank from %d to %d rows" % (previous_rows, n))
    return n


def refresh(data, force=False):
    """Bring the local copy up to the published release. Returns 'up_to_date' or 'refreshed'."""
    data = Path(data)
    with _lock:
        _state["last_check"] = _now()
        remote = remote_release()
        cur = current(data)
        if cur and not force and cur["as_of"] == remote["updated_at"]:
            return "up_to_date"
        _state["phase"] = "refreshing" if cur else "bootstrapping"
        _state["last_refresh_started"] = _now()
        stamp = remote["updated_at"][:10]
        work = data / "registry"
        work.mkdir(parents=True, exist_ok=True)
        staging = work / ("staging-" + stamp)
        db_name = "registry/acra-%s-%d.sqlite" % (stamp, int(time.time()))
        new_db = data / db_name
        try:
            if staging.exists():
                shutil.rmtree(staging)
            got = acra.download(staging, ids=remote["ids"])
            if got != len(remote["ids"]):
                raise RuntimeError("downloaded %d of %d files" % (got, len(remote["ids"])))
            rows = acra.build_index(staging, new_db)
            _check(new_db, rows, (cur or {}).get("rows"))
            pointer = {"db": db_name, "as_of": remote["updated_at"], "built_at": _now(), "rows": rows}
            tmp = _pointer(data).with_suffix(".tmp")
            tmp.write_text(json.dumps(pointer), encoding="utf-8")
            os.replace(tmp, _pointer(data))          # the switch: readers open the file the pointer names
        except Exception:
            if new_db.exists():
                new_db.unlink()
            raise
        finally:
            shutil.rmtree(staging, ignore_errors=True)
            _state["phase"] = "ready" if current(data) else "error"
        (data / "acra.sqlite").unlink(missing_ok=True)   # index from the older CLI flow, now superseded
        keep = {db_name, (cur or {}).get("db")}
        for old in work.glob("acra-*.sqlite"):          # keep the new copy and the one it replaced
            if "registry/" + old.name not in keep:
                old.unlink(missing_ok=True)
        return "refreshed"


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
    return out


def _maintain(data):
    """Background loop: provision at start, then check on a schedule. Never exits."""
    while True:
        wait = CHECK_HOURS * 3600
        try:
            result = refresh(data)
            _state["last_error"] = None
            if current(data):
                _state["phase"] = "ready"
            print("registry check:", result, flush=True)
        except Exception as e:
            _state["last_error"] = "%s: %s" % (type(e).__name__, str(e)[:300])
            _state["phase"] = "ready" if current(data) else "bootstrapping"
            wait = RETRY_MINUTES * 60
            print("registry check failed, retrying in %d min: %s" % (RETRY_MINUTES, _state["last_error"]), flush=True)
        time.sleep(wait)


def serve(data, port=8090):
    data = Path(data)
    data.mkdir(parents=True, exist_ok=True)
    threading.Thread(target=_maintain, args=(data,), daemon=True).start()

    class H(BaseHTTPRequestHandler):
        def _send(self, code, body):
            raw = json.dumps(body, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self):
            u = urlparse(self.path)
            q = {k: v[0] for k, v in parse_qs(u.query).items()}
            ready = current(data) is not None
            if u.path == "/health":
                return self._send(200 if ready else 503, {"ok": ready, "phase": _state["phase"]})
            if u.path == "/status":
                return self._send(200, status(data))
            if u.path == "/resolve":
                if not ready:
                    return self._send(503, {"error": "registry is being provisioned", **status(data)})
                if not q.get("name") and not q.get("uen"):
                    return self._send(400, {"error": "name or uen is required"})
                res = acra.resolve(db_path(data), q.get("name", ""), q.get("uen"), q.get("hint"))
                st = status(data)
                return self._send(200, {**res, "registry_as_of": st["registry_as_of"], "registry_stale": st["stale"]})
            return self._send(404, {"error": "not found"})

        def log_message(self, *a):
            pass

    print("registry service on :%d, data in %s" % (port, data), flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), H).serve_forever()
