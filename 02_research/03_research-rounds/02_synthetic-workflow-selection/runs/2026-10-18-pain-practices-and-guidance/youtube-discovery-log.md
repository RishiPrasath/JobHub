# Round 02 YouTube discovery and capture log

Execution date: 2026-10-18, Asia/Singapore (UTC+08:00). Researcher roles: Job-Seeker Practices Researcher and Research Query Strategist. Read the round's `query-plan-draft.md` and run `brief.md` before discovery. Interpretation is in [video-research.md](video-research.md).

## Scope, accounting, and provenance correction

Reviewed all five supplied captions before searching for additions. Additions target Q2 truthful resumes, Q3 interview preparation, Q5 compensation/negotiation, and Q8 practical AI use. Search snippets and titles are discovery aids only. No prevalence or effectiveness claim was accepted from them.

**Candidate accounting: six checked candidate URLs, including one inaccessible URL; five canonical videos, five SRT captures.** The erroneous lower-case video ID counts conservatively as a failed candidate rather than being erased from the cap. No additional candidate was checked after these six. Other videos incidentally returned by web search were not shortlisted, metadata-probed, or captured. The cap is eight additional candidates, not eight required selections.

**Coordinator correction:** built-in browser transcript export had been attempted for only the first four supplied videos in the supplied index's order (`iVeoEF3bzlY`, `0KXDCuxi3jk`, `x2sgf8zlNao`, `fCd4wZQaWqo`). The fifth, `IF3McdG_dSY`, was checked with yt-dlp only. The supplied directory README's statement that browser export failed for all five is overbroad; this report records the correction without editing that shared file. This specialist did not repeat browser export or listen to any source.

No audio listening, browser playback, or visual screen verification was performed. High-impact wording, negations, numeric examples, policy/legal assertions, and claimed outcomes are unverified against audio. Manual caption availability does not imply human accuracy. No paid APIs, plugins, remote writes, audio/video downloads, cookies, authenticated access, or bypasses were used.

## Exact native web queries

Venue: native web search (`web.run`, not YouTube search, yt-dlp search, a plugin, or a paid API). `site:` syntax is a venue-specific adapter. Execution order is preserved below. Per-query wall-clock instants were not separately persisted; searches occurred between the observed local checkpoints 21:42:25+08:00 and 21:44:08+08:00. Do not read these checkpoints as exact timestamps for each query.

| Order | Exact executed query | Intended family / evidence | Retrieval outcome and decision |
|---|---|---|---|
| QV01 | `site:youtube.com/watch interview preparation career service STAR practice job interview` | Q3; attributable career-service practice | First batch was noisy; did not produce a retained university candidate. |
| QV02 | `site:youtube.com/watch truthful resume tailoring AI do not invent experience` | Q2; truthful tailoring and checking | Same batch dominated by irrelevant YouTube-domain pages; reformulated. |
| QV03 | `site:youtube.com/watch Singapore salary negotiation market value job offer` | Q5; Singapore practitioner guidance | No retained Singapore video in this batch. |
| QV04 | `site:youtube.com/watch how I use ChatGPT job search resume interview experience` | Q8; actual sequence rather than promotional promise | Batch returned an unshortlisted interview tutorial plus substantial irrelevant pages. No practice claim inferred. |
| QV05 | `YouTube university careers interview preparation STAR practice` | Q3; university preparation/manual alternative | Found Cedarville webinar through its own university page; UNI page was a discovery dead end for a video. |
| QV06 | `YouTube resume tailoring ChatGPT honest experience Jeff Su` | Q2; worked example with authenticity checks | Found Jeff Su's 2023 tutorial directly and a 2026 title via an index; both titles checked with yt-dlp before use. |
| QV07 | `YouTube CNA Work It salary negotiation` | Q5; Singapore context | Found CNA's salary podcast page, but no direct YouTube link. Retained as an uncaptured gap lead only. |
| QV08 | `YouTube I used ChatGPT job search experience resume interview` | Q8; firsthand candidate | Found Express Tech title; caption inspection later downgraded its personal-outcome framing to tutorial/self-report. Reddit/media hits not adopted in this video assignment. |
| QV09 | `site:youtube.com "CNA" "salary" "negotiate"` | Q5; precision retry | Entire three-query batch returned empty results. |
| QV10 | `site:youtube.com "interview preparation" "university" "STAR"` | Q3; precision retry | Same empty batch; followed the university page already found. |
| QV11 | `site:youtube.com resume "never lie" "AI"` | Q2; disconfirm fabrication | Same empty batch; no conclusion that such material does not exist. |
| QV12 | `"How to ask your boss for more money" youtube` | Q5; focused gap follow-up | Returned Practical Wisdom and a much older Citytv result, alongside the CNA page. Selected Practical Wisdom for concrete comparison steps, with explicit low confidence. |
| QV13 | `youtube salary negotiation know your worth market value Linda Raynier` | Q5; alternative terminology after noise review | Returned salary-research library and Khan Academy leads, coach indexes/articles; did not yield a stronger checked YouTube candidate within this pass. |

