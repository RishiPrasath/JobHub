# Independent UX, story and readability review

Reviewed: 18 October 2026, approximately 22:44 Singapore time. Review target: the latest **v2** visual state, comprising 25 main slides and five appendix slides.

## Verdict

The deck has a coherent visual identity and a substantially stronger opening than a conventional research readout. The two editorial illustrations, the attributed Singapore account, the opposing résumé strategies and the adjacent experiment pages create useful changes of pace. Research-round history belongs in the appendix and is correctly placed there.

**No visible hard text overlap, cut-off title, off-canvas content or table clipping was observed in the reviewed slide images.** This is a finding about these rendered images at the inspected size, not a guarantee about other exports, smaller screens or assistive technology.

The deck still needs a few targeted explanatory corrections before a client handoff. Slide 9's misleading progression is **resolved in v2**. Slide 19 retains a similar visual problem. Slide 2's opening wording is ambiguous, and slide 10 promises example wording but partly presents instructions instead. The story also needs a clearer bridge across applying, interviewing and receiving an offer. These are communication corrections, not requests to change product direction or add research claims.

For the requested captivating domain briefing, the remaining opportunity is **more explanation through a concrete example**, rather than more decoration. Most pages after the second illustration still ask the reader to process prose arranged into columns, tables or numbered text. The current draft is orderly and credible; a worked example would make it more instructive and memorable.

## Scope and version control

This is an independent UX/story/readability check using the repository's UX Expert and Research Presentation Strategist and Designer roles. It covers the visible sequence, composition, title/lead relationship, conceptual encoding, text fit and likely reading friction.

The parent is reviewing evidence and static logic. This review does **not** duplicate source verification, statistical interpretation, source-link auditing, generator inspection or navigation tests. Recommendations below concern how a reader understands what is already presented.

Inspection performed:

- Read the complete first-build `slides.json`, including titles, leads, body content, notes, purposes and transitions.
- Directly inspected **every v1 PNG, slide-01.png through slide-30.png**, individually with `view_image`.
- After the parent supplied v2, read the updated JSON objects for slides **04, 06, 09, 12, 14, 15, 16, 22, 23, 29 and 30** and directly inspected all eleven corresponding v2 PNGs with `view_image`.
- Compared SHA-256 hashes of all 30 v2 PNGs with the visually inspected v1 files. Exactly those eleven images changed. The other nineteen v2 PNGs are byte-identical to their inspected v1 counterparts.
- Rechecked the JSON and all v2 PNG hashes after inspection. None changed during the v2 review interval.

Thus **41 rendered files received direct visual inspection**, covering all 30 positions in the latest deck. This does not mean that all 30 v2 files were reopened visually: eleven were, and nineteen were covered by direct inspection of identical v1 bytes.

Latest reviewed `slides.json` SHA-256:

`ED0B457252A8C73880009EBF4B25DCA20D5480077EAE78F6E1388FE9890D9D04`

The table in the final section identifies the exact images and individual observations. These comments apply to this snapshot. Subsequent content changes require checking their new renders.

## Necessary corrections

Here, “necessary” means a correction recommended for clear client communication. It is not an independent approval/release gate or a judgment about source validity.

### R1. Slide 19 still depicts checkpoint fields as a progression

**Priority: medium. Confidence: high in the visible encoding problem.**

“Source”, “State” and “Next action” appear beneath 01, 02 and 03 on a connecting line. The lead calls this a checkpoint, and the descriptions read as information to preserve together. Numbering and connecting them instead imply successive stages or a transformation from one to another. This is the same type of mismatch the parent has now corrected on slide 9.

Prefer three unnumbered, unconnected fields within one clearly labelled fictional checkpoint example. Alternatively, if an ordered recovery procedure is intended, use actual actions such as reopening the source, checking the saved state and selecting the next task, with the sequence stated explicitly. The former better matches the current content.

Do not remove numbering indiscriminately from all diagrams. Slides 16, 24 and 28 describe procedures for which sequence has meaning. Slide 9's v2 unnumbered treatment is already suitable.

Acceptance check: a reader should identify three pieces of saved context, rather than three mandatory job-search stages. Keep the proposed-aid disclosure visible.

### R2. Slide 2's hook can sound as though the person has secured employment

**Priority: medium. Confidence: high in the ambiguity, untested in readers.**

