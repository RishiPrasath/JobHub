# Technical and responsible-AI research: R-09, R-10, R-14

Date/access date: 2026-10-18. Collector: Technical Architect, incorporating Responsible AI Reviewer and AI Tools Expert perspectives. Status: reviewed desk-research recommendations; human acceptance pending. Subsequent independent review and corrections are recorded in `review.md`. No implementation, security scan, interviews, model benchmark, or legal clearance occurred.

## Scope and evidence

Read `AGENTS.md`, `_agents/README.md`, roles 08/11/15, this run's [brief](brief.md), research instructions 00/01/07, the backlog, both [product](../../../../../_drafts/product-research-strategy.md) and [development](../../../../../_drafts/ai-era-development-strategy.md) drafts, technical/quality strategy documents, and the earlier [workflow synthesis](../../../../04_results/ai-and-job-hunting/2026-10-18-ai-job-hunting-workflows.md), responsible-AI review, tools handoff, and [synthetic fixture](../../../../05_evidence/datasets-and-examples/2026-10-18-synthetic-workflow-check.md). This report extends those findings with capture, lifecycle, architecture and evaluation contracts; consumer-product comparisons, Codex configuration, CI and development methods are outside scope.

**Observed** means content actually inspected in an opened official source. **Reported** means an authority's guidance or vendor's stated policy, not independently verified implementation. **Recommendation** means this report's proposed design. Confidence is high in the narrow source observations, moderate in design applicability, and unmeasured for runtime effectiveness.

## R-09: Capture and rights

**Observed/reported:** RFC 9309 explicitly separates robots rules from access authorization [S01]. LinkedIn's help page prohibits specified scraping/browser automation and copying without content-owner consent [S02]; this is evidence about LinkedIn's policy, not every job board or a judicial determination. IPOS describes a computational-data-analysis exception with lawful-access, purpose and sharing conditions [S10]. That does not establish that preserving and redisplaying complete postings in JobHub qualifies.

**Recommendation:** assess rights per source and operation: access, extraction, storage, model transfer, quotation and redistribution. Record terms URL/version, access conditions, permission/licence evidence, robots check where applicable, review date and unresolved restrictions. A logged-in session, public URL, user upload or permissive robots file is insufficient by itself. Do not bypass access controls. Seek source-specific advice when copyright exceptions, contractual restrictions or jurisdiction interact; no blanket permission is inferred here.

| Capture route | Practical proposal and fallback |
| --- | --- |
| URL retrieval | Use approved sources/APIs; record retrieval failures, redirects and completeness. When unavailable, retain a bookmark and request permitted material. |
| Browser selection | User selects one posting; preview extracted fields and avoid cookies, hidden account data and unrelated page content. Source terms still apply. |
| Pasted text | Low-integration option; ask for source URL/date and mark missing provenance. Pasting does not cure rights restrictions. |
| Screenshot | Crop irrelevant/private content; preserve image coordinates for OCR evidence, flag uncertain digits and missing sections. Offer text correction. |
| Email | Prefer selected-message import over inbox-wide access; strip signatures, recipients and unrelated threads where unnecessary. Sender identity and forwarding are not proof of reuse rights. |
| Manual entry | Always provide a structured fallback; label user assertions separately from verified source statements. |

Preserve immutable versions where retention rights permit; a new capture supersedes rather than silently rewrites the evidence used for an earlier analysis. Deduplicate provisionally by employer, title, location and source identifier; never merge conflicting salary or contract terms silently. Use snapshots for reproducible analysis; recheck availability, deadlines and material terms before consequential preparation. Display “captured on” separately from “last checked.” A content hash detects change, not authenticity.

## Data contract and lifecycle

**Recommendation:** keep profile evidence separate from postings and generated advice. Minimum profile: user-confirmed experience/skills and supporting examples, relevant qualifications, preferences and optional constraints. Exclude identity documents, full birth dates, health narratives, protected-characteristic inference and third-party reference details from routine model inputs. Let users express functional needs, such as predictable hours, without disclosing diagnoses. Keep contact details separate from analysis context; add them only to an explicitly reviewed export.

Proposed logical schema, independent of database or language:

