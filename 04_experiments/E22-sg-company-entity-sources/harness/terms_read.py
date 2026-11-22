"""E22 step 0: read terms pages and robots.txt for each source with real Chrome (Patchright)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from patchright_reader import Reader

OUT = Path(__file__).resolve().parents[1] / "runs/2026-11-21-run-001/outputs/terms"
PAGES = [
    ("mcf-terms", "https://www.mycareersfuture.gov.sg/terms-of-use"),
    ("mcf-home", "https://www.mycareersfuture.gov.sg/"),
    ("bizfile-terms", "https://www.bizfile.gov.sg/terms-of-use"),
    ("datagov-terms", "https://data.gov.sg/privacy-and-terms"),
    ("datagov-licence", "https://data.gov.sg/open-data-licence"),
    ("egazette-terms", "https://www.egazette.gov.sg/terms-of-use/"),
]
with Reader(OUT) as r:
    for label, url in PAGES:
        r.read(url, label)
