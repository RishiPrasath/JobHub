"""Survey candidate tools via the public GitHub REST API (unauthenticated)."""
import json, urllib.request, sys
REPOS = """microsoft/playwright puppeteer/puppeteer SeleniumHQ/selenium chromedp/chromedp go-rod/rod
browserless/browserless steel-dev/steel-browser lightpanda-io/browser apify/crawlee scrapy/scrapy
D4Vinci/Scrapling unclecode/crawl4ai firecrawl/firecrawl jina-ai/reader ScrapeGraphAI/Scrapegraph-ai
encode/httpx lexiforest/curl_cffi rushter/selectolax adbar/trafilatura browser-use/browser-use
browserbase/stagehand microsoft/playwright-mcp Kaliiiiiiiiii-Vinyl/patchright daijro/camoufox
ultrafunkamsterdam/nodriver ultrafunkamsterdam/undetected-chromedriver scrapy-plugins/scrapy-playwright
projectdiscovery/katana mozilla/readability microsoft/markitdown""".split()
out = []
for r in REPOS:
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{r}", headers={"User-Agent": "jobhub-research"})
        d = json.load(urllib.request.urlopen(req, timeout=20))
        out.append(dict(repo=r, stars=d["stargazers_count"], license=(d.get("license") or {}).get("spdx_id"),
                        lang=d.get("language"), pushed=d["pushed_at"][:10], archived=d["archived"],
                        open_issues=d["open_issues_count"], desc=(d.get("description") or "")[:110]))
    except Exception as e:
        out.append(dict(repo=r, error=str(e)[:80]))
json.dump(out, open("outputs/s1_github_survey.json", "w", encoding="utf-8"), indent=1)
for o in out: print(o)
