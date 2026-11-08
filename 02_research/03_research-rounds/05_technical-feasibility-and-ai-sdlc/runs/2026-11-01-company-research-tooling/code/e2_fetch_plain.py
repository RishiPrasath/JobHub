"""E2: robots.txt check + plain HTTP fetch + JSON-LD / visible-text extraction on official sites."""
import json, re, time, urllib.request, urllib.robotparser, urllib.parse
from html.parser import HTMLParser
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
UA = "JobHubResearchBot/0.1 (+research experiment; contact: prasath.rishi@gmail.com)"
SITES = {  # discovered via WebSearch on 2026-11-01; None = no official site found
 "P01": None, "P02": None, "P09": None, "P13": None,
 "P03": "https://www.palo-it.com/", "P04": "https://www.grab.com/sg/", "P05": "https://www.amkh.org.sg/",
 "P06": "https://www.sgh.com.sg/", "P07": "https://www.hrnetgroup.com/", "P08": "https://www.dhl.com/sg-en/home/supply-chain.html",
 "P10": "https://www.marinabaysands.com/", "P11": "https://www.natureland.com.sg/", "P12": "https://www.fairprice.com.sg/",
 "P14": "https://www.littleskoolhouse.com/", "P15": "https://www.randstad.com.sg/",
}

class TextGrab(HTMLParser):
    def __init__(s):
        super().__init__(); s.skip = 0; s.text = []; s.ld = []; s._ld = False; s.title = ""; s._t = False
    def handle_starttag(s, tag, a):
        a = dict(a)
        if tag in ("script", "style", "noscript"):
            if tag == "script" and a.get("type") == "application/ld+json": s._ld = True; s.ld.append("")
            else: s.skip += 1
        if tag == "title": s._t = True
    def handle_endtag(s, tag):
        if tag in ("script", "style", "noscript"):
            if s._ld and tag == "script": s._ld = False
            else: s.skip = max(0, s.skip - 1)
        if tag == "title": s._t = False
    def handle_data(s, d):
        if s._ld: s.ld[-1] += d
        elif s._t: s.title += d
        elif not s.skip and d.strip(): s.text.append(d.strip())

def run():
    out = []
    for pid, url in SITES.items():
        rec = {"id": pid, "url": url}
        if not url: rec["status"] = "no_official_site_found"; out.append(rec); continue
        host = "{0.scheme}://{0.netloc}".format(urllib.parse.urlparse(url))
        t0 = time.time()
        # robots.txt
        rp = urllib.robotparser.RobotFileParser()
        try:
            req = urllib.request.Request(host + "/robots.txt", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                rp.parse(r.read().decode("utf-8", "replace").splitlines()); rec["robots"] = "read"
            rec["robots_allows_page"] = rp.can_fetch(UA, url)
        except Exception as e:
            rec["robots"] = f"unavailable:{getattr(e,'code',type(e).__name__)}"; rec["robots_allows_page"] = None
        if rec["robots_allows_page"] is False:
            rec["status"] = "blocked_by_robots"; out.append(rec); print(pid, rec["status"]); continue
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"}), timeout=25) as r:
                html = r.read(2_000_000).decode("utf-8", "replace"); rec["http"] = r.status; rec["final_url"] = r.geturl()
            g = TextGrab(); g.feed(html)
            text = " ".join(g.text)
            types = []
            for blob in g.ld:
                try:
                    j = json.loads(blob); items = j if isinstance(j, list) else j.get("@graph", [j])
                    types += [str(i.get("@type")) for i in items if isinstance(i, dict)]
                except Exception: pass
            rec.update(title=g.title.strip()[:120], visible_chars=len(text), jsonld_types=types, html_bytes=len(html),
                       status="ok" if len(text) >= 500 else "thin_needs_js_or_blocked")
            (RUN / f"outputs/pages/{pid}_plain.txt").write_text(text[:60000], encoding="utf-8")
        except Exception as e:
            rec["status"] = f"fetch_failed:{getattr(e,'code',type(e).__name__)}"
        rec["seconds"] = round(time.time() - t0, 1); out.append(rec); print(pid, rec["status"], rec.get("visible_chars"), rec["seconds"], flush=True)
        time.sleep(1.5)
    (RUN / "outputs/e2_plain_fetch.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
(RUN / "outputs/pages").mkdir(parents=True, exist_ok=True)
run()
