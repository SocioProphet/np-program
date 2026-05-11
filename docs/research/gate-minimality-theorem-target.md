# Gate Minimality Theorem Target

Status: **theorem target / not established**.

This note records the first concrete theorem target created by the singular-germ enrichment. Its purpose is to close the canonicity gap for the `mu_2` bridge in the half-integer / square-root case.

## 1. The canonicity gap

The `A_1` / square-root singularity naturally produces a two-sheeted branch system and a sign monodromy. This supports the `mu_2` bridge:

```text
singular monodromy -> chi_2 sign -> topological torsion sign -> gate-loop sign
```

However, the gate realization is not yet canonical. A sign can be represented in many groups. Without an additional minimality or universality principle, choosing `SO(3)` may be compatible but not forced.

## 2. Why the naive statement is false

The statement “`SO(3)` is minimal for representing a sign” is false. A sign is already representable in smaller structures, for example through `U(1)` using `-1`.

Therefore the theorem must include the geometry that makes `SO(3)` meaningful for the Lawful Learning framework.

The admissible target is not merely a group carrying `Z/2`; it is a compact-Lie gate factor that:

1. acts on the spatial triad used by the Lawful Learning geometry;
2. admits a nontrivial double-cover lift with central sign;
3. supports a faithful equivariant action on the distinguished `A_1` monodromy eigendirection;
4. composes with the existing torus phase gates `T^k`;
5. preserves the constraint-complex polarization required by the encoding map `E_phi`.

## 3. Candidate theorem statement

### Gate minimality conjecture, half-integer case

Let `C` be the category of compact connected Lie gate factors `H` equipped with:

- a faithful real representation `rho: H -> SO(3)` on the Lawful Learning spatial triad;
- a connected double cover `\tilde H -> H` whose kernel contains a central element acting as `-1` on the distinguished lifted eigendirection;
- an equivariant action on the `A_1` Milnor cohomology sign representation, compatible with `E_phi`.

Then `SO(3)`, with double cover `Spin(3) = SU(2)`, is terminal-minimal in `C` among non-abelian compact connected Lie gate factors realizing the half-integer monodromy sign.

## 4. What must be proved

The proof should split into four checks.

### Check 1: representation admissibility

Show that the spatial-triad requirement forces the target representation to land in or factor through `SO(3)`.

### Check 2: double-cover sign

Show that the nontrivial loop in `SO(3)` lifts to a path in `Spin(3)` ending at the nontrivial central element `-I`, and that this central element realizes the `A_1` sign on the distinguished eigendirection.

### Check 3: exclusion of abelian-only targets

Show that `U(1)` or finite cyclic targets can represent the sign but fail the full admissibility package: spatial-triad action, non-abelian active-set action, and Lawful Learning polarization compatibility.

### Check 4: minimality inside the admissible class

Show that any admissible compact connected non-abelian gate factor for the spatial triad either factors through `SO(3)` or contains redundant structure relative to the `A_1` sign realization.

## 5. Expected conclusion

If proved, the result does not prove P vs NP, Lawful Learning, or the proof-character program. It proves something narrower but important:

```text
for the half-integer singular-germ bridge, SO(3)/Spin(3) is not an arbitrary decorative gate choice; it is the minimal non-abelian compact-Lie realization compatible with the Lawful Learning spatial triad and the A_1 sign monodromy.
```

That would close the canonicity gap for the first bridge instance.

## 6. Open risks

1. The admissible category `C` may be too narrowly defined and therefore theorem becomes tautological.
2. If the spatial-triad requirement is weakened, `SO(3)` will not be minimal.
3. If the active-set action does not require non-abelian structure, abelian sign targets compete.
4. The proof depends on the precise Lawful Learning geometry, so this theorem must be versioned against the committed gate model.

## 7. Required next artifact

A formal version of `C` with objects, morphisms, and admissibility constraints. This should be written before any proof attempt.
