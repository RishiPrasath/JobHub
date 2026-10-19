# Public and internal evidence audit: Rounds 01 and 02

Audit date: 2026-10-18, Asia/Singapore. Author: Evidence Synthesizer. Status: evidence and presentation handoff; neither owner acceptance nor a product decision.

## 1. Inventory first: scope and inspection boundary

The assigned corpus contains **64 existing files, 704,368 bytes: 54 Markdown files and ten SRT files**. This is the complete file inventory of Round 01, Round 02, and `02_research/05_evidence`, including hidden/ignored files found by recursive filesystem enumeration. It is a subset of the parent audit's reported 136 research files outside presentations (126 Markdown and ten SRT), not a claim that the whole research repository has only 64 files. Root instructions, the backlog and future-round placeholders belong to the parent's separate coverage; selected upstream context used here is listed below.

All 54 assigned Markdown files were read. All ten captions were parsed, their normalized text read in bounded batches, and consequential examples revisited with their original timestamps. Truncated terminal output was followed by smaller reads. Caption inspection is **text inspection, not listening or screen verification**. SHA-256 checks matched all ten capture-log hashes; 3,587 cues were recovered. No unreadable assigned local file or byte-identical duplicate was found. Repeated sources and summaries are evidential dependencies, even when files differ.

No private drive was re-scanned. The private source documents and historical JSON outputs described in the repository are **not present as raw files in this assigned corpus**. This audit read the two repository process reviews and their safe inventories; it did not reopen their private originals. Statements about those originals remain attributed to the earlier reviewer. No participant, employer, author, or other chat was contacted. No external write, download, workflow execution, implementation, commit, or push is part of this audit.

Classification used below:

- **Read:** substantive text inspected; caption details and external spot-check boundaries are explicit below.
- **Metadata:** existence, reference, schema/allowlisted description, or navigation only; not a substantive reread of the original.
- **Duplicate:** byte-identical local copy, or explicitly identified repeated source material. None of the 64 files is a byte-identical copy; source-level repetitions are separately mapped.
- **Unreadable:** an attempted substantive read failed. None locally; selected external failures are recorded in section 5.

### 1.1 Exhaustive assigned file inventory

Prefixes are exact repository-relative directories:

- `R1` = `02_research/03_research-rounds/01_public-web-user-insights`.
- `R2` = `02_research/03_research-rounds/02_synthetic-workflow-selection`.
- `E` = `02_research/05_evidence`.

`R1/runs/2026-10-18-web-based-user-insights` is abbreviated `R1/W`; `R2/runs/2026-10-18-synthetic-workflow-comparison` is `R2/H`; `R2/runs/2026-10-18-pain-practices-and-guidance` is `R2/X`. These aliases qualify source IDs throughout this audit; an unqualified S01, D01, I01, or C01 would be ambiguous.

| Exact path using the prefixes above | Class | Evidence role / audit note |
|---|---|---|
| R1/README.md | Read | Completed bounded public pass; no priority validation. |
| R1/round-brief.md | Read | Planned decision, public-only scope and completion rule. |
| R1/run-index.md | Read | One executed run; no additional run inferred. |
| R1/round-synthesis.md | Read | Current unranked synthesis and targeted H3 stop disposition. |
| R1/decision-gate.md | Read | Close bounded pass; next AI-practice question; no scope acceptance. |
| R1/W/README.md | Read | Run status and planned file contract. |
| R1/W/brief.md | Read | Planned passes and stopping conditions; full stop rule uncertified. |
| R1/W/query-plan.md | Read | Q1–Q9 retrieval portfolio, source independence and contrary queries. |
| R1/W/query-log.md | Read | Actual query strings, failures, exclusions and narrow H3 stop check. |
| R1/W/sources.md | Read | S01–S12, plus screened-not-retained sources. |
| R1/W/observations.md | Read | O01–O12 source reports; not observed JobHub use. |
| R1/W/findings.md | Read | H1/H2/H3 comparison; device-loss chain not established. |
| R1/W/limitations.md | Read | Transfer, denominators, retrieval and measurement boundaries. |
| R2/README.md | Read | Expanded current scope; historical folder slug retained. |
| R2/round-brief.md | Read | Ten objectives, authorised expansion and historical boundary. |
| R2/run-index.md | Read | Both historical and expanded runs preserved. |
| R2/query-plan-draft.md | Read | Adopted portfolio, not an unexecuted research result; stale closing instruction remains. |
| R2/round-synthesis.md | Read | Expanded pass and independent-review disposition. |
| R2/decision-gate.md | Read | Proposed single-task experiment; acceptance remains open. |
| R2/H/README.md | Read | Completed fictional paper comparison. |
| R2/H/brief.md | Read | Historical setup; still says in progress / Round 01 incomplete. |
| R2/H/sources.md | Read | Reuses Round 00; no new external collection or private inspection. |
| R2/H/hypothesis-cards.md | Read | Unranked design hypotheses and manual alternatives. |
| R2/H/scenario-cards.md | Read | Fictional Jordan/Mira, postings and stress events. |
| R2/H/flows.md | Read | Proposed text flow; contains preserved reasoning/label errors. |
| R2/H/rubric.md | Read | Predeclared D1–D12, hard stops and challenge cases. |
| R2/H/observations.md | Read | Agent paper traces A1–A7/B1–B7 and post-review category changes. |
| R2/H/ux-review.md | Read | Independent Codex document critique, not participant testing. |
| R2/H/findings.md | Read | Preserves B6 failure and A4 absence ambiguity; no workflow winner. |
| R2/H/limitations.md | Read | Untested software, recovery, fairness and warning branches. |
| R2/X/README.md | Read | Current bounded pass; review corrections recorded. |
| R2/X/brief.md | Read | All ten objectives and distinct file ownership. |
| R2/X/query-plan.md | Read | Adopted nine-family portfolio and retrieval adaptations. |
| R2/X/query-log.md | Read | 46 reported executed strings; indexes specialist logs. |
| R2/X/sources.md | Read | P/D/C/I/V namespaces and family dependence. |
| R2/X/observations.md | Read | Ten condensed observation routes; videos separately timestamped. |
| R2/X/practices-research.md | Read | P01–P12; E01–E15; screened/access records and concrete accounts. |
| R2/X/domain-research.md | Read | D01–D12; DQ01–DQ14; pay, fit and employer-language distinctions. |
| R2/X/coordinator-research.md | Read | C01/C02 primary experiments; four queries and original inspection limits. |
| R2/X/video-research.md | Read | V01–V10; timestamps, advice/accounts, caveats and statistics quarantine. |
| R2/X/youtube-discovery-log.md | Read | QV01–QV13, six URL checks, capture provenance, hashes, failures and cleanup record. |
| R2/X/internal-process-review.md | Read | I01–I16, safe S01–S25/T01–T05 inventory; original private files not reread here. |
| R2/X/rubric.md | Read | Research-quality criteria; not a JobHub performance rubric. |
| R2/X/findings.md | Read | F01–F12 integrated interpretation and proposed experiment. |
| R2/X/coverage.md | Read | Ten objectives investigated; explicit residual gaps. |
| R2/X/limitations.md | Read | Completion is bounded research completion. |
| R2/X/review.md | Read | Recorded independent review, external spot checks, corrections and read-back. |
| E/README.md | Read | Evidence repository conventions; not raw empirical material. |
| E/datasets-and-examples/2026-10-18-synthetic-workflow-check.md | Read | Prepared fictional fixture; not a model/product test result. |
| E/external/2026-10-18-ai-job-hunting-index.md | Read | Pointer to Round 00 source registers; no full source archive. |
| E/external/2026-10-18-job-search-friction.md | Read | Thirteen-record Round 00 evidence map and review limits. |
| E/external/2026-10-18-remaining-research-index.md | Read | Source-group pointer; product/UX/development/risk/Codex IDs are local to their registers. |
| E/internal-job-hunt-workspace/2026-10-18-process-review.md | Read | Earlier seven-document review plus linked trust-contract addendum; one-owner process. |
| E/external/youtube/2026-10-18-job-posting-red-flags/README.md | Read | Five supplied video IDs, dates, capture method; now correctly says four browser-export attempts. |
| E/external/youtube/2026-10-18-job-posting-red-flags/iVeoEF3bzlY.en-orig.srt | Read | V01; complete caption text; automatic. |
| E/external/youtube/2026-10-18-job-posting-red-flags/0KXDCuxi3jk.en-orig.srt | Read | V02; complete caption text; automatic. |
| E/external/youtube/2026-10-18-job-posting-red-flags/x2sgf8zlNao.en-orig.srt | Read | V03; complete caption text; automatic; suspect negation. |
| E/external/youtube/2026-10-18-job-posting-red-flags/fCd4wZQaWqo.en-orig.srt | Read | V04; complete caption text; automatic; same creator as V02. |
| E/external/youtube/2026-10-18-job-posting-red-flags/IF3McdG_dSY.en-orig.srt | Read | V05; complete caption text; automatic; commentary, not observed prevalence. |
| E/external/youtube/2026-10-18-round-02-additional/pmnY5V16GSE.en.srt | Read | V06; complete caption text; listed manual track. |
| E/external/youtube/2026-10-18-round-02-additional/N1Fm4JYae1I.en-orig.srt | Read | V07; complete caption text; automatic; same creator as V06. |
| E/external/youtube/2026-10-18-round-02-additional/ay_wtOte5Gc.en-US.srt | Read | V08; complete 653-cue caption text, including later culturally specific material. |
| E/external/youtube/2026-10-18-round-02-additional/HHGQ_QeHjF0.en-orig.srt | Read | V09; complete caption text; tutorial, no demonstrated employment outcome. |
| E/external/youtube/2026-10-18-round-02-additional/Risf_QQGX2o.en.srt | Read | V10; complete caption text; listed manual track; historical raise advice. |

