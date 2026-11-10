# Part C: simulated pilot, rubric (frozen before any persona call)

SIMULATED. Personas created by tools/persona_creator.py are language-model simulations. This pilot cannot satisfy any Part C threshold (the plan needs 6 to 8 real job seekers) and cannot raise a need level. It only pilots the stimuli and the coding rubric and stress-tests the wording.

## Design
- 6 personas (kind job_seeker, mixed digital comfort, time pressure and trust), created from a fixed brief.
- Each persona is shown the 6 stimuli in data/partC_stimuli.json in a rotated order (Latin square: persona i starts at stimulus i).
- One call per persona (agent model openai/gpt-oss-20b, reasoning effort low, temperature 0.7). Reply format: JSON object keyed by stimulus id with free-text fields "meaning" (what it means about the employer) and "next" (what they would do next). No yes/no cue questions are asked.

## Coding (one coder: the specialist, an AI; no second coder, stated as a limitation)
For each answer:
- S2 (impersonation) CORRECT if the answer says the warning is about scammers or fraudsters imitating the company, or the company being a target, and does not say or imply the company itself did wrong. INCORRECT if it reads the item as misconduct by the company, or as a reason to avoid the company for what it did, or is unclear which.
- S4 and S5 (nothing found) NOT-CLEAN-TREATING if the answer says only that nothing was seen in the sources checked, or keeps some doubt, or plans more checks. CLEAN-TREATING if it calls the employer safe, clean, verified, fine, legitimate or good to go with no caveat. Scored separately for S4 and S5.
- S6 (non-employment) EMPLOYMENT-FLAG if the answer takes it as a sign of a bad employer or a reason not to apply because of it; NOT-FLAG if it says it is not about employment or is a weak or neutral signal.
- S1 and S3: record whether S3 (complaint alert) is read as a regulator finding; S1 should be read as a confirmed regulator action.
- Record each next-step in a few words.

## Reporting
Counts per measure out of 6, labelled simulated. The Part C thresholds are NOT evaluated (Not run with participants).