| Record | Required distinctions |
| --- | --- |
| SourceVersion | `source_id`, `version_id`, URL/origin, capture method/time, source publication/update date or null, content hash, completeness, language, rights status, superseded version, retention class |
| Claim | field/value/unit, `explicit / user_reported / inferred / unknown / conflicting`, evidence locator and source version, extraction method/version, confidence rationale, reviewer correction |
| ProfileEvidence | user ownership, claim and supporting evidence, confirmation time, purpose, sensitivity, allowed processing destinations |
| AnalysisRun | input version IDs, model/provider/product identifier, prompt/schema/tool versions, settings, output claims, cost/latency/failure metadata, review status |
| Action | proposed/reviewed/executed state, exact payload and destination, authorization reference, execution result; never infer submission from document generation |

Null salary means unknown or unavailable, not zero. Preserve a reason such as absent from a complete captured posting, incomplete capture, failed extraction or conflicting values; only the first supports “not stated in the captured posting.” An unstated qualification is unknown, not absent. Preserve currency, pay period, ranges and qualification wording before normalization. Every material inference needs an explanation and evidence; every explicit claim must resolve to the captured passage or image region. Corrections create traceable revisions and invalidate dependent advice.

**Proposed lifecycle:** capture → classify/redact → user review → purpose-limited storage → selected processing → versioned result → correction/export/deletion. Encrypt transport and stored personal data, separate keys/secrets, restrict tenant access, and exclude private profiles from Git and default telemetry. Prefer transient raw uploads: propose deletion after confirmed extraction, with a maximum 24-hour failed-upload window; retain originals longer only for a stated user purpose. Propose 30-day content-free operational logs and 30-day backup expiry, subject to explicit owner approval and implementation verification. Review inactive records rather than inventing a universal legal retention period.

Deletion must cover originals, OCR, derived claims, embeddings, caches, exports under service control and provider objects. Track pending vendor/backup expiry, revoke access promptly, and ensure restored backups reapply deletion records. Explain copies outside JobHub's control and any justified legal hold. A hidden UI record is not evidence of erasure.

Separate three retention classes: raw original uploads; authorised evidence excerpts/image crops; and derived claims/analysis. Each needs its own disclosed purpose, rights, expiry and deletion behavior. Deleting an original may leave a minimal evidence excerpt only when separately permitted and disclosed; it must not silently retain the original under another label. When supporting content expires, mark dependent citations “Evidence no longer available” and downgrade verification or request a new permitted source. Hashes, coordinates and remembered model text cannot reproduce deleted evidence. “Immutable version” means no silent modification during its permitted lifetime, not exemption from deletion.

## R-10: Singapore applicability, fairness and architecture

**Observed/reported:** PDPC's obligations page covers purpose, notification/consent, accuracy, protection, retention, overseas transfer, access/correction, accountability and breach assessment [S03]. Its 2024 AI guidance summary addresses development, consumer information and possible data-intermediary roles [S04]. Its July 2026 generative-AI summary adds lifecycle responsibility allocation and handling individual requests [S05]. These landing pages were inspected; their full guideline PDFs were not successfully reviewed.

**Recommendation:** if JobHub operates as an organisation handling personal data within PDPA scope, map each processing purpose, party, destination and applicable obligation before a personal-data pilot. Do not assume research exceptions, anonymisation, consent or a Singapore storage region resolves all obligations. Confirm operator/provider roles, exceptions, overseas safeguards, complaint contact and incident responsibilities against complete guidance and the actual service arrangement. This is a conditional implementation checklist, not legal advice or compliance certification.

Fairness controls should preserve opportunity: explain requirement-by-requirement evidence, distinguish mandatory from preferred criteria, and show transferable experience. Avoid opaque fit percentages, hiring probabilities and automatic exclusion. Let users correct evidence, disagree and continue exploring. Do not infer age, ethnicity, disability or immigration status from names, writing or career gaps. Where work authorization or a licence is relevant, request an optional explicit fact and identify the source requirement. Test equivalent evidence across names, writing styles, career breaks and sectors; name-masking alone is insufficient. Company allegations remain attributed and qualified, never transformed into established misconduct.

Architecture options are recommendations for comparison, not adopted choices:

| Option | Benefits | Costs and revisit condition |
| --- | --- | --- |
| Local processing/storage | Offline access and smaller remote-data exposure | Device loss, backup/key recovery and hardware support; reconsider if multi-device continuity is essential. A remote model call still transfers data. |
| Cloud service | Central recovery, coordinated updates and cross-device state | Tenant isolation, operational security, transfers, contracts and deletion obligations; reconsider if these exceed owner capacity. |
| Hybrid | Local raw profile/capture with selected redacted remote analysis | More complex sync, conflict resolution and deletion; reconsider if measured privacy benefit does not justify complexity. |

