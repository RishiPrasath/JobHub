"""Builds data/pack.json (the Singapore rule pack, version 0.1, posting wording only).

Sources were read on 2026-11-10 with WebFetch (a fetch tool that returns a model-written summary of the page,
not the raw page). Wording lists come from the TAFEP page "Writing job advertisements" and the Tripartite
Guidelines page. Categories 3 to 5 have only partial or no TAFEP/MOM source for posting wording; that is
recorded per entry (source_support) and not hidden.

Run: python build_pack.py   (rewrites pack_v0.2_posthoc.json; POST HOC edit of build_pack.py made after run-001 results)
"""
import json
from pathlib import Path

ACCESS = "2026-11-10"

SOURCES = {
    "S1": {"name": "TAFEP, Tripartite Guidelines on Fair Employment Practices (web page)",
           "url": "https://www.tal.sg/tafep/getting-started/fair/tripartite-guidelines", "accessed": ACCESS,
           "loaded": True},
    "S2": {"name": "TAFEP, Writing job advertisements (web page)",
           "url": "https://www.tal.sg/tafep/employment-practices/recruitment/writing-job-advertisements",
           "accessed": ACCESS, "loaded": True},
    "S3": {"name": "MOM, Fair Consideration Framework (web page, last updated 8 Aug 2025)",
           "url": "https://www.mom.gov.sg/employment-practices/fair-consideration-framework", "accessed": ACCESS,
           "loaded": True},
    "S4": {"name": "MOM, Allowable salary deductions (web page)",
           "url": "https://www.mom.gov.sg/employment-practices/salary/salary-deductions", "accessed": ACCESS,
           "loaded": True},
    "S5": {"name": "MOM FAQ, employment agency fees for workers (web page)",
           "url": "https://www.mom.gov.sg/faq/employment-agencies/how-will-foreign-workers-know-the-amount-that-they-are-expected-to-pay-the-singapore-ea",
           "accessed": ACCESS, "loaded": True},
    "S6": {"name": "MOM, Key employment terms (web page)",
           "url": "https://www.mom.gov.sg/employment-practices/contract-of-service/key-employment-terms",
           "accessed": ACCESS, "loaded": True},
}

CATS = {
    1: "Exclusionary or discriminatory wording",
    2: "Questionable screening requirements",
    3: "Requests for money or sensitive information",
    4: "Unpaid work or unclear compensation",
    5: "Misleading or dehumanising presentation",
}

NOT_EST = ("The wording alone does not show the employer's intent, whether the role has a job-related reason, "
           "or how any law applies. It needs a human reading and the employer's own explanation.")

E = []


def add(eid, cat, label, desc, patterns, suppress, synonyms, examples, counter, src, support, why, q,
        negation=True, window=100):
    E.append(dict(entry_id=eid, category=cat, category_name=CATS[cat], label=label, description=desc,
                  patterns=patterns, suppress=suppress, negation_aware=negation, suppress_window=window,
                  synonyms=synonyms, examples=examples, counterexamples=counter, source_ids=src,
                  source_support=support, why_it_may_matter=why, what_is_not_established=NOT_EST,
                  suggested_question=q))


# ---- Category 1 ----
add("P1-AGE", 1, "Age-coded wording", "age ranges, age limits, 'young', 'youthful', 'digital native', 'fresh graduates only'",
    [r"\bage[d]?\s*(?:of|between|from)?\s*\d{2}\s*(?:to|-|–|and)\s*\d{2}\b",
     r"\b(?:below|under|above|over)\s+(?:the\s+age\s+of\s+)?\d{2}\s*(?:only|years|yrs)\b",
     r"\bminimum\s+aged?\s+\d{2}\b",
     r"\byoung(?:er)?\b", r"\byouth(?:ful)?\b", r"\bdigital\s+natives?\b",
     r"\bfresh\s+grad(?:uate)?s?\s+only\b"],
    [r"young\s+(?:children|child|kids|learners|students)", r"youth\s+(?:programme|program|work|worker|centre|center|services)",
     r"all\s+ages", r"older\s+workers", r"mature\s+(?:candidates|workers)", r"regardless\s+of\s+age"],
    ["age 25 to 30", "below 30 only", "young", "youthful", "digital native", "minimum aged 21 and above"],
    ["Age 25 to 30 only", "Below 30 only", "Young/Youthful working environment", "Minimum aged 21 and above"],
    ["Candidates are required to load and unload sacks of rice of at least 10kg each (a stated physical task)",
     "Teach young children aged 3 to 6 (age of the people served, not of the applicant)"],
    ["S2", "S1"], "direct",
    "TAFEP guidance says age should generally not be a selection criterion and that a physical task should be described instead of an age group.",
    "Could you tell me how the age or experience wording in the posting relates to the duties of the role?")
