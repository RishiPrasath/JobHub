"""E16 run-002: re-read the primary terms pages that run-001 could not open.

Terms, robots and developer pages only. No review, company or forum page is
fetched (E16 method rule). Uses tools/clearcote_reader.py (Clearcote open
build, no key). Output: runs/2026-11-21-run-002/outputs/.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[3] / "tools"))
from clearcote_reader import Reader  # noqa: E402

OUT = HERE.parents[1] / "runs" / "2026-11-21-run-002" / "outputs"

TARGETS = [
    ("glassdoor-com-terms", "https://www.glassdoor.com/about/terms/"),
    ("glassdoor-com-legal-terms", "https://www.glassdoor.com/legal/terms-of-use"),
    ("glassdoor-sg-terms", "https://www.glassdoor.sg/about/terms/"),
    ("glassdoor-developer", "https://www.glassdoor.com/developer/index.htm"),
    ("reddit-user-agreement", "https://redditinc.com/policies/user-agreement"),
    ("reddit-data-api-terms", "https://redditinc.com/policies/data-api-terms"),
    ("gmp-terms", "https://cloud.google.com/maps-platform/terms"),
    ("gmp-service-specific-terms", "https://cloud.google.com/maps-platform/terms/maps-service-terms"),
    ("gmp-places-policies", "https://developers.google.com/maps/documentation/places/web-service/policies"),
]

if __name__ == "__main__":
    with Reader(OUT) as r:
        for label, url in TARGETS:
            r.read(url, label)
