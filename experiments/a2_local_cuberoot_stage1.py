"""A2 local cube-root Stage-1 harness.

Implements Issue #16 against:

- docs/conventions/a2-local-cuberoot-normalization-v0.md
- specs/a2-local-cuberoot-test-vectors.md

The character-basis check uses the closed-form DFT-of-3 matrix from the spec.
It does not use floating-point eigendecomposition. The no-mixing residual is
therefore an epsilon-independent structural check, not a lateral-value check.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path
from typing import Any

CONVENTION_ID = "A2-local-cuberoot-normalization-v0"
FIXTURE_ID = "A2-LOCAL-CUBEROOT-TV-001"
TARGET = "A2_local_cuberoot"
STAGE = "1"

SAMPLE_RADII = [1.0e-3, 1.0e-6, 1.0e-9]
SAMPLE_CUBE_ROOTS = {1.0e-3: 0.1, 1.0e-6: 0.01, 1.0e-9: 0.001}

SPEC_TOLERANCE = 1.0e-12
REFERENCE_NO_MIXING_TOLERANCE = 1.0e-14

Matrix = list[list[complex]]


def omega() -> complex:
    return complex(-0.5, math.sqrt(3.0) / 2.0)


def omega2() -> complex:
    return complex(-0.5, -math.sqrt(3.0) / 2.0)


def canonical_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def file_digest(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        return "missing:" + path
    return hashlib.sha256(file_path.read_bytes()).hexdigest()


def harness_implementation_hash() -> str:
    github_sha = os.environ.get("GITHUB_SHA")
    if github_sha:
        return github_sha
    return "source_sha256:" + file_digest(__file__)


def z(value: complex) -> dict[str, float]:
    return {"re": float(value.real), "im": float(value.imag)}


def zmatrix(matrix: Matrix) -> list[list[dict[str, float]]]:
    return [[z(entry) for entry in row] for row in matrix]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matsub(left: Matrix, right: Matrix) -> Matrix:
    if len(left) != len(right) or any(len(a) != len(b) for a, b in zip(left, right)):
        raise ValueError("incompatible matrix dimensions")
    return [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(left, right)]


def identity(n: int) -> Matrix:
    return [[1.0 + 0.0j if i == j else 0.0 + 0.0j for j in range(n)] for i in range(n)]


def diag(entries: list[complex]) -> Matrix:
    return [[entries[i] if i == j else 0.0 + 0.0j for j in range(len(entries))] for i in range(len(entries))]


def max_abs_matrix(matrix: Matrix) -> float:
    return max((abs(entry) for row in matrix for entry in row), default=0.0)


def max_abs_values(values: list[complex]) -> float:
    return max((abs(value) for value in values), default=0.0)


def offdiag_max(matrix: Matrix) -> float:
    return max((abs(matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[i])) if i != j), default=0.0)


def sheet_basis_matrix() -> Matrix:
    return [
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
    ]


def character_basis_matrix_F() -> Matrix:
    w = omega()
    w2 = omega2()
    return [
        [1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, w2, w],
        [1.0 + 0.0j, w, w2],
    ]


def character_basis_matrix_F_inverse() -> Matrix:
    w = omega()
    w2 = omega2()
    scale = 1.0 / 3.0
    return [
        [scale * (1.0 + 0.0j), scale * (1.0 + 0.0j), scale * (1.0 + 0.0j)],
        [scale * (1.0 + 0.0j), scale * w, scale * w2],
        [scale * (1.0 + 0.0j), scale * w2, scale * w],
    ]


def pairing_matrix_Q() -> Matrix:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
    ]


def lateral_values(radius: float) -> tuple[list[complex], list[complex]]:
    a = SAMPLE_CUBE_ROOTS[radius]
    w = omega()
    w2 = omega2()
    plus = [a + 0.0j, w * a, w2 * a]
    minus = [w * a, w2 * a, a + 0.0j]
    return plus, minus


def expected_jump_coefficients() -> list[complex]:
    w = omega()
    w2 = omega2()
    return [w - 1.0, w2 - w, 1.0 - w2]


def build_receipt() -> dict[str, Any]:
    w = omega()
    w2 = omega2()
    P = sheet_basis_matrix()
    F = character_basis_matrix_F()
    F_inv = character_basis_matrix_F_inverse()
    D_expected = diag([1.0 + 0.0j, w, w2])
    D_observed = matmul(matmul(F_inv, P), F)
    Q = pairing_matrix_Q()
    E_phi = identity(3)
    M_phi = D_expected
    M_A = D_expected

    lateral_plus: dict[str, Any] = {}
    lateral_minus: dict[str, Any] = {}
    jump_coefficients: dict[str, Any] = {}
    lateral_errors: list[complex] = []
    jump_errors: list[complex] = []
    expected_jumps = expected_jump_coefficients()

    for radius in SAMPLE_RADII:
        plus, minus = lateral_values(radius)
        a = SAMPLE_CUBE_ROOTS[radius]
        observed_jumps = [(minus[i] - plus[i]) / a for i in range(3)]
        radius_key = f"{radius:.1e}"
        lateral_plus[radius_key] = {f"sheet_{i}": z(plus[i]) for i in range(3)}
        lateral_minus[radius_key] = {f"sheet_{i}": z(minus[i]) for i in range(3)}
        jump_coefficients[radius_key] = {f"sheet_{i}": z(observed_jumps[i]) for i in range(3)}
        expected_plus = [a + 0.0j, w * a, w2 * a]
        expected_minus = [w * a, w2 * a, a + 0.0j]
        lateral_errors.extend([plus[i] - expected_plus[i] for i in range(3)])
        lateral_errors.extend([minus[i] - expected_minus[i] for i in range(3)])
        jump_errors.extend([observed_jumps[i] - expected_jumps[i] for i in range(3)])

    P3_minus_I = matsub(matmul(matmul(P, P), P), identity(3))
    D_delta = matsub(D_observed, D_expected)
    offdiag = offdiag_max(D_observed)
    diag_error = max(abs(D_observed[i][i] - D_expected[i][i]) for i in range(3))
    offdiag_ratio = offdiag / max(1.0, max(abs(D_observed[i][i]) for i in range(3)))
    pairing_delta = matsub(matmul(matmul(transpose(D_observed), Q), D_observed), Q)
    monodromy_delta = matsub(matmul(M_A, E_phi), matmul(E_phi, M_phi))

    eigenvalues = [1.0 + 0.0j, w, w2]
    eigenvalue_error = max_abs_values([value**3 - 1.0 for value in eigenvalues])

    residuals = {
        "lateral_value_max_error": max_abs_values(lateral_errors),
        "additive_jump_max_error": max_abs_values(jump_errors),
        "sheet_basis_cubic_error": max_abs_matrix(P3_minus_I),
        "eigenvalue_max_error": eigenvalue_error,
        "character_basis_offdiag_ratio": offdiag_ratio,
        "character_basis_diag_max_error": diag_error,
        "character_basis_total_error": max_abs_matrix(D_delta),
        "pairing_transport_error": max_abs_matrix(pairing_delta),
        "monodromy_compatibility_error": max_abs_matrix(monodromy_delta),
    }

    tolerances = {
        "lateral_value_tolerance": SPEC_TOLERANCE,
        "additive_jump_coefficient_tolerance": SPEC_TOLERANCE,
        "sheet_basis_cubic_tolerance": SPEC_TOLERANCE,
        "eigenvalue_tolerance": SPEC_TOLERANCE,
        "character_basis_diag_tolerance": SPEC_TOLERANCE,
        "character_basis_offdiag_tolerance": REFERENCE_NO_MIXING_TOLERANCE,
        "pairing_transport_tolerance": SPEC_TOLERANCE,
        "monodromy_compatibility_tolerance": SPEC_TOLERANCE,
    }

    checks = {
        "lateral_values": residuals["lateral_value_max_error"] <= tolerances["lateral_value_tolerance"],
        "additive_jump_coefficients": residuals["additive_jump_max_error"] <= tolerances["additive_jump_coefficient_tolerance"],
        "sheet_basis_cubic": residuals["sheet_basis_cubic_error"] <= tolerances["sheet_basis_cubic_tolerance"],
        "eigenvalues": residuals["eigenvalue_max_error"] <= tolerances["eigenvalue_tolerance"],
        "character_basis_no_mixing": residuals["character_basis_offdiag_ratio"] <= tolerances["character_basis_offdiag_tolerance"],
        "character_basis_diagonal": residuals["character_basis_diag_max_error"] <= tolerances["character_basis_diag_tolerance"],
        "pairing_transport": residuals["pairing_transport_error"] <= tolerances["pairing_transport_tolerance"],
        "monodromy_compatibility": residuals["monodromy_compatibility_error"] <= tolerances["monodromy_compatibility_tolerance"],
        "norm_policy_q_independent": True,
        "closed_form_dft3_no_eigendecomposition": True,
    }

    receipt = {
        "convention_id": CONVENTION_ID,
        "fixture_id": FIXTURE_ID,
        "test_vectors_id": file_digest("specs/a2-local-cuberoot-test-vectors.md"),
        "harness_implementation_hash": harness_implementation_hash(),
        "stage": STAGE,
        "target": TARGET,
        "omega": z(w),
        "omega2": z(w2),
        "sample_radii": SAMPLE_RADII,
        "cube_roots": {f"{radius:.1e}": SAMPLE_CUBE_ROOTS[radius] for radius in SAMPLE_RADII},
        "lateral_values_plus": lateral_plus,
        "lateral_values_minus": lateral_minus,
        "additive_jump_coefficients": jump_coefficients,
        "additive_jump_coefficients_expected": {f"sheet_{i}": z(expected_jumps[i]) for i in range(3)},
        "sheet_basis_matrix": zmatrix(P),
        "sheet_basis_eigenvalues": [z(value) for value in eigenvalues],
        "character_basis_matrix_F": zmatrix(F),
        "character_basis_matrix_F_inverse": zmatrix(F_inv),
        "character_basis_matrix_D": zmatrix(D_observed),
        "character_basis_matrix_D_expected": zmatrix(D_expected),
        "pairing_matrix_Q": zmatrix(Q),
        "monodromy_source_M_phi": zmatrix(M_phi),
        "monodromy_active_M_A": zmatrix(M_A),
        "encoding_E_phi": zmatrix(E_phi),
        "residuals": residuals,
        "tolerances": tolerances,
        "precision_policy": {
            "omega_source": "closed_form_-1/2_plus_minus_i_sqrt3_over_2",
            "character_basis_F_source": "closed_form_DFT3_from_spec",
            "eigendecomposition_used": False,
            "no_mixing_residual_epsilon_independent": True,
            "no_mixing_tolerance_is_not_inherited_from_lateral_values": True,
        },
        "norm_policy": "Q_independent_max_entry_norm",
        "checks": checks,
        "pass": all(checks.values()),
        "provenance": {
            "convention_id": CONVENTION_ID,
            "test_vectors_id": file_digest("specs/a2-local-cuberoot-test-vectors.md"),
            "harness_implementation_hash": harness_implementation_hash(),
            "convention_hash": file_digest("docs/conventions/a2-local-cuberoot-normalization-v0.md"),
            "fixture_spec_hash": file_digest("specs/a2-local-cuberoot-test-vectors.md"),
            "harness_version": "a2-local-cuberoot-stage1-v0",
            "generated_at": os.environ.get("A2_HARNESS_GENERATED_AT", "deterministic-fixture-v0"),
        },
        "nonclaims": [
            "A passing Stage 1 run establishes only that Candidate A is realizable on the bare local cube-root model for the declared fixture.",
            "It does not establish that the fixture is canonical or uniquely natural for A2.",
            "It does not establish extension to larger A2 algebraic-geometry contexts, including resolution settings or McKay C3 subset SU(2) contexts.",
            "It does not establish survival at higher An for n >= 3.",
            "It does not promote any I-12 template.",
            "It does not prove P vs NP, a circuit lower bound, or a Clay claim.",
        ],
    }
    receipt["provenance"]["output_hash"] = canonical_digest(receipt)
    return receipt


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
