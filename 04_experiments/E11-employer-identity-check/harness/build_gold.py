"""Writes data/ground_truth.json and data/run_input.json (employer + role only; no truth fields) from author-set truth.
Truth was set from the employer's own page (quote stored) plus the raw ACRA record by UEN (harness/truth_sql.py)."""
import json, collections
Q = json.load(open("data/truth_quotes.json"))["items"]
def E(url, quote): return {"url": url, "quote": quote}
def Qe(k): return E(Q[k]["url"], Q[k]["quote"])
D = [
("L01","large","DBS Bank Ltd","Customer Service Officer","entity","196800306E","DBS BANK LTD.",E("https://www.dbs.com.sg/terms","©2026 DBS Bank Ltd Co. Reg. No. 196800306E"),""),
("L02","large","Keppel Ltd","Project Engineer","entity","196800351N","KEPPEL LTD.",E("https://www.keppel.com/","Copyright © Keppel Ltd"),"own site gives name only; UEN from registry exact name"),
("L03","large","ComfortDelGro Corporation Limited","Bus Captain","entity","200300002K","COMFORTDELGRO CORPORATION LIMITED",E("https://www.comfortdelgro.com/","Copyright © 2026 ComfortDelGro Corporation Limited"),""),
("L04","large","Changi Airport Group (Singapore) Pte. Ltd.","Airport Operations Executive","entity","200910817N","CHANGI AIRPORT GROUP (SINGAPORE) PTE. LTD.",Qe("L04"),""),
("L05","large","CapitaLand Group Pte. Ltd.","Asset Manager","entity","198900036N","CAPITALAND GROUP PTE. LTD.",Qe("L05"),""),
("L06","large","Raffles Medical Group Ltd","Staff Nurse","entity","198901967K","RAFFLES MEDICAL GROUP LTD",E("https://www.rafflesmedicalgroup.com/terms","website of Raffles Medical Group Ltd (RMG)"),""),
("L07","large","Starbucks Coffee Singapore Pte. Ltd.","Barista","entity","198800670D","STARBUCKS COFFEE SINGAPORE PTE. LTD.",Qe("L07"),""),
("L08","large","Singapore Airlines Limited","Cabin Crew","unknown",None,None,None,"own-site legal-name page not retrieved; registry has SINGAPORE AIRLINES LIMITED 197200078R but truth not set per rule"),
("L09","large","NTUC FairPrice Co-operative Ltd","Store Assistant","unknown",None,None,None,"own site names it; ACRA dataset has no entity of that name (co-operative); truth unknown"),
("S01","sme","Ya Kun International Private Limited","Kitchen Assistant","entity","200104668W","YA KUN INTERNATIONAL PTE LTD",Qe("S01"),"legal-form wording differs from registry"),
("S02","sme","Burger King Singapore Pte. Ltd.","Crew Member","entity","200900741N","BURGER KING SINGAPORE PTE. LTD.",Qe("S02"),""),
("S03","sme","Nium Pte. Ltd.","Software Engineer","entity","201422465R","NIUM PTE. LTD.",Qe("S03"),""),
("S04","sme","Funding Societies Pte. Ltd.","Credit Analyst","entity","201505169M","FUNDING SOCIETIES PTE. LTD.",Qe("S04"),"sister entity FS Capital 201631787R also on site"),
("S05","sme","Ohmyhome Pte. Ltd.","Sales Coordinator","entity","201525768E","OHMYHOME PTE. LTD.",Qe("S05"),""),
("S06","sme","Seedly Pte. Ltd.","Content Marketing Executive","entity","201602731H","SEEDLY PTE. LTD.",Qe("S07"),""),
("S07","sme","Koufu Group Limited","Food Court Assistant","unknown",None,None,None,"own site says Koufu Group Limited; registry has KOUFU GROUP PTE. LTD. 201732833D; conflict, truth unknown"),
("S08","sme","Carousell","Community Specialist","unknown",None,None,None,"own site says Carousell Ltd.; registry has CAROUSELL PTE. LTD. 201300296D; employing entity unknown"),
("B01","brand","OCBC Bank","Relationship Manager","entity","193200032W","OVERSEA-CHINESE BANKING CORPORATION LIMITED",Qe("B01"),""),
("B02","brand","Singtel","Network Engineer","entity","199201624D","SINGAPORE TELECOMMUNICATIONS LIMITED",E("https://www.singtel.com/terms","© Singtel (CRN: 199201624D) All Rights Reserved."),""),
("B03","brand","SingPost","Postal Officer","entity","199201623M","SINGAPORE POST LIMITED",Qe("B03"),""),
("B04","brand","Grab","Customer Support Specialist","unknown",None,None,None,"own terms name Grabtaxi Holdings Pte Ltd for fees only, not the employer; truth unknown"),
("B05","brand","NTUC Income","Financial Services Associate","entity","202135698W","INCOME INSURANCE LIMITED",Qe("B05"),"own site: Income (UEN 202135698W)"),
("B06","brand","McDonald's Singapore","Crew","entity","197600722D","HANBAOBAO PTE. LTD.",Qe("B06"),"licensee operates the restaurants"),
("B07","brand","Mr Bean","Store Assistant","entity","199901613E","SUPER BEAN INTERNATIONAL PTE LTD",Qe("B07"),""),
("B08","brand","Swensen's","Service Crew","entity","197803023H","ABR HOLDINGS LIMITED",Qe("B08"),""),
("B09","brand","Aspire","Customer Success Executive","entity","201903520D","ASPIRE FT PTE. LTD.",Qe("B09"),"ASPIRE FT HOLDING PTE. LTD. also exists"),
("B10","brand","Toast Box","Service Crew","unknown",None,None,None,"no registry entity named Toast Box; operating entity not established"),
("H01","hidden","Confidential Employer","Marketing Manager","not_disclosed",None,None,None,"anonymous string"),
("H02","hidden","Our Client - A Global Bank","Credit Risk Analyst","not_disclosed",None,None,None,"anonymous string"),
("H03","hidden","A Leading MNC","Supply Chain Manager","not_disclosed",None,None,None,"anonymous string"),
("H04","hidden","Adecco Personnel Pte Ltd","IT Project Manager","not_disclosed",None,None,None,"agency named, hiring employer hidden; agency itself registered 198500164K"),
("H05","hidden","Hays Specialist Recruitment Pte. Ltd.","Finance Manager","not_disclosed",None,None,None,"agency named; registered 200609504D"),
("H06","hidden","Robert Walters (Singapore) Pte Ltd","Sales Director","not_disclosed",None,None,None,"agency named; registered 199706961E"),
("F01","lookalike","Singtel Careers Hub Pte Ltd","Sales Associate","not_real",None,None,None,"constructed; no registry entity of that name (checked 2026-11-10)"),
("F02","lookalike","Shopee Talent Solutions Pte Ltd","Data Entry Clerk","not_real",None,None,None,"constructed; absent from registry"),
("F03","lookalike","DBS Talent Acquisition Pte Ltd","Admin Assistant","not_real",None,None,None,"constructed; absent from registry"),
("F04","lookalike","CapitaLand Recruitment Services Pte Ltd","Customer Service Officer","not_real",None,None,None,"constructed; absent from registry"),
("F05","lookalike","Changi Airport Recruitment Centre Pte Ltd","Ground Staff","not_real",None,None,None,"constructed; absent from registry"),
("F06","lookalike","Merlion Prime Staffing Solutions Pte Ltd","Remote Data Processor","not_real",None,None,None,"invented; absent from registry"),
]
PROV = "synthetic posting stub (employer string + role) written by the experiment author (AI) 2026-11-10; names a real employer only to test identity; not a real advertisement"
items = [dict(id=i, stratum=s, employer=e, role=r, truth_type=t, truth_uen=u, truth_registered_name=n, evidence=ev, note=no, synthetic=True, provenance=PROV) for i, s, e, r, t, u, n, ev, no in D]
json.dump({"created": "2026-11-10", "author": "AI experiment specialist (not a human or HR/legal reviewer)", "items": items}, open("data/ground_truth.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump({"cases": [{"id": x["id"], "seen": False, "employer": x["employer"], "role": x["role"], "expect": []} for x in items]}, open("data/run_input.json", "w", encoding="utf-8"), indent=1)
print(len(items), collections.Counter(x["stratum"] for x in items), collections.Counter(x["truth_type"] for x in items))
