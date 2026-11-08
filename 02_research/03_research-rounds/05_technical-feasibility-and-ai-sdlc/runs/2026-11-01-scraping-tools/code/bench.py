"""Benchmark: same URLs through five fetch/render tools. Run inside the bench network.
Usage: python bench.py <tool>   (tools: httpx, playwright, crawl4ai, lightpanda, steel)
"""
import json, sys, time, re, urllib.robotparser, urllib.parse, httpx
UA = "JobHubResearchBot/0.1 (+local research; contact: owner)"
tool = sys.argv[1]
urls = json.load(open("/work/data/urls.json"))
items = urls["homepages"] + urls["mcf_jobs"]
PAUSE = 1.5

def allowed(u):
    p = urllib.parse.urlparse(u)
    rp = urllib.robotparser.RobotFileParser()
    try:
        r = httpx.get(f"{p.scheme}://{p.netloc}/robots.txt", headers={"User-Agent": UA}, timeout=10, follow_redirects=True)
        if r.status_code >= 400: return True
        rp.parse(r.text.splitlines())
        return rp.can_fetch(UA, u)
    except Exception:
        return True

def words(name):
    return [w.lower() for w in re.findall(r"[A-Za-z]{4,}", name) if w.lower() not in ("pte", "limited", "singapore", "services", "board")]

def run_httpx(u):
    import trafilatura
    r = httpx.get(u, headers={"User-Agent": UA}, timeout=25, follow_redirects=True)
    return r.status_code, trafilatura.extract(r.text) or ""

pw = None
def pw_ctx(endpoint=None):
    global pw
    from playwright.sync_api import sync_playwright
    if pw is None:
        pw = sync_playwright().start()
    return pw

def run_playwright(u):
    p = pw_ctx()
    b = p.chromium.launch(args=["--no-sandbox"])
    try:
        pg = b.new_context(user_agent=UA).new_page()
        resp = pg.goto(u, timeout=30000, wait_until="load")
        try: pg.wait_for_load_state("networkidle", timeout=8000)
        except Exception: pass
        return (resp.status if resp else 0), pg.inner_text("body")
    finally:
        b.close()

def run_lightpanda(u):
    p = pw_ctx()
    b = p.chromium.connect_over_cdp("ws://172.22.0.3:9222")
    try:
        ctx = b.new_context()
        pg = ctx.new_page()
        resp = pg.goto(u, timeout=30000, wait_until="load")
        return (resp.status if resp else 0), pg.evaluate("document.body ? document.body.innerText : ''")
    finally:
        b.close()

def run_crawl4ai(u):
    r = httpx.post("http://crawl4ai:11235/md", headers={"Authorization": "Bearer bench-local-token"},
                   json={"url": u, "f": "fit"}, timeout=90)
    j = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
    return r.status_code, (j.get("markdown") or "")

def run_steel(u):
    r = httpx.post("http://steel:3000/v1/scrape", json={"url": u, "format": ["markdown"]}, timeout=90)
    j = r.json()
    c = j.get("content", {})
    return r.status_code, (c.get("markdown") or "") if isinstance(c, dict) else str(c)

def _wrap(mode):
    def f(u):
        r = httpx.post("http://fetch:8080/fetch", headers={"Authorization": "Bearer local-dev-token"},
                       json={"url": u, "mode": mode}, timeout=120)
        j = r.json()
        rec_tier[0] = j.get("tier")
        return r.status_code, j.get("text") or ""
    return f
rec_tier = [None]
fn = {"wrapper_auto": _wrap("auto"), "wrapper_render": _wrap("render"), "httpx": run_httpx, "playwright": run_playwright, "crawl4ai": run_crawl4ai,
      "lightpanda": run_lightpanda, "steel": run_steel}[tool]
out = []
for it in items:
    u = it["url"]
    rec = {"employer": it["employer"], "url": u, "kind": it.get("kind", "homepage"), "tool": tool}
    if not allowed(u):
        rec.update(status="skipped_robots"); out.append(rec); print(rec["status"], u); continue
    t = time.time()
    try:
        code, text = fn(u)
        rec.update(tier=rec_tier[0], http=code, seconds=round(time.time() - t, 2), chars=len(text.strip()),
                   name_hit=any(w in text.lower() for w in words(it["employer"])),
                   status="ok" if len(text.strip()) > 200 else "thin", sample=text.strip()[:160].replace("\n", " "))
    except Exception as e:
        rec.update(status="error", seconds=round(time.time() - t, 2), error=str(e)[:150])
    out.append(rec); print(rec["status"], rec.get("seconds"), rec.get("chars"), u, flush=True)
    time.sleep(PAUSE)
json.dump(out, open(f"/work/outputs/b_{tool}.json", "w", encoding="utf-8"), indent=1)
