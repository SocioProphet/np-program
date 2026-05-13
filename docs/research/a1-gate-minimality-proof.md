# `A_1` Gate Minimality Proof Note

Status: **proof note / conditional theorem**.

This note proves the Lie-theoretic part of the `A_1` gate-minimality target, conditional on the polarization compatibility contract in `docs/research/polarization-compatibility.md` and the committed Lawful Learning spatial-triad model.

It does not prove P vs NP, does not validate Lawful Learning, and does not establish the bridge for arbitrary proof-class generating functions.

## 1. Setup

Let `T_phi` be a proof-class generating function whose local singular germ is of square-root / `A_1` type. The branch system is two-sheeted, and the bridge-relevant reduced cohomology contains a one-dimensional sign line `L_phi` on which the generator of local monodromy acts by `-1`.

Let `V_sp ≅ R^3` be the Lawful Learning spatial triad. Let `H` be a compact connected Lie gate factor equipped with an orthogonal real representation

```math
\rho: H \longrightarrow SO(V_{sp}) \cong SO(3).
```

The admissibility package for the `A_1` bridge is:

1. `rho` is faithful on the gate factor under consideration;
2. the induced active-set action is non-abelian;
3. the gate factor is compact, connected, and Lie;
4. the gate trajectory contains the nontrivial `Z/2` loop class required by the half-integer branch sign;
5. the encoding `E_phi` is polarization-compatible: the transported pairing and filtration are preserved and the sign eigendirection is fixed before execution.

The theorem below proves that these assumptions force the triad gate factor to be `SO(3)`.

## 2. Theorem

### Theorem: `A_1` triad gate minimality

Under the admissibility package above, any compact connected Lie gate factor acting faithfully and orthogonally on the Lawful Learning spatial triad with non-abelian active-set action has triad image `SO(3)`. If the triad representation is faithful, then the gate factor is isomorphic to `SO(3)`.

Moreover, the nontrivial loop in `SO(3)` lifts through

```text
Spin(3) = SU(2) -> SO(3)
```

to a path starting at `I` and ending at `-I`, realizing the `A_1` monodromy sign on the distinguished lifted eigendirection specified by `E_phi`.

## 3. Proof

### Step 1: the triad image is a connected compact subgroup of `SO(3)`

Because `H` is compact and connected and `rho` is continuous, `rho(H)` is a compact connected Lie subgroup of `SO(3)`. Because `rho` is orthogonal on the triad, the image lies in `SO(3)` after fixing the orientation convention for the spatial triad.

If the original representation lands in `O(3)`, connectedness forces the determinant sign to be constant. Since the identity has determinant `+1`, the entire image lies in `SO(3)`.

### Step 2: proper connected compact subgroups of `SO(3)` are abelian

The Lie algebra of a connected Lie subgroup of `SO(3)` is a Lie subalgebra of `so(3)`. The nonzero proper Lie subalgebras of `so(3)` are one-dimensional. Each one-dimensional Lie algebra is abelian, and its connected subgroup is conjugate to a circle rotation subgroup `SO(2)` inside `SO(3)`.

Thus a connected compact subgroup of `SO(3)` is one of:

```text
trivial group,
SO(2)-type circle subgroup,
SO(3).
```

The first two are abelian. Therefore any connected compact subgroup of `SO(3)` whose induced action must support non-abelian active-set behavior must have image `SO(3)`.

### Step 3: faithful triad action identifies the gate factor

Since `rho(H)=SO(3)` and `rho` is faithful on the gate factor, `rho` is an isomorphism of compact connected Lie groups from `H` onto `SO(3)`.

Therefore `H ≅ SO(3)`.

This proves uniqueness/minimality in the admissible triad category: any additional compact connected Lie structure either fails faithfulness on the triad factor or is redundant relative to the `A_1` bridge.

### Step 4: the `Spin(3)` lift gives the sign

The universal double cover of `SO(3)` is

```text
Spin(3) = SU(2) -> SO(3),
```

with kernel `{+I, -I}`. The nontrivial loop class in

```text
pi_1(SO(3)) ≅ Z/2
```

lifts to a path in `SU(2)` beginning at `I` and ending at `-I`. The endpoint `-I` is the nontrivial central element and acts as multiplication by `-1` on the distinguished lifted sign line.

By polarization compatibility, that sign line is not selected after the computation. It is the image under `E_phi` of the `A_1` monodromy line `L_phi`. Thus the gate-side sign is the transported singular-germ sign.

### Step 5: exclusion of `U(1)` and other abelian sign carriers

`U(1)` can represent the number `-1`, and it can act on a real three-dimensional space as a rotation plane plus a fixed axis. This is why sign-realization alone is insufficient.

However, any such `U(1)` action is abelian. It cannot satisfy the non-abelian active-set action required by the species bifurcation. It also cannot be the uniquely minimal non-abelian triad gate factor. Therefore `U(1)` is excluded by the admissibility package, not by inability to display a sign.

This completes the proof. `□`

## 4. What is proved

The proof establishes:

```text
Within the committed Lawful Learning spatial-triad admissible class, the half-integer / A_1 mu_2 bridge forces SO(3) as the minimal non-abelian compact connected gate factor, and Spin(3) supplies the canonical lifted sign.
```

This closes the first Lie-theoretic part of the canonicity gap.

## 5. What remains conditional

The proof still depends on the following external commitments:

1. The Lawful Learning model really commits to a spatial triad.
2. The active-set action must be non-abelian for the non-abelian species lane.
3. The encoding `E_phi` must be supplied and ledgered for each instance.
4. Polarization compatibility must hold for the claimed encoding.
5. The proof-class generating function must be in the scoped singularity class, presently algebraic isolated singularities for the base theory.

## 6. Implementation consequences

A Catalan `mu_2` run must not merely output a matrix with eigenvalue `-1`. It must also provide:

```text
E_phi_matrix
source_pairing_gram_matrix
active_constraint_pairing_gram_matrix
monodromy_matrix_source
monodromy_matrix_gate
commutator_norm
pairing_preservation_error
filtration_preservation_report
Spin_lift_start
Spin_lift_end
```

The sign passes only when the eigendirection is specified by `E_phi` and the gate loop lifts from `I` to `-I`.

## 7. Nonclaims

This theorem does not apply if:

- the spatial triad is removed;
- non-abelian active-set action is not required;
- the group is allowed to be disconnected or non-Lie without additional hypotheses;
- the singularity is outside the declared algebraic isolated scope;
- polarization compatibility is not established.

It does not imply any complexity-theoretic lower bound or any P vs NP result.
