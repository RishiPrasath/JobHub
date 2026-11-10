"""Reconcile labeller A (specialist) and labeller B (blind fresh sub-agent) into data/gold.json.
Rule, fixed before any matcher ran:
- Both agree on primary: gold primary = that code. accept = union of A's alt codes, plus any B alt codes that A adopts (ADOPT_B below).
- Primaries differ: resolved case by case (RESOLVE below); every disagreement is written to data/label_disagreements.json.
- true_no_match = both labellers said NONE. none_acceptable = NONE is an accepted answer (true no-match, or a resolved ambiguity).
Rerunnable. Does not call any model."""
import json
from pathlib import Path

E = Path(__file__).resolve().parents[1]
A = {a["id"]: a for a in json.loads((E / "data/labels_A.json").read_text(encoding="utf-8"))}
B = {b["id"]: b for b in json.loads((E / "data/labels_B.json").read_text(encoding="utf-8"))}
P = {p["id"]: p for p in json.loads((E / "data/postings.json").read_text(encoding="utf-8"))}

# B alt codes that A, on seeing them, accepts as defensible (others rejected: reasons in FINDINGS)
ADOPT_B = {"X3-06": ["25141"], "X3-23": ["24314"], "X3-32": ["31002"]}
REJECT_B = {"X3-31": ["21411"], "X3-34": ["21411"], "SYN-22": ["24233"]}  # B alt rejected by A
# primaries differ: id -> (primary, accept, resolution)
RESOLVE = {
    "X3-36": ("34341", ["34341", "51201"], "Demi chef is a chef rank; cook also defensible. Both accepted."),
    "X3-42": ("43112", ["43112", "33131"], "Both accounts-clerk and assistant-accountant levels defensible. Both accepted."),
    "X3-46": ("43112", ["43112", "43111", "NONE"], "A coded ledger clerk, B said title gives no clear duties. Genuinely ambiguous; clerk codes and NONE all accepted; excluded from the true no-match set."),
    "X3-58": ("25112", ["25112", "21231"], "Data business analyst: business analyst or data analyst. Both accepted."),
    "SYN-21": ("43112", ["43112", "33131"], "Accounts payable executive: clerk or assistant accountant. Both accepted."),
    "SYN-25": ("21662", ["21662", "26544"], "Video editor: multimedia/animator or video editor. Both accepted."),
    "SYN-26": ("24314", ["24314", "26413"], "Social content creator: digital marketing or content writer. Both accepted."),
}


def main():
    gold, dis = [], []
    for pid in A:
        a, b = A[pid], B[pid]
        if a["primary"] == b["code"]:
            primary = a["primary"]
            accept = [primary] + [c for c in a["alt"] if c != primary] + ADOPT_B.get(pid, [])
            agree = "agree"
            # A flagged the item ambiguous but B agreed on a primary: keep A's alt list, do not add NONE
        else:
            primary, accept, why = RESOLVE[pid]
            agree = "disagree_resolved"
            dis.append({"id": pid, "title": P[pid]["title"], "A": a["primary"], "B": b["code"],
                        "B_alt": b.get("alt", []), "A_alt": a["alt"], "resolution": why, "accept": accept})
        if pid in REJECT_B:
            dis.append({"id": pid, "title": P[pid]["title"], "note": "B alt rejected by A", "B_alt_rejected": REJECT_B[pid],
                        "A": a["primary"], "B": b["code"]})
        true_nm = a["primary"] == "NONE" and b["code"] == "NONE"
        # A said NONE with an alt (e.g. X3-53): NONE accepted but alt code also accepted; B decides
        if a["primary"] == "NONE" and a["alt"]:
            accept = ["NONE"] + [c for c in a["alt"]]
            true_nm = False  # alt present: ambiguous, not a clean no-match
        gold.append({
            "id": pid, "title": P[pid]["title"], "family": P[pid]["family"], "stratum": P[pid]["stratum"],
            "synthetic": P[pid]["synthetic"],
            "primary": primary, "accept": accept,
            "true_no_match": bool(true_nm), "none_acceptable": "NONE" in accept,
            "too_senior": a["too_senior"], "too_junior": a["too_junior"],
            "labeller_agreement": agree, "A_primary": a["primary"], "B_primary": b["code"],
            "reason_A": a["reason"], "reason_B": b["reason"],
        })
    (E / "data/gold.json").write_text(json.dumps(gold, ensure_ascii=False, indent=1), encoding="utf-8")
    (E / "data/label_disagreements.json").write_text(json.dumps(dis, ensure_ascii=False, indent=1), encoding="utf-8")
    n = len(gold)
    print(n, "gold;", "true_no_match", sum(g["true_no_match"] for g in gold), "none_acceptable",
          sum(g["none_acceptable"] for g in gold), "disagree", sum(g["labeller_agreement"] != "agree" for g in gold))


if __name__ == "__main__":
    main()
