# Part B protocol (frozen 2026-11-10 before any arm ran)

## Sample (reduced, by coordinator instruction)
10 organisations: 5 known problems and 5 controls (data/partB_groundtruth.json). README planned 30. Sample supports direction only.

## Arms
- **Fixed sweep (web part).** Blind sub-agent (Haiku model) given only the organisation name. It runs exactly these six WebSearch queries, once each, no others, and reads no pages. Query templates (name in double quotes):
  1. "NAME" Singapore regulator penalty fine
  2. "NAME" enforcement action Singapore
  3. "NAME" court judgment Singapore
  4. "NAME" complaints Singapore
  5. "NAME" retrenchment layoffs Singapore
  6. "NAME" scam fraud warning Singapore
- **Fixed sweep (list check).** Deterministic script harness/list_check.py compares the name to the readable official lists: the MOM EA Directory flagged list (26) and the MOM stop-work-order list (143 rows). MAS and CASE lists are Singapore-wide financial and consumer lists read in E10; they are not re-read here (no employment relevance for these agencies; stated as a gap). NOTE: because the known problems were selected from the MOM EA flagged list, the list check finds them BY CONSTRUCTION. It tests name matching on the controls (false matches), not recall. Recall of the web part is reported separately and is the informative number.
- **Free-form.** Blind sub-agent (Haiku) given only the organisation name; up to 8 searches and 4 page reads; own wording.
- Executors never see the ground truth, whether the organisation is a known problem or a control, or the other arm's output.

## Output format required from both arms (so it can be scored)
JSON list of items: {claim, entity_the_claim_is_about, category (employer_action | impersonation_warning_about_brand | consumer_complaint | other_entity | non_employment | other), source_url, quoted_evidence}. Plus "queries_run", "pages_read" and "failed_reads".

## Scoring (lead specialist, after all runs)
Per the gold-label rubric. Unsupported claim = claim with no source URL, or whose quoted evidence or source does not support it (spot-checked by opening the cited URL where possible). Impersonation handling = every item that is a warning about the brand being imitated is labelled impersonation_warning_about_brand. Cost = tool uses and tokens reported by the harness.

## Threshold use
Thresholds as in protocol/thresholds.md. With 5 known problems recall moves in steps of 20 points. With 5 controls, one wrong flag = 20%, so the 10% control criterion is tested as zero wrong flags.
