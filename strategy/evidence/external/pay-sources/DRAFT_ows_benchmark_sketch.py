"""DRAFT sketch: pay benchmark lookup from MOM Occupational Wages on data.gov.sg.

Source: "Resident Occupational Wages, June 2025" (MOM), data.gov.sg dataset
d_9917e751f7498502f70052a940a3f312, Singapore Open Data Licence v1.0.
Attribution string must be shown wherever the benchmark is shown.

Online mode uses the public data.gov.sg APIs (no key: 4 datastore calls / 10 s,
2 download calls / 10 s). Offline mode reads a local CSV snapshot.
Not for MyCareersFuture: its terms bar reuse; posting pay comes from the user's paste.
"""
from __future__ import annotations
import csv, json, sys, time, urllib.request, urllib.parse
from datetime import date

DATASET = "d_9917e751f7498502f70052a940a3f312"          # all industries, 523 occupations
DATASET_BY_INDUSTRY = "d_523d376ff1d501a338add925f3313fd1"  # 1,579 rows, occ x industry
ODL = "https://data.gov.sg/open-data-licence"

def attribution(accessed: date) -> str:
    return (f"Contains information from Resident Occupational Wages, June 2025 accessed on "
            f"{accessed.isoformat()} from data.gov.sg which is made available under the terms "
            f"of the Singapore Open Data Licence version 1.0 {ODL}")

def fetch_rows_online(dataset: str = DATASET) -> list[dict]:
    """Paged datastore_search; stays under the no-key rate limit."""
    rows, offset = [], 0
    while True:
        q = urllib.parse.urlencode({"resource_id": dataset, "limit": 1000, "offset": offset})
        with urllib.request.urlopen(f"https://data.gov.sg/api/action/datastore_search?{q}") as r:
            res = json.load(r)["result"]
        rows += res["records"]
        offset += len(res["records"])
        if offset >= res["total"] or not res["records"]:
            return rows
        time.sleep(3)

def download_csv_url(dataset: str = DATASET) -> str:
    """Bulk route: poll-download returns a short-lived signed CSV URL."""
    with urllib.request.urlopen(
        f"https://api-open.data.gov.sg/v1/public/api/datasets/{dataset}/poll-download") as r:
        return json.load(r)["data"]["url"]

def load_rows_offline(path: str) -> list[dict]:
    """Local snapshot in the E10 column layout (ssoc2024, occupation, gross_p25, ...)."""
    out = []
    for r in csv.DictReader(open(path, encoding="utf-8")):
        out.append({"occ_desc": r["occupation"].strip().lower(), "ssoc2024": r.get("ssoc2024"),
                    "mthly_gross_wage_25_pctile": r["gross_p25"],
                    "mthly_gross_wage_50_pctile": r["gross_median"],
                    "mthly_gross_wage_75_pctile": r["gross_p75"]})
    return out

def benchmark(rows: list[dict], confirmed_occupation: str, posted_min: int | None = None,
              posted_max: int | None = None) -> dict | None:
    """Occupation must already be confirmed by the user (FEAT-009 shortlist-and-confirm).
    Returns None for 'none of these' or an unknown title: show no benchmark."""
    key = confirmed_occupation.strip().lower()
    row = next((r for r in rows if r["occ_desc"].strip().lower() == key), None)
    if row is None:
        return None
    p25, p50, p75 = (int(row[f"mthly_gross_wage_{p}_pctile"]) for p in (25, 50, 75))
    out = {"occupation": row["occ_desc"], "gross_p25": p25, "gross_median": p50, "gross_p75": p75,
           "basis": ("Monthly gross wage, full-time resident employees, private establishments with "
                     "25+ employees, all industries, June 2025. Excludes bonuses and employer CPF.")}
    if posted_min and posted_max:
        mid = (posted_min + posted_max) / 2
        out["posted_midpoint"] = mid
        out["position"] = ("below 25th percentile" if mid < p25 else
                           "above 75th percentile" if mid > p75 else "between 25th and 75th")
    return out

if __name__ == "__main__":
    rows = load_rows_offline(sys.argv[1]) if len(sys.argv) > 1 else fetch_rows_online()
    print(len(rows), "occupations")
    print(json.dumps(benchmark(rows, "Statistical officer/Data analyst", 3600, 4500), indent=2))
    print(benchmark(rows, "none of these"))
    print(attribution(date.today()))
