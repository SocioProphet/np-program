# A2 Polarization Compatibility

Status: **theorem-input definition / construction target / not yet proved canonical**.

This note specifies the polarization data assumed by the `A_2` gate-minimality proof note. It is the rank-2 analogue of `docs/research/polarization-compatibility.md`, but it uses the `A_2` / `SU(3)` data: Hermitian form, volume form, and order-3 monodromy.

It does not prove `T_{A_2}`. It defines the admissible data required before an implementation may claim that a singular-germ or Stokes-side construction realizes the hypotheses of `T_{A_2}`.

## 1. Purpose

The `A_2` gate-minimality theorem assumes a three-dimensional active set

```math
V_A \cong \mathbb{C}^3
```

with two transported invariants:

```math
H_A: V_A \times \overline{V_A} \to \mathbb{C}
```

and

```math
\varepsilon_A \in \wedge^3 V_A^*.
```

Here `H_A` is Hermitian and non-degenerate. The form `epsilon_A` is a non-zero antisymmetric trilinear volume form.

The compatibility condition asserts that these are not post-hoc choices. They must be transported from declared source-side data through a ledgered encoding map before the gate action is evaluated.

## 2. Source-side data

An `A_2` polarization claim must declare source-side data:

```text
source_object_id
source_convention_id
source_module M_phi
source_monodromy T_phi
mu3_generator gamma_phi
source_hermitian_form h_phi
source_volume_form omega_phi
source_filtration W_phi
source_basis_id
normalization_id
```

The expected monodromy class is order 3:

```math
\gamma_\phi^3 = 1.
```

Under the committed convention, the nontrivial generator is identified with

```math
\omega = e^{2\pi i/3}.
```

The source-side convention must state whether the provenance is:

1. lattice/root-system convention (`A_2` as the rank-2 root system / `sl_3` label);
2. singularity/Stokes convention (`A_2` as an isolated-singularity or branch-data convention);
3. a declared bridge between the two.

No implementation may silently move between these conventions.

## 3. Encoding data

A compatibility artifact must emit a ledgered encoding map

```math
E_\phi: M_\phi \to V_A.
```

Required properties:

1. `E_phi` is declared before monodromy or gate evaluation.
2. `E_phi` is injective on the bridge-relevant source subspace.
3. `E_phi` maps the declared order-3 source eigenspaces to the declared active eigenspaces.
4. `E_phi` preserves the declared filtration up to an explicit report.
5. `E_phi` carries a content hash or replayable matrix representation.

An unledgered reconstruction of `E_phi` after observing the gate-side result is inadmissible.

## 4. Transported Hermitian form

Let `h_phi` be the source Hermitian form. The transported Hermitian form `H_A` is defined on `im(E_phi)` by

```math
H_A(E_\phi(u), E_\phi(v)) = h_\phi(u,v).
```

If `im(E_phi)` is extended to all of `V_A`, the extension must be declared. Allowed extension classes:

1. direct Hermitian extension with declared orthogonal complement;
2. minimal non-degenerate extension preserving the active filtration;
3. replayable numerical Gram-matrix extension;
4. convention-specific extension declared by a named compatibility document.

Unledgered extension choices are inadmissible.

## 5. Transported volume form

Let `omega_phi` be the source-side alternating trilinear datum or its declared Stokes/lattice analogue. The transported volume form `epsilon_A` must satisfy

```math
\varepsilon_A(E_\phi(u), E_\phi(v), E_\phi(w)) = \omega_\phi(u,v,w)
```

where the right-hand side is defined on the bridge-relevant three-dimensional source datum.

If the source-side datum is not naturally trilinear, the artifact must declare the construction that promotes it to a volume datum. Examples:

1. ordered basis wedge from three monodromy sectors;
2. lattice orientation form;
3. determinant form induced by a declared basis;
4. Stokes-sector cyclic orientation form.

The promotion rule must be hashed or otherwise replayable.

## 6. Gate-side preservation requirement

Let

```math
\rho_A: G \to GL(V_A)
```

be the active-set representation. An `A_2` gate action is polarization-compatible if, for every admissible gate element `g`,

