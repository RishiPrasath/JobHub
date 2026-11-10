"""Scoped format and accessibility check for resume files (DOCX and PDF). Code only, no model.

It reports structural features that some parsers handle badly and says why. It never says a resume
is "ATS-safe" and never predicts how any particular system will read a file.
Run: python harness/format_check.py   -> outputs/format_check/results.json
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

import fitz

sys.path.insert(0, str(Path(__file__).parent))
from common import DATA, OUTPUTS  # noqa: E402

CAVEAT = ("Parsers differ between systems. This check lists structural features that some parsers handle badly; "
          "it does not tell you how any particular system will read your file.")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE = re.compile(r"(\+?\d[\d\s().-]{7,}\d)")
SECTIONS = re.compile(r"^\s*(summary|profile|objective|experience|work experience|employment( history)?|education|skills|"
                      r"certifications?|projects?|languages)\s*:?\s*$", re.I)
BANNED = re.compile(r"ats[\s-]*(safe|friendly|proof|compliant|ready|optimi[sz]ed|approved)|will pass|guarantee|"
                    r"passes? (the )?ats|beat(s)? the ats|100\s*%\s*(compatible|safe)", re.I)

WHY = {
    "image_text": "Text inside a picture is not text to a parser. Words, dates or contact details in an image may be missing from what a system reads.",
    "table_core": "Some parsers read table cells out of order or skip them. Core content (jobs, dates, duties) held in a table may be mixed up or lost.",
    "header_contact": "Some parsers ignore page headers. Contact details kept only in the header may not be read.",
    "footer_contact": "Some parsers ignore page footers. Contact details kept only in the footer may not be read.",
    "text_box": "Text in a text box sits outside the main text flow. Some parsers skip it or read it out of order.",
    "multi_column": "Columns can be read straight across the page instead of down each column, which mixes the order of your content.",
    "non_selectable": "The page has no selectable text (it looks like a scan or picture). A parser would have nothing to read without text recognition.",
    "missing_headings": "No standard section headings found. Parsers and screen readers use headings such as Experience and Education to find sections.",
}
FIX = {
    "image_text": "Put the words in normal text.", "table_core": "Use plain paragraphs and lists for jobs and dates.",
    "header_contact": "Repeat contact details in the main body.", "footer_contact": "Repeat contact details in the main body.",
    "text_box": "Move the text into the main body.", "multi_column": "Use a single column.",
    "non_selectable": "Export from the original document so the text is selectable.", "missing_headings": "Add headings such as Experience, Education and Skills.",
}


def finding(code, where):
    return {"code": code, "where": where, "why": WHY[code], "suggestion": FIX[code]}


# ---------------- DOCX ----------------
def check_docx(path: Path):
    f = []
    z = zipfile.ZipFile(path)
    names = z.namelist()
    doc = z.read("word/document.xml").decode("utf8", "ignore")
    body_text = " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", doc))
    # images in body
    if re.search(r"<w:drawing>.*?<pic:pic", doc, flags=re.S) or "<v:imagedata" in doc:
        f.append(finding("image_text", "body: picture found; any words inside it cannot be read as text"))
    # text boxes
    if "txbxContent" in doc:
        f.append(finding("text_box", "body: text box found"))
    # columns
    for m in re.finditer(r"<w:cols\b[^>]*>", doc):
        n = re.search(r'w:num="(\d+)"', m.group())
        if n and int(n.group(1)) >= 2:
            f.append(finding("multi_column", f"section with {n.group(1)} columns"))
            break
    # tables carrying core content
    tbls = re.findall(r"<w:tbl>.*?</w:tbl>", doc, flags=re.S)
    if tbls:
        ttxt = " ".join(" ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", t)) for t in tbls)
        total = len(body_text)
        if total and (len(ttxt) / total > 0.25 or EMAIL.search(ttxt) or PHONE.search(ttxt)):
            f.append(finding("table_core", f"table holds {len(ttxt)} of {total} characters of text"))
    # headers and footers
    for n in names:
        if re.fullmatch(r"word/header\d*\.xml", n) or re.fullmatch(r"word/footer\d*\.xml", n):
            t = " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", z.read(n).decode("utf8", "ignore")))
            if EMAIL.search(t) or PHONE.search(t):
                inbody = EMAIL.search(body_text) or PHONE.search(body_text)
                if not inbody:
                    f.append(finding("header_contact" if "header" in n else "footer_contact", f"{n}: email or phone only here"))
    # headings
    has_style = re.search(r'<w:pStyle w:val="Heading\d?"', doc) is not None
    paras = [" ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)) for p in re.findall(r"<w:p[ >].*?</w:p>", doc, flags=re.S)]
    labels = sum(1 for p in paras if SECTIONS.match(p))
    if not has_style and labels < 2:
        f.append(finding("missing_headings", "no heading styles and fewer than 2 standard section labels"))
    return f


# ---------------- PDF ----------------
def check_pdf(path: Path):
    f = []
    d = fitz.open(path)
    all_text, body_text = "", ""
    img_pages = []
    for pno, page in enumerate(d):
        W, H = page.rect.width, page.rect.height
        txt = page.get_text()
        all_text += txt
        imgs = page.get_images(full=True)
        cover = 0.0
        for im in imgs:
            for r in page.get_image_rects(im[0]):
                cover = max(cover, r.get_area() / (W * H))
        if len(txt.strip()) < 40 and cover > 0.5:
            f.append(finding("non_selectable", f"page {pno + 1}: image covers {cover:.0%} and almost no selectable text"))
        elif cover > 0.01:
            f.append(finding("image_text", f"page {pno + 1}: picture found; any words inside it cannot be read as text"))
        # blocks
        blocks = [b for b in page.get_text("blocks") if b[6] == 0 and len(b[4].strip()) > 25]
        left = [b for b in blocks if b[0] < 0.35 * W]
        right = [b for b in blocks if b[0] > 0.42 * W]
        overlap = any(l[1] < r[3] and r[1] < l[3] for l in left for r in right)
        if left and right and overlap and len(right) >= 1 and len(left) >= 1:
            f.append(finding("multi_column", f"page {pno + 1}: text blocks sit side by side"))
        # tables
        try:
            tabs = page.find_tables()
            for t in tabs.tables:
                cells = [c for row in t.extract() for c in row if c]
                if sum(len(c) for c in cells) > 0.25 * max(len(txt), 1) and len(t.extract()) >= 2:
                    f.append(finding("table_core", f"page {pno + 1}: ruled table holds much of the page text"))
                    break
        except Exception:
            pass
        # header and footer zones
        for (y0, y1, code) in ((0, 0.08 * H, "header_contact"), (0.93 * H, H, "footer_contact")):
            zone = " ".join(b[4] for b in page.get_text("blocks") if b[1] >= y0 and b[3] <= y1 + 1)
            mid = " ".join(b[4] for b in page.get_text("blocks") if b[1] > 0.08 * H and b[3] < 0.93 * H)
            if (EMAIL.search(zone) or PHONE.search(zone)) and not (EMAIL.search(mid) or PHONE.search(mid)):
                f.append(finding(code, f"page {pno + 1}: email or phone only in the page margin zone"))
        body_text += txt
    labels = sum(1 for ln in all_text.splitlines() if SECTIONS.match(ln))
    if len(all_text.strip()) >= 40 and labels < 2:
        f.append(finding("missing_headings", "fewer than 2 standard section labels found in the text"))
    # de-duplicate by code
    seen, out = set(), []
    for x in f:
        if x["code"] not in seen:
            seen.add(x["code"]); out.append(x)
    return out


def message_for(findings):
    if not findings:
        return "No structural problems were found by this check. " + CAVEAT
    return f"{len(findings)} structural feature(s) found that some parsers handle badly. " + CAVEAT


def run(stress: bool = False):
    gold = json.loads((DATA / "gold" / ("format_stress_gold.json" if stress else "format_gold.json")).read_text(encoding="utf-8"))
    res = {}
    for name in sorted(gold["files"]):
        p = DATA / ("format_stress" if stress else "format_fixtures") / name
        fs = check_docx(p) if name.endswith(".docx") else check_pdf(p)
        res[name] = {"findings": fs, "message": message_for(fs)}
    planted = found = 0
    false_flags = 0
    clean = 0
    missed, extra = [], []
    banned = []
    for name, g in gold["files"].items():
        codes = {x["code"] for x in res[name]["findings"]}
        for c in g["planted"]:
            planted += 1
            if c in codes:
                found += 1
            else:
                missed.append((name, c))
        if g["clean"]:
            clean += 1
            if codes:
                false_flags += 1; extra.append((name, sorted(codes)))
        else:
            for c in codes - set(g["planted"]):
                extra.append((name, c))
        txt = res[name]["message"] + " " + " ".join(x["why"] + " " + x["suggestion"] + " " + x["where"] for x in res[name]["findings"])
        if BANNED.search(txt):
            banned.append(name)
    summary = {"planted": planted, "found": found, "recall": round(found / planted, 3), "clean_files": clean,
               "clean_files_with_false_flags": false_flags, "missed": missed, "unplanted_extra_flags": extra,
               "files_with_banned_wording": banned, "caveat": CAVEAT, "format_proxy": gold.get("format_proxy", "None. Real DOCX and PDF files.")}
    od = OUTPUTS / ("format_check_stress_POSTHOC" if stress else "format_check")
    od.mkdir(parents=True, exist_ok=True)
    (od / "results.json").write_text(json.dumps({"summary": summary, "files": res}, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    run(stress="--stress" in sys.argv)
