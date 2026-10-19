# Independent Round 03 presentation review

19 October 2026. Evidence and readability QA only. Author/coordinator owns corrections and acceptance.

## Final targeted readback: v8

**All four original must-fix groups are resolved in the inspected v8 previews and latest JSON. No unresolved slide finding within this targeted scope.** This readback supersedes the initial findings below; it does not constitute owner acceptance or a full-deck compatibility test.

JSON SHA256: `EE3D4E411CFBC1578BD65C31613EB776B899AEC9CC8E94D1CCA5F5F085AD1722`, unchanged across the readback. Still 48 slides, 30 main and 18 appendix. All 48 v8 preview files were present. Individually inspected the actual **1280×720 v8 images at original size for slides 26, 27, 35, 36, 42, 45, 46 and 47**. All 13 profile labels were checked in JSON; representative breadth/deeper-profile headings were checked visually in those six profile images. No clipping, overlap or unreadable wrapping was observed in this sample. Slide 27's shortened takeaway now fits on one line with clear space above its footnote.

| Original group | Readback result |
| --- | --- |
| 1. Slides 27/36: AI evidence versus uptake | **Resolved.** Both now explicitly describe limited evidence of applicant AI use. The changed text is present and fits in the v8 images. |
| 2. Slide 42: conditional allowances | **Resolved.** R3-C01 is embedded, cited by the allowance claim and included in the original-source URLs. Its URL, publication date, event period, observation, limits, locator and family match the retained worker-c JSON record. Visible footnote dates scheme terms to 6 November 2025 and states these are not guaranteed basic pay. Notes retain completion/appointment conditions and the shared Income source family. The 2020 story remains dated and historical. |
| 3. Slides 35–47: interpretation labels | **Resolved.** All 13 JSON profiles have the exact heading “Suggested checks” and a visible lead stating “Checks are research interpretation.” Both labels render clearly in the six profile images sampled. The other seven profile images were not re-inspected in v8. |
| 4. Slides 26/45/46: plain language | **Resolved.** Slide 26 uses “dated job reference,” “Dated activity for this job” and “Dated statement or record for this job.” Slide 45 groups hospitals under healthcare and schools under education. Slide 46 explicitly says the linked frameworks were not read and refers to skills supported by one's own work. All changes are present and fit in their v8 images. |

**49 distinct R3 claim IDs now resolve to 49 embedded records**, with no missing claim IDs. This pass rechecked R3-C01 against its local original record; it did not repeat the initial full metadata comparison for every older record. No external research or source opening occurred.

Handoff status: **delivery-label item resolved.** The current README correctly states **48/30/18**, the **19 October 2026** cutoff, **v8** as the current export and `jobhub-domain-brief-v8.pptx` as the editing file. The author updated it during readback; the v8 labels were subsequently verified directly. `audit-round3.md` exists; its contents were not re-audited in this targeted pass. This label-only follow-up adds no visual inspection, package/static-validation claim or owner acceptance; the inspection limits below remain unchanged.

Inspection limits: this was an eight-image v8 readback plus targeted JSON/record checks, not a repeat visual review of all 48 slides. No final PPTX inspection, browser navigation, printing, Office/LibreOffice test, screen-reader evaluation, accessibility conformance test or user-comprehension study occurred. No build or mutation-producing verifier was run. Only `review-round3.md` was updated; no slide or research content was edited.

## Initial review scope and snapshot (v6)

Confirmed **48 slides: 30 main, 18 appendix**. Reviewed new main slides **23–27** and all **13 profiles, 35–47**. Also checked slides 1, 4, 20, 28–29, 31 and 48 for dates, research boundaries and namespaces. Latest JSON checked: SHA256 `DC54E293609E353F74709089DD3E82F46966B9A262D05A5E6B38083010434DC0`. The author changed the JSON during review; the added R3-C03 finance citation is present in this snapshot.

Inspected the requested AGENTS/role files and presentations skill, style, template and finalization guidance; `slides.json`, generated claim-map conventions, README and build/verification logic. Research trace used the Round 03 run `2026-10-19-cross-industry-and-vacancy-credibility`: findings, comparison, limitations, coverage, practices, arts/trades supplement, vacancy-credibility report, all 13 industry-profile Markdown files, relevant six-sector report passages, and selected source records in seven contribution JSON files. The additional R3-C01 allowance record was inspected in `contributions/worker-c.json`.

Visually inspected individual **1280×720 v6 PNGs at original size** for slides 23–27 and 35–47, plus 1, 4, 28, 29, 31 and 48. No web search or external source opening occurred.

## Initial must-fix findings (all resolved in v8 above)

