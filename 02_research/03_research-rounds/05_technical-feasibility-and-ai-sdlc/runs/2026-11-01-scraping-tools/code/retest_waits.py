"""Retest Crawl4AI (raw markdown, wait) and Lightpanda (wait + settle) on the 5 job pages."""
import json, time, httpx, sys
from playwright.sync_api import sync_playwright
jobs = json.load(open("/work/data/urls.json"))["mcf_jobs"]
LP = sys.argv[1]
out = []
for j in jobs:
    u = j["url"]
    t = time.time()
    r = httpx.post("http://crawl4ai:11235/md", headers={"Authorization": "Bearer bench-local-token"},
                   json={"url": u, "f": "raw"}, timeout=90)
    md = (r.json().get("markdown") or "")
    out.append(dict(tool="crawl4ai_raw", url=u[:80], chars=len(md), seconds=round(time.time() - t, 2),
                    has_responsibilities=("esponsibilit" in md)))
    time.sleep(2)
with sync_playwright() as p:
    for j in jobs:
        u = j["url"]
        t = time.time()
        b = p.chromium.connect_over_cdp(f"ws://{LP}:9222")
        pg = b.new_context().new_page()
        try:
            pg.goto(u, timeout=30000, wait_until="load")
            try: pg.wait_for_load_state("networkidle", timeout=8000)
            except Exception: pass
            pg.wait_for_timeout(3000)
            txt = pg.evaluate("document.body ? document.body.innerText : ''")
        except Exception as e:
            txt = "ERR " + str(e)[:80]
        b.close()
        out.append(dict(tool="lightpanda_wait", url=u[:80], chars=len(txt), seconds=round(time.time() - t, 2),
                        has_responsibilities=("esponsibilit" in txt)))
        time.sleep(2)
json.dump(out, open("/work/outputs/retest_waits.json", "w"), indent=1)
for o in out: print(o)
