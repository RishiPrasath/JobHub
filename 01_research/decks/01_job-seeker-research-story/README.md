# The work behind getting a job

A self-reading research briefing for the JobHub owner and clients learning the domain before product analysis. **48 slides: 30 in the main story and 18 in the appendix.** Research cutoff: 19 October 2026. Current export: **v8**. Independent targeted v8 readback passed; final owner acceptance remains outstanding.

## Start reading

Open `index.html` directly in Chrome or Edge. It is a single offline file with embedded slide images, selectable/reflowing text, explanations and sources. No Microsoft Office, account, server, installation or upload is needed. External original-source links need internet access; repository evidence links depend on keeping the repository alongside the deck.

- **Previous / Next**, arrow keys or the slide selector navigate.
- **Readable text** or R switches from slide visuals to a reflowing HTML reading format.
- **Explanation and sources** or N opens the current slide's notes.
- **Show all** displays the full briefing. Combine it with readable text for continuous reading.
- **Print / PDF** opens the browser print dialog. PDF printing has not been visually tested.

For desktop editing, use `jobhub-domain-brief-v8.pptx`. Text, seven tables and explanatory diagrams are native/editable slide objects; the two illustrations are embedded images. LibreOffice Impress is a free alternative to Microsoft Office, but this deck was not tested inside either application. The original v5 remains unchanged. v6 and v7 are prior Round03 candidates retained before the independent-review corrections.

## Story and editorial approach

The briefing follows job-seeker decisions rather than research-run chronology:

1. Encountering an opportunity and understanding the journey.
2. Distinguishing preparation effort from conditions software cannot change.
3. Investigating legitimacy and fit, then expressing real experience.
4. Understanding varied AI use and different experimental outcomes.
5. Preparing for interviews, comparing pay and considering negotiation.
6. Returning to unfinished work and comparing existing alternatives.
7. Recognising evidence limits and discussing a bounded next task.

Slides 1–22 explain the earlier-round evidence. Slides 23–27 add Round03's industry/occupation distinctions, six-context comparison, ghost-posting meanings and historical local case, verification questions, and implications/limits. Existing limits, a candidate test and closing remain at 28–30.

The appendix preserves round history, video limitations, AI-era development and unresolved provider/platform choices at 31–34. Slides 35–47 visibly cover all 13 industry profiles in S01–S13 order: six deeper inquiries (S02/S03/S05/S07/S08/S10) and seven breadth-only summaries. The evidence guide is last at 48. The profile text is available in HTML reading mode and `slides.md`. These are bounded summaries, not fictional personas, customer segments or sector rankings. The illustrations and resume examples are fictional and labelled.

The [storyboard](storyboard.md) records the teaching purpose and transition for every slide. The [claim map](claim-map.md) links messages and boundaries to evidence records. Source identifiers such as P01 are local to a run; main-story P/D/C/I/V identifiers refer to the expanded Round 02 run unless explicitly qualified.

## Research audit

Three parallel specialists divided the review into non-overlapping primary responsibilities:

- [Baseline audit](audit-baseline.md): all Round 00 runs and promoted thematic results, with sampled original-source checks.
- [Public and internal evidence audit](audit-public-and-internal.md): all Round 01/02 files and repository evidence, including all ten SRT caption texts, with selected original-source checks.
- [Story and audience audit](audit-story-and-audience.md): strategy, drafts, research intent/instructions, decisions, future plans and the earlier briefing.

The combined inventories record **136 research files outside presentations: 126 Markdown files and ten SRTs**, at the 18 October audit. These are historical coverage counts, not independent sources, research participants or an audit of every current file. The verifier reconstructs that exact dated set from explicit inventories. One historical Round03 placeholder path has since moved; new files and current byte changes do not retroactively expand that audit.

The separate [Round03 inspection record and file manifest](audit-round3.md) records 38 locally inspected files, distinguishing full report reads from selected JSON source-record inspection. The master maps new claims to 49 qualified source records with original URLs, dates, passage locators and limitations. This presentation task performed no new web retrieval or original-source verification. The research reviewer checked the integration and six deep reports, but did not independently review all 13 short profiles or the slides. The [independent deck review](review-round3.md) prompted four correction groups adopted in v8. Its final targeted v8 readback passed all four, using eight individual images plus JSON/record checks; this does not imply a repeat review of every final slide or owner acceptance. Its residual README-v7 observation was checked against the live handoff and is stale: the current export and editing filename are v8.

