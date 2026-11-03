# JobHub UX Prototype — Single-Posting Review

This is a platform-agnostic, static-data UX prototype for the first JobHub workflow.

## Purpose

Test whether a job seeker can review one captured posting, distinguish source evidence from AI suggestions, identify unknowns and contradictions, choose useful verification questions and record a personal next action.

## Included

- Three captured fixtures from Run 002.
- Source snapshot and capture metadata.
- Section-level review states.
- Inline review controls only for interpretations, gaps, conflicts and other decision-relevant claims.
- Direct source facts are readable without requiring user confirmation; they can still be corrected if the capture is wrong.
- Source ownership and locators.
- Unknowns, contradictions and verification questions.
- Continue, investigate, save, pause and decline decisions.
- Local save/resume simulation through browser storage.
- Invalid/AI-draft warning and manual-review boundary.

## Excluded

- Live AI calls.
- Job-board scraping or login.
- Fit scores or candidate ranking.
- Scam, legitimacy or hiring verdicts.
- Resume rewriting.
- Employer messaging or application submission.
- Sensitive-question answering.
- Final platform, mobile/web or architecture decision.

## Prototype flow

```text
Choose posting
  -> inspect source snapshot
  -> read the continuous report from top to bottom
  -> review sections and claims inline
  -> confirm/edit/reject/leave important claims unresolved
  -> inspect unknowns and contradictions
  -> review questions
  -> choose personal decision
  -> save and resume
```

## How to use

Open `index.html` in a browser. Start with the Part-Time Admin Assistant fixture and follow:

1. Read the report from the posting identity and source snapshot through to `Your decision`.
2. Review the missing duties and compensation rules inline.
3. Review the contradiction and unknowns sections.
4. Edit or reject a claim.
5. Review decision-changing questions.
6. Choose `Decline`, add a rationale and save.
7. Reload or use `Resume saved review` to inspect recovery.

The report intentionally keeps every evidence section visible. The user should not have to open separate tabs to discover what the posting does or does not establish.

This is a UX test instrument, not a production application.
