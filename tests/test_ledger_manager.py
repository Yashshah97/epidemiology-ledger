import unittest
from epidemiology_ledger import ledger_manager

class TestLedgerManager(unittest.TestCase):

    def test_create_ledger(self):
        manager = ledger_manager.LedgerManager()
        manager.create_ledger('test')
        self.assertIn('test', manager.ledgers)

    def test_write_event(self):
        manager = ledger_manager.LedgerManager()
        manager.create_ledger('test')
        event = {'timestamp': 1, 'disease_spread': 0.5}
        manager.write_event('test', event)
        self.assertEqual(len(manager.read_events('test')), 1)

    def test_read_events(self):
        manager = ledger_manager.LedgerManager()
        manager.create_ledger('test')
        event1 = {'timestamp': 1, 'disease_spread': 0.5}
        event2 = {'timestamp': 2, 'disease_spread': 0.6}
        manager.write_event('test', event1)
        manager.write_event('test', event2)
        self.assertEqual(len(manager.read_events('test')), 2)

    def test_verify_ledger(self):
        manager = ledger_manager.LedgerManager()
        manager.create_ledger('test')
        event1 = {'timestamp': 1, 'disease_spread': 0.5}
        event2 = {'timestamp': 2, 'disease_spread': 0.6}
        manager.write_event('test', event1)
        manager.write_event('test', event2)
        self.assertTrue(manager.verify_ledger('test'))

if __name__ == '__main__':
    unittest.main()
