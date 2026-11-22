"""Polite single-page reader built on Patchright, driving real Chrome headed.

Used by E22 (Singapore company entity sources, 2026-11-21). Patchright is a
Playwright-compatible fork. Here it is used only to render pages that need
JavaScript, on sources whose terms and robots.txt allow automated access.

Rules this reader enforces (AGENTS.md and the owner's instructions):
- robots.txt is read first; a disallowed URL is never fetched.
- At least MIN_DELAY seconds between requests to the same host, or the
  host's Crawl-delay if larger.
- An HTTP 401/403 or a bot-challenge, CAPTCHA or login page is recorded as
  "blocked" and NOT worked around. A 429 on a permitted page gets one slow
  retry after RETRY_WAIT seconds, then is recorded.
- Fresh throwaway browser profile: no logins, no saved cookies, no form
  submission. No credentials anywhere.

Usage:
    from patchright_reader import Reader
    with Reader(out_dir) as r:
        rec = r.read("https://example.com/terms", label="example-terms")
"""
from __future__ import annotations

import hashlib
import json
import tempfile
import time
import urllib.error
import urllib.request
import urllib.robotparser
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

READER_VERSION = "patchright-reader 0.1.0 (real Chrome, headed)"
ROBOTS_AGENT = "JobHubResearch"
MIN_DELAY = 5.0
RETRY_WAIT = 30.0
NAV_TIMEOUT_MS = 60_000
SETTLE_MS = 6_000
CHALLENGE_MARKERS = (
    "just a moment", "verify you are human", "are you a robot",
    "checking your browser", "captcha", "access denied", "request blocked",
    "unusual traffic", "press & hold", "attention required",
)
LOGIN_MARKERS = ("sign in to continue", "log in to continue", "please log in", "singpass login")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class Reader:
    def __init__(self, out_dir: Path, headless: bool = False):
        self.out_dir = Path(out_dir)
        (self.out_dir / "raw").mkdir(parents=True, exist_ok=True)
        self.headless = headless
        self._robots: dict = {}
        self._last: dict[str, float] = {}
        self.log_path = self.out_dir / "reads.jsonl"
        self.responses: list[dict] = []

    def __enter__(self):
        from patchright.sync_api import sync_playwright
        self._pw = sync_playwright().start()
        self._tmp = tempfile.TemporaryDirectory(prefix="jobhub-pr-")
        # Patchright's recommended setup: real Chrome, persistent context, no custom UA.
        self._ctx = self._pw.chromium.launch_persistent_context(
            user_data_dir=self._tmp.name, channel="chrome",
            headless=self.headless, no_viewport=True)
        return self

    def __exit__(self, *exc):
        try:
            self._ctx.close()
            self._pw.stop()
        finally:
            self._tmp.cleanup()

    def robots(self, url: str):
        u = urlparse(url)
        base = f"{u.scheme}://{u.netloc}"
        if base in self._robots:
            return self._robots[base]
        rp = urllib.robotparser.RobotFileParser()
        try:
            req = urllib.request.Request(base + "/robots.txt", headers={"User-Agent": ROBOTS_AGENT})
            with urllib.request.urlopen(req, timeout=20) as resp:
                body = resp.read().decode("utf-8", "replace")
            rp.parse(body.splitlines())
            note = f"robots.txt read ({len(body)} bytes)"
            (self.out_dir / "raw" / f"robots__{u.netloc}.txt").write_text(body, encoding="utf-8")
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                rp.disallow_all = True
                note = f"robots.txt HTTP {e.code}: treated as disallow all"
            else:
                rp.allow_all = True
                note = f"robots.txt HTTP {e.code}: no rules, allow"
        except Exception as e:
            rp = None
            note = f"robots.txt unreachable ({type(e).__name__}): not fetched"
        self._robots[base] = (rp, note)
        return rp, note

    def read(self, url: str, label: str, capture_json: str | None = None) -> dict:
        """Render url. If capture_json is a substring, JSON responses whose URL
        contains it are saved (to see which API a page calls)."""
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
        for attempt in (1, 2):
            wait = self._last.get(host, 0) + delay - time.time()
            if wait > 0:
                time.sleep(wait)
            self._attempt(url, label, rec, capture_json)
            self._last[host] = time.time()
            if rec.get("status") == 429 and attempt == 1:
                rec["retried_after_429"] = True
                time.sleep(RETRY_WAIT)
                continue
            break
        return self._log(rec)

    def _attempt(self, url, label, rec, capture_json):
        page = self._ctx.new_page()
        captured = []
        if capture_json:
            def on_resp(r):
                if capture_json in r.url and "json" in (r.headers.get("content-type") or ""):
                    try:
                        captured.append({"url": r.url, "status": r.status, "body": r.json()})
                    except Exception:
                        pass
            page.on("response", on_resp)
        try:
            resp = page.goto(url, wait_until="domcontentloaded", timeout=NAV_TIMEOUT_MS)
            page.wait_for_timeout(SETTLE_MS)
            status = resp.status if resp else None
            title = page.title()
            text = page.evaluate("() => document.body ? document.body.innerText : ''") or ""
            rec.update(status=status, final_url=page.url, title=title, text_chars=len(text))
            low = (title + " " + text[:3000]).lower()
            marker = next((m for m in CHALLENGE_MARKERS if m in low), None)
            login = next((m for m in LOGIN_MARKERS if m in low), None)
            if status in (401, 403, 429):
                rec["outcome"] = "blocked_http"
            elif status and status >= 400:
                rec["outcome"] = "http_error"
            elif marker and len(text) < 4000:
                rec["outcome"] = "blocked_challenge"
                rec["challenge_marker"] = marker
            elif login and len(text) < 4000:
                rec["outcome"] = "blocked_login"
                rec["login_marker"] = login
            elif len(text.strip()) < 200:
                rec["outcome"] = "rendered_empty"
            else:
                rec["outcome"] = "read"
            if text:
                rec["text_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
                (self.out_dir / "raw" / f"{label}.txt").write_text(text, encoding="utf-8")
            if captured:
                rec["captured_json"] = len(captured)
                (self.out_dir / "raw" / f"{label}__api.json").write_text(
                    json.dumps(captured, ensure_ascii=False, indent=1)[:2_000_000], encoding="utf-8")
        except Exception as e:
            rec["outcome"] = "error"
            rec["error"] = f"{type(e).__name__}: {str(e)[:300]}"
        finally:
            page.close()

    def _log(self, rec: dict) -> dict:
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"[{rec['outcome']}] {rec.get('status')} {rec['label']} {rec['url']}")
        return rec
