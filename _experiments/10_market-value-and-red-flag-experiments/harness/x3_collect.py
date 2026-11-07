"""X3: collect MCF postings with monthly salary via the local fetch-render service.
Usage: python x3_collect.py OUT_JSON
Rule (protocol X3): per term, newest-sorted pages 0 and 1, first 5 postings with a Monthly range.
"""
import json, re, sys, time, urllib.parse, urllib.request

TERMS = ["accountant", "software engineer", "staff nurse", "warehouse supervisor",
         "marketing executive", "customer service officer", "mechanical engineer",
         "cook", "human resource executive", "administrative assistant",
         "sales executive", "data analyst"]
FETCH = "http://localhost:8080/fetch"
TOKEN = "local-dev-token"
SAL = re.compile(r"^\$([\d,]+)to\$([\d,]+)$")


def fetch(url):
    body = json.dumps({"url": url, "mode": "render", "settle_ms": 6000}).encode()
    req = urllib.request.Request(FETCH, body, {"Content-Type": "application/json",
                                               "Authorization": "Bearer " + TOKEN})
    with urllib.request.urlopen(req, timeout=150) as r:
        return json.load(r)


def parse(text):
    i = text.find("jobs found")
    lines = [l.strip() for l in text[i:].splitlines() if l.strip()]
    out = []
    for k, l in enumerate(lines):
        m = SAL.match(l)
        if not m or k + 1 >= len(lines) or lines[k + 1] != "Monthly" or k < 10:
            continue
        posted, apps, skills = lines[k - 1], lines[k - 2], lines[k - 3]
        function, seniority, employment, location, title = lines[k-4], lines[k-5], lines[k-6], lines[k-7], lines[k-8]
        employer = lines[k - 9]
        if employer.startswith("TYPICALLY REPLIES"):
            employer = lines[k - 10]
        if not posted.startswith("Posted"):
            continue
        out.append(dict(employer=employer, title=title, location=location, employment_type=employment,
                        seniority=seniority, function=function, posted=posted,
                        salary_min=int(m.group(1).replace(",", "")), salary_max=int(m.group(2).replace(",", ""))))
    return out


def main(out):
    results = {}
    for term in TERMS:
        found = []
        for page in (0, 1):
            url = ("https://www.mycareersfuture.gov.sg/search?search=%s&sortBy=new_posting_date&page=%d"
                   % (urllib.parse.quote(term), page))
            try:
                d = fetch(url)
                found += parse(d["text"])
            except Exception as e:
                print("ERR", term, page, e)
            time.sleep(3)
            if len(found) >= 5:
                break
        results[term] = [dict(f, term=term) for f in found[:5]]
        print(term, len(results[term]), flush=True)
    json.dump(results, open(out, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
