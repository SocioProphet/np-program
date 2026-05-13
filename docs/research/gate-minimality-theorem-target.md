# Gate Minimality Theorem Target

Status: **theorem target / refined**.

This note records the first concrete theorem target created by the singular-germ enrichment. Its purpose is to close the canonicity gap for the `mu_2` bridge in the half-integer / square-root case.

The target is now explicitly split into two layers:

1. **Spatial quotient:** the non-abelian triad image is forced to be `SO(3)`.
2. **Spin-polarized lift:** the polarization-visible minimal object is the cover `SU(2)=Spin(3) -> SO(3)`.

This distinction is necessary because `SO(3)` carries the spatial loop class, while `SU(2)` carries the central element `-I` that acts on the lifted spin/polarization module.

## 1. The canonicity gap

The `A_1` / square-root singularity naturally produces a two-sheeted branch system and a sign monodromy. This supports the `mu_2` bridge:

```text
singular monodromy -> chi_2 sign -> topological torsion sign -> gate-loop sign
```

However, the gate realization is not canonical merely because it displays a sign. A sign can be represented in `U(1)` by the element `-1`. Sign-realization alone selects nothing.

The gate target becomes meaningful only after the Lawful Learning geometry and polarization data are included.

## 2. Corrected admissibility conditions

The admissible object is not merely a group carrying `-1`; it is a spin-polarized gate object with:

1. **Spatial triad action.** A compact connected Lie object induces a nontrivial orthogonal real 3-dimensional action on the Lawful Learning spatial triad.
2. **Non-abelian active-set action.** Its lifted active/branch action is non-abelian. This preserves the abelian/non-abelian species bifurcation.
3. **Connected compact Lie regularity.** The relevant factors are compact, connected, and Lie, so the monodromy representation is controlled by standard differential topology.
4. **Distinguished `Z/2` spatial loop.** The spatial quotient carries the nontrivial loop in `pi_1(SO(3))` required by the half-integer branch sign.
5. **Spin lift.** The nontrivial spatial loop lifts to a central element acting as `-id` on the lifted active branch module.
6. **Polarization compatibility.** The lifted action preserves the pairing and filtration transported from the `A_1` singular germ by the encoding map `E_phi`.

Condition 6 is the load-bearing canonicity condition. Conditions 1–5 force the correct Lie-theoretic arena; condition 6 prevents arbitrary representation substitution from changing the bridge.

## 3. Why `U(1)` is excluded

`U(1)` can represent a sign, and it can act on a real three-dimensional space as a rotation plane plus a fixed axis. Therefore it is incorrect to exclude `U(1)` by sign-realization or by bare 3-dimensional representability.

`U(1)` is excluded because it is abelian and cannot supply the non-abelian active-set action required by the species bifurcation. It also does not implement the same spatial-loop-to-spin-central-element conversion required by the Catalan `A_1` harness.

## 4. Lie-theoretic reduction

The spatial image is a connected compact subgroup of `SO(3)`.

The connected compact subgroups of `SO(3)` relevant here are:

```text
SO(2)      abelian
SO(3)      non-abelian
```

Thus a compact connected Lie object acting non-abelianly through the spatial triad must have spatial image `SO(3)`.

But the polarization-visible sign is not a group element of `SO(3)`. It is the central element in the spin cover:

```text
SU(2)=Spin(3) -> SO(3).
```

Therefore the minimal theorem target is the pair `SU(2) -> SO(3)`, not `SO(3)` alone.

## 5. Candidate theorem statements

### T1: Admissibility

Any gate object realizing the `A_1` spin-polarized semantics must provide the six structures listed in Section 2.

### T2: Spin-polarized minimality

Assume T1 and the polarization compatibility contract in:

```text
docs/research/polarization-compatibility.md
```

Then the minimal spin-polarized gate object for the half-integer `mu_2` bridge is:

```text
SU(2)=Spin(3) -> SO(3)
```

where:

- `SO(3)` is the forced non-abelian spatial triad image;
- `SU(2)` is the minimal compact connected lift carrying the central element `-I`;
- the standard spin action on the lifted branch module preserves the transported symplectic pairing;
- the central `-I` realizes the `A_1` sign on the distinguished lifted eigendirection.

## 6. Proof plan

### Step 1: force the spatial image

Show that the spatial action has connected compact image in `SO(3)`.

### Step 2: exclude abelian images

Show that connected proper compact subgroups of `SO(3)` are abelian circle-type subgroups. These cannot satisfy the non-abelian active-set action requirement.

### Step 3: recover `SO(3)` spatial quotient

Conclude that the spatial image must be all of `SO(3)`.

### Step 4: attach the spin lift

Show that the nontrivial loop in `SO(3)` lifts through `Spin(3)=SU(2)` to a path ending at `-I`, and that this central element acts as `-id` on the lifted active branch module.

### Step 5: apply polarization compatibility

Use the pairing transported by `E_phi` to show that the lifted spin representation, not an after-the-fact eigenspace selection, realizes the singular-germ sign.

## 7. Expected conclusion

If proved, the result does not prove P vs NP, Lawful Learning, or the proof-character program. It proves something narrower but important:

```text
for the half-integer singular-germ bridge, the spatial quotient is forced to SO(3), and the polarization-visible minimal lift is SU(2)=Spin(3).
```

That closes the canonicity gap for the first bridge instance under the `A_1` assumptions.

## 8. Open risks

1. If the spatial-triad requirement is weakened, `SO(3)` will not be forced as the spatial quotient.
2. If non-abelian active-set action is removed, abelian sign targets such as `U(1)` compete.
3. If polarization compatibility is too narrowly defined, the theorem becomes tautological.
4. If the polarization is orthogonal rather than spin/symplectic, the minimal object may revert to `SO(3)` or change type.
5. The proof depends on the precise Lawful Learning gate geometry, so this theorem must be versioned against the committed gate model.

## 9. Current proof note

The current proof note is:

```text
docs/research/a1-gate-minimality-proof.md
```

It proves the refined spin-polarized statement conditionally on the polarization compatibility contract.
