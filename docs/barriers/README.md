# Complexity Barrier Registry

Status: **required side condition for lower-bound-shaped claims**.  
Scope: P vs NP, proof complexity, circuit lower bounds, algebraic complexity, average-case complexity, and agentic proof-search claims.

This registry turns the doctrine's barrier-awareness requirement into a concrete checklist. Any artifact that resembles a lower bound, separation, generator/verifier collapse, proof-system separation, or Clay-adjacent claim must attach a barrier entry before promotion beyond Stage I.

## 1. Registry rule

Every lower-bound-shaped claim must carry the following record:

```yaml
claim_id: string
claim_type: theorem | conjecture | empirical | heuristic | roadmap
basis: string
stage: candidate_found | verified | understood | generalized
barriers:
  relativization: pass | fail | unknown | not_applicable
  natural_proofs: pass | fail | unknown | not_applicable
  algebrization: pass | fail | unknown | not_applicable
  proof_complexity_transfer: pass | fail | unknown | not_applicable
  average_case_transfer: pass | fail | unknown | not_applicable
notes: string
references: list[string]
```

Default is conservative:

```text
unknown => no Clay-proximity promotion
fail    => demote or restrict claim
pass    => allowed to proceed, not proof of P vs NP
```

Passing a barrier check only means the artifact is not obviously blocked by that barrier. It does not imply the target separation is true.

## 2. Relativization

Canonical source: Baker-Gill-Solovay, *Relativizations of the P =? NP Question*, 1975.

### Barrier statement

A technique that remains valid relative to every oracle cannot resolve P vs NP, because there are oracles `A` with:

```text
P^A = NP^A
```

and oracles `B` with:

```text
P^B != NP^B
```

### Required questions

```text
Does the proposed argument relativize?
Does it use only black-box access to a language, verifier, generator, proof system, or oracle?
Does the argument survive arbitrary oracle extension?
Does it distinguish the unrelativized world from known relativized worlds?
```

### Automatic failure modes

- diagonalization-only arguments;
- black-box simulation arguments;
- search-process rhetoric treated as lower bound;
- oracle-stable proof-size comparisons without additional nonrelativizing structure.

### Program use

The morphology doctrine can measure proof, witness, and generator structure under oracle changes. That is admissible. It cannot infer P vs NP movement unless it identifies a nonrelativizing invariant.

## 3. Natural proofs

Canonical source: Razborov-Rudich, *Natural Proofs*, 1997.

### Barrier statement

A circuit-lower-bound method is blocked, under standard pseudorandomness assumptions, when the separating property is both:

```text
constructive: efficiently decidable from the function truth table or representation
large: true for a non-negligible fraction of functions
```

### Required questions

```text
Is the proposed property constructive?
Is the proposed property large?
Does it apply to an explicit Boolean function family?
Does it distinguish pseudorandom functions from random functions?
Does it assume or violate standard cryptographic pseudorandomness assumptions?
```

### Automatic failure modes

- counting-based lower-bound arguments without anti-largeness analysis;
- efficiently testable generic morphology properties presented as circuit lower bounds;
- empirical distinguishers over finite samples promoted to general lower bounds.

### Program use

The proof-character generating function `P_B` may define structured observables. If an observable becomes a Boolean-function property, it must be classified as constructive/nonconstructive and large/small before any lower-bound interpretation.

## 4. Algebrization

Canonical source: Aaronson-Wigderson, *Algebrization: A New Barrier in Complexity Theory*, 2008.

### Barrier statement

Some nonrelativizing arguments still fail because they relativize after the oracle is replaced by, or supplemented with, a low-degree algebraic extension.

### Required questions

```text
Does the proposed argument merely arithmetize a relativizing argument?
Does it survive access to low-degree oracle extensions?
Is the singular-geometric structure intrinsic or just an algebraic repackaging of black-box behavior?
Can the argument separate worlds that agree under algebrized access?
```

### Automatic failure modes

- assuming algebraic language is automatically non-algebrizing;
- using polynomial extensions without explaining why the barrier does not apply;
- treating Stokes, monodromy, or finite-part data as barrier-escaping without a nonalgebrizing mechanism.

### Program use

Singular geometry is allowed and central to this repo. It does not, by itself, defeat algebrization. GCT adjacency must document whether the proposed obstruction lives outside the algebrizing template.

## 5. Proof-complexity transfer barrier

Canonical sources: Cook-Reckhow proof systems; Krajicek and Pudlak-style proof-complexity surveys.

### Barrier statement

A statement about one proof basis, corpus, or restricted proof system does not automatically transfer to stronger systems.

### Required questions

