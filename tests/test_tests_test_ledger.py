import unittest
from tempfile import TemporaryDirectory
from typing import List
from epidemiology_ledger import Ledger, tests_test_ledger

class TestLedgerFunctions(unittest.TestCase):
    def test_get_root_hash(self) -> None:
        """Test getting the root hash."""
        with TemporaryDirectory() as dir_path:
            ledger = Ledger(dir_path)
            self.assertEqual(ledger.get_root_hash(), "root_hash")

if __name__ == "__main__":
    unittest.main()
