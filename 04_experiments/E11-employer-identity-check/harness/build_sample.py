"""Builds the synthetic sample (postings.json), the ground truth (ground_truth.json) and the flow input (run_input.json).
Written BEFORE any run of the system under test, then frozen by hash (protocol/FROZEN.md). Every posting is synthetic: the employer
names are real publicly known employers (or constructed names), the role/text is invented by the experiment author (an AI).
Truth comes from the employer's own public page (quote in data/truth_quotes.json) plus the raw ACRA registry record by UEN
(harness/truth_sql.py). Registry-mirror sites were not used."""
import json
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parents[1] / "data"
Q = json.load(open(D / "truth_quotes.json", encoding="utf-8"))["items"]


def ent(i, stratum, employer, role, uen, regname, qkey, note=""):
    return dict(id=i, stratum=stratum, employer=employer, role=role, truth="entity", truth_uen=uen,
                truth_registered_name=regname, evidence=[qkey] if qkey else [], note=note)


def unk(i, stratum, employer, role, plausible, note, qkey=None):
    return dict(id=i, stratum=stratum, employer=employer, role=role, truth="unknown", plausible_uens=plausible,
                evidence=[qkey] if qkey else [], note=note)


def nd(i, employer, role, note):
    return dict(id=i, stratum="hidden", employer=employer, role=role, truth="not_disclosed", evidence=[], note=note)


def fake(i, employer, role, note):
    return dict(id=i, stratum="lookalike", employer=employer, role=role, truth="not_real", evidence=[],
                note=note + " Registry (raw ACRA, exact and wildcard name search) has no entity with this name.")


