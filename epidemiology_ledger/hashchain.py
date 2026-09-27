"""
Handles hash-chaining of events in a tamper-evident manner.
"""

class HashChain:
    """
    A tamper-evident hash-chained event log.

    Attributes:
        data (list): The list of events, where each event is a string or bytes object.
        hashes (dict): A dictionary mapping indices to the hash of each event.
    """

    def __init__(self):
        self.data = []
        self.hashes = {}

    def add_event(self, event: str | bytes) -> None:
        """
        Add an event to the ledger.

        Args:
            event (str or bytes): The new event to be added.
        """
        if not isinstance(event, (str, bytes)):
            raise TypeError("Event must be a string or bytes object")
        
        self.data.append(event)
        self.hashes[len(self.data) - 1] = self._hash_event(event)

    def _hash_event(self, event: str | bytes) -> int:
        """
        Compute the hash of an event.

        Args:
            event (str or bytes): The event to be hashed.
        
        Returns:
            int: The hash of the event as a 32-bit integer.
        """
        import hashlib
        if isinstance(event, str):
            return int(hashlib.md5(event.encode()).hexdigest(), 16)
        else:
            return int(hashlib.md5(event).hexdigest(), 16)

    def is_valid(self) -> bool:
        """
        Check whether the ledger has been tampered with.

        Returns:
            bool: True if the ledger is valid, False otherwise.
        """
        for i in range(1, len(self.data)):
            expected_hash = self._hash_event(self.data[i - 1])
            actual_hash = self.hashes.get(i - 1)
            if expected_hash != actual_hash:
                return False
        return True

    def get_hashchain(self) -> list[int]:
        """
        Get the hash chain of events.

        Returns:
            list: A list of hashes, where each hash is a 32-bit integer.
        """
        return [self.hashes[i] for i in range(len(self.data))]

# Example usage:

ledger = HashChain()
ledger.add_event(b"Event 1")
ledger.add_event(b"Event 2")

print(ledger.is_valid())  # Should print: True
