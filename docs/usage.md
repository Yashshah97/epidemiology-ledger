# Usage

```python
import epidemiology_ledger
```

Each module is self-contained; see docstrings for the API:

- `epidemiology_ledger.ledgers` — The base class for append-only ledgers.
- `epidemiology_ledger.events` — Defines the event classes and their relationships to each other.
- `epidemiology_ledger.hashchain` — Handles hash-chaining of events in a tamper-evident manner.
- `epidemiology_ledger.ledger_manager` — Manages the creation, reading, and writing of ledgers.
- `epidemiology_ledger.tests_test_ledger` — Unit tests for the append-only ledger functionality.
- `epidemiology_ledger.core` — main domain logic and public entry points