“You found a job. Now what?” can mean receiving a job or offer. Its right-hand questions and lead actually concern discovering a vacancy. That moment matters because the deck later covers interviews and offer decisions.

Use “You found an opening. Now what?” or “A job posting caught your attention. Now what?” The first preserves the current short, engaging composition. Keep the illustrative-situation disclosure.

Acceptance check: the opening is immediately understood as the start of investigating an opportunity, without relying on the lead to correct the headline.

### R3. Slide 10 should show wording where it promises wording

**Priority: medium. Confidence: high.**

The middle column is titled “Reviewable wording”. Its first row supplies a résumé-style sentence. The next two rows instead say “Explain a real communication or problem-solving example” and “Describe the actual support provided and its outcome”. Those are writing instructions, so the page mixes a demonstrated result with tasks the reader still has to imagine completing.

Choose one teaching purpose. For a client domain briefing, show one complete, explicitly fictional example of known experience, truthful wording and an unresolved qualification. The other two rows can become prompts or secondary examples. If all three remain instructions, rename the middle column accordingly, while recognising that this would preserve the abstraction.

Do not invent a quantified achievement, credential or responsibility to make the example persuasive. Have the evidence/content owner approve any replacement wording.

Acceptance check: a reader can point to the actual rewritten sentence and explain what changed and what stayed unknown.

### R4. Make the journey transitions visible without implying an inevitable offer

**Priority: medium. Confidence: moderate, based on the full reading sequence.**

Slide 3 includes “Apply”, but the following main story goes from résumé preparation and AI studies to interview rehearsal at 16, then immediately to pay/offer evaluation at 17. The JSON transitions explain the intended handoffs, but those transitions are not themselves visible in the PNGs. A newcomer receives little help distinguishing preparing a document, submitting it, being shortlisted and receiving an offer. Return/interruption appears only after negotiation at 19.

A small visible bridge is sufficient. For example, a journey locator or short conditional sentence can identify “After an application, if shortlisted…” before interviews and “If an offer arrives…” before offer evaluation. Give the reader a brief distinction between a prepared document and a submitted application. This need not add a new slide or turn the briefing into an exhaustive procedural manual.

Also make clear that interruption can happen throughout the journey. Moving slide 19 is optional; presenting it as a cross-cutting concern is enough. Preserve the caveat about the unsubstantiated specific device-loss episode.

Acceptance check: readers can place preparation, submission, interviews and offer decisions on the map without interpreting every earlier stage as a successful funnel.

## Optional improvements with the greatest benefit

### O1. Improve the explanatory variety, not just the number of layouts

There are twelve declared layout names, but the visual families are narrower: eight `columns` pages, four `contrast` pages, five tables and five `flow` pages. Columns and contrasts are almost the same reading task with a change of heading colour. Once the second image has appeared at 12, slides 16–24 return to text-based explanations throughout.

The highest-value improvement is a single concrete example carried across the opportunity/fit/tailoring section at 7–10. An annotated fictional posting or career statement could make visible:

- what the source actually states;
- what relevance is being interpreted;
- what remains unknown and needs checking.

This would give readers a method they can explain, rather than another list of criteria. It could also satisfy R3. Label the material fictional and avoid making it look like evidence from a real application. No extra illustration, product screenshot or invented chart is needed.

Slide 8's two-column table is already a sensible genuine mapping. Slide 17's compensation categories and slide 21's alternatives also benefit from alignment. Keep tables that clarify relationships.

### O2. Keep the late main story focused on the client's domain learning

Slides 19–24 shift among a proposed checkpoint, the owner's internal process, competing alternatives, AI review costs, research limits and a proposed experiment. Each is defensible, but the sequence feels like a research/product handoff after the main domain journey has ended.

For a client-facing cut, consider moving slide 20's internal-workflow detail to the appendix or making its main-page message a short, plain-language principle. “Historical extraction problems”, “untested current runtime” and “maintenance demands” require internal project context. Their presence is relevant to an owner review but less helpful to someone learning job searching.

Consider placing slide 22's review-cost explanation directly after the AI-use discussion at 13, where slide 12 has just promised “things to check”. It would connect assistance to its practical cost before the experiments. Keep the experiment pair together. This is an editorial option, not a demand to recut the whole deck.

### O3. Give the lowest text bands more breathing room