The 2018 translator-ad case and the Income account published on 31 December 2020 remain historical. The Wild Rice notice is dated 21 November 2025 with December 2025 audition deadlines, not a live opportunity. The international machinist supplement does not resolve Singapore trades coverage. No current Singapore ghost-job rate or automatic deception score follows.

The team reviewed the repository's sanitised internal-process records. It did not re-open the original private drive documents or re-run their workflows. The original public sources received selected spot checks, not a full independent replication. Caption inspection is not listening to or visually analysing video. Historical fictional comparisons and unstarted future rounds remain distinct from empirical findings.

Independent evidence review informed revisions to statistical denominators, accessible rehearsal formats, the scope of prior policy inspection, source namespaces and the distinction between external study results and JobHub's unmeasured benefit. The [independent visual review](review-new-deck.md) includes the final targeted readback: its four communication corrections are resolved. Additional revisions shorten crowded takeaways and translate internal terminology. Reader comprehension remains untested.

## Maintain and rebuild

`slides.json` is the master content. `build.mjs` generates the editable deck, embedded-image HTML, `slides.md`, storyboard and claim map. Markdown is Marp-compatible source, not a separately tested Marp export. Changes made directly in a desktop presentation application do not synchronise back automatically.

The generator uses Codex's bundled `@oai/artifact-tool`, presentation helpers and Python. Content and HTML are portable; the build environment is not an independent open-source presentation engine. Override `JOBHUB_RUNTIME_ROOT` and `JOBHUB_PRESENTATION_SKILL` when those bundled paths change. No substitutes were installed.

From the repository root in PowerShell, choose a new export version to preserve validated files:

```powershell
$env:JOBHUB_DECK_REVISION = 'v9'
& 'C:/Users/prasa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' './02_research/07_presentations/01_job-seeker-research-story/build.mjs'
& 'C:/Users/prasa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' './02_research/07_presentations/01_job-seeker-research-story/verify.mjs'
```

Update this README's current export only after review. Build candidates, rendered previews, prior drafts and validation receipts belong in the ignored sibling `.build/01_job-seeker-research-story/` folder. The earlier 21-slide briefing remains untouched in `../00_research-findings/`.

Use `verify.mjs --check-only` for validation without writing a receipt. The verifier derives slide, main-story and table counts from the master; it preserves navigation, embedded-image and offline-link checks. It reports the historical baseline separately from current files and the Round03 manifest. New files receive no implied inspection status. If parent status edits change a manifest snapshot, inspect the change and refresh its hash explicitly. [Update and handoff plan](round3-update-plan.md).

## Agent and assets

Use the [Research Presentation Strategist and Designer](../../../_agents/18_research-presentation-strategist.md) for future briefings. It is a reusable role definition integrated into the repository agent catalogue and instructions, not an installed presentation application or a separate native runtime registration. For parallel work, provide that role file and a bounded task to a specialist.

The [asset record](ASSETS.md) contains both final illustration paths and exact prompts. The built-in image tool created them. Its fictional editorial style supports the learning sequence without serving as source evidence.

## Verification boundaries

The authoring workflow rendered all 48 slides. Final v8 file checks passed package integrity, geometry, declared fonts, seven native tables and re-import, with zero layout findings or warnings. All additions received individual visual inspection; final changed previews were re-inspected and the whole deck scanned. The HTML includes those slide PNGs plus real text and claim/source notes. Static tests cover dynamic counts, local links, image dimensions, navigation/reading/print logic, offline dependencies, profile depth labels and local claim-record metadata. Historical baseline coverage and Round03 inspection remain distinct. Receipts and the contact sheet are in `../.build/01_job-seeker-research-story/v8/`.

Actual browser rendering, printing, assistive-technology compatibility and opening in Microsoft Office/LibreOffice were not tested. The app's automated local-file browser preview was blocked by URL policy; no workaround server was used. Neither visual inspection nor package checks establishes accessibility conformance or reader comprehension. No product scope or privacy implementation is accepted by creating this deck.
