# Epidemiology Append-Only Ledger

This project provides an append-only ledger designed to track the progression of diseases, ensuring that any attempt to alter or manipulate historical data is detectable through its tamper-evident hash-chain architecture. Built using pure Python, this system includes comprehensive testing and documentation for ease of use and integration into disease spread modeling applications. Its append-only nature ensures a permanent record of events, providing a secure foundation for epidemiological analysis.

## What makes it unique

Combines disease spread modeling with a tamper-evident hash-chained event log — a niche where few ready-made tools exist.

## Features

- **`epidemiology_ledger/ledgers.py`** — The base class for append-only ledgers.
- **`epidemiology_ledger/events.py`** — Defines the event classes and their relationships to each other.
- **`epidemiology_ledger/hashchain.py`** — Handles hash-chaining of events in a tamper-evident manner.
- **`epidemiology_ledger/ledger_manager.py`** — Manages the creation, reading, and writing of ledgers.
- **`epidemiology_ledger/tests_test_ledger.py`** — Unit tests for the append-only ledger functionality.
- **`epidemiology_ledger/core.py`** — main domain logic and public entry points

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/epidemiology-ledger.git
cd epidemiology-ledger

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
epidemiology-ledger/
├── epidemiology_ledger/
│   ├── ledgers.py
│   ├── events.py
│   ├── hashchain.py
│   ├── ledger_manager.py
│   ├── tests_test_ledger.py
│   ├── core.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **epidemiology** · Archetype: **ledger** ·
Built autonomously by JARVIS on 2026-09-27. MIT licensed.