ITEMS = [
    # large
    ent("L01", "large", "DBS Bank Ltd", "Customer Service Officer", "196800306E", "DBS BANK LTD.", "L01"),
    ent("L02", "large", "Keppel Ltd", "Project Engineer", "196800351N", "KEPPEL LTD.", "L02"),
    ent("L03", "large", "ComfortDelGro Corporation Limited", "Bus Captain", "200300002K", "COMFORTDELGRO CORPORATION LIMITED", "L03"),
    ent("L04", "large", "Changi Airport Group (Singapore) Pte. Ltd.", "Airport Operations Executive", "200910817N", "CHANGI AIRPORT GROUP (SINGAPORE) PTE. LTD.", "L04"),
    ent("L05", "large", "CapitaLand Group Pte. Ltd.", "Asset Manager", "198900036N", "CAPITALAND GROUP PTE. LTD.", "L05",
        note="CapitaLand Investment Limited is a separate entity named in the same policy."),
    ent("L06", "large", "Raffles Medical Group Ltd", "Staff Nurse", "198901967K", "RAFFLES MEDICAL GROUP LTD", "L06"),
    ent("L07", "large", "Starbucks Coffee Singapore Pte. Ltd.", "Barista", "198800670D", "STARBUCKS COFFEE SINGAPORE PTE. LTD.", "L07"),
    unk("L08", "large", "Singapore Airlines Limited", "Cabin Crew", ["197200078R"],
        "Own-site legal-name page not retrieved in this run (privacy URL 404). Registry has exactly one SINGAPORE AIRLINES LIMITED (197200078R), but the rule needs the employer's own page, so truth is kept unknown."),
    unk("L09", "large", "NTUC FairPrice Co-operative Ltd", "Store Assistant", [],
        "Own site names NTUC FairPrice Co-operative Ltd only in product data; the ACRA dataset has no entity with that name (a co-operative may be registered elsewhere). Truth unknown; no ACRA entity is plausible, so any accepted ACRA entity is scored wrong."),
    # SME / small chains / startups
    ent("S01", "sme", "Ya Kun International Private Limited", "Kitchen Assistant", "200104668W", "YA KUN INTERNATIONAL PTE LTD", "S01",
        note="Own site says 'Private Limited'; registry says 'PTE LTD'."),
    ent("S02", "sme", "Burger King Singapore Pte. Ltd.", "Crew Member", "200900741N", "BURGER KING SINGAPORE PTE. LTD.", "S02"),
    ent("S03", "sme", "Nium Pte. Ltd.", "Software Engineer", "201422465R", "NIUM PTE. LTD.", "S03"),
    ent("S04", "sme", "Funding Societies Pte. Ltd.", "Credit Analyst", "201505169M", "FUNDING SOCIETIES PTE. LTD.", "S04",
        note="Terms name two entities 'and/or' (also FS Capital 201631787R); the posted name matches the first."),
    ent("S05", "sme", "Ohmyhome Pte. Ltd.", "Property Consultant", "201525768E", "OHMYHOME PTE. LTD.", "S05"),
    ent("S06", "sme", "Seedly Pte. Ltd.", "Content Writer", "201602731H", "SEEDLY PTE. LTD.", "S07",
        note="Part of MoneyHero Group per own site."),
    unk("S07", "sme", "Koufu Group Limited", "Food Court Assistant", ["201732833D"],
        "Own site says 'Koufu Group Limited'; the registry's only KOUFU GROUP entity is 'KOUFU GROUP PTE. LTD.' (201732833D). Name and legal form disagree, so truth is kept unknown.", "S06"),
    unk("S08", "sme", "Carousell", "Community Operations Executive", ["201300296D"],
        "Own site says 'Carousell Ltd.' (a non-Singapore form); the registry has CAROUSELL PTE. LTD. (201300296D), which the site evidence does not tie to the operating employer. Truth unknown; 201300296D is listed as plausible.", "S08"),
    # brand differs from registered name
    ent("B01", "brand", "OCBC Bank", "Relationship Manager", "193200032W", "OVERSEA-CHINESE BANKING CORPORATION LIMITED", "B01"),
    ent("B02", "brand", "Singtel", "Network Engineer", "199201624D", "SINGAPORE TELECOMMUNICATIONS LIMITED", "B02"),
    ent("B03", "brand", "SingPost", "Postal Officer", "199201623M", "SINGAPORE POST LIMITED", "B03"),
    ent("B05", "brand", "NTUC Income", "Customer Service Executive", "202135698W", "INCOME INSURANCE LIMITED", "B05",
        note="Own site footer: 'Income (UEN 202135698W)'. The registry's NTUC INCOME HOLDINGS (201731790R) is a different entity."),
    ent("B06", "brand", "McDonald's Singapore", "Crew Member", "197600722D", "HANBAOBAO PTE. LTD.", "B06",
        note="Own privacy page names Hanbaobao Pte. Ltd. as 'Licensee of McDonald's'."),
    ent("B07", "brand", "Mr Bean", "Store Assistant", "199901613E", "SUPER BEAN INTERNATIONAL PTE LTD", "B07"),
    ent("B08", "brand", "Swensen's", "Service Crew", "197803023H", "ABR HOLDINGS LIMITED", "B08"),
    ent("B09", "brand", "Aspire", "Customer Success Associate", "201903520D", "ASPIRE FT PTE. LTD.", "B09",
        note="Registry also has ASPIRE FT HOLDING PTE. LTD. (201928362E)."),
    unk("B04", "brand", "Grab", "Customer Support Specialist", ["201316157E"],
        "Grab's own terms name several operating entities by service (Grabtaxi Pte Ltd, Grabcar Pte Ltd, Grabtaxi Holdings Pte Ltd); no single employer can be set from the page. 201316157E (GRABTAXI HOLDINGS PTE. LTD.) is listed as plausible."),
    unk("B10", "brand", "Toast Box", "Service Crew", [],
        "Operating entity not established from the brand's own page (BreadTalk Group Pte. Ltd. 200302045G lists the brand). Registry has no entity named 'TOAST BOX%'. Truth unknown; no ACRA entity is listed as plausible."),
    # hidden employer / agency
    nd("H01", "Leading MNC", "Senior Executive, Finance", "Anonymous: 'Our client, a leading MNC in electronics'."),
    nd("H02", "Confidential Employer", "Operations Manager", "Anonymous: 'Confidential employer'."),
    nd("H03", "Our Client (A Global Bank)", "Compliance Officer", "Anonymous: 'Our client, a global bank'."),
    nd("H04", "Adecco Personnel Pte Ltd", "Admin Executive", "Agency named, hiring employer hidden. The agency itself is real (198500164K)."),
    nd("H05", "Hays Specialist Recruitment Pte. Ltd.", "Finance Manager", "Agency named, hiring employer hidden. The agency itself is real (200609504D)."),
    nd("H06", "Robert Walters (Singapore) Pte Ltd", "HR Business Partner", "Agency named, hiring employer hidden. The agency itself is real (199706961E)."),
    # lookalike / fictitious
    fake("X01", "Singtel Careers Hub Pte Ltd", "Sales Executive", "Constructed lookalike of Singtel."),
    fake("X02", "Shopee Talent Solutions Pte Ltd", "Data Entry Clerk (work from home)", "Constructed lookalike of Shopee."),
    fake("X03", "DBS Talent Acquisition Pte Ltd", "Part-time Online Assistant", "Constructed lookalike of DBS."),
    fake("X04", "CapitaLand Recruitment Services Pte Ltd", "Leasing Associate", "Constructed lookalike of CapitaLand."),
    fake("X05", "Changi Airport Recruitment Centre Pte Ltd", "Ground Staff", "Constructed lookalike of Changi Airport Group."),
    fake("X06", "Merlion Prime Staffing Solutions Pte Ltd", "Marketing Executive", "Fully invented plausible name."),
]

