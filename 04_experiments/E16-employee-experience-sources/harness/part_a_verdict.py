"""E16 Part A verdict. Rerunnable, no network, no model calls.

Reads data/source_classification.csv and applies the frozen Part A threshold:
pass = at least one EXISTING external source classed A (permitted for the intended use).
Job-seeker contributions are reported separately because they are not an existing source.
"""
import csv
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(root / "data" / "source_classification.csv", encoding="utf-8")))
counts = {}
for r in rows:
    key = r["class"].split(" ")[0]
    counts[key] = counts.get(key, 0) + 1
    print(f'{r["id"]:>2}  {r["source"]:<36} {r["class"]}')
print("\nclass counts:", counts)
external_a = [r["source"] for r in rows if r["class"].startswith("A") and r["id"] != "10"]
print("existing external sources classed A:", external_a or "none")
print("Part A verdict (strict, external sources):", "PASS" if external_a else "FAIL")
print("Note: job-seeker contributions are class A in principle but are not an existing source (0 coverage).")
