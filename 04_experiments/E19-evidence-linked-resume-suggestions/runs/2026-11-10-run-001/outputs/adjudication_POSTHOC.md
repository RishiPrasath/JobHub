# Post hoc adjudication of displayed M2 suggestions (AI reviewer, not a human)

Made after the automated scoring, by the same AI specialist that wrote the gold labels, by reading every displayed M2 suggestion in `review_dump.md` (qwen 47, gpt-oss-20b 28). It is not independent of the gold labels and is not a pass condition. The automated scorer numbers stay the primary figures.

Labels: GAP-TIED = a true fact shown against a requirement whose gold status is `gap` (the suggestion implies the requirement is met); BORDERLINE = wording slightly stronger or less contextual than the ledger entry; OK = faithful.

## qwen/qwen3.8-27b, M2, run 1 (47 displayed)

| Set | Req | Text (shortened) | Label | Why |
|---|---|---|---|---|
| P02-B | R1 | Diploma in Business Administration, Eastside Polytechnic | GAP-TIED | Requirement is an Automotive Nitec or diploma. Fact is true, but shown as if it answers the requirement. |
| P02-B | R4 | Work 3 days a week | GAP-TIED | Requirement is a 5.5-day week. Fact is true and irrelevant to it. |
| P03-A | R4 | Full-time role at Harbourline Freight | GAP-TIED | Requirement is availability 2 to 3 weekdays. A "full-time" fact points the wrong way. |
| P08-A | R2 | Scheduled and tracked daily delivery trips for 8 vans | GAP-TIED | Requirement is leading a sales team. Adjacent fact. |
| P10-B | R2 | Counted the cash at close and balanced the till | GAP-TIED | Requirement is regular stock counts. This is the planted adjacent-skill trap, and it got through the code check. |
| P05-A | R1 | ...in a customer-facing role at Harbourline Freight | BORDERLINE | The entry is Dispatch Coordinator; "customer-facing role" is stronger than "liaised with customers about delays". |
| (other 41) | | | OK | |

GAP-TIED 5/47 = 10.6%; with BORDERLINE 6/47 = 12.8%.

## openai/gpt-oss-20b, M2, run 1 (28 displayed, 19 sets)

| Set | Req | Text (shortened) | Label | Why |
|---|---|---|---|---|
| P05-A | R1 | ...providing direct customer-facing support | BORDERLINE | Stronger than "liaised with drivers and customers about delays". |
| P09-B | R1 | Built an Excel sheet to plan the budget of a pop-up stall within a $2,000 budget | BORDERLINE | Leaves out that it was a class assignment, so it can read as event experience. The ledger entry says assignment; the wording drops it. |
| (other 26) | | | OK | |

GAP-TIED 0/28; with BORDERLINE 2/28 = 7.1%.

## Items dropped by the code check (qwen 3, 20b 1)

| Model | Set | Req | Dropped for | Fair? |
|---|---|---|---|---|
| qwen | P04-A R1 | "Over 2 years ... 1.5 years ... 2 years" | numbers 1.5 and 2 not in entries | Yes. Derived and partly invented arithmetic. |
| qwen | P05-A R2 | "...to manage daily delivery trips" | word "manage" not in cited entry | Questionable. A mild verb change. |
| qwen | P10-B R5 | "Holds Standard First Aid (CPR and AED) certification" for workplace safety | "certification" not in entry | Yes. It was an adjacent credential for a gap requirement. |
| 20b | P03-A R1 | "Maintained a shared Excel dispatch log to record daily delivery trips" | "record" not in entry | No. Harmless verb. |

## What this shows

- The code check passed no fabricated credential, employer or metric. Both models stayed faithful to the ledger text before the filter (raw automated unsupported rate 2.0% for qwen and 3.4% for 20b; the two raw flags were a derived-number item and the harmless verb "record").
- What the code check cannot see is relevance: a true fact placed against a requirement it does not answer. All five such items came from qwen and all five reached the user (gpt-oss-20b had none, but it also showed fewer suggestions: 28 against 47, and none on the two all-gap sets). Catching them needs a requirement-to-entry match step (or the user), not a fact lookup.