add("P1-GENDER", 1, "Gender-coded wording", "'female preferred', 'men only', 'strong guys', 'female working environment'",
    [r"\b(?:female|male|ladies|lady|gentlemen|girls?|guys?|men|women)s?\s+(?:only|preferred|wanted|needed)\b",
     r"\bpreferably\s+(?:female|male|a\s+(?:woman|man|lady))\b", r"\bstrong\s+guys?\b",
     r"\bfemale\s+working\s+environment\b"],
    [r"both\s+genders", r"all\s+genders", r"male\s+and\s+female", r"men\s+and\s+women", r"regardless\s+of\s+gender"],
    ["female preferred", "ladies only", "men only", "strong guys needed"],
    ["Strong guys needed", "Preferably female", "Female working environment"],
    ["Both genders may apply (gender-specific job title)",
     "Female therapists for female customers where the reason is stated (listed by TAFEP as acceptable)"],
    ["S2", "S1"], "direct",
    "TAFEP guidance says gender should not be a criterion unless there is a practical requirement, and that the reason should be stated.",
    "Could you tell me whether the gender wording is tied to a requirement of the role, and what that requirement is?")
add("P1-RACE", 1, "Race-coded wording", "'Chinese preferred', 'Malay only', 'Mandarin-speaking environment' as a race proxy",
    [r"\b(?:chinese|malay|indian|eurasian|caucasian)(?:\s*/\s*(?:chinese|malay|indian|eurasian))*\s+(?:preferred|only)\b",
     r"\bchinese\s+race\b",
     r"\b(?:chinese|malay|tamil|mandarin|hokkien)(?:\s*/\s*\w+)*[\s-]+speaking\s+environment\b"],
    [r"all\s+races", r"regardless\s+of\s+race"],
    ["Chinese preferred", "Malay only", "Indian only"],
    ["Chinese/Malay/Indian preferred", "Chinese/Malay/Indian only", "Chinese/Malay/Tamil speaking environment"],
    ["All races are welcome (acceptable wording per TAFEP)"],
    ["S2", "S1"], "direct",
    "TAFEP guidance says race should not be a selection criterion. 'All races are welcome' is given as acceptable wording.",
    "Could you tell me whether the wording about race or the working environment is a requirement of the role, and why?")
add("P1-RELIGION", 1, "Religion-coded wording", "'Muslim only', 'Christian preferred'",
    [r"\b(?:christian|buddhist|muslim|hindu|catholic|sikh|taoist)s?(?:\s*/\s*\w+)*\s+(?:preferred|only)\b"],
    [r"regardless\s+of\s+religion"],
    ["Muslim only", "Christian preferred"],
    ["Christian/Buddhist/Muslim/Hindu preferred", "Christian/Buddhist/Muslim/Hindu only"],
    ["Hindu priest required to perform wedding ceremony (religious function; acceptable per TAFEP)"],
    ["S2", "S1"], "direct",
    "TAFEP guidance says religion should not be a criterion unless the job involves religious functions or certification standards.",
    "Could you tell me whether the religion wording relates to a religious function or certification the role requires?")
