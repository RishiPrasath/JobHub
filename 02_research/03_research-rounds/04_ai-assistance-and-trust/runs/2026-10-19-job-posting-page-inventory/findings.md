# Findings and implications

## Finding 1 — Use a layered posting record

The useful common denominator is not a fixed list of headings. It is a layered record:

1. page identity and access state;
2. source ownership and provenance;
3. raw visible sections and labels;
4. normalized fields where mapping is justified;
5. missingness, conditions, contradictions and uncertainty;
6. relationships to search cards, employer pages and application routes.

This allows JobHub to compare postings without pretending that different boards use identical content structures.

## Finding 2 — Preserve labels and raw wording

The same concept appears under different labels, while similarly named sections can contain different scopes. Store the original heading/value and add a normalized interpretation only when confidence is sufficient. A normalized field without the raw label would make later review difficult and could erase important context.

## Finding 3 — Treat platform signals as a separate evidence layer

Match scores, verified/promoted badges, applicant counts, response indicators, network signals, translations, recommendations and salary teasers are useful for understanding a user’s experience. They are not equivalent to employer-authored facts. A future assistant should show their source and avoid using them as proof of fit, quality or hiring intent.

## Finding 4 — Make uncertainty first-class

The observed pages justify separate states for present, partial/vague, conditional, contradictory, not present, not visible, blocked, not applicable and unknown. This is particularly important for pay, status, dates, worksite, application route and client identity.

## Finding 5 — Compare cards and details

Search pages expose useful compressed signals but do not contain enough context for role fit, truthful resume tailoring or vacancy-credibility review. The research model should preserve the search-card observation and, when possible, link it to the detail-page observation. Differences should be reported rather than overwritten.

## Finding 6 — Build a page ecosystem model

The next evidence model should allow a vacancy family to connect:

`search result` → `detail page` → `employer/agency context` → `application destination` → `support/lifecycle evidence`

This is more robust than treating every URL as an independent job or every page as a self-contained record.

## Finding 7 — Industry and occupation are separate dimensions

The sample already shows that logistics/trade, public service, office/professional and frontline roles foreground different fields. The difference may come from occupation, seniority, work arrangement or regulation rather than industry alone. Future round records should keep these dimensions separate.

## Recommended next actions

1. Add a source-comparison matrix for the Round 04 evidence package.
2. Expand the balanced sample using the sampling specialist’s proposed employer-hosted, ATS, public-service, event, PDF, talent-pool and unavailable-page strata.
3. Test at least one card/detail pair per board and record discrepancies.
4. Add field-level ownership and state coding to the research evidence template.
5. Validate the taxonomy with two independent reviewers before using “common” or “frequent” language.
6. Keep product decisions separate: this run supports a data and research vocabulary, not a parser specification or chosen platform architecture.
