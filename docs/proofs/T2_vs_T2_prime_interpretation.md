# T2 vs T2' Interpretation Table

Status: **reference note / harness interpretation / not a new theorem**.  
Depends on: `docs/proofs/a1-gate-minimality-faithful.md`.  
Purpose: preserve the Catalan A1 harness numerical predicates while making their theorem-version interpretation explicit.

## 0. Why this note exists

The Catalan A1 harness can remain numerically version-agnostic. The same five predicate values are meaningful under both the non-faithful theorem `T2` and the faithful theorem `T2'`:

```text
Stokes = -1
Catalan jump = -4
pairing preserved
commutator = 2 sqrt(2)
zeta = -I
```

What changes is not the arithmetic. What changes is where the structure lives.

Under `T2`, the sign data is internal to `G = SU(2)`. Under `T2'`, the spatial group is `G = SO(3)` and the sign data lives in the auxiliary `Spin(3)`-structure on `V_A`.

## 1. Branch summary

| Aspect | Non-faithful `T2` | Faithful `T2'` |
|---|---|---|
| Triad action | nontrivial, not faithful | faithful into `SO(3)` |
| Minimal `G` | `SU(2)` | `SO(3)` |
| Location of `-I` | central element of `G` | auxiliary `Spin(3)`, not `G` |
| Loop class | path class in `G` | `gamma in pi_1(SO(3)) = Z/2` |
| `V_A` data | `G` representation | auxiliary `Spin(3)` representation |
| Polarization | internal to `G` | compatibility between `G` and auxiliary spin |
| Ontology | `G` carries the sign | `G` acts through spin data carrying the sign |

## 2. Predicate interpretation table

| Predicate | `T2` interpretation | `T2'` interpretation |
|---|---|---|
| `stokes_multiplier_observed == -1` | Witnesses central `-I in G = SU(2)` via monodromy. | Witnesses the A1 `Z/2` monodromy whose lifted endpoint is read through the auxiliary spin structure. |
| `catalan_jump_coefficient ~= -4` | Quantitative witness for the central `-I` via the Catalan branch jump. | Same numerical content; interpreted as a quantitative witness for the auxiliary spin structure, not for `G` itself. |
| `pairing_preservation` | `G` preserves `Q_A` on `V_A`. | Auxiliary `sigma` takes values in `SL(V_A) = Sp(V_A, Q_A)`; `G` acts on `V_A` only projectively through `sigma`. |
| `commutator_norm == 2 sqrt(2)` | Pauli matrices are in the Lie algebra of `G = SU(2)`. | Pauli matrices are in the Lie algebra of `Spin(3)`; the auxiliary structure carries the nonabelian spinor action. The Lie algebras `so(3)` and `spin(3)` are isomorphic, so the value is invariant. |
| `zeta == -I` | `zeta = -I in G`. | `zeta = sigma(gamma_tilde(1)) = -I` in the auxiliary `Spin(3)`-structure; it is not an element of `G = SO(3)`. |

## 3. Recommended harness metadata

The harness should remain version-agnostic unless it is explicitly testing theorem-version semantics. Its metadata should point to both theorem references and this interpretation table:

```json
{
  "proof_reference_T2": "docs/proofs/a1-gate-minimality.md",
  "proof_reference_T2_prime": "docs/proofs/a1-gate-minimality-faithful.md",
  "predicate_interpretation_table": "docs/proofs/T2_vs_T2_prime_interpretation.md",
  "central_element_location_T2": "G = SU(2)",
  "central_element_location_T2_prime": "auxiliary_spin_structure_on_V_A"
}
```

If the harness report includes a single theorem version, then for the faithful branch it should use:

```json
{
  "proof_reference": "docs/proofs/a1-gate-minimality-faithful.md",
  "theorem_version": "T2_prime",
  "central_element_location": "auxiliary_spin_structure_on_V_A"
}
```

## 4. Hash-chain note

Changing only the documentation-level proof references or predicate interpretation table changes the report metadata and therefore may change the hash-chain head. The numerical regression target is unchanged.

A valid rerun should show:

```text
same numerical predicates
new metadata hash if proof_reference fields changed
```

## 5. Nonclaims

This note does not decide between `T2` and `T2'` as a matter of pure mathematics. They answer different structural questions.

It does not add a new harness predicate, does not change the Catalan jump calculation, and does not claim complexity-theoretic progress.

Its role is narrower: prevent consumers from reading the faithful-branch `zeta = -I` as an element of `G = SO(3)`. Under `T2'`, it is a statement about the auxiliary spin frame.