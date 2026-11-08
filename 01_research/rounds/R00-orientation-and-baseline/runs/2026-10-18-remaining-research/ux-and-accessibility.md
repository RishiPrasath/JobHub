# UX, product surfaces and accessibility

Date: 2026-10-18. Roles: UX and User-Flow Designer with UX Expert perspective; one collector. Status: reviewed desk research; human acceptance pending and no platform approval. Subsequent review is recorded in `review.md`.

## Scope and evidence boundary

Coverage: R-06 and UX/R-15, with implications for R-02/05/09/10. Inspected: `AGENTS.md`, `_agents/README.md`, roles 07/13, the [brief](brief.md), instructions README and 00/01/02/05, backlog, and both [product](../../../../../_drafts/product-research-strategy.md) and [development](../../../../../_drafts/ai-era-development-strategy.md) drafts.

Prior [UX findings](../2026-10-18-ai-job-hunting-workflows/specialists/ux-workflows.md) document a preparation workflow, propose comprehension/return exercises, and explicitly lack device-behaviour evidence. The [friction review](../2026-10-18-job-search-friction/specialists/workflow-review.md) distinguishes unsuitable working conditions, information uncertainty and process effort. This report extends those findings with capability constraints and testable interactions; it does not repeat population research or claim that software fixes employment conditions.

**Observed** means documents or tracker state directly inspected. **Reported** means a provider documents a capability, not that JobHub demonstrated it. **Recommendation** means a proposed design or study. Confidence is high in inspected WCAG levels, moderate in platform capability transfer, and low in product preference and usability until observed with users. Native web searches and source opens were performed; ten substantive primary sources are registered below.

## Surface comparison and provisional direction

**Recommendation:** compare a responsive capture-and-preparation prototype with a capture-companion alternative. Responsive web permits examining one journey at multiple widths; this is not architecture approval. Mobile-only participants must be able to complete preparation.

| Alternative | Proposed responsibility and benefit | Cost, limitation and selection evidence |
| --- | --- | --- |
| Desktop-focused web | Spacious posting/evidence/draft comparison; familiar keyboard editing | Risks excluding phone-only use. Prefer only if actual recruitment establishes desktop availability and sustained preparation needs. |
| Responsive web | Same saved jobs and preparation actions across widths; link-based entry | Requires deliberate content order and touch/keyboard testing. A collapsed desktop dashboard is insufficient. |
| Mobile-first web | Short capture, review and return steps; sequential drafting | Long documents may require more navigation. Compare sequential editing against desktop comparison before assuming either wins. |
| Installed PWA | Optional home-screen return, implemented offline work and supported share reception | Installation, storage and permission conditions vary. Installation alone proves neither offline readiness nor share reception [U02–U05]. |
| Native mobile | OS-specific capture entry and device integration | Android receiving intents and Apple's Share extensions are distinct mechanisms [U07/U08]. Distribution, lifecycle and accessibility work multiply; justify through observed capture failures. |
| Browser extension plus workspace | User-invoked capture while viewing a posting | Chrome `activeTab` provides temporary access after invocation, with restrictions [U06]. Does not establish universal browser/mobile reach or permission to reuse portal content. |
| Multiple surfaces | Quick capture on one device, deeper work wherever convenient | Adds account, sync, conflict and support burden. Choose only if handoff benefit exceeds these extra failure points. |

**Reported capabilities:** outbound Web Share sends content; Web Share Target registers an installed web app to receive it. Chrome also warns that incoming fields can vary [U02]. **Observed:** WebKit issue 194593 remains `NEW` [U03]. **Inference:** do not promise iPhone PWA share reception; retain paste/manual capture and test actual supported devices. An open issue is not a complete compatibility matrix.

Offline functionality needs implemented storage/caching, and browser data can be evicted or cleared [U05]. Recommend initially testing previously saved text and queued notes; new remote analysis should say it needs a connection. Local saving must never imply cross-device availability.

