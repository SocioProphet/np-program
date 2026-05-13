# Polarization Compatibility

Status: **load-bearing axiom / theorem-input definition / not yet proved canonical**.

This note makes explicit the polarization condition in the gate-minimality program: the lifted gate action must preserve the pairing transported from the singular germ. This is the condition that prevents the `SO(3)` / `Spin(3)` gate realization from being an arbitrary representation choice.

## 1. Purpose

The singular-germ bridge sends local data of a proof-class generating function `T_phi` into a gate / constraint system. The bridge is only canonical if it preserves the pairings and filtrations that are intrinsic on the singular side.

For an algebraic isolated germ, the source side carries:

```text
Milnor fiber F_phi
cohomology H^*(F_phi)
monodromy T = T_s T_u
filtration data
polarization / intersection-type pairing Q_phi
```

The gate side carries:

```text
active constraint complex K_A
constraint vector space V_A
lifted active branch module B_A
codimension / activity filtration W_A
holonomy representation rho_A
spin/polarization representation rho_spin
ledgered gate trajectory gamma
```

Polarization compatibility is the assertion that the encoding `E_phi` transports the source pairing into a preserved gate-side pairing.

## 2. Encoding data

Let:

```text
E_phi: bridge-relevant singular data -> active gate data
```

be the encoding map. Depending on the singularity, this may include reduced cohomology, branch-state data, or lifted spin/polarization data.

Admissibility requires:

1. `E_phi` maps distinguished monodromy eigenspaces into distinguished gate eigenspaces.
2. `E_phi` respects the relevant filtrations: weight / codimension / activity.
3. `E_phi` is injective on the bridge-relevant subspace.
4. `E_phi` has ledgered provenance: the map is part of the artifact, not reconstructed after observing the result.
5. In the `A_1` case, `E_phi` distinguishes the reduced sign line from the lifted two-dimensional branch module.

## 3. Transported polarization

Let `Q_phi` be the source pairing on the bridge-relevant source module. Define the transported gate-side pairing `Q_A` on `im(E_phi)` by:

```math
Q_A(E_phi(u), E_phi(v)) = Q_phi(u,v)
```

If `E_phi` is extended to a larger active constraint space, `Q_A` must be extended by a declared rule. Acceptable extensions are:

1. orthogonal direct-sum extension;
2. symplectic direct-sum extension where the lifted module is spin/symplectic;
3. minimal nondegenerate extension preserving the activity filtration;
4. explicitly ledgered numerical extension with replayable Gram matrix.

Unledgered extension choices are inadmissible.

## 4. Polarization-compatible gate action

Let `rho_A` be the active-constraint representation of the gate object, and let `rho_spin` be the lifted representation when spin/polarization data are present.

A gate action is **polarization-compatible** with `E_phi` if, for every admissible lifted gate element `g` and for every `u,v` in the bridge-relevant source module,

```math
Q_A(rho(g)E_phi(u), rho(g)E_phi(v)) = Q_A(E_phi(u), E_phi(v))
```

and the following diagrams commute:

```text
source module --source monodromy--> source module
      | E_phi                         | E_phi
      v                               v
active module -----gate monodromy---> active module
```

and

```text
source filtration --E_phi--> active filtration
```

Thus the gate-side monodromy is not merely numerically equal to the singular monodromy; it is the transported action under `E_phi`.

## 5. The `A_1` / half-integer case

For the square-root / `A_1` bridge, the branch system is two-sheeted.

There are two related but distinct source modules:

```text
L_phi      = one-dimensional reduced sign line
B_phi      = two-dimensional branch-state / spin-lift module
```

The sign line records monodromy by `-1`. The branch-state module is the lifted space on which the spin/polarization structure is represented.

The required data are:

```text
L_phi        sign line of the A_1 branch system
B_phi        lifted two-dimensional branch module
Q_phi^spin   normalized symplectic pairing on B_phi
E_phi(L)     distinguished gate sign eigendirection
E_phi(B)     lifted active branch module B_A
rho_spin     spin action preserving Q_A
rho(gamma)   -1 on E_phi(L), and -id on the lifted spin endpoint
```

Polarization compatibility forces the sign line, branch module, and gate eigendirection to be identified before execution. A run cannot choose the eigendirection after seeing which eigenvalue is `-1`.

## 6. Why this is load-bearing

Without polarization compatibility, any group that can display a sign can be substituted into the bridge. That makes the bridge representation-dependent.

With polarization compatibility, the admissible gate object must preserve the transported pairing and filtration. This is what lets the gate-minimality theorem argue that `SU(2)=Spin(3)` over the spatial quotient `SO(3)` is forced inside the Lawful Learning spatial-triad model rather than merely convenient.

## 7. Implementation requirements

Every implementation claiming polarization compatibility must emit:

```text
source_pairing_gram_matrix
active_constraint_pairing_gram_matrix
E_phi_matrix
source_sign_line_id
source_branch_module_id
active_branch_module_id
monodromy_matrix_source
monodromy_matrix_gate
spin_endpoint
commutator_norm
pairing_preservation_error
filtration_preservation_report
hash_chain
```

Hard pass conditions:

```text
commutator_norm <= tolerance
pairing_preservation_error <= tolerance
filtration_preservation_report == pass
E_phi_matrix declared before monodromy evaluation
spin_endpoint == -I for the A1 nontrivial lift
```

## 8. Nonclaims

This note does not prove that every proof-class generating function admits such an encoding. It defines what counts as an admissible encoding when the bridge is claimed.
