import unittest
from epidemiology_ledger import ledgers

class TestAppendOnlyLedger(unittest.TestCase):
    def test_record_event(self):
        ledger = ledgers.AppendOnlyLedger()
        event1 = {'hash': 'event1_hash'}
        event2 = {'hash': 'event2_hash'}
        self.assertEqual(ledger.record_event(event1), 'event1_hash')
        self.assertEqual(ledger.record_event(event2), 'event2_hash')

    def test_record_event_invalid_hash(self):
        ledger = ledgers.AppendOnlyLedger()
        event1 = {'hash': 'event1_hash'}
        event2 = {'hash': 'invalid_hash'}
        with self.assertRaises(ValueError):
            ledger.record_event(event2)

    def test_get_events(self):
        ledger = ledgers.AppendOnlyLedger()
        event1 = {'hash': 'event1_hash'}
        event2 = {'hash': 'event2_hash'}
        ledger.record_event(event1)
        ledger.record_event(event2)
        self.assertEqual(ledger.get_events(), [event1, event2])

if __name__ == '__main__':
    unittest.main()
