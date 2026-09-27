import unittest
from epidemiology_ledger import events

class TestEvents(unittest.TestCase):
    def test_event_hash(self):
        event = events.PersonExposed(1, 1643723400)
        with self.assertRaises(NotImplementedError):
            print(event.hash)

    def test_person_exposed_init(self):
        person_exposed = events.PersonExposed(1, 1643723400)
        self.assertEqual(person_exposed.id, 1)
        self.assertEqual(person_exposed.timestamp, 1643723400)

    def test_person_infected_init(self):
        person_infected = events.PersonInfected(1, 2, 1643723400)
        self.assertEqual(person_infected.id, 1)
        self.assertEqual(person_infected.exposure_id, 2)
        self.assertEqual(person_infected.timestamp, 1643723400)

    def test_event_log_init(self):
        event_log = events.EventLog()
        self.assertEqual(event_log.events, [])

if __name__ == '__main__':
    unittest.main()
