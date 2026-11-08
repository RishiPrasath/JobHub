"""Search MyCareersFuture in the user's browser through Kimi WebBridge and print the job links found.

Usage: python mcf_search.py <session> "<search term>" [--sort new_posting_date|relevancy]
One session per persona = one browser tab group. Read-only: opens a public search page and reads the job cards.
No login, no clicking, no applying. Waits between page loads. Stops with an error JSON on any non-search page.
"""
import json, sys, time, urllib.parse, urllib.request

DAEMON = "http://127.0.0.1:10086/command"
JS = r"""(async () => {
  for (let i = 0; i < 20 && !document.querySelector('a[href*="/job/"]'); i++) await new Promise(r => setTimeout(r, 500));
  const seen = new Set(), out = [];
  for (const a of document.querySelectorAll('a[href*="/job/"]')) {
    const h = a.href.split('?')[0];
    if (seen.has(h)) continue; seen.add(h);
    const card = a.closest('[data-testid="job-card"]') || a.parentElement;
    out.push({url: h, text: (card ? card.innerText : a.innerText).replace(/\s+/g, ' ').slice(0, 260)});
  }
  return JSON.stringify({title: document.title, final_url: location.href, n: out.length, jobs: out.slice(0, 20)});
})()"""


def call(session, action, args):
    body = json.dumps({"action": action, "args": args, "session": session}).encode("utf-8")
    req = urllib.request.Request(DAEMON, body, {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=90))


def main():
    sys.stdout.reconfigure(encoding="utf-8")   # job titles contain emoji; Windows defaults to cp1252
    session, term = sys.argv[1], sys.argv[2]
    sort = sys.argv[sys.argv.index("--sort") + 1] if "--sort" in sys.argv else "new_posting_date"
    url = "https://www.mycareersfuture.gov.sg/search?search=%s&sortBy=%s&page=0" % (urllib.parse.quote(term), sort)
    try:
        nav = call(session, "navigate", {"url": url, "group_title": "JobHub job search: " + session.replace("jobhub-", "")})
        if not nav.get("ok"):
            print(json.dumps({"error": "navigate_failed", "detail": nav})); return
        res = call(session, "evaluate", {"code": JS})
        data = json.loads(res["data"]["value"])
    except Exception as e:
        print(json.dumps({"error": type(e).__name__, "detail": str(e)[:200]})); return
    if "mycareersfuture.gov.sg/search" not in data.get("final_url", ""):
        print(json.dumps({"error": "not_a_search_page", "final_url": data.get("final_url"), "title": data.get("title")})); return
    print(json.dumps({"term": term, "search_url": url, "n_found": data["n"], "jobs": data["jobs"]}, ensure_ascii=False))
    time.sleep(3)   # pause before the caller's next page load


main()