```math
H_A(\rho_A(g)v, \rho_A(g)w) = H_A(v,w)
```

and

```math
\varepsilon_A(\rho_A(g)v, \rho_A(g)w, \rho_A(g)u) = \varepsilon_A(v,w,u).
```

Equivalently, the gate-side image lies in

```math
U(V_A,H_A) \cap SL(V_A,\varepsilon_A) \cong SU(3).
```

## 7. Order-3 monodromy diagram

The order-3 monodromy diagram must commute:

```text
source module --gamma_phi--> source module
      | E_phi                   | E_phi
      v                         v
active module --zeta_A2-----> active module
```

with

```math
\zeta_{A_2} = \omega I_3 \in Z(SU(3)).
```

Hard condition:

```math
E_\phi(\gamma_\phi u) = \zeta_{A_2} E_\phi(u)
```

on the bridge-relevant subspace.

The artifact must report:

```text
mu3_generator_source
mu3_generator_gate
monodromy_matrix_source
monodromy_matrix_gate
monodromy_commutation_error
```

## 8. No-symmetric-bilinear exclusion

The `A_2` theorem requires the active representation to preserve no non-degenerate symmetric bilinear form on `V_A`. This is the condition that excludes real-orthogonal alternatives such as the complexified standard representation of `SO(3)`.

An implementation must therefore report either:

1. a symbolic invariant decomposition proving no trivial summand in `Sym^2(V_A^*)`; or
2. a numerical invariant-search result with a declared tolerance and basis provenance.

Minimum report fields:

```text
symmetric_bilinear_search_method
symmetric_bilinear_candidate_norm
symmetric_bilinear_invariant_norm
symmetric_bilinear_tolerance
symmetric_bilinear_result
```

Pass condition:

```text
symmetric_bilinear_result == none_detected
```

This test does not prove the theorem globally. It only certifies that the chosen implementation did not accidentally instantiate an orthogonal branch.

## 9. Required implementation artifact

Every `A_2` polarization-compatibility run must emit:

```text
source_object_id
source_convention_id
source_basis_id
normalization_id
source_hermitian_gram_matrix
source_volume_tensor
E_phi_matrix
active_basis_id
active_hermitian_gram_matrix
active_volume_tensor
mu3_generator_source
mu3_generator_gate
monodromy_matrix_source
monodromy_matrix_gate
monodromy_commutation_error
hermitian_preservation_error
volume_preservation_error
filtration_preservation_report
symmetric_bilinear_search_method
symmetric_bilinear_invariant_norm
symmetric_bilinear_tolerance
symmetric_bilinear_result
hash_chain
```

## 10. Hard pass conditions

```text
E_phi_matrix declared before monodromy evaluation
monodromy_commutation_error <= tolerance
hermitian_preservation_error <= tolerance
volume_preservation_error <= tolerance
filtration_preservation_report == pass
symmetric_bilinear_result == none_detected
mu3_generator_gate == omega_I3
source_convention_id declared
normalization_id declared
hash_chain complete
```

A failure in any pass condition means the implementation has not realized the hypotheses of `T_{A_2}`. It does not by itself falsify `T_{A_2}`.

## 11. Relation to the A1 document

The `A_1` polarization note uses a symplectic pairing on a two-dimensional lifted branch module. The `A_2` note replaces that with:

```text
Hermitian form + volume form + no symmetric bilinear form
```

This reflects the Frobenius-Schur transition:

```text
A1 / SU(2) defining representation: quaternionic, symplectic
A2 / SU(3) defining representation: complex, no invariant bilinear form
```

## 12. Nonclaims

This note does not claim:

- construction of the source object for every proof-class generating function;
- proof that every `A_2` Stokes datum admits the required `E_phi`;
- proof of `T_{A_2}`;
- proof of the combined `A_1 x A_2` gate;
- proof of the `D_4` or `E_8` lifts;
- equivalence between root-system convention and isolated-singularity convention without a declared bridge.

It is only the compatibility contract for implementations claiming to instantiate the `A_2` theorem's hypotheses.
