# JobHub research findings

21 slides for reading before product analysis. Covers Rounds 00–02, with most detail on the completed expanded Round 02 evidence run. This is a research briefing, not an approved product scope or architecture.

## Read without Microsoft Office

Open `index.html` directly from File Explorer in Chrome or Edge. No installation, server, internet connection or account is needed for the slides themselves. Original external source links require internet access.

- Previous / Next or the arrow keys change slides. Home / End jump to the beginning or end.
- Press N or expand **Reading notes and sources** for context and references.
- **Read all slides** displays the entire briefing as a reading document.
- **Print / Save PDF** opens the browser print dialog. Select the browser's PDF destination if desired. This does not create a pre-verified PDF automatically.

Repository evidence links open local Markdown files. How the browser displays those files depends on its file handling.

For editing in a desktop presentation application, use `jobhub-research-findings-v2.pptx`. LibreOffice Impress is a free alternative. It was not installed or used to test this deck.

## Files and source of truth

| File | Purpose |
| --- | --- |
| `index.html` | Standalone reading presentation with source links and notes |
| `jobhub-research-findings-v2.pptx` | Current editable 21-slide export, including six native tables and speaker notes |
| `slides.json` | Master slide content used to generate both formats |
| `slides.md` | Generated Marp-compatible Markdown for future use, not a separately tested Marp export |
| `build.mjs` | Generator using the bundled Codex presentation runtime |
| `verify.mjs` | Static link/content checks and isolated navigation-logic tests |

Edit `slides.json` for coordinated changes. Edits made directly in PowerPoint/Impress or `slides.md` do not automatically update the other formats. The current HTML uses custom styling, not the Marp or reveal.js engines.

The source links point back to the repository's research records and selected original sources. Caption review does not imply listening to or visually analysing a video. Internal findings are sanitised process observations. The presentation does not include raw personal application materials.

## Rebuild

The current generator depends on Codex's bundled `@oai/artifact-tool`, presentation skill helpers and Python runtime. The content and HTML are portable, but this generator is not a standalone open-source slide engine. Override `JOBHUB_RUNTIME_ROOT` and `JOBHUB_PRESENTATION_SKILL` if the bundled locations change.

Run from the repository root in PowerShell, selecting a fresh version to avoid overwriting a validated export:

```powershell
$env:JOBHUB_DECK_REVISION = 'v3'
& 'C:/Users/prasa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' './02_research/07_presentations/00_research-findings/build.mjs'
& 'C:/Users/prasa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' './02_research/07_presentations/00_research-findings/verify.mjs'
```

Rebuilding regenerates HTML and Markdown, and creates a new PPTX. Update this README to identify the new current export after review. Rendered previews and validation receipts stay in the ignored parent `.build/00_research-findings/` directory. The earlier 20-slide export is preserved there as `superseded-v1.pptx`.

## Verification boundary

Slide previews were visually inspected. The 21-slide PPTX passed package, geometry, font-policy, native-table and re-import checks. An independent specialist reviewed the slide content against research records. HTML checks cover slide counts, local evidence links, offline dependencies and navigation logic, not actual browser layout rendering. Automated local-file browser preview was blocked by the app's URL policy, so no browser or print rendering test is claimed. Microsoft Office and LibreOffice compatibility were not tested in those applications.
