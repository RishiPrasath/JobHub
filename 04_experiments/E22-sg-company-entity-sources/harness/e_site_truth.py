"""E22 Part E: read each brand's own home page and one privacy/terms page (Patchright,
real Chrome, headed) and extract stated legal entity names and UEN-shaped strings."""
import json, re, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from patchright_reader import Reader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "runs/2026-11-21-run-001/outputs/site_truth"
sample = json.loads((ROOT / "data/sample.json").read_text(encoding="utf-8"))

NAME_RE = re.compile(r"\b([A-Z][A-Za-z0-9&.,'()\- ]{1,80}?\b(?:PTE\.?\s*LTD\.?|Pte\.?\s*Ltd\.?|LIMITED|Limited|Private Limited|PRIVATE LIMITED))")
UEN_RE = re.compile(r"\b((?:19|20)\d{7}[A-Z]|[TSR]\d{2}[A-Z]{2}\d{4}[A-Z]|\d{8}[A-Z])\b")
LINK_WORDS = ("privacy", "terms", "legal", "data protection", "pdpa")

def extract(text):
    names = sorted({re.sub(r"\s+", " ", m).strip(" ,.(") for m in NAME_RE.findall(text)})
    uens = sorted(set(UEN_RE.findall(text)))
    return names[:40], uens[:20]

results = []
with Reader(OUT) as r:
    for b in sample["brands"]:
        row = {"id": b["id"], "brand": b["brand"], "home": b["home"]}
        rec = r.read(b["home"], f"{b['id']}-home")
        row["home_outcome"] = rec["outcome"]
        txt_path = OUT / "raw" / f"{b['id']}-home.txt"
        texts = [txt_path.read_text(encoding="utf-8")] if txt_path.exists() else []
        # find a privacy/terms link on the rendered page
        link = None
        if rec["outcome"] == "read":
            page = r._ctx.new_page()
            try:
                page.goto(b["home"], wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(4000)
                links = page.evaluate("""() => [...document.querySelectorAll('a[href]')].map(a => [a.innerText.trim().toLowerCase(), a.href])""")
                for word in LINK_WORDS:
                    for t, h in links:
                        if word in t and h.startswith("http"):
                            link = h; break
                    if link: break
            except Exception as e:
                row["link_error"] = str(e)[:200]
            finally:
                page.close()
                r._last[rec.get("final_url", b["home"]).split("/")[2]] = time.time()
        row["policy_url"] = link
        if link:
            rec2 = r.read(link, f"{b['id']}-policy")
            row["policy_outcome"] = rec2["outcome"]
            p = OUT / "raw" / f"{b['id']}-policy.txt"
            if p.exists():
                texts.append(p.read_text(encoding="utf-8"))
        names, uens = extract("\n".join(texts))
        row["stated_names"], row["stated_uens"] = names, uens
        results.append(row)
        print(b["brand"], "|", names[:6], uens[:4])
(OUT / "site_truth_extract.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
