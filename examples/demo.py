"""Demo for Epidemiology Append-Only Ledger."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import epidemiology_ledger

print("Epidemiology Append-Only Ledger", "v" + epidemiology_ledger.__version__)
print("modules:", [m for m in dir(epidemiology_ledger) if not m.startswith('_')])
