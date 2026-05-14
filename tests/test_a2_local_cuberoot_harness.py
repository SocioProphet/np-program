"""Tests for the Stage-1 A2 local cube-root harness."""

from __future__ import annotations

import inspect
import unittest

from experiments import a2_local_cuberoot_harness as h


class A2LocalCubeRootHarnessTests(unittest.TestCase):
    def test_stage1_receipt_passes_and_does_not_claim_stage2(self) -> None:
        receipt = h.compute_receipt(implementation_hash="test-hash", generated_at="2026-05-14T00:00:00+00:00")

        self.assertTrue(receipt["stage1_pass"])
        self.assertFalse(receipt["stage2_claimed"])
        self.assertEqual(receipt["convention_id"], h.CONVENTION_ID)
        self.assertEqual(receipt["target"], "A2_local_cuberoot")

        for key in [
            "source",
            "version",
            "generated_by",
            "date",
            "checksum",
            "stage1_pass",
            "stage2_claimed",
            "convention_id",
            "test_vectors_id",
            "harness_implementation_hash",
        ]:
            self.assertIn(key, receipt)

        self.assertIsInstance(receipt["checksum"], str)
        self.assertGreater(len(receipt["checksum"]), 32)

    def test_residuals_within_tolerance(self) -> None:
        receipt = h.compute_receipt(implementation_hash="test-hash", generated_at="2026-05-14T00:00:00+00:00")

        for name, value in receipt["residuals"].items():
            self.assertLessEqual(value, h.TOLERANCE, name)

    def test_closed_form_character_matrix_no_eigendecomposition(self) -> None:
        source = inspect.getsource(h)

        forbidden = [
            "numpy.linalg.eig",
            "scipy.linalg.eig",
            "numpy.linalg.eigh",
            "torch.linalg.eig",
            ".eig(",
            ".eigh(",
        ]
        for token in forbidden:
            self.assertNotIn(token, source)

        f = h.character_matrix_f()
        w = h.omega()
        w2 = h.omega2()
        self.assertEqual(f[0], [1.0 + 0.0j, 1.0 + 0.0j, 1.0 + 0.0j])
        self.assertEqual(f[1], [1.0 + 0.0j, w2, w])
        self.assertEqual(f[2], [1.0 + 0.0j, w, w2])

    def test_non_pairing_residuals_are_q_independent(self) -> None:
        default = h.compute_matrices()["residuals"]
        identity_q = h.compute_matrices(pairing_q=h.identity(3))["residuals"]

        non_pairing_keys = [
            "sheet_basis_cubic_error",
            "eigenvalue_max_error",
            "character_basis_offdiag_ratio",
            "character_basis_diag_max_error",
            "monodromy_compatibility_error",
        ]

        for key in non_pairing_keys:
            self.assertEqual(default[key], identity_q[key], key)

    def test_transport_map_rank_nullity_and_intertwining(self) -> None:
        receipt = h.compute_receipt(implementation_hash="test-hash", generated_at="2026-05-14T00:00:00+00:00")

        self.assertEqual(receipt["transport_checks"]["E_phi_rank"], 3)
        self.assertEqual(receipt["transport_checks"]["E_phi_nullity"], 0)
        self.assertLessEqual(receipt["residuals"]["monodromy_compatibility_error"], h.TOLERANCE)

    def test_pairing_matrix_is_not_identity_norm_proxy(self) -> None:
        q = h.pairing_matrix_q()

        self.assertEqual(q[0][0], 1.0 + 0.0j)
        self.assertEqual(q[1][2], 1.0 + 0.0j)
        self.assertEqual(q[2][1], 1.0 + 0.0j)
        self.assertEqual(q[1][1], 0.0 + 0.0j)
        self.assertEqual(q[2][2], 0.0 + 0.0j)

        receipt = h.compute_receipt(implementation_hash="test-hash", generated_at="2026-05-14T00:00:00+00:00")
        self.assertEqual(receipt["norm_policy"], "Q_independent")


if __name__ == "__main__":
    unittest.main()
