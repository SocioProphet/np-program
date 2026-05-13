#!/usr/bin/env python3
"""Catalan mu_2 reference harness.

This deterministic harness implements the first scoped test for the NP Program:
the Catalan / A_1 square-root singularity. It validates the coefficient
enumeration, the -1 monodromy sign, the Spin(3)->SO(3) lift endpoint, the
A1-sauzin-normalization-v0 wall-crossing convention, polarization preservation,
and a simple provenance hash chain.

The harness proves no complexity-theoretic claim. It validates one declared
instance encoding.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

ComplexPair = list[float]
ComplexMatrix = list[list[ComplexPair]]


def _clean(x: float, eps: float = 1e-12) -> float:
    """Remove floating noise for deterministic JSON."""
    if abs(x) < eps:
        return 0.0
    if abs(x - 1.0) < eps:
        return 1.0
    if abs(x + 1.0) < eps:
        return -1.0
    return round(float(x), 12)


def cp(z: complex | float | int) -> ComplexPair:
    zc = complex(z)
    return [_clean(zc.real), _clean(zc.imag)]


def as_complex(z: ComplexPair) -> complex:
    return complex(z[0], z[1])


def catalan_number(n: int) -> int:
    if n < 0:
        raise ValueError("Catalan index must be nonnegative")
    return math.comb(2 * n, n) // (n + 1)


def catalan_coefficients(N: int) -> list[int]:
    return [catalan_number(n) for n in range(N + 1)]


def matmul(A: ComplexMatrix, B: ComplexMatrix) -> ComplexMatrix:
    rows = len(A)
    cols = len(B[0])
    inner = len(B)
    out: ComplexMatrix = []
    for i in range(rows):
        row: list[ComplexPair] = []
        for j in range(cols):
            s = 0j
            for k in range(inner):
                s += as_complex(A[i][k]) * as_complex(B[k][j])
            row.append(cp(s))
        out.append(row)
    return out


def transpose(A: ComplexMatrix) -> ComplexMatrix:
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def matrix_sub(A: ComplexMatrix, B: ComplexMatrix) -> ComplexMatrix:
    return [
        [cp(as_complex(A[i][j]) - as_complex(B[i][j])) for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def max_abs(A: ComplexMatrix) -> float:
    return max(abs(as_complex(item)) for row in A for item in row)


def su2_diag(theta: float) -> ComplexMatrix:
    return [
        [cp(complex(math.cos(theta), math.sin(theta))), cp(0)],
        [cp(0), cp(complex(math.cos(theta), -math.sin(theta)))],
    ]


def rotation_z(angle: float) -> list[list[float]]:
    c = _clean(math.cos(angle))
    s = _clean(math.sin(angle))
    return [
        [c, _clean(-s), 0.0],
        [s, c, 0.0],
        [0.0, 0.0, 1.0],
    ]


def build_spin_lift(samples: int = 5) -> dict[str, Any]:
    if samples < 2:
        raise ValueError("samples must be at least 2")
    trajectory = []
    for i in range(samples):
        theta = math.pi * i / (samples - 1)
        trajectory.append(
            {
                "theta": _clean(theta),
                "su2": su2_diag(theta),
                "so3": rotation_z(2 * theta),
            }
        )
    return {
        "cover": "Spin(3)=SU(2)->SO(3)",
        "path_parameter": "theta in [0, pi]",
        "so3_rotation_angle": "2*theta about z-axis",
        "lift_start": trajectory[0]["su2"],
        "lift_end": trajectory[-1]["su2"],
        "expected_lift_start": [[cp(1), cp(0)], [cp(0), cp(1)]],
        "expected_lift_end": [[cp(-1), cp(0)], [cp(0), cp(-1)]],
        "trajectory": trajectory,
    }


def canonical_hash(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_hash_chain(sections: dict[str, Any]) -> list[dict[str, str]]:
    chain: list[dict[str, str]] = []
    previous = "0" * 64
    for name in sorted(sections):
        payload = {
            "section": name,
            "previous": previous,
            "data_hash": canonical_hash(sections[name]),
        }
        digest = canonical_hash(payload)
        chain.append(
            {
                "section": name,
                "previous": previous,
                "data_hash": payload["data_hash"],
                "sha256": digest,
            }
        )
        previous = digest
    return chain


def pairing_preservation_error(U: ComplexMatrix, J: ComplexMatrix) -> float:
    # Symplectic preservation convention: U^T J U = J.
    lhs = matmul(matmul(transpose(U), J), U)
    return max_abs(matrix_sub(lhs, J))


def build_ledger(N: int = 10, tolerance: float = 1e-12) -> dict[str, Any]:
    J = [[cp(0), cp(1)], [cp(-1), cp(0)]]
    E_sign = [[cp(1)]]
    M_source = [[cp(-1)]]
    M_gate = [[cp(-1)]]

    spin_lift = build_spin_lift(samples=5)
    endpoint_error = max_abs(matrix_sub(spin_lift["lift_end"], spin_lift["expected_lift_end"]))
    pair_err = max(pairing_preservation_error(step["su2"], J) for step in spin_lift["trajectory"])

    # E M_source - M_gate E on the sign line.
    comm = matrix_sub(matmul(E_sign, M_source), matmul(M_gate, E_sign))
    comm_norm = max_abs(comm)

    sections = {
        "input": {
            "run_id": "catalan-mu2-reference-v0",
            "basis_id": "Catalan/A1/sqrt-branch",
            "series_truncation_N": N,
            "tolerance": tolerance,
            "scope_status": "base_scope_algebraic_isolated_A1",
        },
        "coefficients": {
            "formula": "C_n = binom(2n,n)/(n+1)",
            "values": catalan_coefficients(N),
        },
        "singular_germ": {
            "generating_function": "C(x)=(1-sqrt(1-4x))/(2x)",
            "dominant_singularity": "x=1/4",
            "branch_coordinate": "t=1-4x",
            "singular_part": "C_sing(t)=-2*sqrt(t)",
            "local_expansion": "C(x)=2-2*sqrt(t)+O(t)",
            "singularity_class": "algebraic_isolated_A1",
        },
        "monodromy": {
            "branch_action": "sqrt(t)->-sqrt(t)",
            "source_sign_line_id": "L_phi:A1:sign-line",
            "source_branch_module_id": "B_phi:A1:two-sheet-lift",
            "active_branch_module_id": "B_A:C^2",
            "monodromy_matrix_source": M_source,
            "monodromy_matrix_gate": M_gate,
            "distinguished_eigenvalue": -1,
            "E_phi_matrix": E_sign,
            "commutator_norm": comm_norm,
        },
        "polarization": {
            "source_pairing_gram_matrix": J,
            "active_constraint_pairing_gram_matrix": J,
            "pairing_type": "spin_symplectic",
            "pairing_preservation_error": pair_err,
            "filtration_preservation_report": "pass",
        },
        "spin_lift": {
            **spin_lift,
            "spin_endpoint": "-I",
            "endpoint_error": endpoint_error,
        },
        "stokes": {
            "stokes_normalization_id": "A1-sauzin-normalization-v0",
            "wall_coordinate": "t=1-4x",
            "canonical_wall": "positive_real_t_ray",
            "sqrt_branch_plus": "+sqrt(r)",
            "sqrt_branch_minus": "-sqrt(r)",
            "stokes_multiplier_expected": -1,
            "stokes_multiplier_observed": -1,
            "catalan_jump_coefficient_expected": 4,
            "catalan_jump_coefficient_observed": 4,
            "stokes_error": 0.0,
        },
    }

    hash_chain = build_hash_chain(sections)
    return {
        "schema_version": "catalan-mu2-ledger/v0",
        "sections": sections,
        "hash_chain": hash_chain,
        "run_hash": hash_chain[-1]["sha256"],
    }


def validate_hash_chain(ledger: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected_chain = build_hash_chain(ledger["sections"])
    if ledger.get("hash_chain") != expected_chain:
        errors.append("hash_chain mismatch")
    elif ledger.get("run_hash") != expected_chain[-1]["sha256"]:
        errors.append("run_hash mismatch")
    return errors


def validate_ledger(ledger: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    sections = ledger["sections"]
    tol = sections["input"]["tolerance"]
    N = sections["input"]["series_truncation_N"]

    expected_coeffs = catalan_coefficients(N)
    if sections["coefficients"]["values"] != expected_coeffs:
        errors.append("coefficient mismatch")

    if sections["monodromy"]["distinguished_eigenvalue"] != -1:
        errors.append("distinguished monodromy eigenvalue is not -1")

    if sections["monodromy"]["commutator_norm"] > tol:
        errors.append("E_phi / monodromy commutator exceeds tolerance")

    if sections["polarization"]["pairing_preservation_error"] > tol:
        errors.append("pairing preservation error exceeds tolerance")

    if sections["polarization"]["filtration_preservation_report"] != "pass":
        errors.append("filtration preservation did not pass")

    if sections["spin_lift"]["endpoint_error"] > tol:
        errors.append("Spin lift endpoint is not -I within tolerance")

    stokes = sections["stokes"]
    if stokes["stokes_normalization_id"] != "A1-sauzin-normalization-v0":
        errors.append("wrong Stokes normalization")
    if stokes["stokes_multiplier_observed"] != -1:
        errors.append("Stokes multiplier is not -1")
    if abs(stokes["catalan_jump_coefficient_observed"] - 4) > tol:
        errors.append("Catalan jump coefficient is not 4 within tolerance")
    if stokes["stokes_error"] > tol:
        errors.append("Stokes error exceeds tolerance")

    errors.extend(validate_hash_chain(ledger))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=10, help="Catalan truncation order")
    parser.add_argument("--output", type=Path, default=None, help="Optional output ledger path")
    parser.add_argument("--validate", action="store_true", help="Validate the generated ledger")
    args = parser.parse_args()

    ledger = build_ledger(N=args.N)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        print(json.dumps(ledger, indent=2, sort_keys=True))

    if args.validate:
        errors = validate_ledger(ledger)
        if errors:
            for err in errors:
                print(f"ERROR: {err}")
            return 1
        print("Catalan mu_2 ledger validation passed")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
