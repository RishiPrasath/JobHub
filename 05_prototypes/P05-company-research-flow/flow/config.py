"""Settings, all from environment variables so the compose file is the single place to change them."""
import os

REGISTRY_URL = os.environ.get("REGISTRY_URL", "http://registry:8090").rstrip("/")
OPENSERP_URL = os.environ.get("OPENSERP_URL", "http://openserp:7000").rstrip("/")
FETCH_URL = os.environ.get("FETCH_URL", "http://fetch:8080").rstrip("/")
FETCH_TOKEN = os.environ.get("FETCH_TOKEN", "local-dev-token")

# 'fetch' = the repo's own fetch-render service (robots.txt checked, honest identity, private addresses refused).
# 'openserp' = OpenSERP's /extract (looks like a real browser, ignores robots.txt); only for comparison.
READER = os.environ.get("READER", "fetch")
# 'conservative' = never read review/job boards whose terms restrict scraping, link out instead. 'permissive' = read Indeed and JobStreet too.
READ_POLICY = os.environ.get("READ_POLICY", "conservative")

SEARCH_ENGINES = os.environ.get("SEARCH_ENGINES", "duckduckgo,bing")
MAX_QUERIES = int(os.environ.get("MAX_QUERIES", "5"))
MAX_PAGES = int(os.environ.get("MAX_PAGES", "8"))
PER_DOMAIN = int(os.environ.get("PER_DOMAIN", "2"))
PAGE_CHARS = int(os.environ.get("PAGE_CHARS", "3200"))        # characters of each page given to the model
DEADLINE_SECONDS = float(os.environ.get("DEADLINE_SECONDS", "300"))   # whole research run; later steps are skipped past it

GROQ_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_URL = (os.environ.get("GROQ_BASE_URL") or "https://api.groq.com/openai/v1").rstrip("/") + "/chat/completions"
MODEL = os.environ.get("GROQ_MODEL") or "openai/gpt-oss-120b"
LLM_TPM = int(os.environ.get("LLM_TPM_BUDGET", "6500"))

PORT = int(os.environ.get("FLOW_PORT", "8100"))
JOB_WORKERS = int(os.environ.get("JOB_WORKERS", "2"))
CACHE_SECONDS = int(os.environ.get("CACHE_SECONDS", "3600"))
MAX_NAME_CHARS = 200

DISCLAIMER = ("This shows whether the company exists and matches the name in the posting, and what public sources say about it. "
              "It is not a judgement of the employer. Anything marked unverified or not read could not be confirmed.")
