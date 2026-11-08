# Formatting, ATS readability and accessibility

## What the evidence supports

Semantic structure matters across formats: real headings, logical reading order, meaningful links, selectable/resizable text, suitable contrast and text alternatives where needed. Government and W3C guidance supports readable typography, plain language, spacing, left alignment, non-colour cues and reflow.

ATS behaviour is implementation-specific. Greenhouse and Workday document failures or sensitivities involving images, graphics, tables, headers, footers, text boxes, columns, image-based styles and word order. These are product-specific operational facts, not a universal rule that every ATS rejects every column or PDF.

## Trade-off matrix

| Area | Evidence-backed tension | Conservative interpretation |
|---|---|---|
| Headings | Visual styling is not the same as semantic headings | Use real heading styles and test navigation/reading order |
| Columns | Can scan well but may harm reflow or parser order | Single-column is a compatibility option, not a universal law |
| Tables | Compact comparison can create parser/screen-reader complexity | Use only when genuinely tabular; keep simple and labelled |
| Graphics/icons | Useful for visual roles but image text is fragile | Keep consequential facts in real text; graphics optional |
| Colour | Helps hierarchy but cannot carry meaning alone | Pair colour with labels, weight, spacing or patterns |
| PDF/DOCX | PDF preserves appearance; DOCX preserves editability; both can fail structurally | Validate the actual export separately for each format |
| Brevity | Dense pages save space but increase cognitive and mobile load | Relevance and comprehension matter more than a universal page limit |
| Mobile/interruption | Autosave and reflow help, but invisible state weakens control | Show save state, version history, recovery and undo |
| Accessibility/ATS | Both need selectable text and logical order, but priorities can diverge by role/channel | Offer scoped checks and warnings; never promise “ATS-safe” universally |

## Responsible-AI control matrix

| Risk | Minimum control |
|---|---|
| Fabricated claim | Generate only from confirmed evidence; flag unsupported claims before export |
| Keyword overfitting | Show requirement and supporting candidate evidence beside each suggestion |
| Missing-field inference | Preserve `unknown`, `not stated`, `conflicting` and `inferred` as distinct states |
| Proxy discrimination | Avoid sensitive-trait inference; test equivalent evidence across gaps, names, styles and sectors |
| Privacy exposure | Minimise fields, separate contact data from analysis, disclose processing and deletion |
| Provenance loss | Attach source spans/document locations and capture dates to consequential suggestions |
| Automation bias | Require review-before-accept with edit, reject, keep-original and uncertainty actions |
| Homogenisation | Preserve original wording, offer alternatives and measure correction effort/voice loss |
| Accessibility regression | Test structure, extraction and assistive-technology behaviour of generated DOCX/PDF |
| Irreversible action | Separate draft, reviewed, approved and submitted states; require explicit approval |
| Prompt injection | Treat postings, resumes and pages as untrusted data; isolate extraction from action tools |
| Over-confident fit advice | Explain requirement-by-requirement evidence and gaps; avoid hiring-probability claims |

## Human-control sequence

1. Preserve the original resume and captured posting.
2. Extract claims with source locations.
3. Show AI suggestions as proposed changes.
4. Let the candidate approve, reject, edit, keep original or mark uncertain.
5. Keep a version and undo path.
6. Require explicit export approval.
7. Keep any future external submission as a separate, explicit permission step.

## Open tests

The evidence supports testing whether users can identify each change and its support, correct a fabricated/overstrong claim, understand unknown versus inferred, resume on another device, navigate by headings with assistive technology, preserve text order in exports and understand the exact payload before sharing.
