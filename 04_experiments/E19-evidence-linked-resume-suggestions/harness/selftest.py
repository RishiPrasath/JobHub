"""Self-test of the checker and scorer on hand-written suggestions (no model output). Run before the model run."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from score import score_run  # noqa: E402

CASES = [
    # (set, method, requirement, ids, text, expect_displayed, expect_unsupported)
    ("P01-A", "M2", "R2", ["A-W1"], "Coordinated 12 to 15 delivery trips a day for 8 vans.", True, False),
    ("P01-A", "M2", "R1", ["A-CE1"], "Holds a Class 4 licence.", False, True),
    ("P01-A", "M2", "R1", ["A-CE1"], "Will obtain a Class 4 licence.", False, True),
    ("P01-A", "M2", "R2", ["A-W1"], "Reduced delivery delays by 20%.", False, True),
    ("P04-A", "M2", "R2", ["A-SK1"], "Uses advanced Excel functions such as pivot tables.", False, True),
    ("P04-A", "M2", "R2", ["A-SK1"], "Basic Excel: sorting, filtering and simple sums.", True, False),
    ("P02-A", "M2", "R1", ["A-ED1"], "Nitec Logistics graduate.", False, True),
    ("P02-A", "M2", "R1", ["A-ED1"], "Nitec in Logistics, ITE College West (2019 to 2021).", True, False),
    ("P09-B", "M2", "R1", ["B-PR1"], "Planned a $2,000 event budget for Harbourview Bakery.", False, True),
    ("P09-B", "M2", "R3", ["B-PR1"], "Built an Excel sheet to plan a pop-up stall budget of $2,000 in a class assignment.", True, False),
    ("P03-B", "M2", "R2", ["B-W1"], "Answer the front-desk phone and greet patients at a dental clinic.", True, False),
    ("P03-A", "M2", "R1", ["A-W1"], "Administrative experience keeping records up to date.", False, True),
    ("P06-A", "M2", "R1", ["A-ED1"], "Holds CSCP and a Diploma in Supply Chain Management.", False, True),
    ("P10-A", "M2", "R2", ["A-W2", "A-SK3"], "Did weekly stock counts for a cold room of about 400 pallets.", True, False),
    ("P10-A", "M2", "R2", ["A-W1"], "Did weekly stock counts for a cold room of about 400 pallets.", False, True),
]


def main():
    bad = 0
    for sid, m, req, ids, text, exp_disp, exp_unsup in CASES:
        parsed = {"suggestions": [{"requirement": req, "entry_ids": ids, "text": text}], "gaps": []}
        r = score_run(m, sid, parsed, "")
        it = r["raw_items"][0]
        ok = (it["displayed"] == exp_disp) and (it["unsupported"] == exp_unsup)
        bad += not ok
        print("OK  " if ok else "FAIL", sid, req, text[:60], "| displayed", it["displayed"], "| unsup", it["unsupported"],
              "| checker", it.get("check_fails"), "| flags", [f["code"] + ":" + f["detail"] for f in it["flags"]][:3])
    print("failures:", bad)


if __name__ == "__main__":
    main()
