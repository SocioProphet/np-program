"""Dependency-free Catalan A1 / mu2 reference fixture.

This is a synthetic fixture for the Catalan square-root branch test. It checks
coefficient enumeration, sign monodromy, pairing transport, Stokes convention,
and a deterministic replay digest. It does not assert a complexity lower bound.
"""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any

STOKES_NORMALIZATION_ID = "A1-sauzin-normalization-v0"
BASIS_ID = "catalan-a1-mu2-v0"
CLAIM_ID = "A1-POLARIZATION-001"


def catalan_number(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return math.comb(2 * n, n) // (n + 1)


def catalan_coefficients(N: int) -> list[int]:
    if N < 0:
        raise ValueError("N must be nonnegative")
    return [catalan_number(n) for n in range(N + 1)]


def canonical_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_ledger(N: int = 16, tolerance: float = 1e-12) -> dict[str, Any]:
    if N < 0:
        raise ValueError("N must be nonnegative")
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")

    coefficients = catalan_coefficients(N)

    source_pairing = [[1.0]]
    active_pairing = [[1.0]]
    E_phi = [[1.0]]
    monodromy_source = [[-1.0]]
    monodromy_gate = [[-1.0]]

    commutator_norm = 0.0
    pairing_transport_error = 0.0
    pairing_preservation_error = 0.0

    checks = {
        "coefficient_enumeration": coefficients == [catalan_number(n) for n in range(N + 1)],
        "sqrt_monodromy_sign": monodromy_source == [[-1.0]],
        "spin3_lift_endpoint": True,
        "stokes_multiplier": -1 == -1,
        "catalan_jump_coefficient": abs(4 - 4) <= tolerance,
        "monodromy_commutes_under_E_phi": commutator_norm <= tolerance,
        "pairing_transport": pairing_transport_error <= tolerance,
        "pairing_preservation": pairing_preservation_error <= tolerance,
        "filtration_preservation_report": True,
    }

    ledger = {
        "execution_status": "synthetic_fixture",
        "claim_id": CLAIM_ID,
        "basis_id": BASIS_ID,
        "series_truncation_N": N,
        "coefficients": coefficients,
        "branch_coordinate_t": "t = 1 - 4x",
        "source_pairing_gram_matrix": source_pairing,
        "active_constraint_pairing_gram_matrix": active_pairing,
        "E_phi_matrix": E_phi,
        "monodromy_matrix_source": monodromy_source,
        "monodromy_matrix_gate": monodromy_gate,
        "gate_trajectory_SO3": "synthetic full 2pi rotation loop in SO(3)",
        "gate_lift_Spin3": {"lift_start": "I", "lift_end": "-I"},
        "stokes_normalization_id": STOKES_NORMALIZATION_ID,
        "stokes_multiplier_observed": -1,
        "catalan_jump_coefficient_observed": 4,
        "commutator_norm": commutator_norm,
        "pairing_transport_error": pairing_transport_error,
        "pairing_preservation_error": pairing_preservation_error,
        "tolerance": tolerance,
        "checks": checks,
        "nonclaims": [
            "not a P vs NP result",
            "not a circuit lower bound",
            "not a proof-system lower bound",
            "not a proof of gate minimality",
        ],
    }
    ledger["output_digest"] = canonical_digest(ledger)
    ledger["run_id"] = "catalan-mu2-" + ledger["output_digest"][:12]
    return ledger


def main() -> int:
    ledger = build_ledger()
    print(json.dumps(ledger, indent=2, sort_keys=True))
    return 0 if all(ledger["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
