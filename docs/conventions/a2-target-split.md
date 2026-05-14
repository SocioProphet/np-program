# A2 Target Split Convention

Status: **blocking convention / target-splitting note / not a theorem claim**.  
Related issue: `#12` — A2 vs Fuss-Catalan singularity mismatch.  
Depends on: `docs/proofs/c3-layer1-a2-group-identification.md`, `docs/proofs/c3-layer2-a2-polarization-candidates.md`, `docs/scope/singularity-classes.md`.

## 0. Purpose

This note prevents a false identification:

```text
Fuss-Catalan order-3 critical branch ≠ pure A2 local cube-root branch.
```

The proposed `A2-fusscatalan-normalization-v0` draft conflated these objects. That draft is blocked until the target is split and the correct local singularity is chosen.

## 1. Target F — Fuss-Catalan order-3 critical branch

The order-3 Fuss-Catalan generating function is:

```text
y = 1 + x y^3.
```

Equivalently:

```text
F(x,y) = y - 1 - x y^3 = 0.
```

The dominant critical point satisfies:

```text
F(x0,y0) = 0
F_y(x0,y0) = 0
```

which gives:

```text
y0 = 3/2
x0 = 4/27.
```

Since:

```text
F_yy(x0,y0) ≠ 0,
```

this is a generic algebraic critical point with square-root Puiseux behavior. Its coefficients have the expected form:

```text
C_n^(3) ~ const · (27/4)^n · n^(-3/2).
```

The exponent `-3/2` is the square-root signature. Therefore Target F is not a three-sheet `mu3` cube-root harness.

A future Target F convention should be named separately, for example:

```text
fusscatalan-order3-critical-normalization-v0
```

and should test:

```text
coefficient enumeration
critical point x0 = 4/27, y0 = 3/2
local square-root coefficient
A1-type Puiseux exponent with growth constant 27/4
scope and provenance
```

## 2. Target A2 — pure local cube-root model

A pure A2 local cube-root target is instead modeled locally by:

```text
u^3 = t
```

or an equivalent local normal form with three sheets and `mu3` monodromy.

A future Target A2 convention should be named separately, for example:

```text
A2-local-cuberoot-normalization-v0
```

and should test:

```text
three-sheet local structure
mu3 monodromy / character data
principal-sheet rule
three lateral-value slots
Candidate A no-mixing/readout-sheet contract
Layer 2 polarization data if Stage-2 promotion is attempted
```

## 3. Immediate rule

Do not use the label:

```text
A2-fusscatalan-normalization-v0
```

unless the spec explicitly states which target it means and resolves the mismatch. Until then, that label is blocked.

## 4. Impact on C-3' Layer 2

Candidate A in the C-3' Layer 2 note applies to the pure local A2 cube-root target, not automatically to the order-3 Fuss-Catalan critical branch.

The order-3 Fuss-Catalan harness may still be useful as a Stage-1 dimensional / coefficient-growth test, but it cannot supply the `mu3` sheet-grading contract unless a separate local model or change of target is supplied.

## 5. Nonclaims

This note does not claim:

- that the C-3' Layer 1 or Layer 2 notes are false;
- that order-3 Fuss-Catalan data are unimportant;
- that the pure A2 cube-root target is already implemented;
- that A2 has a Stage-2 gate-minimality theorem;
- that any P vs NP or Clay result follows.

It is a target-splitting convention. Its function is to prevent a mathematically ill-typed harness contract from entering the repo.