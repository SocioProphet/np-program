# A2 Stage-2 Attestation Scaffold

Status: **Stage-2 attestation scaffold / theorem-context gate / not a theorem claim**.  
Depends on:

```text
docs/conventions/a2-target-split.md
docs/conventions/a2-local-cuberoot-normalization-v0.md
specs/a2-local-cuberoot-test-vectors.md
docs/proofs/c3-layer1-a2-group-identification.md
docs/proofs/c3-layer2-a2-polarization-candidates.md
```

Related issue:

```text
#16 — Implement A2 local cube-root Stage-1 harness
```

## 0. Purpose

A passing Stage-1 harness against `A2-local-cuberoot-normalization-v0` demonstrates that the fixture data satisfies the declared computational predicates.

It does not demonstrate that the fixture data correctly instantiates the theorem-context objects.

This note states what Stage 2 must additionally attest before any A2 result can be promoted beyond fixture-level evidence.

## 1. What Stage 1 establishes

A Stage-1 pass on the A2 local cube-root fixture establishes:

```text
1. The closed-form local cube-root fixture satisfies its declared predicate set.
2. The sheet-basis and character-basis matrices agree with the convention.
3. The additive jump vector matches the declared mu3 jump vector.
4. The pairing matrix is preserved by the declared character-basis monodromy.
5. The intertwining equation M_A^(2) E_phi^(2) = E_phi^(2) M_phi^(2) holds for the fixture.
6. Q-independent residual norms satisfy the declared tolerances.
7. Provenance fields bind the run to the convention, test vectors, and implementation hash.
```

Stage 1 is a consistency check on the fixture against the predicate set. It is not a theorem-context attestation.

## 2. What Stage 2 must attest

Stage 2 must attest that the fixture objects are the intended theorem-context data, or else explicitly declare which objects remain open.

The fixture data currently has the form:

```text
H_phi^(2) = C e_0 ⊕ C e_1 ⊕ C e_2
V_A^(2)   = C v_0 ⊕ C v_1 ⊕ C v_2
E_phi^(2)(e_j) = v_j
M_phi^(2) = diag(1, omega, omega^2)
M_A^(2)   = diag(1, omega, omega^2)
Q(v_i, v_j) = 1 if i + j ≡ 0 mod 3, else 0.
```

Stage 2 must decide whether this is merely a reference fixture or the actual theorem-context object.

## 3. Object-by-object attestation requirements

### 3.1 `V_A^(2)`

Stage 1 tests a fixture active space:

```text
V_A^(2) = C^3.
```

Stage 2 must attest:

```text
1. that C^3 is the intended A2 auxiliary active space for the theorem context; or
2. that C^3 is only a local fixture space, with a different global V_A^(2) still open.
```

The attestation must specify whether the dimension and representation are inherited from the `mu3` character decomposition, from an A2 root-system construction, from an auxiliary group representation, or from another declared source.

It must also state that the auxiliary structure is not automatically the universal cover of a spatial group. The A1 faithful proof's warning remains active: higher `A_k` auxiliary groups must be derived from their own polarization data.

### 3.2 `Q_A^(2)`

Stage 1 tests the fixture pairing:

```text
Q = [[1, 0, 0],
     [0, 0, 1],
     [0, 1, 0]].
```

This is the conjugate-character pairing. It is nondegenerate but not positive-definite.

Stage 2 must attest:

```text
1. that this is the intended bilinear form for the A2 theorem context; or
2. that it is only a local fixture pairing and the theorem-context pairing remains open.
```

The attestation must name the form type:

```text
symmetric bilinear | Hermitian | symplectic | Cartan/Killing-derived | other declared form
```

and must state how it is compatible with the selected A2 auxiliary group or monodromy structure.

Stage 2 must also preserve the Q-independent norm rule for numerical residuals. Numerical norm policy is not a theorem-context form choice.

### 3.3 `E_phi^(2)`

`E_phi^(2)` is an encoding / transport map, not an energy functional.

Stage 1 tests the fixture map:

```text
E_phi^(2)(e_j) = v_j.
```

Stage 2 must attest:

```text
1. that this is the intended A2 transport map from source sheet/character data to active data; or
2. that it is only a local fixture identification and the theorem-context transport map remains open.
```

The attestation must address:

```text
- predeclaration before harness execution;
- nondegeneracy of the transported source channels;
- filtration preservation or the A2 analog of filtration preservation;
- no post-hoc sheet or character selection;
- compatibility with the selected pairing and monodromy.
```

