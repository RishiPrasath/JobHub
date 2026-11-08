"""robots.txt-respecting plain HTTP page capture. Blocked pages are reported as blocked, never worked around."""
import time, urllib.parse, urllib.request, urllib.robotparser
from html.parser import HTMLParser

UA = "JobHubResearchBot/0.1 (research prototype)"


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
        self.title = ""
        self._t = False

    def handle_starttag(self, tag, a):
        if tag in ("script", "style", "noscript"):
            self.skip += 1
        if tag == "title":
            self._t = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.skip = max(0, self.skip - 1)
        if tag == "title":
            self._t = False

    def handle_data(self, d):
        if self._t:
            self.title += d
        elif not self.skip and d.strip():
            self.parts.append(d.strip())


def fetch(url, timeout=25):
    host = "{0.scheme}://{0.netloc}".format(urllib.parse.urlparse(url))
    rec = {"url": url, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    rp = urllib.robotparser.RobotFileParser()
    try:
        with urllib.request.urlopen(urllib.request.Request(host + "/robots.txt", headers={"User-Agent": UA}), timeout=20) as r:
            rp.parse(r.read().decode("utf-8", "replace").splitlines())
        rec["robots"] = "read"
        if not rp.can_fetch(UA, url):
            return {**rec, "status": "blocked_by_robots", "text": ""}
    except Exception as e:
        rec["robots"] = "unavailable:%s" % getattr(e, "code", type(e).__name__)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"}), timeout=timeout) as r:
            html = r.read(2_000_000).decode("utf-8", "replace")
            rec["http"] = r.status
    except Exception as e:
        return {**rec, "status": "blocked_or_failed:%s" % getattr(e, "code", type(e).__name__), "text": ""}
    p = _Text()
    p.feed(html)
    text = "\n".join(p.parts)
    return {**rec, "status": "ok" if len(text) >= 500 else "thin", "title": p.title.strip()[:120], "text": text}
