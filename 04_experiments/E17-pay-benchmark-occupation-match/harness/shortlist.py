"""Lexical shortlist: about 25 candidate occupations per posting from the 523-entry MOM table.
Design (fixed before any matcher run; no model call):
  - The MOM table has titles only (no duty descriptors), so the index is the occupation title.
  - Score = 0.6 * cosine(word 1-2gram TF-IDF) + 0.4 * cosine(char 3-5gram TF-IDF, word-boundary) between
    posting title and occupation title, plus 0.15 * cosine(word TF-IDF) between posting function and occupation title.
  - Seniority words in the posting title ("senior", "junior", "executive", "assistant", "manager", "supervisor") are kept
    because they appear in occupation titles and carry level information.
  - Take the top K=25 by score.
Usage: python shortlist.py   -> writes runs/.../outputs/shortlists.json and prints recall against data/gold.json."""
import json
import re
import sys
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

E = Path(__file__).resolve().parents[1]
MOM = E.parent / "E10-market-value-and-red-flag-experiments" / "data" / "mom" / "occupations_all_industries.csv"
K = 25
NOISE = re.compile(r"[^\w\s/&-]", re.UNICODE)


def clean(s: str) -> str:
    s = NOISE.sub(" ", s.lower())
    s = re.sub(r"\([^)]*\)", " ", s) if False else s  # keep bracket text; it can carry the real role
    return re.sub(r"\s+", " ", s).strip()


def load_table():
    import csv
    rows = list(csv.DictReader(open(MOM, encoding="utf-8")))
    return [(r["ssoc2024"], r["occupation"]) for r in rows]


def build():
    table = load_table()
    titles = [clean(t.replace("/", " ")) for _, t in table]
    wv = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit(titles)
    cv = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True).fit(titles)
    return table, titles, wv, cv, wv.transform(titles), cv.transform(titles)


def shortlist(posts, k=K):
    table, titles, wv, cv, W, C = build()
    out = {}
    for p in posts:
        q = clean(p["title"].replace("/", " "))
        f = clean(p["function"].replace("/", " "))
        s = 0.6 * cosine_similarity(wv.transform([q]), W)[0] + 0.4 * cosine_similarity(cv.transform([q]), C)[0]
        s = s + 0.15 * cosine_similarity(wv.transform([f]), W)[0]
        idx = s.argsort()[::-1][:k]
        out[p["id"]] = [{"code": table[i][0], "title": table[i][1], "score": round(float(s[i]), 4)} for i in idx]
    return out


def main():
    posts = json.loads((E / "data/postings.json").read_text(encoding="utf-8"))
    sl = shortlist(posts)
    outdir = E / "runs/2026-11-10-run-001/outputs"
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "shortlists.json").write_text(json.dumps(sl, ensure_ascii=False, indent=1), encoding="utf-8")
    gold = {g["id"]: g for g in json.loads((E / "data/gold.json").read_text(encoding="utf-8"))}
    codes_ok = lost = 0
    miss = []
    for pid, g in gold.items():
        real = [c for c in g["accept"] if c != "NONE"]
        if not real:
            continue
        codes_ok += 1
        have = {c["code"] for c in sl[pid]}
        if not (set(real) & have):
            lost += 1
            miss.append((pid, g["title"], real))
    print(f"postings with a real gold code: {codes_ok}; gold code absent from the {K}-shortlist: {lost} ({lost/codes_ok:.1%})")
    for m in miss:
        print("  lost:", m)


if __name__ == "__main__":
    sys.exit(main())
