from copy import deepcopy
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


def test_negative_monodromy_fixture_fails():
    ledger = h.build_ledger(N=2)
    bad = deepcopy(ledger)
    bad["sections"]["monodromy"]["distinguished_eigenvalue"] = 1
    errors = h.validate_ledger(bad)
    assert "distinguished monodromy eigenvalue is not -1" in errors


def test_negative_spin_endpoint_fixture_fails():
    ledger = h.build_ledger(N=2)
    bad = deepcopy(ledger)
    bad["sections"]["spin_lift"]["endpoint_error"] = 1.0
    errors = h.validate_ledger(bad)
    assert "Spin lift endpoint is not -I within tolerance" in errors


def test_negative_stokes_fixture_fails():
    ledger = h.build_ledger(N=2)
    bad = deepcopy(ledger)
    bad["sections"]["stokes"]["stokes_multiplier_observed"] = 1
    errors = h.validate_ledger(bad)
    assert "Stokes multiplier is not -1" in errors


def test_negative_hash_chain_fixture_fails():
    ledger = h.build_ledger(N=2)
    bad = deepcopy(ledger)
    bad["sections"]["coefficients"]["values"][0] = 999
    errors = h.validate_ledger(bad)
    assert "coefficient mismatch" in errors
    assert "hash_chain mismatch" in errors
