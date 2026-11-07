"""Small JSON-over-HTTP helper. Separates 'the service answered with an error' from 'the service is not reachable'."""
import json
import urllib.error
import urllib.request


class Unavailable(Exception):
    """The service could not be reached or timed out. Callers must report this, never treat it as 'nothing found'."""


def call(method, url, headers=None, body=None, timeout=20):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    hdrs = dict(headers or {})
    if data is not None:
        hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw, code = r.read(), r.status
    except urllib.error.HTTPError as e:
        raw, code = e.read(), e.code
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        raise Unavailable("%s: %s" % (type(e).__name__, str(e)[:140]))
    try:
        return code, json.loads(raw)
    except ValueError:
        return code, {"_raw": raw[:300].decode("utf-8", "replace")}
