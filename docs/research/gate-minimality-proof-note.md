# Gate Minimality Proof Note for the A1 / mu2 Bridge

Status: **Track A2 proof note / conditional theorem / not a Clay claim**.  
Depends on: `docs/foundations/polarization.md`, `docs/research/gate-minimality-theorem-target.md`, `docs/barriers/README.md`.

## 0. Purpose

This note proves the Lie-theoretic core of the `A1` / `mu2` gate-minimality target under the assumptions already declared in the repository.

The result is intentionally narrow. It says that once the Lawful Learning spatial triad, non-abelian active-set action, compact connected Lie regularity, nontrivial `Z/2` loop class, and polarization-compatible encoding are all required, the minimal gate image for the half-integer sign bridge is `SO(3)`, with `Spin(3)=SU(2)` supplying the double-cover lift.

It does not prove P vs NP, does not prove a circuit lower bound, and does not prove a proof-system lower bound.

## 1. Definitions

### 1.1 A1 bridge datum

An `A1` bridge datum consists of:

```text
D_A1 = (L_phi, Q_phi, T_phi, V_A, Q_A, E_phi, G, rho, gamma)
```

where:

- `L_phi` is the one-dimensional source sign line of the `A1` branch system;
- `Q_phi` is a declared nonzero source pairing on `L_phi`;
- `T_phi|L_phi = -1` is the source monodromy;
- `V_A` is the active constraint vector space;
- `Q_A` is the active-side pairing transported from `Q_phi`;
- `E_phi: L_phi -> V_A` is declared before execution and is injective;
- `G` is a compact connected Lie gate factor;
- `rho: G -> GL(V_A)` is the active representation;
- `gamma` is a declared loop or path realizing the active monodromy.

The polarization rules are imported from `docs/foundations/polarization.md`.

### 1.2 Admissible A1 gate object

An admissible `A1` gate object is a tuple:

```text
(G, rho_tri, rho_A, gamma, E_phi, Q_A)
```

satisfying:

1. `G` is compact, connected, and Lie.
2. `rho_tri: G -> SO(3)` is a faithful orthogonal real three-dimensional representation on the spatial triad.
3. The induced active-set action is non-abelian.
4. The loop class of `gamma` realizes the required `Z/2` sign for the half-integer branch.
5. `E_phi` is polarization-compatible and filtration-compatible in the sense of `docs/foundations/polarization.md`.

The faithful triad representation is part of the admissibility class. If faithfulness is removed, finite covers or redundant central factors can appear and uniqueness must be stated only at the level of triad image.

## 2. Theorem

### Gate minimality theorem, A1 conditional form

Let `(G, rho_tri, rho_A, gamma, E_phi, Q_A)` be an admissible `A1` gate object.

Then the triad image `rho_tri(G)` is `SO(3)`. If `rho_tri` is faithful, then `G` is isomorphic to `SO(3)`.

Moreover, the nontrivial loop class in `SO(3)` lifts through:

```text
Spin(3)=SU(2) -> SO(3)
```

to a path beginning at `I` and ending at `-I`, realizing the `A1` sign on the transported source line `E_phi(L_phi)`.

Therefore `SO(3)`, with `Spin(3)=SU(2)` as its double cover, is the minimal non-abelian compact connected triad gate realization compatible with the `A1` sign bridge and the declared polarization transport.

## 3. Proof

### Step 1 — triad image is a connected compact subgroup of SO(3)

By assumption, `rho_tri` is an orthogonal real three-dimensional representation. Thus its image lies in `O(3)`. The admissibility condition specifies orientation-preserving spatial-triad gate motion, so the image lies in `SO(3)`.

Because `G` is compact and connected and `rho_tri` is continuous, `rho_tri(G)` is a compact connected Lie subgroup of `SO(3)`.

If `rho_tri` is faithful, then `G` is isomorphic to its image as a compact connected Lie group.

### Step 2 — connected proper compact subgroups relevant to SO(3) are abelian circle-type groups

A connected Lie subgroup of `SO(3)` has Lie algebra a Lie subalgebra of `so(3)`. The Lie algebra `so(3)` is three-dimensional and simple. Its proper nonzero Lie subalgebras are one-dimensional rotation-axis subalgebras. A one-dimensional connected compact Lie group is circle-type and abelian.

