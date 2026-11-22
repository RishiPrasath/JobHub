"""One-click link-outs to review sites that bar automated access.

JobHub only builds a URL. It never fetches these sites, never copies a rating
or a review, and never checks whether the page exists, because their terms bar
scraping and bots (E16 runs 001-003). The user opens the link and reads the
reviews themselves.
"""
from urllib.parse import quote_plus

# url_status says how sure we are that the pattern lands on the right page:
#   documented  - the site publishes this URL format
#   unverified  - pattern from general knowledge; a person should click-check it
#                 (JobHub may not test it with a bot)
PROVIDERS = [
    {
        "id": "glassdoor",
        "label": "Glassdoor",
        "what": "Employee reviews, salaries and interview reports",
        "pattern": "https://www.glassdoor.sg/Search/results.htm?keyword={q}",
        "url_status": "unverified",
    },
    {
        "id": "indeed",
        "label": "Indeed",
        "what": "Company reviews and ratings",
        "pattern": "https://sg.indeed.com/companies/search?q={q}&l=Singapore",
        "url_status": "unverified",
    },
    {
        "id": "jobstreet",
        "label": "JobStreet",
        "what": "Company reviews",
        "pattern": "https://sg.jobstreet.com/companies/search?q={q}",
        "url_status": "unverified",
    },
    {
        "id": "google_maps",
        "label": "Google Maps",
        "what": "Reviews of the company's premises (often customers, not staff)",
        # Google Maps URLs, documented at developers.google.com/maps/documentation/urls
        "pattern": "https://www.google.com/maps/search/?api=1&query={q}",
        "url_status": "documented",
        "suffix": " Singapore",
    },
]


def build_linkouts(name: str, overrides: dict[str, str] | None = None) -> list[dict]:
    """Return one link per provider for this search name.

    overrides maps a provider id to a direct company-page URL that a person
    has checked (for example a Glassdoor overview page). It replaces the
    search URL for that provider.
    """
    overrides = overrides or {}
    links = []
    for p in PROVIDERS:
        if p["id"] in overrides:
            url, status = overrides[p["id"]], "checked_by_person"
        else:
            url = p["pattern"].format(q=quote_plus(name + p.get("suffix", "")))
            status = p["url_status"]
        links.append({
            "provider": p["id"],
            "label": f"Open {p['label']}",
            "what": p["what"],
            "url": url,
            "url_status": status,
            "fetched_by_jobhub": False,
        })
    return links
