import unittest

from experiments.a2_local_cuberoot_stage1 import (
    CONVENTION_ID,
    FIXTURE_ID,
    REFERENCE_NO_MIXING_TOLERANCE,
    SPEC_TOLERANCE,
    SAMPLE_RADII,
    build_receipt,
)


class A2LocalCuberootStage1Test(unittest.TestCase):
    def test_receipt_passes(self):
        receipt = build_receipt()
        self.assertTrue(receipt["pass"])
        self.assertTrue(all(receipt["checks"].values()))

    def test_required_provenance_fields_are_present(self):
        receipt = build_receipt()
        self.assertEqual(receipt["convention_id"], CONVENTION_ID)
        self.assertEqual(receipt["fixture_id"], FIXTURE_ID)
        self.assertIn("test_vectors_id", receipt)
        self.assertIn("harness_implementation_hash", receipt)
        self.assertEqual(receipt["provenance"]["convention_id"], CONVENTION_ID)
        self.assertIn("test_vectors_id", receipt["provenance"])
        self.assertIn("harness_implementation_hash", receipt["provenance"])
        self.assertIn("output_hash", receipt["provenance"])

    def test_precision_policy_uses_closed_form_dft3(self):
        receipt = build_receipt()
        policy = receipt["precision_policy"]
        self.assertFalse(policy["eigendecomposition_used"])
        self.assertTrue(policy["no_mixing_residual_epsilon_independent"])
        self.assertTrue(policy["no_mixing_tolerance_is_not_inherited_from_lateral_values"])
        self.assertEqual(receipt["tolerances"]["character_basis_offdiag_tolerance"], REFERENCE_NO_MIXING_TOLERANCE)
        self.assertLessEqual(receipt["residuals"]["character_basis_offdiag_ratio"], REFERENCE_NO_MIXING_TOLERANCE)

    def test_lateral_values_cover_required_radii(self):
        receipt = build_receipt()
        self.assertEqual(receipt["sample_radii"], SAMPLE_RADII)
        for radius in SAMPLE_RADII:
            key = f"{radius:.1e}"
            self.assertIn(key, receipt["lateral_values_plus"])
            self.assertIn(key, receipt["lateral_values_minus"])
            self.assertIn(key, receipt["additive_jump_coefficients"])
        self.assertLessEqual(receipt["residuals"]["lateral_value_max_error"], SPEC_TOLERANCE)
        self.assertLessEqual(receipt["residuals"]["additive_jump_max_error"], SPEC_TOLERANCE)

    def test_q_independent_norm_policy(self):
        receipt = build_receipt()
        self.assertEqual(receipt["norm_policy"], "Q_independent_max_entry_norm")
        self.assertTrue(receipt["checks"]["norm_policy_q_independent"])
        self.assertLessEqual(receipt["residuals"]["pairing_transport_error"], SPEC_TOLERANCE)
        self.assertLessEqual(receipt["residuals"]["monodromy_compatibility_error"], SPEC_TOLERANCE)

    def test_nonclaim_boundary_is_mechanical(self):
        receipt = build_receipt()
        nonclaims = "\n".join(receipt["nonclaims"])
        self.assertIn("bare local cube-root model", nonclaims)
        self.assertIn("not establish that the fixture is canonical", nonclaims)
        self.assertIn("larger A2 algebraic-geometry contexts", nonclaims)
        self.assertIn("higher An", nonclaims)
        self.assertIn("I-12", nonclaims)
        self.assertIn("P vs NP", nonclaims)

    def test_receipt_is_deterministic_under_fixed_inputs(self):
        first = build_receipt()
        second = build_receipt()
        self.assertEqual(first["provenance"]["output_hash"], second["provenance"]["output_hash"])


if __name__ == "__main__":
    unittest.main()
