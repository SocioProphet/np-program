# Catalan p=2 Monodromy Ledger

Fixture citation: `[HG-EX-001 @ 988307215ad38ccb16514311222184a1b757752b]`  
Operator citation: `[PFK-OP-040 @ 988307215ad38ccb16514311222184a1b757752b]`  
Schema citation: `[PFK-SCHEMA-001 @ 988307215ad38ccb16514311222184a1b757752b]`  
Boundary anti-seed: framework Catalan fixture boundary plus `[A-PFK-OP-001 @ 988307215ad38ccb16514311222184a1b757752b]`

## Status

Fixture-grade only.

Computing the Catalan / mu2 fixture is apparatus validation. It does not promote any np-program claim grade and does not constitute P-vs-NP progress.

## What this ledger records

This directory records the np-program instantiation of the Catalan p=2 monodromy test: encode, ledger, recompute monodromy, verify Spin lift, and check committed Stokes normalization, all per the protocol in `specs/catalan-mu2-reference-implementation.md`.

Each ledger entry, when emitted as a PFK-compatible artifact, must:

1. be schema-valid against `PFK-SCHEMA-001` (claim ledger row) if it is a claim-ledger row;
2. cite `HG-EX-001` as the framework fixture;
3. cite `PFK-OP-040` as the operator family invoked;
4. cite the Catalan fixture boundary and `A-PFK-OP-001` as anti-seed controls;
5. carry fixture-grade claim discipline;
6. preserve method-distance status unless a later PR explicitly promotes it.

Empirical-protocol fields N1/N2/S1/S2/S3 are not required for single-fixture calibration. Multi-window or multi-perturbation studies must comply with PFK protocol discipline.

## Existing fixture

`sample_ledger.json` remains the deterministic local sample used by `tests/test_catalan_mu2.py`.
