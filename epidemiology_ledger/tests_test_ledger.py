import unittest
from tempfile import TemporaryDirectory
from typing import List

class TestLedger(unittest.TestCase):
    def test_append(self) -> None:
        """Test appending to the ledger."""
        with TemporaryDirectory() as dir_path:
            ledger = Ledger(dir_path)
            initial_hash = ledger.get_root_hash()
            ledger.append("Event 1")
            self.assertNotEqual(initial_hash, ledger.get_root_hash())

    def test_retrieve_events(self) -> None:
        """Test retrieving events from the ledger."""
        with TemporaryDirectory() as dir_path:
            ledger = Ledger(dir_path)
            initial_hash = ledger.get_root_hash()
            ledger.append("Event 1")
            self.assertEqual(ledger.retrieve_events(initial_hash), ["Event 1"])
            self.assertEqual(ledger.retrieve_events(), ["Event 1"])

    def test_invalid_append(self) -> None:
        """Test appending to an invalid ledger."""
        with TemporaryDirectory() as dir_path:
            ledger = Ledger(dir_path)
            with self.assertRaises(ValueError):
                ledger.append("Invalid Event")

class Ledger:
    def __init__(self, directory: str) -> None:
        """
        Initialize the append-only ledger.

        :param directory: The path to the ledger's directory.
        """
        import os
        self.directory = directory

    def get_root_hash(self) -> str:
        """Get the root hash of the ledger."""
        return "root_hash"

    def append(self, event: str) -> None:
        """
        Append an event to the ledger.

        :param event: The event to append.
        """
        raise NotImplementedError()

    def retrieve_events(self, start_hash: str = "") -> List[str]:
        """
        Retrieve events from the ledger starting with a given hash.

        :param start_hash: The hash of the first event to retrieve (default is empty string).
        :return: A list of events.
        """
        raise NotImplementedError()

if __name__ == "__main__":
    unittest.main()
