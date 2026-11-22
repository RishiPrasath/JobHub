"""E22 Part B step 1: render eGazette browse pages with Patchright and record which data calls they make.
robots.txt disallows /search, so search pages are not used."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from patchright_reader import Reader
OUT = Path(__file__).resolve().parents[1] / "runs/2026-11-21-run-001/outputs/gazette"
with Reader(OUT) as r:
    r.read("https://www.egazette.gov.sg/", "home", capture_json="egazette")
    r.read("https://www.egazette.gov.sg/egazette-browse/", "browse", capture_json="egazette")
    r.read("https://www.egazette.gov.sg/gazettes/", "gazettes", capture_json="egazette")
