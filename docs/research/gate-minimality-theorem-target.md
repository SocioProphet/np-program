# Gate Minimality Theorem Target

Status: **theorem target / not established**.

This note records the first concrete theorem target created by the singular-germ enrichment. Its purpose is to close the canonicity gap for the `mu_2` bridge in the half-integer / square-root case.

## 1. The canonicity gap

The `A_1` / square-root singularity naturally produces a two-sheeted branch system and a sign monodromy. This supports the `mu_2` bridge:

```text
singular monodromy -> chi_2 sign -> topological torsion sign -> gate-loop sign
```

However, the gate realization is not canonical merely because it displays a sign. A sign can be represented in `U(1)` by the element `-1`. Sign-realization alone selects nothing.

The gate target becomes meaningful only after the Lawful Learning geometry is included.

## 2. Corrected admissibility conditions

The admissible target is not merely a group carrying `Z/2`; it is a compact connected Lie gate factor whose action satisfies all of the following:

1. **Spatial triad action.** It acts by an orthogonal real 3-dimensional representation on the Lawful Learning spatial triad.
2. **Non-abelian active-set action.** Its induced action on the active constraint set is non-abelian. This preserves the abelian/non-abelian species bifurcation.
3. **Connected compact Lie regularity.** The group is compact, connected, and Lie, so the monodromy representation is controlled by standard differential topology.
4. **Nontrivial fundamental group.** Its fundamental group contains the required `Z/2` loop class for the half-integer branch sign.
5. **Polarization compatibility.** The action preserves the pairing and filtration transported from the `A_1` singular germ by the encoding map `E_phi`.

Condition 5 is the load-bearing canonicity condition. Conditions 1–4 force the correct Lie-theoretic arena; condition 5 prevents arbitrary conjugation or representation substitution from changing the bridge.

## 3. Why `U(1)` is excluded

`U(1)` can represent a sign, and it can act faithfully on a real 3-dimensional space as a rotation plane plus a fixed axis. Therefore it is incorrect to exclude `U(1)` by sign-realization or by bare 3-dimensional representability.

`U(1)` is excluded because it is abelian and cannot supply the non-abelian active-set action required by the species bifurcation. It also cannot be the minimal non-abelian compact connected gate factor compatible with the spatial-triad bridge.

## 4. Lie-theoretic reduction

Once a faithful orthogonal 3-dimensional gate action is required, the image of the gate factor is a connected compact subgroup of `SO(3)`.

The connected compact subgroups of `SO(3)` relevant here are:

```text
SO(2)      abelian
SO(3)      non-abelian
```

Thus a compact connected Lie group acting faithfully and non-abelianly on the triad must have image `SO(3)`. If the representation is faithful, the group itself is isomorphic to `SO(3)`.

This is the clean reason the corrected theorem is attackable: the classical Lie-theoretic part is short. The new work is proving that the representation and pairing are forced by the encoding `E_phi`.

## 5. Candidate theorem statement

### Gate minimality theorem target, `A_1` case

Let `C_{A1}` be the class of compact connected Lie gate factors `H` equipped with:

- a faithful orthogonal real 3-dimensional representation on the Lawful Learning spatial triad;
- a non-abelian induced action on the active constraint set;
- a nontrivial `Z/2` loop class realizing the half-integer branch sign;
- a polarization-compatible encoding `E_phi` of the `A_1` singular germ into the active constraint complex.

Then `SO(3)`, with double cover `Spin(3)=SU(2)`, is the uniquely minimal object of `C_{A1}` for the half-integer `mu_2` bridge.

More concretely: any object in `C_{A1}` has triad image `SO(3)`; if the triad representation is faithful, the object is isomorphic to `SO(3)`. Additional group structure is redundant for the `A_1` sign bridge.

## 6. Proof plan

### Step 1: force the triad image

Show that a faithful orthogonal 3-dimensional action identifies `H` with a connected compact subgroup of `SO(3)`.

### Step 2: exclude abelian images

Show that connected proper compact subgroups of `SO(3)` are abelian circle-type subgroups. These cannot satisfy the non-abelian active-set action requirement.

### Step 3: recover `SO(3)`

Conclude that the triad image must be all of `SO(3)`. With faithful representation, `H ≅ SO(3)`.

### Step 4: attach the `mu_2` lift

Show that the nontrivial loop in `SO(3)` lifts through `Spin(3)=SU(2)` to a path ending at `-I`, realizing the `A_1` sign on the distinguished lifted eigendirection.

### Step 5: prove polarization compatibility

Use the pairing transported by `E_phi` to show that the identified eigendirection and action are fixed before execution, not selected after seeing the result.

## 7. Expected conclusion

If proved, the result does not prove P vs NP, Lawful Learning, or the proof-character program. It proves something narrower but important:

```text
for the half-integer singular-germ bridge, SO(3)/Spin(3) is not an arbitrary decorative gate choice; it is the minimal non-abelian compact-Lie realization compatible with the Lawful Learning spatial triad, polarization compatibility, and the A_1 sign monodromy.
```

That would close the canonicity gap for the first bridge instance.

## 8. Open risks

1. If the spatial-triad requirement is weakened, `SO(3)` will not be minimal.
2. If non-abelian active-set action is removed, abelian sign targets such as `U(1)` compete.
3. If polarization compatibility is too narrowly defined, the theorem becomes tautological.
4. The proof depends on the precise Lawful Learning gate geometry, so this theorem must be versioned against the committed gate model.

## 9. Required next artifact

The polarization compatibility condition is now specified separately in:

```text
docs/research/polarization-compatibility.md
```

The next artifact is a proof note for Steps 1–4 above, treating Step 5 as an assumption imported from the polarization compatibility document.
