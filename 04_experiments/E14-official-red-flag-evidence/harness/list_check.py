"""Deterministic direct check of readable official lists (Part B fixed sweep, list part).

Usage (from anywhere): python harness/list_check.py PATH_TO_SWO_LINES_TXT > runs/2026-11-10-run-001/outputs/partB/list_check.json

Reads data/mom_ea_directory_flagged_2026-11-10.json and the stop-work-order lines file.
Matching: upper case, strip punctuation, drop generic words (Pte, Ltd, Singapore, ...), then a match means the
token sets are equal, or the shorter name has >= 2 tokens and all are contained in the longer one.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parents[1]
STOP = {"PTE", "LTD", "PRIVATE", "LIMITED", "SINGAPORE", "SG", "CO", "THE", "AND", "SPECIALIST", "SERVICES", "SERVICE"}


def toks(s):
    s = re.sub(r"[^A-Z0-9 ]", " ", s.upper())
    return {t for t in s.split() if t not in STOP}


def match(a, b):
    ta, tb = toks(a), toks(b)
    if not ta or not tb:
        return False
    if ta == tb:
        return True
    s, l = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    return len(s) >= 2 and s <= l


def main():
    gt = json.loads((HERE / "data/partB_groundtruth.json").read_text(encoding="utf-8"))
    ea = json.loads((HERE / "data/mom_ea_directory_flagged_2026-11-10.json").read_text(encoding="utf-8"))["agencies"]
    # SWO lines file is not stored in the repo (MOM note: do not reproduce without permission); pass its path as argv[1]
    swo_p = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "no-such-file"
    swo = swo_p.read_text(encoding="utf-8").splitlines() if swo_p.exists() else []
    out = []
    for org in gt["known"] + gt["controls"]:
        hits = [f'EA directory: {a["name"]} ({a["status"]})' for a in ea if match(org["name"], a["name"])]
        hits += [f"SWO list line: {n[:80]}" for n in swo if match(org["name"], n)]
        out.append({"id": org["id"], "name": org["name"], "list_hits": hits})
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