Totals: R1 13; R2 34 (six round-level, eleven historical, seventeen expanded); E 17 (seven Markdown, ten captions). **Read 64; Metadata-only 0; byte-identical Duplicate 0; Unreadable 0 within these roots.**

### 1.2 Supporting context and historical/placeholder routes

These are additional to the 64-file count. A file cited by an index is not automatically substantively audited.

| Repository-relative file or referenced group | Class / inspection | Treatment |
|---|---|---|
| AGENTS.md | Read completely | Source hierarchy, human boundaries, preserve other work. |
| _agents/README.md | Read completely | Role selection; not evidence about job seekers. |
| _agents/02_evidence-synthesizer.md | Read completely | Claim classes, provenance, contradictions and uncertainty. |
| 02_research/00_research-charter.md | Read | Context only; parent owns whole-corpus instruction audit. |
| 02_research/00_research-intent-register.md | Read | Confirms expanded run and unranked hypotheses. |
| 02_research/01_research-backlog.md | Read | Context; coverage is desk treatment, not empirical closure. |
| 02_research/02_instructions/00_common-research-protocol.md | Read | Query planning and promotion boundary. |
| 02_research/03_research-rounds/README.md | Read | Current sequence/status, future rounds planned. |
| _prompts/01_round-02-synthetic-workflow-selection.md | Read | Filename retained, contents now expanded; do not infer current scope from slug. |
| 02_research/03_research-rounds/00_orientation-and-baseline/round-synthesis.md | Read | Prior orientation only. |
| 02_research/03_research-rounds/00_orientation-and-baseline/decision-gate.md | Read | Proposed transition to Round 01, historical next step. |
| 02_research/03_research-rounds/00_orientation-and-baseline/runs/2026-10-18-job-search-friction/sources.md | Read | Original URLs, thirteen source records and dependencies. |
| Same friction run: findings.md | Read | Prior H1/H2/H3 definitions and threshold distinctions. |
| Same friction run: limitations.md | Read | Earlier scope, reporting inconsistencies and withheld claims. |
| Same friction run: specialists/practices.md | Read | Five original record descriptions, denominators and source limitations. |
| Same friction run: specialists/targeted-gap-pass.md | Read | G01/G02 population distinction and method inconsistency. |
| Same friction run: specialists/domain.md, specialists/synthesis.md, specialists/workflow-review.md, specialists/product-review.md, notes.md, brief.md | Metadata: linked references identified | Not independently reread in this assigned audit; no claim of auditing all Round 00 runs. |
| 02_research/03_research-rounds/00_orientation-and-baseline/runs/2026-10-18-ai-job-hunting-workflows/sources.md | Read | Pointer register; not a new inspection of all underlying tool/study records. |
| 02_research/03_research-rounds/00_orientation-and-baseline/runs/2026-10-18-remaining-research/sources.md | Read | Register index and interpretation rules. |
| Same remaining-research run: product-market.md, ux-and-accessibility.md, development-method.md, technical-and-responsible-ai.md, codex-and-delivery.md, review.md | Metadata: linked routes identified | Broader Round 00 collection not exhaustively re-audited here. Historical flow references do not create new empirical support. |
| 02_research/04_results/00_cross-research-synthesis.md | Read | Earlier promoted recommendation; its next-step link still points to Round 01. |
| Other 04_results reports referenced by R2/H/sources.md | Metadata: source-map references | Secondary summaries; not counted as independent evidence. |
| 02_research/07_presentations/README.md | Read | Presentations are derived briefings, not new evidence. |
| Existing presentation decks, .build directories, PNGs, JSON and inspect.ndjson files | Metadata: filenames/extensions identified outside assigned roots | Presentation generation/inspection artifacts, not participant datasets. Not substantively inspected or altered here. |
| Round 03–06 README placeholders | Metadata: filenames/current planned status identified | Separate specialist scope; no completed runs inferred from these paths. |

There is **no enormous generated dataset under the assigned three roots**: the entire set is approximately 704 KB. The largest raw file is the 88,393-byte V08 caption. All existing assigned text was manageable. Large presentation inspect data elsewhere was not substituted for research evidence. The five additional `.info.json` files named in the discovery log were already removed before this audit; their earlier combined 5,271,806-byte size and cleanup timestamps are **reported historical metadata**, not files inspected now. Do not list them as present or as unreadable research data. No original private runtime JSON or session log is mirrored under `05_evidence`.

## 2. Chronology and evidence classes: preserve the distinctions

All runs carry the date 2026-10-18; date alone cannot order them. Current navigation explicitly records the historical comparison before the completed Round 01 pass and expanded Round 02 after the owner's scope expansion. Exact historical run start/end instants are not reconstructed.

| Layer | What it actually contains | Permitted conclusion |
|---|---|---|
| Round 00 orientation | Source registers, selected public accounts/studies, internal process review and design recommendations | Bounded prior context, not fresh Round 01/02 observations. |
| R2/H historical fictional run | Agent-written Jordan/Mira cases, proposed flows, predeclared rubric, paper trace and independent Codex critique | A specific written inference can be inconsistent; nothing about real user frequency, preference or hiring benefit. |
| R1/W public run | Twelve opened-source records, public accounts, studies, surveys, query/observation ledgers | Mechanisms and counterexamples in bounded contexts; no ranked greatest problem. |
| R2/X expanded run | Twelve Practices, twelve Domain, two Coordinator records; ten captions; one-owner internal process review | Broader reported pains/practices/guidance, experimental context and process strengths/gaps, with distinct evidence weights. |
| Round syntheses/gates | Coordinator reconciliation and proposed next activity | Research disposition and proposal, not acceptance, implementation or validation. |

Use **observed repository fact** for inspected file contents/counts, **source-reported claim** for external experience/study findings, **interpretation** for synthesis, **hypothesis/proposal** for a candidate aid, and **unknown** for the unresolved effect. The earlier internal reviewer observed private files; this auditor observed that review's report. Those are different verification levels.

Hypothesis IDs are not stable across rounds. Round 00 friction H1 concerns feedback/repeated preparation, H2 assessment effort, H3 feasible conditions. Round 01 H1 concerns preparation/checking, H2 practical conditions, H3 interruption/return. A slide labelled only “H3 confirmed” would therefore be both ambiguous and misleading.

## 3. Round 01: exact source routes and what changed

Canonical records: [sources](../../03_research-rounds/01_public-web-user-insights/runs/2026-10-18-web-based-user-insights/sources.md), [observations](../../03_research-rounds/01_public-web-user-insights/runs/2026-10-18-web-based-user-insights/observations.md), [query log](../../03_research-rounds/01_public-web-user-insights/runs/2026-10-18-web-based-user-insights/query-log.md). Access recorded by the run is 2026-10-18 throughout. Original sources were not all independently reopened in this audit; section 5 identifies actual spot checks and failures. Relative or index-derived forum dates remain uncertain.

