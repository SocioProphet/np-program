#!/usr/bin/env python3
"""Validate singularity-scope declaration files.

This validator intentionally uses only the Python standard library. It enforces the
repository's small JSON-schema contract without requiring jsonschema as a runtime
or CI dependency.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = [
    "schema_version",
    "artifact_id",
    "singularity_class",
    "local_coordinate",
    "is_isolated",
    "is_algebraic",
    "has_branching",
    "has_log_terms",
    "has_irregular_terms",
    "monodromy_model",
    "stokes_model",
    "finite_part_model",
    "scope_status",
]

ALLOWED_FIELDS = set(REQUIRED_FIELDS) | {"notes"}

SINGULARITY_CLASSES = {
    "algebraic_isolated_A1",
    "algebraic_isolated_Ak",
    "algebraic_isolated_Dk",
    "algebraic_isolated_Ek",
    "algebraic_logarithmic",
    "d_finite_regular",
    "d_finite_irregular",
    "rational_poles_only",
    "transcendental_essential",
    "natural_boundary",
    "unknown",
}

SCOPE_STATUS = {
    "base_scope",
    "in_scope_with_unipotent_register",
    "boundary_case_by_case",
    "extension_scope",
    "finite_defect_only",
    "out_of_base_scope",
}

STRING_FIELDS = {
    "schema_version",
    "artifact_id",
    "singularity_class",
    "local_coordinate",
    "monodromy_model",
    "stokes_model",
    "finite_part_model",
    "scope_status",
    "notes",
}

BOOLEAN_FIELDS = {
    "is_isolated",
    "is_algebraic",
    "has_branching",
    "has_log_terms",
    "has_irregular_terms",
}


def validate_scope_payload(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    missing = [field for field in REQUIRED_FIELDS if field not in payload]
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")

    extra = sorted(set(payload) - ALLOWED_FIELDS)
    if extra:
        errors.append(f"unexpected fields: {', '.join(extra)}")

    for field in STRING_FIELDS & set(payload):
        if not isinstance(payload[field], str) or not payload[field].strip():
            errors.append(f"{field} must be a nonempty string")

    for field in BOOLEAN_FIELDS & set(payload):
        if not isinstance(payload[field], bool):
            errors.append(f"{field} must be boolean")

    if payload.get("schema_version") != "singularity-scope/v0":
        errors.append("schema_version must equal singularity-scope/v0")

    if payload.get("singularity_class") not in SINGULARITY_CLASSES:
        errors.append(f"unsupported singularity_class: {payload.get('singularity_class')}")

    if payload.get("scope_status") not in SCOPE_STATUS:
        errors.append(f"unsupported scope_status: {payload.get('scope_status')}")

    # Base-scope bridge claims are deliberately narrow.
    if payload.get("scope_status") == "base_scope":
        if not payload.get("is_isolated"):
            errors.append("base_scope requires is_isolated=true")
        if not payload.get("is_algebraic"):
            errors.append("base_scope requires is_algebraic=true")
        if payload.get("has_irregular_terms"):
            errors.append("base_scope requires has_irregular_terms=false")

    return errors


def validate_file(path: Path) -> list[str]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"]

    if not isinstance(payload, dict):
        return ["payload must be a JSON object"]

    return validate_scope_payload(payload)


def iter_targets(paths: list[Path]) -> list[Path]:
    targets: list[Path] = []
    for path in paths:
        if path.is_dir():
            targets.extend(sorted(path.glob("*.scope.json")))
        else:
            targets.append(path)
    return targets


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path("docs/scope/examples")],
        help="Scope declaration files or directories containing *.scope.json files",
    )
    args = parser.parse_args()

    failures = 0
    targets = iter_targets(args.paths)
    if not targets:
        print("ERROR: no scope declaration files found")
        return 1

    for path in targets:
        errors = validate_file(path)
        if errors:
            failures += 1
            for err in errors:
                print(f"ERROR {path}: {err}")
        else:
            print(f"OK {path}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
