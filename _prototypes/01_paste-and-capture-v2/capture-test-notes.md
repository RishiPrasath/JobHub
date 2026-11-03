# V2 Capture Feasibility Notes

Date: 2026-10-28

These are bounded prototype checks, not a claim that every job-board page can be captured reliably.

## Test 1 — public detail page

URL:

`https://www.mycareersfuture.gov.sg/job/admin/administrative-assistant-jl-apba-tg-human-resource-cf7aa95eae2db786bc0e8c74ef6d440b?event=Search&source=MCF`

Observed with a fresh Playwright browser context:

```json
{
  "http_status": 200,
  "page_title_present": true,
  "visible_text_characters": 6263,
  "roles_and_responsibilities_present": true,
  "classification": "usable_detail_page"
}
```

The page exposed a title, employer, location, employment type, salary range, closing date and role responsibilities. This is a viable input for the capture runner, subject to change over time.

## Test 2 — search-results page

URL:

`https://www.mycareersfuture.gov.sg/search?uen=200503644G`

Observed:

```json
{
  "http_status": 200,
  "page_title": "Search results | MyCareersFuture Singapore",
  "visible_text_characters": 7600,
  "roles_and_responsibilities_present": false,
  "classification": "search_result_only"
}
```

The page contained job cards and search controls, but it should not be treated as one complete job posting.

## Test 3 — repeated navigation variability

When the detail URL was opened after the search-results page in the same automated context, the response still returned HTTP 200 but exposed only a short page without the role body. This demonstrates that HTTP status alone is insufficient:

```text
HTTP 200 does not necessarily mean a complete posting was captured.
```

The capture runner should therefore classify the visible content, preserve the raw capture, and offer pasted text whenever the page is partial, blocked, redirected or otherwise incomplete.

## Implication for V2

The user-facing language should stay simple:

```text
We captured the main job details.
```

or:

```text
We could not read the full posting. Paste the job text instead.
```

The user should not need to understand Playwright, HTTP status codes, JSON-LD or anti-bot behaviour.