Method note: initial portfolios were reviewed after three searches per main family produced noise or gaps. QV12–QV13 were two deliberate salary-gap follow-ups after that review, not an unreported expansion of the initial portfolio. Counts/rankings and retrieved repetition are not evidence. Search batches can mix results; the outcome column identifies useful batch leads, not a guaranteed per-query ranking.

Opened discovery pages (2026-10-18, within the interval above):

- [CNA salary podcast](https://www.channelnewsasia.com/podcasts/negotiating-salary-strategies-work-it-podcast-4040371): identifies Ken Tan of Persolkelly; relevant pay/benefits and last-drawn-salary topics. No video ID obtained. Its legal/policy statements were not accepted or independently validated here.
- [Cedarville webinar source page](https://www.cedarville.edu/media/videos/cu-grad-webinars-interview-preparation-with-jeff-reep-ay_wtote5gc): direct YouTube link ultimately resolved to the case-sensitive ID `ay_wtOte5Gc`. Native link opening returned an internal error. A public-page HTML read recovered the exact link; no player/media was downloaded by that read.
- [University of Northern Iowa interviewing](https://careerservices.uni.edu/students/interviewing): source offered mock-interview and document resources, not a retained direct video.
- [Khan Academy salary-negotiation lead](https://www.khanacademy.org/college-careers-more/career-content/career-profiles-start-a-business/freelance-journalist-and-podcaster/v/misha-freelance-journalist-and-podcaster-salary-negotiation): text extraction returned zero lines; no YouTube URL was checked and no content finding accepted.
- [SDSU salary research/negotiation library page](https://libguides.sdsu.edu/c.php?g=1049249&p=7883449): open failed with HTTP 429. No retry, bypass, video enumeration, or capture; page remains a retrieval gap.

These are discovery leads, not additional caption-reviewed videos. Third-party indexes were not used as substitutes for the actual captions. Search-hit claims about statistics/outcomes were not promoted to evidence.

## Candidate ledger and actual checks

All successful records below came from live `py -m yt_dlp --skip-download --no-playlist --dump-json --no-warnings URL` checks, inspecting `id`, `title`, `channel`, `upload_date`, `duration`, and English keys under `subtitles` and `automatic_captions`. Existing installed version: **2026.08.19**, observed 2026-10-18T21:42:25+08:00. No package was installed or upgraded. Checks ran between that checkpoint and capture start at 21:44:37+08:00; exact per-check completion times were not separately persisted.

| Candidate | URL / result | Creator; upload date; duration | English tracks observed | Selection / capture decision |
|---|---|---|---|---|
| C01 / V06 | https://www.youtube.com/watch?v=pmnY5V16GSE | Jeff Su; 2023-04-25; 619 sec | Manual `en`; automatic `en`, `en-orig` | Capture `en`; concrete invented-title detection, comparison, and interview-answer workflow beyond red flags. |
| C02 / V09 | https://www.youtube.com/watch?v=HHGQ_QeHjF0 | Express Tech (metadata channel has trailing whitespace); 2025-04-24; 166 sec | No manual English; automatic `en-orig`, `en` | Capture `en-orig`; remote-job search sequence and checking omissions. Downgraded after analysis: no demonstrated dream-job success. |
| C03 / V07 | https://www.youtube.com/watch?v=N1Fm4JYae1I | Jeff Su; 2026-09-15; 789 sec | No manual English; automatic `en-orig`, `en` | Capture `en-orig`; adds fact-first drafting, verifiable metrics, and labelled project evidence. Same creator as C01; statistics quarantined. |
| C04 / failed | https://www.youtube.com/watch?v=ay_wtote5gc | Unavailable; creator/date/duration and captions not returned | Unknown, not established absent | Exact failure: `ERROR: [youtube] ay_wtote5gc: This video is unavailable`. Erroneous ID inferred from lower-case page slug; counts toward cap. |
| C05 / V08 | https://www.youtube.com/watch?v=ay_wtOte5Gc | Cedarville University; 2026-04-13; 3459 sec | Manual `en-US`; automatic `en-US`, `en-orig`, `en` | Correct link from publisher HTML. Capture `en-US`; long interview toolbox/notes/mock-practice material provides a manual alternative. Cultural and normative limits retained. |
| C06 / V10 | https://www.youtube.com/watch?v=Risf_QQGX2o | Practical Wisdom - Interesting Ideas; 2020-08-17; 634 sec | Manual `en`; automatic `en`, `en-orig` | Capture `en`; compensation comparability and non-salary alternatives. Weak/old general advice; not established expert or salary data. |

Observed titles (metadata): C01 **Land a Job using ChatGPT: The Definitive Guide!**; C02 **I Used ChatGPT to Apply For My Dream Job. Here's How**; C03 **Write a Killer Résumé in the AI Era: 5 New Rules!**; C05 **CU Grad Webinars — Interview Preparation With Jeff Reep**; C06 **Salary Negotiation | How To Ask Your Boss For More Money**. Failed C04 has no independently returned metadata. C04/C05 are the same intended source, conservatively counted as two checked URLs.

All five additions complement rather than extend the supplied red-flag set. The salary capture concerns a current-job raise and international examples; Singapore offer negotiation remains a gap. Most clips are instruction rather than independently observed seeker practice. No independent success rates are established.

## Reproduction and capture events

Caption root, relative to repository: `02_research/05_evidence/external/youtube/2026-10-18-round-02-additional/`.

For each successful candidate, run with the selected language in the ledger:

```powershell
py -m yt_dlp --skip-download --write-subs --write-auto-subs --sub-langs LANGUAGE --sub-format srt --write-info-json --no-playlist --no-warnings -P '02_research/05_evidence/external/youtube/2026-10-18-round-02-additional' -o '%(id)s.%(ext)s' 'https://www.youtube.com/watch?v=VIDEO_ID'
```

The exact executed pairs were `(pmnY5V16GSE, en)`, `(N1Fm4JYae1I, en-orig)`, `(ay_wtOte5Gc, en-US)`, `(HHGQ_QeHjF0, en-orig)`, `(Risf_QQGX2o, en)`, in that order. Both subtitle switches allow the named manual track when available and automatic fallback where selected. Each capture reported writing the selected SRT and metadata. No format media file was saved: yt-dlp printed format selection despite `--skip-download`, which is not evidence of an audio/video transfer.

For future reproduction, omit `--write-info-json` unless necessary; capture the minimal ledger fields instead of retaining signed-URL-heavy player metadata.

| Capture start observed (+08:00) | Relative caption file under root | Bytes | Cues; first start–last end | Provenance |
|---|---|---:|---|---|
| 2026-10-18T21:44:37.6154041 | `pmnY5V16GSE.en.srt` | 22,773 | 314; 00:00:00.000–00:10:19.040 | Listed manual English track `en`; full text read. |
| 2026-10-18T21:44:40.0559455 | `N1Fm4JYae1I.en-orig.srt` | 25,963 | 359; 00:00:00.000–00:13:09.560 | Automatic original English; full text read. |
| 2026-10-18T21:44:42.4443849 | `ay_wtOte5Gc.en-US.srt` | 88,393 | 653; 00:00:00.000–00:57:38.520 | Listed manual English (US) track; full text read. |
| 2026-10-18T21:44:44.9231339 | `HHGQ_QeHjF0.en-orig.srt` | 5,274 | 73; 00:00:00.080–00:02:41.480 | Automatic original English; full text read. |
| 2026-10-18T21:44:47.0140799 | `Risf_QQGX2o.en.srt` | 17,956 | 189; 00:00:00.170–00:10:32.970 | Listed manual English track; full text read. |

All five successful completions were observed before the 21:45:48.9393388+08:00 checkpoint. Capture times are local script timestamps, not inferred publication dates. Cues need not cover introductions, trailing silence, or every instant of the declared video duration.

## File integrity and supplied-set coverage

Hashes checked on local SRT bytes, SHA-256. Original metadata below comes from the supplied index, not a fresh metadata download. Source analysis links and publication dates are in `video-research.md`.

| File | Cues | Caption coverage | SHA-256 |
|---|---:|---|---|
| Supplied `iVeoEF3bzlY.en-orig.srt` | 796 | 00:00:03.200–00:27:00.119 | `2641213F00349ED225C4A470901F68088CC22DDBD311894F63CD261E2C375F82` |
| Supplied `0KXDCuxi3jk.en-orig.srt` | 244 | 00:00:00.160–00:08:34.000 | `9668B4211DE80834A500857AD4BC3F9D8DC1A0996F0266B66D8A5911A6B64F52` |
| Supplied `x2sgf8zlNao.en-orig.srt` | 315 | 00:00:00.000–00:10:19.929 | `428C9912F6207A6943431B75B047CBDE3251DCB9CC96ABC1790F2CE66DD8F0FF` |
| Supplied `fCd4wZQaWqo.en-orig.srt` | 298 | 00:00:00.000–00:09:20.240 | `45DCF7EDAD859852A4884C9C1967E2B607E56C38494D97973BE6DE65BCB08A82` |
| Supplied `IF3McdG_dSY.en-orig.srt` | 346 | 00:00:00.000–00:13:24.320 | `10668C13DD48F1615EA7FE0EBF99CB32E2EA860CE9A111469F738C0B6BDFC02C` |
| Additional `pmnY5V16GSE.en.srt` | 314 | See capture table | `02A11763248B793979E3E04755776DF7193BD848015C5B97D1DB07BB3F943785` |
| Additional `N1Fm4JYae1I.en-orig.srt` | 359 | See capture table | `6DF55C94DFFCA768C90CA4DCEC34A2B9697E7BA0A9311873F0D820DE7B8B932B` |
| Additional `ay_wtOte5Gc.en-US.srt` | 653 | See capture table | `0151C8148B8B22B34829497EA1228455D88A2736B369793541D64F255E122F2F` |
| Additional `HHGQ_QeHjF0.en-orig.srt` | 73 | See capture table | `212C3B2FFFF801A87A863A07073710146A4B90B92D46891948D122579AE1CBE3` |
| Additional `Risf_QQGX2o.en.srt` | 189 | See capture table | `0382B1BC6B0806F0B22B761C6637C375CCA3AB4AC82FAC8010FEB7213436D299` |

Original root: `02_research/05_evidence/external/youtube/2026-10-18-job-posting-red-flags/`. All five original files are automatic `en-orig` captures. Total: 1,999 supplied cues + 1,588 additional cues = 3,587. Parsing/read completion does not establish audio accuracy or representativeness.

## Metadata minimisation and verification

At the coordinator's explicit request, preserve all SRTs and minimal title/channel/date/duration/caption provenance above; remove only these newly generated metadata files after recording it:

```text
C:\Users\prasa\Documents\Github\JobHub\02_research\05_evidence\external\youtube\2026-10-18-round-02-additional\pmnY5V16GSE.info.json
C:\Users\prasa\Documents\Github\JobHub\02_research\05_evidence\external\youtube\2026-10-18-round-02-additional\N1Fm4JYae1I.info.json
C:\Users\prasa\Documents\Github\JobHub\02_research\05_evidence\external\youtube\2026-10-18-round-02-additional\ay_wtOte5Gc.info.json
C:\Users\prasa\Documents\Github\JobHub\02_research\05_evidence\external\youtube\2026-10-18-round-02-additional\HHGQ_QeHjF0.info.json
C:\Users\prasa\Documents\Github\JobHub\02_research\05_evidence\external\youtube\2026-10-18-round-02-additional\Risf_QQGX2o.info.json
```

These contained approximately 5.27 MB of player metadata and are reproducible with yt-dlp, subject to future source availability. This log deliberately excludes signed player URLs. Deletion was scoped by resolved literal paths; no wildcard, recursion, supplied-file change, or shared-file cleanup was used.

Completed cleanup checkpoint: **2026-10-18T21:51:18.5649332+08:00**. Confirmed each of the five resolved file parents exactly matched the assigned additional-evidence directory, verified this provenance log existed, and removed those five literal paths with PowerShell `Remove-Item -LiteralPath`. Removed **5,271,806 bytes**. This was permanent local deletion of reproducible generated metadata, not a recycle-bin operation. All SRT files were preserved.

Validation checkpoint: **2026-10-18T21:51:36.3323939+08:00**. Confirmed ten SRT files, 3,587 nonempty cues, all ten SHA-256 hashes matching this log, and 12 local Markdown links resolving. Additional directory contained exactly five SRT files, zero metadata JSON, and zero audio/video files. Per-caption provenance is explicit above: five supplied automatic tracks; two additional automatic tracks; three additional tracks listed in yt-dlp's manual-subtitle table. The latter means **manual-track provenance, not independently verified human transcription**.

Candidate gaps/exclusions at handoff: failed C04 is retained in the count; the CNA salary page did not yield a checked YouTube video; the SDSU lead returned 429; Khan text extraction was empty; UNI led to documents rather than a retained video. These page failures are logged without inventing video metadata or claiming missing English captions. Express Tech remains a weak tutorial, not a verified success story; Practical Wisdom remains weak historical salary guidance. No further collection was undertaken after the coordinator requested closure with the existing five captures.

Stop: thematic complements captured, bounded candidate checks complete, transcript analysis complete, unsupported statistics separated, and unresolved Singapore/firsthand/accessibility/device-continuation gaps handed off. This is neither exhaustive discovery nor source saturation.
