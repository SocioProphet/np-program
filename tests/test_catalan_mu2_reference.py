import unittest

from experiments.catalan_mu2_reference import build_ledger, catalan_coefficients, catalan_number


class CatalanMu2ReferenceTest(unittest.TestCase):
    def test_catalan_numbers(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)
        self.assertEqual(catalan_coefficients(5), [1, 1, 2, 5, 14, 42])

    def test_reference_ledger_checks_pass(self):
        ledger = build_ledger(N=12)
        self.assertEqual(ledger["execution_status"], "synthetic_fixture")
        self.assertEqual(ledger["claim_id"], "A1-POLARIZATION-001")
        self.assertTrue(all(ledger["checks"].values()))

    def test_reference_ledger_is_deterministic(self):
        first = build_ledger(N=8)
        second = build_ledger(N=8)
        self.assertEqual(first["output_digest"], second["output_digest"])
        self.assertEqual(first["run_id"], second["run_id"])

    def test_polarization_fields_are_present(self):
        ledger = build_ledger(N=4)
        self.assertEqual(ledger["source_pairing_gram_matrix"], [[1.0]])
        self.assertEqual(ledger["active_constraint_pairing_gram_matrix"], [[1.0]])
        self.assertEqual(ledger["E_phi_matrix"], [[1.0]])
        self.assertEqual(ledger["monodromy_matrix_source"], [[-1.0]])
        self.assertEqual(ledger["monodromy_matrix_gate"], [[-1.0]])


if __name__ == "__main__":
    unittest.main()
