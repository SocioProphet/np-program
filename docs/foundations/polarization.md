# Polarization Foundation for the A1 / mu2 Bridge

Status: **theorem-input foundation / Track A1 / not a Clay claim**.  
Date: 2026-05-12.  
Depends on: `docs/research/polarization-compatibility.md`, `docs/research/gate-minimality-theorem-target.md`, `docs/proofs/a1-gate-minimality-faithful.md`, `docs/proofs/T2_vs_T2_prime_interpretation.md`, `specs/catalan-mu2-reference-implementation.md`, `docs/barriers/README.md`.

## 0. Purpose

This note supplies the formal foundation that the gate-minimality theorem needs. It upgrades polarization compatibility from a roadmap condition into a citeable definition package for the `A1` / Catalan / `mu2` bridge.

It does not prove P vs NP, does not assert a Boolean lower bound, and does not claim that singular-germ invariants transfer to proof complexity. It only defines the source pairing, active-constraint pairing, encoding map, and preservation checks required before the `SO(3)` / `Spin(3)` gate-minimality target can be treated as mathematical rather than decorative.

### 0.1 T2' design commitment

This foundation now commits to the faithful-triad branch `T2'` as the default Track A1 interpretation.

Under `T2'`:

```text
G = SO(3)
rho_spatial: G -> SO(3) is faithful
the -I lives in the auxiliary Spin(3)-structure on V_A, not in G
```

The central sign tested by the Catalan harness is therefore interpreted as:

```text
zeta = sigma(gamma_tilde(1)) = -I
```

where `gamma_tilde` is the lift of the distinguished generator of `pi_1(SO(3)) = Z/2` to the auxiliary `Spin(3)` frame and `sigma: Spin(3) -> SL(V_A)` is the spinor representation preserving `Q_A`.

This does not invalidate the non-faithful `T2` branch. It fixes the default semantics for this foundation: spatial symmetry and auxiliary spin data are distinct structures. The non-faithful branch remains available only when a document explicitly declares that its minimal group is `G = SU(2)` and that the central `-I` is internal to `G`.

### 0.2 Higher-Ak barrier

The `A1` fact that `Spin(3)` is isomorphic to the universal cover of `SO(3)` is incidental. Under the faithful branch, the auxiliary group is data on `V_A`, not simply the universal cover of the spatial group. For `A_k` with `k > 1`, the auxiliary group must be re-derived from the relevant polarization space, pairing, and central monodromy structure.

Any `A2` or higher extension that obtains its auxiliary group by mechanically taking a universal cover of the spatial symmetry group is out of scope until a separate theorem supplies the missing categorical setup.

## 1. Objects

### 1.1 Source singular-germ data

Let `phi` be a declared algebraic isolated singular germ in the active scope of the repository. For the first bridge instance, `phi` is the `A1` square-root / two-sheeted branch germ.

The source package is:

```text
S_phi = (
  F_phi,
  H_phi,
  T_phi,
  W_phi,
  Filt_phi,
  Q_phi,
  conventions_phi,
  provenance_phi
)
```

where:

- `F_phi` is the Milnor fiber or declared equivalent branch fiber;
- `H_phi` is the bridge-relevant cohomology or reduced cohomology subspace;
- `T_phi` is the monodromy action on `H_phi`;
- `W_phi` is the relevant weight or monodromy filtration;
- `Filt_phi` records any additional filtration used by the bridge;
- `Q_phi` is the source pairing, normalized under the committed convention;
- `conventions_phi` records branch, sign, Stokes, and normalization choices;
- `provenance_phi` records source text, code, commit, and hash data.

For `A1`, the bridge-relevant source subspace is the sign line:

```text
L_phi subset H_phi
rank(L_phi) = 1
T_phi|L_phi = -1
Q_phi(e,e) != 0 for any nonzero basis vector e of L_phi
```

The normalization of `Q_phi` may be `+1`, `-1`, or another declared nonzero scalar, but it must be fixed before evaluation.

### 1.2 Active constraint data

The gate-side package is:

```text
A = (
  K_A,
  V_A,
  W_A,
  Filt_A,
  G_A,
  rho_A,
  gamma_A,
  Q_A,
  provenance_A
)
```

where:

