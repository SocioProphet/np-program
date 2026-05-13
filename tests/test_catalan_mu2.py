from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments" / "catalan_mu2"))

import catalan_mu2_harness as h


def test_catalan_numbers():
    assert h.catalan_coefficients(10) == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]


def test_generated_ledger_validates():
    ledger = h.build_ledger(N=10)
    assert h.validate_ledger(ledger) == []


def test_sample_ledger_validates():
    path = ROOT / "ledgers" / "catalan_mu2" / "sample_ledger.json"
    ledger = json.loads(path.read_text(encoding="utf-8"))
    assert h.validate_ledger(ledger) == []


def test_spin_lift_endpoint_is_minus_identity():
    ledger = h.build_ledger(N=2)
    end = ledger["sections"]["spin_lift"]["lift_end"]
    assert end == [[[-1.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [-1.0, 0.0]]]


def test_stokes_convention_hard_check():
    ledger = h.build_ledger(N=2)
    stokes = ledger["sections"]["stokes"]
    assert stokes["stokes_normalization_id"] == "A1-sauzin-normalization-v0"
    assert stokes["stokes_multiplier_observed"] == -1
    assert stokes["catalan_jump_coefficient_observed"] == 4
