"""Write protocol/FROZEN.md: UTC time and sha256 of the thresholds, rubric, scoring rules, Part B protocol, every gold
file, the postings, the prompt and the harness copy. Refuses to overwrite an existing FROZEN.md (hashes are final)."""
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import E12, REPO, sha256  # noqa: E402

out = E12 / "protocol" / "FROZEN.md"
if out.exists():
    sys.exit("FROZEN.md already exists; not overwriting.")
files = [E12 / "protocol" / n for n in ("thresholds.md", "question-rubric.md", "scoring-rules.md", "part-b-simulated-pilot.md", "sample-design.md")]
files += sorted((E12 / "data" / "gold").glob("*.json"))
files += sorted((E12 / "data" / "postings").glob("*.txt"))
files += [E12 / "harness" / "guarded-role-review-v2.md", E12 / "harness" / "claim_review_harness.py"]
e08 = REPO / "04_experiments" / "E08-user-interface-and-human-review" / "runs"
cmp_ = [(E12 / "harness" / "guarded-role-review-v2.md", e08 / "2026-10-27-run-002" / "prompts" / "guarded-role-review-v2.md"),
        (E12 / "harness" / "claim_review_harness.py", e08 / "2026-10-20-run-001" / "code" / "claim_review_harness.py")]
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
lines = ["# FROZEN", "", f"Frozen at {now} (UTC), before the first model call of run 2026-11-10-run-001.", "",
         "Thresholds, rubric, scoring rules, Part B protocol, gold labels, postings and the E08 prompt and harness copies are hashed below. They are not changed afterwards; a change is a new, labelled run. Nothing is committed to git because the owner has not asked for commits (see FINDINGS.md, Deviations).", "",
         "| file | sha256 |", "|---|---|"]
for f in files:
    lines.append(f"| {f.relative_to(E12).as_posix()} | {sha256(f)} |")
lines += ["", "## E08 byte-identity check", ""]
for mine, theirs in cmp_:
    lines.append(f"- {mine.relative_to(E12).as_posix()} equals {theirs.relative_to(REPO).as_posix()}: {sha256(mine) == sha256(theirs)}")
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(out.read_text(encoding="utf-8"))
