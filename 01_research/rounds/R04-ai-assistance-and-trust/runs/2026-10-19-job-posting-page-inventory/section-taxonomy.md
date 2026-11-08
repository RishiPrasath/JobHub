# Cross-board section and field taxonomy

This is a proposed recording vocabulary derived from the sample and specialist review. It is not a claim that all fields occur on all pages. Preserve the original label alongside any normalized field.

## Page types

1. `search_results` — query, filters, sort, result cards and pagination.
2. `job_detail` — one vacancy or requisition with role content and application route.
3. `employer_or_agency_profile` — organization context and related vacancies.
4. `career_landing` — employer, sector or public-service proposition and navigation.
5. `application_page` — application/interstitial route and required information.
6. `support_lifecycle` — posting, reposting, expiry, moderation or account guidance.
7. `related_jobs` — recommendations or same-employer links.
8. `error_or_blocked` — page exists but substantive content is unavailable.

## Canonical field groups

### A. Identity and provenance

`job_title`, `reference_id`, `employer`, `agency_or_recruiter`, `client`, `department_or_team`, `occupation`, `seniority`, `source_relationship`, `listing_status`.

Keep employer, agency, client and worksite separate. A board displaying a field does not prove who authored it.

### B. Location and work arrangement

`country_or_region`, `city`, `worksite`, `address`, `multiple_locations`, `remote`, `hybrid`, `on_site`, `travel`, `deployment`, `relocation`, `accommodation`, `commute_or_transport`, `location_meaning`.

### C. Employment arrangement

`employment_type`, `contract_duration`, `permanent`, `full_time`, `part_time`, `temporary`, `casual_or_on_call`, `freelance_or_gig`, `internship`, `live_in`, `direct_or_agency`, `probation`, `start_date`.

### D. Time and working conditions

`hours`, `days`, `shifts`, `night_work`, `weekend_work`, `overtime`, `on_call`, `rotation`, `seasonal_work`, `posted_at`, `updated_at`, `expiry_at`, `closing_at`, `response_expectation`.

### E. Compensation

`base_pay`, `hourly_pay`, `pay_range`, `currency`, `pay_frequency`, `allowance`, `commission`, `bonus`, `overtime_pay`, `tips`, `benefits`, `conditional_pay`, `up_to_language`, `guarantee_status`.

Do not convert “monthly income including allowances and overtime” into base salary. Preserve whether a figure is guaranteed, conditional, estimated, or only a platform teaser.

### F. Role content

`summary`, `purpose`, `responsibilities`, `daily_tasks`, `deliverables`, `performance_expectations`, `customer_or_public_contact`, `supervision`, `team`, `tools`, `equipment`, `physical_demands`, `environment`, `safety`, `travel`.

### G. Requirements and eligibility

`education`, `qualification`, `licence`, `certification`, `experience`, `skills`, `tools`, `language`, `work_authorisation`, `residency`, `physical_or_medical`, `background_check`, `driver_requirement`, `security_clearance`, `mandatory_or_preferred`, `trainability`.

### H. Process and application

`application_method`, `application_recipient`, `external_destination`, `documents`, `screening_questions`, `interview`, `technical_or_practical_test`, `portfolio_or_audition`, `trial`, `references`, `background_screening`, `process_timeline`, `follow_up`, `response_signal`.

### I. Employer, intermediary and support context

`employer_description`, `industry`, `organization_scale`, `public_or_private`, `agency_context`, `client_disclosure`, `company_registration`, `benefits`, `training`, `progression`, `mentoring`, `flexibility`, `accessibility`, `language_support`, `transport_or_housing`, `employee_support`.

### J. Platform context

`match_score`, `recommended`, `urgent`, `response_badge`, `translation`, `category`, `salary_estimate`, `similar_jobs`, `employer_rating`, `application_status`, `verified`, `promoted`, `actively_reviewing`, `applicant_count`, `network_signal`, `save`, `share`, `report`, `job_alert`.

Platform context is useful, but it must not be merged into employer claims. “Verified,” “actively reviewing,” a match score or an applicant count describes a platform signal unless the source explicitly says otherwise.

## Field-level record

```text
field_id:
raw_label:
raw_value:
normalized_value:
content_state: present | partial | conditional | contradictory | not_present | not_visible | blocked | not_applicable | unknown
interpretation_state: clear | vague | platform_generated | unverified | stale_possible | not_comparable
ownership: employer | agency | government | platform | user_generated | mixed | unknown
source_location: heading | header | card | table | footer | support_page | other
evidence_reference:
researcher_note:
```

## Recommended distinction model

`visible page fact` → `field classification` → `interpretation` → `unresolved question`

Do not skip the middle steps. For example, “normally responds in 24 hours” is a visible platform/employer signal; it is not the same as a guaranteed response time. “Not visible” is an access observation; it is not evidence that the employer omitted the information.

## Search-card record

For a search page record: `query`, `location`, `filters`, `sort`, `result_count`, `page_number`, `card_title`, `card_employer`, `card_location`, `card_pay`, `card_arrangement`, `card_posted_or_updated`, `card_snippet`, `badges`, `application_signal`, `destination`, `missing_card_fields`.

Compare this record with the corresponding detail page before treating card content as a complete vacancy record.
