"""Polite single-page reader built on the Clearcote browser (Python SDK).

Used by the 2026-11-21 reruns of scraping-related experiments (E14, E16).
Clearcote is a Chromium build driven through Playwright. Here it is used only
as a rendering browser for pages that a plain fetch could not render.

Rules this reader enforces (from AGENTS.md and the owner's instructions):
- robots.txt is read first; a disallowed URL is never fetched.
- At least MIN_DELAY seconds between requests to the same host, or the
  host's Crawl-delay if larger.
- One attempt per URL. An HTTP 401/403/429 or a bot-challenge page is
  recorded as "blocked" and NOT retried or worked around. Clearcote's
  fingerprint features are not used to get past a block.
- No login, no cookies carried between runs, no form submission.
- No keys or credentials: the open build needs none. If a licence key is
  ever used it must come from the CLEARCOTE_LICENSE_KEY env var.

Usage (from a harness):
    from clearcote_reader import Reader
    with Reader(out_dir) as r:
        rec = r.read("https://example.com/terms", label="example-terms")
"""
from __future__ import annotations

import hashlib
import json
import time
import urllib.error
import urllib.request
import urllib.robotparser
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

READER_VERSION = "clearcote-reader 0.1.0"
ROBOTS_AGENT = "JobHubResearch"
MIN_DELAY = 5.0
NAV_TIMEOUT_MS = 45_000
SETTLE_MS = 4_000
CHALLENGE_MARKERS = (
    "just a moment",
    "verify you are human",
    "are you a robot",
    "checking your browser",
    "captcha",
    "access denied",
    "request blocked",
    "unusual traffic",
    "press & hold",
    "attention required",
)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class Reader:
    def __init__(self, out_dir: Path, fingerprint: str = "jobhub-research-2026-11-21"):
        self.out_dir = Path(out_dir)
        (self.out_dir / "raw").mkdir(parents=True, exist_ok=True)
        self.fingerprint = fingerprint
        self._robots: dict[str, tuple[urllib.robotparser.RobotFileParser | None, str]] = {}
        self._last: dict[str, float] = {}
        self._ctx = None
        self.log_path = self.out_dir / "reads.jsonl"

    # browser lifecycle -------------------------------------------------
    def __enter__(self):
        from clearcote import launch  # imported here so robots checks work without it

        self._ctx = launch(fingerprint=self.fingerprint, platform="windows",
                           brand="Chrome", headless=True)
        return self

    def __exit__(self, *exc):
        if self._ctx is not None:
            self._ctx.close()

    # robots ------------------------------------------------------------
    def robots(self, url: str):
        u = urlparse(url)
        base = f"{u.scheme}://{u.netloc}"
        if base in self._robots:
            return self._robots[base]
        rp = urllib.robotparser.RobotFileParser()
        note = ""
        try:
            req = urllib.request.Request(base + "/robots.txt",
                                         headers={"User-Agent": ROBOTS_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                body = resp.read().decode("utf-8", "replace")
            rp.parse(body.splitlines())
            note = f"robots.txt read ({len(body)} bytes)"
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                rp.disallow_all = True
                note = f"robots.txt HTTP {e.code}: treated as disallow all"
            else:
                rp.allow_all = True
                note = f"robots.txt HTTP {e.code}: no rules, allow"
        except Exception as e:  # network errors: be conservative
            rp = None
            note = f"robots.txt unreachable ({type(e).__name__}): not fetched"
        self._robots[base] = (rp, note)
        return rp, note

    # read --------------------------------------------------------------
    def read(self, url: str, label: str) -> dict:
        rec = {"label": label, "url": url, "time_utc": _now(), "reader": READER_VERSION}
        rp, note = self.robots(url)
        rec["robots"] = note
        allowed = bool(rp) and rp.can_fetch(ROBOTS_AGENT, url) and rp.can_fetch("*", url)
        rec["robots_allowed"] = allowed
        if not allowed:
            rec["outcome"] = "skipped_robots"
            return self._log(rec)
        host = urlparse(url).netloc
        delay = MIN_DELAY
        try:
            cd = rp.crawl_delay("*")
            if cd:
                delay = max(delay, float(cd))
        except Exception:
            pass
        wait = self._last.get(host, 0) + delay - time.time()
        if wait > 0:
            time.sleep(wait)
        page = self._ctx.new_page()
        try:
            resp = page.goto(url, wait_until="domcontentloaded", timeout=NAV_TIMEOUT_MS)
            page.wait_for_timeout(SETTLE_MS)
            status = resp.status if resp else None
            title = page.title()
            text = page.evaluate("() => document.body ? document.body.innerText : ''") or ""
            rec.update(status=status, final_url=page.url, title=title, text_chars=len(text))
            low = (title + " " + text[:3000]).lower()
            marker = next((m for m in CHALLENGE_MARKERS if m in low), None)
            if status in (401, 403, 429):
                rec["outcome"] = "blocked_http"
            elif status and status >= 400:
                rec["outcome"] = "http_error"
            elif marker and len(text) < 4000:
                rec["outcome"] = "blocked_challenge"
                rec["challenge_marker"] = marker
            elif len(text.strip()) < 200:
                rec["outcome"] = "rendered_empty"
            else:
                rec["outcome"] = "read"
            if text:
                h = hashlib.sha256(text.encode("utf-8")).hexdigest()
                rec["text_sha256"] = h
                (self.out_dir / "raw" / f"{label}.txt").write_text(text, encoding="utf-8")
        except Exception as e:
            rec["outcome"] = "error"
            rec["error"] = f"{type(e).__name__}: {str(e)[:300]}"
        finally:
            self._last[host] = time.time()
            page.close()
        return self._log(rec)

    def _log(self, rec: dict) -> dict:
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"[{rec['outcome']}] {rec.get('status')} {rec['label']} {rec['url']}")
        return rec
