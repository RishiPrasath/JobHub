"""Post hoc (run-002): ask a model that has never seen the snapshot step to write 10 harder, messier pastes.
Each request fixes the field states, so the label is known by construction (and then checked by eye before freezing).
All text is synthetic. Usage: python harness/gen_heldout.py
"""
import json, sys
from pathlib import Path
EXP = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(EXP.parents[1] / "tools"))
from llm_client import chat

MODEL = "openai/gpt-oss-120b"
BASE = ("Write the raw text that a person would get by pressing Select All then Copy on a {board_desc} job page in Singapore, for a fictional "
        "employer and a made-up job. Output the pasted text ONLY: no commentary, no markdown, no code fences. Include realistic page furniture "
        "(menu text, buttons, banners, footer links). Target 250 to 400 words. Requirements for this paste:\n{req}\n"
        "Today is 2026-11-10; any dates you write must be in November or December 2026.")
BOARDS = {"jobstreet": "JobStreet-style (left list of search result cards plus the selected job detail on the right)",
          "mcf": "MyCareersFuture-style", "fastjobs": "FastJobs-style mobile-friendly", "company": "company careers page"}
H = [
 ("H01", "jobstreet", "clerical", "- the job description is plain prose paragraphs with NO headings and NO bullet points\n- the employer is named\n- NO salary or pay information anywhere in the selected job (other cards in the left list may show salaries)\n- NO closing date anywhere, only 'Posted Nd ago'"),
 ("H02", "jobstreet", "professional", "- the description uses bullets under 'Your day to day' and 'About you'\n- the employer is named\n- pay is shown as 'Up to $3,000 + commission'\n- the closing date is written inside a sentence of the description as 'applications will be reviewed until 28 November 2026'"),
 ("H03", "mcf", "professional", "- the employer is NOT named: the page says 'Our client, a leading multinational (name withheld by the agency)'\n- description is prose paragraphs with no headings\n- salary range shown\n- shows 'Closing on 14 Dec 2026'"),
 ("H04", "mcf", "clerical", "- the header lines appear AFTER the description in the copied text (order mixed up)\n- employer named, salary range shown\n- closing shown only as 'Closing in 3 days'\n- includes badges such as 'Job Match: 64%' and 'Be an early applicant'"),
 ("H05", "fastjobs", "manual", "- uses emoji bullets for duties\n- the page says the pay per day\n- NO employer name anywhere (only 'Posted by a verified employer')\n- NO closing date, only 'Posted 5 hours ago'"),
 ("H06", "fastjobs", "gig", "- a short phone-style copy with no menu text, starting with one line like an emoji, the job title and the pay\n- the employer is named in a line near the top\n- duties given in 2 or 3 short lines\n- the text says 'Apply anytime, no deadline'"),
 ("H07", "company", "professional", "- sections written as prose under 'About the role' and 'About you'\n- employer named\n- the pay range is written inside a sentence in the prose\n- a deadline is written in a sentence as 'Please apply by 30 November 2026'"),
 ("H08", "company", "clerical", "- employer named, job title shown\n- duties as bullets\n- the page says 'Salary will be discussed at interview'\n- the page says applications are 'open until the position is filled'"),
 ("H09", "jobstreet", "manual", "- a few words of Chinese appear in the menu or banner (for example 招聘 or 立即申请)\n- employer shown as 'Private Advertiser'\n- pay $12 - $14 per hour is shown\n- NO closing date\n- duties as short bullets"),
 ("H10", "company", "part-time", "- duties and requirements are in one prose paragraph, no headings\n- employer named\n- NO pay mentioned\n- NO closing date mentioned\n- includes a cookie banner and a newsletter signup block in the middle of the text"),
]
out = EXP / "data/heldout/pastes"
raw = EXP / "runs/2026-11-10-run-002/outputs/raw/gen"
for hid, board, jtype, req in H:
    r = chat(MODEL, [{"role": "user", "content": BASE.format(board_desc=BOARDS[board], req=req)}], max_tokens=1100, temperature=0.8,
             reasoning_effort="low", cache_dir=str(raw), tag=hid)
    txt = r["content"].strip()
    (out / f"{hid}.txt").write_bytes(txt.encode("utf-8"))
    print(hid, len(txt), r["usage"].get("total_tokens"), flush=True)
json.dump([{"id": h[0], "board": h[1], "job_type": h[2], "requested": h[3]} for h in H], open(EXP / "data/heldout/requests.json", "w"), indent=1, ensure_ascii=False)