WebKit documents web push for iOS/iPadOS 16.4 Home Screen web apps with user interaction and permission [U04]. That is a conditional capability, not guaranteed reminder delivery. Recommend opt-in reminders after a user chooses a next action, discreet notification text, quiet controls and an in-product return list. Declining notifications must leave the journey usable. Neither notifications nor native packaging should be justified by hypothetical engagement gains.

## Concrete interruptible journey

This journey is a **recommendation**. Test synthetic service/operations and professional roles, then consented, redacted examples.

| Transition | User-visible state and next action | Failure, recovery and control |
| --- | --- | --- |
| Discover → capture | Paste URL/text, or use an available capture entry. Preview received content; optional “Why I saved this.” | Malformed link: retain input and explain correction. Unsupported source: save link only or paste text. Never imply a full posting was captured when only a URL arrived. |
| Capture → saved | Show role/company if available, capture time, source and “Link saved” or “Posting saved.” Review later is valid. | Missing title can use an editable placeholder. Duplicate candidate: open existing, keep separate, or review a merge; never silently replace notes. Save failure retains recoverable input and offers retry/copy. |
| Saved → interrupted | Record latest acknowledged save and chosen next action. User can close without completing a profile. | Distinguish “Saved on this device,” “Waiting to sync” and “Available on your other devices.” Storage failure must not show success. Resume retry must not create duplicates. |
| Return → orient | “Continue reviewing this role”; show prior note, unfinished step and last saved time. Keep same-device return available. | Expired login preserves draft where the agreed privacy model permits. Missing remote changes: explain pending sync. Concurrent edits: show both versions and let the user resolve them. |
| Orient → assess | Show requirements, user evidence, unknowns and source excerpts. Let users save, defer, skip or prepare. | Missing pay is “Not stated in captured posting,” not poor pay. Capture failure is separate from absence. User correction keeps its origin and can be undone. |
| Assess → prepare | Build a short checklist; connect each application claim to user-confirmed experience. Draft, review and export in separate steps. | Analysis timeout preserves capture and offers retry/manual review. Unsupported achievement requires correction or removal. Export failure retains the draft and offers a copyable version. |
| Prepare → external application → return | User reviews documents, opens employer process, then records their actual outcome. Interview work reuses the chosen application version. | Opening a link/exporting a file never marks “Applied.” Keep submitted status user-confirmed. Do not promise to undo an employer submission. |

For changed postings, keep the captured version, retrieval time and newly checked version distinguishable. Show meaningful differences and which advice may need review. A failed refresh means “Could not check,” not “Closed.” If removal is confirmed, preserve the user's preparation and offer archive or continued interview practice. Recommend reversible archive with a persistent restore route; a disappearing toast must not be the only undo. Permanent deletion and snapshot-retention policy remain owner decisions.

## Information, explanation and cognitive load

**Recommendation:** start navigation with “Saved jobs,” “Applications,” and “My experience,” plus consistent help/settings. Keep preparation inside each job, with Overview, Evidence, Preparation and Activity. Test this against a simpler single job page before adding global work queues. An empty state should offer one example and “Save a job,” without requiring a complete CV.

Lead each job with identity, status and one next action. Group related fields; use spacing and headings consistently; keep secondary options visually quieter. On narrow layouts, place the source immediately after its associated claim, rather than far below a long analysis. Offer an explicit evidence disclosure button, not hover-only explanations. Preserve a readable linear order when comparison panels collapse.

Use four plain labels: “Posting says,” “Your confirmed experience,” “Possible implication,” and “Not known.” For example, a synthetic posting's rotating-shift requirement can support “Check whether the schedule works for you”; it cannot establish an unsafe employer or predict rejection. Reveal the excerpt, source/date and reason for the suggestion. Distinguish source reliability, extraction uncertainty and personal relevance; a single confidence percentage conflates them. Prefer explained strengths and unresolved requirements over an unexplained fit score. Provide “Correct this” and “This does not reflect my situation.”

Keep summaries short, with detail available on request. Avoid anxiety-inducing badges for missing information, application streaks and fabricated completion estimates. During analysis, name the actual activity, provide cancellation, and allow return later. Test labels with people unfamiliar with AI terminology and across occupations; plain English alone does not prove language inclusion.