For the first technical experiment, recommend a portable source/claim contract and deterministic capture/review baseline. Compare local and managed-cloud operation using synthetic data before selecting deployment. Add hybrid synchronization only if observed journeys require it. Keep extraction, evidence storage, analysis and external actions as distinct logical boundaries; this does not prescribe microservices or any stack.

### Threat controls and corresponding fixtures

OWASP documents indirect/multimodal injection and excessive agency [S06]. These proposed controls address plausible JobHub threats; they are not findings from an application scan.

| Risk | Proposed mitigation | Required fixture result |
| --- | --- | --- |
| Prompt injection | Treat posting/email/image text as data; isolated extraction without action credentials; validate citations | Embedded instructions cannot disclose profile data, alter authorization or trigger tools |
| Excessive agency | Narrow tools, application-enforced permissions, payload-specific approval and idempotency | Expired approval, changed recipient or replay produces no send/submission |
| Improper output | Schema validation, safe rendering, parameterized storage and export escaping | Malicious HTML, links and spreadsheet formulas remain inert |
| Leakage | Per-user retrieval authorization, minimized context, secret isolation, redacted traces | Cross-user IDs, cache collisions and log requests reveal no foreign/private content |
| Supply chain | Reviewed/pinned dependencies, model artefacts and connectors; provenance/licence inventory; restricted network access | Unapproved package/tool changes are blocked; rollback preserves evidence |
| Fetch abuse/consumption | Block private-network destinations and unsafe redirects; size, time, token and retry limits | Redirect-to-localhost, huge files and retry loops fail safely within budget |

Filtering and prompts alone cannot establish isolation. Test the controls outside the model, including rendering and storage paths. Manual approval must show the exact content, destination and sensitive fields; it cannot compensate for hidden or misleading payloads.

## R-14: Select by task and operating conditions

**Reported provider limits, not audited guarantees:** OpenAI API data controls distinguish training use, abuse logs, application state and endpoint-specific exceptions; ZDR requires eligibility/approval [S07]. Anthropic's commercial ZDR arrangements cover eligible products with exceptions; its covered-model policy adds retention for specified organisations/models, with stated eligibility exceptions [S08]. Gemini Developer API terms distinguish unpaid from billing-enabled paid service: unpaid service warns against personal/confidential inputs; paid-service prompts/responses are not used for product improvement [S09]. None establishes universal zero retention. Consumer ChatGPT, Claude and Gemini app terms must not be inferred from these API policies.

**Recommendation:** shortlist OpenAI GPT, Anthropic Claude and Google Gemini API families for the same synthetic tasks, only after recording the exact available model, product, billing tier, region, features and data agreement. A local open-weight candidate is an alternative when its licence, hardware and measured quality are acceptable, not an assumed equivalent. Do not rank families from marketing or declare a best/latest model.

Before enabling Gemini Search grounding, separately review its display/storage/reuse restrictions and additional retention against the evidence ledger and cross-provider evaluation [S09]. Ordinary generation and grounded retrieval are not interchangeable contracts. Prefer separately licensed retrieval if the proposed use cannot satisfy the selected feature's terms; no such integration is approved here.

Before participant recruitment or a provider-backed pilot, the owner must approve an age scope and confirm provider compatibility. Propose adult-only initial research, without deciding eventual product eligibility. Youth access requires a separate provider/design/consent assessment; participant consent does not override service restrictions.

| Task | Deterministic/manual baseline | Model-assisted assessment |
| --- | --- | --- |
| Research | Curated primary sources and claim ledger | Correct citations, contradiction handling and fresh-source retrieval; verify opened pages |
| Design critique | Human heuristic/accessibility checklist | Actionable alternatives grounded in user goals; no invented participant evidence |
| Code assistance | Small manually reviewed change with fixed acceptance checks | Correctness, maintainability, correction time and permission adherence |
| Extraction | Rules, typed fields and user confirmation | Field accuracy, OCR uncertainty, source spans and abstention |
| Evaluation | Schema/assertion checks plus blinded human rubric | Calibrated secondary grading; never sole judge of its own output |

Measure the complete task: billed input/output/cache tokens, image and tool charges, retries, infrastructure and human correction time. Record dated pricing currency, actual billed cost where available, median/tail latency, timeouts, refusal, malformed output and truncation rates; report cost per accepted result including failures. No costs or performance were measured here. Keep task prompts and source fixtures constant, repeat variable tasks, and pin or record model snapshots, aliases, settings, provider policies and tool versions. Re-evaluate after material changes; do not silently fail over personal data to an unapproved provider.

