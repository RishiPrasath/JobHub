"""Local cache of verified official sites, keyed by UEN. Each employer is searched once; later lookups need no external service."""
import sqlite3, time
from pathlib import Path


def _con(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.execute("create table if not exists site(uen text primary key, legal_name text, url text, title text, description text, "
                "verified text, found_by text, checked_at text)")
    return con


def get(path, uen):
    con = _con(path)
    r = con.execute("select uen,legal_name,url,title,description,verified,found_by,checked_at from site where uen=?", (uen,)).fetchone()
    con.close()
    return dict(zip(("uen", "legal_name", "url", "title", "description", "verified", "found_by", "checked_at"), r)) if r else None


def put(path, uen, legal_name, url, title, description, verified, found_by):
    con = _con(path)
    con.execute("insert or replace into site values(?,?,?,?,?,?,?,?)",
                (uen, legal_name, url, title, description, verified, found_by, time.strftime("%Y-%m-%d")))
    con.commit()
    con.close()
