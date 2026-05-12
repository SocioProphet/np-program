# Clay-Track Program Structure

Status: **roadmap / barrier-aware / no Clay claim**.  
Date: 2026-05-12.  
Scope: P vs NP adjacency for the `np-program` repository.

## 0. Direct framing

The program is currently a **candidate invariant grammar** with one bridge instance, the `mu_2` / Catalan / `A_1` case, approaching theorem-grade discipline. The standard Clay P vs NP problem is a statement about uniform deterministic Turing machines, nondeterministic polynomial-time verification, and polynomial-time decidability of NP-complete languages. This repository does not currently contain a direct attack vector on that statement.

The repository therefore keeps its Clay-proximity low by default: **0-5%** until there is a concrete complexity-theoretic result, not merely a morphological or geometric analogy.

This is a feature, not a weakness. The correct path is to harden the internal mathematics first, then test whether the resulting machinery has traction against known complexity-theoretic barriers. If no traction is found, the successful output is a disciplined proof-analysis and infrastructure program, not a Clay program.

## 1. Barrier landscape

Any lower-bound-shaped claim must be tested against at least three standard barriers.

### Relativization

Techniques that survive arbitrary oracle access cannot decide P vs NP, since there are oracles `A` with `P^A = NP^A` and oracles `B` with `P^B != NP^B`.

Program consequence: diagonalization, black-box simulation, and oracle-stable search rhetoric cannot be promoted as Clay movement.

### Natural proofs

A combinatorial property used for general circuit lower bounds is blocked, under standard pseudorandomness assumptions, when it is both constructive and large.

Program consequence: any proposed invariant over Boolean functions must explicitly declare whether it is constructive and whether it is large. If both are true, it is presumed natural and cannot carry a general circuit lower-bound claim without a separate escape argument.

### Algebrization

Even many non-relativizing arithmetization techniques still relativize when machines are given access to low-degree extensions of oracles.

Program consequence: algebraic or singular-geometric language is not automatically non-algebrizing. Every algebraic bridge must state whether it survives algebrized oracle access.

## 2. Where this framework might engage

### Proof complexity

This is the most natural near-term surface. The doctrine already treats proof systems, proof morphology, basis-relative proof length, depth, compression, provenance, and proof-character generating functions as first-class objects.

Clay-adjacent objective: determine whether a proof-class generating function `P_B` and its singular-germ decomposition encode known proof-complexity invariants such as size, width, depth, space, substitution cost, or proof-system simulation cost.

Near-term diagnostic:

```text
Does P_B correspond to a known proof-system invariant or produce a new one that survives comparison against classical restricted systems?
```

If yes, this lane can contribute to proof complexity proper. If no, the connection remains methodological.

### Geometric complexity theory adjacency

The singular-germ regime stack is algebraic-geometric in flavor. GCT studies orbit-closure containment questions for objects such as determinant and permanent, and the permanent-vs-determinant problem is a major algebraic-complexity analog of P vs NP.

Clay-adjacent objective: test whether Milnor fibers, singularities of orbit closures, mixed-Hodge data, or finite-part residue data can interact with GCT obstruction theory in a non-decorative way.

Near-term diagnostic:

```text
Does a natural map exist from this program's singular-germ regime data into a representation-theoretic obstruction, multiplicity obstruction, or orbit-closure invariant?
```

If yes, this becomes the highest Clay-adjacent lane. If no, the algebraic geometry remains a useful analogy but not a GCT contribution.

### Average-case and meta-complexity

The renormalized-defect regime extracts finite invariants from sequences that fail exact closure. This resembles the broad meta-complexity question of distinguishing structured residuals from pseudorandom or incompressible behavior.

Clay-adjacent objective: test whether renormalized defect can be formulated as a distribution-aware complexity measure rather than an after-the-fact diagnostic.

Near-term diagnostic:

```text
Can renormalized defect be defined before observing the result, on a declared input distribution, with an explicit null model and tranche metadata?
```

If yes, this lane may connect to average-case complexity or MCSP-style questions. If no, it remains an empirical analysis tool.

## 3. Where this framework cannot currently engage

The current framework has no native path to:

- direct Boolean circuit lower bounds for explicit functions;
- diagonalization-based P vs NP separation;
- pure reduction arguments proving P vs NP;
- agentic-search claims that bypass worst-case complexity;
- generator/verifier collapse claims.

Any artifact that appears to make one of these moves must be demoted unless it supplies a formal barrier analysis.

## 4. Three tracks across eight quarters

The earlier phrase "six quarters" is corrected here: the actual structure is **eight quarters** because Track C runs through Q8.

### Track A — harden the framework to preprint grade, Q1-Q2

Goal: produce internal mathematical results before making any Clay-adjacent commitments.

#### A1. Polarization compatibility

Deliverable: `docs/foundations/polarization.md`.

Work:

- define the bilinear or Hermitian form on the active constraint complex;
- show how it descends from the Hodge/intersection-type polarization on the bridge-relevant cohomology;
- verify preservation by the Catalan / `A_1` bridge action;
- make the pairing, Gram matrix, and encoding map ledgered inputs rather than post-hoc choices.

#### A2. Gate minimality theorem for `SO(3)` / `Spin(3)`

Deliverable: arXiv-ready theorem note, 15-25 pages.

