"""Independent registry lookup for ground truth. Uses the official ACRA open dataset on data.gov.sg (UEN dataset),
NOT the P03 registry service and NOT any registry-mirror site. Usage: registry_lookup.py "name" ["name2" ...]"""
import json, sys, urllib.parse, urllib.request, time
RID = "d_3f960c10fed6145404ca7b821f263b87"
def q(text, limit=8):
    url = "https://data.gov.sg/api/action/datastore_search?resource_id=%s&limit=%d&q=%s" % (RID, limit, urllib.parse.quote(text))
    for _ in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "JobHubE11-truth/0.1"}), timeout=40))["result"]["records"]
        except Exception as e:
            err = str(e); time.sleep(5)
    return [{"error": err}]
if __name__ == "__main__":
    for name in sys.argv[1:]:
        print("##", name)
        for r in q(name):
            print("  ", r.get("uen"), "|", r.get("entity_name"), "|", r.get("uen_status_desc"), "|", r.get("entity_type_desc"), "|", r.get("uen_issue_date"), r.get("error", ""))