- `K_A` is the active constraint complex;
- `V_A` is the finite-dimensional active constraint vector space;
- `W_A` is the codimension / activity filtration;
- `Filt_A` records any additional operational filtration;
- `G_A` is the declared compact connected Lie gate factor;
- `rho_A` records the declared gate-side action; under `T2'`, its spatial component is faithful into `SO(3)` while the `V_A` action is mediated by the auxiliary `Spin(3)` structure;
- `gamma_A` is the ledgered gate loop or path;
- `Q_A` is the active-side pairing;
- `provenance_A` records code, matrix, convention, and hash data.

For the gate-minimality theorem target under `T2'`, the spatial-triad component must be a faithful orthogonal real 3-dimensional representation of `SO(3)`, and the active-set action must be non-abelian through the auxiliary spin structure.

## 2. Encoding map

A polarization-ready bridge includes a linear map:

```text
E_phi: H_phi_bridge -> V_A
```

where `H_phi_bridge` is the declared bridge-relevant subspace of `H_phi`.

Admissibility requires:

1. `E_phi` is declared before monodromy or gate evaluation.
2. `E_phi` is injective on `H_phi_bridge`.
3. `E_phi` maps monodromy eigenspaces into the corresponding gate eigenspaces.
4. `E_phi` respects declared filtrations.
5. `E_phi` is ledgered as an input artifact with hash and convention data.

For the `A1` bridge:

```text
E_phi: L_phi -> V_A
E_phi(e) = v_minus
sigma(gamma_tilde(1)) E_phi(e) = -E_phi(e)
Q_A(v_minus, v_minus) = Q_phi(e,e)
```

The eigendirection `v_minus` must be selected before execution. Selecting the eigendirection after observing the `-1` eigenvalue is inadmissible.

## 3. Transported pairing

On the image of `E_phi`, define:

```text
Q_A(E_phi(u), E_phi(v)) := Q_phi(u,v)
```

This defines `Q_A` on `im(E_phi)`. If the active vector space contains additional directions, the extension of `Q_A` must be one of:

1. orthogonal direct-sum extension;
2. minimal nondegenerate extension preserving `W_A`;
3. explicitly ledgered Gram-matrix extension.

The extension rule is part of the artifact. An unledgered extension is not admissible.

In matrix form, if `G_phi` is the Gram matrix of `Q_phi`, `G_active` is the Gram matrix of `Q_A`, and `E` is the matrix of `E_phi`, then polarization transport requires:

```text
E^T G_active E = G_phi
```

or the Hermitian variant:

```text
E^* G_active E = G_phi
```

when the chosen vector spaces are complex.

## 4. Monodromy and gate compatibility

Let `M_phi` be the matrix of source monodromy on `H_phi_bridge`. Let `M_A` be the matrix induced on `V_A` by the auxiliary spin evaluation under the declared gate loop.

Under `T2'`, the spatial group is `G = SO(3)`, but the concrete sign action on `V_A` is:

```text
M_A = sigma(gamma_tilde(1)).
```

The bridge is monodromy-compatible when:

```text
M_A E = E M_phi
```

Equivalently:

```text
commutator_error := ||M_A E - E M_phi|| <= tolerance
```

For the `A1` sign line, this reduces to:

```text
M_phi = [-1]
sigma(gamma_tilde(1)) E(e) = -E(e)
```

This is necessary but not sufficient. Sign compatibility alone does not force the faithful `SO(3)` / auxiliary `Spin(3)` structure because abelian or stray-sign targets can also display a sign. The gate-minimality theorem additionally uses spatial-triad faithfulness, non-abelian active-set action, compact-connected Lie regularity, coherent loop class, and the polarization condition above.

## 5. Pairing preservation

Under `T2'`, pairing preservation is a property of the auxiliary spin representation:

```text
sigma(g)^T G_active sigma(g) = G_active
```

for every admissible `g in Spin(3)` used by the bridge, or the Hermitian variant:

```text
sigma(g)^* G_active sigma(g) = G_active
```

For a ledgered loop `gamma_A`, the minimum replay condition is:

```text
pairing_preservation_error := ||M_A^T G_active M_A - G_active|| <= tolerance
```

or, in Hermitian form:

```text
pairing_preservation_error := ||M_A^* G_active M_A - G_active|| <= tolerance
```

## 6. Filtration preservation

The bridge must preserve the declared filtration structure.

Let:

