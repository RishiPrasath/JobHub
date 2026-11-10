"""Build the E17 sample: 60 X3 postings (metadata only, salary withheld, read-only from E10) + synthetic postings.
Rerunnable. Writes data/postings.json (full record incl. family, used only for reporting) and
data/postings_blind.json (title, seniority, employment_type, function only; what a labeller or matcher sees)."""
import json
from pathlib import Path

E17 = Path(__file__).resolve().parents[1]
X3 = E17.parents[0] / "E10-market-value-and-red-flag-experiments" / "outputs" / "x3" / "postings_ids.json"

FAMILY_OF_TERM = {
    "accountant": "accounting", "software engineer": "software", "staff nurse": "nursing",
    "warehouse supervisor": "warehouse supervisor", "marketing executive": "marketing",
    "customer service officer": "customer service", "mechanical engineer": "engineering",
    "cook": "kitchen", "human resource executive": "hr", "administrative assistant": "admin",
    "sales executive": "sales", "data analyst": "data",
}

# (title, seniority, employment_type, function, family, stratum)
S = [
 ("Electrician (Industrial, Class 2 licence)", "Non-Executive", "Permanent", "Building And Construction", "trades", "new_family"),
 ("Plumber", "Non-Executive", "Full Time", "Building And Construction", "trades", "new_family"),
 ("Welder (6G, Shipyard)", "Non-Executive", "Contract", "Manufacturing", "trades", "new_family"),
 ("Aircon Technician", "Non-Executive", "Full Time", "Building And Construction", "trades", "new_family"),
 ("Class 3 Lorry Driver", "Non-Executive", "Full Time", "Logistics / Supply Chain", "drivers", "new_family"),
 ("Part-time Food Delivery Rider (Motorcycle)", "Non-Executive", "Part Time", "Logistics / Supply Chain", "drivers", "new_family"),
 ("Forklift Operator", "Non-Executive", "Contract", "Logistics / Supply Chain", "drivers", "new_family"),
 ("Retail Sales Assistant (Weekend)", "Non-Executive", "Part Time", "Sales / Retail", "retail", "new_family"),
 ("Store Manager (Fashion Retail)", "Manager", "Permanent", "Sales / Retail", "retail", "new_family"),
 ("Retail Store Supervisor", "Executive", "Full Time", "Sales / Retail", "retail", "new_family"),
 ("Relief Teacher (Primary School)", "Professional", "Contract", "Education And Training", "education", "new_family"),
 ("Preschool Teacher (Nursery)", "Executive", "Full Time", "Education And Training", "education", "new_family"),
 ("Secondary Maths Tutor", "Non-Executive", "Part Time", "Education And Training", "education", "new_family"),
 ("Barista", "Non-Executive", "Full Time", "F&B", "hospitality", "new_family"),
 ("Hotel Front Desk Receptionist", "Junior Executive", "Full Time", "Hotel / Hospitality", "hospitality", "new_family"),
 ("Housekeeping Attendant (Hotel)", "Non-Executive", "Full Time", "Hotel / Hospitality", "hospitality", "new_family"),
 ("Pastry Chef", "Executive", "Full Time", "F&B", "hospitality", "new_family"),
 ("Healthcare Assistant (Nursing Home)", "Non-Executive", "Full Time", "Healthcare / Pharmaceutical", "healthcare support", "new_family"),
 ("Pharmacy Assistant", "Non-Executive", "Full Time", "Healthcare / Pharmaceutical", "healthcare support", "new_family"),
 ("Physiotherapist", "Professional", "Permanent", "Healthcare / Pharmaceutical", "healthcare support", "new_family"),
 ("Accounts Payable Executive", "Executive", "Permanent", "Accounting / Auditing / Taxation", "finance operations", "new_family"),
 ("Payroll Executive", "Executive", "Permanent", "Human Resources", "finance operations", "new_family"),
 ("Credit Control Officer", "Junior Executive", "Full Time", "Banking And Finance", "finance operations", "new_family"),
 ("Graphic Designer", "Executive", "Full Time", "Arts / Creative / Entertainment", "creative", "new_family"),
 ("Video Editor", "Executive", "Contract", "Advertising / Media", "creative", "new_family"),
 ("Social Media Content Creator", "Executive", "Full Time", "Advertising / Media", "creative", "new_family"),
 ("Security Officer (Condominium)", "Non-Executive", "Full Time", "Security", "other", "new_family"),
 ("Office Cleaner", "Non-Executive", "Contract", "Building Maintenance", "other", "new_family"),
 ("Personal Trainer", "Executive", "Full Time", "Sports / Fitness", "other", "new_family"),
 ("Social Worker (Family Service Centre)", "Professional", "Permanent", "Social Services", "other", "new_family"),
 # X3 failure types: promotional, generic sales and marketing, supervisor-type with no clear table match
 ("NO EXPERIENCE NEEDED!! Earn big, train with us, join the fun team 🔥", "Fresh/Entry Level", "Permanent", "Sales / Retail", "promotional", "failure_type"),
 ("Brand Ambassador (Travel Opportunities ✈️ Bonus Every Week)", "Non-Executive", "Permanent", "Events / Promotions", "promotional", "failure_type"),
 ("Work From Home Part Time Admin (Flexible, Earn Daily)", "Fresh/Entry Level", "Part Time", "Admin / Secretarial", "promotional", "failure_type"),
 ("Sales and Marketing Executive", "Executive", "Full Time", "Marketing / Public Relations", "generic sales and marketing", "failure_type"),
 ("Marketing & Sales Associate (Basic + Uncapped Commission)", "Junior Executive", "Permanent", "Sales / Retail", "generic sales and marketing", "failure_type"),
 ("Business Development Associate", "Junior Executive", "Full Time", "Sales / Retail", "generic sales and marketing", "failure_type"),
 ("Stores Supervisor (Cold Chain Distribution)", "Executive", "Full Time", "Logistics / Supply Chain", "supervisor-type", "failure_type"),
 ("Production Supervisor (Electronics Assembly)", "Executive", "Full Time", "Manufacturing", "supervisor-type", "failure_type"),
 ("Logistics Supervisor", "Executive", "Full Time", "Logistics / Supply Chain", "supervisor-type", "failure_type"),
 ("Cleaning Operations Supervisor", "Executive", "Full Time", "Building Maintenance", "supervisor-type", "failure_type"),
]


def main():
    x3 = json.loads(X3.read_text(encoding="utf-8"))
    out = []
    for p in x3:
        out.append({"id": f"X3-{p['id']:02d}", "source": "E10-X3", "synthetic": False,
                    "title": p["title"], "seniority": p["seniority"], "employment_type": p["employment_type"],
                    "function": p["function"], "family": FAMILY_OF_TERM[p["term"]],
                    "stratum": "x3_reuse"})
    for i, (t, sn, et, fn, fam, st) in enumerate(S, 1):
        out.append({"id": f"SYN-{i:02d}", "source": "synthetic", "synthetic": True, "title": t,
                    "seniority": sn, "employment_type": et, "function": fn, "family": fam, "stratum": st})
    (E17 / "data").mkdir(exist_ok=True)
    (E17 / "data" / "postings.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    blind = [{k: p[k] for k in ("id", "title", "seniority", "employment_type", "function")} for p in out]
    (E17 / "data" / "postings_blind.json").write_text(json.dumps(blind, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(out), "postings;", sum(p["synthetic"] for p in out), "synthetic")


main()
