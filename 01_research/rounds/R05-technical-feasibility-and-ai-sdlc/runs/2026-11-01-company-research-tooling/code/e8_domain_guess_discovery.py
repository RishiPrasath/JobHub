"""E8: find the official site by guessing domains from the registered name, then verifying the page. No search engine, no key.
Only the candidate company's own homepage is fetched, after a robots.txt check."""
import json, re, socket, sys, time, urllib.request, urllib.robotparser, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
UA = "JobHubResearchBot/0.1 (research experiment; contact: prasath.rishi@gmail.com)"
NOISE = {"pte", "ltd", "limited", "private", "co", "operative", "the", "of", "and", "singapore", "sg", "international", "holdings", "group"}
TLDS = [".com.sg", ".sg", ".com", ".org.sg", ".com.my"]


def words(s):
    return [t for t in re.sub(r"[^a-z0-9 ]", " ", s.lower()).split()]


def candidates(names):
    bases = set()
    for n in names:
        w = [t for t in words(n) if t not in NOISE]
        if not w:
            continue
        bases.update({"".join(w), "-".join(w), w[0]} | ({"".join(w[:2]), "-".join(w[:2])} if len(w) > 1 else set()))
    bases = {b for b in bases if len(b) >= 4}
    return [b + t for b in sorted(bases) for t in TLDS]


def resolves(domain):
    try:
        socket.getaddrinfo(domain, 443, type=socket.SOCK_STREAM)
        return True
    except OSError:
        return False


class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip = 0; self.t = []; self.title = ""; self._ti = False
    def handle_starttag(self, tag, a):
        if tag in ("script", "style", "noscript"): self.skip += 1
        if tag == "title": self._ti = True
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"): self.skip = max(0, self.skip - 1)
        if tag == "title": self._ti = False
    def handle_data(self, d):
        if self._ti: self.title += d
        elif not self.skip and d.strip(): self.t.append(d.strip())


def check(domain, name_tokens):
    url = "https://" + domain + "/"
    rp = urllib.robotparser.RobotFileParser()
    try:
        with urllib.request.urlopen(urllib.request.Request(url + "robots.txt", headers={"User-Agent": UA}), timeout=10) as r:
            rp.parse(r.read().decode("utf-8", "replace").splitlines())
        if not rp.can_fetch(UA, url):
            return {"domain": domain, "status": "robots_disallow"}
    except Exception:
        pass
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=12) as r:
            html = r.read(600_000).decode("utf-8", "replace"); final = r.geturl()
    except Exception as e:
        return {"domain": domain, "status": "fetch_failed:" + str(getattr(e, "code", type(e).__name__))}
    p = P(); p.feed(html); text = " ".join(p.t).lower(); title = p.title.lower()
    head = title + " " + text[:3000]
    hit = [t for t in name_tokens if t in head]
    return {"domain": domain, "final_url": final, "status": "fetched", "chars": len(text), "title": p.title.strip()[:80],
            "name_tokens_found": len(hit), "name_tokens": len(name_tokens), "name_in_title": any(t in title for t in name_tokens)}


def main():
    postings = {p["id"]: p for p in json.loads((RUN / "data/postings_v2.json").read_text(encoding="utf-8"))}
    acra = {r["id"]: r for r in json.loads((RUN / "outputs/e1c_acra_rules_v2.json").read_text(encoding="utf-8"))}
    out = []
    for pid, p in postings.items():
        legal = (acra[pid]["chosen"] or {}).get("name", "")
        names = [p["employer"], legal] + ([p["hint"]] if p.get("hint") else [])
        cands = candidates(names)
        name_tokens = sorted({t for t in words(legal or p["employer"]) if t not in NOISE and len(t) > 2})
        t0 = time.time()
        with ThreadPoolExecutor(16) as ex:
            live = [d for d, ok in zip(cands, ex.map(resolves, cands)) if ok]
        with ThreadPoolExecutor(6) as ex:
            checked = list(ex.map(lambda d: check(d, name_tokens), live))
        good = [c for c in checked if c["status"] == "fetched" and c["chars"] >= 300 and c["name_tokens"] and c["name_tokens_found"] == c["name_tokens"]]
        good.sort(key=lambda c: (-c["name_in_title"], len(c["domain"])))
        out.append({"id": pid, "employer": p["employer"], "candidates_tried": len(cands), "dns_live": len(live),
                    "verified": good[:3], "other_live": [{k: c.get(k) for k in ("domain", "status", "title", "name_tokens_found", "name_tokens")} for c in checked if c not in good][:4],
                    "seconds": round(time.time() - t0, 1)})
        print(pid, p["employer"][:28], "| tried", len(cands), "dns", len(live), "| verified:", [g["domain"] for g in good[:2]], f'{out[-1]["seconds"]}s', flush=True)
    (RUN / "outputs/e8_domain_guess.json").write_text(json.dumps(out, indent=1), encoding="utf-8")


main()
