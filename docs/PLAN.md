# Architecture Plan

- `epidemiology_ledger/ledgers.py` — The base class for append-only ledgers.
- `epidemiology_ledger/events.py` — Defines the event classes and their relationships to each other.
- `epidemiology_ledger/hashchain.py` — Handles hash-chaining of events in a tamper-evident manner.
- `epidemiology_ledger/ledger_manager.py` — Manages the creation, reading, and writing of ledgers.
- `epidemiology_ledger/tests_test_ledger.py` — Unit tests for the append-only ledger functionality.
- `epidemiology_ledger/core.py` — main domain logic and public entry points
