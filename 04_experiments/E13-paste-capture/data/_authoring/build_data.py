"""Authoring script for the E13 synthetic pastes and gold labels. Run once; outputs are then frozen.

All postings are invented (fictional employers, synthetic: true). Layouts imitate how text looks when a
person selects a whole page and copies it. Gold labels are the author's declarations in SPECS and are
written here, not derived from the snapshot step (which does not exist when this runs).
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
(OUT / "pastes").mkdir(exist_ok=True)

NB = " "
ZW = "​"

# ------------------------------------------------------------------------------------------------
# Specs. state keys: employer in {present, hidden_labelled, missing}; pay/closing in {present,
# explicit_absence, missing}. *_line is the exact text shown in the paste for that field (None = absent).
# ------------------------------------------------------------------------------------------------
def S(**k):
    k.setdefault("noise", [])
    k.setdefault("crlf", False)
    k.setdefault("closing_iso", None)
    k.setdefault("level", "Executive")
    return k

SPECS = [
 # ---------------- MyCareersFuture (9) ----------------
 S(id="P01", board="mcf", jtype="professional", title="Senior Accountant", employer_state="present",
   employer_line="Harbourline Advisory Pte Ltd", loc="Robinson Road, CBD", etype="Full Time", level="Senior Executive",
   pay_state="present", pay_line="$6,500 to $8,500", closing_state="present",
   closing_line="Closing on 5 Dec 2026", closing_iso="2026-12-05", posted="Posted 3 Nov 2026", captured="2026-11-10T09:12:00+08:00",
   duties=["Prepare monthly management accounts and consolidations for three regional entities", "Lead the year-end audit and liaise with external auditors", "Review GST filings and corporate tax computations", "Mentor two junior accountants"],
   reqs=["Degree in Accountancy; CPA or ACCA preferred", "At least 6 years of experience, including audit or a shared-services environment", "Strong Excel and an ERP such as NetSuite"],
   noise=["cookie", "badge"]),
 S(id="P02", board="mcf", jtype="clerical", title="Administrative Assistant", employer_state="present",
   employer_line="Greenfold Logistics Pte Ltd", loc="Tuas South Avenue 6", etype="Full Time", level="Junior Executive",
   pay_state="present", pay_line="$2,400 to $3,000", closing_state="present",
   closing_line="Closing on 20 Nov 2026", closing_iso="2026-11-20", posted="Posted 28 Oct 2026", captured="2026-11-09T18:40:00+08:00",
   duties=["Handle incoming calls, emails and courier bookings", "Prepare delivery orders, invoices and purchase requisitions", "Maintain filing and vendor records", "Support the operations manager with weekly reports"],
   reqs=["GCE O level or diploma", "1 year of office administration experience", "Able to work from 8.30am to 5.30pm, Monday to Friday"],
   noise=["similar", "badge"]),
 S(id="P03", board="mcf", jtype="manual", title="Warehouse Assistant (Shift)", employer_state="present",
   employer_line="Eastgate Cold Chain Pte Ltd", loc="Pandan Crescent", etype="Full Time", level="Non-executive",
   pay_state="present", pay_line="$2,200 to $2,800", closing_state="present",
   closing_line="Closing on 30 Nov 2026", closing_iso="2026-11-30", posted="Posted 1 Nov 2026", captured="2026-11-10T07:55:00+08:00",
   duties=["Receive, check and put away chilled and frozen goods", "Pick and pack orders using a handheld scanner", "Operate a reach truck (training provided)", "Keep the cold room clean and report temperature faults"],
   reqs=["Able to work rotating 12-hour shifts, including weekends", "Comfortable in cold storage (-18 degrees Celsius)", "Forklift licence is an advantage"],
   noise=["similar"]),
 S(id="P04", board="mcf", jtype="contract", title="Project Coordinator (12-month contract)", employer_state="present",
   employer_line="Meridian Civil Works Pte Ltd", loc="Jurong East Street 21", etype="Contract", level="Executive",
   pay_state="present", pay_line="$3,800 to $4,500", closing_state="present",
   closing_line="Closing on 6 Nov 2026", closing_iso="2026-11-06", posted="Posted 20 Oct 2026", captured="2026-11-02T13:05:00+08:00",
   duties=["Track project schedules, submissions and site instructions", "Prepare progress claims and variation order summaries", "Coordinate meetings between consultants and subcontractors", "Maintain the document control register"],
   reqs=["Diploma in Civil Engineering, Building or related", "2 years of experience in construction project administration", "Proficient in MS Project and Excel"]),
 S(id="P05", board="mcf", jtype="part-time", title="Part-Time Library Assistant", employer_state="present",
   employer_line="Parkview Community Services", loc="Bishan", etype="Part Time", level="Non-executive",
   pay_state="present", pay_line="$13 to $15 Hourly", closing_state="present",
   closing_line="Closing on 25 Nov 2026", closing_iso="2026-11-25", posted="Posted 4 Nov 2026", captured="2026-11-10T10:30:00+08:00",
   duties=["Shelve and tidy books and magazines", "Assist members with borrowing and returns at the counter", "Help run weekend reading sessions for children"],
   reqs=["Friendly and patient with children and seniors", "Able to work 16 hours a week including Saturday mornings", "Basic computer skills"], crlf=True),
 S(id="P06", board="mcf", jtype="professional", title="Data Analyst", employer_state="hidden_labelled",
   employer_line="Hiring company: Confidential (advertised by Brightway Talent Pte Ltd)", loc="Central", etype="Permanent", level="Executive",
   pay_state="present", pay_line="$4,500 to $6,000", closing_state="present",
   closing_line="Closing on 12 Dec 2026", closing_iso="2026-12-12", posted="Posted 6 Nov 2026", captured="2026-11-10T11:20:00+08:00",
   duties=["Build dashboards in Power BI for the commercial team", "Clean and reconcile sales data from three source systems", "Answer ad hoc questions from finance and marketing", "Document data definitions"],
   reqs=["Degree in Statistics, Data Science, Business or related", "2 to 4 years of SQL and Power BI experience", "Clear written English"], noise=["badge"]),
 S(id="P07", board="mcf", jtype="clerical", title="Customer Service Officer", employer_state="present",
   employer_line="Sunrise Telecom Services Pte Ltd", loc="Paya Lebar", etype="Full Time", level="Junior Executive",
   pay_state="present", pay_line="$2,600 to $3,200", closing_state="present",
   closing_line="Closing on 18 Nov 2026", closing_iso="2026-11-18", posted="Posted 2 Nov 2026", captured="2026-11-08T21:15:00+08:00",
   duties=["Respond to customer calls, chats and emails on billing and plan changes", "Log cases and escalate complex issues", "Meet monthly service quality targets"],
   reqs=["Good spoken English and Mandarin or Malay", "Shift work including some weekends", "Prior call centre experience is an advantage"], noise=["mixed"]),
 S(id="P08", board="mcf", jtype="professional", title="Software Engineer (Backend)", employer_state="present",
   employer_line="Quillstone Systems Pte Ltd", loc="one-north", etype="Permanent", level="Executive",
   pay_state="missing", pay_line=None, closing_state="missing", closing_line=None, posted=None, captured="2026-11-09T09:00:00+08:00",
   duties=["Design and build REST services in Java and Spring Boot", "Write unit and integration tests and review pull requests", "Support the production on-call rotation one week in six", "Work with product managers to refine requirements"],
   reqs=["Degree in Computer Science or equivalent experience", "3 or more years of backend development", "Familiar with Docker, PostgreSQL and a cloud provider"],
   noise=["head_trim"]),
 S(id="P09", board="mcf", jtype="gig", title="Freelance Event Crew" + ZW, employer_state="present",
   employer_line="Spotlight Event Services", loc="Various locations", etype="Freelance", level="Non-executive",
   pay_state="present", pay_line="$120 to $150 Daily", closing_state="present",
   closing_line="Closing on 18 Nov 2026", closing_iso="2026-11-18", posted="Posted 5 Nov 2026", captured="2026-11-10T16:45:00+08:00",
   duties=["Set up and dismantle stages, booths and signage", "Assist with crowd flow and guest registration", "Follow the event supervisor's instructions"],
   reqs=["Able to lift 15 kg", "Available for at least 3 events a month, many on weekends", "Own transport for early morning call times"], pay_nb=True),
 # ---------------- JobStreet (8) ----------------
 S(id="P10", board="jobstreet", jtype="professional", title="Marketing Executive", employer_state="present",
   employer_line="Lumen & Pine Pte Ltd", loc="Kallang, Singapore", etype="Full time", level="Junior",
   pay_state="missing", pay_line=None, closing_state="missing", closing_line=None, posted="Posted 4d ago", captured="2026-11-08T12:10:00+08:00",
   duties=["Plan and publish content on Instagram, TikTok and LinkedIn", "Coordinate photo shoots and influencer collaborations", "Track campaign results and report monthly", "Support retail promotions with the sales team"],
   reqs=["Degree or diploma in Marketing or Communications", "1 to 2 years of social media experience", "Portfolio of content work is a plus"], noise=["badge"]),
 S(id="P11", board="jobstreet", jtype="manual", title="Cleaner (Shopping Mall)", employer_state="hidden_labelled",
   employer_line="Private Advertiser", loc="Tampines, Singapore", etype="Full time", level="Entry",
   pay_state="present", pay_line="$1,900 - $2,300 per month", closing_state="present",
   closing_line="Applications close on 28 Nov 2026.", closing_iso="2026-11-28", posted="Posted 2d ago", captured="2026-11-10T08:05:00+08:00",
   duties=["Clean common areas, toilets and food court tables", "Empty bins and replenish toilet supplies", "Operate a floor scrubber after training"],
   reqs=["Able to stand and walk for long periods", "Shift work: 7am to 4pm or 1pm to 10pm", "Singaporeans and PRs preferred; work permit holders may apply"]),
 S(id="P12", board="jobstreet", jtype="clerical", title="HR Admin Assistant", employer_state="present",
   employer_line="Oakridge Facilities Management", loc="Ubi, Singapore", etype="Full time", level="Entry",
   pay_state="present", pay_line=f"S${NB}2,800{NB}-{NB}S${NB}3,400 per month", closing_state="missing", closing_line=None, posted="Posted 5d ago", captured="2026-11-09T14:20:00+08:00",
   duties=["Maintain employee records and update the HRIS", "Prepare employment contracts and onboarding packs", "Process claims and leave applications", "Assist with recruitment scheduling and interview arrangements"],
   reqs=["Diploma in Human Resource or Business Administration", "Experience with payroll is an advantage", "Meticulous and able to keep information confidential"], noise=["cookie"]),
 S(id="P13", board="jobstreet", jtype="contract", title="Business Development Manager (Contract)", employer_state="present",
   employer_line="Atlas Freight Solutions", loc="Changi, Singapore", etype="Contract/Temp", level="Mid-Senior",
   pay_state="explicit_absence", pay_line="Salary negotiable depending on experience", closing_state="explicit_absence", closing_line="This role is open until filled.", posted="Posted 6d ago", captured="2026-11-07T10:00:00+08:00",
   duties=["Grow air and sea freight accounts in the electronics sector", "Prepare quotations and negotiate rates with carriers", "Visit key accounts and report the pipeline weekly"],
   reqs=["5 years of freight forwarding sales", "Existing customer network in Singapore and Malaysia", "Contract of 9 months with possible extension"]),
 S(id="P14", board="jobstreet", jtype="part-time", title="Part-time Barista", employer_state="present",
   employer_line="Cedar Bean Coffee Co", loc="Orchard, Singapore", etype="Part time", level="Entry",
   pay_state="present", pay_line="$11 - $13 per hour", closing_state="missing", closing_line=None, posted="Posted 1d ago", captured="2026-11-10T09:40:00+08:00",
   duties=["Prepare espresso drinks and filter coffee to recipe", "Take orders and handle payments", "Keep the bar and storage tidy and follow food hygiene rules"],
   reqs=["Minimum 3 shifts per week, including one weekend day", "Barista experience is an advantage but training is provided", "Positive and reliable"], crlf=True),
 S(id="P15", board="jobstreet", jtype="gig", title="Weekend Delivery Rider (Self-employed)", employer_state="present",
   employer_line="Swiftdrop Pte Ltd", loc="Island-wide", etype="Casual/Vacation", level="Entry",
   pay_state="present", pay_line="Earn up to $18 per hour", closing_state="explicit_absence", closing_line="Ongoing recruitment, no closing date.", posted="Posted 8d ago", captured="2026-11-02T11:30:00+08:00",
   duties=["Pick up and deliver food and parcels using the Swiftdrop app", "Choose your own hours and zones", "Keep the delivery bag clean"],
   reqs=["Own bicycle, e-bike or motorcycle with valid licence", "Smartphone with data plan", "Rider insurance details provided at onboarding"]),
 S(id="P16", board="jobstreet", jtype="professional", title="Operations Analyst", employer_state="present",
   employer_line="Riverbend Insurance (Singapore)", loc="Raffles Place, Singapore", etype="Full time", level="Junior",
   pay_state="missing", pay_line=None, closing_state="present", closing_line="Apply before 30 Nov 2026.", closing_iso="2026-11-30", posted="Posted 3d ago", captured="2026-11-10T13:25:00+08:00",
   duties=["Monitor claims processing queues and flag delays", "Produce weekly service level reports", "Recommend process improvements with the claims team"],
   reqs=["Degree in Business, Mathematics or Economics", "Proficiency in Excel; SQL is an advantage", "Interest in insurance operations"], noise=["tail_trim"]),
 S(id="P17", board="jobstreet", jtype="clerical", title="Receptionist", employer_state="present",
   employer_line="Willowbrook Dental Group", loc="Bukit Timah, Singapore", etype="Full time", level="Entry",
   pay_state="missing", pay_line=None, closing_state="missing", closing_line=None, posted="Posted 7d ago", captured="2026-11-03T15:50:00+08:00",
   duties=["Greet patients and manage appointments", "Handle phone calls, payments and insurance claims", "Prepare patient files and maintain the reception area"],
   reqs=["Pleasant and presentable", "Basic knowledge of Excel and Word", "Able to work Saturdays on a rotation"], noise=["similar", "badge"]),
 # ---------------- FastJobs (6) ----------------
 S(id="P18", board="fastjobs", jtype="manual", title="Warehouse Packer" + ZW, employer_state="present",
   employer_line="Orbitrade Fulfilment", loc="Woodlands", etype="Full-time", level="Entry",
   pay_state="present", pay_line="$11/hr", closing_state="missing", closing_line=None, posted="Posted 1 day ago", captured="2026-11-10T07:30:00+08:00",
   duties=["Pick, pack and label parcels", "Check stock against the packing list", "Move cartons by hand or pallet jack"],
   reqs=["Can start immediately", "Able to work 6 days a week, 8 hours a day", "No experience needed"], noise=["urgent"]),
 S(id="P19", board="fastjobs", jtype="manual", title="F&B Service Crew", employer_state="present",
   employer_line="Kopi Corner (3 outlets)", loc="Jurong, Clementi, Bedok", etype="Full-time / Part-time", level="Entry",
   pay_state="present", pay_line="$10 - $12/hr", closing_state="explicit_absence", closing_line="Hiring until positions are filled", posted="Posted 3 days ago", captured="2026-11-08T17:00:00+08:00",
   duties=["Take orders and serve food and drinks", "Clear and clean tables", "Help the kitchen with simple prep when it is quiet"],
   reqs=["Friendly and quick learner", "Able to work weekends", "Meals provided on shift"], noise=["urgent"]),
 S(id="P20", board="fastjobs", jtype="gig", title="Event Usher (1-day)", employer_state="present",
   employer_line="Sparkline Events", loc="Marina Bay Sands Expo", etype="Temporary", level="Entry",
   pay_state="present", pay_line="$90/day", closing_state="present", closing_line="Event date: 22 Nov 2026. Apply by 18 Nov 2026.", closing_iso="2026-11-18", posted="Posted 2 days ago", captured="2026-11-09T12:00:00+08:00",
   duties=["Guide visitors to the correct halls", "Hand out programme booklets", "Answer basic questions at the information counter"],
   reqs=["Smart casual attire, black shoes", "8 hour shift with a meal break", "Singapore Citizen, PR or student pass holders only"]),
 S(id="P21", board="fastjobs", jtype="part-time", title="Retail Assistant (Weekends)", employer_state="hidden_labelled",
   employer_line="Company: Retail Brand (name shown after you apply)", loc="Vivocity", etype="Part-time", level="Entry",
   pay_state="present", pay_line="$10.50/hr", closing_state="missing", closing_line=None, posted="Posted 6 days ago", captured="2026-11-06T19:10:00+08:00",
   duties=["Welcome customers and assist with fitting rooms", "Replenish stock and keep displays neat", "Operate the cash register"],
   reqs=["Saturday and Sunday availability, 10am to 10pm shifts", "Customer-oriented", "Retail experience preferred"]),
 S(id="P22", board="fastjobs", jtype="manual", title="Security Officer", employer_state="present",
   employer_line="Bastion Guard Services", loc="Various sites", etype="Full-time", level="Entry",
   pay_state="present", pay_line="$2,300 - $2,900 per month", closing_state="present", closing_line="Closing date: 30 Nov 2026", closing_iso="2026-11-30", posted="Posted 4 days ago", captured="2026-11-10T10:10:00+08:00",
   duties=["Patrol the premises and check access passes", "Record incidents in the occurrence log", "Respond to alarms and escalate to the supervisor"],
   reqs=["Valid PLRD security officer certificate", "12-hour shifts, 6 days a week with overtime", "Singaporeans or PRs only"], crlf=True),
 S(id="P23", board="fastjobs", jtype="clerical", title="Data Entry Clerk (Temp)", employer_state="missing",
   employer_line=None, loc="Kallang", etype="Temporary", level="Entry",
   pay_state="present", pay_line="$12.50/hr", closing_state="missing", closing_line=None, posted="Posted 2 days ago", captured="2026-11-09T09:25:00+08:00",
   duties=["Key invoice and delivery data into the company system", "Check entries against source documents", "File documents in date order"],
   reqs=["Typing speed of 35 words per minute or better", "3-month contract", "Detail oriented"], noise=["head_trim_employer"]),
 # ---------------- Company career pages (7) ----------------
 S(id="P24", board="company", jtype="professional", title="Product Designer", employer_state="present",
   employer_line="Tidewater Labs", loc="Singapore (hybrid)", etype="Full-time", level="",
   pay_state="missing", pay_line=None, closing_state="present", closing_line="Applications close 4 December 2026", closing_iso="2026-12-04", posted=None, captured="2026-11-07T20:00:00+08:00",
   duties=["Design flows and interfaces for our logistics dashboard", "Run research sessions with warehouse operators", "Work in Figma with engineers and ship weekly", "Maintain and extend the design system"],
   reqs=["3 or more years in product or UX design", "A portfolio showing end-to-end work", "Comfortable with data-dense interfaces"], noise=["cookie"]),
 S(id="P25", board="company", jtype="professional", title="Senior Data Engineer", employer_state="present",
   employer_line="Kestrel Payments", loc="Singapore", etype="Full-time", level="",
   pay_state="explicit_absence", pay_line="Salary: not published on this page, discussed at interview", closing_state="explicit_absence", closing_line="We review applications on a rolling basis.", posted=None, captured="2026-11-05T15:15:00+08:00",
   duties=["Build batch and streaming pipelines on our data platform", "Own data quality checks and alerting", "Partner with risk and fraud analysts on feature tables"],
   reqs=["5 years of data engineering, Python and SQL", "Experience with Kafka or similar", "Knowledge of payments data is helpful"]),
 S(id="P26", board="company", jtype="manual", title="Kitchen Assistant", employer_state="present",
   employer_line="Marlowe Hotels", loc="Sentosa", etype="Full-time", level="",
   pay_state="present", pay_line="$2,000 basic plus service charge", closing_state="present", closing_line="Closing date: 27 Nov 2026", closing_iso="2026-11-27", posted=None, captured="2026-11-10T08:40:00+08:00",
   duties=["Wash, peel and cut ingredients for the hotel kitchens", "Keep stations and equipment clean to hygiene standards", "Support the chefs during banquets"],
   reqs=["Able to work shifts including public holidays", "Basic food hygiene certificate (can be obtained after joining)", "Hotel discount and staff meals"]),
 S(id="P27", board="company", jtype="clerical", title="Finance Admin Executive (6-month contract)", employer_state="present",
   employer_line="Ironwood Holdings", loc="Singapore", etype="Contract", level="",
   pay_state="missing", pay_line=None, closing_state="missing", closing_line=None, posted=None, captured="2026-11-06T09:55:00+08:00",
   duties=["Process supplier invoices and payments", "Reconcile bank statements monthly", "Assist with petty cash and expense claims"],
   reqs=["Diploma in Accounting", "1 year of accounts payable experience", "Able to start within one month"]),
 S(id="P28", board="company", jtype="contract", title="Site Safety Officer (Contract)", employer_state="present",
   employer_line="Delta Marine Engineering", loc="Tuas Shipyard", etype="Contract", level="",
   pay_state="present", pay_line="$3,600 - $4,200 per month", closing_state="present", closing_line="Closing date: 15/12/2026", closing_iso="2026-12-15", posted=None, captured="2026-11-10T14:00:00+08:00",
   duties=["Conduct daily site inspections and toolbox talks", "Investigate incidents and prepare reports for the safety manager", "Check permits to work for hot work and confined spaces"],
   reqs=["Workplace Safety and Health Coordinator or equivalent", "3 years in a shipyard or construction site", "Contract of 12 months"]),
 S(id="P29", board="company", jtype="professional", title="Customer Success Manager", employer_state="present",
   employer_line="Nimbus Cloud Software", loc="Singapore", etype="Full-time", level="",
   pay_state="present", pay_line="SGD 5,500 - 7,000 per month", closing_state="present", closing_line="Closing in 9 days", closing_iso="2026-11-19", posted=None, captured="2026-11-10T09:30:00+08:00",
   duties=["Onboard new enterprise customers and drive adoption", "Run quarterly business reviews and renewals", "Act as the voice of the customer to product teams"],
   reqs=["4 years in customer success or account management for SaaS", "Strong presentation skills", "Experience with a CRM"], noise=["cookie", "dup"]),
 S(id="P30", board="company", jtype="part-time", title="Tuition Centre Administrator (Part-time)", employer_state="present",
   employer_line="Brightpath Learning Centre", loc="Hougang", etype="Part-time", level="",
   pay_state="present", pay_line="$14 per hour", closing_state="present", closing_line="Applications close 20 Nov 2026", closing_iso="2026-11-20", posted=None, captured="2026-11-04T16:20:00+08:00",
   duties=["Register students and collect fees", "Answer parent enquiries by phone and WhatsApp", "Prepare class materials and attendance sheets"],
   reqs=["Weekdays 2pm to 9pm and Saturday mornings", "Friendly with parents and children", "Basic Excel"]),
]

# ------------------------------------------------------------------------------------------------
# Renderers
# ------------------------------------------------------------------------------------------------
def bullets(items, mark):
    return [f"{mark}{x}" if mark else x for x in items]


def pay_text(s):
    t = s["pay_line"]
    if t and s.get("pay_nb"):
        t = t.replace(" to ", f"{NB}to{NB}")
    return t


def r_mcf(s):
    L = []
    if "cookie" in s["noise"]:
        L += ["We use cookies to improve your experience. By continuing to use this site you agree to our Privacy Statement.", "Accept all", "Manage preferences", ""]
    L += ["Skip to main content", "MyCareersFuture", "Jobs", "Employers", "Career Resources", "Log in", "Sign up", ""]
    head = [s["title"]]
    if s["employer_line"]:
        head.append(s["employer_line"])
    head += [s["loc"], f"{s['etype']}", s["level"] if s["level"] else ""]
    head = [h for h in head if h]
    if "badge" in s["noise"]:
        head.insert(1, "New") if s["id"] == "P02" else head.append("Job Match: 78%")
    meta = []
    if s["closing_line"]:
        meta.append(s["closing_line"] + (" · " + s["posted"] if s["posted"] else ""))
    elif s["posted"]:
        meta.append(s["posted"])
    pay = [pay_text(s), "Monthly" if "Hourly" not in (s["pay_line"] or "") and "Daily" not in (s["pay_line"] or "") else ""] if s["pay_line"] else []
    pay = [p for p in pay if p]
    action = ["Apply now", "Save job", "Share"]
    desc = ["Job Description", "Roles & Responsibilities"] + s["duties"] + ["", "Requirements"] + s["reqs"] + ["", "Skills", "Communication · Teamwork · Problem solving", "", "Additional Information",
            f"Job Post ID: MCF-2026-{abs(hash(s['id'])) % 10**7 if False else 1000000 + int(s['id'][1:]) * 137}", f"Employment type: {s['etype']}"]
    about = ["", "About the company", "We are an established company hiring in Singapore. Learn more on our company page."] if s["employer_state"] == "present" else []
    sim = []
    if "similar" in s["noise"]:
        sim = ["", "Similar jobs", "Operations Executive", "Crestline Trading Pte Ltd", "$3,000 to $3,800 Monthly", "Closing on 22 Nov 2026", "Store Assistant", "Pioneer Mart Pte Ltd", "$2,000 to $2,500 Monthly", "Closing on 3 Dec 2026"]
    foot = ["", "About MyCareersFuture", "Terms of Use", "Privacy Statement", "Report this job", "© 2026 Government of Singapore"]
    if "mixed" in s["noise"]:
        body = desc + [""] + head + meta + pay + action + about + sim + foot
        return L[:8] + body if False else L + body
    if "head_trim" in s["noise"]:
        return desc + about + sim + foot  # user started copying at "Job Description"
    return L + head + meta + pay + action + [""] + desc + about + sim + foot


def r_jobstreet(s):
    L = []
    if "cookie" in s["noise"]:
        L += ["We use cookies to give you the best experience on JobStreet. Read our Cookie Policy.", "Accept", "Decline", ""]
    L += ["Skip to content", "JobStreet", "Find jobs", "Career advice", "Companies", "Sign in", "Employer site", "", "Back to search results", ""]
    head = [s["title"]]
    if s["employer_line"]:
        head.append(s["employer_line"])
    head += [s["loc"], s["etype"]]
    if s["pay_line"]:
        head.append(pay_text(s))
    if "badge" in s["noise"]:
        head += ["Be an early applicant" if s["id"] != "P17" else "Featured"]
    head += ["Quick apply", "Save", s["posted"] or ""]
    head = [h for h in head if h]
    duties = bullets(s["duties"], "• ")
    reqs = bullets(s["reqs"], "• ")
    desc = ["Job description", "Responsibilities:"] + duties + ["", "Requirements:"] + reqs
    if s["closing_line"]:
        desc += ["", s["closing_line"]]
    desc += ["", "Report this job", "Be careful: never pay money to get a job. Learn more about safety.", "",
             "Additional information", f"Career level: {s['level']}", f"Job type: {s['etype']}", "Job specializations: see listing", ""]
    comp = ["Company overview", "About us: " + (s["employer_line"] or "") if s["employer_state"] == "present" else "About us", ""] if s["employer_state"] == "present" else []
    sim = []
    if "similar" in s["noise"]:
        sim = ["Jobs you might like", "Dental Assistant", "Pearl Smiles Clinic", "Bukit Merah", "$2,300 - $2,800 per month", "Posted 2d ago",
               "Front Desk Officer", "Anchorpoint Property", "Tanjong Pagar", "$2,500 - $3,200 per month", "Posted 4d ago"]
    foot = ["", "About JobStreet", "Privacy", "Terms and conditions", "© 2026 JobStreet"]
    if "tail_trim" in s["noise"]:
        lines = L + head + [""] + desc
        end = lines.index("Report this job")
        return lines[:end - 2] if lines[end - 2] == "" else lines[:end]
    return L + head + [""] + desc + comp + sim + foot


def r_fastjobs(s):
    L = ["FastJobs", "Home", "Jobs", "Companies", "For Employers", "Login / Register", ""]
    if "urgent" in s["noise"]:
        L += ["URGENT HIRING", ""]
    L += [s["title"]]
    if s["employer_line"]:
        L.append(s["employer_line"])
    pay = [f"Pay: {pay_text(s)}"] if s["pay_line"] else []
    L += pay + [f"Location: {s['loc']}", f"Job type: {s['etype']}", s["posted"] or "", "12 people viewed this job", ""]
    L += ["Job Responsibilities:"] + bullets(s["duties"], "- ") + ["", "Requirements:"] + bullets(s["reqs"], "- ")
    how = ["", "How to apply", "Tap Apply Now or WhatsApp our recruiter."]
    if s["closing_line"]:
        how.append(s["closing_line"])
    how += ["Apply Now", "Save", ""]
    foot = ["Safety tip: never pay a fee to get a job.", "Terms", "Privacy", "© 2026 FastJobs"]
    out = L + how + foot
    if "head_trim_employer" in s["noise"]:
        out = [x for x in out if x != ""]
    return out


def r_company(s):
    L = []
    if "cookie" in s["noise"]:
        L += ["This website uses cookies. Accept all cookies?", "Accept", "Reject non-essential", ""]
    brand = s["employer_line"] or ""
    L += [brand, "About us", "Our culture", "Careers", "News", "Contact", "", "Back to all jobs", "", s["title"], f"Location: {s['loc']}", f"Employment: {s['etype']}"]
    if s["pay_line"]:
        L.append(f"Salary: {pay_text(s)}" if s["pay_state"] == "explicit_absence" else f"Compensation: {pay_text(s)}")
    if s["closing_line"]:
        L.append(s["closing_line"] if s["closing_state"] != "explicit_absence" else s["closing_line"])
    L += ["", "Apply for this job", ""]
    sec = ["Overview", f"Join {brand} and help us grow." if brand else "", "", "What you'll do"] + bullets(s["duties"], "") + ["", "What you'll bring"] + bullets(s["reqs"], "")
    sec += ["", "Benefits", "Annual leave, medical insurance, training budget", "", "Equal opportunity employer."]
    foot = ["", "Share this job: LinkedIn · Facebook · Email", "Privacy policy", f"© 2026 {brand}"]
    out = L + sec + foot
    if "dup" in s["noise"]:
        out = out + ["", "---"] + L[-3:] + sec[:7]  # copied the overview/duties area twice
    return out


RENDER = {"mcf": r_mcf, "jobstreet": r_jobstreet, "fastjobs": r_fastjobs, "company": r_company}


def to_text(lines, crlf):
    txt = "\n".join(lines)
    while "\n\n\n" in txt:
        txt = txt.replace("\n\n\n", "\n\n")
    if crlf:
        txt = txt.replace("\n", "\r\n")
    return txt


texts = {}
labels = []
for s in SPECS:
    texts[s["id"]] = to_text(RENDER[s["board"]](s), s["crlf"])
    labels.append({
        "id": s["id"], "synthetic": True, "set": "complete30", "board": s["board"], "job_type": s["jtype"],
        "captured_at": s["captured"], "partial_truth": False, "partial_type": None, "source_id": None,
        "fields": {
            "title": "present" if "head_trim" not in s["noise"] else "missing",
            "employer": s["employer_state"] if "head_trim" not in s["noise"] else ("present" if s["employer_state"] == "present" and False else "missing"),
            "pay": s["pay_state"], "duties": "present", "closing": s["closing_state"] if "head_trim" not in s["noise"] else "missing",
        },
        "closing_date_iso": s["closing_iso"] if "head_trim" not in s["noise"] else None,
    })

# P08 head-trimmed: paste starts at "Job Description"; the company is named only in the About section ("About the company" text names
# nobody), so title, employer, pay and closing are all missing. Overridden explicitly for clarity.
for l in labels:
    if l["id"] == "P08":
        l["fields"] = {"title": "missing", "employer": "missing", "pay": "missing", "duties": "present", "closing": "missing"}
        l["closing_date_iso"] = None
    if l["id"] == "P16":
        # tail-trimmed before 'Report this job'; closing sentence sits after requirements and is kept
        pass

# ------------------------------------------------------------------------------------------------
# Partial pastes P31..P40
# ------------------------------------------------------------------------------------------------
def cut_mid_sentence(txt, marker, extra_chars):
    """Cut `extra_chars` after the first occurrence of `marker`, forcing a mid-word cut."""
    i = txt.index(marker) + len(marker) + extra_chars
    while i < len(txt) and not txt[i].isalpha():
        i += 1
    while i + 1 < len(txt) and txt[i + 1].isalpha() and txt[i - 1].isalpha() is False:
        i += 1
    return txt[:i]


partials = []

# P31 cut off mid-sentence in duties (from P01)
t = texts["P01"]
i = t.index("Lead the year-end audit and liaise with ex")
partials.append(("P31", "cut_off", "P01", t[: i + len("Lead the year-end audit and liaise with ex")] ))
# P32 cut mid-word in duties (from P12)
t = texts["P12"]
i = t.index("Process claims and leave applic")
partials.append(("P32", "cut_off", "P12", t[: i + len("Process claims and leave applic")]))
# P33 show-more teaser (from P20)
t = texts["P20"]
i = t.index("Guide visitors to the correct halls")
partials.append(("P33", "cut_off", "P20", t[:i] + "Guide visitors to the correct halls\nHand out programme booklets\nAnswer basic quest...\nShow more"))
# P34 cut mid-sentence in requirements (from P28)
t = texts["P28"]
i = t.index("Workplace Safety and Health Coordinator or equ")
partials.append(("P34", "cut_off", "P28", t[: i + len("Workplace Safety and Health Coordinator or equ")]))

# P35 role body missing, MCF page whose body had not loaded (from P02)
t = texts["P02"]
a = t.index("Job Description")
b = t.index("Additional Information")
partials.append(("P35", "no_body", "P02", t[:a] + "Job Description\nLoading...\n\n" + t[b:]))
# P36 role body missing, JobStreet (from P15): description removed, only side sections copied
t = texts["P15"]
a = t.index("Job description")
b = t.index("Additional information")
partials.append(("P36", "no_body", "P15", t[:a] + t[b:]))
# P37 role body missing, company page (from P25): header and apply button only
t = texts["P25"]
a = t.index("Overview")
b = t.index("Share this job")
partials.append(("P37", "no_body", "P25", t[:a] + t[b:]))

# P38 MCF search results cards
p38 = """Skip to main content
MyCareersFuture
Jobs
Employers
Career Resources
Log in
Sign up