1. **Slide 27, “What the extension changes”; slide 36, “S02 Food and hospitality” — describe the evidence gap, not low actual AI use.** “AI use by occupation is thin” can imply low uptake. F07 and the limitations establish limited evidence, with uptake unknown. Use “Evidence of applicant AI use by occupation is limited.” Likewise replace slide 36's “Housekeeping, outcomes and AI use remain thin” with “Evidence on housekeeping, outcomes and applicant AI use is limited.” Keep these concise enough to preserve the existing layout. Confidence: high.

2. **Slide 42, “S08 Finance and insurance” — complete the allowance citation.** Its second claim names “conditional allowances” but cites M14/C05/C09/C11. C09 describes a **fixed** allowance; the completion/appointment conditions come from **R3-C01**, currently absent from the embedded evidence records. Add that retained record, its original URL and the claim citation, preserving its scheme date of **6 November 2025**, or remove the conditional-allowance example. Do not present it as recurring guaranteed basic pay. R3-C03 now supports the separate internal specialist-transfer example; no further fix is needed for that citation. Confidence: high.

3. **Slides 35–47, profile right columns — label reviewer suggestions visibly.** “What matters” combines recommended checks with evidence statements. The JSON marks these mostly as interpretation, but a reader looking only at the slide cannot see that distinction. Use a heading such as **“Suggested checks”**, with “Research interpretation” in the common profile explanation/lead, or an equally clear visible label. This is a communication correction, not validation that the checks improve outcomes. Confidence: moderate, heuristic readability judgement.

4. **Slides 26, 45 and 46 — remove internal research language from reader-facing copy.** On 26, explain “requisition” as a job reference and replace “Attributable, period-specific evidence” with a concrete phrase such as “A dated statement or record for this job.” On 45, replace “Public hospitals and schools retain their actual activity” with “Group public hospitals under healthcare and schools under education.” On 46, use “This review did not read the linked frameworks” and “skills supported by your own work” instead of “not thereby inspected” and “personally evidenced skills.” The point is understandable after reading the research, but these phrases make an unfamiliar reader do unnecessary interpretation. Confidence: moderate, heuristic judgement.

## Initial evidence checks and limits retained

- **All 48 distinct R3 claim IDs resolve** in the latest JSON. Their URL, publication date, event period, observation, limit and locator fields match their selected underlying source records. Every declared `refs` key resolves and every declared local source path existed when checked. ID resolution does not prove that each citation supports every clause; item 2 is such a support gap.
- Slide 25 correctly identifies the **4 July 2018 MOM alert**, unnamed agency and unknown underlying event date. It does not claim current Singapore prevalence or accuse a current employer.
- Slide 42 visibly dates the curated Income story **31 December 2020**. Notes retain unknown transition dates/pay and the historical 2025 DBS programme boundary. No personal pay-cut claim appears.
- Slide 44 correctly treats Wild Rice's **21 November 2025** notice and **December 2025 deadlines** as historical, with possible 2026/27 casting rather than a current job or verified hire.
- Slide 41 keeps the Singapore operator/machinist gap visible. R3-P04 is international/unspecified, with no Singapore setting established; past assessments and proposed future tests remain separate in its notes. It cannot fill the local gap. Prefer that precise geographic wording to implying a known foreign country.
- Slides 4, 20, 28–29 preserve public-source/internal-document scope, no direct JobHub user study, unmeasured benefit and owner control of any proposed test. Owner-only checking would not establish representative usefulness.
- Slides 23–24 and 48 treat 13 profiles/six inquiries as coverage organisers. Repeated hotel, SingHealth and Income records are not independent votes, participants or proof of confidence. Earlier unqualified P/D/C/I/V IDs remain tied to expanded Round 02; R3- identifies the new run. The cutoff is now **19 October 2026**.

## Initial delivery gates and untested areas (historical v6 status)

The README is still a prior-version handoff: **30 total / 25 main / five appendix, 18 October cutoff, v5 export**. Before delivery, update it to the reviewed final version and boundaries, keeping the **136-file audit explicitly historical**. Slide 48 notes refer to `audit-round3.md`, which did not yet exist when checked; supply that audit or correct the statement. These are pending author finalization tasks, not files changed by this reviewer.

No clipping, overlapping text or missing table content was visible in the requested v6 previews. Slide 27's two-line takeaway sits close to the footnote; shorten it if revised copy needs more room. Body/table text was legible at native preview size. This does not establish readability at a smaller display or successful comprehension.

A v7 build directory appeared during review. **No v7 or subsequent previews, final PPTX, browser navigation, printing, Office/LibreOffice behaviour, screen-reader reading order, accessibility conformance or user comprehension were tested.** No build or mutation-producing verifier was run. After corrections, the author should rebuild and obtain targeted visual readback of changed slides and the final handoff.

Only this review file was created. No presentation/research content, other agents' work or product decisions were changed. No PowerPoint validation, user study or owner acceptance is claimed.
