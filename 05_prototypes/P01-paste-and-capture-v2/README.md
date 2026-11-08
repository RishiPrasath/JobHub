# JobHub UX Prototype V2 — Paste and Capture

This prototype tests a simpler user-facing workflow:

```text
Paste a job posting or provide a link
  -> extract the useful details
  -> see what the role involves
  -> compare it with your skills
  -> see what is missing or worth checking
  -> decide what to do next
```

## What changed from V1

V1 tested evidence review and human correction. That was useful for validating provenance, but it exposed too much internal workflow in the primary interface.

V2 is intentionally more direct:

- no section navigation;
- no claim-by-claim approval as the default experience;
- no completeness score;
- no fit or scam verdict;
- no application submission or employer messaging;
- source evidence remains available, but it is not the first thing the user must manage.

## Main user questions

The report is organised around the questions a job seeker actually has:

1. What is this role?
2. What would I be doing?
3. What do they expect from me?
4. What do I get and under what conditions?
5. Does it appear relevant to my skills?
6. What important information is missing?
7. What should I check before proceeding?

## Open the prototype

Open `index.html` directly, or serve this folder locally:

```powershell
python -m http.server 8766
```

The browser prototype uses a local deterministic parser so the interaction can be tested without an API key. It includes an example posting and accepts pasted text.

## Link capture and LLM experiment

`capture-and-extract.mjs` is a separate optional runner. It uses Playwright to capture visible page text and JSON-LD metadata, then optionally sends the captured text to an OpenAI-compatible endpoint such as Groq using the OpenAI SDK.

Install dependencies:

```powershell
npm install
```

Capture only:

```powershell
node capture-and-extract.mjs --url "https://example.com/job" --out "capture.json"
```

Capture and extract with the local `.env` configuration:

```powershell
node capture-and-extract.mjs --url "https://example.com/job" --out "capture.json" --extract
```

The runner must treat link capture as best-effort. A blocked, expired, logged-in, JavaScript-only or anti-bot page should fall back to pasted text rather than being presented as successfully captured.

## Prototype boundary

The report describes the posting. It does not determine whether a role is legitimate, guarantee fit, predict hiring, or make a decision for the user. “Things to check” are source-based signals and missing information, not a fraud verdict.
