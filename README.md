# DetectionForge
Offline regression test harness for a **limited Sigma-style YAML subset** against JSONL events.

## Run
```sh
pip install -r requirements.txt
python detectionforge.py examples/rule.yml examples/events.jsonl
python -m unittest discover -s tests -v
```
Matches a named detection selector against fields, including `contains` and glob patterns. Unsupported conditions raise exceptions. Intended to support repeatable defensive detection-rule tests; this is not a full Sigma engine or production SIEM.
