# YouTube source captures — job-posting red flags

Captured: 2026-10-18

## Capture status

The Codex browser's built-in YouTube transcript export reported that no transcript was available for the first four videos. The fifth video was checked through `yt-dlp` only. A local `yt-dlp` check found English original auto-generated caption tracks for all five. The caption files below were extracted as timestamped SRT files without downloading the videos. The browser result was an access limitation, not proof that captions were absent.

These are machine-generated captions. Verify important wording, salary figures, qualifications, negations, and other high-impact claims against the video at the recorded timestamp before using them as evidence.

## Sources

| Video | Channel | Published | Caption capture |
|---|---|---:|---|
| [Spot the red flags in job listings \| Work It podcast](https://www.youtube.com/watch?v=iVeoEF3bzlY) | CNA | 2025-06-09 | [iVeoEF3bzlY.en-orig.srt](iVeoEF3bzlY.en-orig.srt) |
| [7 Sneaky Red Flags To Pay Attention To In Your Job Search](https://www.youtube.com/watch?v=0KXDCuxi3jk) | A Life After Layoff | 2025-06-09 | [0KXDCuxi3jk.en-orig.srt](0KXDCuxi3jk.en-orig.srt) |
| [Major RED FLAGS to look out for in Job Postings!](https://www.youtube.com/watch?v=x2sgf8zlNao) | Recruiter Preston | 2023-04-28 | [x2sgf8zlNao.en-orig.srt](x2sgf8zlNao.en-orig.srt) |
| [10 Red Flags to Look Out For In Job Postings](https://www.youtube.com/watch?v=fCd4wZQaWqo) | A Life After Layoff | 2021-12-28 | [fCd4wZQaWqo.en-orig.srt](fCd4wZQaWqo.en-orig.srt) |
| [6 Things Your Boss SECRETLY Means by “Nobody Wants to Work”](https://www.youtube.com/watch?v=IF3McdG_dSY) | Dani Careers | 2026-10-11 | [IF3McdG_dSY.en-orig.srt](IF3McdG_dSY.en-orig.srt) |

## Reproduction command

```powershell
py -m yt_dlp --skip-download --write-auto-subs --sub-langs "en-orig" --sub-format srt --no-playlist "YOUTUBE_URL"
```

The captions are source material only. They are not yet analyzed findings, prevalence evidence, or proof that job seekers generally experience the described problems.
