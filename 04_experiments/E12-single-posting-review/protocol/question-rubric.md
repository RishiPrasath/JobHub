# FEAT-003 question-quality rubric (written before any question was rated)

Rater: Claude (an AI model), not a human or HR/legal reviewer. This is a stated limitation: the ratings are an AI's reading of the four checks against gold labels that the same AI wrote before the run. They are not independent of each other.

Unit: every distinct question string in a model output: each entry in `decision_changing_questions` plus each non-null `claims[].verification_question`, de-duplicated by exact (case-insensitive, trimmed) text within one output. Every question from every run (gpt-oss-120b run 1 and run 2, qwen run 1) is rated.

A question passes only if all four checks pass. Each check is yes/no.

## Check 1: targets a decision-critical gap
Yes only if the question asks about a gap that is listed in the frozen gold labels for that posting with `critical: true`. The rater records the gold gap ID. A question that asks about a gold gap with `critical: false`, a gap not in the gold file, a fact the posting already states, or something generic ("Can you tell me more about the role?") is No. Sensitivity analysis (reported separately, not the headline): the rater may mark a non-gold question as "unlisted but critical" when it plainly could change continue/investigate/decline; the headline figure counts these as No.

## Check 2: needs the employer; a public lookup could not answer it
Yes if the gold gap has `lookup: "none"` (only the employer can answer), or the question asks for something specific to this employer or role even though a general official rule exists. No if the gold gap has a lookup source (ACRA, MOM EA directory, PLRD security agency list, MOH licensed-facility list, and so on) and the question asks the employer for what that lookup would establish (for example "is the agency licensed?"). Those items belong to FEAT-001 as lookups.

## Check 3: neutral tone
Yes if it reads as an ordinary candidate question. No if it accuses or implies bad faith or fraud ("are you a scam", "why are you hiding...", "prove you are genuine"), uses the words scam, fake, fraud, illegal, suspicious, or demands documents the employer has no reason to give at this stage, or pressures ("answer immediately").

## Check 4: right official route named, where one exists
Applies only when the gold gap has a `route` (an official source exists for the point, for example the MOM Progressive Wage Model, MOM key employment terms, MOM Employment Agency directory, CPF Board, PDPC NRIC guidance, MOM Platform Workers Act guidance). Yes if the question text (or the claim it is attached to) names that route or an equivalent official body. No if a route exists and the question does not name it. If the gold gap has `route: null`, the check is Not Applicable and counts as Yes. Pass-rates are therefore reported with and without N/A counted, so the effect is visible.

Caveat on routes: route labels in the gold files come from the author's (an AI's) general knowledge of Singapore guidance, not from a live check of the official pages. They are plausible, not verified.

## Recording
Ratings are written to runs/<run>/scoring/question-ratings.json as {qid: {gap, c1, c2, c3, c4, na4, note}} by the rater after reading the question and the gold file. Ratings are never edited after scoring is computed; a re-rating is a new file.