## Accessibility requirements and practical evaluation

**Observed standard:** WCAG 2.2's published Recommendation is dated 2024-12-12 [U01]. Recommend an AA target, subject to owner acceptance and complete evaluation. Selected mappings are not a conformance checklist:

| Criteria | Level |
| --- | --- |
| 1.3.1 relationships; 1.4.1 colour; 2.1.1 keyboard; 2.1.2 traps; 2.4.3 focus order; 3.3.1 errors; 4.1.2 name/role/value | A |
| 1.4.3 contrast; 1.4.4 text resizing; 1.4.10 reflow; 1.4.11 non-text contrast; 1.4.12 spacing | AA |
| 2.4.7 visible focus; 2.4.11 focus not entirely obscured; 2.5.7 dragging alternatives; 2.5.8 targets; 3.3.8 authentication; 4.1.3 status | AA |
| 2.2.2 pause/stop/hide; 2.3.1 flash thresholds | A |
| 2.3.3 interaction animation; 2.4.13 focus appearance | AAA |

Resizing covers 200%; vertical reflow uses 320 CSS pixels, with exceptions. Target minimum is 24×24 CSS pixels with exceptions, not an unconditional 44-pixel AA rule. Motion criteria have distinct applicability; reduced-motion support is not equivalent to passing them [U01].

**Proposed validation:** run the entire synthetic journey with keyboard alone, then NVDA/Chrome and VoiceOver/Safari on recorded versions, supplemented by participants' own configurations. Check capture controls, source disclosures, error recovery, draft editing and restore. Record focus location after every dialog, navigation and retry. Screen-reader users should hear save outcomes once and find the relevant evidence without listening to every streamed token.

At enlarged text and narrow widths, inspect long role names, source links, error text, sticky actions and document previews for clipping or hidden controls. Apply text-spacing overrides and OS text settings. Measure text/control contrast in default, focus and error states. Test reduced motion, touch targets, non-drag reordering and password-manager/paste use. Combine automated checks with manual tasks; record exact defect, affected journey, environment and retest result. No accessibility checks, software tests or certification were performed in this research run.

## Inclusive usability protocol

**Recommendation:** after owner approval, run two formative rounds of six to eight adults, revising between rounds. This is a practical study size, not population representation. Recruit active Singapore seekers/returners through varied channels, including community/career-support routes; do not rely only on developer contacts. Include service/trades/operations, graduates and career transitions, phone-only users, low digital confidence and varied access needs. Recruit by relevant behaviours and accommodations, without requiring diagnoses. Disability is not evidence of inability to consent.

Offer remote/in-person modes, accessible materials, interpreters or support people where requested, breaks and flexible scheduling. Let participants use familiar assistive technology; address participants directly and ask before assisting [U10]. Propose 45–60 minutes with additional setup time; avoid timing people against an able-bodied speed norm. Agree compensation in advance, independent of task success or withdrawal.

Before the session, explain purpose, observers, voluntary participation, data collected, retention, withdrawal contact and any transcription/AI processing. Obtain accessible recorded consent; separate recording permission from participation and allow notes-only sessions [U09]. Use synthetic profiles by default; never require live applications, private credentials or unredacted CVs. Agree a deletion schedule and participant-ID handling before collection. GOV.UK supplies research practice, not Singapore legal clearance.

Tasks: capture an incomplete posting; interrupt at a disclosed pause; return on the same device or a second device the participant actually uses; explain an inference and unknown; inspect a changed posting; correct a seeded unsupported claim; recover from save/export failure; archive and restore. Counterbalance variants and ask neutral prompts. Measure unaided completion, help, errors, recovery and evidence comprehension; time is descriptive. Record participant statements separately from observed actions. Any task-blocking exclusion, lost work or false submission state requires correction and retest, regardless of aggregate success. This replaces treating the earlier four-of-five pilot proposal as acceptance evidence.

## Owner learning and next decision

