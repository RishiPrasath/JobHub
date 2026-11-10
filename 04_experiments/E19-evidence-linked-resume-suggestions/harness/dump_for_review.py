"""Write a readable dump of scored items so the AI reviewer can adjudicate them (post hoc, labelled).
Usage: python harness/dump_for_review.py   -> outputs/review_dump.md
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import OUTPUTS  # noqa: E402

lines = []
for p in sorted((OUTPUTS / "scored").glob("*.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    m = d["meta"]["method"]
    if m == "M3":
        continue
    lines.append(f"\n## {p.stem}\n")
    for sid, v in d["sets"].items():
        for it in v["raw_items"]:
            fl = "; ".join(f"{f['type']}:{f['detail']}" for f in it["flags"] if f["type"] != "negated_mention")
            status = "SHOWN" if it.get("displayed", True) else "DROPPED(" + ",".join(it.get("check_fails", [])) + ")"
            lines.append(f"- {sid} {it['requirement']} [{it['req_status']}] {it['entry_ids']} {status} | {it['text']} | flags: {fl or 'none'}")
(OUTPUTS / "review_dump.md").write_text("\n".join(lines), encoding="utf-8")
print(len(lines), "lines")
