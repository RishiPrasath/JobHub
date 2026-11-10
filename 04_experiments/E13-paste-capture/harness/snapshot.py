"""Minimal snapshot step for E13 (paste in, dated snapshot out).

Deterministic: regular expressions and counts. No model is called here.
  - stores the pasted text unchanged, with its capture time (nothing is normalised in storage)
  - detects the five minimum fields on a normalised COPY of the text
  - flags partial pastes (cut off, no role body, only cards or navigation)
  - applies the stale rule and returns the notice with a prompt to paste again
  - keeps corrections as separate revisions and can restore the original

This is a test instrument, not the product. Version below is recorded in every run.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

VERSION = "snapshot-step 0.1.0 (E13, deterministic)"
SGT = timezone(timedelta(hours=8))
STALE_DAYS = 7
NOTICE_TEXT = "This copy of the posting may be out of date. Paste the posting again to refresh it."

MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}


# ---------------------------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------------------------
def normalise(text: str) -> str:
    """Normalised COPY for analysis only. Never used for storage."""
    t = text.replace("\r\n", "\n").replace("\r", "\n")
    t = t.replace(" ", " ").replace("​", "").replace("﻿", "")
    return t


def lines_of(text: str) -> list[str]:
    return [ln.strip() for ln in normalise(text).split("\n") if ln.strip()]


def words(s: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9$'&\-]+", s)


ROLE = (r"assistant|executive|manager|officer|engineer|analyst|clerk|cleaner|packer|crew|usher|barista|rider|designer|"
        r"coordinator|administrator|accountant|receptionist|specialist|technician|supervisor|driver|cook|chef|developer|"
        r"consultant|operator|associate|director|representative|agent|teacher|tutor|nurse|cashier|attendant|worker|helper|"
        r"planner|scientist|architect|secretary|trainee|intern|lead|promoter|packer|picker|porter")
ROLE_RE = re.compile(rf"\b({ROLE})s?\b", re.I)
SMALL = {"and", "of", "the", "for", "in", "to", "a", "an", "&", "at", "on", "with", "or"}

BODY_HEADS = {"job description", "roles & responsibilities", "roles and responsibilities", "responsibilities", "job responsibilities",
              "key responsibilities", "requirements", "job requirements", "qualifications", "what you'll do", "what you will do",
              "what you'll bring", "what you will bring", "about the role", "the role", "duties", "your role", "who we are looking for"}
STOP_HEADS = {"skills", "additional information", "benefits", "how to apply", "report this job", "company overview", "about the company",
              "similar jobs", "jobs you might like", "related jobs", "recommended jobs", "apply for this job", "equal opportunity employer.",
              "about myc areersfuture", "about mycareersfuture", "about jobstreet", "privacy", "terms and conditions", "terms of use"}
CARD_HEADS = {"similar jobs", "jobs you might like", "related jobs", "recommended jobs", "you may also like"}
FOOT_START = ("about mycareersfuture", "about jobstreet", "privacy", "terms", "©")
PLATFORMS = ("mycareersfuture", "jobstreet", "fastjobs", "government of singapore", "seek", "indeed", "linkedin")


def head_key(line: str) -> str:
    return line.strip().rstrip(":").strip().lower()


def title_like(line: str) -> bool:
    if len(line) > 80 or ":" in line or "$" in line or line.endswith(".") or line[:1] in "•-–*":
        return False
    core = re.sub(r"\(.*?\)", "", line).strip()
    ws = [w for w in words(core) if w.lower() not in SMALL]
    if not (1 <= len(ws) <= 7) or not ROLE_RE.search(core):
        return False
    cap = sum(1 for w in ws if w[0].isupper() or w[0].isdigit())
    return cap / len(ws) >= 0.6


def card_region(lines: list[str]) -> tuple[int, int]:
    for i, ln in enumerate(lines):
        if head_key(ln) in CARD_HEADS:
            for j in range(i + 1, len(lines)):
                if lines[j].lower().startswith(FOOT_START):
                    return i, j
            return i, len(lines)
    return -1, -1


# ---------------------------------------------------------------------------------------------
# dates
# ---------------------------------------------------------------------------------------------
DATE_TXT = r"(?P<d>\d{1,2})(?:st|nd|rd|th)?\s+(?P<m>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?,?\s+(?P<y>\d{4})"
DATE_NUM = r"(?P<d2>\d{1,2})[/.-](?P<m2>\d{1,2})[/.-](?P<y2>\d{4})"
DATE_ISO = r"(?P<y3>\d{4})-(?P<m3>\d{2})-(?P<d3>\d{2})"
CLOSE_KEY = r"(?:clos(?:es|ing|e)(?:\s+date)?|deadline|apply\s+(?:by|before)|expires?|valid\s+until|last\s+day(?:\s+to\s+apply)?)"
CLOSE_DATE_RE = re.compile(rf"{CLOSE_KEY}\W{{0,3}}(?:on\s+|is\s+)?(?:{DATE_TXT}|{DATE_NUM}|{DATE_ISO})", re.I)
CLOSE_REL_RE = re.compile(r"clos(?:es|ing)\s+in\s+(\d+)\s+days?", re.I)
CLOSE_NONE_RE = re.compile(r"open\s+until\s+(?:filled|further\s+notice)|until\s+(?:the\s+)?(?:position|positions|role|roles|vacancy|vacancies)\s+(?:is|are)\s+filled|"
                           r"no\s+closing\s+date|rolling\s+basis|ongoing\s+recruitment|continuous(?:ly)?\s+hiring|hiring\s+until|until\s+filled", re.I)


def parse_close(m: re.Match) -> date | None:
    g = m.groupdict()
    try:
        if g.get("d"):
            return date(int(g["y"]), MONTHS[g["m"].lower()[:3]], int(g["d"]))
        if g.get("d2"):
            return date(int(g["y2"]), int(g["m2"]), int(g["d2"]))  # day first (Singapore)
        if g.get("y3"):
            return date(int(g["y3"]), int(g["m3"]), int(g["d3"]))
    except ValueError:
        return None
    return None


# ---------------------------------------------------------------------------------------------
# analysis
# ---------------------------------------------------------------------------------------------
MONEY_RE = re.compile(r"(?:S\$|SGD|\$)\s?\d[\d,]*(?:\.\d+)?", re.I)
PAY_NONE_RE = re.compile(r"(?:salary|pay|compensation|remuneration)[^\n]{0,60}?(?:negotiable|not\s+(?:disclosed|published|stated|shown|provided)|undisclosed|to\s+be\s+discussed|discussed\s+at\s+interview|on\s+request)|salary\s+undisclosed", re.I)
SUFFIX_RE = re.compile(r"\b(pte\.?\s*ltd\.?|ltd\.?|limited|llp|inc\.?|corporation|corp\.?|group|holdings|services|solutions|systems|labs|enterprises|associates|co\.?)\s*$|\bpte\s+ltd\b", re.I)
UI_RE = re.compile(r"^(new|featured|urgent hiring|be an early applicant|apply now|save( job)?|share|quick apply|job match.*|accept.*|decline|manage preferences|reject.*)$", re.I)
TYPE_RE = re.compile(r"\b(full[- ]?time|part[- ]?time|contract|permanent|temporary|freelance|casual|internship|entry|junior|senior|mid-senior|non-executive|executive)\b", re.I)
HIDDEN_LABEL_RE = re.compile(r"^(hiring company|company|employer|advertiser|posted by)\b.*(confidential|hidden|not disclosed|shown after|withheld)|^private advertiser$|"
                             r"(company|employer) name.*(confidential|hidden|not disclosed|withheld|shown after)|^confidential (employer|company)$", re.I)
LABEL_EMP_RE = re.compile(r"^(?:company|employer|hiring company)\s*:\s*(\S.*)$", re.I)
TEASER_RE = re.compile(r"(show more|read more|see more|view more|continue reading|\.\.\.|…)\s*$", re.I)
FOOTERISH = re.compile(r"(©|privacy|terms|apply|save|share|report this job|posted|closing|safety tip|tap apply)", re.I)
SEARCH_SIGNS = [re.compile(p, re.I) for p in (r"^search results", r"\d+\s+jobs?(\s+found)?$", r"^sort by", r"^filters?\b", r"^page \d", r"^open positions", r"^view all \d+", r"jobs? in singapore$")]


def analyse(text: str, captured_at: datetime) -> dict:
    ls = lines_of(text)
    cs, ce = card_region(ls)
    main = [ln for i, ln in enumerate(ls) if not (cs <= i < ce)]
    joined = "\n".join(main)

    # --- title ---
    title = None
    t_idx = None
    for i, ln in enumerate(main):
        if head_key(ln) in BODY_HEADS or head_key(ln) in STOP_HEADS:
            continue
        m = re.match(r"^(?:job title|position|role)\s*:\s*(\S.*)$", ln, re.I)
        if m:
            title, t_idx = m.group(1), i
            break
        if title_like(ln):
            title, t_idx = ln, i
            break

    # --- employer ---
    employer_state, employer_val = "missing", None
    for ln in main:
        if HIDDEN_LABEL_RE.search(ln):
            employer_state, employer_val = "hidden_labelled", ln
            break
    if employer_state == "missing":
        for ln in main:
            m = LABEL_EMP_RE.match(ln)
            if m:
                employer_state, employer_val = "present", m.group(1)
                break
    if employer_state == "missing":
        for ln in main:
            if SUFFIX_RE.search(ln) and len(words(ln)) <= 8 and not ln.startswith(("•", "-")) and not re.search(r"about |advertised|©|\bwe\b|join ", ln, re.I):
                employer_state, employer_val = "present", ln
                break
    if employer_state == "missing" and t_idx is not None:
        for ln in main[t_idx + 1:t_idx + 4]:
            if UI_RE.match(ln) or MONEY_RE.search(ln) or re.match(r"^(pay|location|salary|job type)\s*:", ln, re.I) or re.search(r"posted|viewed", ln, re.I):
                continue
            if TYPE_RE.search(ln) or ln.endswith(", Singapore") or len(words(ln)) > 8 or not (ln[0].isupper() or ln[0].isdigit()):
                continue
            employer_state, employer_val = "present", ln
            break
    if employer_state == "missing":
        for ln in main:
            m = re.match(r"^©\s*\d{4}\s+(.+)$", ln)
            if m and not any(p in m.group(1).lower() for p in PLATFORMS):
                employer_state, employer_val = "present", m.group(1)
                break

    # --- pay ---
    mm = MONEY_RE.search(joined)
    if mm:
        pay_state, pay_val = "present", mm.group(0)
    else:
        pn = PAY_NONE_RE.search(joined)
        pay_state, pay_val = ("explicit_absence", pn.group(0)) if pn else ("missing", None)

    # --- closing date ---
    close_state, close_val, close_iso = "missing", None, None
    cm = CLOSE_DATE_RE.search(joined)
    if cm and parse_close(cm):
        close_state, close_val, close_iso = "present", cm.group(0), parse_close(cm).isoformat()
    else:
        rm = CLOSE_REL_RE.search(joined)
        if rm:
            d = captured_at.astimezone(SGT).date() + timedelta(days=int(rm.group(1)))
            close_state, close_val, close_iso = "present", rm.group(0), d.isoformat()
        else:
            nm = CLOSE_NONE_RE.search(joined)
            if nm:
                close_state, close_val = "explicit_absence", nm.group(0)

    # --- role body ---
    body_lines = 0
    in_body = False
    for ln in main:
        k = head_key(ln)
        if k in BODY_HEADS:
            in_body = True
            continue
        if k in STOP_HEADS:
            in_body = False
            continue
        if in_body and len(words(ln)) >= 3:
            body_lines += 1
    long_lines = sum(1 for ln in main if len(words(ln)) >= 10 and not re.search(r"cookie|privacy|safety|never pay|be careful", ln, re.I))
    duties_state = "present" if (body_lines >= 3 or long_lines >= 3) else "missing"

    # --- partial flags ---
    reasons = []
    last = ls[-1] if ls else ""
    if TEASER_RE.search(last):
        reasons.append("cut_off")
    else:
        tail = ls[-3:]
        if (len(words(last)) > 4 and not re.search(r"[.!?:;)\"']$|\d$", last) and not any(FOOTERISH.search(x) for x in tail)
                and head_key(last) not in BODY_HEADS | STOP_HEADS):
            reasons.append("cut_off")
    if duties_state == "missing":
        reasons.append("no_body")
    distinct_titles = {ln for ln in main if title_like(ln)}
    signs = sum(1 for ln in main for p in SEARCH_SIGNS if p.search(ln))
    if signs >= 2 or len(distinct_titles) >= 3:
        reasons.append("cards_nav")
    miss = [f for f, s in (("title", "present" if title else "missing"), ("employer", employer_state), ("pay", pay_state),
                           ("duties", duties_state), ("closing", close_state)) if s == "missing"]
    return {
        "fields": {"title": "present" if title else "missing", "employer": employer_state, "pay": pay_state,
                   "duties": duties_state, "closing": close_state},
        "values": {"title": title, "employer": employer_val, "pay": pay_val, "closing": close_val},
        "closing_date_iso": close_iso,
        "partial_flag": bool(reasons), "partial_reasons": reasons,
        "missing_fields": miss,
        "minimum_fields_present": not miss,
    }


# ---------------------------------------------------------------------------------------------
# stale rule
# ---------------------------------------------------------------------------------------------
def parse_dt(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def stale_check(captured_at: datetime, closing_date: date | None, now: datetime) -> dict:
    reasons = []
    if closing_date is not None and closing_date < now.astimezone(SGT).date():
        reasons.append("closing_passed")
    if now - captured_at > timedelta(days=STALE_DAYS):
        reasons.append("snapshot_old")
    return {"notice": bool(reasons), "reasons": reasons, "message": NOTICE_TEXT if reasons else None}


# ---------------------------------------------------------------------------------------------
# storage
# ---------------------------------------------------------------------------------------------
def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class SnapshotStore:
    def __init__(self, directory: str | Path):
        self.dir = Path(directory)
        self.dir.mkdir(parents=True, exist_ok=True)

    def _path(self, sid: str) -> Path:
        return self.dir / f"{sid}.json"

    def capture(self, sid: str, raw: bytes, captured_at: datetime) -> dict:
        text = raw.decode("utf-8")  # no newline translation, no normalisation
        rec = {"id": sid, "version": VERSION, "captured_at": captured_at.isoformat(), "original_text": text,
               "original_sha256": sha(text), "revisions": [], "analysis": analyse(text, captured_at)}
        self._path(sid).write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8", newline="")
        return rec

    def load(self, sid: str) -> dict:
        return json.loads(self._path(sid).read_text(encoding="utf-8"))

    def correct(self, sid: str, new_text: str, corrected_at: datetime) -> dict:
        rec = self.load(sid)
        rec["revisions"].append({"corrected_at": corrected_at.isoformat(), "text": new_text})
        self._path(sid).write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8", newline="")
        return rec

    def current_text(self, sid: str) -> str:
        rec = self.load(sid)
        return rec["revisions"][-1]["text"] if rec["revisions"] else rec["original_text"]

    def restore_original(self, sid: str) -> str:
        return self.load(sid)["original_text"]