The owner should map one recent workflow, sketch competing job pages, write missing-data/error text, and explain each next action. Practise keyboard/enlarged-text use, then observe consented sessions without coaching. Log evidence versus assumptions; rank harm, exclusion and recovery cost. These exercises do not simulate disabled users' experiences.

Delegate to AI bounded alternatives, terminology consistency checks, scenario generation and critique linked to specific criteria. Require each critique to name its evidence, uncertainty and alternative. The owner retains recruitment ethics, interpretation of user behaviour, prioritisation and acceptance. Attractive generated screens and synthetic personas are not validation.

Next recommendation: approve a bounded prototype study comparing responsive sequential preparation with a capture-companion journey. Add an extension only if repeated browser capture friction warrants its permissions/maintenance; consider native capture if necessary OS reception cannot meet users' needs through web fallbacks. Keep a single surface if handoff adds little benefit. Device ownership, interruption frequency, willingness to install, supported browser combinations, real source payloads and language/access barriers remain unmeasured. These gaps prevent a final platform decision, but do not prevent testing the concrete flow above.

## Source register and verification

All sources accessed and opened on **2026-10-18**. Dates below are displayed publication/update/version dates; unknown dates are not inferred from crawl timestamps. H = high confidence in documentary content; M = moderate applicability pending device or local validation.

| ID | Primary source and date | Inspected scope; limitation/confidence |
| --- | --- | --- |
| U01 | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), Recommendation 2024-12-12 | Selected criteria, levels, exceptions and version header; normative web standard, no JobHub evaluation. H. |
| U02 | [Chrome Web Share Target](https://developer.chrome.com/docs/capabilities/web-apis/web-share-target), updated 2019-11-08 | Installation, receiving versus sending, manifest and payload caveats; old footer, no exhaustive current device matrix. M. |
| U03 | [WebKit issue 194593](https://bugs.webkit.org/show_bug.cgi?id=194593), filed 2019-02-13 | Observed NEW status and request scope; comments are not release guarantees. M. |
| U04 | [WebKit web push](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/), 2023-02-16 | iOS/iPadOS 16.4 introduction, Home Screen, gesture/permission and Focus; historical beta announcement, not present-device verification. M. |
| U05 | [web.dev Offline data](https://web.dev/learn/pwa/offline-data), updated 2022-01-10 | Storage, persistence, quotas and deletion; no offline or sync demonstration. M. |
| U06 | [Chrome activeTab](https://developer.chrome.com/docs/extensions/develop/concepts/activeTab), displayed update 2012-09-21 | Invocation, temporary access, same-origin continuation and restricted pages; unusual old footer retained, Chrome-specific. M. |
| U07 | [Android receiving data](https://developer.android.com/develop/ui/compose/sharing/receive), updated 2026-10-16 | Intent/MIME registration, preview/confirmation, validation; provider example, not stack selection or measured usability. H/M. |
| U08 | [Apple Share extensions](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html), archived; date not established | Input context, preview, validation and constrained UI; architectural explanation, current SDK behaviour untested. M. |
| U09 | [GOV.UK informed consent](https://www.gov.uk/service-manual/user-research/getting-users-consent-for-research), published 2016-05-24, updated 2018-11-05 | Accessible consent, disclosure, withdrawal and records; adapted research guidance, not Singapore law. H/M. |
| U10 | [GOV.UK research with disabled people](https://www.gov.uk/service-manual/user-research/running-research-sessions-with-people-with-disabilities), published 2017-10-03 | Before/during/after sessions, own equipment and respectful assistance; no JobHub participant evidence. H/M. |

Access limitation: [Apple's current web-push page](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers) opened to a JavaScript shell; its offered Markdown link returned an internal error. Search text was not substituted for inspected content. U04 therefore supports a qualified historical capability statement. All other registered pages exposed substantive text. No demos were installed or exercised.

Collector verification: checked source IDs and criterion levels against opened documents. All five local links resolve; no trailing whitespace was found. Only this assigned report was written; the collector spawned no subagents and performed no commits, external mutations, interviews or usability tests. Subsequent coordinator and independent review are recorded in `review.md`; human acceptance remains pending.
