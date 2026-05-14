# V4 / GF(4) MOLS Readout-Basis Foundation

Status: **structural guardrail / theorem-input doctrine / not a Clay claim**.  
Scope: Track A1, Catalan `mu_2`, polarization compatibility, and future A2/A3 symmetry extensions.

## 0. Purpose

This note records the algebraic correction surfaced by the cipher / Latin-square experiment:

```text
involution + selectivity + balance + composability
```

are not supplied by an arbitrary sign flip. They are supplied, at order four, by the Klein four-group

```text
V4 = Z/2 x Z/2
```

and by the finite-field orthogonal Latin-square construction over `GF(4)`, not by the cyclic group `Z/4`.

This is a guardrail. It prevents the A1 `mu_2` sign fixture from being silently inflated into a full order-four symmetry statement, and it prevents false cyclic-center reasoning from propagating into Track A2 or Track A3.

## 1. Correct order-four structure

The correct order-four object is the elementary abelian group:

```text
V4 = {0, 1, a, b}
```

with every nonzero element self-inverse. In the `GF(4)` model, the elements may be represented as

```text
0, 1, alpha, alpha + 1
```

with relation

```text
alpha^2 = alpha + 1.
```

The additive group of `GF(4)` is `V4`. This is the structure that supplies coordinate-wise involutions while preserving a balanced Latin-square action.

## 2. Why `Z/4` is rejected

The cyclic group `Z/4` has elements of order four. It is not an all-involutive sign-flip group.

Its Cayley table is a Latin square, but the cyclic order-four table does not provide the required orthogonal mate. Equivalently, cyclic Latin squares of even order have no orthogonal mate. Therefore `Z/4` fails the readout-basis requirement for the order-four symmetry lane.

This rejection is load-bearing. A fixture or proof note that treats the cyclic `Z/4` table as the mate for the required order-four orthogonal structure must fail.

## 3. GF(4) MOLS construction

For a finite field `F = GF(4)`, the standard affine construction gives mutually orthogonal Latin squares:

```text
L_m(x, y) = m x + y
```

for distinct slopes `m` in `F`.

A concrete pair used by the fixture is:

```text
L_1(x, y) = x + y
L_alpha(x, y) = alpha x + y
```

The ordered pairs

```text
(L_1(x, y), L_alpha(x, y))
```

are all distinct as `(x, y)` ranges over `GF(4)^2`. This gives the required sixteen cells with sixteen distinct paired symbols.

## 4. Relation to the Catalan `mu_2` fixture

The Catalan / square-root fixture detects a single `Z/2` sign channel:

```text
sqrt(t) -> -sqrt(t)
```

That is the A1 `mu_2` datum. It is necessary, but it is not the full `V4` datum.

The A1 fixture therefore answers only:

```text
is there a declared sign-line involution?
```

It does not answer:

```text
which copy of Z/2 inside V4 is active?
```

and it does not answer:

```text
does the full GF(4) orthogonal readout structure exist?
```

Those are Track A2/A3 questions unless explicitly pulled into a new A1 refinement.

## 5. Coordinate basis versus readout basis

A coordinate-basis involution flips a direction. A readout-basis involution flips the direction that the declared observable actually reads.

The cipher experiment showed the practical failure mode: sign flips can be reversible and balanced while still spraying energy across the wrong coordinates. The mathematical guardrail is the same here. A sign action is admissible only after the basis, pairing, filtration, and readout direction have been declared before evaluation.

For this repository, the readout-basis requirements are:

```text
1. declare the source sign line or V4 channel before evaluation;
2. declare the active basis before evaluating monodromy or gate action;
3. declare the transport map E_phi before observing eigenspaces;
4. check pairing preservation;
5. check filtration preservation;
6. reject post-hoc rotations into a successful sign direction.
```

## 6. Barrier posture

This note does not clear relativization, natural-proofs, algebrization, proof-complexity-transfer, or average-case-transfer barriers. It is a structural correction inside the theorem-input lane.

The permitted claim is:

```text
The correct order-four readout-basis object for the current sign-flip doctrine is V4 / GF(4)-MOLS, not cyclic Z/4.
```

The forbidden claims are:

```text
- that this proves a lower bound;
- that this moves P vs NP;
- that the A1 mu_2 fixture identifies a full V4 action;
- that Z/4 can be substituted for GF(4) without changing the doctrine;
- that a coordinate-basis sign flip is already selective.
```

## 7. Implementation hooks

The paired fixtures are:

```text
tests/fixtures/gf4-v4-mols.json
tests/fixtures/invalid-z4-mols.json
```

The valid fixture records the GF(4) field table and the orthogonal pair `L_1`, `L_alpha`. The invalid fixture records the cyclic `Z/4` rejection case.

Future validators should assert:

```text
valid fixture:   16 distinct ordered pairs
invalid fixture: not an admissible MOLS witness
```

## 8. Nonclaims

This note is not a proof of P vs NP, not a proof-complexity lower bound, not a GCT obstruction, and not evidence of Clay-problem progress.

It is a finite algebraic discipline layer: involution alone is not selectivity; the readout basis is the load-bearing object.