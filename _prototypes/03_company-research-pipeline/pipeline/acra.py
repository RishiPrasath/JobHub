"""ACRA entity resolution from data.gov.sg bulk CSVs, indexed in SQLite FTS5. No API key."""
import csv, json, re, sqlite3, time, urllib.request
from difflib import SequenceMatcher
from pathlib import Path

UA = "JobHubResearchBot/0.1 (research prototype)"
META = "https://api-production.data.gov.sg/v2/public/api/collections/2/metadata"
POLL = "https://api-open.data.gov.sg/v1/public/api/datasets/{}/poll-download"
STOP = {"pte", "ltd", "limited", "private", "co", "operative", "the", "of", "and"}   # 'singapore' is kept: it can be the distinctive word
SIBLING_GAP = 0.2   # another live entity within this score of the top one -> needs confirmation


def toks(s):
    return [t for t in re.sub(r"[^a-z0-9 ]", " ", (s or "").lower()).split() if t not in STOP]


def _get(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=timeout)


def download(csv_dir, ids=None):
    """Download every ACRA entity CSV; honours the 429 'retry in 10 seconds' limit."""
    csv_dir = Path(csv_dir)
    csv_dir.mkdir(parents=True, exist_ok=True)
    ids = ids or json.load(_get(META))["data"]["collectionMetadata"]["childDatasets"]
    for i in ids:
        dest = csv_dir / f"{i}.csv"
        if dest.exists():
            continue
        for _ in range(8):
            try:
                r = json.load(_get(POLL.format(i)))
                if r.get("code") == 0 and r["data"].get("url"):
                    dest.write_bytes(_get(r["data"]["url"], 300).read())
                    break
            except Exception:
                pass
            time.sleep(12)
        time.sleep(6)
    return len(list(csv_dir.glob("*.csv")))


def build_index(csv_dir, db_path):
    """(Re)build the SQLite index from the CSVs."""
    db_path = Path(db_path)
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    con.execute("create table ent(id integer primary key, uen, name, f1, f2, f3, type, status, inc, ssic)")
    con.execute("create virtual table fts using fts5(name, former, tokenize='unicode61')")
    csv.field_size_limit(10 ** 7)
    n = 0
    for f in sorted(Path(csv_dir).glob("*.csv")):
        with open(f, encoding="utf-8-sig", newline="") as fh:
            rows, frows = [], []
            for r in csv.DictReader(fh):
                n += 1
                f1, f2, f3 = (r.get(f"former_entity_name{i}", "") for i in (1, 2, 3))
                rows.append((n, r["uen"], r["entity_name"], f1, f2, f3, r["entity_type_description"],
                             r["entity_status_description"], r["registration_incorporation_date"], r["primary_ssic_description"]))
                frows.append((n, " ".join(toks(r["entity_name"])), " ".join(toks(" ".join((f1, f2, f3))))))
            con.executemany("insert into ent values(?,?,?,?,?,?,?,?,?,?)", rows)
            con.executemany("insert into fts(rowid,name,former) values(?,?,?)", frows)
    con.execute("create index ix_uen on ent(uen)")
    con.commit()
    con.close()
    return n


def _variants(tokens):
    """Original tokens plus versions with one adjacent pair joined ('grab taxi' -> 'grabtaxi')."""
    out = [tokens]
    for i in range(len(tokens) - 1):
        out.append(tokens[:i] + [tokens[i] + tokens[i + 1]] + tokens[i + 2:])
    return out


def _search(con, tokens, limit=60):
    if not tokens:
        return {}
    q = " OR ".join("(" + " AND ".join('"%s"' % t for t in v) + ")" for v in _variants(tokens))
    rows = con.execute("select e.uen,e.name,e.f1,e.f2,e.f3,e.type,e.status,e.inc,e.ssic from fts join ent e on e.id=fts.rowid "
                       "where fts match ? limit ?", (q, limit)).fetchall()
    return {r[0]: r for r in rows}


def _score(q_tokens, row):
    names = [row[1], row[2], row[3], row[4]]
    qs = " ".join(q_tokens)
    return max(SequenceMatcher(None, qs, " ".join(toks(n))).ratio() for n in names if n)


def _is_live(row):
    return row[6].lower().startswith("live")


PUBLIC_BODY = re.compile(r"\b(board|authority|ministry|council|agency|commission|department)\b", re.I)


