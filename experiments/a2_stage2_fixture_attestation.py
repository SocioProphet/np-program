"""A2 Stage-2 fixture-only object attestation.

Implements Issue #27. This module does not claim theorem-context naturality,
A2 gate minimality, I-12 promotion, P vs NP, or any Clay result. It attests
five declared fixture objects independently against the consolidated Stage-1
A2 local cube-root receipt.
"""

from __future__ import annotations

import hashlib
import json
import os
from copy import deepcopy
from pathlib import Path
from typing import Any

from experiments import a2_local_cuberoot_stage1 as stage1

EVIDENCE_CLASS = "fixture_only_reproducible_structural_attestation"
VERSION = "a2-stage2-fixture-attestation-v0"
GENERATED_BY = "experiments.a2_stage2_fixture_attestation.build_receipt"
DEFAULT_GENERATED_AT = "2026-05-14T00:00:00Z"
REQUIRED_OBJECT_COUNT = 5

SOURCE_BASIS = ["e_0", "e_1", "e_2"]
ACTIVE_BASIS = ["v_0", "v_1", "v_2"]

Matrix = list[list[complex]]


def canonical_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def file_digest(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        return "missing:" + path
    return hashlib.sha256(file_path.read_bytes()).hexdigest()


def implementation_hash() -> str:
    github_sha = os.environ.get("GITHUB_SHA")
    if github_sha:
        return github_sha
    return "source_sha256:" + file_digest(__file__)


def generated_at() -> str:
    return os.environ.get("A2_STAGE2_GENERATED_AT", DEFAULT_GENERATED_AT)


def _matrix_shape(matrix: Matrix) -> tuple[int, int]:
    return (len(matrix), len(matrix[0]) if matrix else 0)


def _matrix_equal(left: Matrix, right: Matrix, tolerance: float = stage1.SPEC_TOLERANCE) -> bool:
    if _matrix_shape(left) != _matrix_shape(right):
        return False
    return all(abs(left[i][j] - right[i][j]) <= tolerance for i in range(len(left)) for j in range(len(left[0])))


def _status(passed: bool) -> str:
    return "pass" if passed else "fail"


def base_fixture() -> dict[str, Any]:
    omega = stage1.omega()
    omega2 = stage1.omega2()
    diagonal = stage1.diag([1.0 + 0.0j, omega, omega2])
    return {
        "V_A_2": {
            "object_type": "active_fixture_space",
            "dimension": 3,
            "basis": list(ACTIVE_BASIS),
            "evidence_class": EVIDENCE_CLASS,
            "theorem_context_canonical": False,
        },
        "Q_A_2": {
            "object_type": "fixture_pairing",
            "basis": list(ACTIVE_BASIS),
            "matrix": stage1.pairing_matrix_Q(),
            "rank": stage1.matrix_rank(stage1.pairing_matrix_Q()),
            "residual_norm_policy": "Q_independent_max_entry_norm",
            "theorem_context_form_claimed": False,
        },
        "E_phi_2": {
            "object_type": "transport_encoding_map",
            "source_basis": list(SOURCE_BASIS),
            "target_basis": list(ACTIVE_BASIS),
            "matrix": stage1.identity(3),
            "rank": stage1.matrix_rank(stage1.identity(3)),
            "nullity": stage1.nullity(stage1.identity(3)),
            "determinant_or_condition_number_used": False,
            "energy_functional_claimed": False,
        },
        "M_phi_2": {
            "object_type": "source_fixture_monodromy",
            "local_model": "u^3 = t",
            "basis": list(SOURCE_BASIS),
            "matrix": diagonal,
            "eigenvalue_source": "closed_form_omega_values_not_eigendecomposition",
            "theorem_context_monodromy_claimed": False,
        },
        "M_A_2": {
            "object_type": "active_fixture_monodromy",
            "basis": list(ACTIVE_BASIS),
            "matrix": diagonal,
            "theorem_context_gate_action_claimed": False,
            "gate_minimality_claimed": False,
        },
    }


def evaluate_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    expected_diag = stage1.diag([1.0 + 0.0j, stage1.omega(), stage1.omega2()])
    expected_q = stage1.pairing_matrix_Q()
    expected_e = stage1.identity(3)

    q_matrix = fixture["Q_A_2"]["matrix"]
    e_matrix = fixture["E_phi_2"]["matrix"]
    m_phi = fixture["M_phi_2"]["matrix"]
    m_a = fixture["M_A_2"]["matrix"]

    pairing_delta = stage1.matsub(stage1.matmul(stage1.matmul(stage1.transpose(m_a), q_matrix), m_a), q_matrix)
    intertwining_delta = stage1.matsub(stage1.matmul(m_a, e_matrix), stage1.matmul(e_matrix, m_phi))

    q_independent_residual = stage1.q_independent_max_entry_norm(pairing_delta, q_matrix)
    q_identity_residual = stage1.q_independent_max_entry_norm(pairing_delta, stage1.identity(3))
    intertwining_residual = stage1.q_independent_max_entry_norm(intertwining_delta, q_matrix)

    object_attestations = {
        "V_A_2": _status(
            fixture["V_A_2"]["dimension"] == 3
            and fixture["V_A_2"]["basis"] == ACTIVE_BASIS
            and fixture["V_A_2"]["evidence_class"] == EVIDENCE_CLASS
            and fixture["V_A_2"]["theorem_context_canonical"] is False
        ),
        "Q_A_2": _status(
            _matrix_equal(q_matrix, expected_q)
            and fixture["Q_A_2"]["rank"] == 3
            and fixture["Q_A_2"]["residual_norm_policy"] == "Q_independent_max_entry_norm"
            and q_independent_residual <= stage1.SPEC_TOLERANCE
            and q_independent_residual == q_identity_residual
            and fixture["Q_A_2"]["theorem_context_form_claimed"] is False
        ),
        "E_phi_2": _status(
            fixture["E_phi_2"]["object_type"] == "transport_encoding_map"
            and _matrix_equal(e_matrix, expected_e)
            and fixture["E_phi_2"]["rank"] == 3
            and fixture["E_phi_2"]["nullity"] == 0
            and fixture["E_phi_2"]["determinant_or_condition_number_used"] is False
            and fixture["E_phi_2"]["energy_functional_claimed"] is False
            and intertwining_residual <= stage1.SPEC_TOLERANCE
        ),
        "M_phi_2": _status(
            _matrix_equal(m_phi, expected_diag)
            and fixture["M_phi_2"]["local_model"] == "u^3 = t"
            and fixture["M_phi_2"]["basis"] == SOURCE_BASIS
            and fixture["M_phi_2"]["eigenvalue_source"] == "closed_form_omega_values_not_eigendecomposition"
            and fixture["M_phi_2"]["theorem_context_monodromy_claimed"] is False
        ),
        "M_A_2": _status(
            _matrix_equal(m_a, expected_diag)
            and fixture["M_A_2"]["basis"] == ACTIVE_BASIS
            and fixture["M_A_2"]["theorem_context_gate_action_claimed"] is False
            and fixture["M_A_2"]["gate_minimality_claimed"] is False
            and intertwining_residual <= stage1.SPEC_TOLERANCE
        ),
    }

    protocol_validity = {
        "closed_form_DFT3": _status(stage1.build_receipt()["precision_policy"]["eigendecomposition_used"] is False),
        "Q_independent_residuals": _status(q_independent_residual == q_identity_residual),
        "transport_not_energy_functional": _status(fixture["E_phi_2"]["energy_functional_claimed"] is False),
    }

    pass_count = sum(1 for value in object_attestations.values() if value == "pass")
    all_five = pass_count == REQUIRED_OBJECT_COUNT

    return {
        "object_attestations": object_attestations,
        "protocol_validity": protocol_validity,
        "prediction_outcomes": {"all_five_objects_attested": _status(all_five)},
        "partial_pass_count": pass_count,
        "required_object_count": REQUIRED_OBJECT_COUNT,
        "residuals": {
            "pairing_transport_error": q_independent_residual,
            "pairing_transport_identity_q_error": q_identity_residual,
            "monodromy_compatibility_error": intertwining_residual,
        },
        "stage2_pass": all_five and all(value == "pass" for value in protocol_validity.values()),
    }


def build_receipt(fixture: dict[str, Any] | None = None) -> dict[str, Any]:
    fixture = fixture or base_fixture()
    stage1_receipt = stage1.build_receipt()
    evaluation = evaluate_fixture(fixture)

    core = {
        "fixture": {
            "V_A_2": {**fixture["V_A_2"]},
            "Q_A_2": {**fixture["Q_A_2"], "matrix": stage1.zmatrix(fixture["Q_A_2"]["matrix"])},
            "E_phi_2": {**fixture["E_phi_2"], "matrix": stage1.zmatrix(fixture["E_phi_2"]["matrix"])},
            "M_phi_2": {**fixture["M_phi_2"], "matrix": stage1.zmatrix(fixture["M_phi_2"]["matrix"])},
            "M_A_2": {**fixture["M_A_2"], "matrix": stage1.zmatrix(fixture["M_A_2"]["matrix"])},
        },
        "evaluation": evaluation,
    }

    receipt = {
        "stage": "2",
        "evidence_class": EVIDENCE_CLASS,
        "theorem_context_claimed": False,
        "stage2_pass": evaluation["stage2_pass"],
        "partial_pass_count": evaluation["partial_pass_count"],
        "required_object_count": REQUIRED_OBJECT_COUNT,
        "object_attestations": evaluation["object_attestations"],
        "protocol_validity": evaluation["protocol_validity"],
        "prediction_outcomes": evaluation["prediction_outcomes"],
        "residuals": evaluation["residuals"],
        "fixture": core["fixture"],
        "provenance": {
            "convention_id": stage1.CONVENTION_ID,
            "test_vectors_id": stage1.file_digest("specs/a2-local-cuberoot-test-vectors.md"),
            "stage1_receipt_hash": stage1_receipt["provenance"]["output_hash"],
            "stage2_attestation_hash": canonical_digest(core),
            "implementation_hash": implementation_hash(),
            "generated_by": GENERATED_BY,
            "generated_at": generated_at(),
        },
        "nonclaims": [
            "Stage-2 fixture-only attestation does not establish A2 gate minimality.",
            "Stage-2 fixture-only attestation does not establish theorem-context naturality.",
            "Stage-2 fixture-only attestation does not establish that the local cube-root fixture is canonical.",
            "Stage-2 fixture-only attestation does not extend to A3 or higher A_n.",
            "Stage-2 fixture-only attestation does not complete the C-6' general A_n template.",
            "Stage-2 fixture-only attestation does not promote I-12.",
            "Stage-2 fixture-only attestation does not prove P vs NP or any Clay result.",
        ],
    }
    return receipt


def mutated_receipt(mutation: str) -> dict[str, Any]:
    fixture = deepcopy(base_fixture())
    if mutation == "wrong_dimension":
        fixture["V_A_2"]["dimension"] = 2
    elif mutation == "wrong_pairing":
        fixture["Q_A_2"]["matrix"] = stage1.identity(3)
        fixture["Q_A_2"]["rank"] = stage1.matrix_rank(stage1.identity(3))
    elif mutation == "energy_functional_leak":
        fixture["E_phi_2"]["energy_functional_claimed"] = True
    elif mutation == "wrong_source_monodromy":
        fixture["M_phi_2"]["matrix"] = stage1.identity(3)
    elif mutation == "gate_minimality_claim":
        fixture["M_A_2"]["gate_minimality_claimed"] = True
    else:
        raise ValueError(f"unknown mutation: {mutation}")
    return build_receipt(fixture)


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["stage2_pass"] and receipt["theorem_context_claimed"] is False else 1


if __name__ == "__main__":
    raise SystemExit(main())
