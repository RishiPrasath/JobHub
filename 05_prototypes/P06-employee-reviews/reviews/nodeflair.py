"""NodeFlair probe: research only, never shown in the product.

NodeFlair's robots.txt allows / for all agents (Disallow: /api/v2) with the
Cloudflare content signal "search=yes, ai-train=no, use=reference". Its terms
do not bar automated reading, but say no part of the content may be used for
commercial purposes without a licence (E16 run-003). So this module:

- reads robots.txt first and stops if the page is disallowed,
- sends one request per company, at least MIN_DELAY_S apart,
- keeps only the aggregate numbers from the page's schema.org
  EmployerAggregateRating block (count, rating, website), never review text,
- marks every result display_allowed=False.

Showing anything from NodeFlair needs a licence and a new owner decision
(decision 0005). Do not feed the output to a model (ai-train=no).
"""
import json
import re
import time
import urllib.request
import urllib.robotparser
from datetime import datetime, timezone

BASE = "https://nodeflair.com"
USER_AGENT = "JobHub-research/0.1 (Python urllib; aggregate probe, no review text kept)"
MIN_DELAY_S = 6
_last_request = 0.0

_LD_RE = re.compile(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', re.S | re.I)

NOT_FOR_DISPLAY = ("NodeFlair terms need a licence for commercial use, and its newest reviews for the "
                   "employers checked are over 2 years old. Kept for research only.")


def parse_aggregate(html: str) -> dict | None:
    """Pull the EmployerAggregateRating block out of a reviews page."""
    for block in _LD_RE.findall(html):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        for item in data if isinstance(data, list) else [data]:
            if isinstance(item, dict) and item.get("@type") == "EmployerAggregateRating":
                org = item.get("itemReviewed") or {}
                return {
                    "review_count": item.get("reviewCount"),
                    "rating": item.get("ratingValue"),
                    "best": item.get("bestRating"),
                    "company_name": org.get("name"),
                    "company_website": org.get("sameAs"),
                    "nodeflair_url": org.get("url"),
                }
    return None


def _robots_allows(url: str) -> bool:
    rp = urllib.robotparser.RobotFileParser(BASE + "/robots.txt")
    rp.read()
    return rp.can_fetch(USER_AGENT, url)


def probe(slug: str, timeout: int = 30) -> dict:
    """Fetch one company's reviews page and keep only the aggregate numbers."""
    global _last_request
    url = f"{BASE}/companies/{slug}/reviews"
    result = {"slug": slug, "url": url, "display_allowed": False, "why_not_shown": NOT_FOR_DISPLAY,
              "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    if not _robots_allows(url):
        result.update(status="robots_disallowed")
        return result
    wait = MIN_DELAY_S - (time.time() - _last_request)
    if wait > 0:
        time.sleep(wait)
    _last_request = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            html = r.read().decode("utf-8", "replace")
            result["http_status"] = r.status
    except urllib.error.HTTPError as e:
        # 403/429/503 or a Cloudflare challenge: stop, do not retry around it.
        result.update(status="blocked_or_error", http_status=e.code)
        return result
    except Exception as e:  # timeouts are common on this site
        result.update(status="error", error=type(e).__name__)
        return result
    result["seconds"] = round(time.time() - t0, 1)
    agg = parse_aggregate(html)
    result.update(status="ok" if agg else "no_aggregate", aggregate=agg)
    return result