Therefore a connected proper positive-dimensional subgroup of `SO(3)` is conjugate to an `SO(2)` rotation subgroup and is abelian. The trivial subgroup is also abelian.

### Step 3 — non-abelian active-set action forces full SO(3) image

The admissibility class excludes abelian active-set action. If the triad image were a proper connected subgroup of `SO(3)`, Step 2 would make it abelian. Such an image cannot supply the required non-abelian active-set behavior through the faithful spatial-triad gate factor.

Hence the triad image cannot be proper. It follows that:

```text
rho_tri(G) = SO(3)
```

If `rho_tri` is faithful, then:

```text
G ≅ SO(3)
```

This proves the minimal Lie-theoretic gate image.

### Step 4 — the Z/2 loop lifts through Spin(3)

The universal double cover of `SO(3)` is:

```text
Spin(3)=SU(2) -> SO(3)
```

The fundamental group of `SO(3)` is `Z/2`. The nontrivial loop class in `SO(3)` lifts to a path in `SU(2)` beginning at `I` and ending at the nontrivial central element `-I`.

For the `A1` bridge, this endpoint acts as the sign on the lifted half-integer line. Thus the lifted path realizes the same `mu2` sign as the source monodromy:

```text
T_phi|L_phi = -1
```

### Step 5 — polarization prevents post-selection of the sign direction

The preceding steps show that `SO(3)` is forced as the minimal non-abelian compact connected triad image, but sign realization alone is not enough. Abelian targets can also display a sign.

The polarization foundation supplies the missing canonicity condition. The encoding map:

```text
E_phi: L_phi -> V_A
```

is declared before execution, is injective, transports the source pairing, and satisfies:

```text
Q_A(E_phi(u), E_phi(v)) = Q_phi(u,v)
```

The active monodromy must commute with source monodromy under this encoding:

```text
M_A E_phi = E_phi M_phi
```

and must preserve the active pairing:

```text
M_A^T G_A M_A = G_A
```

Therefore the sign eigendirection is not selected after seeing which gate direction carries eigenvalue `-1`. It is fixed by the transported source line and pairing.

This proves the conditional theorem.

## 4. Minimality interpretation

The theorem proves minimality in the declared admissibility class, not absolute minimality among all groups carrying a sign.

The following competitors are excluded only because of declared admissibility conditions:

- `U(1)` / `SO(2)` can realize a sign-like phase but is abelian, so it fails the non-abelian active-set condition.
- A disconnected finite group can carry a sign but fails compact connected Lie regularity.
- A larger compact connected group can map onto `SO(3)` but contains redundant structure for the triad image.
- A non-faithful cover can realize the same triad image but is not minimal as a faithful triad gate object.

Thus the precise conclusion is:

```text
SO(3) is the minimal faithful non-abelian compact connected spatial-triad gate image for the A1 sign bridge under polarization compatibility.
```

## 5. Barrier posture

This proof is Lie-theoretic and local to the `A1` gate realization. It is not a lower-bound proof.

Barrier registry status:

```yaml
claim_id: GATE-MINIMALITY-001
relativization: not_applicable
natural_proofs: not_applicable
algebrization: not_applicable
proof_complexity_transfer: not_applicable
average_case_transfer: not_applicable
```

If this theorem is later used as part of a proof-complexity, GCT, or meta-complexity claim, the later claim must receive its own barrier entry. This proof does not transfer complexity-theoretic content by itself.

## 6. What remains open

1. The Catalan `mu2` fixture must be hardened so the replay ledger computes matrix products rather than relying on zero-valued placeholders.
2. Failure fixtures must reject post-selected eigendirections, missing pairings, wrong monodromy sign, wrong Stokes normalization, and nondeterministic digests.
3. Track B must determine whether any preserved pairing or filtration maps to proof size, formula depth, width, simulation cost, substitution cost, orbit-closure obstruction data, or another recognized complexity-theoretic invariant.

## 7. Nonclaims

This note does not claim:

- P = NP;
- P != NP;
- NP != coNP;
- a circuit lower bound;
- a proof-system lower bound;
- a GCT obstruction;
- that singular-germ invariants transfer to proof complexity;
- that algebrization is escaped;
- that `SO(3)` is forced without the spatial-triad, non-abelian active-set, compact-connected, `Z/2`, and polarization assumptions.
