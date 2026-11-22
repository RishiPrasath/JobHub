# E22: Singapore company entity sources

Status: run 2026-11-21 (run-001, small volume). See [FINDINGS.md](FINDINGS.md).
Affects: FEAT-001, ASM-001 (employer identity), and the source list in [DRAFT_sg-company-data-free-legal-sources.md](../../strategy/evidence/external/DRAFT_sg-company-data-free-legal-sources.md)

## Question

Can free, legally usable sources take a brand name or a domain from a job posting to the right ACRA entity (UEN)? How often is a name-only match ambiguous or wrong?

## Layout

- `protocol/PROTOCOL.md` plan, sources, volume caps and thresholds
- `data/sample.json` 20 brands and 6 constructed lookalikes; `data/truth.json` truth set from the brands' own sites
- `harness/` code: `terms_read.py` (step 0), `e_site_truth.py` (Part E), `a_acra_match.py` (Part A), `c_domain_chain.py` (Part C), `b_gazette_*.py` (Part B), `score.py`
- Browser reader: [tools/patchright_reader.py](../../tools/patchright_reader.py) (Patchright driving real Chrome, headed, throwaway profile)
- `runs/2026-11-21-run-001/outputs/` raw results, never edited (one privacy redaction noted in FINDINGS)

## Rerun

```
python 04_experiments/E22-sg-company-entity-sources/harness/terms_read.py
python 04_experiments/E22-sg-company-entity-sources/harness/e_site_truth.py
python 04_experiments/E22-sg-company-entity-sources/harness/a_acra_match.py
python 04_experiments/E22-sg-company-entity-sources/harness/c_domain_chain.py
python 04_experiments/E22-sg-company-entity-sources/harness/b_gazette_explore.py
python 04_experiments/E22-sg-company-entity-sources/harness/b_gazette_notices.py
python 04_experiments/E22-sg-company-entity-sources/harness/b_gazette_pdfs.py
python 04_experiments/E22-sg-company-entity-sources/harness/score.py
```

Needs `pip install patchright pypdf` and Google Chrome. A new run needs a new run folder; the harness paths point at run-001.

## Attribution

Contains information from "Entities Registered with ACRA" accessed on 21 November 2026 from data.gov.sg, which is made available under the terms of the Singapore Open Data Licence version 1.0 (https://data.gov.sg/open-data-licence).

e-Gazette extracts are subject to copyright of the Singapore Government and are reproduced with the permission of the Singapore Government. Check www.egazette.gov.sg for the latest e-Gazettes.
