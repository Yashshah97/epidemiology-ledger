"""
Append-Only Ledger Base Class.

This module provides the base class for append-only ledgers. An append-only ledger is a data structure that records events in an order-preserving manner.
The ledger is tamper-evident, meaning any attempt to modify or delete an event will result in a new version being recorded with a different hash value.
"""

class AppendOnlyLedger:
    """
    Base class for append-only ledgers.

    Attributes:
        events (list): A list of events recorded by the ledger.
        current_hash (str): The hash value of the most recent event.
    """

    def __init__(self):
        self.events = []
        self.current_hash = None

    def record_event(self, event):
        """
        Record an event in the ledger.

        Args:
            event (dict): An event to be recorded by the ledger. The event should have a 'hash' key with its hash value.

        Returns:
            str: The new current hash value of the ledger.
        """
        if self.current_hash is not None:
            previous_event = self.events[-1]
            expected_hash = self._calculate_hash(previous_event, event)
            if expected_hash != event['hash']:
                raise ValueError("Invalid event hash")
        self.events.append(event)
        self.current_hash = event['hash']
        return self.current_hash

    def _calculate_hash(self, previous_event, new_event):
        """
        Calculate the expected hash value of a new event based on the previous event.

        Args:
            previous_event (dict): The previous event in the ledger.
            new_event (dict): The new event to be recorded by the ledger.

        Returns:
            str: The expected hash value of the new event.
        """
        # For simplicity, we use a basic hash calculation here. In a real-world application,
        # you would want to use a cryptographically secure hash function like SHA-256 or BLAKE2.
        return f"{previous_event['hash']}::{new_event['hash']}"

    def get_events(self):
        """
        Get the events recorded by the ledger.

        Returns:
            list: A list of events recorded by the ledger.
        """
        return self.events
