"""F5 A2 Stage-2 vacuity execution report.

Executes the adversarial non-examples declared in Issue #31 against the
Stage-2 fixture-only attestation. A clean F5 run is not confirmation of A2
naturality; it only means these adversaries did not expose vacuity.
"""

from __future__ import annotations

import json
from copy import deepcopy
from typing import Any, Callable

from experiments import a2_stage2_fixture_attestation as stage2

F5_ISSUE = "#31"
F5_SPEC = "docs/falsification/five-layer-falsification-spec.md"
ARTIFACT_UNDER_TEST = "experiments/a2_stage2_fixture_attestation.py"


def _empty_fixture() -> dict[str, Any]:
    return {}


def _null_fixture() -> dict[str, Any]:
    return {
        "V_A_2": None,
        "Q_A_2": None,
        "E_phi_2": None,
        "M_phi_2": None,
        "M_A_2": None,
    }


def _identity_only_fixture() -> dict[str, Any]:
    fixture = deepcopy(stage2.base_fixture())
    fixture["Q_A_2"]["matrix"] = stage2.stage1.identity(3)
    fixture["Q_A_2"]["rank"] = stage2.stage1.matrix_rank(stage2.stage1.identity(3))
    fixture["M_phi_2"]["matrix"] = stage2.stage1.identity(3)
    fixture["M_A_2"]["matrix"] = stage2.stage1.identity(3)
    return fixture


def _partial_pass_fixture() -> dict[str, Any]:
    fixture = deepcopy(stage2.base_fixture())
    fixture["V_A_2"]["dimension"] = 2
    return fixture


CASES: dict[str, dict[str, Any]] = {
    "wrong_active_space_dimension": {
        "vacuity_class": "V2_input_independence",
        "expected_failed_fields": ["object_attestations.V_A_2"],
        "runner": lambda: stage2.mutated_receipt("wrong_dimension"),
    },
    "wrong_pairing_matrix": {
        "vacuity_class": "V2_input_independence",
        "expected_failed_fields": ["object_attestations.Q_A_2"],
        "runner": lambda: stage2.mutated_receipt("wrong_pairing"),
    },
    "energy_functional_leakage": {
        "vacuity_class": "V2_input_independence",
        "expected_failed_fields": ["object_attestations.E_phi_2", "protocol_validity.transport_not_energy_functional"],
        "runner": lambda: stage2.mutated_receipt("energy_functional_leak"),
    },
    "wrong_source_monodromy": {
        "vacuity_class": "V2_input_independence",
        "expected_failed_fields": ["object_attestations.M_phi_2", "object_attestations.E_phi_2", "object_attestations.M_A_2"],
        "runner": lambda: stage2.mutated_receipt("wrong_source_monodromy"),
    },
    "gate_minimality_claim_leakage": {
        "vacuity_class": "V2_input_independence",
        "expected_failed_fields": ["object_attestations.M_A_2"],
        "runner": lambda: stage2.mutated_receipt("gate_minimality_claim"),
    },
    "q_dependent_residual_policy": {
        "vacuity_class": "V2_input_independence",
        "expected_failed_fields": ["object_attestations.Q_A_2", "protocol_validity.Q_independent_residuals"],
        "runner": lambda: stage2.mutated_receipt("q_dependent_residual_policy"),
    },
    "partial_pass_promotion": {
        "vacuity_class": "V2_input_independence",
        "expected_failed_fields": ["object_attestations.V_A_2", "prediction_outcomes.all_five_objects_attested"],
        "runner": lambda: stage2.build_receipt(_partial_pass_fixture()),
    },
    "empty_fixture": {
        "vacuity_class": "V1_trivial_pass",
        "expected_failed_fields": ["exception"],
        "runner": lambda: stage2.build_receipt(_empty_fixture()),
    },
    "null_fixture": {
        "vacuity_class": "V1_trivial_pass",
        "expected_failed_fields": ["exception"],
        "runner": lambda: stage2.build_receipt(_null_fixture()),
    },
    "identity_only_fixture": {
        "vacuity_class": "V1_trivial_pass",
        "expected_failed_fields": ["object_attestations.Q_A_2", "object_attestations.M_phi_2"],
        "runner": lambda: stage2.build_receipt(_identity_only_fixture()),
    },
    "shape_correct_semantically_wrong": {
        "vacuity_class": "V3_type_correct_semantic_vacuity",
        "expected_failed_fields": ["object_attestations.M_phi_2", "object_attestations.E_phi_2", "object_attestations.M_A_2"],
        "runner": lambda: stage2.mutated_receipt("shape_correct_semantically_wrong"),
    },
}


