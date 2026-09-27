"""Smoke tests for core."""
import unittest

from epidemiology_ledger import core


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(core, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(core) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
