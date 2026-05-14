"""Dependency-free Catalan A1 / mu2 reference fixture.

This synthetic fixture validates the Catalan square-root branch test with
explicit matrix checks and a structured replay ledger. It does not assert a
complexity lower bound, a proof-system lower bound, or P vs NP progress.
"""

from __future__ import annotations

import hashlib
import json
import math
from copy import deepcopy
from typing import Any

STOKES_NORMALIZATION_ID = "A1-sauzin-normalization-v0"
BASIS_ID = "catalan-a1-mu2-v0"
CLAIM_ID = "A1-POLARIZATION-001"

Matrix = list[list[float]]


def catalan_number(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return math.comb(2 * n, n) // (n + 1)


def catalan_coefficients(N: int) -> list[int]:
    if N < 0:
        raise ValueError("N must be nonnegative")
    return [catalan_number(n) for n in range(N + 1)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def transpose(matrix: Matrix) -> Matrix:
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


def matsub(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right)):
        raise ValueError("incompatible matrix dimensions")
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(left, right)]


def frobenius_norm(matrix: Matrix) -> float:
    return math.sqrt(sum(entry * entry for row in matrix for entry in row))


def canonical_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _within(value: float, tolerance: float) -> bool:
    return abs(value) <= tolerance


def default_fixture() -> dict[str, Any]:
    return {
        "source": {
            "germ": "A1",
            "source_basis": ["e"],
            "source_pairing_gram_matrix": [[1.0]],
            "monodromy_matrix_source": [[-1.0]],
            "conventions_hash": canonical_digest({"stokes": STOKES_NORMALIZATION_ID}),
        },
        "active": {
            "active_basis": ["v_minus"],
            "active_constraint_pairing_gram_matrix": [[1.0]],
            "monodromy_matrix_gate": [[-1.0]],
            "gate_group": "SO(3)",
            "gate_loop": "synthetic full 2pi rotation loop in SO(3)",
            "gate_lift_Spin3": {"lift_start": "I", "lift_end": "-I"},
        },
        "encoding": {
            "E_phi_matrix": [[1.0]],
            "declared_before_evaluation": True,
        },
        "filtration": {
            "source_filtration": {"level_0": ["e"]},
            "active_filtration": {"level_0": ["v_minus"]},
            "filtration_preservation_report": "pass",
        },
        "stokes": {
            "stokes_normalization_id": STOKES_NORMALIZATION_ID,
            "stokes_multiplier_observed": -1,
            "catalan_jump_coefficient_observed": 4,
        },
    }


