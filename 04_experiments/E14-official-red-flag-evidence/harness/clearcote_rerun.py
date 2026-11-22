"""E14 run-002: retry with the Clearcote browser what run-001 could not read.

Stage 1 (terms): SGX terms pages, and the terms of the two hosts whose cited
pages returned HTTP 403 in Part B (ComplaintsBoard, Robert Walters).
Stage 2 (content), only after a human-in-the-loop check of stage 1 terms:
pass --stage content with the labels to read.

Uses tools/clearcote_reader.py (open build, no key, robots first, one try
per URL, blocks recorded not bypassed). Output: runs/2026-11-21-run-002/outputs/.
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[3] / "tools"))
from clearcote_reader import Reader  # noqa: E402

OUT = HERE.parents[1] / "runs" / "2026-11-21-run-002" / "outputs"

TERMS = [
    ("sgx-terms-use", "https://www.sgx.com/terms-use"),
    ("sgx-datadirect-terms", "https://datadirect.sgx.com/Terms"),
    ("complaintsboard-terms", "https://www.complaintsboard.com/terms"),
    ("robertwalters-my-terms", "https://www.robertwalters.com.my/terms-and-conditions.html"),
]
CONTENT = {
    "robertwalters-my-legal-disclaimer": "https://www.robertwalters.com.my/legal-disclaimer.html",
    "sgx-announcements": "https://www.sgx.com/securities/company-announcements",
    # Part B citations that returned HTTP 403 in run-001 (verification only)
    "cite-O10-robertwalters-my-fraud": "https://www.robertwalters.com.my/fraud-alert.html",
    "cite-O04-complaintsboard-c660552": "https://www.complaintsboard.com/recruit-express-pte-ltd-attitude-about-a-staff-from-recruit-express-singapore-c660552",
}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["terms", "content"], default="terms")
    ap.add_argument("labels", nargs="*")
    a = ap.parse_args()
    with Reader(OUT) as r:
        if a.stage == "terms":
            for label, url in TERMS:
                r.read(url, label)
        else:
            for label in a.labels:
                r.read(CONTENT[label], label)