add("P1-NATIONALITY", 1, "Nationality or work-pass wording", "'non-Singaporeans preferred', 'S Pass quota available', 'work passes will be applied', national service status",
    [r"\bnon[- ]singaporeans?\b",
     r"\b(?:foreigners?|international\s+candidates?)\s+(?:are\s+)?(?:preferred|welcome|only)\b",
     r"\b(?:ep|s\s*pass|work\s*permit|wp|dp|ltvp|ltsvp)(?:\s*/\s*[a-z\s]+)*\s+holders?\s+(?:are\s+)?(?:preferred|welcome|only)\b",
     r"\bs\s*pass\s+quota\b", r"\bwork\s+passes?\s+will\s+be\s+applied\b",
     r"\bcandidates?\s+with\s+\w+\s+as\s+(?:a\s+)?first\s+language\b",
     r"\b(?:italian|korean|japanese|filipino)\s+(?:chef|nationals?)\s+preferred\b",
     r"\b(?:completed|exempted\s+from|not\s+liable\s+for)\s+national\s+service\b"],
    [], ["non-Singaporeans preferred", "foreigners welcome", "S Pass quota available"],
    ["Non-Singaporeans/foreigners/international candidates preferred/welcome/only", "S Pass quota available",
     "Work passes will be applied for successful candidates"],
    ["Stating that a vacancy is advertised on MyCareersFuture for 14 days (Fair Consideration Framework notice)"],
    ["S2", "S3"], "direct",
    "TAFEP guidance says nationality should not be a criterion, especially wording that prefers non-Singaporeans.",
    "Could you tell me how the nationality or work-pass wording relates to the role, and whether all applicants are considered?")
add("P1-LANGUAGE", 1, "Language wording without a stated reason", "'native Mandarin', 'bilingual in English and Malay', 'Tagalog speaking'",
    [r"\bnative\s+(?:mandarin|malay|bahasa(?:\s+melayu)?|tamil|korean|japanese|english)\b",
     r"\bbilingual\s+in\s+english\s+and\s+(?:mandarin|malay|tamil|chinese)\b",
     r"\b(?:tagalog|thai|mandarin|malay|tamil)[\s-]+speaking\b"],
    [r"\b(?:because|since|serve|communicate|assist|support|customers?|clients?|teach(?:er|ing)?|tutor)\b"],
    ["native Mandarin speaker", "bilingual in English and Tamil"],
    ["Native Mandarin/Bahasa Malayu/Tamil language/speaking", "Bilingual in English and Mandarin/Malay/Tamil"],
    ["Chinese-language teacher for pre-school centre (reason stated)",
     "Fluency in Tagalog needed because most counter customers speak Tagalog (reason stated)"],
    ["S2"], "direct",
    "TAFEP guidance says to state the reason for any language requirement and to keep the advertisement in the language of the medium.",
    "Could you tell me why this language is needed for the role, for example which customers or duties it serves?",
    window=120)

# ---- Category 2 ----
add("P2-FAMILY", 2, "Marital status, family plans or pregnancy", "marital status, 'plan to have children', pregnancy, family commitments",
    [r"\bmarital\s+status\b", r"\b(?:single|unmarried|married)\s+(?:only|preferred|candidates|females?|males?|ladies)\b",
     r"\bplan(?:ning)?\s+to\s+have\s+(?:children|kids|a\s+baby|a\s+family)\b",
     r"\b(?:family\s+plans|pregnan(?:t|cy)|family\s+commitments?)\b", r"\bnumber\s+of\s+children\b"],
    [r"(?:maternity|paternity|parental|childcare)\s+(?:leave|benefits|support)"],
    ["marital status", "plan to have children", "pregnant", "family commitments"],
    ["Are you planning to have children soon?", "whether pregnant or have children", "Marital status and family responsibilities"],
    ["Maternity and paternity leave listed as benefits"],
    ["S1", "S2"], "direct",
    "TAFEP guidance says marital status and family responsibilities should not be selection criteria, and lists 'Are you planning to have children soon?' as a question not to ask.",
    "Could you tell me why marital status or family plans are asked for at the application stage, and whether they affect selection?")
add("P2-PHOTO", 2, "Photograph or body-measurement request", "asks for photographs, full-body photos, height and weight",
    [r"\b(?:attach|include|submit|send|provide|upload)\s+(?:a\s+|your\s+)?(?:recent\s+)?(?:passport[- ]size(?:d)?\s+|full[- ]body\s+|colou?r\s+)?photo(?:graph)?s?\b",
     r"\bphoto(?:graph)?s?\s+(?:is|are)\s+(?:required|a\s+must|mandatory)\b", r"\bfull[- ]body\s+photo",
     r"\bheight\s+and\s+weight\b"],
    [], ["attach photo", "full-body photograph", "height and weight"],
    ["Remove fields on photographs (application forms)", "Attach a recent full-body photograph"],
    ["Request photos at the job offer stage with the reason stated"],
    ["S1"], "direct",
    "TAFEP guidance says to remove photograph fields from application forms, or to request photographs at the job offer stage with the reason stated.",
    "Could you tell me why a photograph is needed at the application stage, and whether it can be provided later?")