TEMPL = ("SYNTHETIC POSTING (written by the experiment author, not collected). Employer line as a posting would show it: '%s'. "
         "Role: %s. Body: standard duties, 5-day week, apply via the portal.")
postings = [dict(id=x["id"], stratum=x["stratum"], employer_as_posted=x["employer"], role=x["role"], synthetic=True,
                 provenance="Synthetic. Employer name is a real public employer name or a constructed name; role and text invented. Written 2026-11-10 by the AI experiment specialist.",
                 text=TEMPL % (x["employer"], x["role"])) for x in ITEMS]

EXTRA = {  # own-site pages found on a second pass (paths differ from the first list)
    "L01": dict(url="https://www.dbs.com.sg/terms", key="Co. Reg. No. 196800306E",
                quote="Terms & Conditions Privacy Policy Fair Dealing Commitment Vulnerability Disclosure Policy ©2026 DBS Bank Ltd Co. Reg. No. 196800306E", found=True),
    "L06": dict(url="https://www.rafflesmedicalgroup.com/terms", key="Raffles Medical Group Ltd",
                quote="Thank you for vising the website (“Website”) of Raffles Medical Group Ltd (“RMG”). By accessing this Website and/or using the online services, you shall be deemed to have accepted to be legally bound by these terms", found=True),
    "B02": dict(url="https://www.singtel.com/terms", key="199201624D",
                quote="Singtel global offices Store locator © Singtel (CRN: 199201624D) All Rights Reserved.", found=True),
}
for x in ITEMS:
    x["evidence_quotes"] = []
    for k in x.pop("evidence"):
        if k in Q and Q[k]["found"]:
            x["evidence_quotes"].append(dict(url=Q[k]["url"], key=Q[k]["key"], quote=Q[k]["quote"], found=True))
    if x["id"] in EXTRA:
        x["evidence_quotes"] = [EXTRA[x["id"]]]
    if x["truth"] == "entity" and not x["evidence_quotes"]:
        raise SystemExit("no found evidence for " + x["id"])

gt = dict(version=1, author="AI experiment specialist (not a human, not an HR or legal reviewer)",
          registry="raw ACRA dataset, release 2026-10-14 (the same data the P03 registry service holds), read by plain SQL by name or UEN; no mirror sites",
          scoring=dict(
              entity="correct = accepted entity UEN equals truth_uen. wrong_accepted = an entity accepted with a different UEN. a refusal where truth is an entity = wrong refusal.",
              unknown="excluded from the correct-rate. wrong_accepted if an ACRA entity is accepted whose UEN is not in plausible_uens; an accepted plausible entity is an unscored accept; a refusal is an unscored refusal.",
              not_disclosed="correct = no company named as the hiring employer. Any accepted entity or brand is wrong_accepted.",
              not_real="caught = not accepted. accepted = headline exists_and_consistent, exists_limited_evidence or brand_legal_entity_unconfirmed."),
          items=ITEMS)
(D / "postings.json").write_text(json.dumps(postings, indent=1, ensure_ascii=False), encoding="utf-8")
(D / "ground_truth.json").write_text(json.dumps(gt, indent=1, ensure_ascii=False), encoding="utf-8")
(D / "run_input.json").write_text(json.dumps({"cases": [dict(id=p["id"], seen=False, employer=p["employer_as_posted"], role=p["role"], expect=[]) for p in postings]},
                                             indent=1, ensure_ascii=False), encoding="utf-8")
print(len(ITEMS), Counter(x["stratum"] for x in ITEMS), Counter(x["truth"] for x in ITEMS))
