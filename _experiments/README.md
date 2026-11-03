# JobHub Experiments

This folder contains reproducible experiments used to evaluate JobHub ideas, AI behaviour and proposed workflows.

Each experiment should preserve the full chain:

```text
question → fixture → prompt → code → raw output → review → findings → limitations
```

## Structure

- `00_templates/` — reusable experiment documents and checklists.
- `01_source-grounding/` — whether model claims remain linked to source evidence.
- `02_contradiction-handling/` — conflicting, stale or mismatched job-posting information.
- `03_profile-comparison/` — cautious comparison of candidate facts with role requirements.
- `04_resume-alignment/` — truthful, evidence-backed resume suggestions.
- `05_prompt-injection-and-safety/` — untrusted content, privacy and external-action resistance.
- `06_industry-portability/` — shared and sector-specific review fields.
- `07_model-comparison/` — model accuracy, consistency, latency and output differences.
- `08_user-interface-and-human-review/` — correction, accessibility, interruption and recovery tests.

Reusable SDK instructions live in [Tools/OpenAI SDK](../Tools/OpenAI%20SDK/briefing.md). Product interpretation belongs in [analysis](../analysis/README.md).

## Naming convention

Use dated run folders:

```text
YYYY-MM-DD-run-001/
```

Do not overwrite previous runs. Create a new run when the fixture, prompt, model or evaluation method changes materially.
