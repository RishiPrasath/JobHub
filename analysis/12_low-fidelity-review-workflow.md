# Low-Fidelity Single-Posting Review Workflow

Status: prepared and exercised as an analyst walkthrough

Date: 2026-10-27

## Purpose

This is the smallest workflow to test before choosing a first JobHub build scope. It helps a job seeker decide whether one posting deserves more time while keeping source evidence, uncertainty and human decisions separate.

## Workflow

```text
1. Open posting snapshot
   -> 2. Orient to source and capture date
   -> 3. Review evidence sections
   -> 4. Inspect and correct claims
   -> 5. Review unknowns and contradictions
   -> 6. Select decision-changing questions
   -> 7. Choose next action and rationale
   -> 8. Save and resume safely
```

## Step 1 — Open the posting snapshot

Show:

- posting ID;
- source/platform;
- source ownership where known;
- original title and employer identity as displayed;
- URL or reference;
- capture date;
- stale or unavailable-source state;
- original source text or captured evidence.

The original snapshot must remain available even if later corrections are made.

## Step 2 — Review evidence sections

Show the following sections independently:

| Section | Allowed states |
|---|---|
| Role identity | covered / unknown / not visible / conflicting |
| Duties | covered / unknown / not visible / conflicting |
| Qualifications | covered / unknown / not visible / conflicting |
| Work conditions | covered / unknown / not visible / conflicting |
| Compensation | covered / unknown / not visible / conflicting |
| Compensation rules | covered / unknown / not visible / conflicting |
| Application process | covered / unknown / not visible / conflicting |
| Employer context | covered / unknown / not visible / conflicting |
| Contradictions | covered / unknown / not visible / conflicting |
| Unknowns | covered / unknown / not visible / conflicting |

No overall completeness percentage should replace these section states.

## Step 3 — Inspect and correct claims

Each material claim must show:

- claim text;
- source locator;
- source owner;
- claim state;
- review status;
- optional verification question.

The reviewer must be able to:

- accept;
- edit;
- reject;
- annotate;
- open the source;
- undo or restore the original draft.

## Step 4 — Review uncertainty

The workflow must keep these distinct:

- employer-authored facts;
- platform-generated signals;
- unknown or not-visible information;
- contradictions;
- AI suggestions;
- the user’s decision.

## Step 5 — Choose questions

Show only questions that could change the user’s next action. Questions must be linked to an unresolved claim or section.

Examples:

- What are the actual duties?
- How is the exact rate determined?
- Who is the legal employer?
- What happens during or after the interview?

The workflow must not automatically contact the employer or answer the question on the user’s behalf.

## Step 6 — Record a decision

Allowed actions:

- continue;
- investigate;
- save;
- pause;
- decline.

The user records a short rationale tied to a fact, unknown or contradiction. The system must not convert the action into a fit, scam or hiring verdict.

## Step 7 — Resume and recovery

On return, restore:

- original source snapshot;
- captured date;
- raw AI output;
- accepted, edited and rejected claims;
- unresolved questions;
- decision and rationale;
- stale-source status.

## Low-fidelity test tasks

For each posting, a reviewer should be able to:

1. identify what the role appears to be;
2. identify the most important missing information;
3. locate the source for consequential claims;
4. distinguish platform signals from employer facts;
5. identify at least one decision-changing question;
6. correct or reject a misleading AI suggestion;
7. choose a next action and explain it;
8. resume after an interruption without losing the review state.

## Acceptance criteria for a first prototype

- No consequential claim is accepted without a source locator or explicit unknown state.
- Contradictions remain visible rather than being silently resolved.
- Platform signals cannot be mistaken for employer facts.
- A user can distinguish AI suggestions from source evidence.
- A user can correct, reject, undo and restore claims.
- The decision and rationale remain user-owned.
- No external action is available from the review flow.
- The workflow remains understandable when duties, employer context or compensation rules are missing.