def evaluate_fixture(fixture: dict[str, Any], N: int = 16, tolerance: float = 1e-12) -> dict[str, Any]:
    if N < 0:
        raise ValueError("N must be nonnegative")
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")

    coefficients = catalan_coefficients(N)
    source = fixture["source"]
    active = fixture["active"]
    encoding = fixture["encoding"]
    filtration = fixture["filtration"]
    stokes = fixture["stokes"]

    source_pairing = source["source_pairing_gram_matrix"]
    active_pairing = active["active_constraint_pairing_gram_matrix"]
    E_phi = encoding["E_phi_matrix"]
    monodromy_source = source["monodromy_matrix_source"]
    monodromy_gate = active["monodromy_matrix_gate"]

    commutator = matsub(matmul(monodromy_gate, E_phi), matmul(E_phi, monodromy_source))
    transported_pairing = matmul(matmul(transpose(E_phi), active_pairing), E_phi)
    pairing_transport_delta = matsub(transported_pairing, source_pairing)
    preserved_pairing = matmul(matmul(transpose(monodromy_gate), active_pairing), monodromy_gate)
    pairing_preservation_delta = matsub(preserved_pairing, active_pairing)

    commutator_norm = frobenius_norm(commutator)
    pairing_transport_error = frobenius_norm(pairing_transport_delta)
    pairing_preservation_error = frobenius_norm(pairing_preservation_delta)

    expected_coefficients = [catalan_number(n) for n in range(N + 1)]
    checks = {
        "coefficient_enumeration": coefficients == expected_coefficients,
        "source_pairing_nonzero": source_pairing != [[0.0]],
        "E_declared_before_evaluation": bool(encoding["declared_before_evaluation"]),
        "sqrt_monodromy_sign": monodromy_source == [[-1.0]],
        "spin3_lift_endpoint": active["gate_lift_Spin3"] == {"lift_start": "I", "lift_end": "-I"},
        "stokes_normalization": stokes["stokes_normalization_id"] == STOKES_NORMALIZATION_ID,
        "stokes_multiplier": stokes["stokes_multiplier_observed"] == -1,
        "catalan_jump_coefficient": abs(stokes["catalan_jump_coefficient_observed"] - 4) <= tolerance,
        "monodromy_commutes_under_E_phi": _within(commutator_norm, tolerance),
        "pairing_transport": _within(pairing_transport_error, tolerance),
        "pairing_preservation": _within(pairing_preservation_error, tolerance),
        "filtration_preservation_report": filtration["filtration_preservation_report"] == "pass",
    }

    replay_payload = {
        "source": source,
        "active": active,
        "encoding": encoding,
        "filtration": filtration,
        "stokes": stokes,
        "checks": checks,
        "computed": {
            "commutator": commutator,
            "transported_pairing": transported_pairing,
            "preserved_pairing": preserved_pairing,
            "commutator_norm": commutator_norm,
            "pairing_transport_error": pairing_transport_error,
            "pairing_preservation_error": pairing_preservation_error,
        },
    }

    output_digest = canonical_digest(replay_payload)
    return {
        "run_id": "catalan-mu2-" + output_digest[:12],
        "execution_status": "synthetic_fixture",
        "claim_id": CLAIM_ID,
        "basis_id": BASIS_ID,
        "series_truncation_N": N,
        "coefficients": coefficients,
        "branch_coordinate_t": "t = 1 - 4x",
        "source": source,
        "active": active,
        "encoding": encoding,
        "filtration": filtration,
        "stokes": stokes,
        "checks": checks,
        "computed": replay_payload["computed"],
        "tolerance": tolerance,
        "output_digest": output_digest,
        "hash_chain": [
            canonical_digest({"label": "coefficients", "payload": coefficients}),
            canonical_digest({"label": "source", "payload": source}),
            canonical_digest({"label": "active", "payload": active}),
            canonical_digest({"label": "encoding", "payload": encoding}),
            canonical_digest({"label": "checks", "payload": checks}),
        ],
        "nonclaims": [
            "not a P vs NP result",
            "not a circuit lower bound",
            "not a proof-system lower bound",
            "not a proof of gate minimality",
        ],
    }


def build_ledger(N: int = 16, tolerance: float = 1e-12) -> dict[str, Any]:
    return evaluate_fixture(default_fixture(), N=N, tolerance=tolerance)


def mutated_ledger(mutation: str, N: int = 16, tolerance: float = 1e-12) -> dict[str, Any]:
    fixture = deepcopy(default_fixture())
    if mutation == "post_selected_eigendirection":
        fixture["encoding"]["declared_before_evaluation"] = False
    elif mutation == "missing_pairing":
        fixture["source"]["source_pairing_gram_matrix"] = [[0.0]]
    elif mutation == "wrong_stokes_normalization":
        fixture["stokes"]["stokes_normalization_id"] = "wrong-normalization"
    elif mutation == "wrong_monodromy_sign":
        fixture["source"]["monodromy_matrix_source"] = [[1.0]]
    elif mutation == "wrong_active_pairing":
        fixture["active"]["active_constraint_pairing_gram_matrix"] = [[2.0]]
    elif mutation == "failed_filtration":
        fixture["filtration"]["filtration_preservation_report"] = "fail"
    else:
        raise ValueError(f"unknown mutation: {mutation}")
    return evaluate_fixture(fixture, N=N, tolerance=tolerance)


def main() -> int:
    ledger = build_ledger()
    print(json.dumps(ledger, indent=2, sort_keys=True))
    return 0 if all(ledger["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
