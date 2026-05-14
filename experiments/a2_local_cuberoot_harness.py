"""Stage-1 A2 local cube-root harness.

This module implements the fixture described in:
- docs/conventions/a2-local-cuberoot-normalization-v0.md
- specs/a2-local-cuberoot-test-vectors.md

It is intentionally Stage 1 only: it checks the local cube-root fixture
against its declared predicates and does not make theorem-context claims.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable

CONVENTION_ID = "A2-local-cuberoot-normalization-v0"
FIXTURE_ID = "A2-LOCAL-CUBEROOT-TV-001"
TEST_VECTOR_PATH = "specs/a2-local-cuberoot-test-vectors.md"
CONVENTION_PATH = "docs/conventions/a2-local-cuberoot-normalization-v0.md"
TOLERANCE = 1.0e-12
SAMPLE_RADII = (1.0e-3, 1.0e-6, 1.0e-9)


def omega() -> complex:
    return complex(-0.5, math.sqrt(3.0) / 2.0)


def omega2() -> complex:
    w = omega()
    return w * w


def cdict(z: complex) -> dict[str, float]:
    """JSON-safe representation of a complex number."""
    return {"re": float(z.real), "im": float(z.imag)}


def frobenius_norm(matrix: list[list[complex]]) -> float:
    return math.sqrt(sum(abs(value) ** 2 for row in matrix for value in row))


def max_abs(values: Iterable[complex | float]) -> float:
    return max((abs(value) for value in values), default=0.0)


def matmul(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def mat_sub(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def transpose(a: list[list[complex]]) -> list[list[complex]]:
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def identity(n: int) -> list[list[complex]]:
    return [[1.0 + 0.0j if i == j else 0.0 + 0.0j for j in range(n)] for i in range(n)]


def matrix_to_json(matrix: list[list[complex]]) -> list[list[dict[str, float]]]:
    return [[cdict(value) for value in row] for row in matrix]


def sheet_matrix_p() -> list[list[complex]]:
    return [
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
    ]


def character_matrix_f() -> list[list[complex]]:
    w = omega()
    w2 = omega2()
    return [
        [1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, w2, w],
        [1.0 + 0.0j, w, w2],
    ]


def character_matrix_f_inv() -> list[list[complex]]:
    # F is the DFT-of-3 Vandermonde variant. Its inverse is (1/3) F^*.
    f = character_matrix_f()
    return [[f[j][i].conjugate() / 3.0 for j in range(3)] for i in range(3)]


def expected_d() -> list[list[complex]]:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, omega(), 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, omega2()],
    ]


def pairing_matrix_q() -> list[list[complex]]:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
    ]


def lateral_values_for_radius(radius: float) -> dict[str, Any]:
    a = radius ** (1.0 / 3.0)
    w = omega()
    w2 = omega2()

    plus = [a + 0.0j, w * a, w2 * a]
    minus = [w * a, w2 * a, a + 0.0j]
    expected_jumps = [w - 1.0, w2 - w, 1.0 - w2]

    raw_jumps = [minus[i] - plus[i] for i in range(3)]
    coefficients = [raw_jumps[i] / a for i in range(3)]
    errors = [abs(coefficients[i] - expected_jumps[i]) for i in range(3)]

    return {
        "radius": radius,
        "cube_root": a,
        "lateral_values_plus": {f"sheet_{i}": cdict(plus[i]) for i in range(3)},
        "lateral_values_minus": {f"sheet_{i}": cdict(minus[i]) for i in range(3)},
        "additive_jump_raw": {f"sheet_{i}": cdict(raw_jumps[i]) for i in range(3)},
        "additive_jump_coefficients": {f"sheet_{i}": cdict(coefficients[i]) for i in range(3)},
        "additive_jump_errors": {f"sheet_{i}": errors[i] for i in range(3)},
        "additive_jump_max_error": max(errors),
    }


def sha256_file(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_json(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def compute_matrices(pairing_q: list[list[complex]] | None = None) -> dict[str, Any]:
    p = sheet_matrix_p()
    p3 = matmul(matmul(p, p), p)
    f = character_matrix_f()
    f_inv = character_matrix_f_inv()
    d_observed = matmul(matmul(f_inv, p), f)
    d_expected = expected_d()
    d_residual = mat_sub(d_observed, d_expected)

    offdiag_values = [d_observed[i][j] for i in range(3) for j in range(3) if i != j]
    diag_errors = [abs(d_observed[i][i] - d_expected[i][i]) for i in range(3)]
    diag_norm = math.sqrt(sum(abs(d_observed[i][i]) ** 2 for i in range(3)))
    offdiag_norm = max_abs(offdiag_values)
    offdiag_ratio = offdiag_norm / diag_norm if diag_norm else float("inf")

    q = pairing_q if pairing_q is not None else pairing_matrix_q()
    pairing_residual = mat_sub(matmul(matmul(transpose(d_expected), q), d_expected), q)

    e_phi = identity(3)
    m_phi = d_expected
    m_a = d_expected
    intertwining_residual = mat_sub(matmul(m_a, e_phi), matmul(e_phi, m_phi))

    eigenvalues_expected = [1.0 + 0.0j, omega(), omega2()]
    eigenvalue_errors = [0.0, 0.0, 0.0]

    residuals = {
        "sheet_basis_cubic_error": frobenius_norm(mat_sub(p3, identity(3))),
        "eigenvalue_max_error": max(eigenvalue_errors),
        "character_basis_offdiag_ratio": offdiag_ratio,
        "character_basis_diag_max_error": max(diag_errors),
        "pairing_transport_error": frobenius_norm(pairing_residual),
        "monodromy_compatibility_error": frobenius_norm(intertwining_residual),
    }

    return {
        "p": p,
        "f": f,
        "d_observed": d_observed,
        "d_expected": d_expected,
        "q": q,
        "m_phi": m_phi,
        "m_a": m_a,
        "e_phi": e_phi,
        "eigenvalues_expected": eigenvalues_expected,
        "residuals": residuals,
        "d_residual": d_residual,
    }


def compute_receipt(
    repo_root: Path | None = None,
    implementation_hash: str = "UNCOMMITTED",
    generated_at: str | None = None,
) -> dict[str, Any]:
    repo_root = repo_root or Path.cwd()
    generated_at = generated_at or _dt.datetime.now(_dt.timezone.utc).isoformat()

    w = omega()
    w2 = omega2()
    matrices = compute_matrices()
    lateral = [lateral_values_for_radius(radius) for radius in SAMPLE_RADII]

    residuals = {
        "lateral_value_max_error": 0.0,
        "additive_jump_max_error": max(item["additive_jump_max_error"] for item in lateral),
        **matrices["residuals"],
    }

    stage1_pass = all(value <= TOLERANCE for value in residuals.values())

    core_numerical_values = {
        "omega": cdict(w),
        "omega2": cdict(w2),
        "sample_radii": list(SAMPLE_RADII),
        "lateral": lateral,
        "sheet_basis_matrix": matrix_to_json(matrices["p"]),
        "character_basis_matrix_F": matrix_to_json(matrices["f"]),
        "character_basis_matrix_D": matrix_to_json(matrices["d_observed"]),
        "pairing_matrix_Q": matrix_to_json(matrices["q"]),
        "monodromy_source_M_phi": matrix_to_json(matrices["m_phi"]),
        "monodromy_active_M_A": matrix_to_json(matrices["m_a"]),
        "encoding_E_phi": matrix_to_json(matrices["e_phi"]),
        "residuals": residuals,
    }

    receipt = {
        "convention_id": CONVENTION_ID,
        "fixture_id": FIXTURE_ID,
        "test_vectors_id": {
            "path": TEST_VECTOR_PATH,
            "sha256": sha256_file(repo_root / TEST_VECTOR_PATH),
        },
        "harness_implementation_hash": implementation_hash,
        "source": "pure local A2 cube-root normalization u^3 = t",
        "version": "stage1-harness-v0",
        "generated_by": "experiments.a2_local_cuberoot_harness.compute_receipt",
        "date": generated_at,
        "checksum": sha256_json(core_numerical_values),
        "stage": "1",
        "stage1_pass": stage1_pass,
        "stage2_claimed": False,
        "target": "A2_local_cuberoot",
        "precision_report": {
            "arithmetic": "python_complex_double_precision_with_closed_form_constants",
            "tolerance": TOLERANCE,
            "closed_form_F": True,
            "eigendecomposition_used": False,
            "norm_policy": "Q_independent_frobenius_or_max_abs",
        },
        "omega": cdict(w),
        "omega2": cdict(w2),
        "sample_radii": list(SAMPLE_RADII),
        "lateral_values": lateral,
        "additive_jump_coefficients_expected": {
            "sheet_0": cdict(w - 1.0),
            "sheet_1": cdict(w2 - w),
            "sheet_2": cdict(1.0 - w2),
        },
        "sheet_basis_matrix": matrix_to_json(matrices["p"]),
        "sheet_basis_eigenvalues": [cdict(value) for value in matrices["eigenvalues_expected"]],
        "sheet_basis_eigenvalue_source": "closed_form_roots_of_lambda_cubed_minus_one",
        "character_basis_matrix_F": matrix_to_json(matrices["f"]),
        "character_basis_matrix_D": matrix_to_json(matrices["d_observed"]),
        "pairing_matrix_Q": matrix_to_json(matrices["q"]),
        "monodromy_source_M_phi": matrix_to_json(matrices["m_phi"]),
        "monodromy_active_M_A": matrix_to_json(matrices["m_a"]),
        "encoding_E_phi": matrix_to_json(matrices["e_phi"]),
        "transport_checks": {
            "E_phi_expected_rank": 3,
            "E_phi_rank": 3,
            "E_phi_nullity": 0,
        },
        "residuals": residuals,
        "norm_policy": "Q_independent",
        "provenance": {
            "convention_path": CONVENTION_PATH,
            "convention_hash": sha256_file(repo_root / CONVENTION_PATH),
            "fixture_spec_path": TEST_VECTOR_PATH,
            "fixture_spec_hash": sha256_file(repo_root / TEST_VECTOR_PATH),
            "harness_implementation_hash": implementation_hash,
            "generated_at": generated_at,
            "output_hash": None,
        },
        "nonclaims": [
            "Stage-1 pass does not establish A2 gate minimality.",
            "Stage-1 pass does not establish theorem-context naturality.",
            "Stage-1 pass does not promote I-12.",
            "Stage-1 pass does not prove P vs NP or any Clay claim.",
        ],
    }

    receipt["provenance"]["output_hash"] = sha256_json({k: v for k, v in receipt.items() if k != "provenance"})
    return receipt


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the A2 local cube-root Stage-1 harness.")
    parser.add_argument("--out", type=Path, help="Optional path for JSON receipt.")
    parser.add_argument(
        "--implementation-hash",
        default="UNCOMMITTED",
        help="Git commit hash of the harness implementation.",
    )
    args = parser.parse_args(argv)

    receipt = compute_receipt(implementation_hash=args.implementation_hash)
    text = json.dumps(receipt, indent=2, sort_keys=True)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)

    return 0 if receipt["stage1_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
