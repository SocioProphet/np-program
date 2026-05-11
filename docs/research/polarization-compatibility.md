# Polarization Compatibility

Status: **load-bearing axiom / theorem-input definition / not yet proved canonical**.

This note makes explicit the fifth condition in the gate-minimality program: the gate action must preserve the pairing transported from the singular germ. This is the condition that prevents the `SO(3)` gate realization from being an arbitrary representation choice.

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
codimension / activity filtration W_A
holonomy representation rho_A
ledgered gate trajectory gamma
```

Polarization compatibility is the assertion that the encoding `E_phi` transports the source pairing into a preserved gate-side pairing.

## 2. Encoding data

Let:

```text
E_phi: H^*(F_phi) -> V_A
```

be the linear part of the encoding map from singular-germ cohomology to the active constraint vector space.

Admissibility requires:

1. `E_phi` maps the distinguished monodromy eigenspaces into distinguished gate eigenspaces.
2. `E_phi` respects the relevant filtrations: weight / codimension / activity.
3. `E_phi` is injective on the bridge-relevant subspace, especially the sign line in the `A_1` case.
4. `E_phi` has ledgered provenance: the map is part of the artifact, not reconstructed after observing the result.

## 3. Transported polarization

Let `Q_phi` be the source pairing on the bridge-relevant cohomology subspace. Define the transported gate-side pairing `Q_A` on `im(E_phi)` by:

```math
Q_A(E_phi(u), E_phi(v)) = Q_phi(u,v)
```

If `E_phi` is extended to a larger active constraint space, `Q_A` must be extended by a declared rule. Acceptable extensions are:

1. orthogonal direct-sum extension;
2. minimal nondegenerate extension preserving the activity filtration;
3. explicitly ledgered numerical extension with replayable Gram matrix.

Unledgered extension choices are inadmissible.

## 4. Polarization-compatible gate action

Let `rho_A: G -> GL(V_A)` be the active-constraint representation of the gate group.

A gate action is **polarization-compatible** with `E_phi` if, for every admissible gate element `g` and for every `u,v` in the bridge-relevant source subspace,

```math
Q_A(rho_A(g)E_phi(u), rho_A(g)E_phi(v)) = Q_A(E_phi(u), E_phi(v))
```

and the following diagrams commute:

```text
H^*(F_phi) --T_phi--> H^*(F_phi)
   | E_phi                 | E_phi
   v                       v
V_A --------rho_A(gamma)--> V_A
```

and

```text
filtration on H^*(F_phi) --E_phi--> filtration on V_A
```

Thus the gate-side monodromy is not merely numerically equal to the singular monodromy; it is the transported action under `E_phi`.

## 5. The `A_1` / half-integer case

For the square-root / `A_1` bridge, the branch system is two-sheeted. The bridge-relevant reduced cohomology is a one-dimensional sign line.

The required data are:

```text
L_phi      = sign line of the A_1 branch system
Q_phi      = normalized nonzero pairing on L_phi
E_phi(L)   = distinguished gate eigendirection
rho(gamma) = -1 on E_phi(L)
```

Polarization compatibility forces the sign line and gate eigendirection to be identified before execution. A run cannot choose the eigendirection after seeing which eigenvalue is `-1`.

## 6. Why this is load-bearing

Without polarization compatibility, any group that can display a sign can be substituted into the bridge. That makes the bridge representation-dependent.

With polarization compatibility, the admissible gate group must preserve the transported pairing and filtration. This is what lets the gate-minimality theorem argue that `SO(3)` / `Spin(3)` is forced inside the Lawful Learning spatial-triad model rather than merely convenient.

## 7. Implementation requirements

Every implementation claiming polarization compatibility must emit:

```text
source_pairing_gram_matrix
active_constraint_pairing_gram_matrix
E_phi_matrix
monodromy_matrix_source
monodromy_matrix_gate
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
```

## 8. Nonclaims

This note does not prove that every proof-class generating function admits such an encoding. It defines what counts as an admissible encoding when the bridge is claimed.