def _same_name(q_tokens, row):
    """True when the query and any registered name of the entity have exactly the same tokens."""
    return any(n and sorted(toks(n)) == sorted(q_tokens) for n in (row[1], row[2], row[3], row[4]))


def _record(score, row, partial=False):
    return {"score": round(score, 3), "uen": row[0], "name": row[1], "type": row[5], "status": row[6],
            "incorporated": row[7], "ssic": row[8], "partial_name_match": partial}


def resolve(db_path, employer, uen=None, hint=None):
    """Return {'state', 'chosen', 'candidates', 'why'}. States: exact_by_uen, exact, likely,
    needs_confirmation, unresolved. Never silently picks between sibling entities."""
    con = sqlite3.connect(db_path)
    if uen:
        r = con.execute("select uen,name,f1,f2,f3,type,status,inc,ssic from ent where uen=?", (uen,)).fetchone()
        con.close()
        if r:
            return {"state": "exact_by_uen", "chosen": _record(1.0, r), "candidates": [], "why": "UEN supplied by the posting"}
        return {"state": "unresolved", "chosen": None, "candidates": [], "why": "UEN %s not in registry" % uen}
    q = toks(hint or employer)
    found = _search(con, q)
    partial = False
    if not found and len(q) > 1:           # brand prefix / extra token: retry with one token dropped
        for i in range(len(q)):
            found.update(_search(con, q[:i] + q[i + 1:]))
        partial = bool(found)
    con.close()
    scored = sorted(((_score(q, r), r) for r in found.values()), key=lambda x: -x[0])
    cands = [_record(s, r, partial) for s, r in scored[:6]]
    if not scored:
        if PUBLIC_BODY.search(employer):
            return {"state": "public_body", "chosen": None, "candidates": [],
                    "why": "looks like a statutory board or government body; these are not in the company registry datasets"}
        return {"state": "unresolved", "chosen": None, "candidates": [], "why": "no registry name contains the name tokens"}
    live = [(s, r) for s, r in scored if _is_live(r)]
    pool = live or scored                   # prefer live entities; dissolved ones are context only
    top_s, top_r = pool[0]
    rivals = [r for s, r in pool[1:] if top_s - s <= SIBLING_GAP and s >= 0.6]
    base = {"candidates": cands}
    if partial and PUBLIC_BODY.search(employer):
        return {"state": "public_body", "chosen": None, "candidates": cands,
                "why": "looks like a statutory board or government body; the closest registry names are unrelated companies"}
    if partial:
        return {**base, "state": "needs_confirmation", "chosen": _record(top_s, top_r, True),
                "why": "matched only after dropping a name token (brand or extra word)"}
    if rivals and not partial and top_s >= 0.99 and _same_name(q, top_r) and not any(_same_name(q, r) for r in rivals):
        # the posted name is a registered name word for word; other entities only add words to it
        return {**base, "state": "exact", "chosen": _record(top_s, top_r),
                "why": "posted name matches this registered name exactly; %d sibling entity(ies) with extra words: %s"
                       % (len(rivals), ", ".join(r[1] for r in rivals[:3])), "siblings": [r[1] for r in rivals]}
    if rivals:
        return {**base, "state": "needs_confirmation", "chosen": _record(top_s, top_r),
                "why": "%d other live entity(ies) share the name stem: %s" % (len(rivals), ", ".join(r[1] for r in rivals[:3]))}
    if top_s >= 0.95 and sorted(toks(top_r[1])) != sorted(q) and _same_name(q, top_r):
        return {**base, "state": "needs_confirmation", "chosen": _record(top_s, top_r),
                "why": "matches a former or alternate registered name; current name is " + top_r[1]}
    if top_s >= 0.95:
        return {**base, "state": "exact", "chosen": _record(top_s, top_r), "why": "single live entity with matching name"}
    extra = [t for t in toks(top_r[1]) if t not in q]
    if top_s >= 0.8 and extra:
        return {**base, "state": "needs_confirmation", "chosen": _record(top_s, top_r),
                "why": "closest registered name adds words not in the posted name: " + " ".join(extra)}
    if top_s >= 0.8:
        return {**base, "state": "likely", "chosen": _record(top_s, top_r), "why": "name differs from registered name"}
    return {**base, "state": "needs_confirmation", "chosen": _record(top_s, top_r), "why": "weak name match"}
