from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import validate_singularity_scope as v


def valid_payload():
    return {
        "schema_version": "singularity-scope/v0",
        "artifact_id": "fixture-a1",
        "singularity_class": "algebraic_isolated_A1",
        "local_coordinate": "t = 1 - 4x",
        "is_isolated": True,
        "is_algebraic": True,
        "has_branching": True,
        "has_log_terms": False,
        "has_irregular_terms": False,
        "monodromy_model": "sqrt(t) -> -sqrt(t)",
        "stokes_model": "A1-sauzin-normalization-v0",
        "finite_part_model": "regular analytic part after singular subtraction",
        "scope_status": "base_scope",
    }


def test_catalan_scope_declaration_validates():
    path = ROOT / "docs" / "scope" / "examples" / "catalan-a1.scope.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert v.validate_scope_payload(payload) == []


def test_valid_payload_accepts_base_scope():
    assert v.validate_scope_payload(valid_payload()) == []


def test_missing_required_field_fails():
    payload = valid_payload()
    del payload["artifact_id"]
    errors = v.validate_scope_payload(payload)
    assert any("missing required fields" in err for err in errors)


def test_unknown_singularity_class_fails():
    payload = valid_payload()
    payload["singularity_class"] = "wild_unknown_class"
    errors = v.validate_scope_payload(payload)
    assert any("unsupported singularity_class" in err for err in errors)


def test_base_scope_requires_algebraic_isolated_non_irregular():
    payload = valid_payload()
    payload["is_algebraic"] = False
    payload["is_isolated"] = False
    payload["has_irregular_terms"] = True
    errors = v.validate_scope_payload(payload)
    assert "base_scope requires is_isolated=true" in errors
    assert "base_scope requires is_algebraic=true" in errors
    assert "base_scope requires has_irregular_terms=false" in errors
