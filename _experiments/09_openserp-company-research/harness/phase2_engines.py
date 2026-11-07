"""Phase 2a: which engines answer from this environment, how fast, and what a failure looks like.
6 engines x 2 queries, 8 s apart (the service also rate-limits to 10/min per engine)."""
import json, os, time, urllib.parse, urllib.request, urllib.error

BASE = os.environ.get("OPENSERP_URL", "http://openserp:7000")
OUT = "/outputs/phase2/engines"
os.makedirs(OUT, exist_ok=True)
ENGINES = ["duckduckgo", "bing", "google", "ecosia", "yandex", "baidu"]
QUERIES = {"known": "Randstad Singapore employee reviews", "obscure": "Zzqxv Qwlmt Holdings Singapore scam"}
rows = []
for eng in ENGINES:
    for qid, q in QUERIES.items():
        url = f"{BASE}/{eng}/search?" + urllib.parse.urlencode({"text": q, "limit": 8})
        t = time.time()
        code, body = None, b""
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                code, body = r.status, r.read()
        except urllib.error.HTTPError as e:
            code, body = e.code, e.read()
        except Exception as e:
            code, body = type(e).__name__, str(e).encode()
        secs = round(time.time() - t, 2)
        rec = {"engine": eng, "query_id": qid, "query": q, "http": code, "seconds": secs}
        try:
            j = json.loads(body)
            res = j.get("results", [])
            rec.update(organic=sum(1 for r in res if r.get("type") == "organic"), ads=sum(1 for r in res if r.get("type") == "ad"),
                       other=sum(1 for r in res if r.get("type") not in ("organic", "ad")),
                       took_ms=j.get("meta", {}).get("took_ms"), engines_failed=j.get("meta", {}).get("engines_failed"),
                       top_domains=[r.get("domain") for r in res if r.get("type") == "organic"][:5])
            if "error" in j:
                rec["error"] = {k: j[k] for k in ("error", "code", "message") if k in j}
            json.dump(j, open(f"{OUT}/{eng}_{qid}.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        except Exception:
            rec["raw"] = body[:300].decode("utf-8", "replace")
        rows.append(rec)
        print(f"{eng:11} {qid:8} http={str(code):4} {secs:6.1f}s organic={rec.get('organic')} ads={rec.get('ads')} err={rec.get('error') or rec.get('engines_failed') or ''} top={rec.get('top_domains', [])[:3]}", flush=True)
        time.sleep(8)
json.dump(rows, open("/outputs/phase2/engines_summary.json", "w", encoding="utf-8"), indent=1)
