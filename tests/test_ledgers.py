"""Smoke tests for ledgers."""
import unittest

from epidemiology_ledger import ledgers


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(ledgers, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(ledgers) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
