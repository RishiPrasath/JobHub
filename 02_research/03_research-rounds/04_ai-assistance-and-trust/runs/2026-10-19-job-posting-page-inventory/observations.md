# Observations

These are evidence-bounded observations from the 20 inspected page observations. They are not prevalence estimates.

## Cross-page observations

1. Job-board information is an ecosystem, not one page. Search results, detail pages, company/public-service pages, application routes, related jobs and support/lifecycle pages each expose different parts of the vacancy context.
2. The strongest recurring detail-page groups in this sample are identity, location/arrangement, compensation where disclosed, role content, requirements, application actions and platform controls.
3. Search cards tend to compress content into title, employer, location, arrangement, pay/date/snippet and badges. Detail pages add the duties, qualifications, process and conditions needed for interpretation.
4. Labels vary materially: `What will your role be`, `Key responsibilities`, `Roles & Responsibilities`, `About the role`, `What you will be doing` and `Job details` overlap but are not identical.
5. Structured fields and free text coexist. Structured fields make comparison easier but can hide qualifiers; free text preserves nuance but makes extraction and comparison harder.
6. Platform-generated signals are prominent on several boards: match scores, verified/promoted badges, response indicators, applicant counts, relevance, network signals, translation and recommendations. These must remain distinct from employer-authored evidence.
7. Compensation requires decomposition. Pages may show a range, hourly rate, “monthly income” including overtime/allowances, benefits, commission, a salary teaser or conditional language. A single salary field would lose important meaning.
8. Time fields are not interchangeable. Posted, updated, expiring, closing, response expectation and underlying hiring status are different concepts.
9. Identity is relational. Employer, recruiter/agency, client, government agency, source platform, application recipient and physical worksite may be different entities.
10. Public-service recruitment exposes more process and classification structure in some pages, including agency, closing date, contract type and response expectations. This is a source-pattern observation, not a universal government rule.
11. Frontline and trade pages may make shifts, days, licences, exact worksites, overtime and allowances more prominent than office-oriented pages.
12. A page can be visibly present yet informationally partial. Indeed’s compact page and LinkedIn’s dynamic detail view show why missingness and access state must be recorded separately.

## Specific anomalies and useful caution cases

- Jobstreet’s visible job title/body and URL/title metadata did not align cleanly. Record the mismatch; do not silently choose one.
- An Indeed detail page exposed a `Key Responsibilities` section while requirements and benefits were not visible in the inspected content. This is a partial page observation, not evidence of omission.
- LinkedIn’s header metadata was visible while the description body did not render in the inspected view. Search cards and header signals cannot replace detail content.
- FastJobs support material states that expired listings older than 60 days can become retired/inaccessible from an employer dashboard. That documents platform lifecycle behaviour; it does not prove a posting was fake or stale.
- MyCareersFuture displayed machine-translation controls and a skills-match panel. These are platform-generated context and must not be treated as employer claims.
- Chrome fallback checks added useful access distinctions: GrabJobs presented a Cloudflare security-verification page; PERSOL presented an explicit maintenance page; Tech in Asia exposed a readable startup-jobs landing page but its selected detail remained a dynamic shell; and Jobs Lah exposed Singapore landing/search shells without visible result cards in the inspected state.
- Jobs Lah’s Singapore landing page exposes job search, company exploration, job-type/location routes, resume templates, a salary calculator, an interview guide, jobseeker FAQs and employer posting links. These are platform ecosystem sections, not evidence that a specific vacancy was available.
- GovTech’s direct career page is readable and routes applicants to Careers@Gov, demonstrating that employer career pages can be contextual shells around a separate recruitment portal.

## What the sample does not establish

- the prevalence of any section or field;
- that a vacancy is genuine, active, ghost, fake or closed;
- that a board’s badges accurately describe employer behaviour;
- that all pages from a platform share the same template;
- that a missing visible field does not exist behind interaction or an external application route;
- that a salary range is comparable across roles, employers or industries;
- that page structure alone can establish good fit or job quality.
