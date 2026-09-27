import unittest
from epidemiology_ledger import hashchain

class TestHashChain(unittest.TestCase):
    def test_add_event(self):
        ledger = hashchain.HashChain()
        event1 = b"Event 1"
        event2 = b"Event 2"
        ledger.add_event(event1)
        ledger.add_event(event2)

        self.assertEqual(len(ledger.data), 2)
        self.assertEqual(len(ledger.hashes), 2)
        self.assertEqual(ledger.data[0], event1)
        self.assertEqual(ledger.data[1], event2)

    def test_is_valid(self):
        ledger = hashchain.HashChain()
        event1 = b"Event 1"
        event2 = b"Event 2"
        ledger.add_event(event1)
        ledger.add_event(event2)

        self.assertTrue(ledger.is_valid())

        # Tamper with the ledger
        ledger.hashes[0] += 1

        self.assertFalse(ledger.is_valid())

    def test_get_hashchain(self):
        ledger = hashchain.HashChain()
        event1 = b"Event 1"
        event2 = b"Event 2"
        ledger.add_event(event1)
        ledger.add_event(event2)

        hash_chain = ledger.get_hashchain()

        self.assertEqual(len(hash_chain), 2)
        self.assertIsInstance(hash_chain[0], int)
        self.assertIsInstance(hash_chain[1], int)

if __name__ == "__main__":
    unittest.main()
