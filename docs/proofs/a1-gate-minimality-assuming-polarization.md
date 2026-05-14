# A1 Gate Minimality Assuming Polarization Compatibility

Status: **theorem-input bridge lemma / Track A1 / not a Clay claim**.  
Depends on: `docs/foundations/polarization.md`, `docs/proofs/a1-gate-minimality-faithful.md`, `specs/catalan-mu2-reference-implementation.md`.  
Purpose: isolate the exact contract that the gate-minimality proof may consume from polarization compatibility before any A2/Fuss-Catalan extension is attempted.

## 0. Why this note exists

The A1 gate-minimality proof should not silently assume that a sign line found in computation is the correct readout direction. That is the role of polarization compatibility.

This note states the bridge lemma:

```text
If the A1 source sign line is transported into the active vector space by a predeclared polarization-compatible map, then the gate-minimality theorem may treat the resulting -1 eigendirection as a legitimate readout direction rather than as a post-hoc coordinate-basis sign flip.
```

It does not reprove polarization compatibility. It assumes the contract defined in `docs/foundations/polarization.md` and records what follows for A1 gate minimality.

## 1. Input data

Assume an A1 source package:

```text
S_phi = (H_phi_bridge, L_phi, M_phi, Q_phi, conventions_phi)
```

with:

```text
H_phi_bridge = L_phi
rank(L_phi) = 1
M_phi|L_phi = [-1]
Q_phi(e, e) != 0
```

for a chosen nonzero source-basis vector `e`.

Assume active-side data:

```text
A = (V_A, Q_A, W_A, G, rho_spatial, S, gamma)
```

where, under the faithful branch `T2'`:

```text
G = SO(3)
rho_spatial: G -> SO(3) is faithful
S is an auxiliary Spin(3)-structure on V_A
sigma: Spin(3) -> Sp(V_A, Q_A)
gamma in pi_1(SO(3)) = Z/2
```

Let `gamma_tilde` be the lifted path in `Spin(3)` with endpoint `gamma_tilde(1)`.

## 2. Polarization compatibility assumption

Assume a predeclared encoding map:

```text
E_phi: L_phi -> V_A
```

satisfying the A1 polarization contract:

```text
1. E_phi is declared before monodromy or gate evaluation.
2. E_phi is injective on L_phi.
3. E_phi maps the A1 source monodromy eigendirection to the active spin eigendirection.
4. E_phi respects the declared filtration.
5. E_phi preserves the pairing:
   E^T G_active E = G_phi
   or the Hermitian variant when applicable.
6. The active spin action preserves Q_A.
```

Under `T2'`, the active sign action is:

```text
M_A = sigma(gamma_tilde(1)).
```

The monodromy-compatibility equation is:

```text
M_A E_phi = E_phi M_phi.
```

For the A1 sign line this reduces to:

```text
sigma(gamma_tilde(1)) E_phi(e) = -E_phi(e).
```

## 3. Lemma: polarization turns sign compatibility into readout compatibility

### Lemma A1-POL-MIN-001

If the assumptions in Sections 1 and 2 hold, then the active `-1` eigendirection used by the A1 gate-minimality theorem is a readout-compatible direction, not a post-selected coordinate-basis sign direction.

### Proof

Because `E_phi` is declared before gate evaluation, the active vector

```text
v_minus = E_phi(e)
```

is fixed independently of the observed eigenspace decomposition of any later gate computation.

Because `E_phi` is injective and `Q_phi(e,e) != 0`, the transported vector is nonzero and nondegenerate with respect to the transported pairing:

```text
Q_A(v_minus, v_minus) = Q_phi(e,e) != 0.
```

Because the monodromy-compatibility equation holds,

```text
sigma(gamma_tilde(1)) v_minus = -v_minus.
```

Therefore the `-1` action occurs on the predeclared transported source sign line, not on a sign direction chosen after observing the active representation.

Because `sigma` preserves `Q_A`, the sign action is compatible with the active polarization rather than a stray or external sign. Because filtration preservation is assumed, the sign line has not been moved across undeclared complexity or activity levels.

Thus the active `-1` eigendirection is a legitimate readout direction for the A1 gate-minimality theorem under the declared polarization contract. This proves the lemma.

## 4. Consequence for A1 gate minimality

The faithful A1 theorem `T2'` may use the following object as admissible input:

```text
v_minus = E_phi(e)
M_A v_minus = -v_minus
Q_A(v_minus, v_minus) = Q_phi(e,e) != 0
```

with the interpretation:

```text
M_A = sigma(gamma_tilde(1))
```

and not:

```text
M_A is an element of G = SO(3).
```

Therefore, the Catalan harness predicate

```text
zeta = -I
```

is admissible for `T2'` only when read as:

```text
zeta = sigma(gamma_tilde(1)) = -I on V_A.
```

## 5. Failure modes blocked by the lemma

### 5.1 Post-hoc eigendirection selection

Failure:

```text
Observe a -1 eigenspace first, then define E_phi to land there.
```

Blocked because `E_phi` must be declared before evaluation.

### 5.2 Coordinate-basis sign flip without readout alignment

Failure:

```text
A sign flip exists somewhere in V_A, so the A1 semantics are realized.
```

Blocked because the sign must occur on `E_phi(L_phi)`, the transported source sign line.

### 5.3 Stray central sign

Failure:

```text
A separate U(1) or scalar factor supplies -I.
```

Blocked because the sign must arise as `sigma(gamma_tilde(1))`, the auxiliary spin lift of the distinguished `SO(3)` loop.

### 5.4 Pairing collapse

Failure:

```text
The source sign line maps to a null or degenerate active direction.
```

Blocked because pairing transport requires `Q_A(E_phi(e), E_phi(e)) = Q_phi(e,e) != 0`.

### 5.5 Filtration drift

Failure:

```text
The sign line is moved into an undeclared active level.
```

Blocked because filtration preservation is part of the polarization contract.

## 6. Relation to the coordinate/readout-basis KB pattern

The canonical cross-repo pattern is:

```text
SocioProphet/systems-learning-loops/kb/patterns/coordinate-basis-vs-readout-basis-involution.md
```

This lemma is the A1 local implementation of that guardrail:

```text
involution alone is not selectivity;
polarization-compatible transport supplies the readout-basis condition for A1.
```

The lemma does not claim that the same construction works for `A2` or higher `A_k`. It only states what A1 gate minimality may consume once the A1 polarization contract is satisfied.

## 7. Relation to A2 / Fuss-Catalan work

This note is logically prior to the A2 harness.

The A2 harness may test dimensional, branch, Stokes, and sheet-structure data, but those outputs are not enough to inherit the A1 gate-minimality status. A2 requires its own data:

```text
V_A^(2)
Q_A^(2)
monodromy^(2)
polarization^(2)
readout map E_phi^(2)
central/obstruction class attachment
```

The A2/Fuss-Catalan harness is therefore Stage 1 unless it also supplies the Stage 2 cohomological/polarization attachment required by C-3' and its higher-Ak generalization.

## 8. Nonclaims

This note does not claim:

- P = NP;
- P != NP;
- a circuit lower bound;
- a proof-complexity lower bound;
- that the Catalan harness proves the Track A transfer theorem;
- that A2 inherits A1 gate minimality;
- that every `mu_p` sign or root-of-unity channel has a readout-basis realization;
- that the Part B cipher experiment proves anything about proof complexity.

It is a narrow bridge lemma: assuming A1 polarization compatibility, the A1 gate-minimality proof may treat the transported sign line as a legitimate readout direction.