add("P2-HEALTH", 2, "Health, disability or religion disclosure", "asks applicants to state religion, race, age, medical history or disabilities",
    [r"\b(?:state|declare|disclose|indicate|provide)\s+(?:your\s+)?(?:religion|race|age|medical\s+(?:conditions?|history)|disabilit(?:y|ies)|health\s+(?:status|conditions?))\b",
     r"\b(?:perfect|excellent)\s+health\b", r"\bno\s+(?:medical\s+history|health\s+(?:issues|problems))\b",
     r"\bdo\s+you\s+have\s+any\s+disabilit"],
    [r"\b(?:fitness|licen[cs]e|regulat)"],
    ["state your religion", "perfect health", "no medical history"],
    ["Do you have any disabilities?", "Remove fields on age, gender, race, religion, marital status and family responsibilities, or disability"],
    ["Medical fitness check required by transport regulations"],
    ["S1"], "direct",
    "TAFEP guidance says application forms should not ask for age, gender, race, religion, marital status, family responsibilities or disability, unless there is a stated reason.",
    "Could you tell me whether the health or personal detail is required by the duties or by a regulation, and at what stage it is needed?")
add("P2-IDINFO", 2, "Identity-number or social-account request at application", "NRIC required up front, social media passwords",
    [r"\bnric\s+(?:number|no\.?)\s+(?:is\s+)?(?:required|must|to\s+be\s+(?:provided|included))\b",
     r"\b(?:provide|include|state)\s+(?:your\s+)?nric\b",
     r"\bsocial\s+media\s+(?:password|login|account\s+access)\b", r"\bfacebook\s+(?:password|login)\b"],
    [], ["provide your NRIC", "social media password"],
    ["Provide your NRIC number in the application"],
    ["Accept other forms of identification such as passport numbers"],
    ["S1"], "partial",
    "TAFEP says NRIC numbers can reveal a person's age, so other identification can be accepted. Social-account access has no TAFEP/MOM source in the pack.",
    "Could you tell me at what stage an identity number is needed and whether another form of identification is accepted?")
add("P2-APPEARANCE", 2, "Appearance-based wording", "'good-looking', 'pleasant appearance'",
    [r"\b(?:good[- ]looking|pleasant\s+appearance|good\s+looks|attractive\s+(?:female|male|ladies|girls?))\b"],
    [], ["good-looking", "pleasant appearance"], ["Good-looking front desk staff"],
    ["Well-groomed or professional appearance linked to a stated dress code"],
    ["S1"], "partial",
    "TAFEP's merit principle says selection should rest on skills, experience or ability to perform the job. The page does not name appearance wording, so the support is indirect.",
    "Could you tell me how the appearance wording relates to the duties, and what the dress or grooming expectations are?")

# ---- Category 3 ----
add("P3-FEE", 3, "Fee, deposit or cost charged to applicant", "registration, training, course, placement fees or deposits",
    [r"\b(?:registration|processing|admin(?:istration)?|training|placement|uniform|deposit|security|application|joining|course|kit)\s+(?:fee|fees|charge|charges|deposit|deposits)\b",
     r"\b(?:refundable\s+)?(?:security\s+)?deposit\s+of\s+\$?\s*\d[\d,]*",
     r"\bpay\s+(?:a\s+|an\s+)(?:\$\s*\d[\d,]*|fee|deposit)\b", r"\bpayable\s+(?:before|prior\s+to|upfront|in\s+advance)\b",
     r"\bpay\s+(?:for\s+)?(?:your\s+own\s+)?(?:uniforms?|training|starter\s+kit|materials?)\b"],
    [r"\b(?:sponsor(?:ed)?|reimburs(?:e|ed)|paid\s+by\s+(?:the\s+)?company|company[- ]paid|at\s+no\s+cost)\b"],
    ["registration fee", "security deposit", "pay for training", "course fee"],
    ["A $300 training fee is payable before you start", "A refundable security deposit of $500"],
    ["Training fully sponsored by the company", "We never charge candidates any fee"],
    ["S5", "S4"], "partial",
    "MOM caps agency fees collected from foreign workers (no more than one month of fixed monthly salary per year of service, capped at two months) and says some salary deductions cannot be a condition of employment for migrant workers. Neither page speaks to employer-charged fees for all applicants, so support is partial.",
    "Could you tell me what the fee or deposit is for, whether it is refundable, and when it is returned?")