```text
W_phi^i H_phi_bridge
W_A^i V_A
```

be the source and active filtrations. Filtration compatibility requires:

```text
E_phi(W_phi^i H_phi_bridge) subset W_A^i V_A
```

for every declared level `i`, and:

```text
M_A(W_A^i) subset W_A^i
```

for the auxiliary spin action used in the replay.

The implementation report must make this machine-checkable by emitting basis indices or projection matrices for each filtration level.

## 7. Complexity-theoretic interpretation of `E_phi`

The role of `E_phi` is not to prove a lower bound. Its role is to prevent a singular-germ invariant from becoming detached from the declared computational basis.

The intended complexity-theoretic interpretation is:

```text
source side:      algebraic / singular-germ invariant
active side:      declared proof, formula, circuit, or constraint morphology basis
E_phi:            typed transport map from source invariant into active morphology coordinates
Q preservation:   no loss or post-hoc rotation of the invariant under the transport
filtration:       declared hierarchy of cost, depth, width, activity, or basis-change levels
```

For the Catalan `A1` instance, the combinatorial side is deliberately modest. Catalan coefficients enumerate binary-tree and parenthesization structures that can serve as formula-shape or parse-shape corpora. The square-root singularity supplies a one-dimensional sign-line invariant. The map `E_phi` says where that sign-line invariant lives in the active constraint coordinates before any gate trajectory or monodromy computation is evaluated.

Thus:

- nondegeneracy of the transported pairing means the source invariant did not collapse under encoding;
- monodromy compatibility means the active-side trajectory realizes the declared source monodromy rather than a post-selected sign;
- filtration preservation means the bridge has not silently moved data across declared complexity levels;
- deterministic replay means the bridge is an auditable artifact rather than an interpretation after the fact.

What this could mean for complexity theory is conditional. A future Track B or Track C result would need to prove that a preserved pairing or filtration corresponds to a known proof-complexity or circuit-complexity quantity such as proof size, formula depth, width, simulation cost, substitution cost, or orbit-closure obstruction data.

Until such a transfer theorem or restricted-system theorem exists, `E_phi` has only the following status:

```text
well-typed invariant transport, not lower bound evidence
```

This is why the bridge is useful but not yet Clay-proximate. It creates a place where a complexity interpretation can be tested without claiming that the interpretation has already succeeded.

## 8. The A1 / Catalan specialization

The first test instance is intentionally small.

### Source side

```text
H_phi_bridge = L_phi
basis = [e]
M_phi = [-1]
G_phi = [q]
q != 0
```

### Active side under T2'

```text
G = SO(3)
auxiliary group = Spin(3)
V_A includes a declared direction v_minus
E = column vector selecting v_minus
sigma(gamma_tilde(1)) v_minus = -v_minus
E^T G_active E = [q]
```

### Minimal checks

```text
source_pairing_nonzero == true
E_declared_before_evaluation == true
rank(E) == 1
commutator_norm <= tolerance
pairing_transport_error <= tolerance
pairing_preservation_error <= tolerance
filtration_preservation_report == pass
```

The expected theorem value of this specialization is narrow: it supports the gate-minimality proof note by preventing arbitrary sign-realizing representations from being substituted after the fact.

## 9. Replay schema

Every replay artifact claiming polarization compatibility must emit:

```yaml
artifact_id: string
execution_status: doctrine_only | synthetic_fixture | runtime_executed | runtime_partial
claim_id: A1-POLARIZATION-001
theorem_branch: T2_prime
source:
  germ: A1
  source_pairing_gram_matrix: matrix
  monodromy_matrix_source: matrix
  source_basis: list[string]
  conventions_hash: string
active:
  spatial_group: SO(3)
  auxiliary_group: Spin(3)
  active_constraint_pairing_gram_matrix: matrix
  auxiliary_spin_action_matrix: matrix
  active_basis: list[string]
  gate_loop: gamma in pi_1(SO(3))
encoding:
  E_phi_matrix: matrix
  declared_before_evaluation: boolean
filtration:
  source_filtration: object
  active_filtration: object
  filtration_preservation_report: pass | fail
checks:
  source_pairing_nonzero: boolean
  encoding_rank: integer
  commutator_norm: number
  pairing_transport_error: number
  pairing_preservation_error: number
  tolerance: number
provenance:
  repo: string
  commit: string
  input_hash_chain: list[string]
  output_hash: string
  generated_at: string
```