Search results
6 jobs found
Sort by: Most relevant
Filters: Salary · Employment type · Category · Posted within

Administrative Assistant
Greenfold Logistics Pte Ltd
Tuas
$2,400 to $3,000
Monthly
Full Time
Posted 28 Oct 2026

Admin Executive
Crestline Trading Pte Ltd
Kallang
$2,800 to $3,400
Monthly
Full Time
Posted 30 Oct 2026

Customer Service Officer
Sunrise Telecom Services Pte Ltd
Paya Lebar
$2,600 to $3,200
Monthly
Full Time
Posted 2 Nov 2026

Office Assistant
Pioneer Mart Pte Ltd
Woodlands
$2,000 to $2,400
Monthly
Part Time
Posted 5 Nov 2026

Page 1 of 3
Next
About MyCareersFuture
Terms of Use
Privacy Statement
© 2026 Government of Singapore"""
partials.append(("P38", "cards_nav", None, p38))
# P39 JobStreet results list
p39 = """Skip to content
JobStreet
Find jobs
Career advice
Companies
Sign in
Employer site

receptionist jobs in Singapore
128 jobs
Sort by relevance
Filter: Classification, Work type, Pay, Date listed

Receptionist
Willowbrook Dental Group
Bukit Timah
Posted 7d ago
Quick apply