| Qualified source / observation | Original source and dates | Context / support / limit |
|---|---|---|
| R1/W S01 / O01 | [Reuschel, McDonnall & Burton, online application accessibility](https://www.blind.msstate.edu/sites/www.blind.msstate.edu/files/2023-12/Reuschel%20et%20al%20%282023%29%20Accessibility%20and%20Usability%20of%20Online%20Job%20Applications.pdf), 2023 | Three expert blind testers, 30 selected US company sites, 90 desktop trials. Ledger reports 50 independent completions and at least one blocker on 23 sites. Sampled task evidence, not 90 people, Singapore evidence or a device-switching study. Original failed to reopen here. |
| R1/W S02 / O02 | [Desktop versus phone discussion, thread 1r0dch3](https://www.reddit.com/r/jobsearchhacks/comments/1r0dch3/why_does_applying_for_jobs_feel_easier_on_desktop/), approximately April 2026 from relative display | Phone convenience versus document/multitab effort; another reply prefers desktop browsing too. Unknown geography/occupation and promotional contamination. No lost-opportunity sequence. |
| R1/W S03 / O03 | [MOM Job Vacancies 2025](https://stats.mom.gov.sg/iMAS_PdfLibrary/mrsd_JV2025.pdf), March 2026; reference 2025-09-30 | 16,910 establishments, 85.9% response, larger private establishments/public sector. Employer perceptions of non-PMET recruitment difficulty; schedules/pay/physical work/prospects. Same report as Round 00 D01 and R2/X D08. No applicant testimony or posting-omission rate. |
| R1/W S04 / O04 | [Randstad Workmonitor Singapore](https://www.randstad.com.sg/hr-trends/employer-brand/flexible-work-a-must-have-for-singapore-randstad-workmonitor/), 2024-04-22; field date not disclosed | Reported 759 employees and seekers; 42% stated they would decline an inflexible role. Mixed population, unknown recruitment/subgroup base; intention, not observed rejection. Keep this figure out of a general seeker-prevalence slide. |
| R1/W S05 / O05 | [Commute offer discussion, thread 1ffqahp](https://www.reddit.com/r/askSingapore/comments/1ffqahp/will_you_turn_down_job_offer_due_to_long_commute/), index date 2024-09-13 | One Singapore graduate account learns location after interview and weighs commute against pay/benefits/possible arrangements. Original ad and final decision unknown. Useful late-discovery example, not proof of deliberate omission. |
| R1/W S06 / O06 | [Night-shift offer discussion, thread 1s7o905](https://www.reddit.com/r/singaporejobs/comments/1s7o905/need_advice_can_take_job_with_night_shifts_or_nah/), index date 2026-03-30 | Known alternating 12-hour shifts at verbal offer; pay, interest and stability trade-off. Demonstrates deliberation with information available, not necessarily missing information. |
| R1/W S07 / O07 | [Dumont, De Marco & Helsper manuscript](https://eprints.lse.ac.uk/120166/1/Online_job_search_discouragement_How_employment_platforms_and_digital_exclusion_shape_the_experience_of_low_qualified_job_seekers_2023.pdf), [publisher DOI](https://onlinelibrary.wiley.com/doi/10.1111/ntwe.12279); online September 2023 / issue 2024; 2020–22 fieldwork | Twenty lower-qualified unemployed interviewees in Spain; repeated profiles, uncertain fields/status and one immediate phone application. Mechanism and counterexample, not current Singapore frequency. Original failed to reopen here; this audit retains the source ledger's scope. |
| R1/W S08 / O08 | [Cross-sector search, thread 1k6mrf5](https://www.reddit.com/r/askSingapore/comments/1k6mrf5/is_it_me_or_is_the_job_market_really_that_bad/), 2025-04-24 | General résumé across service/admin/call-centre/finance/retail, with AI cover-letter and shift-constraint discussion. Post/replies are distinct people; no verified AI effect. Counters universal per-role rewriting. |
| R1/W S09 / O09 | [Fifteen-month search, thread 1x4rc80](https://www.reddit.com/r/singaporejobs/comments/1x4rc80/got_two_offers_this_week_after_jobsearching_for/), 2026-10-13 | Tech product-management account: per-role folders, descriptions, interview notes and checked AI edits. Another reply questions universal tailoring. Reported offers do not establish that the method caused them. |
| R1/W S10 / O10 | [AI context repetition, thread 1v6dhlr](https://www.reddit.com/r/jobsearchhacks/comments/1v6dhlr/i_noticed_using_ai_to_help_with_the_job_search_is/), 2026-07-25 | Re-entering résumé/role/stage context and maintaining a separate tracker; a reply describes correcting an experience calculation. Geography unknown, promotion risk, no measured burden. |
| R1/W S11 / O11 | [Application tracking discussion, thread 1qlh81g](https://www.reddit.com/r/jobsearchhacks/comments/1qlh81g/how_do_you_keep_track_of_job_applications_without/), 2026-01-24 | Email folders, PDFs, small spreadsheets and no-tracking alternatives coexist with follow-up burden. Selected reports, not a demand estimate for a dedicated tracker. |
| R1/W S12 / O12 | [TestGorilla Skills-Based Hiring 2025](https://assets.ctfassets.net/vztl6s0hp3ro/6ea5daAQcxr7926XPdSrY9/2653b8509ba5d4a92f7292c97641176f/skills-based-hiring_the-state-of-skills-based-hiring-2025.pdf), 2025; April 2025 panel | Vendor-published UK/US survey, 1,076 current/recent seekers plus separate hiring panel. AI use and non-use; no Singapore adoption estimate or causal efficacy. |

The [run findings](../../03_research-rounds/01_public-web-user-insights/runs/2026-10-18-web-based-user-insights/findings.md) support unranked questions, not a validated shortlist winner. H1 has some repeated-entry/checking evidence; H2 has conditions/choice evidence; H3 has general context/access evidence. Their strength does not establish comparative burden.

The precise **Singapore phone discovery → intended laptop return → failed transition → lost opportunity** chain was not retrieved. Q4/Q8/Q9 searches and the additional narrow stop-check retained no complete account. Do not splice the screen-reader study, a desktop preference and a tracking complaint into a composite participant story. Retrieval failure is not disproof.

Round 01's planned elapsed blocks and judgment that another 30 minutes could not change the shortlist were not logged sufficiently to certify its full stopping rule. The current gate explicitly closes a bounded pass despite these limits. Its next question about checking/correcting/rejecting AI output is a sequencing proposal, not product selection.

Screened sources remain screened: [MOM EP advertising guidance](https://www.mom.gov.sg/passes-and-permits/employment-pass/consider-all-candidates-fairly), [Tilburg letter-evaluation research record](https://research.tilburguniversity.edu/en/publications/labor-market-signals-the-role-of-large-language-models/), and forum IDs `1wt7qfp`, `1p08d61`, `1d1lsi6`, `1dst3nr` were opened but not retained as additional observations. Their original URL routes are in R1/W/sources.md. Guidance and letter evaluation do not become everyday workflow testimony; repeated forum material does not add independent samples.

## 4. Latest expanded Round 02: source inventory and concrete accounts

Canonical ledgers: [Practices](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/practices-research.md), [Domain](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/domain-research.md), [Coordinator](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/coordinator-research.md). All record access on 2026-10-18. The 26 entries are records, not 26 independent studies or newly discovered populations.

### 4.1 Practices P01–P12

| Qualified ID | Original source / publication and underlying date | Concrete support and boundary |
|---|---|---|
| R2/X P01 | [TODAY/CNA Jobseekers' Diaries](https://www.channelnewsasia.com/today/voices/jobseekers-diaries-i-couldnt-get-job-4-months-then-i-worked-my-resume-and-interview-skills-4645931), 2021-10-31, updated 2025-11-07; June 2020–February 2021 experience | Retail-to-healthcare-operations account reports over 80 résumés/four months and four interviews without an offer, then training/WSG support and later LinkedIn contact preceding a job. One selected retrospective, pandemic context; updated page is not new fieldwork and success cannot be attributed to one intervention. |
| R2/X P02 | [Interview rounds, thread 1ulduhg](https://www.reddit.com/r/singaporejobs/comments/1ulduhg/going_through_insane_numbers_of_rounds_just_to/), absolute date unresolved, conflicting one-/three-month displays | Employed, self-described non-tech applicant takes leave for rounds and faces uncertain further stages. Other replies separately discuss correcting extracted résumé fields, a compressed successful five-round week, and a longer unsuccessful sequence. Do not combine these into one person or a typical number of rounds. |
| R2/X P03 | [Han & Malka, SVA Voices on Work](https://www.socialventures.org.au/wp-content/uploads/2026/01/Voices-on-Work_-AI-in-Job-Application-.pdf), January 2026; August–November 2025 | Western Sydney primary cohort: 13 disadvantaged non-university young people, interviews/focus groups; reference: 50 Sydney university students, interviews/survey; ages 18–30. Non-use/caution/template-only use versus review/rewording. Network recruitment; not 63 disadvantaged interviewees or a representative adoption survey. |
| R2/X P04 | [Connecting Scotland findings](https://www.gov.scot/publications/evaluation-connecting-scotland-phase-3-digital-support-employability/pages/5/), [methods](https://www.gov.scot/publications/evaluation-connecting-scotland-phase-3-digital-support-employability/pages/4/), 2023-07-06; surveys closed 2022-06-30 and 2023-03-07 | Eighteen telephone interviews; 591 welcome/447 impact responses from 9,143 users, voluntary non-panel samples. Shared devices, awkward phone attachments and library time constraints; also a successful remote interview route. Programme testimony, not causal support or a phone-to-laptop loss sequence. |
| R2/X P05 | [AI CV discussion, thread 1umzwwa](https://www.reddit.com/r/singaporejobs/comments/1umzwwa/have_u_use_ai_to_enhance_ur_cv/), absolute date unknown, conflicting three-/four-month displays | One reply describes returning weeks later to an unfinished AI-assisted résumé and struggling to understand it; callbacks/non-callbacks and rewriting are separately reported. Concrete draft-recovery account, not lost posting, diagnosed hallucination or measured AI benefit. |
| R2/X P06 | [Claude résumé discussion, thread 1vhlme4](https://www.reddit.com/r/singaporejobs/comments/1vhlme4/i_tested_claudes_new_ai_resume_design_feature/), absolute date unknown, two-month display | Author reports a visually improved PDF, then Claude's warning about non-selectable text, and asks whether résumé/design/browser explains it. No file or parser inspected. Evidence of checking behavior, not a reproduced ATS failure or general provider defect. |
| R2/X P07 | [NUS Create an Impressive Resume](https://www.nus.edu.sg/cfg/students/career-resources/create-an-impressive-resume), publication date not displayed | Advice on relevant real experience, action/results, AI accuracy/intent review, personal-data caution and human feedback. Student/graduate guidance, not observed adherence or current provider-policy review. |
| R2/X P08 | [NUS Ace Your Job Interview](https://www.nus.edu.sg/cfg/students/career-resources/ace-your-job-interview), publication date not displayed | Confirm format/technology, research employer/role, use real examples, verify AI research, practice with peers/advisers; mentions an AI tool. Advice, not proof of effectiveness or universal AI need. |
| R2/X P09 | [Interview practice, thread 1whlodl](https://www.reddit.com/r/singaporejobs/comments/1whlodl/for_the_last_job_interview_you_really_truly_cared/), absolute date unknown, one-month display | Different replies describe company/technical research, AI plus family help, and five/six reusable stories practiced aloud. No mention of AI is not proof of non-use. Service-research/promotion risk and outcomes unverified. |
| R2/X P10 | [Tailoring fatigue, thread 1wy5757](https://www.reddit.com/r/jobs/comments/1wy5757/im_sick_and_tired_of_tailoring_my_resume_to_every/), absolute date unknown, last-week/two-day discrepancy | OP reports interview requests associated with intensive tailoring; replies report two/three versions, master-résumé selection, or more interviews with a stable résumé. Different people/roles/periods; neither method wins causally. Geography unspecified. |
| R2/X P11 | [Mangadi & Petersen, JobX study](https://scielo.org.za/scielo.php?pid=S1560-683X2024000100046&script=sci_arttext), SAJIM 2024, DOI 10.4102/sajim.v26i1.1850; reviews collected 2023-04-15 | All 368 available Google Play reviews, thematic UTAUT analysis with Atlas.ti AI coding/refinement. Positive CV/mobile/data-free experience alongside crashes/failed saves. Review text is not verified usage, hiring outcomes or complete offline functionality. South African context. |
| R2/X P12 | [Singapore Women's Weekly returner account](https://www.womensweekly.com.sg/your-life/mid-career-mum-back-to-work-struggle-find-job-fit), 2026-02-28; retrospective return-to-work search | Marketing returner reports tasks/presentations/final interviews without a permanent offer and family-compatible work constraints. WSG-sponsored editorial plus separate coach advice. Same article as Round 00 friction P04; not new independent corroboration. |

These accounts give concrete mechanisms: scheduling work around existing employment, correcting extracted fields, reading one's own unfinished draft again, checking an export, reusing experience stories, and choosing when to tailor. They do **not** quantify how common or costly these mechanisms are. Do not write interview-style dialogue for any of these public authors.

Practices screening IDs D01–D06 are **not** Domain D01–D12. Screened material includes [Ask a Manager honesty advice](https://www.askamanager.org/2020/07/should-i-lie-on-my-resume-to-make-myself-stand-out.html) (open failed), forum `1vs8j49` (questionable self-reply provenance), and `1wt1tap` (summary of the original P09 discussion). P08's initial timeout was recovered; it is not an unreadable retained source. E11's `site.content...` expression was malformed. E13 did not retrieve the exact H3 sequence. Neither a failed query nor a summary post adds a participant or source family.

### 4.2 Domain D01–D12

| Qualified ID | Original source / date | Claim scope and quantitative or interpretation boundary |
|---|---|---|
| R2/X D01 | [ScamShield legitimacy FAQ](https://ask.gov.sg/scamshield/questions/cmdcv46bt017g36wpmgi0mc2t), exact date unavailable; relative one-year update | Official checks of company/contact identity and suspicious requests. Advice, not detector accuracy or proof that registration authenticates a recruiter. |
| R2/X D02 | [TAFEP Recruitment Practices standard](https://www.tal.sg/tafep/getting-started/progressive/tripartite-standards), date not displayed | Relevant objective selection/interview criteria. Employer practice standard, not adjudication, current legal certification or observed compliance. |
| R2/X D03 | [WSG low skills-match FAQ](https://ask.gov.sg/wsg/questions/clp9j4c1p0031azywcqpjen8w), exact date unknown; three-year update display | Applicants may still apply with a low score. Permission is not a selection probability, credential exemption or validated JobHub fit model. |
| R2/X D04 | [MOM Occupational Wages 2025](https://stats.mom.gov.sg/Pages/Occupational-Wages-Tables2025.aspx?PageVersion=512), release recorded 2026-06-30; reference June 2025; [methodology](https://stats.mom.gov.sg/iMAS_Tables1/Wages/Wages_2025/Coverage-and-Methodology-of-OWS-2025.pdf) | 5,230 larger private establishments, about 391,300 full-time resident employees, 98% response; survey plus administrative data. Gross/basic wage definitions differ; bonuses/employer CPF/equity/noncash benefits are not all included. No occupation-specific cells or personalised estimate extracted. |
| R2/X D05 | [MOM key employment terms](https://www.mom.gov.sg/employment-practices/contract-of-service/key-employment-terms), date not displayed | Source's conditional applicability and listed duties/hours/pay/leave/notice fields supply a clarification checklist. Not a contract ruling or proof that every component is negotiable. |
| R2/X D06 | [NUS Evaluate Job Offers](https://nus.edu.sg/cfg/students/career-resources/evaluate-job-offers), [negotiation PDF](https://nus.edu.sg/cfg/docs/default-source/students/career-resources/evaluate-job-offers/dos-and-donts-of-salary-negotiation.pdf), dates not displayed | Research comparable roles, priorities and a supported counterproposal; PDF acknowledges possible withdrawal. Advice for students/graduates; categorical moral/timing statements are not adopted as universal/legal rules. |
| R2/X D07 | [Cullen, Pakzad-Hurson & Perez-Truglia, Pushing the Envelope](https://www.unibocconi.it/sites/default/files/Negotiations_WP.pdf?VersionId=_4ah18kiNSVAZlbDGBrP6PIxYrUnuYLh), June 2025 working-paper version, NBER 33903 | Collector reports two experiments with over 3,100 US technology job seekers recruited through levels.fyi; encouragement increased negotiation attempts/compensation, discounted coaching did not significantly increase attempts. Selected population, follow-up reporting, not peer-reviewed in inspected version. Current audit open failed; earlier independent review also timed out. No numerical local uplift or safety probability adopted. |
| R2/X D08 | [MOM Job Vacancies 2025](https://stats.mom.gov.sg/iMAS_PdfLibrary/mrsd_JV2025.pdf), March 2026, 2025-09-30 reference | Same report as R1 S03 / Round 00 D01. Employer-reported specialised-skill constraints and particular non-PMET conditions. Academic qualifications not main determinant for a reported 79.6% of vacancies does not mean verified credentials never matter. Employer denominator, not seeker experience. |
| R2/X D09 | [OECD Labour shortages and labour market inequalities](https://www.oecd.org/en/publications/labour-shortages-and-labour-market-inequalities_14e62ec0-en.html), 2025-03-21 | Official abstract links shortages/job quality/shift/health contexts internationally. Collector could not retrieve full PDF; methods/causality/country estimates not independently inspected. Cannot diagnose an individual Singapore employer's motive. |
| R2/X D10 | [Work content/pay trade-off, thread 1sggfoo](https://www.reddit.com/r/singaporejobs/comments/1sggfoo/2_job_offers_after_career_misstep/), date unknown, five-/six-month discrepancy | Engineer-titled role reportedly administrative; anticipated lower-paying alternatives considered for relevant exposure. Final offers/acceptance unknown; no proof of deliberate bait-and-switch or typical salary. |
| R2/X D11 | [Negotiation thread 1uvtw7m](https://www.reddit.com/r/singaporejobs/comments/1uvtw7m/please_share_with_me_tips_for_salary_nego_should/), selected comment two-month display, absolute date unknown | Specific comment at collector lines 430–455: base unchanged, RSUs increased, vesting-limited package. Perceived leverage includes budget knowledge/urgency; anonymous outcome unverified. Other replies disagree on always negotiating. Do not convert this into an average gain or base-pay result. |
| R2/X D12 | [SkillsFuture Skills Demand 2023/24](https://www.skillsfuture.gov.sg/docs/default-source/skills-report-2023/ssg_2023_10nov2023_sdfe_final-(3).pdf), copyright 2023; 2019–22 postings | pp.94–95 practitioner career-change guidance; pp.100–101 define posting-based skill breadth. Coach-mediated transition example, not direct participant testimony. Breadth of mentions does not establish personal proficiency or predict 2026 demand. |

D01/D02/D03/D05/D06/D12 contain guidance or standards; D04/D08 contain defined official measurement; D07 is experimental research; D09 is abstract-only research; D10/D11 are unverified accounts. Treating all twelve as observed user behavior would erase the main evidential distinction.

### 4.3 C01 and C02: include the experiments, preserve the bases

Both original abstracts were **directly reopened and inspected in this audit on 2026-10-18**. The current employer-post PDF title/date were checked too. These results must not disappear behind blanket wording that the corpus has no measured outcomes; this run performed no original participant/product experiments, but it includes studies that did.

| Qualified ID / original | Verified reported result | Unit, comparator and limit |
|---|---|---|
| R2/X C01: van Inwegen, Munyikwa & Horton, [Algorithmic Writing Assistance on Jobseekers' Resumes Increases Hires](https://arxiv.org/abs/2301.08083), submitted 2023-01-19, arXiv 2301.08083v1 | Abstract reports **8% relative increase in hiring probability** for treated job seekers, in an online-market field experiment involving nearly half a million seekers; no evidence of lower employer satisfaction. | Treatment is algorithmic résumé writing assistance versus control. Eight percent is **not eight percentage points**; the inspected abstract does not provide the baseline needed for an absolute probability conversion. Not a test of invented qualifications, every present-day chatbot, Singapore job seeking or JobHub. Audit check is abstract-level, not a full-paper/microdata replication. |
| R2/X C02: Wiles & Horton, [More, but Worse: The Marketplace Effects of AI-Generated Job Posts](https://www.emmawiles.com/storage/jobot.pdf), **2026-09-04** version | Abstract reports employers **19% more likely to post**, **44% less time writing posts**, and **no discernible increase in matches**. It also reports more generic/less informative text. | Randomised offer of AI-generated employer first drafts in an online labor market, compared with control. Nineteen percent is a relative posting-probability increase, not 19 percentage points; introduction reports the corresponding six-point difference. Time comparison is drafting time among employers posting, not total recruitment time or job-seeker time. No discernible matching gain is not proof of exact equality or a universal harmful AI effect. Audit checked title/abstract and pertinent introduction passages, not all 72 pages/appendices. |

C02's application-time/welfare accounting uses setting-specific assumptions; its roughly six-to-one cost comparison is **model-based accounting**, not a measured JobHub time loss and not necessary for a public story. Its older search title, *Generative AI and Labor Market Matching Efficiency*, must not replace the inspected September 2026 title/version.

These experiments concern different sides of a market, different interventions and different outcomes. They support the question of whether assistance improves useful information, not a winner between tools. Shared Horton authorship means distinct experiments are **not independent research-team replications**. V07's half-million/8% narration closely overlaps C01's result; do not count it as another experiment. V07's separate applicant-pitch/screening claim is not C02's employer-post experiment.

## 5. Direct external spot checks and verification limits

Read-only checks used the original public URLs already in the evidence. This was verification of the recorded source chain, not another discovery sweep. No full-page archive was written.

| Original / IDs | Actual audit inspection | Disposition |
|---|---|---|
| arxiv.org/abs/2301.08083 — R2/X C01 | Title, authors, submission date, complete abstract | Directly supports the bounded 8% result above. |
| emmawiles.com/storage/jobot.pdf — R2/X C02 | September 4 title page/abstract; relevant introduction on posting, writing time and matching | Directly supports 19% / 44% / no discernible matching increase, with conditional/accounting limits. |
| SVA Voices on Work PDF — R2/X P03 | Research approach p.7, findings p.8 and executive-summary field dates p.4 | Confirms 13 versus 50 cohorts and August–November 2025 fieldwork. Background statistics quoted from other reports are not this cohort's results. |
| Connecting Scotland methods/findings — R2/X P04 | Methods and respondent table; relevant access findings | Confirms non-panel voluntary design, 18 interviews, 591/447 responses and low response rates. Findings describe barriers as source reports; do not universalise the report's stronger wording about phones. |
| SciELO JobX article — R2/X P11 | Data sampling, analysis and results context | Confirms all 368 reviews collected 15 April 2023 and AI-assisted thematic coding. No raw reviews were independently re-coded here. |
| MOM 2025 wage methodology — R2/X D04 | Population/reference period, exclusions and basic/gross definitions | Confirms 5,230 establishments / about 391,300 employees / 98% response; before employee CPF and tax deductions. Not take-home pay or a full compensation valuation. |
| Bocconi negotiation PDF — R2/X D07 | Attempted open returned Internal Error | **Unreadable external attempt.** Preserve original collector's June 2025 bounded report; not independently reproduced here. No invented effect size. |
| Mississippi author-hosted PDF — R1/W S01 | Attempted open returned Internal Error | **Unreadable external attempt.** Local source ledger remains readable; do not claim a current reproduction of 50/90 or 23/30. |
| LSE manuscript PDF — R1/W S07 | Attempted open returned Internal Error | **Unreadable external attempt.** Earlier run itself discloses a later fetch failure; keep original collector/publisher provenance, not a fresh full-text check. |

Other public originals, including the forum accounts, were inspected through their complete repository source records in this audit, **not all reopened live**. This audit therefore establishes the completeness, distinctions and traceability of the research record, with selected original-source checks; it does not independently authenticate every public account or reproduce every cited study.

## 6. Caption evidence: every source, integrity and concrete examples

Canonical [video report](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/video-research.md) and [discovery/capture log](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/youtube-discovery-log.md) supply creator/upload/track provenance. Captures were made 2026-10-18. This audit independently parsed all files and matched every hash. There are seven automatic tracks and three tracks listed as manual; the latter classification does not verify human authorship or transcription accuracy.

### 6.1 Caption inventory and integrity

The filenames below resolve in the exact E directories in section 1.1. Suffix `en-orig` is automatic original English; additional `en`/`en-US` tracks are listed manual in the logged metadata. Bytes and cue ranges are current local observations.

| R2/X video ID / file stem | Bytes / cues | First start → last end | SHA-256 |
|---|---|---|---|
| V01 iVeoEF3bzlY.en-orig | 58,119 / 796 | 00:00:03.200 → 00:27:00.119 | 2641213F00349ED225C4A470901F68088CC22DDBD311894F63CD261E2C375F82 |
| V02 0KXDCuxi3jk.en-orig | 17,692 / 244 | 00:00:00.160 → 00:08:34.000 | 9668B4211DE80834A500857AD4BC3F9D8DC1A0996F0266B66D8A5911A6B64F52 |
| V03 x2sgf8zlNao.en-orig | 22,913 / 315 | 00:00:00.000 → 00:10:19.929 | 428C9912F6207A6943431B75B047CBDE3251DCB9CC96ABC1790F2CE66DD8F0FF |
| V04 fCd4wZQaWqo.en-orig | 21,611 / 298 | 00:00:00.000 → 00:09:20.240 | 45DCF7EDAD859852A4884C9C1967E2B607E56C38494D97973BE6DE65BCB08A82 |
| V05 IF3McdG_dSY.en-orig | 24,528 / 346 | 00:00:00.000 → 00:13:24.320 | 10668C13DD48F1615EA7FE0EBF99CB32E2EA860CE9A111469F738C0B6BDFC02C |
| V06 pmnY5V16GSE.en | 22,773 / 314 | 00:00:00.000 → 00:10:19.040 | 02A11763248B793979E3E04755776DF7193BD848015C5B97D1DB07BB3F943785 |
| V07 N1Fm4JYae1I.en-orig | 25,963 / 359 | 00:00:00.000 → 00:13:09.560 | 6DF55C94DFFCA768C90CA4DCEC34A2B9697E7BA0A9311873F0D820DE7B8B932B |
| V08 ay_wtOte5Gc.en-US | 88,393 / 653 | 00:00:00.000 → 00:57:38.520 | 0151C8148B8B22B34829497EA1228455D88A2736B369793541D64F255E122F2F |
| V09 HHGQ_QeHjF0.en-orig | 5,274 / 73 | 00:00:00.080 → 00:02:41.480 | 212C3B2FFFF801A87A863A07073710146A4B90B92D46891948D122579AE1CBE3 |
| V10 Risf_QQGX2o.en | 17,956 / 189 | 00:00:00.170 → 00:10:32.970 | 0382B1BC6B0806F0B22B761C6637C375CCA3AB4AC82FAC8010FEB7213436D299 |

Total 1,999 supplied + 1,588 additional = **3,587 cues**. Cue counts describe text structure, not people, independent claims or evidence quality. Caption end time need not equal metadata video duration.

### 6.2 Source-by-source appraisal

| Qualified ID / original URL / creator / upload date | Caption examples checked | Counterevidence, scope and usable story treatment |
|---|---|---|
| R2/X V01 [iVeoEF3bzlY](https://www.youtube.com/watch?v=iVeoEF3bzlY), CNA Work It, 2025-06-09 | 05:55–08:35: practitioner translates pace/pay/self-starter language negatively, while host argues pace can disclose real demands. 08:35–09:40 distinguishes partial match from essential skills. 16:00–18:20 host recounts a friend's eventual start after a transparent lower-role offer/delay. 22:00–26:15 listener's leave problem and hosts' scheduling suggestions. | Singapore practitioner/host advice, listener report and secondhand account, not representative research. Preserve disagreement, including the hosts' unsupported minimisation of total leave burden. Fake-job percentages and portal repost/response claims remain unverified. A delayed hire is not automatically fake; no contractual safety conclusion. |
| R2/X V02 [0KXDCuxi3jk](https://www.youtube.com/watch?v=0KXDCuxi3jk), A Life After Layoff, 2025-06-09 | 03:20–04:28 speaker reports a weekend startup hiring-strategy assignment, rejection and later reuse of ideas; distinguishes brief samples from extensive unpaid consulting. 05:20–06:09 explicitly allows informed contracting. | International recruiter perspective and uncorroborated personal account. No prevalence of idea theft or universal response deadline. Sales/coaching promotion; same creator family as V04. Ask about assessment scope/terms rather than assert misconduct. |
| R2/X V03 [x2sgf8zlNao](https://www.youtube.com/watch?v=x2sgf8zlNao), Recruiter Preston, 2023-04-28 | 01:22–01:53 allows strict qualifications for regulated/difficult work; caption has a suspect negation. 02:46–03:02 interprets no-experience hiring as churn. 04:30–06:27 recommends review comparison with unsupported star-rating/motive rules. | Technology recruiter, US references. Training/entry-level work, legitimate agency anonymity and limited website resources are alternatives to negative interpretations. Do not quote the suspect negation, infer review honesty from stars or promote historical legal claims. |
| R2/X V04 [fCd4wZQaWqo](https://www.youtube.com/watch?v=fCd4wZQaWqo), A Life After Layoff, 2021-12-28 | 02:30–03:37 repeated/multicity advertising, with hard-to-fill role/location exceptions. 04:20–05:34 manager-title/director-responsibility personal comparison. 06:42–07:28 contract/temp-to-perm concern, with explicit informed-contracting exception. | Older international recruiter advice. Title/level is speaker judgment; high pay, repeated ads and contracts have multiple explanations. Job-board prices/protections are not current verified facts. V02/V04 are one creator family. |
| R2/X V05 [IF3McdG_dSY](https://www.youtube.com/watch?v=IF3McdG_dSY), Dani Careers, 2026-10-11 | 00:40–02:10 training-investment explanation; 02:13–03:55 absorbed workload; 03:56–05:58 ghost/internal-posting narrative; 10:50–12:30 questions about staffing/pay and a manager who acknowledges/corrects low pay. | Commentary with illustrative situations, not an identified employer investigation or participant diary. A pause after a budget question is not a ghost-job test. Genuine skill/supply/shift/finance constraints remain alternatives. Quits do not measure loyalty. |
| R2/X V06 [pmnY5V16GSE](https://www.youtube.com/watch?v=pmnY5V16GSE), Jeff Su, 2023-04-25 | **03:50–04:18:** narrator requests original/updated comparison and identifies a changed title from Senior Management Consultant to product manager. Brief caption quote at 04:16.918: **“can't change my title”**. 06:40–09:45 builds role-specific interview answers and a document answer bank. | Narrated demonstration, not an inspected screen, personal application outcome or model error rate. Strong concrete example of checking a consequential edit. Same AI's diff is not independent verification. Suggestions for metrics do not supply true achievements. Multi-prompt superiority unverified. |
| R2/X V07 [N1Fm4JYae1I](https://www.youtube.com/watch?v=N1Fm4JYae1I), Jeff Su, 2026-09-15 | 07:00–08:30 separates facts/result/contribution/method before wording. **09:52–10:06:** provide verifiable numbers before rewriting; brief caption quote: **“Do not add or change any facts or numbers.”** 10:50–12:20 separates projects from workplace experience. | Useful fact-first advice, same creator as V06; worked ticket/view metrics are illustrations, not candidate achievements. C01-like experimental number should route to C01. Other surveys/effects, universal file limits and screening claims remain excluded. |
| R2/X V08 [ay_wtOte5Gc](https://www.youtube.com/watch?v=ay_wtOte5Gc), Cedarville University / Jeff Reep, 2026-04-13 | 03:00–08:00 experience toolbox and recorded mocks; 13:00–16:20 real stories/STAR; **18:45–21:10 notebook/folder of past questions and experiences**; 26:20–27:50 secondhand accounting-versus-finance emphasis mismatch; 37:15–38:30 follow-up timeline; 45:45–48:20 camera notes and flexible practice. | Manual alternative, US university/faith audience, secondhand student stories. Entire caption was read, including 29:50 onward appearance/eye-contact norms and 53:00 onward identity/religious examples. Do not import these as universal evaluation criteria. Legal and survey claims unverified; story selection/rehearsal advice is not demonstrated efficacy. |
| R2/X V09 [HHGQ_QeHjF0](https://www.youtube.com/watch?v=HHGQ_QeHjF0), Express Tech, 2025-04-24 | Full 00:00–02:41 text describes a remote social-media/content job prompt, generated descriptions/pay/links, Nigerian examples and a claimed frequent use. | Title suggests a dream-job journey, but captions demonstrate no employer-page verification, application, interview, offer or employment. Use only as weak narrated workflow/checking-omission example. No visual or current-link verification. |
| R2/X V10 [Risf_QQGX2o](https://www.youtube.com/watch?v=Risf_QQGX2o), Practical Wisdom – Interesting Ideas, 2020-08-17 | 01:45–04:25 contribution record/comparable roles; 04:25–04:50 unsupported uplift rule; 06:10–06:55 budget limits and alternatives; later meeting/rejection advice. | Old international current-job raise advice, no named expert established. Do not use its PayScale statistic, 15% uplift, colleague-disclosure tactic, or entitlement language as a rule. Domain official/research sources carry pay analysis. |

Only the two short creator-caption quotations above are offered as quotation candidates. They are accurately present in local caption text, **not audio-verified quotations or participant testimony**. Do not silently repair automatic captions and present the result as a verified spoken quote. Paraphrase other material and retain its evidence label.

### 6.3 Quarantined numbers and discovery limitations

- V01/V05 repeat ResumeBuilder fake-job claims; they are not independent CNA/Dani surveys or Singapore rates. Greenhouse classifications have a different platform/denominator. The conditional interview statistic in V05 is not a share of all employers or interviews.
- V07's readability, tailoring, AI-approval, metrics and AI-skills percentages are not accepted from the video. Its quoted application-rate comparison is observational as narrated, not automatically an experiment. The separate applicant-pitch screening effect does not become C02. C01's original abstract, not this video, supports the bounded 8% result.
- V08's preparation number is garbled; its handshake/dress surveys lack verified methods. V10's PayScale figure concerns a selected high-earner group, not all negotiators; its uplift rule is advice, not an estimate.
- Thirteen QV strings were logged; six additional checked URLs yielded five canonical captures. The sixth check was the erroneous lower-case `ay_wtote5gc`; corrected `ay_wtOte5Gc` is case-sensitive. Do not call this six successfully reviewed new videos or a sixth independent source.
- CNA salary podcast page, UNI interviewing page, empty Khan extraction and SDSU HTTP 429 remain discovery leads/access gaps, not additional caption-reviewed sources. No Singapore salary video was captured in the additions.
- The discovery log's statement that the supplied README overclaims five browser-export attempts is now stale: the current README correctly specifies the first four; the fifth was checked via yt-dlp only. Preserve the historical correction without alleging a current inconsistency that has been fixed.

## 7. Internal process: reported originals, bounded observations, no private re-scan

Primary local record: [expanded internal review](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/internal-process-review.md); earlier record: [evidence process review](../../05_evidence/internal-job-hunt-workspace/2026-10-18-process-review.md). These are one owner's purposive process-document sample, not a cohort of users. Earlier I01–I07 are not equivalent IDs to expanded I01–I16.

The expanded reviewer reports 25 process documents plus five historical artifacts, accessed 2026-10-18. Most authoring metadata is July 2026; a discovery binding has September changes. The current auditor did not access the private drive, private profile, résumé, contact records, contract, correspondence, application outcomes, session bodies or runtime originals.

### 7.1 Exhaustive safe original-source accounting

The following **Metadata** classification means the original's identity/inspection boundary is known through the repository review, not that its original contents were read in this audit. Safe aliases are sufficient; private absolute paths and target identities are unnecessary for a presentation.

| Expanded internal source ID | Safe purpose / original type | Current audit class |
|---|---|---|
| Internal S01 | Workspace index and coordination/source order | Metadata via report |
| Internal S02 | Context map, storage ownership and allocations | Metadata via report |
| Internal S03 | Workspace manifest, resource/retention/verification declarations | Metadata via report |
| Internal S04 | Discovery workflow manifest | Metadata via report |
| Internal S05 | Intake/filter workflow manifest | Metadata via report |
| Internal S06 | Capture workflow manifest | Metadata via report |
| Internal S07 | Role-review workflow manifest | Metadata via report |
| Internal S08 | Selected company-intelligence manifest sections | Metadata via report |
| Internal S09 | Interview-preparation manifest | Metadata via report |
| Internal S10 | Source-trust contract | Metadata via report |
| Internal S11 | Candidate-fit and claim-authority contract | Metadata via report |
| Internal S12 | Workspace discovery binding/change log | Metadata via report |
| Internal S13 | Workspace capture binding | Metadata via report |
| Internal S14 | Workspace interview-preparation binding | Metadata via report |
| Internal S15 | CLI tool reference, asserted tested labels | Metadata via report; no command run |
| Internal S16 | Native runtime binding/mutation gate | Metadata via report |
| Internal S17 | Résumé-generation phase specification | Metadata via report; no exported artifact inspected |
| Internal S18 | Daily practice execution/scoring/retry specification | Metadata via report; no completed attempt inspected |
| Internal S19 | Post-interview debrief/calibration specification | Metadata via report; no private debrief inspected |
| Internal S20 | One-role review phase and rubric | Metadata via report |
| Internal S21 | Profile-integrity agent index | Metadata via report; actual profile/prompt excluded |
| Internal S22 | Compensation strategist index | Metadata via report |
| Internal S23 | Compensation strategist prompt | Metadata via report; treated as evidence, not instructions |
| Internal S24 | Historical lab README | Metadata via report |
| Internal S25 | Selected action-routing map and targeted operation-ID search | Metadata via report; not a complete implementation audit |
| Internal T01 | July 5 loading-shell extraction JSON | Metadata/allowlisted fields reported; original not here |
| Internal T02 | July 5 non-live diagnostic JSON | Metadata/allowlisted fields reported; original not here |
| Internal T03 | July 5 page-not-found extraction JSON | Metadata/allowlisted fields reported; original not here |
| Internal T04 | Later July 5 search-result JSON structure/counts only | Metadata; vacancy identities/content excluded in original review too |
| Internal T05 | Later July 5 detail-object JSON keys/status only | Metadata; employer/pay/description values excluded in original review too |

Private directory filenames used for navigation were not substantive evidence. Unopened directories/link targets are **unreviewed**, not inaccessible or proved absent. This table does not add 30 files to the current local 64-file corpus or assert a new inspection of those originals.

### 7.2 Strengths, weaknesses and gaps: I01–I16

| Expanded observation | Documented strength / issue reported | What can safely follow |
|---|---|---|
| I01 ownership | Coordination, application truth, claims and learning have owners; local working-copy extension sits beside coordination-only wording. | Potential reconciliation burden, not proof of duplicate live records or a chosen architecture. |
| I02 save/capture | Intake does not automatically start capture; saving and applying appear under a broader preparation workflow. | Lightweight save/return remains unverified, not measured abandonment. |
| I03 trust versus fit | Company, vacancy, contact authority, requested activity and fit are separate; soft signals can prompt holds/review. | A reusable distinction, not validated scam detection or known hold-recovery cost. |
| I04 truthful claims | Profile evidence is authority; work/projects/certification/learning/unsupported claims and gaps are distinguished. | Missing record evidence can wrongly suppress a viable role; technical-career assumptions need testing. No real career claim checked. |
| I05 résumé readiness | Draft, structured export input, PDF, receipt and human approval are distinct; existence alone is insufficient. | Useful intended quality rule; no exporter receipt/render/ATS/upload was inspected. |
| I06 practice evidence | Attempts specify time, hints, output, verification, failure/explanation and unseen retries. | No completed attempt, score calibration or predictive readiness evidence. |
| I07 disruption/learning | Deferred/disrupted work and gap limits are documented; debrief distinguishes recollection/interpretation. | Hard gates could burden urgent preparation; this is a hypothesis, not timed friction. |
| I08 compensation | Sources, level/location, full package and rehearsal are covered; first-number/review-window advice is categorical. | Do not make personalised tech-oriented prompt rules universal, especially for fixed scales/shift work/deadlines. |
| I09 human control | Human capture, fit, draft, PDF and submission decisions are prescribed. | Handoff/coordination cost is unmeasured; no inference that every specialist actually ran. |
| I10 control references | Discovery manifest versions 3.29 versus binding 3.30; trust phases omitted from human package maps; phase next pointer differs; targeted search reports no source-trust operation IDs in 56 declared operations. | Reported documentation inconsistencies, not demonstrated runtime bypass or failed security control. Need owner-controlled verification before an operational claim. |
| I11 historical outputs | T01/T03 positive status with loading/404 content; T04/T05 later structured outputs. | Tool completion is not usable evidence; history is mixed, not universal retrieval failure or verified repair. |
| I12 routing | Typed attempts/fallback decisions/terminal receipts are specified; sampled artifacts are provider outputs. | End-to-end route order/exhaustion reliability was not reconstructed. Tested labels are assertions without sufficient linked trace. |
| I13 sector assumptions | Six-factor rubric/skills taxonomy and interview modules are technology-oriented. | Concrete personalised priorities, not cross-industry defaults or a validated fit model. |
| I14 retained evidence | Contact/export/practice/debrief provenance and some cache retention are specified. | Effective minimisation/access isolation/provider handling/deletion not demonstrated; no privacy design selected. |
| I15 freshness/outcomes | July verification metadata/empty evidence list coexist with September change entries. | Metadata cannot establish current verification; empty manifest field does not prove no evidence elsewhere. Outcomes/time saved unknown. |
| I16 uneven coverage | Disruption recovery and honest recall are specified. | No observed device handoff, offline return, assistive technology, rejection coping, networking practice, manual comparison or cover-letter output check in the sample. Sampling gaps are not proof that no such practice exists. |

Historical runtime examples are especially useful if phrased accurately: **the repository review reports** T01 had `status: ok`, `blocked: false`, `text_length: 10`, and `Loading...`; T03 had positive status with a page-not-found title/canonical `/404`; T02 had `live: false`. Conversely T04 reportedly contained two structured results and T05 one structured job object. Structure is not content validation. Neither later file contained the reported complete routing receipt fields `fallback_chain_trace`, `terminal_chain_status`, or `route_id`. July artifacts predate later control changes; no current failure, confirmed fix, submission or hiring result follows.

An external-facing story should refer to **one configured personal process** and these general distinctions, without exposing private locators, exact private configurations, contact exports or application identities. This audit's private-process section is internal review material, not clearance to publish it.

## 8. Historical fictional run: useful failures, no invented participants

The [fixture](../../05_evidence/datasets-and-examples/2026-10-18-synthetic-workflow-check.md) was prepared rather than tested against ChatGPT/Claude/Gemini. R2/H later walked written scenarios against written flows. Jordan and Mira, every posting and employer-like detail, source changes, expiry events and malicious instructions are fictional. The owner did not perform the walkthrough; no job seeker or running software was tested.

| Trace / dimension | Concrete result in the written documents | Presentation boundary |
|---|---|---|
| A4 / D2–D3 | Jordan confirms no SQL, but supplied retail history does not explicitly confirm no three years of analytics. “Confirmed absence” overreaches if applied to both. | Distinguish confirmed absent from unsupported/not supplied; do not invent omitted history. This is an agent document critique. |
| B6 / D2,D3,D6,D9 | Two distinct weekly 22:00 closes cannot fit weekday finish-by-18:00 plus only one available weekend day. Day assignment alone cannot solve it. | The historical flow's potential-conflict label is a definite logical understatement under the given fiction. Employer exception or corrected availability remains possible but unverified. |
| B7 | Next-action emphasis inherits B6's understated conflict. | Correct the conclusion and its dependent action before reusing a script; recorded critique is not evidence the source flow has been edited. |
| A1/B1 / D1 | Link-only/partial capture cannot establish that an employer omitted salary/hours. | Distinguish unread field from not stated in complete captured text. |
| A2–A3/B2–B3 / D7 | Return cues and partial-save wording exist, but pending-save closure/recovery are underspecified. | Written intention, not tested persistence/sync or real user recovery. |
| A5/A6 / D5 | Truthful supplied bullet and version change are visible, but correction dependency invalidation is incomplete. | No actual model generation, export, source refresh or error-rate measurement. |
| D8 | Saved/prepared/link-opened/applied are deliberately separate. | Positive paper design property, not observed submission telemetry. |
| D10–D12 | Manual row-plus-note baseline preserves essential facts if maintained; structured flow adds checking. | No built spreadsheet, timing, preference, readability, keyboard or screen-reader outcome. |

No fabricated-claim or unauthorised-action hard stop was recorded in the paper script, but that cannot verify prompt-injection defences. Equivalent-profile and uncorroborated-company-warning fixture branches were not executed. The absence of those results is not a fairness or employer-warning pass.

The historical brief's in-progress status and repeated Round-01-not-started wording are stale relative to current files. Current R2 navigation explains the chronology; preserve original records as history rather than silently treating them as current gate status. Same-day links resolve to mutable current targets, so their old wording is not an immutable historical snapshot. R2/H's priority tie is absence of a supported demand ranking, not proof of equal market need.

## 9. Contradictions and dependencies that must survive storytelling

| Tempting simplification | Contrary evidence / missing link | Safe interpretation |
|---|---|---|
| Every job requires a new résumé | R1 S08 general résumé; R2 P10 both intensive tailoring and reuse stories | Different strategies are reported; no universal best method or causal comparison. |
| AI saves effort | R2 P05 rewriting/return difficulty, P06 artifact checking, C02 no matching gain | Benefits depend on intervention; include setup, correction, verification, export and recovery effort. JobHub net benefit unknown. |
| AI never helps | C01 experimental relative hiring increase; P09 mixed human/AI routines | Bounded evidence of potential help, not all-provider efficacy. |
| Every warning phrase means a bad employer | V01 host/practitioner disagreement, V03 essential requirements, V02/V04 contracting exceptions, D08 real skill constraints | Signals generate specific checks; they do not establish intent or wrongdoing. |
| Known schedule means job fits | R1 S06 known but potentially unsuitable shifts; fictional B schedule fits while qualifications do not | Conditions, essential criteria and actual evidence are separate dimensions. |
| Low match score means ineligible | D03 permits application despite score; verified applicable credentials can still matter | Do not confuse portal score, missing profile evidence and actual missing mandatory qualification. |
| Phones cannot support applications | R1 S07 immediate phone application; R2 P11 positive mobile reviews; P04 access constraints | Device/task/context differ. No platform decision or exact loss chain follows. |
| More notes/agents prove useful preparation | Internal intended gates, manual alternatives P09/V08 and historical baseline | Document count is activity, not learning, readiness, reduced effort or demand. |
| Positive execution status proves source quality | Internal T01/T03 versus later T04/T05 | Check actual usable evidence and chronology, not status alone. |
| More public references mean more independent confirmation | Repeated MOM report; repeated Women's Weekly story; shared NUS/WSG/Reddit/creator families | Maintain source-family dependence, not a source-count score. |
| Coaching caused a later offer | P01 and earlier Round 00 success accounts have multiple changes/contacts | Temporal sequence, no counterfactual efficacy estimate. |
| Non-participating caregivers are failed seekers | Round 00 G01 intention denominator versus G02 constrained-choice qualitative sample | Different populations/questions; neither supplies a prospective-user count. |

Specific dependencies: R1 S03 = R2 D08 = Round 00 friction D01; R2 P12 = Round 00 friction P04. P07/P08/D06 share NUS career guidance provenance. P01/P12/D12 contain WSG-related support narratives. V02/V04 and V06/V07 each share a creator. V01/V05 repeat a survey family. C01/C02 share authorship and V07 overlaps C01's result. Different Reddit threads may describe distinct accounts but do not create representative or demonstrably independent samples. Different MOM instruments are not the same dataset merely because they share a publisher; distinguish institutional provenance from exact duplication.

Relevant older studies retain their caveats. [SBF/Empact Employability Fund evaluation](https://sbffoundation.org.sg/wp-content/uploads/2024/03/SBF-Foundation-Employability-Fund-Evaluation-report.pdf), Round 00 friction P05, covers selected supported employment, evaluation October 2022–August 2023/programme July 2020–June 2023; stated 26 interviews do not fully reconcile with subgroup counts. [NUS SSR–TOUCH chapter 16](https://fass.nus.edu.sg/ssr/wp-content/uploads/sites/8/2026/03/SSR_TOUCH_Proceedings_Final-1.pdf), G02, published 2026-03-31, reports 40 convenience/snowball interviews July 2024–March 2025 plus three groups/nine stakeholders; eligibility ages 45–65 conflict with a later 40–59 description. Their bounded feasibility accounts are not contemporary general frontline prevalence. [MOM caregiver-return answer](https://www.mom.gov.sg/newsroom/parliament-questions-and-replies/2026/0302-written-answer-to-pq-on-time-taken-for-caregivers-to-return-to-workforce), G01, 2026-03-02, does not disclose the cohort period/method behind its return/intention statistics. Do not turn non-return into failed search or caregiver market size.

## 10. Objective coverage: investigated does not mean resolved

The current [coverage record](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/coverage.md) maps all ten objectives. The audit agrees that each has evidence or an explicit gap. It does not certify equal depth or closure of every question.

| Objective | Traceable support | What remains unresolved |
|---|---|---|
| 1. Search/application/interview pains | P01/P02/P10/P12 → F01/F06/F07 | Comparative active effort versus waiting, prevalence, psychometric confidence change and measured information overload. |
| 2. Fit, red flags, skills and verification | D01–D03/D05/D10/D12; I03/I04/I13 → F02/F03 | No detector performance, actual applicant assessment, verified eligibility or employer-intent test. |
| 3. Pay, market value and negotiation | D04–D07/D11; I08 → F04/F05 | No occupation-cell extraction, personalised salary, local causal negotiation result or withdrawal-risk rate. |
| 4. Truthful résumé/cover letter/interview help | P03/P07/P08/P10, C01, I04–I07, V06/V07/V08 → F06/F07 | Actual draft/export fidelity, cover-letter checking behavior, calibration and real learning transfer. |
| 5. AI use/checking/privacy/manual alternatives | P03/P05/P06/P07/P09/P10, C01/C02, I14 → F08/F12 | Current provider handling, access/retention/deletion and measured end-to-end net effort. Privacy advice is not observed compliance. |
| 6. Capture/interruption/return/access | P04/P05/P11, I02/I07/I16 → F09 | Exact Singapore device-loss chain; local assistive-tech/phone-only/low-confidence completion evidence. |
| 7. Employer language/job quality | D08/D09; V01–V05 → F03 | Exact local phrase encounter/motive; no phrase-to-verdict validation. |
| 8. Five supplied plus bounded new videos | V01–V10 and QV01–QV13 → F11 | No audio/screen verification, independent video statistics or new Singapore salary caption. |
| 9. Internal strengths/weaknesses/gaps | S01–S25/T01–T05 reported in I01–I16 → F10 | Single-owner sample; current execution, outcomes, private-data quality and coordination cost untested. |
| 10. Traceability/contradictions/next step | F01–F12, sources, review, limitations and gate | Owner acceptance, demand, segment/platform/architecture and benefit remain undecided. |

F01–F12 are coordinator interpretations assembled from specialist reports, not twelve independent findings from participants. Confidence is high for inspected record properties, bounded/moderate for particular source-reported mechanisms, and low or unknown for transfer, prevalence, causal JobHub benefit and product priority.

## 11. Process and review audit

The expanded run records **15 Practices + 14 Domain + four Coordinator + 13 video = 46 executed query strings**. The arithmetic and named rows reconcile. That is reported execution documented in logs, not a reproduction of original search-tool histories or elapsed timing. Batches sometimes combine results, so exact result ranking/attribution cannot be reconstructed. Initial-query limits prompted logged follow-ups rather than guaranteeing a hard three-search total in every family.

Practices logs preserve weak/malformed E11, failed honesty-page access, excluded self-reply/summary threads, and E13's missing exact device sequence. Domain logs preserve WSG redirect/empty extraction, NBER failures, a university-hosted replacement, and OECD full-PDF size failure (13,350,420 bytes). The OECD abstract was retained; the full method was not. Video logs preserve noisy/empty batches, failed lower-case ID and uncaptured salary leads. Failed access and snippets are not hidden source evidence.

The [independent review](../../03_research-rounds/02_synthetic-workflow-selection/runs/2026-10-18-pain-practices-and-guidance/review.md) reports a separate reviewer, original-source spot checks, all caption hashes/counts, selected caption passages and complete V09 text. It explicitly did **not** independently read all ten captions, inspect private originals, or inspect original specialist tool-call histories. Independent D07 retrieval timed out. Its correction/read-back record supports bounded research closure, not independent replication of every study or final owner acceptance.

Material corrections recorded there were privacy coverage/F12, qualifying no-measurement wording, replacing stale current Round 01 dependencies, video integration, C01/C02 family overlap, and narrowing a multi-component evidence-pack proposal to one task. This audit directly confirms the corrected integrated wording is present. The review's historical count of 122 local links and 27 documents is a prior validation result, not this audit's independent check count.

Current versus historical status needs deliberate presentation: R2/H remains dated fictional evidence; R2/X is current research. R2/query-plan-draft.md was adopted but retains a closing instruction to create the new run. Specialist handoffs still say synthesis/review pending because they describe their handoff stage. R1's gate describes historical paper work as the next context; R2's later expansion supersedes it. The older cross-research synthesis still proposes executing Round 01. These are navigation/history issues, not proof that completed work did not happen. None authorises selecting a product or reopening private research.

## 12. Story candidates and safe concrete examples

These are editorial candidates for owner review. They are not new research findings, approved features or invented composite participants. A public story should state the evidence class near each example and put detailed IDs/URLs in its source appendix.

| Candidate story beat | Exact evidence route / concrete example | What the narration may say; what it must preserve |
|---|---|---|
| The work starts before writing and continues after it | R2 P02 employed non-tech interview leave/round uncertainty; P12 assignments/final interviews; V01 listener leave segment | Reported effort includes scheduling, correction, attendance and waiting. Do not assign a typical number of hours or promise software removes employer delays. |
| Fit is more than title or keyword coverage | R2 D10 administrative work under engineering title; D03 low-score permission; R1 S05/S06 commute/shift deliberation | Ask about real tasks, conditions, confirmed evidence and essential gaps. No inferred licence rule, job suitability score or finding of bait-and-switch. |
| Show the edit that crosses the line | V06 03:50–04:18 narrated title change, paired with P07 accuracy guidance | A concrete tutorial demonstrates why consequential edits need checking. Label it caption-based narration, not a verified participant outcome or model defect rate. |
| Reuse real stories, then practice explaining them | V08 18:45–21:10 notebook; P09 spoken-story practice; P10 stable/master résumé alternatives | Manual and human approaches are credible comparators. Advice/self-report cannot establish which method saves time or wins more offers. |
| AI has different effects in different workflows | C01 8% relative hiring-probability increase; C02 19% relative posting increase, 44% drafting-time reduction, no discernible match gain | Experimental findings are useful and bounded; different interventions/markets/outcomes, shared authorship, no JobHub result. Never convert relative effects into percentage points. |
| Return to the actual unfinished work | P05 difficult return to an unfinished draft; P04 shared/library access; P11 save failures and positive mobile reviews | These support broader recovery/access questions. Do not turn them into one person's phone-to-laptop lost-opportunity story. |
| Compare a package before calling it market value | D04 measurement definitions; D11 base unchanged/equity increased; D05 terms checklist | One reported package trade-off and official definitions show why components/conditions matter. No current personal salary, universal uplift or local success rate. |
| Convert concern into a verifiable question | V01 fast-pace disagreement and delayed-hire counterexample; D01 authenticity versus D08 shortage explanations | Ask about scope, headcount, duties and specific requested actions. Do not diagnose bad faith from a phrase, a pause or an expired/repeated post. |
| Internal design lesson: completion is not usable evidence | Reported internal T01/T03 shell/error versus T04/T05 structured outputs; I05 readiness distinction | Internal-only process example, attributed to the existing review. Not current reliability, a demonstrated fix, or permission to publish private tooling details. |
| Fictional examples can expose reasoning mistakes | R2/H B6 availability contradiction and A4 unsupported-history distinction | Clearly label fiction and agent paper review. A useful illustration of checking combined constraints, not testimony, demand or a tested product. |

An editorial through-line supported by these sources is: job seekers may need to decide what deserves effort, express real experience, verify changes, and recover the next action; assistance should be compared with manual/human alternatives using truthful information and total work. This is **synthesis**, not a statement that all job seekers want an evidence-pack product.

Avoid invented prevalence, invented interview dialogue, a composite participant assembled from different posts, implied listening, current legal/provider claims not checked here, and claims that every objective is solved. No experimental result here establishes JobHub demand, value, willingness to pay, hiring impact, accessible implementation or a preferred surface.

## 13. Handoff and validation boundary

Observed checks in this audit: complete assigned-root enumeration including hidden/ignored files; all 64 files read as specified; all ten caption hashes/cue counts matched; no byte-identical local duplicates; qualified IDs reconciled; selected original studies/methods directly checked with failures recorded. Private originals remained unopened. No new data collection, model comparison, participant session or software test is claimed.

The output is this Markdown audit only. All other existing files belong to the owner/other workers. Any subsequent slide review is read-only and does not silently change this research into accepted scope. The appropriate next owner decision is which bounded uncertainty, if any, to test with identical facts and a credible manual baseline; the current gate's truthful-example selection experiment remains a proposal.

