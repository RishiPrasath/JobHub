"""Generate the 16 synthetic resume files for the E19 format and accessibility check.

Real DOCX files are written with python-docx and real PDF files with PyMuPDF. All content is
synthetic (fictional names, example.com addresses, 555 phone numbers).
Run: python harness/make_format_fixtures.py   (from the experiment folder)
Writes data/format_fixtures/*.docx|pdf and data/gold/format_gold.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import fitz
from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "data" / "format_fixtures"
OUT.mkdir(parents=True, exist_ok=True)
TMP = HERE / "data" / "format_fixtures" / "_tmp"
TMP.mkdir(exist_ok=True)

PEOPLE = [
    ("Sam Lee", "sam.lee@example.com", "+65 5550 0101"),
    ("Mei Tan", "mei.tan@example.com", "+65 5550 0102"),
    ("Ravi Kumar", "ravi.kumar@example.com", "+65 5550 0103"),
    ("Aisha Rahman", "aisha.rahman@example.com", "+65 5550 0104"),
    ("Joel Chua", "joel.chua@example.com", "+65 5550 0105"),
    ("Hui Min Goh", "huimin.goh@example.com", "+65 5550 0106"),
    ("Daniel Teo", "daniel.teo@example.com", "+65 5550 0107"),
    ("Nur Aini", "nur.aini@example.com", "+65 5550 0108"),
    ("Kevin Lau", "kevin.lau@example.com", "+65 5550 0109"),
    ("Grace Ong", "grace.ong@example.com", "+65 5550 0110"),
    ("Farid Hamid", "farid.hamid@example.com", "+65 5550 0111"),
    ("Li Ting Sim", "liting.sim@example.com", "+65 5550 0112"),
    ("Marcus Yeo", "marcus.yeo@example.com", "+65 5550 0113"),
    ("Deepa Menon", "deepa.menon@example.com", "+65 5550 0114"),
    ("Ben Foo", "ben.foo@example.com", "+65 5550 0115"),
    ("Chloe Lim", "chloe.lim@example.com", "+65 5550 0116"),
]


def content(i: int):
    name, email, phone = PEOPLE[i]
    return {
        "name": name, "email": email, "phone": phone,
        "summary": "Reliable coordinator with three years of customer-facing and operations work.",
        "jobs": [
            ("Operations Assistant, Northgate Supplies Pte Ltd, 2023 to present",
             ["Prepared daily delivery schedules for the team.", "Answered customer questions by phone and email."]),
            ("Sales Assistant, Eastbay Stationers, 2021 to 2023",
             ["Served customers and operated the till.", "Restocked shelves and counted stock each week."]),
        ],
        "edu": "Diploma in Business Studies, Westlake Polytechnic, 2018 to 2021",
        "skills": "Excel (basic), Word, scheduling, customer service",
    }


def font(size, bold=False):
    return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf", size)


def text_png(lines, path, w=900, size=26):
    h = 20 + len(lines) * (size + 12)
    im = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(im)
    y = 10
    for ln in lines:
        d.text((12, y), ln, fill="black", font=font(size))
        y += size + 12
    im.save(path)
    return path


def body_lines(c):
    out = ["Summary", c["summary"], "Experience"]
    for title, bullets in c["jobs"]:
        out.append(title)
        out += ["- " + b for b in bullets]
    out += ["Education", c["edu"], "Skills", c["skills"]]
    return out


# ---------------- DOCX builders ----------------
def docx_standard(c, contact_in_body=True, headings=True, doc=None):
    d = doc or Document()
    if contact_in_body:
        d.add_heading(c["name"], 0)
        d.add_paragraph(f'{c["email"]} | {c["phone"]} | Singapore')
    def h(t):
        if headings:
            d.add_heading(t, 1)
        else:
            d.add_paragraph(t)
    h("Summary") if headings else None
    d.add_paragraph(c["summary"])
    if headings:
        h("Experience")
    for title, bullets in c["jobs"]:
        p = d.add_paragraph(); r = p.add_run(title); r.bold = headings
        for b in bullets:
            d.add_paragraph(b, style="List Bullet")
    if headings:
        h("Education")
    d.add_paragraph(c["edu"])
    if headings:
        h("Skills")
    d.add_paragraph(c["skills"])
    return d


def make_docs():
    specs = {}
    # F01 image text (experience as picture)
    c = content(0); d = Document()
    d.add_heading(c["name"], 0); d.add_paragraph(f'{c["email"]} | {c["phone"]}')
    d.add_heading("Experience", 1)
    lines = []
    for t, bl in c["jobs"]:
        lines.append(t); lines += ["- " + b for b in bl]
    d.add_picture(str(text_png(lines, TMP / "f01.png")), width=Inches(5.8))
    d.add_heading("Education", 1); d.add_paragraph(c["edu"])
    d.add_heading("Skills", 1); d.add_paragraph(c["skills"])
    d.save(OUT / "F01_docx_experience_as_image.docx"); specs["F01_docx_experience_as_image.docx"] = ["image_text"]
    # F02 table carrying core content
    c = content(1); d = Document()
    d.add_heading(c["name"], 0); d.add_paragraph(f'{c["email"]} | {c["phone"]}')
    d.add_heading("Experience", 1)
    t = d.add_table(rows=2, cols=2); t.style = "Table Grid"
    for r, (title, bl) in enumerate(c["jobs"]):
        t.cell(r, 0).text = title.split(",", 2)[-1].strip()
        t.cell(r, 1).text = title.split(",")[0] + ": " + " ".join(bl)
    d.add_heading("Education", 1); d.add_paragraph(c["edu"])
    d.add_heading("Skills", 1); d.add_paragraph(c["skills"])
    d.save(OUT / "F02_docx_experience_in_table.docx"); specs["F02_docx_experience_in_table.docx"] = ["table_core"]
    # F03 header holds contact
    c = content(2); d = Document()
    d.sections[0].header.paragraphs[0].text = f'{c["name"]}  {c["email"]}  {c["phone"]}'
    docx_standard(c, contact_in_body=False, doc=d)
    d.save(OUT / "F03_docx_contact_in_header.docx"); specs["F03_docx_contact_in_header.docx"] = ["header_contact"]
    # F04 footer holds contact
    c = content(3); d = Document()
    d.add_heading(c["name"], 0)
    d.sections[0].footer.paragraphs[0].text = f'{c["email"]}  {c["phone"]}'
    docx_standard(c, contact_in_body=False, doc=d)
    d.save(OUT / "F04_docx_contact_in_footer.docx"); specs["F04_docx_contact_in_footer.docx"] = ["footer_contact"]
    # F05 text box (VML) holding skills and contact
    c = content(4); d = Document()
    d.add_heading(c["name"], 0)
    p = d.add_paragraph()
    xml = (
        '<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:v="urn:schemas-microsoft-com:vml"><w:pict><v:shape type="#_x0000_t202" '
        'style="width:200pt;height:70pt" stroked="f"><v:textbox><w:txbxContent><w:p><w:r><w:t>'
        f'{c["email"]} | {c["phone"]}</w:t></w:r></w:p><w:p><w:r><w:t>Skills: {c["skills"]}</w:t></w:r></w:p>'
        '</w:txbxContent></v:textbox></v:shape></w:pict></w:r>')
    p._p.append(parse_xml(xml))
    docx_standard(c, contact_in_body=False, doc=d)
    d.save(OUT / "F05_docx_text_box.docx"); specs["F05_docx_text_box.docx"] = ["text_box"]
    # F06 two columns
    c = content(5); d = Document()
    sect = d.sections[0]._sectPr
    cols = OxmlElement("w:cols"); cols.set(qn("w:num"), "2"); cols.set(qn("w:space"), "720"); sect.append(cols)
    docx_standard(c, doc=d)
    d.save(OUT / "F06_docx_two_columns.docx"); specs["F06_docx_two_columns.docx"] = ["multi_column"]
    # F07 no headings
    c = content(6)
    d = docx_standard(c, headings=False)
    d.save(OUT / "F07_docx_no_headings.docx"); specs["F07_docx_no_headings.docx"] = ["missing_headings"]
    # C01 clean docx
    c = content(12); d = docx_standard(c)
    d.save(OUT / "C01_docx_clean.docx"); specs["C01_docx_clean.docx"] = []
    # C02 clean docx with harmless header (name only) and footer (page label), pipe-separated skills
    c = content(13); d = Document()
    d.sections[0].header.paragraphs[0].text = c["name"]
    d.sections[0].footer.paragraphs[0].text = "Page 1 of 2"
    c2 = dict(c); c2["skills"] = "Excel (basic) | Word | scheduling | customer service"
    docx_standard(c2, doc=d)
    d.save(OUT / "C02_docx_clean_header_footer.docx"); specs["C02_docx_clean_header_footer.docx"] = []
    return specs


# ---------------- PDF builders ----------------
def pdf_text_page(page, c, x=54, y=60, width=480, contact=True, headings=True, size=10.5):
    if contact:
        page.insert_text((x, y), c["name"], fontsize=16, fontname="hebo"); y += 18
        page.insert_text((x, y), f'{c["email"]} | {c["phone"]} | Singapore', fontsize=size); y += 26
    for ln in body_lines(c):
        if ln in ("Summary", "Experience", "Education", "Skills"):
            if not headings:
                continue
            y += 6
            page.insert_text((x, y), ln, fontsize=12.5, fontname="hebo"); y += 16
        else:
            page.insert_text((x, y), ln, fontsize=size); y += 14
    return y


def make_pdfs():
    specs = {}
    # F08 non-selectable (image only)
    c = content(7)
    tmp = fitz.open(); pg = tmp.new_page(); pdf_text_page(pg, c)
    pix = pg.get_pixmap(dpi=110); tmp.close()
    d = fitz.open(); pg = d.new_page(); pg.insert_image(pg.rect, pixmap=pix)
    d.save(OUT / "F08_pdf_scanned_no_text_layer.pdf"); d.close(); specs["F08_pdf_scanned_no_text_layer.pdf"] = ["non_selectable"]
    # F09 contact block as image
    c = content(8); d = fitz.open(); pg = d.new_page()
    png = text_png([c["name"], f'{c["email"]} | {c["phone"]}'], TMP / "f09.png", w=700, size=24)
    pg.insert_image(fitz.Rect(54, 40, 54 + 350, 40 + 52), filename=str(png))
    pdf_text_page(pg, c, y=120, contact=False)
    d.save(OUT / "F09_pdf_contact_as_image.pdf"); d.close(); specs["F09_pdf_contact_as_image.pdf"] = ["image_text"]
    # F10 two columns
    c = content(9); d = fitz.open(); pg = d.new_page()
    pg.insert_text((54, 60), c["name"], fontsize=16, fontname="hebo")
    pg.insert_text((54, 78), f'{c["email"]} | {c["phone"]} | Singapore', fontsize=10.5)
    left = "Skills\n" + c["skills"] + "\n\nEducation\n" + c["edu"]
    right = "Experience\n" + "\n".join(t + "\n" + "\n".join("- " + b for b in bl) + "\n" for t, bl in c["jobs"])
    pg.insert_textbox(fitz.Rect(54, 110, 220, 700), left, fontsize=10.5)
    pg.insert_textbox(fitz.Rect(300, 110, 560, 700), right, fontsize=10.5)
    d.save(OUT / "F10_pdf_two_columns.pdf"); d.close(); specs["F10_pdf_two_columns.pdf"] = ["multi_column"]
    # F11 header holds contact
    c = content(10); d = fitz.open(); pg = d.new_page()
    pg.insert_text((54, 28), f'{c["name"]}  {c["email"]}  {c["phone"]}', fontsize=9.5)
    pdf_text_page(pg, c, y=90, contact=False)
    d.save(OUT / "F11_pdf_contact_in_header.pdf"); d.close(); specs["F11_pdf_contact_in_header.pdf"] = ["header_contact"]
    # F12 table with core content (ruled grid)
    c = content(11); d = fitz.open(); pg = d.new_page()
    pg.insert_text((54, 60), c["name"], fontsize=16, fontname="hebo")
    pg.insert_text((54, 78), f'{c["email"]} | {c["phone"]} | Singapore', fontsize=10.5)
    pg.insert_text((54, 108), "Experience", fontsize=12.5, fontname="hebo")
    y0 = 118
    for r, (title, bl) in enumerate(c["jobs"]):
        top = y0 + r * 80
        for cx0, cx1 in ((54, 200), (200, 540)):
            pg.draw_rect(fitz.Rect(cx0, top, cx1, top + 78), color=(0, 0, 0), width=0.8)
        pg.insert_textbox(fitz.Rect(58, top + 4, 198, top + 76), title.split(",", 2)[-1].strip(), fontsize=10)
        pg.insert_textbox(fitz.Rect(204, top + 4, 538, top + 76), title.split(",")[0] + "\n" + "\n".join("- " + b for b in bl), fontsize=10)
    pg.insert_text((54, 300), "Education", fontsize=12.5, fontname="hebo"); pg.insert_text((54, 316), c["edu"], fontsize=10.5)
    pg.insert_text((54, 340), "Skills", fontsize=12.5, fontname="hebo"); pg.insert_text((54, 356), c["skills"], fontsize=10.5)
    d.save(OUT / "F12_pdf_experience_in_table.pdf"); d.close(); specs["F12_pdf_experience_in_table.pdf"] = ["table_core"]
    # C03 clean single column pdf
    c = content(14); d = fitz.open(); pg = d.new_page(); pdf_text_page(pg, c)
    d.save(OUT / "C03_pdf_clean.pdf"); d.close(); specs["C03_pdf_clean.pdf"] = []
    # C04 clean pdf with a hyperlink, bullets and a second page
    c = content(15); d = fitz.open(); pg = d.new_page()
    y = pdf_text_page(pg, c)
    pg.insert_text((54, y + 14), "Portfolio: example.com/chloe", fontsize=10.5)
    pg.insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(54, y + 4, 200, y + 18), "uri": "https://example.com/chloe"})
    pg2 = d.new_page(); pg2.insert_text((54, 60), "Projects", fontsize=12.5, fontname="hebo")
    pg2.insert_text((54, 78), "- Stock count sheet for a school club (team of 3)", fontsize=10.5)
    d.save(OUT / "C04_pdf_clean_two_pages_link.pdf"); d.close(); specs["C04_pdf_clean_two_pages_link.pdf"] = []
    return specs


if __name__ == "__main__":
    specs = {}
    specs.update(make_docs()); specs.update(make_pdfs())
    gold = {
        "version": "format-gold-v1",
        "author": "AI specialist (Claude Sonnet 5.5), written 2026-11-10 with the fixture generator, before any check was run",
        "problem_codes": ["image_text", "table_core", "header_contact", "footer_contact", "text_box", "multi_column", "non_selectable", "missing_headings"],
        "format_proxy": "None. Real DOCX (python-docx) and real PDF (PyMuPDF) files.",
        "files": {k: {"planted": v, "clean": not v} for k, v in sorted(specs.items())},
    }
    (HERE / "data" / "gold" / "format_gold.json").write_text(json.dumps(gold, indent=1), encoding="utf-8")
    n = sum(len(v) for v in specs.values())
    print(len(specs), "files,", n, "planted problems,", sum(1 for v in specs.values() if not v), "clean")
