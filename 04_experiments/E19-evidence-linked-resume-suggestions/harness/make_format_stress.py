"""POST HOC stress set for the format check (written after the main format check had run on the frozen 16 files).

Ten extra files that vary the planted problems or add legitimate features, to see whether the rules generalise.
Gold for this set is written here, before the check is run on these files. Reported separately from the frozen result.
Writes data/format_stress/*.docx|pdf and data/gold/format_stress_gold.json.
"""
from __future__ import annotations

import json
from pathlib import Path

import fitz
from docx import Document
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from docx.shared import Inches
from PIL import Image, ImageDraw

import make_format_fixtures as mf

HERE = mf.HERE
OUT = HERE / "data" / "format_stress"
OUT.mkdir(parents=True, exist_ok=True)
TMP = OUT / "_tmp"
TMP.mkdir(exist_ok=True)
specs = {}


def logo(path):
    im = Image.new("RGB", (120, 60), "#2255aa")
    ImageDraw.Draw(im).rectangle((10, 10, 110, 50), outline="white")
    im.save(path)
    return path


# S01 docx: clean resume with a small logo image in the header (decorative). Planted: none (logo image is allowed); expect: no flag.
c = mf.content(0); d = Document()
d.sections[0].header.paragraphs[0].add_run().add_picture(str(logo(TMP / "l.png")), width=Inches(0.8))
mf.docx_standard(c, doc=d); d.save(OUT / "S01_docx_clean_logo_in_header.docx"); specs["S01_docx_clean_logo_in_header.docx"] = []
# S02 docx: section labels in plain capitals, no heading styles (headings present as text). Expect: no flag.
c = mf.content(1); d = Document(); d.add_paragraph(c["name"]); d.add_paragraph(f'{c["email"]} | {c["phone"]}')
for lbl, body in (("SUMMARY", c["summary"]), ("EXPERIENCE", "\n".join(t for t, _ in c["jobs"])), ("EDUCATION", c["edu"]), ("SKILLS", c["skills"])):
    d.add_paragraph(lbl); d.add_paragraph(body)
d.save(OUT / "S02_docx_clean_caps_labels_no_styles.docx"); specs["S02_docx_clean_caps_labels_no_styles.docx"] = []
# S03 docx: three columns. Planted multi_column.
c = mf.content(2); d = Document(); cols = OxmlElement("w:cols"); cols.set(qn("w:num"), "3"); d.sections[0]._sectPr.append(cols)
mf.docx_standard(c, doc=d); d.save(OUT / "S03_docx_three_columns.docx"); specs["S03_docx_three_columns.docx"] = ["multi_column"]
# S04 docx: whole resume inside one big table (layout table). Planted table_core.
c = mf.content(3); d = Document(); t = d.add_table(rows=1, cols=1)
cell = t.cell(0, 0); cell.text = c["name"] + "\n" + c["email"] + " | " + c["phone"] + "\nExperience\n" + "\n".join(x for x, _ in c["jobs"]) + "\nEducation\n" + c["edu"] + "\nSkills\n" + c["skills"]
d.save(OUT / "S04_docx_layout_table.docx"); specs["S04_docx_layout_table.docx"] = ["table_core"]
# S05 docx: contact details inside a text box located in the header. Planted text_box and header_contact.
c = mf.content(4); d = Document()
p = d.sections[0].header.paragraphs[0]
xml = ('<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:v="urn:schemas-microsoft-com:vml"><w:pict>'
       '<v:shape type="#_x0000_t202" style="width:200pt;height:30pt"><v:textbox><w:txbxContent><w:p><w:r><w:t>'
       f'{c["email"]} {c["phone"]}</w:t></w:r></w:p></w:txbxContent></v:textbox></v:shape></w:pict></w:r>')
p._p.append(parse_xml(xml))
mf.docx_standard(c, contact_in_body=False, doc=d); d.save(OUT / "S05_docx_textbox_in_header.docx")
specs["S05_docx_textbox_in_header.docx"] = ["header_contact", "text_box"]
# S06 pdf: three columns. Planted multi_column.
c = mf.content(5); d = fitz.open(); pg = d.new_page()
pg.insert_text((54, 60), c["name"], fontsize=16, fontname="hebo"); pg.insert_text((54, 78), f'{c["email"]} | {c["phone"]}', fontsize=10)
for x, txt in ((54, "Skills\n" + c["skills"]), (225, "Education\n" + c["edu"]), (395, "Experience\n" + "\n".join(t for t, _ in c["jobs"]))):
    pg.insert_textbox(fitz.Rect(x, 110, x + 150, 700), txt, fontsize=10)
d.save(OUT / "S06_pdf_three_columns.pdf"); d.close(); specs["S06_pdf_three_columns.pdf"] = ["multi_column"]
# S07 pdf: contact only in footer. Planted footer_contact.
c = mf.content(6); d = fitz.open(); pg = d.new_page(); mf.pdf_text_page(pg, c, contact=False, y=60)
pg.insert_text((54, 820), f'{c["name"]}  {c["email"]}  {c["phone"]}', fontsize=9)
d.save(OUT / "S07_pdf_contact_in_footer.pdf"); d.close(); specs["S07_pdf_contact_in_footer.pdf"] = ["footer_contact"]
# S08 pdf: clean resume with a small decorative logo image. Expect no flag (a logo is not a planted problem); a flag here is a false flag.
c = mf.content(7); d = fitz.open(); pg = d.new_page(); mf.pdf_text_page(pg, c)
pg.insert_image(fitz.Rect(480, 40, 540, 70), filename=str(logo(TMP / "l2.png")))
d.save(OUT / "S08_pdf_clean_logo.pdf"); d.close(); specs["S08_pdf_clean_logo.pdf"] = []
# S09 pdf: clean, but headings written as 'Work Experience' and 'Academic Background' (non-standard labels) plus 'Skills'.
c = mf.content(8); d = fitz.open(); pg = d.new_page(); y = 60
pg.insert_text((54, y), c["name"], fontsize=16, fontname="hebo"); y += 18
pg.insert_text((54, y), f'{c["email"]} | {c["phone"]}', fontsize=10.5); y += 28
for h, body in (("Work Experience", "\n".join(t for t, _ in c["jobs"])), ("Academic Background", c["edu"]), ("Skills", c["skills"])):
    pg.insert_text((54, y), h, fontsize=12.5, fontname="hebo"); y += 16
    for ln in body.split("\n"):
        pg.insert_text((54, y), ln, fontsize=10.5); y += 14
    y += 8
d.save(OUT / "S09_pdf_clean_nonstandard_labels.pdf"); d.close(); specs["S09_pdf_clean_nonstandard_labels.pdf"] = []
# S10 docx: scanned look, entire page is one picture. Planted image_text.
c = mf.content(9); d = Document(); lines = mf.body_lines(c)
d.add_picture(str(mf.text_png([c["name"], c["email"] + " | " + c["phone"]] + lines, TMP / "s10.png", w=1000)), width=Inches(6))
d.save(OUT / "S10_docx_whole_page_picture.docx"); specs["S10_docx_whole_page_picture.docx"] = ["image_text"]

gold = {"version": "format-stress-gold-v1", "status": "POST HOC: written after the frozen 16-file check had run. Expectations written before the check was run on these files.",
        "files": {k: {"planted": v, "clean": not v} for k, v in sorted(specs.items())}}
(HERE / "data" / "gold" / "format_stress_gold.json").write_text(json.dumps(gold, indent=1), encoding="utf-8")
import shutil; shutil.rmtree(TMP)
print(len(specs), "stress files")
