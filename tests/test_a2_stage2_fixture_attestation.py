import unittest

from experiments import a2_f5_vacuity_report as f5
from experiments import a2_stage2_fixture_attestation as stage2


class A2Stage2FixtureAttestationTest(unittest.TestCase):
    def test_stage2_receipt_passes_all_five_objects(self):
        receipt = stage2.build_receipt()
        self.assertEqual(receipt["stage"], "2")
        self.assertEqual(receipt["evidence_class"], stage2.EVIDENCE_CLASS)
        self.assertFalse(receipt["theorem_context_claimed"])
        self.assertTrue(receipt["stage2_pass"])
        self.assertEqual(receipt["partial_pass_count"], 5)
        self.assertEqual(receipt["required_object_count"], 5)
        self.assertEqual(set(receipt["object_attestations"].keys()), {"V_A_2", "Q_A_2", "E_phi_2", "M_phi_2", "M_A_2"})
        self.assertTrue(all(status == "pass" for status in receipt["object_attestations"].values()))

    def test_protocol_and_prediction_fields_are_separate(self):
        receipt = stage2.build_receipt()
        self.assertEqual(set(receipt["protocol_validity"].keys()), {
            "closed_form_DFT3",
            "Q_independent_residuals",
            "transport_not_energy_functional",
        })
        self.assertEqual(receipt["prediction_outcomes"], {"all_five_objects_attested": "pass"})
        self.assertTrue(all(status == "pass" for status in receipt["protocol_validity"].values()))

    def test_receipt_provenance_fields(self):
        receipt = stage2.build_receipt()
        provenance = receipt["provenance"]
        self.assertEqual(provenance["convention_id"], "A2-local-cuberoot-normalization-v0")
        self.assertIn("test_vectors_id", provenance)
        self.assertIn("stage1_receipt_hash", provenance)
        self.assertIn("stage2_attestation_hash", provenance)
        self.assertIn("implementation_hash", provenance)
        self.assertEqual(provenance["generated_by"], stage2.GENERATED_BY)
        self.assertIn("generated_at", provenance)

    def test_stage2_is_fixture_only(self):
        receipt = stage2.build_receipt()
        self.assertFalse(receipt["theorem_context_claimed"])
        nonclaims = "\n".join(receipt["nonclaims"])
        self.assertIn("does not establish A2 gate minimality", nonclaims)
        self.assertIn("does not establish theorem-context naturality", nonclaims)
        self.assertIn("does not establish that the local cube-root fixture is canonical", nonclaims)
        self.assertIn("does not extend to A3", nonclaims)
        self.assertIn("does not complete the C-6'", nonclaims)
        self.assertIn("does not promote I-12", nonclaims)
        self.assertIn("does not prove P vs NP", nonclaims)

    def test_wrong_dimension_fails_only_v_object_and_stage2(self):
        receipt = stage2.mutated_receipt("wrong_dimension")
        self.assertFalse(receipt["stage2_pass"])
        self.assertEqual(receipt["partial_pass_count"], 4)
        self.assertEqual(receipt["object_attestations"]["V_A_2"], "fail")
        for key in ["Q_A_2", "E_phi_2", "M_phi_2", "M_A_2"]:
            self.assertEqual(receipt["object_attestations"][key], "pass")

    def test_wrong_pairing_fails_q_object(self):
        receipt = stage2.mutated_receipt("wrong_pairing")
        self.assertFalse(receipt["stage2_pass"])
        self.assertEqual(receipt["object_attestations"]["Q_A_2"], "fail")

    def test_energy_functional_leak_fails_transport_protocol(self):
        receipt = stage2.mutated_receipt("energy_functional_leak")
        self.assertFalse(receipt["stage2_pass"])
        self.assertEqual(receipt["object_attestations"]["E_phi_2"], "fail")
        self.assertEqual(receipt["protocol_validity"]["transport_not_energy_functional"], "fail")

    def test_wrong_source_monodromy_fails_source_and_active_intertwining(self):
        receipt = stage2.mutated_receipt("wrong_source_monodromy")
        self.assertFalse(receipt["stage2_pass"])
        self.assertEqual(receipt["object_attestations"]["M_phi_2"], "fail")
        self.assertEqual(receipt["object_attestations"]["E_phi_2"], "fail")
        self.assertEqual(receipt["object_attestations"]["M_A_2"], "fail")

    def test_gate_minimality_claim_fails_active_object(self):
        receipt = stage2.mutated_receipt("gate_minimality_claim")
        self.assertFalse(receipt["stage2_pass"])
        self.assertEqual(receipt["object_attestations"]["M_A_2"], "fail")

    def test_q_dependent_policy_fails_protocol(self):
        receipt = stage2.mutated_receipt("q_dependent_residual_policy")
        self.assertFalse(receipt["stage2_pass"])
        self.assertEqual(receipt["object_attestations"]["Q_A_2"], "fail")
        self.assertEqual(receipt["protocol_validity"]["Q_independent_residuals"], "fail")

    def test_shape_correct_semantically_wrong_fixture_fails(self):
        receipt = stage2.mutated_receipt("shape_correct_semantically_wrong")
        self.assertFalse(receipt["stage2_pass"])
        self.assertEqual(receipt["object_attestations"]["M_phi_2"], "fail")
        self.assertEqual(receipt["object_attestations"]["E_phi_2"], "fail")
        self.assertEqual(receipt["object_attestations"]["M_A_2"], "fail")

    def test_f5_report_covers_required_vacuity_classes(self):
        report = f5.build_report()
        self.assertEqual(report["classification"], "no_vacuity_detected_within_tested_classes")
        self.assertEqual(set(report["tested_vacuity_classes"]), {
            "V1_trivial_pass",
            "V2_input_independence",
            "V3_type_correct_semantic_vacuity",
        })
        self.assertEqual(report["case_count"], 11)
        self.assertTrue(all(result["failed_for_expected_reason"] for result in report["case_results"]), report)
        self.assertTrue(all(not result["stage2_pass"] for result in report["case_results"]), report)
        self.assertTrue(all(not result["theorem_context_claimed"] for result in report["case_results"]), report)

    def test_forbidden_theorem_phrases_absent(self):
        receipt_text = str(stage2.build_receipt()).lower()
        forbidden = [
            "theorem_context_claimed': true",
            "a2 gate minimality established",
            "theorem-context naturality established",
            "i-12 eligible",
            "clay progress",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, receipt_text)


if __name__ == "__main__":
    unittest.main()
