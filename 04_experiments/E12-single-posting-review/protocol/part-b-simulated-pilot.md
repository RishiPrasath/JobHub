# Part B: simulated pilot only (written before any persona call)

Part B of the E12 README needs 6 to 8 real job seekers recruited by the owner. It is **Not run with participants**. Every Part B threshold is reported as **inconclusive (not run)**.

What is run instead is a small SIMULATED pilot of the instrument, using personas made by tools/persona_creator.py (role: agents/roles/19_persona-creator.md). All results from it are labelled simulated. They cannot satisfy or fail any Part B threshold and cannot raise any need level.

## Design
- 6 personas, kind `job_seeker`, brief asks for variety including skimmers and low digital comfort. Creator and agent model: openai/gpt-oss-20b (own rate-limit bucket; leaves the gpt-oss-120b budget for Part A).
- 3 postings: E12-P04 (manual, warehouse), E12-P07 (clerical, customer service; has a real shift-time contradiction), E12-P10 (gig, delivery rider). Every persona sees all three, in a rotated order (persona i starts at posting i mod 3).
- For each persona and posting, in this fixed order (so there is an order effect; stated limitation):
  1. RAW: the persona gets the raw posting lines and answers: gaps (what is missing, conditional or conflicting), the first question they would ask, decision.
  2. WORKSHEET: the same persona gets the guarded AI worksheet for that posting and, per item, answers accept / edit / reject (with the edit or reason), lists any further gaps, the first question, and a decision.
- The worksheet is built from the actual gpt-oss-120b run-1 output for that posting in Part A (the claim list: state, text, source line, owner; plus the questions). One **planted wrong item** is inserted at a seeded random position, not flagged:
  - E12-P04: unsupported claim "The medical benefit covers the employee's dependants." (the posting says only "medical").
  - E12-P07: unsupported claim "The job is permanent." (the posting says "Full time" only).
  - E12-P10: false conflict "The 'up to S$3,500 a month' headline conflicts with S$4.50 per delivery." (the two statements are consistent: one is a maximum and one is a unit rate).
  Planted items are chosen and frozen here, before the pilot.
- The manual-worksheet condition (condition 2 in the README) is not simulated: a persona has no real effort or time, so a comparison of effort between conditions would be meaningless.

## Measures recorded (all simulated)
- Gold gaps found in the RAW step and in the WORKSHEET step, matched with the same kw regexes as Part A plus the rater's reading of a sample. Difference in percentage points (compare only to the README's +25 points for orientation).
- Whether the planted error was caught: the persona rejects or edits that item, or names it as wrong in its notes.
- Accept / edit / reject counts per item, and the share of items accepted untouched (skim indicator, FEAT-004), by persona.
- Not measured: time, ratings of clarity/trust/effort (a simulation has no real time or trust), the one-week follow-up (FEAT-003), reuse intent as evidence.

## What the simulation cannot show
It cannot show whether real people find more gaps, catch the planted error, accept items untouched, or ask an employer anything. The personas are language-model outputs; a model asked to act like a skimmer may over- or under-act it, and a persona that "catches" the planted item may do so only because the model reads the whole prompt carefully. A pass in this pilot is not evidence for a pass with people. The value is only to find defects in the worksheet layout, the planted-item design and the task wording before participants are recruited.
