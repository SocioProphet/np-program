# Coordinate-Basis vs Readout-Basis Involution Reference

Status: **thin cross-repo reference / Track A guardrail / not theorem content**.  
Canonical owner: `SocioProphet/systems-learning-loops`.  
Canonical pattern path:

```text
kb/patterns/coordinate-basis-vs-readout-basis-involution.md
```

## Purpose

This note attaches the canonical coordinate-basis vs readout-basis involution pattern to the `np-program` without duplicating the full KB argument locally.

The local guardrail is:

```text
mu_2 sign detection is not full readout-basis selectivity.
```

## Local interpretation

The Catalan `mu_2` fixture detects a `Z/2` sign channel. It does not identify which `Z/2` factor inside a possible `V4 = Z/2 x Z/2` structure is active, and it does not by itself provide the full `GF(4)` MOLS/readout-basis structure.

Therefore:

```text
A1 mu_2 fixture: detects one sign-line involution.
Track A2/A3: must declare the readout basis and any higher finite-field/MOLS structure separately.
```

The canonical KB pattern records the broader doctrine:

```text
involution + selectivity + balance + composability
```

and the finite algebraic guardrail that the relevant order-four structure is `V4`/`GF(4)`-based, not cyclic `Z4`.

## Cross-repo policy

Do not copy the full argument into this repository. Link to the canonical KB page:

```text
SocioProphet/systems-learning-loops/kb/patterns/coordinate-basis-vs-readout-basis-involution.md
```

## Nonclaims

This reference does not claim:

- P vs NP progress;
- a circuit lower bound;
- a proof-complexity lower bound;
- that the Catalan `mu_2` harness identifies a full `V4` action;
- that the Part B cipher experiment measures circuit lower-bound structure;
- that Track A has cleared relativization, natural-proofs, algebrization, or transfer barriers.

It is a claim-boundary note only.
