"""
Event classes for the epidemiology ledger.
"""

class Event:
    """Base class for all events."""
    def __init__(self):
        pass

    @property
    def hash(self):
        raise NotImplementedError("Subclasses must implement `hash` property")

class PersonExposed(Event):
    """
    A person was exposed to a disease.

    Attributes:
        id (int): Unique identifier of the person.
        timestamp (float): Timestamp when the exposure occurred.
    """
    def __init__(self, id, timestamp):
        super().__init__()
        self.id = id
        self.timestamp = timestamp

class PersonInfected(Event):
    """
    A person was infected with a disease.

    Attributes:
        id (int): Unique identifier of the person.
        exposure_id (int): Identifier of the exposure event.
        timestamp (float): Timestamp when the infection occurred.
    """
    def __init__(self, id, exposure_id, timestamp):
        super().__init__()
        self.id = id
        self.exposure_id = exposure_id
        self.timestamp = timestamp

class PersonRecovered(Event):
    """
    A person recovered from a disease.

    Attributes:
        id (int): Unique identifier of the person.
        infection_id (int): Identifier of the infection event.
        timestamp (float): Timestamp when the recovery occurred.
    """
    def __init__(self, id, infection_id, timestamp):
        super().__init__()
        self.id = id
        self.infection_id = infection_id
        self.timestamp = timestamp

class PersonDied(Event):
    """
    A person died from a disease.

    Attributes:
        id (int): Unique identifier of the person.
        infection_id (int): Identifier of the infection event.
        timestamp (float): Timestamp when the death occurred.
    """
    def __init__(self, id, infection_id, timestamp):
        super().__init__()
        self.id = id
        self.infection_id = infection_id
        self.timestamp = timestamp

class EventLog:
    """A list of events."""
    def __init__(self):
        self.events = []
