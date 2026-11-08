"""Read the public detail page of each collated MyCareersFuture link through Kimi WebBridge (one session, one tab group).
Usage: python mcf_details.py <links_all.json> <out_dir>
Read-only: loads each job page, extracts visible text, company link and any UEN printed on the page. No login, no apply, 3-second pause per page."""
import json, re, sys, time, urllib.request
from pathlib import Path

DAEMON = "http://127.0.0.1:10086/command"
SESSION = "jobhub-job-details"
JS = r"""(async () => {
  for (let i = 0; i < 24 && !(document.querySelector('h1') && document.body.innerText.length > 800); i++) await new Promise(r => setTimeout(r, 500));
  const company = document.querySelector('a[href*="/company/"]');
  const text = document.body.innerText.replace(/[ \t]+/g, ' ').replace(/\n{2,}/g, '\n');
  return JSON.stringify({title: document.title, h1: (document.querySelector('h1') || {}).innerText || '', final_url: location.href,
    company_link: company ? company.href : null, company_text: company ? company.innerText : null, text: text.slice(0, 9000)});
})()"""
UEN = re.compile(r"\b(?:\d{8,9}[A-Z]|[TSR]\d{2}[A-Z]{2}\d{4}[A-Z])\b")


def call(action, args):
    body = json.dumps({"action": action, "args": args, "session": SESSION}).encode("utf-8")
    return json.load(urllib.request.urlopen(urllib.request.Request(DAEMON, body, {"Content-Type": "application/json"}), timeout=90))


def main():
    links = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out_dir = Path(sys.argv[2]); out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for j in links:
        dest = out_dir / (j["id"] + ".json")
        rec = {"id": j["id"], "url": j["url"]}
        if dest.exists() and "error" not in json.loads(dest.read_text(encoding="utf-8")):
            continue   # already captured; reruns only retry failures
        try:
            nav = call("navigate", {"url": j["url"], "group_title": "JobHub job details"})
            if not nav.get("ok"):
                rec["error"] = "navigate_failed"
            else:
                d = json.loads(call("evaluate", {"code": JS})["data"]["value"])
                rec.update(h1=d["h1"], page_title=d["title"], final_url=d["final_url"], company_link=d["company_link"], company_text=d["company_text"],
                           uen_on_page=sorted(set(UEN.findall(d["text"]))), text=d["text"], text_chars=len(d["text"]))
                if "/job/" not in d["final_url"]:
                    rec["error"] = "redirected_away"
        except Exception as e:
            rec["error"] = type(e).__name__ + ": " + str(e)[:100]
        dest.write_text(json.dumps(rec, indent=1, ensure_ascii=False), encoding="utf-8")
        rows.append({k: rec.get(k) for k in ("id", "h1", "company_text", "uen_on_page", "text_chars", "error")})
        print(j["id"], rec.get("h1", "")[:50], "| chars", rec.get("text_chars"), "| uen", rec.get("uen_on_page"), rec.get("error", ""), flush=True)
        time.sleep(6)
    (out_dir / "_summary.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")


main()
