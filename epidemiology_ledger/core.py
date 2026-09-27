"""
Epidemiology Append-Only Ledger Core Module.

This module provides the core functionality for an append-only ledger,
a tamper-evident hash-chained event log. It includes methods to add events,
get the current state, and check if the ledger is valid.
"""

class Event:
    """Represents a single event in the ledger."""
    def __init__(self, timestamp, data):
        self.timestamp = timestamp
        self.data = data

class Ledger:
    """An append-only ledger with tamper-evident hash-chaining."""
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """
        Add a new event to the ledger.

        Args:
            event (Event): The event to add.
        """
        if not isinstance(event, Event):
            raise ValueError("Invalid event type")
        self.events.append(event)

    def get_state(self):
        """
        Get the current state of the ledger as a list of events.

        Returns:
            list: A list of all events in the ledger.
        """
        return self.events

    def is_valid(self, previous_hash=None):
        """
        Check if the ledger is valid by verifying the hash chain.

        Args:
            previous_hash (str): The expected hash of the previous event. Defaults to None.

        Returns:
            bool: True if the ledger is valid, False otherwise.
        """
        if not self.events or (previous_hash and not self._verify_hash_chain(previous_hash)):
            return False
        return True

    def _verify_hash_chain(self, previous_hash):
        """
        Verify the hash chain of events.

        Args:
            previous_hash (str): The expected hash of the previous event.

        Returns:
            bool: True if the hash chain is valid, False otherwise.
        """
        current_hash = self._hash_event(self.events[-1])
        for event in reversed(self.events[:-1]):
            current_hash = self._hash_event(event)
            if current_hash != previous_hash:
                return False
            previous_hash = current_hash
        return True

    @staticmethod
    def _hash_event(event):
        """
        Compute the hash of an event.

        Args:
            event (Event): The event to hash.

        Returns:
            str: The hash of the event.
        """
        import hashlib
        return hashlib.sha256(f"{event.timestamp}{event.data}".encode()).hexdigest()

def create_ledger():
    """Create a new, empty ledger."""
    return Ledger()
