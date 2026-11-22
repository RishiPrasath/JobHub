"""E22 Part B step 3: fetch the 3 notice PDFs picked in step 2.

assets.egazette.gov.sg returns HTTP 403 (S3 AccessDenied) for /robots.txt, i.e. there is no
robots file. Step 2 treated that as disallow-all (Python's legacy rule). RFC 9309 s.2.3.1.3
says a 4xx robots response means the crawler MAY access the server, and the eGazette terms
(clause 11) expressly allow non-abusive automated extraction of e-Gazettes. So the 3 PDFs
are fetched once each, 5 s apart. Text is extracted, entity names and UENs are checked in ACRA."""
import io, json, re, sys, time, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from a_acra_match import call, slim
import pypdf
OUT = Path(__file__).resolve().parents[1] / "runs/2026-11-21-run-001/outputs/gazette"
UEN_RE = re.compile(r"\b((?:19|20)\d{7}[A-Z]|[TSR]\d{2}[A-Z]{2}\d{4}[A-Z]|\d{8}[A-Z])\b")
links = json.loads((OUT / "browse_links.json").read_text(encoding="utf-8"))
picks = [l for l in links if re.search(r"Companies Act.*(344|Wind|Liquidat)|Insolvency", l[0], re.I)][:3]
res = []
for i, (title, url) in enumerate(picks):
    if i: time.sleep(5)
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "JobHubResearch"}), timeout=60) as r:
        data = r.read(); status = r.status
    text = "\n".join(p.extract_text() or "" for p in pypdf.PdfReader(io.BytesIO(data)).pages)
    (OUT / "raw" / f"notice-{i+1}.txt").write_text(text, encoding="utf-8")
    uens = sorted(set(UEN_RE.findall(text)))
    checks = []
    for u in uens[:5]:  # check at most 5 UENs per notice in ACRA
        recs = call({"filters": json.dumps({"uen": u})}).get("records", [])
        checks.append({"uen": u, "acra": [slim(x) for x in recs]})
    res.append({"title": title.split("\n")[0], "url": url, "status": status, "bytes": len(data), "chars": len(text),
                "uens_in_notice": len(uens), "acra_checks": checks})
    print(title.split("\n")[0], status, len(data), "uens:", len(uens), [(c["uen"], c["acra"][0]["entity_name"] if c["acra"] else None, c["acra"][0]["uen_status_desc"] if c["acra"] else None) for c in checks])
(OUT / "notices.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
