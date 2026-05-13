# `A_1` Spin-Polarized Gate Minimality Proof Note

Status: **proof note / conditional theorem**.

This note refines the `A_1` gate-minimality target by separating two statements that were previously conflated:

1. **Admissibility:** what a gate object must carry to realize the `A_1` bridge semantics;
2. **Minimality:** what the smallest spin-polarized object is once those structures are required.

The correction is important: `U(1)` can represent `-1`, so sign-realization alone selects nothing. The theorem is about the structural role: spatial-triad action, non-abelian active-set action, `SO(3)` loop class, `Spin(3)` lift, and polarization compatibility.

This note does not prove P vs NP, does not validate Lawful Learning, and does not establish the bridge for arbitrary proof-class generating functions.

## 1. Source object: the `A_1` germ

Let `T_phi` be a proof-class generating function whose local singular germ is square-root / `A_1` type. The branch system is two-sheeted, and local continuation around the branch point swaps sheets. On the reduced sign line `L_phi`, monodromy acts by `-1`.

For the spin-polarized bridge we distinguish:

```text
L_phi          one-dimensional reduced sign line
B_phi          two-dimensional branch-state module carrying the two sheets
Q_phi^spin     skew/symplectic pairing on the lifted branch-state module
```

The one-dimensional sign line records the `mu_2` monodromy. The two-dimensional branch-state module is the lifted space on which the spin/polarization semantics live. This prevents the proof from pretending that the reduced `A_1` cohomology line is itself a two-dimensional symplectic space.

## 2. Gate object

A spin-polarized gate object for the `A_1` bridge consists of:

```text
\tilde G ----p----> G_sp ----rho_sp----> SO(V_sp) ≅ SO(3)
        \                         
         \--rho_spin--> Sp(B_A, Q_A)
```

where:

- `V_sp ≅ R^3` is the Lawful Learning spatial triad;
- `G_sp` is the spatial rotation image;
- `\tilde G` is a compact connected Lie lift carrying the central sign;
- `rho_spin` acts on the lifted active branch module `B_A ≅ C^2`;
- `Q_A` is the transported symplectic pairing;
- `E_phi` identifies `B_phi` and its sign line with the corresponding active data before execution.

The triad action may be faithful for `G_sp`; it is not required to be faithful for `\tilde G`. This is necessary because `SU(2) -> SO(3)` has kernel `{±I}`, and the central element `-I` must remain visible on the spin/polarization side even though the triad quotient cannot see it.

## 3. T1 — Admissibility

### Theorem T1: admissibility package

Any gate object realizing the `A_1` spin-polarized semantics must supply the following structures:

1. **Connected compact Lie regularity:** the relevant gate factors are compact connected Lie groups.
2. **Spatial-triad action:** the object induces a nontrivial orthogonal action on the Lawful Learning spatial triad.
3. **Non-abelian active-set action:** the active branch/constraint action is non-abelian, preserving the abelian/non-abelian species distinction.
4. **Distinguished `Z/2` rotation loop:** the spatial image carries the nontrivial class in `pi_1(SO(3))` corresponding to the half-integer branch sign.
5. **Spin lift:** the nontrivial spatial loop lifts to a central element acting as `-id` on the lifted active branch module.
6. **Polarization compatibility:** the lifted action preserves the transported pairing `Q_A` and commutes with the encoding `E_phi`.

T1 is a specification theorem: it says what data an admissible instance must exhibit. It does not by itself select the minimal group.

## 4. T2 — Minimality, assuming polarization compatibility

### Theorem T2: `A_1` spin-polarized minimality

Assume the admissibility package T1 and the polarization compatibility contract in `docs/research/polarization-compatibility.md`. Then the minimal spin-polarized gate object is:

```text
SU(2) = Spin(3) ----2:1----> SO(3)
```

with:

- `SO(3)` acting on the spatial triad by the standard vector representation;
- `SU(2)` acting on the lifted branch module `C^2` by the standard spin representation;
- the central element `-I ∈ SU(2)` acting as `-id` on the lifted active branch module;
- the quotient loop in `SO(3)` representing the nontrivial element of `pi_1(SO(3)) ≅ Z/2`.

Equivalently: the spatial image forced by non-abelian triad semantics is `SO(3)`, but the polarization-visible minimal object is its spin cover `SU(2)`.

## 5. Proof of T2

### Step 1: reduce the spatial image

Let the spatial action have image in `O(3)`. Since the gate factor is connected, the determinant is constant, and because the identity has determinant `+1`, the image lies in `SO(3)`.

The connected compact subgroups of `SO(3)` are, up to conjugacy:

