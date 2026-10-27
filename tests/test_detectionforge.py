import unittest,yaml,json,pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from detectionforge import run,match
class Tests(unittest.TestCase):
 def test_rule_against_events(self):
  root=pathlib.Path(__file__).resolve().parents[1]
  rule=yaml.safe_load((root/'examples/rule.yml').read_text())
  events=[json.loads(x) for x in (root/'examples/events.jsonl').read_text().splitlines()]
  self.assertEqual(len(run(rule,events)),1)
 def test_unsupported_condition(self):
  with self.assertRaises(ValueError):
   match({'detection':{'selection':{'x':'y'},'condition':'not selection'}},{'x':'y'})