add("P3-DOCS", 3, "Retention of documents or sensitive credentials", "keeping original passport or certificates, bank PINs, OTP codes",
    [r"\b(?:keep|hold|retain|withhold)\s+(?:your\s+)?(?:original\s+)?(?:passport|certificates?|nric|work\s+permit)",
     r"\bsurrender\s+(?:your\s+)?(?:original\s+)?(?:passport|certificates?)\b",
     r"\bhand\s+over\s+(?:your\s+)?original\s+(?:passport|certificates?)\b",
     r"\bbank\s+(?:account\s+)?(?:pin|password|otp)\b", r"\b(?:otp|one[- ]time\s+password)\b",
     r"\bcredit\s+card\s+(?:number|details)\b"],
    [], ["keep your original passport", "hold your certificates", "bank PIN", "OTP"],
    ["We will keep your original passport and certificates"],
    ["Bring original certificates for verification on the first day and take them home the same day"],
    [], "none",
    "Asking an applicant to hand over original identity documents or bank credentials is a common warning sign. No TAFEP or MOM page in the pack was read for this, so there is no named source.",
    "Could you tell me why the original documents are needed, how long they are kept, and when they are returned?")

# ---- Category 4 ----
add("P4-UNPAID", 4, "Unpaid trial or unpaid work", "unpaid trial, unpaid internship, trial days without pay",
    [r"\bunpaid\s+(?:trial|work|internship|training|probation|test|shift|period|assignment)s?\b",
     r"\b(?:trial|probation|training)\s+(?:days?|period|shifts?)?\s*(?:is|are)?\s*(?:unpaid|without\s+pay)\b",
     r"\bwithout\s+pay\b", r"\bno\s+pay\s+(?:during|for)\b"],
    [], ["unpaid trial", "trial days are unpaid", "without pay"],
    ["Trial days are unpaid", "A 3-day unpaid trial"],
    ["Paid internship with allowance"],
    [], "none",
    "Unpaid work offered as a condition of being considered is a common warning sign. No TAFEP or MOM page in the pack was read for this, so there is no named source.",
    "Could you tell me whether the trial period is paid, how long it lasts, and what work is done during it?")
add("P4-DEDUCT", 4, "Salary deductions or liquidated damages", "liquidated damages, deductions from salary on resignation",
    [r"\bliquidated\s+damages\b", r"\bsalary\s+(?:will\s+be\s+)?deduct",
     r"\bdeduct(?:ed|ion|ions)?\s+(?:from\s+(?:your\s+)?(?:salary|pay|wages)|for\s+(?:resign|leaving|breaking))"],
    [], ["liquidated damages", "deducted from your salary"],
    ["Liquidated damages of $3,000 will be deducted from your salary"],
    ["Deductions for CPF contributions, as required"],
    ["S4"], "direct",
    "The MOM page lists the salary deductions that are allowed and gives liquidated damages as an example of a deduction that is not authorised under the Employment Act for covered employees.",
    "Could you tell me what the deduction covers, when it applies, and which terms of the contract state it?")
add("P4-PAYUNCLEAR", 4, "Unclear pay, commission-only or overtime wording", "commission only, 'earn up to', overtime unpaid or included",
    [r"\bcommission[- ]only\b",
     r"\b(?:overtime|ot)\s+(?:is\s+)?(?:unpaid|not\s+paid|at\s+(?:the\s+)?(?:management's\s+)?discretion|included\s+in\s+(?:the\s+)?(?:basic|salary))\b",
     r"\bno\s+(?:overtime|ot)\s+(?:pay|payment|claim)s?\b", r"\bearn\s+up\s+to\s+\$?\s*\d[\d,]*",
     r"\bunlimited\s+(?:earning|income|commission)", r"\bpay\s+(?:is\s+)?(?:not\s+guaranteed|depends\s+on\s+performance)\b"],
    [r"\bper\s+MOM\b", r"\bEmployment\s+Act\b", r"\bitemis(?:ed|e)\b"],
    ["commission only", "earn up to", "overtime included in salary"],
    ["Commission-only role, earn up to $6,000", "Overtime is included in the basic salary"],
    ["Base salary plus tiered commission with rates written in the contract"],
    ["S6"], "partial",
    "MOM's key employment terms page lists the salary items an employer states in writing (basic salary, allowances, deductions, overtime rate, bonuses). It does not rule on advertising wording, so support is partial.",
    "Could you tell me the guaranteed basic pay, how commission is calculated, and how overtime is paid?")