Work:

- use polarization compatibility as an imported hypothesis;
- prove the compact connected Lie reduction;
- exclude abelian circle-type competitors;
- identify `SO(3)` as the minimal non-abelian triad image;
- attach the `Spin(3)=SU(2)` lift realizing the half-integer sign.

#### A3. Catalan `mu_2` reference implementation

Deliverable: reproducible implementation and ledgered verifier.

Pass conditions:

- committed Sauzin/Stokes normalization;
- declared source pairing and active-constraint pairing;
- declared `E_phi` before monodromy evaluation;
- source and gate monodromy commute under `E_phi` within tolerance;
- replayable hash chain over inputs, matrices, outputs, and convention file.

End-of-Track-A target: one proved theorem target reduced to a clean proof note, one canonical instance, one replayable empirical artifact.

### Track B — identify the Clay-adjacent surface, Q2-Q4

Goal: test the framework against real complexity-theory surfaces, with null results allowed.

#### B1. Proof-complexity engagement

Reading spine:

- Cook / Reckhow proof systems;
- Krajicek, bounded arithmetic and proof complexity;
- Pudlak-style surveys on proof complexity and optimal proof systems;
- classical lower bounds for resolution, cutting planes, bounded-depth Frege, Frege, and extended Frege.

Diagnostic:

```text
Can P_B, with its singular-germ decomposition, encode proof-size distributions in a way that maps to size, width, depth, space, substitution, or simulation cost?
```

Output: 20-30 page technical note ending in explicit go/no-go.

#### B2. GCT engagement

Reading spine:

- Mulmuley-Sohoni GCT I and accessible GCT surveys;
- permanent-vs-determinant orbit-closure formulations;
- occurrence-obstruction limitations;
- multiplicity-obstruction variants.

Diagnostic:

```text
Do singularities in coordinate rings or orbit closures carry bridge-relevant Milnor, Hodge, Stokes, or finite-part data that can interact with obstruction theory?
```

Output: technical note ending in explicit go/no-go.

#### B3. Meta-complexity engagement

Reading spine:

- MCSP and Kolmogorov-complexity approximation literature;
- average-case lower-bound connections;
- learning-theoretic barriers and pseudorandomness constraints.

Diagnostic:

```text
Can renormalized defect be made input-distribution-first, null-model-aware, and non-post-hoc?
```

Output: technical note ending in explicit go/no-go.

End-of-Track-B target: at least one green-lit Clay-adjacent surface, or a documented conclusion that the framework is not presently on a Clay trajectory.

### Track C — commit to one Clay-adjacent target, Q5-Q8

Only one Track-B output may become the primary Track-C target. This prevents a broad, unfalsifiable program from masquerading as progress.

#### C-low: proof-complexity contribution

Most likely; lowest Clay proximity; highest result probability.

Starter target:

```text
Study whether the proof-character generating function for resolution proofs of pigeonhole-style tautologies has singularity structure that detects known proof-size or width lower bounds.
```

Expected output: a proof-complexity paper using singular-germ invariants as a new lens on restricted proof systems.

#### C-mid: GCT obstruction contribution

Less likely; real Clay adjacency; medium result probability.

Starter target:

```text
Find or rule out a natural singular-germ invariant attached to a specific permanent/determinant orbit-closure containment question.
```

Expected output: a GCT-adjacent note. Even a no-go result is useful if it precisely identifies where singular-germ data fails to interact with obstruction theory.

#### C-high: average-case / meta-complexity result

Least likely; highest Clay proximity; lowest result probability.

Starter target:

```text
Identify a complexity-theoretic statement where renormalized defect supplies a nontrivial invariant under declared distributions and null models.
```

Expected output: only admissible if Track B produces an unexpectedly strong bridge.

## 5. Decision gates

### Gate 1 — end Q2

Question:

```text
Has Track A produced polarization formalization and a gate-minimality proof note?
```

If no: stop Clay-track expansion. The framework lacks enough internal theorem content.

### Gate 2 — end Q4

Question:

```text
Has Track B identified at least one concrete Clay-adjacent engagement surface?
```

If no: publish Track A as a disciplined mathematical framework and redirect future effort to applied proof analysis, SocioProphet search/governance, and infrastructure.

### Gate 3 — end Q6

Question:

```text
Has Track C produced a concrete partial result or a clearly stated obstruction?
```

If no: pivot to another Track-B output or reclassify the program as multi-decade foundational work.

## 6. Refusals

This roadmap refuses the following moves:

- claiming P vs NP can be resolved by the current framework;
- claiming any Track-B lane will succeed before the go/no-go note exists;
- skipping Track A;
- generalizing beyond the `p=2` / `A_1` bridge before the first theorem and verifier are stable;
- collapsing proof complexity, GCT, and meta-complexity into one rhetorical umbrella;
- treating singular geometry as an automatic complexity-theory weapon.

## 7. Immediate action

Start with Track A1.

The next deliverable is a compact foundational note that can be cited by the gate-minimality theorem:

```text
docs/foundations/polarization.md
```

Minimum acceptable output:

- source pairing defined;
- active-constraint pairing defined;
- encoding map `E_phi` typed;
- preservation statement written formally;
- Catalan / `A_1` case specialized;
- replay fields specified;
- nonclaims and failure modes explicit.
