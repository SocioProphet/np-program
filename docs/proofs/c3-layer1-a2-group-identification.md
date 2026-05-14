# C-3' Layer 1: A2 Group Identification and Cohomological Consequences

Status: **C-3' Layer 1 draft / theorem-input scoping note / not a Clay claim**.  
Depends on: `docs/proofs/a1-gate-minimality-faithful.md`, `docs/proofs/a1-gate-minimality-assuming-polarization.md`, `docs/foundations/polarization.md`, `docs/scope/singularity-classes.md`.  
Related issue: `#7` — C-3' cohomological projective-representation obstruction.

## 0. Purpose

This note starts the C-3' work by pinning the Layer 1 group-identification problem for the `A2` extension.

The A1 faithful branch has a specific obstruction story:

```text
SO(3) projective action on V_A
H^2(SO(3); U(1)) = Z/2
auxiliary Spin(3) resolves the nontrivial class
zeta = sigma(gamma_tilde(1)) = -I on V_A
```

The `A2` case must not inherit that story by replacing `2` with `3`. The group, obstruction class, monodromy character, and polarization data have to be identified separately.

This file addresses only Layer 1:

```text
Which group or groups are candidates for the A2 obstruction / monodromy / sheet structure?
What are their immediate cohomological consequences?
```

It does not supply Layer 2 data:

```text
V_A^(2), Q_A^(2), monodromy^(2), polarization^(2), E_phi^(2)
```

and it does not prove the A2 gate-minimality theorem.

## 1. Three group roles that must not be conflated

The A2 problem has at least three distinct group roles.

### 1.1 Branch or local monodromy group

For an `A2` cube-root-type local model, the local analytic branch behavior carries a cyclic order-three monodromy:

```text
mu_3 = {1, omega, omega^2}
```

or equivalently a cyclic `C3` action on a chosen root coordinate.

This is the natural group seen by a Fuss-Catalan / cubic-branch harness at Stage 1. It records sheet cycling and root-of-unity multipliers.

### 1.2 McKay finite subgroup

Under the ADE / McKay correspondence, type `A_k` corresponds to the cyclic subgroup:

```text
C_{k+1} subset SU(2).
```

For `A2`, the corresponding finite subgroup is:

```text
C3 subset SU(2).
```

This is a finite ADE label group. It is not the same thing as the faithful spatial group `G = SO(3)` used in the A1 `T2'` branch.

### 1.3 Sheet-permutation or discriminant-loop group

If the model tracks all local sheets and not only a chosen cyclic monodromy generator, a larger sheet-permutation group may appear. For a cubic algebraic equation, the full permutation group of three roots can be:

```text
S3
```

in a generic discriminant setting.

This is not automatically the A2 obstruction group. It becomes relevant only if the A2 harness or proof object includes sheet permutations beyond the cyclic local monodromy.

## 2. Preliminary candidate table

| Role | Candidate | Status | Immediate consequence |
|---|---|---|---|
| Local branch monodromy | `C3` / `mu_3` | primary Stage-1 candidate | captures cubic sheet cycling and root-of-unity multiplier |
| McKay ADE finite subgroup | `C3 subset SU(2)` | primary ADE candidate | Schur multiplier is trivial; no A1-style projective obstruction from `C3` itself |
| Generic cubic sheet permutations | `S3` | conditional candidate | only relevant if harness tracks full sheet permutations / discriminant loops |
| Faithful spatial group | `SO(3)` | inherited only as spatial-triad context, not as A2 obstruction | A1 `H^2(SO(3); U(1))` calculation does not by itself attach to A2 `V_A^(2)` |
| Higher internal carrier | `SU(3)` or other | not justified at Layer 1 | requires independent construction of `V_A^(2)`, pairing, and action |

## 3. Cohomological consequences

### 3.1 Cyclic C3 has trivial Schur multiplier

For finite groups with trivial `U(1)` coefficients, the second cohomology classifying projective representations is the Schur multiplier:

```text
H^2(G; U(1)).
```

For a cyclic group:

```text
H^2(C_n; U(1)) = 0.
```

Therefore:

```text
H^2(C3; U(1)) = 0.
```

If Layer 1 chooses `C3` as the A2 obstruction group, then there is no nontrivial A1-style projective-representation obstruction class at the level of `C3` itself.

This does not mean A2 is trivial. It means the A2 obstruction, if present, must live somewhere else:

```text
- in the monodromy character rather than a projective obstruction;
- in the polarization attachment;
- in a sheet-permutation/discriminant group;
- in a spatial/projective group not yet identified;
- or in a higher categorical/bundle obstruction.
```

### 3.2 C3 still has nontrivial characters