# ---- Category 5 ----
add("P5-RAPID", 5, "Unsupported promises of rapid progression or income", "'director in 6 months', 'six-figure income in', 'be your own boss'",
    [r"\b(?:become|be)\s+(?:a\s+)?(?:manager|director|boss|millionaire|team\s+leader)\s+in\s+(?:just\s+)?(?:\d+|a\s+few|three|six|two)\s+(?:weeks|months)\b",
     r"\bfast[- ]track(?:ed)?\s+to\s+(?:management|director|senior)\b",
     r"\b(?:six|6)[- ]figure\s+(?:income|salary)\s+(?:in|within)\b", r"\bbe\s+your\s+own\s+boss\b",
     r"\bpromot(?:ed|ion)\s+(?:guaranteed|within\s+\d+\s+(?:weeks|months))"],
    [], ["become a director in 6 months", "be your own boss"],
    ["You will become a director in just 6 months"],
    ["Strong performers may be considered for team-lead roles after an annual review"],
    [], "none",
    "Promises of rapid progression that the role does not support are a common warning sign. No TAFEP or MOM page in the pack was read for this, so there is no named source.",
    "Could you tell me how progression works in this role, what the typical timeline has been, and what it depends on?")
add("P5-DEMANDS", 5, "Vague duties with high personal demands, or dehumanising wording", "'willing to do anything', 'no questions asked', 24/7 availability, 'treat the company as family'",
    [r"\bwilling\s+to\s+do\s+anything\b", r"\bno\s+questions\s+asked\b",
     r"\b(?:24/7|24\s*/\s*7)\s+(?:availability|available|on[- ]call)\b", r"\b(?:available|on\s+call)\s+(?:24/7|24\s+hours)\b",
     r"\btreat\s+(?:the\s+)?company\s+(?:as|like)\s+(?:your\s+)?family\b", r"\bthick[- ]skinned?\b",
     r"\bsacrific(?:e|es)\s+(?:your\s+)?(?:weekends|personal|social)", r"\breplaceable\b|\bdisposable\b|\bwarm\s+bodies\b"],
    [], ["willing to do anything", "no questions asked", "available 24/7"],
    ["Must be willing to do anything the company asks, available 24/7, no questions asked"],
    ["On-call rota every fourth week with on-call allowance stated"],
    [], "none",
    "Vague duties paired with high personal demands, or wording that treats workers as interchangeable, are common warning signs. No TAFEP or MOM page in the pack was read for this, so there is no named source.",
    "Could you tell me what the main duties are, what the expected working hours are, and how after-hours work is compensated?")

pack = {
    "pack_version": "0.2-posthoc",
    "created_utc": "2026-11-10",
    "scope": "Singapore; job posting wording only; five categories",
    "author_note": "Written by an AI specialist (not an HR or employment-law reviewer). Not reviewed by a human.",
    "fetch_note": "Pages were read with WebFetch, which returns a model-written summary of the page text, not the raw page. Wording lists may be incomplete.",
    "access_date": ACCESS,
    "categories": CATS,
    "sources": SOURCES,
    "known_source_gap": "TAFEP and MOM pages read do not cover unpaid trials, document retention, or misleading progression claims in postings. Entries P3-DOCS, P4-UNPAID, P5-RAPID and P5-DEMANDS have no named source (source_support = none). The TAFEP table lists 'Only Singaporeans' under acceptable wording, which conflicts with its general nationality rule; the pack deliberately has no pattern for it.",
    "entries": E,
}
out = Path(__file__).with_name("pack_v0.2_posthoc.json")
out.write_text(json.dumps(pack, ensure_ascii=False, indent=1), encoding="utf-8")
print("entries", len(E), "->", out)
