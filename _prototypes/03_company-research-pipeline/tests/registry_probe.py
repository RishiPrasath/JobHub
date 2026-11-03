"""Probe the running registry service (default http://127.0.0.1:8090) with bad inputs and load.
Run on the host:  python tests/registry_probe.py [base_url]
Prints one line per probe: what was sent, the HTTP status, the time, and whether that is acceptable."""
import json, os, statistics, sys, threading, time, urllib.error, urllib.parse, urllib.request

BASE = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8090"


def call(path, method="GET", timeout=30):
    t = time.time()
    try:
        req = urllib.request.Request(BASE + path, method=method, data=b"" if method == "POST" else None)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            return r.status, time.time() - t, body
    except urllib.error.HTTPError as e:
        return e.code, time.time() - t, e.read()
    except Exception as e:
        return type(e).__name__, time.time() - t, str(e).encode()


def q(name, **kw):
    return "/resolve?" + urllib.parse.urlencode({"name": name, **kw})


results = []


def probe(label, path, ok_codes, method="GET", max_seconds=5):
    code, secs, body = call(path, method)
    good = code in ok_codes and secs <= max_seconds
    results.append(good)
    print(("PASS " if good else "FAIL ") + f"{label:44} {str(code):>6} {secs*1000:8.0f} ms  {body[:70]!r}")


print("--- bad and odd inputs")
probe("empty name", "/resolve?name=", (400,))
probe("no parameters", "/resolve", (400,))
probe("whitespace only", q("   "), (200, 400))
probe("punctuation only", q("!!! ??? ..."), (200, 400))
probe("single common word 'singapore'", q("singapore"), (200,))
probe("single common word 'the'", q("the"), (200,))
probe("single common word 'pte ltd'", q("pte ltd"), (200,))
probe("quotes and FTS operators", q('"AND" OR NOT NEAR( ) * -x'), (200, 400))
probe("SQL injection style", q("x'; drop table ent;--"), (200, 400))
probe("unicode (Chinese name)", q("新加坡电信有限公司"), (200,))
probe("unicode (emoji)", q("Coffee ☕ Club 🎉"), (200,))
probe("NUL byte", "/resolve?name=a%00b", (200, 400))
LONG = os.environ.get("SKIP_LONG") != "1"
if LONG: probe("very long name (5,000 chars)", q("alpha beta gamma " * 300), (200, 400), max_seconds=10)
# an oversized request line is refused by closing the connection; the client sees a 414 or a reset depending on timing
if LONG: probe("very long name (200,000 chars)", q("x" * 200000), (400, 414, "ConnectionResetError", "ConnectionAbortedError", "RemoteDisconnected"), max_seconds=10)
if LONG: probe("2,000 distinct tokens", q(" ".join(f"word{i}" for i in range(2000))), (200, 400), max_seconds=10)
probe("UEN lookup that exists", "/resolve?uen=199304055W", (200,))
probe("UEN lookup that does not exist", "/resolve?uen=000000000X", (200,))
probe("UEN with quotes", "/resolve?uen=%22%27%3B--", (200, 400))
probe("unknown path", "/nope", (404,))
probe("path traversal", "/../../etc/passwd", (404, 400))
probe("POST to /resolve", "/resolve?name=x", (404, 405, 501), method="POST")
probe("/status", "/status", (200,))
probe("/health", "/health", (200, 503))
probe("/check on a real employer", q("Randstad Pte Limited").replace("/resolve", "/check"), (200,))
probe("/check on a lookalike", q("DBS Bank Singapore Recruitment Pte Ltd").replace("/resolve", "/check"), (200,))
probe("/check with an ID from a URL", "/check?name=Singtel&url=https%3A%2F%2Fexample.com%2Fcompany%2Fsingtel-199201624D", (200,))
probe("/selftest (runs 12 canary lookups)", "/selftest", (200, 503), max_seconds=15)

print("--- load: 400 lookups, 20 at a time")
names = ["Randstad Pte Limited", "Singapore Telecommunications Limited", "Kyndryl Singapore", "Natureland Care", "Palo IT Singapore",
         "Coffee Club", "Persol Singapore", "Temp-Team", "singapore", "holdings", "pte ltd", "food", "global", "tan"]
lat, codes = [], []
lock = threading.Lock()


def worker(i):
    code, secs, _ = call(q(names[i % len(names)]))
    with lock:
        lat.append(secs); codes.append(code)


t0 = time.time()
threads = []
for i in range(400):
    while sum(th.is_alive() for th in threads) >= 20:
        time.sleep(0.005)
    th = threading.Thread(target=worker, args=(i,)); th.start(); threads.append(th)
for th in threads:
    th.join()
lat.sort()
print(f"     {len(codes)} requests in {time.time()-t0:.1f}s | statuses {sorted(set(map(str, codes)))} | "
      f"p50 {lat[len(lat)//2]*1000:.0f} ms  p95 {lat[int(len(lat)*.95)]*1000:.0f} ms  max {lat[-1]*1000:.0f} ms")
ok = set(codes) == {200} and lat[int(len(lat) * .95)] < 2
results.append(ok)
print("PASS load" if ok else "FAIL load")
print(f"\n{sum(results)} of {len(results)} probes passed")