def _read_path(receipt: dict[str, Any], dotted_path: str) -> Any:
    value: Any = receipt
    for part in dotted_path.split("."):
        value = value[part]
    return value


def _field_failed(receipt: dict[str, Any], dotted_path: str) -> bool:
    return _read_path(receipt, dotted_path) == "fail"


def execute_case(name: str, runner: Callable[[], dict[str, Any]], expected_failed_fields: list[str]) -> dict[str, Any]:
    try:
        receipt = runner()
    except Exception as exc:  # noqa: BLE001 - report classification intentionally captures hard failures.
        expected_exception = "exception" in expected_failed_fields
        return {
            "case": name,
            "outcome": "expected_exception" if expected_exception else "unexpected_exception",
            "stage2_pass": False,
            "theorem_context_claimed": False,
            "expected_failed_fields": expected_failed_fields,
            "observed_failed_fields": ["exception"],
            "failed_for_expected_reason": expected_exception,
            "vacuity_detected": not expected_exception,
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
        }

    observed_failed_fields = [field for field in expected_failed_fields if field != "exception" and _field_failed(receipt, field)]
    stage2_pass = bool(receipt.get("stage2_pass"))
    theorem_context_claimed = bool(receipt.get("theorem_context_claimed"))
    expected_fields_satisfied = len(observed_failed_fields) == len([field for field in expected_failed_fields if field != "exception"])
    failed_for_expected_reason = expected_fields_satisfied and not stage2_pass and not theorem_context_claimed

    return {
        "case": name,
        "outcome": "expected_failure" if failed_for_expected_reason else "vacuity_detected",
        "stage2_pass": stage2_pass,
        "theorem_context_claimed": theorem_context_claimed,
        "expected_failed_fields": expected_failed_fields,
        "observed_failed_fields": observed_failed_fields,
        "failed_for_expected_reason": failed_for_expected_reason,
        "vacuity_detected": not failed_for_expected_reason,
        "partial_pass_count": receipt.get("partial_pass_count"),
        "required_object_count": receipt.get("required_object_count"),
    }


def build_report() -> dict[str, Any]:
    case_results = []
    for name, spec in CASES.items():
        result = execute_case(name, spec["runner"], spec["expected_failed_fields"])
        result["vacuity_class"] = spec["vacuity_class"]
        case_results.append(result)

    vacuity_detected = any(result["vacuity_detected"] for result in case_results)
    tested_classes = sorted({spec["vacuity_class"] for spec in CASES.values()})

    return {
        "issue": F5_ISSUE,
        "layer": 5,
        "claim_id": "A2-STAGE2-FIXTURE-ATTESTATION-F5",
        "attempt_type": "vacuity",
        "artifact_under_test": ARTIFACT_UNDER_TEST,
        "spec_under_test": F5_SPEC,
        "tested_vacuity_classes": tested_classes,
        "case_count": len(case_results),
        "case_results": case_results,
        "classification": "vacuity_detected" if vacuity_detected else "no_vacuity_detected_within_tested_classes",
        "non_confirmation_boundary": "A clean F5 run is not confirmation of A2 theorem-context naturality, A2 gate minimality, I-12 promotion, P vs NP, or any Clay result.",
        "next_action_if_vacuity_detected": "Open Stage-2 hardening issue, mark Stage-2 evidence under-review, and rerun F5 after hardening.",
    }


def main() -> int:
    report = build_report()
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["classification"] == "vacuity_detected" else 0


if __name__ == "__main__":
    raise SystemExit(main())