```text
Which proof system is the basis B?
What is the translation morphism tau between B1 and B2?
What is the cost generating function T_tau?
Is the claimed invariant preserved under simulation?
Does the result target restricted systems, Frege, extended Frege, or all Cook-Reckhow systems?
```

### Automatic failure modes

- comparing proof lengths across systems without translation cost;
- promoting a resolution/cutting-planes/bounded-depth result to Frege or extended Frege;
- using corpus statistics as proof-system lower bounds without worst-case quantification.

### Program use

This repo can contribute earliest to restricted proof systems and proof morphology. A general NP vs coNP claim requires a proof-system-universal statement, not just a corpus invariant.

## 6. Average-case and meta-complexity transfer barrier

Canonical sources: MCSP, Kolmogorov-complexity approximation, hardness-vs-randomness, and average-case complexity literature.

### Barrier statement

Distributional distinguishers, defect measures, and empirical residual structure do not imply worst-case separation without an explicit transfer theorem.

### Required questions

```text
What is the input distribution?
What is the tranche?
What is the null model?
Is the distinguisher defined before observing the data?
Does the result prove worst-case, average-case, smoothed, or empirical behavior?
What transfer theorem is being invoked?
```

### Automatic failure modes

- post-hoc residual extraction;
- unregistered distributions;
- solver-performance claims without tranche metadata;
- claiming average-case structure as worst-case lower bound.

### Program use

Renormalized defect is admissible as an empirical observable only if distribution, tranche, null model, and replay ledger are declared first.

## 7. Claim-stage policy

### Stage I — candidate found

Allowed:

- heuristic connection;
- roadmap;
- analogy;
- finite experiment;
- proposed invariant.

Required:

- barrier registry entry may be incomplete but must identify unknowns.

### Stage II — verified

Allowed:

- checked finite result;
- proved restricted theorem;
- reproducible implementation.

Required:

- barrier registry entry complete for the claim's declared scope.

### Stage III — understood

Allowed:

- explanation of why the result works;
- comparison against known techniques;
- failure boundaries.

Required:

- explicit pass/fail/unknown status for each relevant barrier.

### Stage IV — generalized

Allowed:

- transfer to broader class;
- family theorem;
- cross-basis claim.

Required:

- transfer morphism or theorem;
- no unknown barrier statuses for the promoted scope.

## 8. Current program defaults

```yaml
program: np-program
clay_proximity: 0-5%
default_claim: singular-germ morphology framework
relativization: unknown
natural_proofs: unknown
algebrization: unknown
proof_complexity_transfer: unknown
average_case_transfer: unknown
promotion_policy: no Clay-proximity promotion until Track B go/no-go notes exist
```

## 9. Immediate registry entries

### CLAY-ROADMAP-001

```yaml
claim_id: CLAY-ROADMAP-001
claim_type: roadmap
basis: repository doctrine and singular-germ framework
stage: candidate_found
barriers:
  relativization: unknown
  natural_proofs: unknown
  algebrization: unknown
  proof_complexity_transfer: unknown
  average_case_transfer: unknown
notes: >
  Roadmap only. No lower bound or separation claimed. Track B exists to determine
  whether any surface has real complexity-theoretic engagement.
references:
  - Baker-Gill-Solovay 1975
  - Razborov-Rudich 1997
  - Aaronson-Wigderson 2008
```

### A1-POLARIZATION-001

```yaml
claim_id: A1-POLARIZATION-001
claim_type: theorem-input definition
basis: A_1 singular-germ bridge and active constraint complex
stage: candidate_found
barriers:
  relativization: not_applicable
  natural_proofs: not_applicable
  algebrization: unknown
  proof_complexity_transfer: not_applicable
  average_case_transfer: not_applicable
notes: >
  Foundational definition for the gate-minimality theorem. It is not a complexity
  lower bound. Algebrization remains unknown only if later used for complexity transfer.
references:
  - docs/foundations/polarization.md
  - docs/research/polarization-compatibility.md
```

### GATE-MINIMALITY-001

```yaml
claim_id: GATE-MINIMALITY-001
claim_type: theorem target
basis: Lawful Learning spatial triad, A_1 sign bridge, compact connected Lie gate factors
stage: candidate_found
barriers:
  relativization: not_applicable
  natural_proofs: not_applicable
  algebrization: not_applicable
  proof_complexity_transfer: not_applicable
  average_case_transfer: not_applicable
notes: >
  Lie-theoretic minimality claim for gate realization, not a P vs NP claim.
  May become relevant to complexity only through a later Track-B transfer note.
references:
  - docs/research/gate-minimality-theorem-target.md
```
