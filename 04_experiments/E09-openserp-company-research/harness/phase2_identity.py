"""Phase 2c: what does the extractor look like to the site it visits, does it read robots.txt, and will it fetch
private addresses? This container serves a small page and logs every request headers it receives, then asks the
OpenSERP service to extract it in each mode. Also probes a few internal addresses (SSRF)."""
import json, os, threading, time, urllib.error, urllib.parse, urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

BASE = os.environ.get("OPENSERP_URL", "http://openserp:7000")
SELF = os.environ.get("SELF_HOST", "p2echo")
seen = []
PAGE = ("<html><head><title>Echo test page</title></head><body><nav>Home | About | Careers</nav><article><h1>Echo test page</h1>"
        + "<p>This is a short article used to check what the extractor sends. " * 12 + "</p></article><footer>Privacy policy | Terms</footer>"
        "<script>document.title='rendered:'+navigator.userAgent</script></body></html>")


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        seen.append({"path": self.path, "headers": {k: v for k, v in self.headers.items()}})
        body = (PAGE if self.path.startswith("/page") else "User-agent: *\nDisallow: /page-private\n").encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8" if self.path.startswith("/page") else "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


srv = HTTPServer(("0.0.0.0", 8099), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()


def ex(url, mode="auto"):
    q = urllib.parse.urlencode({"url": url, "mode": mode})
    try:
        with urllib.request.urlopen(f"{BASE}/extract?{q}", timeout=60) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except Exception:
            return e.code, {}
    except Exception as e:
        return type(e).__name__, {"message": str(e)}


out = {"requests_seen_by_site": {}, "ssrf": {}}
for mode in ("fast", "rendered", "auto"):
    seen.clear()
    code, j = ex(f"http://{SELF}:8099/page-{mode}", mode)
    out["requests_seen_by_site"][mode] = {"extract_http": code, "mode_used": (j.get("meta") or {}).get("mode_used"),
                                          "title": j.get("title"), "requests": list(seen)}
    time.sleep(2)

# robots.txt: a path the site disallows
seen.clear()
code, j = ex(f"http://{SELF}:8099/page-private", "fast")
out["robots_disallowed_path"] = {"extract_http": code, "fetched_the_page": any(r["path"] == "/page-private" for r in seen),
                                 "asked_for_robots_txt": any(r["path"] == "/robots.txt" for r in seen)}

# internal addresses
for label, url in (("the service's own health endpoint", "http://127.0.0.1:7000/health"),
                   ("cloud metadata address", "http://169.254.169.254/latest/meta-data/"),
                   ("another container on the private network", f"http://{SELF}:8099/page-internal"),
                   ("file scheme", "file:///etc/passwd")):
    code, j = ex(url, "fast")
    out["ssrf"][label] = {"url": url, "http": code, "got_content": bool(j.get("text") or j.get("markdown")),
                          "detail": (j.get("title") or j.get("message") or j.get("error") or "")[:120]}
    time.sleep(1)

json.dump(out, open("/outputs/phase2/identity_and_ssrf.json", "w", encoding="utf-8"), indent=1)
for mode, v in out["requests_seen_by_site"].items():
    print(f"[{mode}] extract http={v['extract_http']} mode_used={v['mode_used']}  site saw {len(v['requests'])} request(s)")
    for r in v["requests"]:
        h = r["headers"]
        print("   ", r["path"], "| UA:", h.get("User-Agent"), "| sec-ch-ua:", h.get("Sec-Ch-Ua"), "| Accept-Language:", h.get("Accept-Language"))
print("robots:", out["robots_disallowed_path"])
for k, v in out["ssrf"].items():
    print("ssrf", k, "->", v["http"], "content" if v["got_content"] else "no content", v["detail"])
