"""Turns one parsed check output into the plain-language report a job seeker would see (used for the simulated pilot)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHK = json.loads((ROOT / "protocol" / "checklist.json").read_text(encoding="utf-8"))
ITEMS = {i["id"]: i for i in CHK["items"]}
SRC = CHK["sources"]


def render(parsed: dict) -> str:
    st = parsed.get("status", {})
    stated = [i for i, s in st.items() if s == "stated"]
    na = [i for i, s in st.items() if s == "not_applicable"]
    flags = {f.get("id"): f for f in parsed.get("flags", []) if isinstance(f, dict)}
    lines = ["OFFER LETTER CHECK (what this letter states and does not state)", "",
             f"Terms stated in the letter: {len(stated)} of {len(st)} on the checklist ({len(na)} do not apply)."]
    for label, key in (("NOT STATED IN THIS LETTER", "missing"), ("STATED BUT NOT CLEAR", "unclear")):
        its = [i for i, s in st.items() if s == key]
        if its:
            lines += ["", label + ":"]
            for i in its:
                f = flags.get(i, {})
                src = f.get("source")
                s = SRC.get(src if isinstance(src, str) else "", {})
                lines.append(f"- {ITEMS[i]['term']}")
                if f.get("quote"):
                    lines.append(f"  Letter says: \"{f['quote']}\"")
                lines.append(f"  Official guidance: {f.get('guidance', '')}")
                if s:
                    lines.append(f"  Source: {s['title']} ({s['page_date']}), {s['url']}")
    incs = parsed.get("inconsistencies") or []
    if incs:
        lines += ["", "THE LETTER DOES NOT AGREE WITH ITSELF:"]
        for x in incs:
            lines.append(f"- {x.get('note', '')} ({'; '.join(x.get('quotes', []))})")
    lines += ["", "This list shows what the letter does and does not say. It does not say whether anything is fair or lawful, and it is not legal advice. A term not in the letter may be in the contract or staff handbook; you can ask the employer."]
    return "\n".join(lines)
