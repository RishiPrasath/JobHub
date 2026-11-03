# JobHub UX Prototype V3 — Persona-aware job review

V3 tests a more realistic user flow:

```text
Choose an optional review lens
  -> paste a job link or the posting text
  -> try to read the link (or use the pasted text)
  -> see a short, readable report
  -> inspect missing information and concerns
  -> choose what to do next
```

## What V3 is testing

- The review is useful without a personal profile or account.
- A user can select a work context without being classified by it.
- A link and a pasted posting are treated as two input paths to the same report.
- A failed or partial capture has a clear fallback instead of a technical error.
- The first screen answers: what is the role, what would I do, what do they want, what do I get, and what should I verify?
- Industry-specific questions are helpful without producing a universal fit or fraud verdict.

## Run the static prototype

From this folder:

```powershell
python -m http.server 8767
```

Open <http://127.0.0.1:8767/>.

The static preview includes a small link inventory gathered through Chrome. The administrative assistant listing has an observed public-page capture. Other prepared links are deliberately marked as search-result-only or pasted-fallback so the prototype does not pretend that a URL alone proves that the page was read.

## Optional link-capture runner

`server/capture-server.mjs` serves this folder and exposes `POST /api/capture`.
It uses Playwright when the dependency is installed, with a bounded timeout and no login, CAPTCHA, or anti-bot bypass. If the runner cannot read a page, the UI keeps the link and asks for pasted text.

```powershell
npm install
npx playwright install chromium
npm start
```

The browser UI works without the runner. This preserves the guaranteed path: paste the text and review it.

## Persona and source boundaries

The personas are review lenses, not user identities. They change which questions are emphasised; they do not decide whether a person is qualified, suitable, safe, or likely to be hired. The source status is always explicit:

- `Captured from public page`
- `Using pasted text`
- `Partial capture`
- `Search result only`
- `Could not read link`

Prepared links are examples for the prototype and are not recommendations or employer endorsements.

## V3 acceptance checks

- Starting the page does not load dummy job content.
- `No persona` can review a posting.
- At least six work contexts can be selected.
- A pasted posting produces a report without an API key.
- A prepared public link produces either a bounded report or an honest fallback state.
- The same posting remains factually stable when the persona changes.
- Fit language describes evidence and gaps rather than giving a percentage or verdict.
- The report is readable on a phone-sized viewport.
- No external application, message, or save action is performed by the prototype.
