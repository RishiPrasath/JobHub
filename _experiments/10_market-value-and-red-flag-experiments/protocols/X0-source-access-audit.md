# X0: official source access audit

**Question.** For each official source that could show a company's red flags, can it be checked by company name, in what form, and may we access it automatically?

**Sources to audit (fixed):** MAS enforcement actions; PDPC decisions and enforcement; MOM employment agency licences, suspensions and revocations; MOM actions against employers (for example debarment or work-pass penalties, if listed publicly); CASE company alerts or complaints information; SGX company announcements (regulatory); Singapore court judgments (eLitigation or the judiciary's public judgments page); ACRA data (already used).

**For each source record:** URL; publisher; what it lists (entities or individuals, issue types, date range); format (web list, PDF, downloadable data, search form); whether it can be searched or filtered by company name; update frequency; what its terms of use and robots.txt say about automated access (quote the relevant sentence); whether a plain read of the list pages is permitted; whether a machine-readable download exists.

**Method.** One Haiku-model agent reads each source's pages and terms and fills the table; the lead researcher spot-checks three entries.

**Output.** `outputs/x0/source-audit.md` with one row per source and a go or no-go for use in X1 (go = list readable and automated reading permitted or clearly not prohibited; no-go = terms prohibit it or it cannot be read).

**Use.** The go sources define where the X1 ground truth comes from. No-go sources are not used.

**Pass/fail.** Not a hypothesis test. The experiment succeeds if at least three sources are go and together list at least 20 Singapore organisations (not individuals) with a documented issue in the last five years; if not, X1 is run on whatever qualifies and its sample size is stated.
