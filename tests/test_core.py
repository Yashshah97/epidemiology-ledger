import unittest
from epidemiology_ledger import core

class TestLedger(unittest.TestCase):
    def test_create_ledger(self):
        ledger = core.create_ledger()
        self.assertIsInstance(ledger, core.Ledger)

    def test_add_event(self):
        ledger = core.create_ledger()
        event = core.Event(timestamp=1, data="data")
        ledger.add_event(event)
        self.assertEqual(len(ledger.get_state()), 1)

    def test_get_state(self):
        ledger = core.create_ledger()
        event1 = core.Event(timestamp=1, data="data1")
        event2 = core.Event(timestamp=2, data="data2")
        ledger.add_event(event1)
        ledger.add_event(event2)
        self.assertEqual(ledger.get_state(), [event1, event2])

    def test_is_valid(self):
        ledger = core.create_ledger()
        event1 = core.Event(timestamp=1, data="data1")
        event2 = core.Event(timestamp=2, data="data2")
        ledger.add_event(event1)
        ledger.add_event(event2)
        self.assertTrue(ledger.is_valid())

    def test_is_invalid(self):
        ledger = core.create_ledger()
        event1 = core.Event(timestamp=1, data="data1")
        event2 = core.Event(timestamp=2, data="data2")
        ledger.add_event(event1)
        # Remove the hash of event1
        del ledger.events[0].hash
        self.assertFalse(ledger.is_valid())

if __name__ == "__main__":
    unittest.main()
