"""Collect ground-truth evidence from the employer's OWN public pages (homepage, privacy, terms, about).
Plain GET, honest user agent, at most 5 pages per site, no crawling beyond fixed paths. Records every regex hit
(legal-entity-looking strings and registration numbers) with the URL it came from, to data/truth_evidence/<key>.json.
Registry-mirror domains are refused. Usage: python truth_collect.py key=domain [key=domain ...]"""
import json, re, sys, urllib.request, urllib.error, concurrent.futures as cf
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "data" / "truth_evidence"
BANNED = ("sgpbusiness", "companies.sg", "recordowl", "opengovsg", "sgcompanies", "uen.sg", "bizfile")
PATHS = ["/", "/privacy-policy", "/privacy", "/terms", "/terms-and-conditions", "/terms-of-use", "/about", "/legal", "/privacy-statement", "/pdpa"]
UA = "JobHubE11-truthcheck/0.1 (research; single page fetches)"
LEGAL = re.compile(r"([A-Z][A-Za-z0-9&'.,() \-]{2,70}?\s(?:Pte\.? ?Ltd\.?|Private Limited|Limited|Ltd\.?|Co-operative Limited|Berhad|LLP|Inc\.?|LLC))")
REG = re.compile(r"((?:UEN|Co\.? ?Reg(?:istration)?\.? ?(?:No\.?)?|Company (?:Registration )?(?:No\.?|Number)|Reg(?:istration)?\.? ?No\.?|Business Registration)[^A-Za-z0-9]{0,6}[0-9]{8,9}[A-Z]|[0-9]{8,9}[A-Z](?=\W))")
def get(url):
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"}), timeout=15)
        return r.status, r.read(600000).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e: return e.code, ""
    except Exception as e: return 0, ""
def strip(h):
    h = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", h); h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", re.sub(r"&amp;", "&", re.sub(r"&copy;|&#169;", "©", h)))
def one(kv):
    key, dom = kv.split("=", 1)
    if any(b in dom for b in BANNED): return key, {"error": "banned domain"}
    res = {"key": key, "domain": dom, "pages": []}; n = 0
    for p in PATHS:
        if n >= 5: break
        url = "https://%s%s" % (dom, p); st, html = get(url)
        if st != 200 or not html: continue
        n += 1; t = strip(html)
        hits = sorted(set(m.group(1).strip() for m in REG.finditer(t)))[:8]
        legal = sorted(set(m.group(1).strip() for m in LEGAL.finditer(t) if len(m.group(1)) < 80))[:15]
        cr = [t[max(0, m.start()-60):m.end()+120] for m in re.finditer(r"©|Copyright", t)][:3]
        res["pages"].append({"url": url, "status": st, "reg_hits": hits, "legal_names": legal, "copyright": cr})
    (OUT / (key + ".json")).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    return key, res
if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    with cf.ThreadPoolExecutor(8) as ex:
        for k, r in ex.map(one, sys.argv[1:]):
            print("==", k, [p["url"].replace("https://", "") for p in r.get("pages", [])])
            for p in r.get("pages", []):
                for h in p["reg_hits"][:3]: print("   REG ", h)
                for c in p["copyright"][:1]: print("   ©   ", c[:200])
