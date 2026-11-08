# UX Prototype Design Brief — Single-Posting Review

Status: prototype implemented for review

Date: 2026-10-27

## Specialist synthesis

The UX Expert, UX and User-Flow Designer, Product Strategist and Responsible AI Reviewer independently converged on the same narrow prototype:

> A resumable, human-reviewed evidence workspace for one captured job posting.

The prototype must keep four things visibly separate:

1. Source evidence
2. AI draft interpretation
3. Uncertainty and source conflicts
4. The user's own decision

## Prototype scope

The prototype includes:

- one-posting selection;
- source snapshot and capture date;
- section-level states;
- claim-level source locators and ownership;
- inline controls for interpretations, gaps, conflicts and other decision-relevant claims;
- correction controls for direct source facts without requiring confirmation of every fact;
- unknowns, contradictions and verification questions;
- personal decision and rationale;
- local save/resume simulation;
- visible AI-draft-not-verified boundary.

It deliberately excludes fit scores, scam detection, resume rewriting, profile matching, application submission, employer messaging, scraping, sensitive-question handling and final platform/provider decisions.

## Required states

### Claim state

```text
present
conditional
conflicting
unknown
not_visible
platform_signal
```

### Human review state

```text
draft
accepted
edited
rejected
unresolved
```

### Session state

```text
new
source_captured
analysis_pending
review_ready
claim_review
section_review
uncertainty_review
question_review
decision_draft
saved
interrupted
manual_fallback
```

## Prototype artifact

The current static prototype is:

[_prototypes/00_single-posting-review/index.html](../_prototypes/00_single-posting-review/index.html)

It uses static data from Run 002 and does not make live AI or external requests.

## Test sequence

1. Choose the Part-Time Admin Assistant fixture.
2. Inspect the source snapshot and important gaps.
3. Review duties, compensation rules and employer context.
4. Open the contradiction section.
5. Confirm, edit, reject or leave one important claim unresolved.
6. Select a decision-changing question.
7. Choose `Decline` and add a rationale.
8. Save the review.
9. Reload and verify that the decision and review history remain.
10. Repeat with the Driver and Vehicle Mechanic fixtures.

## Success criteria

- The reviewer can understand what the posting actually states.
- Missing information is visible without being treated as wrongdoing.
- Source claims and AI suggestions are distinguishable.
- Contradictions are shown without automatic resolution.
- Corrections are possible at claim level.
- Questions are linked to unresolved sections.
- Decisions remain explicitly user-owned.
- Save/resume does not lose the source or corrections.
- The prototype does not provide external-action controls.

## Next decision

This prototype now needs owner review. The next decision is whether the flow is understandable and useful enough to proceed to a more polished UX prototype, or whether the information hierarchy and interactions should be revised first.

## Prototype revision: continuous report layout

The first implementation used section navigation, but the owner requested a more readable report-like experience. The prototype now presents the source snapshot, every evidence section, decision-changing questions and the personal decision in one continuous top-to-bottom document.

This revision is intended to test whether a person can provide or select one posting and understand the available details without repeatedly switching sections. Claim controls remain inline so the report stays actionable rather than becoming a static summary.

The layout does not change the evidence boundary: source facts, platform signals, AI-drafted claims, unknowns and the user's decision remain visibly distinct. It also does not introduce fit scoring, scam verdicts, application submission or a final mobile/web commitment.