Front Desk Receptionist
Pearl Smiles Clinic
Bukit Merah
$2,300 - $2,800 per month
Posted 3d ago

Hotel Receptionist
Marlowe Hotels
Sentosa
Posted 1d ago

Admin Receptionist (Contract)
Anchorpoint Property
Tanjong Pagar
$2,500 - $3,000 per month
Posted 12d ago

Page 1 2 3 4 5 Next
Set up job alerts for this search
About JobStreet
Privacy
Terms and conditions"""
partials.append(("P39", "cards_nav", None, p39))
# P40 company careers landing / navigation only
p40 = """Tidewater Labs
About us
Our culture
Careers
News
Contact

Careers at Tidewater Labs
Find your next role
Open positions
Engineering
Design
Operations
Customer Success
People
View all 14 open roles

Life at Tidewater
Our values
Benefits
Diversity and inclusion

Subscribe to job alerts
Privacy policy
© 2026 Tidewater Labs"""
partials.append(("P40", "cards_nav", None, p40))

for pid, ptype, src, txt in partials:
    texts[pid] = txt
    base = {"id": pid, "synthetic": True, "set": "partial10", "board": None, "job_type": None, "captured_at": "2026-11-10T09:00:00+08:00",
            "partial_truth": True, "partial_type": ptype, "source_id": src, "closing_date_iso": None}
    if src:
        sl = next(l for l in labels if l["id"] == src)
        base["board"] = sl["board"]
        base["job_type"] = sl["job_type"]
        base["captured_at"] = sl["captured_at"]
    else:
        base["board"] = {"P38": "mcf", "P39": "jobstreet", "P40": "company"}[pid]
        base["job_type"] = "n/a"
    # field labels for partials are descriptive only; field scoring uses the 30 complete pastes
    base["fields"] = None
    labels.append(base)

# write
for pid, txt in texts.items():
    (OUT / "pastes" / f"{pid}.txt").write_bytes(txt.encode("utf-8"))

gold = {
    "note": "Gold labels for E13, written by the experiment author (an AI) before the snapshot step existed. synthetic: true. Frozen; see protocol/FROZEN.md.",
    "field_states": {"employer": ["present", "hidden_labelled", "missing"], "pay": ["present", "explicit_absence", "missing"],
                      "closing": ["present", "explicit_absence", "missing"], "title": ["present", "missing"], "duties": ["present", "missing"]},
    "items": labels,
}
(OUT / "gold_labels.json").write_text(json.dumps(gold, indent=1, ensure_ascii=False), encoding="utf-8")
print(len(texts), "pastes written")
