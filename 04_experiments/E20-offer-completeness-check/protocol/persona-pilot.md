# Simulated pilot of the Part A guide and a Part C style reaction

SIMULATED. Six personas made by `tools/persona_creator.py` (creator model `openai/gpt-oss-120b`, answering model `openai/gpt-oss-20b`). They are language-model inventions, not people. This pilot tries the interview guide and the check's wording. It cannot be Part A or Part C evidence and evaluates no Part A or Part C threshold.

## Personas requested (brief in `harness/persona_pilot.py`)

- 1 manual or shift worker with an offer in the last 12 months
- 2 office professionals (one skims, one reads carefully)
- 1 career switcher
- 2 foreign professionals (one in the Employment Pass process, one already in Singapore)

## Part A guide as piloted

The six questions of the README design, each asked once, plus a seventh meta question ("which question was hard, unclear, repetitive or leading?") added only for the pilot.

1. What they received (verbal, email, letter, contract, handbook), when, and the response deadline.
2. What they checked, how, and with whose help.
3. Whether anything differed from what was advertised or agreed, or was missing, and what they did.
4. What they wish they had known or asked.
5. Whether they would have used a check at offer stage, and what would have stopped them.
6. What they are willing to share (a redacted letter, only the terms, nothing).

## Part C style reaction

Each persona is shown synthetic letter L17 (a multinational-style email offer) and the plain-language report that `harness/render_report.py` makes from the gpt-oss-20b run 1 output for L17. L17 was fixed as the shown letter before any output existed. They answer six questions: what they notice; what is new; what the report says about the employer (is it saying the employer did something wrong?); what they would do next; would they use it at the next offer; what is confusing.

## How the answers are summarised

By the specialist reading each answer and coding it by hand (themes, misreadings, question problems). No threshold is applied.
