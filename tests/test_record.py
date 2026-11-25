import unittest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'src'))
from record import validate

class EvidenceTest(unittest.TestCase):
    def test_pending_remains_pending(self):
        self.assertEqual(validate({'asset':'POTIFY','claim':'example','state':'pending'}),'pending')
    def test_reported_needs_reference(self):
        with self.assertRaises(ValueError):
            validate({'asset':'POTIFY','claim':'example','state':'reported','slot':123})