In the **v2** renders of slides **4, 29 and 30**, the bold takeaway wraps onto two lines and ends very close to the source/limitation footer. I can still distinguish and read both; this is **crowding, not an observed collision or clipping defect**. It weakens the separation between the main message and its supporting boundary and is vulnerable to later copy expansion.

Prefer shortening the takeaway or moving it slightly upward while retaining a clearly separate footer band. Do not shrink the limitation text to solve the spacing problem. Slide 9's shortened v2 takeaway has already improved this issue there.

Some long titles and leads, particularly 21, 29 and 30, use much of the line width but remain inside the image. They do not need automatic rewriting merely because they are long. Check them again if copy changes.

### O4. Show return in the diagrams where it adds meaning

The slide 3 journey says people can revisit stages, while its diagram remains a single numbered line. Slide 16 ends at “Review”, although the explanation includes another practice step. A restrained return connection with a written label could communicate revisit/retry better than prose alone.

Keep any such addition legible and conceptually modest. Do not add a dense network, claim a measured path or imply that every person repeats every stage. The current diagrams are readable, so this is a teaching enhancement rather than a layout repair.

### O5. Translate a few abstract phrases for the unfamiliar reader

Examples include “within this corpus” on 23, “bounded task” on 24, “current runtime” on 20 and “executable Gherkin” on 28. Plain alternatives such as “in the sources reviewed”, “one small comparison”, “how the workflow operates today” and a brief explanation of automated behavior examples would reduce prior-knowledge demands.

Slide 13's “little application AI” is awkward phrasing. “Little use of AI for applications” is easier to understand. Its title could also become “People use AI in different ways”. These are optional copy refinements, not factual corrections.

## What is working and should be preserved

- **Opening and visual identity:** slides 1–2 are inviting and concrete. The dark navy, warm image palette and cream reading pages form a coherent editorial treatment. Fictional-image disclosures are visible.
- **A grounded human example:** slide 5 names a reported Singapore experience and visibly limits its evidential meaning. Its large statement creates pace without pretending to be a participant quotation.
- **Counterexamples inside the story:** slide 11 allows reuse and selective changes to remain credible alternatives, rather than treating maximal tailoring as the only correct routine.
- **Memorable experimental pair:** slides 14–15 make the result labels visible beside the numbers, and the different page treatments signal separate studies. The v2 denominator/relative-change labels fit clearly. This is a communication observation; the parent retains evidence review.
- **Inclusive rehearsal wording:** slide 16's v2 heading and accessible-alternative language avoid making one speaking format universal. The four stages remain readable.
- **A useful ending:** slide 25 has a strong typographic hierarchy and readable discussion questions. It closes the main story before the appendix and does not look like an automatic product approval.
- **No need for a wholesale visual rebuild:** the current spacing, readable tables and restrained styling give the author a sound base. Target the specific teaching problems above.

## Reading UX and accessibility limits

The visible hierarchy, generally large body copy, short blocks and explicit text labels support reading. The dark pages do not depend solely on colour to convey their main messages. Footers are substantially smaller than body text, and the source/limitation band needs particular attention when the whole slide is fitted into a small window.

These are visual observations, not contrast measurements or a WCAG conformance evaluation. I did not inspect native text objects, measure rendered font sizes, test a screen reader or evaluate keyboard/focus behavior. A PNG cannot establish reading order, alt text, selectable text or accessible source links.

The parent reports that the latest HTML uses the exact rendered PNG slides alongside a reflowing HTML transcript. That should be treated as **two reading experiences**: stable slide composition and adaptable text. This review confirms the slide-image composition only. It does not confirm transcript parity, reflow, navigation or accessibility. Actual browser preview is unavailable, and source/static navigation tests belong to the separate parent review.

The following were not opened or tested here: current `index.html`, PPTX, browser slide mode, browser transcript mode, print/PDF output, presentation software, mobile/zoom layouts or assistive technologies. The two artwork assets were viewed as part of slides 1 and 12, not independently at their source resolution. No real readers participated. “Captivating”, ease of understanding and likely confusion are professional UX judgments that still need reader feedback.

## Exact visual inspection inventory

Paths are relative to this review file. **v1 = v2-identical** means that the linked v1 image was directly viewed and its corresponding v2 image has the same SHA-256 hash. **v2 rechecked** means that both versions were directly viewed and the observation below uses v2.

