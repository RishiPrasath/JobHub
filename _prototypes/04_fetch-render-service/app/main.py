"""Fetch-and-render service: plain HTTP first, headless Chromium when the page needs JavaScript.

POST /fetch {"url": "...", "mode": "auto|plain|render", "wait_for": "css selector (optional)"}
GET  /health
Public pages only. robots.txt is honoured, private addresses are refused, user agent is honest.
"""
import asyncio, ipaddress, os, socket, time, urllib.parse, urllib.robotparser
from functools import lru_cache

import httpx
import trafilatura
from fastapi import FastAPI, Header, HTTPException
from playwright.async_api import async_playwright
from pydantic import BaseModel

UA = os.environ.get("FETCH_UA", "JobHubResearchBot/0.1 (+local research service)")
TOKEN = os.environ.get("FETCH_TOKEN", "")
MAX_CONCURRENT = int(os.environ.get("FETCH_CONCURRENCY", "3"))
THIN = int(os.environ.get("FETCH_THIN_CHARS", "200"))
PAGE_TIMEOUT_MS = int(os.environ.get("FETCH_PAGE_TIMEOUT_MS", "30000"))
IDLE_WAIT_MS = int(os.environ.get("FETCH_IDLE_WAIT_MS", "6000"))
MAX_CHARS = int(os.environ.get("FETCH_MAX_CHARS", "60000"))
BLOCKED_TYPES = {"image", "media", "font"}

app = FastAPI(title="fetch-render-service")
state = {}
robots_cache: dict = {}


class Req(BaseModel):
    url: str
    mode: str = "auto"
    wait_for: str | None = None
    settle_ms: int = 0


@lru_cache(maxsize=2048)
def host_is_public(host: str) -> bool:
    try:
        infos = socket.getaddrinfo(host, None)
    except OSError:
        return False
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast:
            return False
    return True


def check_url(url: str) -> urllib.parse.ParseResult:
    p = urllib.parse.urlparse(url)
    if p.scheme not in ("http", "https") or not p.hostname:
        raise HTTPException(400, "only http(s) URLs are allowed")
    if not host_is_public(p.hostname):
        raise HTTPException(400, "host is not a public address")
    return p


async def robots_ok(client: httpx.AsyncClient, p: urllib.parse.ParseResult, url: str) -> bool:
    key = f"{p.scheme}://{p.netloc}"
    hit = robots_cache.get(key)
    if not hit or time.time() - hit[0] > 600:
        rp = urllib.robotparser.RobotFileParser()
        try:
            r = await client.get(key + "/robots.txt", timeout=10)
            rp.parse(r.text.splitlines()) if r.status_code < 400 else rp.parse([])
        except Exception:
            rp.parse([])
        hit = robots_cache[key] = (time.time(), rp)
    return hit[1].can_fetch(UA, url)


def extract(html: str) -> str:
    return (trafilatura.extract(html, include_links=False) or "").strip()


async def plain(client: httpx.AsyncClient, url: str):
    r = await client.get(url, timeout=20)
    return r.status_code, extract(r.text), str(r.url)


async def render(url: str, wait_for: str | None, settle_ms: int):
    ctx = await state["browser"].new_context(user_agent=UA)
    try:
        async def gate(route):
            req = route.request
            if req.resource_type in BLOCKED_TYPES:
                return await route.abort()
            h = urllib.parse.urlparse(req.url).hostname
            if h and not host_is_public(h):
                return await route.abort()
            await route.continue_()
        await ctx.route("**/*", gate)
        page = await ctx.new_page()
        resp = await page.goto(url, timeout=PAGE_TIMEOUT_MS, wait_until="domcontentloaded")
        try:
            await page.wait_for_load_state("networkidle", timeout=IDLE_WAIT_MS)
        except Exception:
            pass
        if wait_for:
            try:
                await page.wait_for_selector(wait_for, timeout=IDLE_WAIT_MS)
            except Exception:
                pass
        if settle_ms:
            await page.wait_for_timeout(min(settle_ms, 10000))
        html = await page.content()
        text = extract(html)
        body = (await page.inner_text("body")).strip()
        # trafilatura drops boilerplate; fall back to the full visible text when it finds little
        out = text if len(text) >= max(THIN, len(body) // 4) else body
        return (resp.status if resp else 0), out, page.url
    finally:
        await ctx.close()


@app.on_event("startup")
async def start():
    state["pw"] = await async_playwright().start()
    state["browser"] = await state["pw"].chromium.launch(args=["--disable-dev-shm-usage"])
    state["sem"] = asyncio.Semaphore(MAX_CONCURRENT)
    state["client"] = httpx.AsyncClient(headers={"User-Agent": UA}, follow_redirects=True)


@app.on_event("shutdown")
async def stop():
    await state["browser"].close()
    await state["pw"].stop()
    await state["client"].aclose()


@app.get("/health")
async def health():
    return {"ok": True, "browser_connected": state["browser"].is_connected()}


@app.post("/fetch")
async def fetch(req: Req, authorization: str | None = Header(default=None)):
    if TOKEN and authorization != f"Bearer {TOKEN}":
        raise HTTPException(401, "bad token")
    if req.mode not in ("auto", "plain", "render"):
        raise HTTPException(400, "mode must be auto, plain or render")
    p = check_url(req.url)
    client = state["client"]
    if not await robots_ok(client, p, req.url):
        return {"url": req.url, "status": "blocked_by_robots", "tier": None, "text": ""}
    t0 = time.time()
    tier, code, text, final = None, 0, "", req.url
    try:
        if req.mode in ("auto", "plain"):
            code, text, final = await plain(client, req.url)
            tier = "plain"
        if req.mode == "render" or (req.mode == "auto" and len(text) < THIN):
            async with state["sem"]:
                code, text, final = await render(req.url, req.wait_for, req.settle_ms)
            tier = "render"
    except HTTPException:
        raise
    except Exception as e:
        return {"url": req.url, "status": "error", "tier": tier, "error": str(e)[:200],
                "seconds": round(time.time() - t0, 2), "text": ""}
    if final != req.url and not host_is_public(urllib.parse.urlparse(final).hostname or ""):
        return {"url": req.url, "status": "error", "error": "redirected to a non-public host", "text": ""}
    return {"url": req.url, "final_url": final, "http": code, "tier": tier,
            "status": "ok" if len(text) >= THIN else "thin", "chars": len(text),
            "seconds": round(time.time() - t0, 2), "text": text[:MAX_CHARS]}
