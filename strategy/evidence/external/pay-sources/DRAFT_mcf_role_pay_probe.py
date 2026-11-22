"""DRAFT feasibility probe: average posted pay for a role on MyCareersFuture (MCF).

NOT FOR SHIPPING. MCF terms (read 2026-11-21) bar storing, reproducing, caching or
transmitting site content without written permission from SWDA. This probe keeps
only aggregate numbers in memory and prints them; it never writes postings to disk.

How it works (verified 2026-11-21 in a real browser): the search page
https://www.mycareersfuture.gov.sg/search?search=<role> calls the site's own
POST https://api.mycareersfuture.gov.sg/v2/search?limit=<n>&page=<p> with JSON
body {"search": "<role>"} (a sortBy value of "relevancy" is rejected; omit it).
Each result carries salary.minimum, salary.maximum, salary.type.salaryType.
We open the search page with Playwright/Patchright and run that same request from
the page, 3 s between pages, max 2 pages of 100 per role. robots.txt allows "*".
No CAPTCHA or block evasion: if a non-200 comes back, stop.

The 2026-11-21 run was executed as the equivalent JS in Claude's built-in browser
(the cloud and device shells have no internet). This Python file has not been run.
"""
from __future__ import annotations
import statistics, sys, time
from playwright.sync_api import sync_playwright  # or: from patchright.sync_api import ...

JS = """async ({q, page, limit}) => {
  const r = await fetch(`https://api.mycareersfuture.gov.sg/v2/search?limit=${limit}&page=${page}`,
    {method: 'POST', credentials: 'include', headers: {'content-type': 'application/json'},
     body: JSON.stringify({search: q})});
  if (r.status !== 200) return {status: r.status};
  const j = await r.json();
  // Return only title + salary numbers; nothing else leaves the page.
  return {status: 200, total: j.total, rows: j.results.map(x => [
    (x.title || '').toLowerCase(), x.salary?.minimum ?? null, x.salary?.maximum ?? null,
    x.salary?.type?.salaryType ?? null])};
}"""

def stats(xs):
    return {"n": len(xs), "min": min(xs), "max": max(xs), "mean": round(statistics.mean(xs)),
            "median": statistics.median(xs)} if xs else {"n": 0}

def aggregate(rows, q):
    words = q.lower().split()
    matched = [r for r in rows if all(w in r[0] for w in words)]   # title must contain every word
    missing = sum(1 for r in matched if r[1] is None or r[2] is None)
    good = [r for r in matched if r[3] == "Monthly" and r[1] and r[2]
            and 500 <= r[1] <= r[2] <= 60000]
    return {"role": q, "fetched": len(rows), "title_matched": len(matched), "omit_salary": missing,
            "excluded_outliers_or_non_monthly": len(matched) - missing - len(good),
            "salary_min": stats([r[1] for r in good]), "salary_max": stats([r[2] for r in good]),
            "midpoint": stats([(r[1] + r[2]) / 2 for r in good])}

def run(roles, max_pages=2, limit=100):
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        for q in roles:
            pg.goto(f"https://www.mycareersfuture.gov.sg/search?search={q.replace(' ', '%20')}")
            rows, total = [], None
            for page in range(max_pages):
                res = pg.evaluate(JS, {"q": q, "page": page, "limit": limit})
                if res["status"] != 200:
                    print(f"{q}: HTTP {res['status']}, stopping", file=sys.stderr); break
                total = res["total"]; rows += res["rows"]
                if len(res["rows"]) < limit: break
                time.sleep(3)
            print({"api_total": total, **aggregate(rows, q)})
            del rows
            time.sleep(5)
        b.close()

if __name__ == "__main__":
    run(sys.argv[1:] or ["software engineer", "data analyst", "accountant", "staff nurse", "hr executive"])