| Slide | Latest title | Exact directly viewed image used for latest judgment | Visual/story observation |
| --- | --- | --- | --- |
| 01 | The work behind getting a job | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-01.png) | Strong human opening. Title, subtitle and fictional disclosure are readable over the dark area. No visible clipping. |
| 02 | You found a job. Now what? | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-02.png) | Clear contrast and hierarchy. Vacancy/employment ambiguity remains: R2. Right-side questions fit. |
| 03 | The job seeker's journey | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-03.png) | Six stages and short prompts fit clearly. Return is explained in prose rather than in the line diagram: O4. |
| 04 | What this research can tell us | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-04.png) | Body remains clear. Revised takeaway wraps close to the footer: O3. No actual overlap observed. |
| 05 | The workload extends beyond the resume | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-05.png) | Case page changes pace successfully. Large left statement and right explanation fit without crossing. |
| 06 | Preparation cannot remove every barrier | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-06.png) | Columns remain readable. Longer revised limitation fits the footer band without clipping. |
| 07 | Which opportunities deserve effort? | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-07.png) | Clear questions and hierarchy. A worked example could make the distinction more tangible: O1. |
| 08 | A warning sign starts a check | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-08.png) | Useful mapping table with readable row labels and checks. No visible table overflow. |
| 09 | Fit is more than a keyword score | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-09.png) | Prior numbers and connectors are gone. False-progression issue resolved; shorter takeaway fits on one line. |
| 10 | Truthful tailoring begins with facts | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-10.png) | Table fits. Two middle cells are instructions rather than finished example wording: R3. |
| 11 | People report different resume strategies | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-11.png) | Readable opposing approaches and an important counterexample. Remains prose-heavy but coherent. |
| 12 | AI enters an already demanding process | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-12.png) | Explicit four-line heading and short fictional-art footer read clearly. Good visual transition; no title/image collision. |
| 13 | How people use AI differs | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-13.png) | Comfortable two-column fit. A small wording refinement would improve plain-language flow: O5. |
| 14 | Clearer writing helped in one experiment | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-14.png) | Strong numerical emphasis with adjacent outcome label. Scope text and revised footer fit. |
| 15 | Cheaper writing did not guarantee more matches | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-15.png) | Both revised two-line metric labels fit. Matching outcome remains prominent and separate. No overlap. |
| 16 | Explaining real experience in interviews | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-16.png) | Four genuine practice steps fit, including the accessible-alternative wording. Optional retry loop: O4. |
| 17 | Pay needs a like-for-like comparison | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-17.png) | Compensation table is legible. Transition from interviews to an offer needs conditional context: R4. |
| 18 | Negotiation depends on the offer | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-18.png) | Three points per column fit; takeaway and limitation remain distinct. No clipping. |
| 19 | Returning to unfinished work | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-19.png) | Clear dark-page layout, but checkpoint components still look like an ordered flow: R1. |
| 20 | What the internal workflow contributes | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-20.png) | Text fits. Internal terminology and owner-specific detail interrupt a general client domain story: O2/O5. |
| 21 | Existing alternatives cover parts of the journey | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-21.png) | Long title stays within the image. Row alignment makes the category comparison readable. |
| 22 | Convenience has a review cost | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-22.png) | Revised long footer fits. Useful message could sit closer to the AI-use pages: O2. |
| 23 | The evidence has clear boundaries | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-23.png) | Clear supported/unknown distinction. Revised scope footer is readable at inspected size. |
| 24 | A bounded task could test usefulness | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-24.png) | Numbered setup/comparison sequence is appropriate. Proposal status is visible. Plain-language title could help: O5. |
| 25 | What should useful help preserve? | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-25.png) | Strong, readable closing composition. Discussion questions fit below the main message. |
| 26 | Appendix: how the research rounds differ | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-26.png) | Administrative chronology is correctly confined to the appendix. Three-row table fits. |
| 27 | Appendix: what the videos contributed | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-27.png) | Contributions and limits are easy to locate. No visible overflow. |
| 28 | Appendix: small, explainable development steps | [v1 = v2-identical](../.build/01_job-seeker-research-story/v1/previews/slide-28.png) | Ordered development sequence is appropriate. Gherkin terminology may need a gloss: O5. |
| 29 | Appendix: platform and provider choices stay open | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-29.png) | Long title fits. Two-line takeaway remains close to the revised footer: O3. |
| 30 | Appendix: evidence guide | [v2 rechecked](../.build/01_job-seeker-research-story/v2/previews/slide-30.png) | Source-category legend fits. Two-line takeaway crowds the footer; source navigation itself is outside this review: O3. |

