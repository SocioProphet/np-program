from pathlib import Path
import os
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
PIN = "988307215ad38ccb16514311222184a1b757752b"
REQUIRED_PFK_PATHS = [
    "proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md",
    "proof_fabric_kernel/docs/SchemaCatalog_v1.md",
    "proof_fabric_kernel/docs/anti-seed-pfk.md",
    "proof_fabric_kernel/schemas/claim_ledger_row.schema.json",
    "proof_fabric_kernel/schemas/event_ir.schema.json",
    "proof_fabric_kernel/schemas/proof_artifact.schema.json",
    "proof_fabric_kernel/schemas/calibration_bundle.schema.json",
]
REQUIRED_DEPENDENCY_CITES = [
    "HG-EX-001",
    "HG-MTH-005",
    "PFK-OP-040",
    "PFK-SCHEMA-001",
    "PFK-SCHEMA-002",
    "A-PFK-OP-001",
    "A-PFK-SCHEMA-001",
]


class TestPFKDependency(unittest.TestCase):
    def test_dependencies_pin_is_exact_heller_godel_registry_expansion_commit(self) -> None:
        text = (ROOT / "DEPENDENCIES.md").read_text(encoding="utf-8")
        self.assertIn(PIN, text)
        self.assertNotIn("current `main`", text.lower())
        for citation in REQUIRED_DEPENDENCY_CITES:
            self.assertIn(citation, text)

    def test_readme_declares_canonical_pfk_dependency(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("SocioProphet/Heller-Godel", text)
        self.assertIn(PIN, text)
        self.assertIn("proof_fabric_kernel", text)

    def test_catalan_spec_and_ledger_use_canonical_citations(self) -> None:
        files = [
            ROOT / "specs/catalan-mu2-reference-implementation.md",
            ROOT / "ledgers/catalan_mu2/README.md",
        ]
        for path in files:
            text = path.read_text(encoding="utf-8")
            self.assertIn("HG-EX-001", text)
            self.assertIn("PFK-OP-040", text)
            self.assertIn(PIN, text)

    def test_no_authoritative_local_schemas_directory_present(self) -> None:
        self.assertFalse((ROOT / "schemas").exists(), "local schemas/ must not replace canonical PFK schemas")

    def test_heller_godel_pfk_paths_resolve_when_available(self) -> None:
        hg_root_value = os.environ.get("HELLER_GODEL_ROOT")
        if not hg_root_value:
            self.skipTest("HELLER_GODEL_ROOT not set; dependency-resolution check runs in dedicated workflow")
        hg_root = Path(hg_root_value)
        missing = [path for path in REQUIRED_PFK_PATHS if not (hg_root / path).exists()]
        self.assertFalse(missing, f"Missing canonical Heller-Godel PFK paths: {missing}")

    def test_markdown_citations_use_pinned_commit_shape(self) -> None:
        citation_pattern = re.compile(r"\[[A-Z0-9\-]+ @ [0-9a-f]{40}\]")
        docs = [
            ROOT / "DEPENDENCIES.md",
            ROOT / "specs/catalan-mu2-reference-implementation.md",
            ROOT / "ledgers/catalan_mu2/README.md",
        ]
        self.assertTrue(any(citation_pattern.search(path.read_text(encoding="utf-8")) for path in docs))


if __name__ == "__main__":
    unittest.main()
