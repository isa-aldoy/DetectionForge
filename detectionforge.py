import argparse,json,fnmatch
from pathlib import Path
import yaml

def match(rule,event):
    d=rule["detection"];condition=d.get("condition","selection")
    if condition not in d or not isinstance(d[condition],dict): raise ValueError("Unsupported condition")
    for key,expected in d[condition].items():
        field,*mod=key.split("|");actual=str(event.get(field,"")).lower()
        options=expected if isinstance(expected,list) else [expected]
        if not any((str(v).lower() in actual if mod==["contains"] else fnmatch.fnmatchcase(actual,str(v).lower())) for v in options):return False
    return True
def run(rule,events):
    return [event for event in events if match(rule,event)]
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("rule");p.add_argument("events");a=p.parse_args()
    rule=yaml.safe_load(Path(a.rule).read_text())
    events=[json.loads(line) for line in Path(a.events).read_text().splitlines() if line.strip()]
    result=run(rule,events);print(json.dumps(result,indent=2))