Additional content inspected in this review: `AGENTS.md`, `_agents/README.md`, `_agents/13_ux-expert.md`, `_agents/18_research-presentation-strategist.md`, the first-build slide JSON and the eleven latest changed slide objects described above. A quick memory-registry search supplied historical orientation only; judgments here are based on the actual new renders and slide content. Earlier presentation-skill guidance was retained from this conversation, not reread as a new source. No run evidence or other reviewers' draft findings were opened for this pass.

## Handoff and changes

Recommended next action: consider R1–R4 as the remaining communication corrections, then choose whether O1's worked example and O2's client-focused sequencing are worth a small revision. Re-render affected slides after changes, especially any page with a long takeaway. Reader comprehension and final acceptance remain with the owner.

Only `review-new-deck.md` was created by this reviewer. No slide content, generator, HTML, artwork, existing audit, rendered image or other agent's file was edited. No browser, export, evidence or user-testing success is implied by this review.

## v5 targeted visual readback

Reviewed 18 October 2026, approximately 22:50 Singapore time. This addendum supersedes the earlier **open R1–R4 statuses** for the specific communication corrections below. The preceding v1/v2 observations remain a historical review record.

**Result: R1–R4 are resolved in the five inspected v5 slides.** The current JSON entries and rendered text agree on the requested corrections. No visible overlap, clipping, cut-off text or new readability problem was observed in these five images.

| Correction | Exact v5 image directly inspected with `view_image` | Readback |
| --- | --- | --- |
| R2: explicit vacancy opening | [slide-02.png](../.build/01_job-seeker-research-story/v5/previews/slide-02.png) | The headline now says “A job opening. Now what?” It clearly introduces a vacancy. The headline, lead and right-hand questions fit without colliding. **Resolved.** |
| R3: completed fictional rewrites | [slide-10.png](../.build/01_job-seeker-research-story/v5/previews/slide-10.png) | All three middle cells now contain completed sentences: maintaining daily inventory records in Excel, responding to delivery-status enquiries, and demonstrating the inventory spreadsheet to a colleague. The lead and footer explicitly identify fictional material, and the unconfirmed qualifications remain separate. Wrapped text fits within all table cells. **Resolved.** |
| R4: application-to-interview bridge | [slide-16.png](../.build/01_job-seeker-research-story/v5/previews/slide-16.png) | The visible lead says “After applying, if shortlisted: rehearse in a format you can use.” It supplies the missing conditional bridge. The four practice steps and accessible-alternative wording remain readable. **Resolved for the interview transition.** |
| R4: conditional offer transition | [slide-17.png](../.build/01_job-seeker-research-story/v5/previews/slide-17.png) | The visible lead starts “If an offer arrives”. It introduces offer comparison without implying an inevitable successful outcome. The lead and compensation table fit clearly. **Resolved for the offer transition.** |
| R1 and remaining R4 state distinction | [slide-19.png](../.build/01_job-seeker-research-story/v5/previews/slide-19.png) | Source, State and Next action are three unnumbered, unconnected fields. The lead explicitly places interruptions at any stage. State includes submission confirmation, and the takeaway says “Saved or prepared does not mean submitted.” The proposed-aid limitation remains visible. No false progression or text collision remains. **Resolved.** |

Scope was deliberately limited to these **five v5 PNGs** and their **five current `slides.json` objects**, including the relevant leads, body text, notes and disclosures. No other v5 slide was visually reopened. No additional research, evidence validation or broad optional-design review was performed. Optional O3/O5 changes elsewhere remain with the parent's render review; this addendum does not certify them.

All earlier limitations still apply: this is inspection of rendered slide images, not actual browser/transcript/reflow testing, print/PDF or PPTX compatibility testing, assistive-technology evaluation, measured contrast or user comprehension testing. The parent reports browser preview remains unavailable. Final acceptance remains with the owner. Only this addendum was appended to `review-new-deck.md`; no deck, generator, content JSON or other agent's work was edited.