Use a compact rubric per output: evidence correctness, uncertainty, usefulness and correction effort each scored 0–2 with written anchors; unsupported consequential claims, leakage and unauthorized actions are separate hard failures. Reuse the existing synthetic fixture and the parent's empirical queue, adding salary OCR/currency, permission denial, deletion/restore, provider outage and cross-user isolation cases. Report results by task, sector and input type; an aggregate score must not hide subgroup failures.

## Launch gates and handoff

**Proposed gates:** synthetic-only exploration until source rights and data routes are reviewed; a personal-data pilot only after approved notices/retention, isolation and deletion/restore checks; broader release only after evidence-grounding and accessibility review, measured latency/cost budgets, recovery rehearsal and named incident ownership. Require zero observed critical failures on the fixed adversarial suite, while acknowledging that a passing finite suite cannot prove safety. Human acceptance remains necessary.

Observe request IDs, version IDs, destination, authorization result, token/cost/latency totals and failure category, not raw resumes by default. Alert on unusual access, deletion backlog and spend; provide a feature-disable path and provider rollback. Practical next action: approve the data/rights contract and benchmark rubric, then run the parent's bounded empirical work. Remaining evidence: source-specific licences, full legal guidance, provider contracts/account eligibility, representative task outcomes and actual operating capacity.

## Primary source register

All sources accessed 2026-10-18. Dates below are publisher/version dates, not search-engine crawl dates. Each record distinguishes inspected scope and limits.

| ID | Source, date/version, inspected scope and limitation |
| --- | --- |
| S01 | [IETF RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html), September 2022. Opened introduction and security considerations; authoritative protocol, no copyright permission. |
| S02 | [LinkedIn prohibited software](https://www.linkedin.com/help/linkedin/answer/a1341387/prohibition-of-scraping-software?lang=en), relative “2 years ago”; exact update unavailable. Opened complete policy summary and quoted agreement restrictions; platform position only. |
| S03 | [PDPC obligations](https://www.pdpc.gov.sg/data-protection-obligations), published/updated 2023-04-03. Read all obligations through native browser after web-tool challenge; overview with exceptions, not full legislation. |
| S04 | [PDPC AI recommendation/decision guidance](https://www.pdpc.gov.sg/organisations/regulations-decisions/regulatory-guidance/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems), 2024-03-01. Browser-opened scope/consumer/intermediary summary; PDF requests failed. |
| S05 | [PDPC generative-AI guidance](https://www.pdpc.gov.sg/organisations/regulations-decisions/regulatory-guidance/advisory-guidelines-on-use-of-personal-data-in-generative-ai), 2026-07-20. Browser-opened lifecycle/individual-request summary; full PDF not inspected. |
| S06 | OWASP [2025 taxonomy](https://genai.owasp.org/llm-top-10/), [injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and [agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/): opened categories, scenarios and controls; 2025 edition released 2024-11-17. [2026 landing page](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) dated 2026-08-03 opened, download failed. Controls use inspected 2025 material, not an asserted latest-edition mapping. |
| S07 | [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data), living documentation, publication/update unspecified. Opened training, abuse retention, endpoint table and exceptions. Product/account-specific policy; OpenAI Docs skill guided verification. |
| S08 | Anthropic [commercial ZDR](https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to), “updated this week,” and [covered models](https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models), dated 2026-09-05, policy effective 2026-06-09. Opened scope, exceptions and retention; no account eligibility verified. |
| S09 | [Gemini API terms](https://ai.google.dev/gemini-api/terms), effective 2026-03-23. Opened use restrictions and unpaid/paid data clauses; also prohibits API clients directed to or likely accessed by under-18s. Youth access would require a separate provider/scope decision. |
| S10 | [IPOS computational data analysis](https://ask.gov.sg/ipos/questions/clglxzrrv00f8l4082ur0u5to), relative “3y ago,” exact date unavailable. Opened conditions on access, purposes and sharing; does not classify JobHub's particular uses. |

Verification: native web searches and source opens performed; three PDPC pages read through browser when text retrieval failed. Search snippets were not substituted for unread guidance. Only this assigned Markdown file was authored; no external writes, commits or application tests. Local link targets, source-ID coverage and whitespace were checked before handoff.
