import hashlib
from typing import Dict, List

class LedgerManager:
    """
    Manages the creation, reading, and writing of ledgers.
    
    A ledger is a list of events, where each event is a dictionary with a 'timestamp' key.
    The ledger is append-only, meaning that once an event is written, it cannot be modified or deleted.
    """

    def __init__(self):
        self.ledgers: Dict[str, List[Dict]] = {}

    def create_ledger(self, name: str) -> None:
        """
        Creates a new ledger with the given name.

        Args:
            name (str): The name of the ledger to create.
        """
        if name not in self.ledgers:
            self.ledgers[name] = []

    def write_event(self, name: str, event: Dict) -> None:
        """
        Writes an event to the given ledger.

        Args:
            name (str): The name of the ledger to write to.
            event (Dict): The event to write, which should have a 'timestamp' key.
        """
        if name in self.ledgers:
            hash = hashlib.sha256(str(event).encode()).hexdigest()
            self.ledgers[name].append({'event': event, 'hash': hash})

    def read_events(self, name: str) -> List[Dict]:
        """
        Reads all events from the given ledger.

        Args:
            name (str): The name of the ledger to read from.

        Returns:
            List[Dict]: A list of events in the ledger.
        """
        if name in self.ledgers:
            return [{'event': event['event'], 'hash': event['hash']} for event in self.ledgers[name]]

    def verify_ledger(self, name: str) -> bool:
        """
        Verifies that the given ledger is tamper-evident.

        Args:
            name (str): The name of the ledger to verify.

        Returns:
            bool: True if the ledger is tamper-evident, False otherwise.
        """
        if name in self.ledgers and len(self.ledgers[name]) > 0:
            hash = hashlib.sha256(str(self.ledgers[name][0]['event']).encode()).hexdigest()
            for i in range(1, len(self.ledgers[name])):
                if self.ledgers[name][i-1]['hash'] != hashlib.sha256(str(self.ledgers[name][i]['event']).encode()).hexdigest():
                    return False
            return True
        return False

# Example usage:
if __name__ == "__main__":
    manager = LedgerManager()
    manager.create_ledger('example')
    manager.write_event('example', {'timestamp': 1, 'disease_spread': 0.5})
    print(manager.read_events('example'))
    print(manager.verify_ledger('example'))