No paid runtime is required for this stage. A doctrine-only or synthetic-fixture artifact is valid if it accurately declares `execution_status` and does not pretend to be a runtime certificate.

## 10. Pass / fail policy

A replay passes A1 only if:

```text
source_pairing_nonzero == true
E_declared_before_evaluation == true
encoding_rank == dim(H_phi_bridge)
commutator_norm <= tolerance
pairing_transport_error <= tolerance
pairing_preservation_error <= tolerance
filtration_preservation_report == pass
```

A replay fails if any of the following occurs:

- `E_phi` is selected after seeing the gate eigenspaces;
- the source pairing is zero or undeclared;
- the active pairing is extended without a rule;
- sign compatibility is used as a substitute for polarization compatibility;
- filtration data is omitted;
- convention hashes are missing;
- the artifact claims theorem status while only supplying a fixture;
- under `T2'`, `zeta = -I` is described as an element of `G = SO(3)` rather than as auxiliary spin data.

## 11. Relation to the gate-minimality theorem

This note supplies the polarization condition in the gate-minimality theorem target.

The faithful theorem branch may cite this note as the definition of a polarization-compatible `A1` bridge. The theorem should still prove its own Lie-theoretic claims:

1. faithful orthogonal triad action embeds the gate factor into `SO(3)`;
2. connected proper compact subgroups relevant to the triad are circle-type and abelian;
3. non-abelian active-set action forces full `SO(3)` image;
4. the nontrivial loop in `pi_1(SO(3))` lifts through the auxiliary `Spin(3)` frame to realize the half-integer sign;
5. the sign direction is fixed by the transported pairing and encoding, not post-selected.

## 12. Barrier applicability design intent

This section records design intent only. It does not mark any barrier as cleared. Barrier status remains governed by `docs/barriers/README.md`.

```yaml
barrier_position:
  relativization:
    status: design_intent_not_cleared
    position: >
      Track A1 is not an oracle-uniform simulation or diagonalization argument.
      It depends on monodromy, pairing transport, and filtration data for a declared
      algebraic family. That is the intended reason it is not obviously a
      relativizing technique. A later lower-bound claim must still prove that the
      relevant invariant distinguishes the unrelativized setting from oracle variants.
  natural_proofs:
    status: design_intent_not_cleared
    position: >
      Track A1 does not currently define a large constructive property of Boolean
      functions. It defines transport of a singular-germ invariant into an active
      morphology basis. If this transport is later converted into a Boolean-function
      property or circuit lower-bound property, that property must be classified for
      constructivity and largeness before promotion.
  algebrization:
    status: design_intent_not_cleared
    position: >
      Track A1 is designed to use geometric and topological data tied to specific
      algebraic families, including monodromy around discriminant loci, transported
      pairings, and filtration preservation. The intended non-algebrizing hope is
      that these are not merely low-degree oracle extensions or arithmetized
      black-box computations. This is not established and is the most important
      barrier question for the approach.
  proof_complexity_transfer:
    status: design_intent_not_cleared
    position: >
      Track A1 does not yet connect the transported pairing to proof-system size,
      width, depth, space, or simulation cost. Any proof-complexity claim requires
      a declared proof basis B, a translation morphism when comparing bases, and a
      theorem explaining what the preserved invariant measures.
  average_case_meta_complexity_transfer:
    status: design_intent_not_cleared
    position: >
      Track A1 is not distributional evidence. If renormalized defect or pairing
      preservation is later used for average-case or meta-complexity claims, the
      input distribution, tranche, null model, and transfer statement must be
      declared before observing the result.
```

## 13. Nonclaims

This file does not claim:

- P = NP;
- P != NP;
- NP != coNP;
- a Boolean circuit lower bound;
- a proof-system lower bound;
- a GCT obstruction;
- that every proof-character generating function admits a polarization-compatible singular-germ encoding;
- that `SO(3)` is forced without the Lawful Learning spatial-triad and non-abelian active-set assumptions;
- that `Spin(3)` should be treated as the universal cover of the spatial group in higher `A_k` cases;
- that Track A1 has cleared relativization, natural-proofs, algebrization, proof-complexity-transfer, or average-case/meta-complexity barriers.

It is a foundation note for Track A1 only.
