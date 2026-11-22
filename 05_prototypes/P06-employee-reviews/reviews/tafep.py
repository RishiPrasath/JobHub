"""TAFEP Tripartite Standards adopters, keyed by UEN.

Source: the public list at
https://www.tal.sg/tafep/getting-started/progressive/tripartite-standards-adopters
which loads one JSON file. TAFEP's terms of use have no clause on automated
access and robots.txt returns 404 (E16 run-003, read 2026-11-21). The list
exists to show job seekers which employers adopted the standards, which is the
use here. One request per refresh; do not poll.

What it means: an employer's own pledge to follow good practice, checked by
TAFEP. It is not employee experience. Not being on the list proves nothing.
"""
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

from .names import normalise_uen

API_URL = "https://www.tal.sg/tafep/api/tal/PageContent/GetTafepTSListing"
PUBLIC_PAGE = "https://www.tal.sg/tafep/getting-started/progressive/tripartite-standards-adopters"
STANDARDS_PAGE = "https://www.tal.sg/tafep/getting-started/progressive/tripartite-standards"
USER_AGENT = "JobHub-research/0.1 (Python urllib; one request per refresh)"
TOTAL_STANDARDS = 10

# Codes and names as the list itself gives them (read 2026-11-22).
STANDARDS = {
    "AFW": "Age-Friendly Workplace Practices",
    "FWA": "Flexible Work Arrangements",
    "GH": "Grievance Handling",
    "LWW": "Advancing Well-Being of Lower-Wage Workers",
    "MFL": "Procurement of Services from Media Freelancers",
    "RP": "Recruitment Practices",
    "SEP": "Contracting with Self Employed Persons",
    "TCE": "Employment of Term-Contract Employees",
    "UCL": "Unpaid Leave for Unexpected Care Needs",
    "WLH": "Work-Life Harmony",
}

CAVEAT = ("These are the employer's own pledges to follow good practice, checked by TAFEP. "
          "They are not employee reviews, and not being on the list does not mean poor practice.")

DEFAULT_CACHE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "cache")


def fetch(cache_dir: str = DEFAULT_CACHE, timeout: int = 120) -> str:
    """Download the list once and save it with its fetch time. Returns the path."""
    os.makedirs(cache_dir, exist_ok=True)
    req = urllib.request.Request(API_URL, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
    rows = json.loads(body)
    if not isinstance(rows, list) or not rows or "CompanyUen" not in rows[0]:
        raise ValueError("TAFEP list has an unexpected shape; not saved")
    fetched = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    path = os.path.join(cache_dir, "tafep_ts_listing.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"fetched_at": fetched, "source": API_URL, "rows": rows}, f)
    return path


def _parse_date(s: str) -> str | None:
    try:
        return datetime.strptime(s.strip(), "%d %b %Y %I:%M %p").strftime("%Y-%m-%d")
    except (ValueError, AttributeError):
        return None


def build_index(rows: list[dict]) -> dict:
    """Group the list's rows (one per employer and standard) by UEN."""
    index: dict[str, dict] = {}
    for r in rows:
        uen = normalise_uen(r.get("CompanyUen", ""))
        if not uen:
            continue
        e = index.setdefault(uen, {"uen": uen, "name": r.get("CompanyName", "").strip(),
                                   "website": "", "industry": r.get("SsicDescription", "").strip(),
                                   "active": {}, "rescinded": {}})
        if r.get("Website") and not e["website"]:
            e["website"] = r["Website"].strip()
        code = (r.get("ProgrammeSubcategoryCode") or "").strip()
        bucket = "active" if r.get("StatusCode") == "ACT" else "rescinded"
        date = _parse_date(r.get("LastUpdatedDate", ""))
        prev = e[bucket].get(code)
        if prev is None or (date and date > prev):
            e[bucket][code] = date
    for e in index.values():
        for code in list(e["rescinded"]):
            if code in e["active"]:
                del e["rescinded"][code]
    return index


class TafepList:
    def __init__(self, rows: list[dict], fetched_at: str | None = None):
        self.index = build_index(rows)
        self.fetched_at = fetched_at
        dates = [d for e in self.index.values() for d in list(e["active"].values()) + list(e["rescinded"].values()) if d]
        self.latest_update = max(dates) if dates else None

    @classmethod
    def load(cls, path: str) -> "TafepList":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):  # a raw list, e.g. a test fixture
            return cls(data)
        return cls(data["rows"], data.get("fetched_at"))

    def age_days(self) -> float | None:
        if not self.fetched_at:
            return None
        t = datetime.strptime(self.fetched_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        return (time.time() - t.timestamp()) / 86400

    def lookup(self, uen: str) -> dict:
        """Badge data for one UEN. Never says anything about an employer not on the list."""
        uen = normalise_uen(uen)
        e = self.index.get(uen)
        base = {"source": "TAFEP Tripartite Standards adopters", "source_url": PUBLIC_PAGE,
                "about_url": STANDARDS_PAGE, "list_updated_to": self.latest_update,
                "fetched_at": self.fetched_at, "caveat": CAVEAT, "uen": uen}
        if not e or not e["active"]:
            base.update(found=False, text=(
                f"Not on TAFEP's list of Tripartite Standards adopters"
                + (f" (list updated to {self.latest_update})" if self.latest_update else "") + "."))
            if e and e["rescinded"]:
                base["rescinded"] = sorted(e["rescinded"])
            return base
        codes = sorted(e["active"], key=lambda c: list(STANDARDS).index(c) if c in STANDARDS else 99)
        names = [STANDARDS.get(c, c) for c in codes]
        base.update(
            found=True, listed_name=e["name"], listed_website=e["website"],
            standards=[{"code": c, "name": STANDARDS.get(c, c), "updated": e["active"][c]} for c in codes],
            rescinded=sorted(e["rescinded"]),
            text=f"Adopted {len(codes)} of {TOTAL_STANDARDS} Tripartite Standards: " + ", ".join(names) + ".",
        )
        return base
