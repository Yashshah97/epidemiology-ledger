"""Smoke tests for ledger_manager."""
import unittest

from epidemiology_ledger import ledger_manager


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(ledger_manager, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(ledger_manager) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