The absence of a Schur-multiplier obstruction is not the absence of monodromy.

`C3` has nontrivial one-dimensional characters:

```text
Hom(C3, U(1)) ~= mu_3.
```

Thus a Stage-1 A2 harness can validly observe:

```text
omega, omega^2
```

as monodromy multipliers or sheet-cycling eigenvalues. Those are character data, not projective-obstruction data.

This distinction is load-bearing:

```text
A1: projective obstruction plus auxiliary Spin(3) realization under T2'.
A2: likely mu_3 character / sheet monodromy at Stage 1, with obstruction attachment still open.
```

### 3.3 S3 is a conditional branch

If the proof object expands from cyclic branch monodromy to full cubic sheet permutations, then `S3` may enter. In that case the cohomology and extension problem must be recalculated for `S3` and for the actual representation/polarization data used.

No A2 result may silently switch from `C3` to `S3` after observing harness output. The group role must be declared before measurement.

### 3.4 SO(3) remains spatial context only unless reattached

The faithful A1 branch uses `SO(3)` as the minimal faithful spatial group and auxiliary `Spin(3)` to resolve the projective action on `V_A`.

For A2, the calculation

```text
H^2(SO(3); U(1)) = Z/2
```

remains true as a fact about `SO(3)` projective representations. But it does not automatically attach to the A2 polarization space. A2 must specify:

```text
V_A^(2)
Q_A^(2)
E_phi^(2)
monodromy^(2)
central or character datum
how SO(3), C3, S3, or another group acts on the declared data
```

without that attachment, the A1 obstruction class is not inherited.

## 4. Layer 1 conclusion

The preliminary Layer 1 conclusion is:

```text
The natural A2 finite/ADE/local-monodromy candidate is C3, not an A1-style Z/2 obstruction group.
```

Because:

```text
H^2(C3; U(1)) = 0,
```

A2 does not possess the same projective-obstruction story at the `C3` level that A1 possesses through the `SO(3)` / `Spin(3)` faithful branch.

The A2 Stage-1 harness may still detect `mu_3` monodromy data. But `mu_3` character data are not enough to supply Stage-2 gate-minimality or polarization attachment.

## 5. Consequence for the A2 / Fuss-Catalan harness

The A2 harness is a Layer 2 instrument only if it emits:

```text
Stokes multipliers
additive jumps
sheet structure
lateral values
coefficient enumeration
normalization metadata
```

Those outputs can validate the analytic `A2` normalization and Stage-1 dimensional behavior.

They do not resolve Layer 1 unless the harness also declares which group role is being tested:

```text
C3 branch monodromy
C3 McKay subgroup
S3 full sheet permutation
SO(3) spatial/projective carrier
other declared group
```

They do not resolve Stage 2 unless the harness or a companion proof supplies:

```text
V_A^(2), Q_A^(2), E_phi^(2), monodromy^(2), polarization^(2), obstruction or character attachment.
```

## 6. Required next Layer 2 data

Before any A2 gate-minimality statement, a follow-up note must define:

```text
1. V_A^(2): active vector or polarization space for A2.
2. Q_A^(2): pairing / symplectic / Hermitian / intersection form data.
3. E_phi^(2): predeclared transport map from the A2 source space.
4. M_phi^(2): source monodromy and its eigen/sheet decomposition.
5. M_A^(2): active-side action corresponding to the declared group role.
6. Compatibility equation: M_A^(2) E_phi^(2) = E_phi^(2) M_phi^(2).
7. Pairing transport: E^* Q_A^(2) E = Q_phi^(2), or declared variant.
8. Filtration preservation.
```

Without these objects, A2 remains Stage 1.

## 7. Nonclaims

This note does not claim:

- an A2 gate-minimality theorem;
- an A2 lower-bound result;
- that `C3` is the final A2 obstruction group;
- that `S3` is irrelevant in every A2 setup;
- that `SU(3)` is the correct carrier group;
- that the A1 `SO(3)` / `Spin(3)` obstruction generalizes;
- that a `mu_3` Stokes multiplier is a readout-compatible active eigendirection;
- any progress on P vs NP or a Clay problem.

It is a Layer 1 scoping note. Its function is to prevent A2 from inheriting A1's projective-obstruction structure without proof.

## 8. Promotion rule

An A2 claim may be promoted beyond Stage 1 only after:

```text
1. the group role is declared before measurement;
2. the cohomological consequence of that group role is stated;
3. the A2-specific polarization data are constructed;
4. the A2 compatibility equations are checked;
5. nonclaim boundaries are preserved.
```

Until then, A2/Fuss-Catalan harness output is analytic normalization evidence only.