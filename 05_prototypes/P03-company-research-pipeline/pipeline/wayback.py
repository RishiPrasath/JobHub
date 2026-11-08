"""Site continuity from the Wayback Machine CDX API (one row per year with a 200 capture)."""
import json, urllib.parse, urllib.request

UA = "JobHubResearchBot/0.1 (research prototype)"


def years(host):
    host = host.removeprefix("www.")
    u = ("https://web.archive.org/cdx/search/cdx?output=json&fl=timestamp&collapse=timestamp:4&filter=statuscode:200&url="
         + urllib.parse.quote(host))
    try:
        rows = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=45))
    except Exception as e:
        return {"host": host, "error": str(getattr(e, "code", type(e).__name__))}
    ys = [r[0][:4] for r in rows[1:]]
    return {"host": host, "first_year": ys[0] if ys else None, "years_with_captures": len(ys)}