```text
trivial group,
SO(2)-type circle subgroup,
SO(3).
```

The proper connected subgroups are abelian. Therefore a non-abelian spatial/active realization cannot have a proper connected spatial image. The spatial image is `SO(3)`.

### Step 2: distinguish spatial quotient from spin lift

The triad action sees `SO(3)`. It does not see the central `-I` element because that element lives in the double cover:

```text
Spin(3)=SU(2) -> SO(3).
```

Thus a theorem stated only in terms of a faithful triad action selects `SO(3)`, while a theorem stated in terms of a polarization-visible spin action selects the pair `SU(2) -> SO(3)`.

This is the correction to the earlier proof note.

### Step 3: the polarization condition selects `SU(2)`

The lifted active branch module is two-dimensional complex symplectic data. The standard compact group preserving this spinor/polarization structure is:

```text
Sp(1) = SU(2).
```

The group `SO(3)` acts faithfully on the real triad, but it does not act faithfully on the two-dimensional spinor module. Its action appears only after projectivizing / quotienting the spin representation, where the central element `-I` becomes invisible.

Therefore the polarization-visible realization of the `A_1` sign requires the spin cover. The central element `-I ∈ SU(2)` acts as `-id` on `C^2`, giving the concrete group element that realizes the `A_1` sign.

### Step 4: verify `SU(2) -> SO(3)` is admissible

The object `SU(2) -> SO(3)` satisfies T1:

- compact connected Lie: yes;
- spatial triad action: through the adjoint/vector quotient `SU(2) -> SO(3)`;
- non-abelian active action: standard `SU(2)` action on `C^2` is non-abelian;
- distinguished `Z/2` loop: the nontrivial loop in `SO(3)` is the quotient loop;
- spin lift: the lifted endpoint is central `-I ∈ SU(2)`;
- polarization compatibility: by assumption, the standard symplectic pairing on the lifted active module is the transported `Q_A`.

### Step 5: minimality

Any admissible object must have spatial image `SO(3)` by Step 1. Any polarization-visible lift of the nontrivial loop must retain the central sign that the spatial quotient forgets. The minimal compact connected Lie cover of `SO(3)` carrying that central sign is `Spin(3)=SU(2)`.

A proper closed connected subgroup of `SU(2)` is abelian, conjugate to a maximal torus `U(1)`, and fails the non-abelian active-set condition. Higher-dimensional compact connected groups may contain or map onto the required `SU(2)` structure, but they add redundant degrees of freedom relative to the `A_1` sign bridge.

Thus the minimal spin-polarized object is the pair:

```text
SU(2) -> SO(3).
```

This completes the conditional proof. `□`

## 6. Counterexamples when conditions are removed

| Removed condition | Counterexample | Why it shows the condition is necessary |
|---|---|---|
| Non-abelian active-set action | `U(1)` | Contains `-1` and can rotate a plane, but is abelian. |
| Polarization / spin visibility | `SO(3)` alone | Has the `Z/2` loop class but not the central `-I` acting on the spinor module. |
| Connected compact Lie regularity | abstract `Z/2` | Has a sign but no controlled Lie monodromy or triad geometry. |
| `Z/2` loop / spin lift | higher groups without chosen lift | Non-abelian structure alone does not identify the half-integer branch sign. |
| Symplectic polarization | orthogonal-only model | The minimal object may revert to `SO(3)` or another orthogonal group. |

## 7. Interaction with the Catalan harness

The Catalan harness verifies an **instance** of the theorem target. It does not independently prove T2.

The contract is:

```text
T2 proves: polarization-compatible A_1 bridge -> minimal spin object SU(2)->SO(3).
Catalan harness verifies: Catalan carries the A_1 sign and the run instantiates the declared spin lift.
```

The Stokes-side checks verify the abstract `Z/2` branch data. The Spin-lift and polarization checks verify that the run realizes that data through the minimal spin-polarized object.

## 8. What remains conditional

The proof depends on:

1. the Lawful Learning spatial triad being part of the committed model;
2. non-abelian active-set action being required for the non-abelian species lane;
3. `E_phi` being supplied and ledgered;
4. polarization compatibility holding for the claimed encoding;
5. the singularity being in the scoped base class: algebraic isolated `A_1` for this theorem.

## 9. Nonclaims

This theorem does not apply if:

- the spatial triad is removed;
- the active action is allowed to be abelian;
- the polarization is orthogonal rather than spin/symplectic;
- the group is allowed to be disconnected or non-Lie without a replacement theory;
- the singularity is outside the declared algebraic isolated `A_1` scope;
- polarization compatibility is not established.

It does not imply any complexity-theoretic lower bound or any P vs NP result.
