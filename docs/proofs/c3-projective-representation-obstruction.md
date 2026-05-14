# C-3' Projective-Representation Obstruction

Status: proof-boundary note / Track A1 / not a Clay claim.

Related issue: #7.

This note records the cohomological obstruction behind the faithful A1 branch. It separates three objects that must not be conflated:

1. the projective-representation obstruction for `SO(3)`;
2. the A1-specific resolution by auxiliary `Spin(3)` data on `V_A`;
3. the higher `A_k` question of how, or whether, an analogous obstruction attaches to the new active space, pairing, monodromy, and central data.

## 1. The obstruction class

For the faithful A1 branch, the spatial group is:

```text
G = SO(3)
```

and the active two-dimensional complex symplectic action is not an ordinary faithful representation of `SO(3)` on `V_A = C^2`.

Instead, it is a projective representation of `SO(3)` whose linear lift is supplied by:

```text
Spin(3) = SU(2) -> SL(2, C) = Sp(C^2, epsilon)
```

The obstruction to lifting the projective representation to an honest linear representation of `SO(3)` is the nontrivial class:

```text
H^2(SO(3); U(1)) = Z/2
```

Equivalently, the nontrivial central extension is:

```text
1 -> Z/2 -> Spin(3) -> SO(3) -> 1
```

The nontrivial loop in:

```text
pi_1(SO(3)) = Z/2
```

lifts to a path in `Spin(3)` whose endpoint is the central element:

```text
-I in Spin(3) = SU(2)
```

This is the cohomological source of the faithful-branch `zeta = -I` predicate.

## 2. How the A1 faithful branch resolves the obstruction

The faithful branch `T2'` does not put `-I` inside the spatial group `G = SO(3)`.

Instead, it uses auxiliary spin data:

```text
sigma: Spin(3) -> Sp(V_A, Q_A)
```

and interprets the sign predicate as:

```text
zeta = sigma(gamma_tilde(1)) = -I on V_A
```

where `gamma_tilde` is the lift of the nontrivial loop class in `SO(3)` to `Spin(3)`.

Thus the obstruction is resolved by passing from projective `SO(3)` action to linear auxiliary `Spin(3)` action on the active space.

This is precisely why the faithful branch says:

```text
-I lives in auxiliary Spin(3), not in G = SO(3).
```

## 3. What the obstruction does and does not prove

The calculation:

```text
H^2(SO(3); U(1)) = Z/2
```

proves that projective representations of `SO(3)` carry a `Z/2` central-extension obstruction.

It does not prove that every future `A_k` active space has an inherited `Z/2` obstruction.

It also does not prove that the auxiliary group for `A_k` is the universal cover of the spatial group. In A1, `Spin(3)` is both the universal cover of `SO(3)` and the auxiliary carrier of the active spinor data. That coincidence is A1-specific and must not be generalized mechanically.

## 4. Separation from A2 and higher Ak

For A2 and higher cases, the framework must rederive the relevant data from the active-space convention.

Required inputs include:

```text
V_A^(k)
Q_A^(k) or replacement invariant data
E_phi^(k) as transport / encoding map
M_phi^(k)
M_A^(k)
central datum
monodromy / character datum
categorical structure
```

For the A2 ADE branch described in Issue #20, the candidate auxiliary carrier is:

```text
SU(3)
```

with:

```text
V_A^(2) = C^3
zeta = omega I_3, omega = exp(2*pi*i/3)
invariant data = Hermitian form + determinant / volume form
```

That path does not inherit the A1 obstruction, because:

```text
H^2(SU(3); U(1)) = 0
```

at the simply connected `SU(3)` carrier level.

Therefore A2 path beta has a different Step-4 problem. It is not an A1-style projective lift from `SO(3)` to `Spin(3)`. It is a convention and invariant-selection problem for the ADE active carrier.

## 5. Failure modes blocked by C-3'

### 5.1 Treating `zeta = -I` as an element of `SO(3)`

Blocked statement:

```text
zeta = -I in G = SO(3)
```

Correct statement:

```text
zeta = sigma(gamma_tilde(1)) = -I on V_A
```

### 5.2 Mechanically inheriting A1 obstruction data in A2

Blocked statement:

```text
A2 inherits the A1 Z/2 projective obstruction.
```

Correct statement:

```text
A2 must specify its active carrier, invariant, and central datum before any
obstruction statement is meaningful.
```

### 5.3 Treating universal covers as theorem data by default

Blocked statement:

```text
the auxiliary group for Ak is automatically the universal cover of the spatial group.
```

Correct statement:

```text
the auxiliary group is determined by the declared active-space and polarization data.
```

## 6. Relation to the existing documents

This note supports:

- `docs/proofs/a1-gate-minimality-faithful.md`
- `docs/proofs/a1-gate-minimality-assuming-polarization.md`
- `docs/proofs/a1-gate-minimality-v3-amendments.md`
- `docs/conventions/a2-gate-convention-corrections.md`

It closes the specific gap named as C-3' in the faithful A1 branch: the obstruction is now stated cohomologically and separated from A2/higher-Ak generalization.

## 7. Nonclaims

This note does not claim:

- A2 gate minimality;
- any higher `A_k` theorem;
- a P vs NP result;
- a circuit lower bound;
- a proof-complexity lower bound;
- any Clay result.

It only records the A1 faithful-branch projective-representation obstruction and prevents accidental inheritance into A2/higher branches.