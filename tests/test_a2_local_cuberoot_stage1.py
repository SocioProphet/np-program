import unittest

from experiments.a2_local_cuberoot_stage1 import (
    CONVENTION_ID,
    FIXTURE_ID,
    REFERENCE_NO_MIXING_TOLERANCE,
    SPEC_TOLERANCE,
    SAMPLE_RADII,
    build_receipt,
    identity,
    q_independent_max_entry_norm,
)


class A2LocalCuberootStage1Test(unittest.TestCase):
    def test_receipt_passes(self):
        receipt = build_receipt()
        self.assertTrue(receipt["pass"])
        self.assertTrue(receipt["stage1_pass"])
        self.assertFalse(receipt["stage2_claimed"])
        self.assertTrue(all(receipt["checks"].values()))

    def test_required_provenance_fields_are_present(self):
        receipt = build_receipt()
        self.assertEqual(receipt["source"], "A2-local-cuberoot-normalization-v0 / A2-LOCAL-CUBEROOT-TV-001")
        self.assertEqual(receipt["version"], "a2-local-cuberoot-stage1-v0")
        self.assertEqual(receipt["generated_by"], "experiments.a2_local_cuberoot_stage1.build_receipt")
        self.assertIn("date", receipt)
        self.assertIn("checksum", receipt)
        self.assertTrue(receipt["stage1_pass"])
        self.assertFalse(receipt["stage2_claimed"])
        self.assertEqual(receipt["convention_id"], CONVENTION_ID)
        self.assertEqual(receipt["fixture_id"], FIXTURE_ID)
        self.assertIn("test_vectors_id", receipt)
        self.assertIn("harness_implementation_hash", receipt)
        self.assertEqual(receipt["provenance"]["convention_id"], CONVENTION_ID)
        self.assertIn("test_vectors_id", receipt["provenance"])
        self.assertIn("harness_implementation_hash", receipt["provenance"])
        self.assertIn("output_hash", receipt["provenance"])

    def test_checksum_covers_core_numerical_values(self):
        first = build_receipt()
        second = build_receipt()
        self.assertEqual(first["checksum"], second["checksum"])
        self.assertEqual(first["checksum"], first["provenance"]["checksum"])
        self.assertIn("residuals", first)
        self.assertIn("transport_encoding", first)
        self.assertIn("lateral_values_plus", first)
        self.assertIn("additive_jump_coefficients", first)

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

        residual_matrix = [[1 + 2j, -3 + 0j], [0.25j, 4 - 1j]]
        q_fixture = [[1 + 0j, 0 + 0j], [0 + 0j, -1 + 0j]]
        q_identity = identity(2)
        self.assertEqual(
            q_independent_max_entry_norm(residual_matrix, q_fixture),
            q_independent_max_entry_norm(residual_matrix, q_identity),
        )

    def test_transport_encoding_not_energy_functional(self):
        receipt = build_receipt()
        transport = receipt["transport_encoding"]
        self.assertEqual(transport["interpretation"], "transport_encoding_map_not_energy_functional")
        self.assertEqual(transport["expected_rank"], 3)
        self.assertEqual(transport["rank"], 3)
        self.assertEqual(transport["nullity"], 0)
        self.assertEqual(transport["kernel_condition"], "trivial_kernel")
        self.assertFalse(transport["determinant_or_condition_number_used"])
        self.assertTrue(receipt["checks"]["transport_encoding_full_rank"])
        self.assertTrue(receipt["checks"]["transport_encoding_trivial_kernel"])
        self.assertTrue(receipt["checks"]["transport_encoding_not_energy_functional"])

    def test_nonclaim_boundary_is_mechanical(self):
        receipt = build_receipt()
        nonclaims = "\n".join(receipt["nonclaims"])
        self.assertIn("bare local cube-root model", nonclaims)
        self.assertIn("Canonicity and unique naturality", nonclaims)
        self.assertIn("out of scope", nonclaims)
        self.assertIn("larger A2 algebraic-geometry contexts", nonclaims)
        self.assertIn("higher An", nonclaims)
        self.assertIn("I-12", nonclaims)
        self.assertIn("P vs NP", nonclaims)

    def test_forbidden_stage2_phrases_absent_from_receipt(self):
        receipt_text = str(build_receipt()).lower()
        forbidden = [
            "confirms theorem-context",
            "establishes naturality",
            "i-12 eligible",
            "promotion-ready",
            "proves a2",
            "validates a2",
            "fixture is canonical",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, receipt_text)

    def test_receipt_is_deterministic_under_fixed_inputs(self):
        first = build_receipt()
        second = build_receipt()
        self.assertEqual(first["provenance"]["output_hash"], second["provenance"]["output_hash"])


if __name__ == "__main__":
    unittest.main()
