"""Re-fetch the employer's own page for each truth item and store a verbatim quote around the key string. Output: data/truth_quotes.json
(reviewed by the experiment author before ground truth is written). Employer pages only; registry mirrors are refused."""
import json, re, sys, urllib.request, datetime
UA = "JobHubE11-truthcheck/0.1 (research; single page fetches)"
ITEMS = {
 "L01": ("https://www.dbs.com.sg/", "196800306E"),
 "L02": ("https://www.keppel.com/", "Copyright © Keppel Ltd"),
 "L03": ("https://www.comfortdelgro.com/", "ComfortDelGro Corporation Limited"),
 "L04": ("https://www.changiairport.com/en/privacy-policy.html", "Changi Airport Group (Singapore) Pte. Ltd."),
 "L05": ("https://www.capitaland.com/privacy-policy", "CapitaLand Group Pte. Ltd."),
 "L06": ("https://www.rafflesmedicalgroup.com/", "Raffles Medical Group Ltd"),
 "L06b": ("https://www.rafflesmedicalgroup.com/privacy-policy", "Raffles Medical Group Ltd"),
 "L07": ("https://www.starbucks.com.sg/privacy-policy", "Starbucks Coffee Singapore Pte. Ltd."),
 "L08": ("https://www.singaporeair.com/en_UK/sg/privacy-policy/", "Singapore Airlines Limited"),
 "S01": ("https://www.yakun.com/privacy-policy", "Ya Kun International Private Limited"),
 "S02": ("https://www.burgerking.com.sg/about", "Burger King Singapore Pte. Ltd."),
 "S03": ("https://www.nium.com/privacy", "Nium Pte. Ltd."),
 "S04": ("https://fundingsocieties.com/terms-of-use", "201505169M"),
 "S05": ("https://ohmyhome.com/terms", "201525768E"),
 "S06": ("https://www.koufu.com.sg/privacy-policy", "Koufu Group Limited"),
 "S07": ("https://seedly.sg/privacy", "Seedly Pte. Ltd."),
 "B01": ("https://www.ocbc.com/", "193200032W"),
 "B02": ("https://www.singtel.com/", "199201624D"),
 "B03": ("https://www.singpost.com/privacy-policy", "199201623M"),
 "B04": ("https://www.grab.com/privacy-policy", "Grabtaxi Holdings"),
 "B04b": ("https://www.grab.com/privacy", "Grabtaxi Holdings"),
 "B05": ("https://www.income.com.sg/terms-of-use", "202135698W"),
 "B06": ("https://www.mcdonalds.com.sg/privacy", "Hanbaobao Pte. Ltd."),
 "B07": ("https://www.mrbean.com.sg/privacy-policy", "Super Bean International Pte Ltd"),
 "B08": ("https://www.swensens.com.sg/privacy-policy", "ABR Holdings Limited"),
 "B09": ("https://aspireapp.com/terms-and-conditions", "Aspire FT Pte. Ltd."),
 "B10": ("https://www.toastbox.com.sg/", "Toast Box"),
}
def txt(u):
    h = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=20).read(1500000).decode("utf8", "ignore")
    h = re.sub(r"(?is)<(script|style).*?</\1>", " ", h); h = re.sub(r"<[^>]+>", " ", h)
    h = h.replace("&amp;", "&").replace("&nbsp;", " ").replace("&copy;", "©").replace("&#038;", "&")
    return re.sub(r"\s+", " ", h)
out = {}
for k, (u, key) in ITEMS.items():
    try:
        t = txt(u); i = t.find(key)
        out[k] = {"url": u, "key": key, "found": i >= 0, "quote": t[max(0, i-140):i+len(key)+140] if i >= 0 else None}
    except Exception as e:
        out[k] = {"url": u, "key": key, "found": False, "error": str(e)[:100]}
    print(k, out[k]["found"], (out[k].get("quote") or out[k].get("error") or "")[:300])
json.dump({"retrieved_utc": datetime.datetime.utcnow().isoformat() + "Z", "items": out}, open("data/truth_quotes.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
