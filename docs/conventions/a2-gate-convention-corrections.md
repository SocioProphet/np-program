# A2 Gate Convention Corrections

Status: convention-decision note / Track A1-to-A2 / not a theorem / not a Clay claim.

Related issue: #20.

This note records the corrected A2 gate-convention fork exposed by attempts to extend A1 gate minimality. It should be read before any A2 theorem-minimality statement, A2 promotion rule, or A_n unification claim.

## 0. Core correction

The A1 -> A_n extension is not a single theorem until the framework commits to what `V_A` means.

The A2 local cube-root harness can supply Stage-1 fixture evidence, but it does not decide the theorem-context carrier. Stage-2 must identify the active space, invariant, central datum, and categorical structure before any theorem statement is allowed.

## 1. Milnor number versus central order

For the singularity class `A_n`, the Milnor number is:

```text
mu(A_n) = n
```

Therefore:

```text
mu(A2) = 2
```

The number `n+1` is a different datum. It appears as:

```text
cyclic monodromy / character order = n + 1
ADE candidate defining-representation dimension = n + 1
center order of SU(n+1) = n + 1
```

For A2, this means:

```text
central order = 3
ADE candidate = SU(3)
defining representation dimension = 3
Milnor number = 2
```

Correct statement:

```text
dim V_A = 3 matches the defining representation of the ADE candidate SU(3)
and the central order n+1 = 3. If V_A is instead identified with the
vanishing-cycle space, then dim V_A = mu(A_n) = n, giving dimension 2 for A2.
This is the fork between the representation branch and the ADE branch.
```

## 2. Path alpha: SU2 representation branch

Path alpha keeps the A1 spatial/spin-frame carrier and lets the A_n distinction enter through representation dimension and Frobenius-Schur type.

Informally:

```text
carrier remains controlled by SU(2) / Spin(3)
central datum remains the A1-style Z/2 datum
V_A changes representation type
```

For A2, this means `SU(2)` acts through a higher-spin representation rather than through the A1 defining spinor representation.

Guardrail:

```text
If the spatial target remains faithful into Spin(3) = SU(2), then SO(3)
is not literally a subgroup of SU(2). SO(3) = PSU(2) re-enters only if
the target changes to SO(3), if the category admits projective
representations, or if a kernel/factor branch is explicitly declared.
```

Under this path, the theorem remains parsimonious but A2 is not distinguished at the group level. A2 distinctions live in the active representation and in the readout/polarization contract.

## 3. Path beta: SU3 ADE branch

Path beta identifies the active space with the ADE defining representation.

For A2:

```text
G_aux = SU(3)
V_A^(2) = C^3
zeta = omega I_3
omega = exp(2*pi*i/3)
central datum = Z/3 or mu_3
```

The invariant data for the defining representation are:

```text
H_A: Hermitian form
epsilon_A in Lambda^3 V_A^*: alternating determinant / volume form
```

Thus the A2 compatibility condition is Hermitian-volume compatibility, not A1 symplectic compatibility.

## 4. SU3 invariant correction

The defining representation `V = C^3` of `SU(3)` does not carry a totally symmetric cubic `d`-symbol invariant on `V^{tensor 3}`.

The symmetric tensor `d_{abc}` is an invariant on the adjoint representation of `SU(3)`, dimension 8.

Therefore:

```text
If V_A = C^3, use the Hermitian form and determinant / volume form.
If the framework requires the symmetric d-symbol, then V_A must be the
adjoint representation, and the active-space interpretation changes.
```

This correction blocks the invalid statement:

```text
SU(3) on C^3 is selected by a symmetric cubic d-symbol.
```

The corrected path-beta statement is:

```text
SU(3) on C^3 is selected by Hermitian structure plus the alternating
volume form epsilon in Lambda^3(C^3)^*.
```

## 5. SU3 subgroup-classification caution

A proof of SU3 minimality cannot use the phrase "the seven conjugacy classes" for closed connected subgroups of `SU(3)`.

Issue-level wording may say:

```text
representative proper connected subgroup types include U(1), T^2,
standard SU(2) acting on 2 + 1, irreducible SO(3) acting on C^3,
U(2), and related embeddings.
```

A theorem proof must specify the exact subgroup classification or embedding restrictions used.

In particular, the Step-2 elimination must address both:

```text
standard SU(2) subset SU(3) acting on 2 + 1
irreducible SO(3) subset SU(3) acting on C^3
```

The irreducible `SO(3)` embedding is nonabelian and preserves a real orthogonal structure. It is not eliminated merely by the nonabelian condition. Its exclusion, if required, must use the declared Hermitian-volume / central-order / active-space compatibility conditions.

## 6. Projective-obstruction change

The A1 faithful branch uses the projective-representation obstruction:

```text
H^2(SO(3); U(1)) = Z/2
```

resolved by auxiliary `Spin(3)` data.

Under path beta, the auxiliary candidate is `SU(3)`, which is simply connected. Therefore:

```text
H^2(SU(3); U(1)) = 0
```

There is no A1-style projective-representation obstruction at the `SU(3)` carrier level. The Step-4 proof structure must change. The A2 issue is not to lift a projective SO(3) action to Spin(3); it is to justify the chosen active-space convention, central `mu_3` datum, and Hermitian-volume invariant.

## 7. Required convention decision

Before an A2 theorem can be stated, the framework must answer:

1. Does `V_A^(2)` mean vanishing-cycle space, sheet/character readout space, or ADE defining representation?
2. Is the central datum inherited A1-style `Z/2`, or the A2 cyclic `Z/3` / `mu_3` datum?
3. Is the invariant symplectic, orthogonal, Hermitian, Hermitian-volume, doubled symplectic, or adjoint cubic?
4. Under the faithful branch, is the spatial group still `SO(3)` with auxiliary data, or does the auxiliary ADE group become the theorem carrier?
5. What exact subgroup-elimination theorem is being used if path beta asserts SU3 minimality?

## 8. Interaction with the existing A2 Stage-1 harness

The existing A2 local cube-root harness targets the pure local model:

```text
u^3 = t
```

with `C3 / mu3` monodromy and three-sheet character data.

That is compatible with path beta, but it does not prove path beta. It supplies local Stage-1 fixture evidence only.

Stage-2 must still attach the fixture to theorem-context data:

```text
V_A^(2)
Q_A^(2) or H_A / epsilon_A
E_phi^(2) as transport / encoding map
M_phi^(2)
M_A^(2)
central datum
categorical structure
subgroup elimination argument
```

## 9. Nonclaims

This note does not claim:

- A2 gate minimality;
- correctness of path alpha;
- correctness of path beta;
- promotion of any A2 fixture to theorem evidence;
- P = NP;
- P != NP;
- a lower bound;
- any Clay result.

It is a convention-control note: it prevents A2 from inheriting A1 claims before the active-space and invariant choices are declared.