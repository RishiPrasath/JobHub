"""E22 Part B step 2: from the eGazette browse page, open up to 3 recent Companies Act
s344/s344A (striking-off) notices and 1 winding-up notice if listed, extract entity names
and UENs, and check them in ACRA. Volume: under 8 page loads, 5 s apart."""
import json, re, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from patchright_reader import Reader
OUT = Path(__file__).resolve().parents[1] / "runs/2026-11-21-run-001/outputs/gazette"
UEN_RE = re.compile(r"\b((?:19|20)\d{7}[A-Z]|[TSR]\d{2}[A-Z]{2}\d{4}[A-Z]|\d{8}[A-Z])\b")

with Reader(OUT) as r:
    page = r._ctx.new_page()
    page.goto("https://www.egazette.gov.sg/egazette-browse/", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(6000)
    links = page.evaluate("""() => [...document.querySelectorAll('a[href]')].map(a => [a.innerText.trim(), a.href])""")
    page.close()
    r._last["www.egazette.gov.sg"] = time.time()
    (OUT / "browse_links.json").write_text(json.dumps(links, indent=1, ensure_ascii=False), encoding="utf-8")
    picks = [l for l in links if re.search(r"Companies Act.*(344|Wind|Liquidat)|Insolvency", l[0], re.I)][:3]
    print("picked:", picks)
    notices = []
    for i, (title, href) in enumerate(picks):
        rec = r.read(href, f"notice-{i+1}")
        p = OUT / "raw" / f"notice-{i+1}.txt"
        text = p.read_text(encoding="utf-8") if p.exists() else ""
        notices.append({"title": title, "url": href, "outcome": rec["outcome"], "final_url": rec.get("final_url"),
                        "uens": sorted(set(UEN_RE.findall(text))), "chars": len(text)})
(OUT / "notices.json").write_text(json.dumps(notices, indent=1, ensure_ascii=False), encoding="utf-8")
for n in notices: print(n["title"], n["outcome"], n["chars"], len(n["uens"]), n["uens"][:5], n["final_url"])