### 3.4 `M_phi^(2)`

Stage 1 tests the source monodromy fixture:

```text
M_phi^(2) = diag(1, omega, omega^2)
```

in the declared character basis.

Stage 2 must attest:

```text
1. that this is the correct source monodromy for the A2 theorem context; or
2. that it is only the local cube-root source monodromy and the theorem-context monodromy remains open.
```

The attestation must distinguish genuine monodromy from coordinate artifact. It must state which singularity or loop is being encircled and in which representation the monodromy acts.

It must also state the barrier-registry relationship: whether this monodromy is intended to supply non-algebrizing structure, or whether no such transfer claim is being made.

### 3.5 `M_A^(2)`

Stage 1 tests the active monodromy fixture:

```text
M_A^(2) = diag(1, omega, omega^2).
```

Stage 2 must attest:

```text
1. that this is the intended active-side monodromy / gate action for the A2 theorem context; or
2. that it is only a fixture matrix and the active theorem-context action remains open.
```

The attestation must specify the ambient moduli or representation context in which `M_A^(2)` lives.

If the local cube-root normalization is a local trivialization of a global object, Stage 2 must state the transition data or explicitly mark it as open.

## 4. Attestation gap table

| Object | Stage 1 tests | Stage 2 must close |
|---|---|---|
| `V_A^(2)` | Fixture active space `C^3` and numerical properties | Correct auxiliary active space for A2 or open design decision |
| `Q_A^(2)` | Preservation under fixture monodromy | Correct form type for A2 theorem context; not conflated with Euclidean norm |
| `E_phi^(2)` | Fixture transport `e_j -> v_j` and intertwining | Correct A2 transport map, nondegeneracy, filtration/no-mixing preservation |
| `M_phi^(2)` | `mu3` eigenvalue/source-monodromy structure | Real theorem-context monodromy, not coordinate artifact |
| `M_A^(2)` | Active fixture matrix | Correct active/gate/moduli object with stated local-to-global meaning |

## 5. Auxiliary-group design decision

Stage 2 cannot be complete without either committing to an A2 auxiliary group or explicitly marking the auxiliary group as open.

A1 faithful branch:

```text
auxiliary group = Spin(3) = SU(2)
V_A = C^2
Q_A = epsilon^{ab}
```

A2 candidates include, but are not limited to:

```text
1. SU(2) again, acting on a higher-dimensional representation such as a spin-1 C^3 space.
2. SU(3), acting on V_A^(2) = C^3 via the fundamental representation.
3. C3 / mu3, acting as the local character group on the fixture.
4. S3 / Weyl group, if a principled full sheet-permutation or root-reflection reattachment is supplied.
5. No Stage-2 obstruction analog, leaving only Stage-1 local normalization evidence.
```

This decision determines:

```text
- the dimension and representation of V_A^(2);
- the form type for Q_A^(2);
- the meaning of auxiliary structure at A2;
- whether Candidate A is theorem-context data or only a fixture.
```

## 6. Relationship to Stage-1 fixture

`A2-local-cuberoot-normalization-v0` is correctly scoped as a local model.

Stage 2 is a companion attestation, not a replacement for the fixture.

```text
Stage 1 answers: does the local computational fixture pass its declared checks?
Stage 2 answers: is this local fixture the intended theorem-context data?
```

Both are required before A2 results can enter a claim ledger as more than fixture evidence.

## 7. Nonclaims

This Stage-2 scaffold does not claim:

```text
- the A2 theorem is true;
- the local cube-root fixture is canonical;
- the local cube-root fixture uniquely represents A2;
- the fixture extends to A2 singularities in larger algebraic-geometric contexts;
- the auxiliary group for A2 is known;
- V_A^(2) must be C^3 in the final theorem context;
- Q_A^(2) must be the fixture pairing in the final theorem context;
- Candidate A survives at higher A_n;
- any I-12 template promotion;
- P vs NP or any Clay result.
```

It defines the attestation gate required after the Stage-1 harness passes.

## 8. Required next issue

If Stage-1 harness implementation succeeds, open a follow-up issue:

```text
Draft A2 Stage-2 theorem-context attestation
```

That issue must choose one of:

```text
1. commit to a theorem-context V_A^(2), Q_A^(2), E_phi^(2), M_phi^(2), M_A^(2);
2. mark one or more objects as open and keep A2 at Stage 1;
3. select Candidate D and explicitly state that no Stage-2 obstruction analog is claimed.
```
