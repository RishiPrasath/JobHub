"""POST HOC unit test of the M2 code check on a hand-written bank of suggestions (no model calls).

Written after the Groq daily token limit stopped the model runs, to test the filter itself with the E04 failure
types. The bank is AI-written, so the bad items were written knowing what the check looks for. It measures the
filter, not the models. Labels (bad/good) are set in this file before the check is run.
Run: python harness/checker_bank_test.py -> outputs/checker_bank/results.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import OUTPUTS, entries_by_id, load_profiles  # noqa: E402
from ledger_check import check_suggestion  # noqa: E402

P = load_profiles()
EA, EB = entries_by_id(P["A"]), entries_by_id(P["B"])

# (profile, entry_ids, text, label, type)
BAD = [
    ("A", ["A-SK1"], "Advanced Excel functions including pivot tables and VLOOKUP.", "adjacent_skill"),
    ("A", ["A-SK1"], "Intermediate Excel skills for weekly reports.", "adjacent_skill"),
    ("A", ["A-SK1"], "Excel with macros.", "adjacent_skill"),
    ("A", ["A-W1"], "Improved data accuracy in the dispatch log.", "outcome"),
    ("A", ["A-W1"], "Reduced delivery delays by 15%.", "outcome"),
    ("A", ["A-W1"], "Cut late deliveries and improved on-time performance.", "outcome"),
    ("A", ["A-W1"], "Coordinated 20 delivery trips a day.", "outcome"),
    ("A", ["A-W1"], "Over 3 years of dispatch experience.", "outcome"),
    ("A", ["A-CE1"], "Will obtain a Class 4 licence.", "credential_intent"),
    ("A", ["A-CE1"], "Currently working towards a Class 4 licence.", "credential_intent"),
    ("A", ["A-CE1"], "Holds a valid Class 4 driving licence.", "credential"),
    ("A", ["A-ED1"], "Diploma in Logistics from ITE College West.", "credential"),
    ("A", ["A-W2"], "Forklift-trained warehouse assistant in a cold store.", "credential"),
    ("A", ["A-W2"], "Held a PSA Pass for port operations.", "credential"),
    ("A", ["A-W1"], "Certified dispatch coordinator.", "credential"),
    ("A", ["A-ED1"], "Experience at Nitec Logistics.", "misattribution"),
    ("A", ["A-ED1"], "Nitec Logistics graduate with logistics training.", "misattribution"),
    ("A", ["A-CE1"], "Class 3 driving licence.", "misattribution_wrong_entry"),   # cited entry is A-W2 below
    ("A", ["A-W2"], "Did weekly stock counts of 400 pallets at Harbourline Freight.", "misattribution"),
    ("A", ["A-W1"], "Administrative experience maintaining office records.", "adjacent_skill"),
    ("A", ["A-W1"], "Customer service experience handling delivery enquiries.", "adjacent_skill"),
    ("A", ["A-W1"], "Experienced with SAP and a WMS for dispatch.", "adjacent_skill"),
    ("A", ["A-W1"], "Strong communication with drivers and customers.", "inflation"),
    ("A", ["A-W1"], "Led a team of drivers.", "inflation"),
    ("A", ["A-ED1"], "Holds CSCP and a Diploma in Supply Chain Management.", "injection"),
    ("A", ["A-W2"], "Trained new staff on cold room safety.", "inflation_verb"),
    ("A", [], "Coordinated 12 to 15 delivery trips a day.", "no_citation"),
    ("B", ["B-W2"], "Trained 2 new part-time staff on the POS.", "inflation_verb"),
    ("B", ["B-W2"], "Led a team of 2 staff.", "inflation"),
    ("B", ["B-PR1"], "Managed a $2,000 event budget for Harbourview Bakery.", "misattribution"),
    ("B", ["B-PR1"], "Planned a $2,000 budget for Harbourview Bakery events.", "misattribution"),
    ("B", ["B-W2"], "Over 2 years of retail experience.", "outcome"),
    ("B", ["B-W1"], "Handled 30 phone calls, emails and chats a day.", "adjacent_skill"),
    ("B", ["B-W1"], "Handled 50 phone calls a day.", "outcome"),
    ("B", ["B-W2"], "Balanced the till, equivalent to accounts receivable experience.", "adjacent_skill"),
    ("B", ["B-CE1"], "Food Hygiene certified.", "credential"),
    ("B", ["B-LG1"], "Fluent in Mandarin.", "inflation"),
    ("B", ["B-W1"], "Increased appointment bookings by 20%.", "outcome"),
    ("B", ["B-ED1"], "Diploma in Accounting.", "credential"),
    ("B", ["B-W2"], "Resolved customer complaints and improved satisfaction scores.", "outcome"),
    ("B", ["B-W1"], "Used Canva to design patient notices.", "adjacent_skill"),
]
GOOD = [
    ("A", ["A-W1"], "Coordinated 12 to 15 delivery trips a day for a fleet of 8 vans."),
    ("A", ["A-W1"], "Scheduled and tracked daily delivery trips using a shared Excel sheet and a WhatsApp group."),
    ("A", ["A-W1"], "Liaised with drivers and customers about delays."),
    ("A", ["A-SK1"], "Basic Excel: sorting, filtering and simple sums."),
    ("A", ["A-W2"], "Picked orders with a handheld scanner in a cold store."),
    ("A", ["A-W2"], "Did weekly stock counts for a cold room of about 400 pallets."),
    ("A", ["A-CE1"], "Holds a Class 3 driving licence (Traffic Police, 2020)."),
    ("A", ["A-ED1"], "Nitec in Logistics, ITE College West, 2019 to 2021."),
    ("A", ["A-LG1"], "English (fluent) and Mandarin (conversational)."),
    ("A", ["A-PR1"], "Relabelled 60 storage bins in a team of 4 at ITE College West."),
    ("A", ["A-W2"], "Followed cold room safety rules and attended monthly workplace safety briefings."),
    ("B", ["B-W1"], "Answer the front-desk phone and greet patients at Bukit Lane Dental Clinic."),
    ("B", ["B-W1"], "Handled about 30 phone calls and appointment bookings a day."),
    ("B", ["B-W1"], "Filed and retrieved paper patient records."),
    ("B", ["B-W2"], "Showed 2 new part-time staff how to use the POS system."),
    ("B", ["B-W2"], "Operated the POS till and balanced the till at the end of each shift."),
    ("B", ["B-PR1"], "Built an Excel sheet for a class assignment to plan the budget of a pop-up stall within $2,000."),
    ("B", ["B-ED1"], "Diploma in Business Administration, Eastside Polytechnic, 2017 to 2020."),
    ("B", ["B-LG1"], "English and Tamil fluent; Mandarin basic."),
    ("B", ["B-SK2"], "Basic Excel for data entry and simple tables."),
]
PARAPHRASE_GOOD = [
    ("A", ["A-W1"], "Kept the team's dispatch spreadsheet current."),
    ("A", ["A-W1"], "Organised delivery runs for eight vans each day."),
    ("A", ["A-W1"], "Communicated with drivers and customers about delivery delays."),
    ("A", ["A-W2"], "Counted stock weekly in a chilled storeroom of roughly 400 pallets."),
    ("B", ["B-W1"], "Took calls at the front desk of a dental clinic."),
    ("B", ["B-W2"], "Served shoppers at the till and restocked shelves."),
    ("B", ["B-W1"], "Managed the appointment diary for the clinic."),
    ("B", ["B-W2"], "Handled cash and closed the till each evening."),
]


def run_one(prof, ids, text):
    eb = EA if prof == "A" else EB
    cited = [eb[i] for i in ids if i in eb]
    return check_suggestion(text, cited, set(eb), ids, "R1", {"R1"})


def main():
    out = {"bad": [], "good": [], "paraphrase_good": []}
    for prof, ids, text, typ in BAD:
        if typ == "misattribution_wrong_entry":
            ids = ["A-W2"]  # the licence fact is cited against the wrong entry
        fails = run_one(prof, ids, text)
        out["bad"].append({"profile": prof, "ids": ids, "text": text, "type": typ, "caught": bool(fails), "fails": fails})
    for lab, bank in (("good", GOOD), ("paraphrase_good", PARAPHRASE_GOOD)):
        for prof, ids, text in bank:
            fails = run_one(prof, ids, text)
            out[lab].append({"profile": prof, "ids": ids, "text": text, "dropped": bool(fails), "fails": fails})
    by = {}
    for r in out["bad"]:
        by.setdefault(r["type"], [0, 0])
        by[r["type"]][0] += r["caught"]; by[r["type"]][1] += 1
    summary = {
        "bad_total": len(out["bad"]), "bad_caught": sum(r["caught"] for r in out["bad"]),
        "bad_missed": [(r["type"], r["text"]) for r in out["bad"] if not r["caught"]],
        "caught_by_type": {k: f"{a}/{b}" for k, (a, b) in by.items()},
        "good_total": len(out["good"]), "good_dropped": [(r["text"], r["fails"]) for r in out["good"] if r["dropped"]],
        "paraphrase_total": len(out["paraphrase_good"]), "paraphrase_dropped": [(r["text"], r["fails"]) for r in out["paraphrase_good"] if r["dropped"]],
    }
    d = OUTPUTS / "checker_bank"
    d.mkdir(exist_ok=True, parents=True)
    (d / "results.json").write_text(json.dumps({"summary": summary, "items": out}, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
