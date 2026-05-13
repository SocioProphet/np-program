# Catalan `mu_2` Reference Harness

This experiment implements the first deterministic test for the NP Program's `A_1` singular-germ bridge.

It validates:

1. Catalan coefficient enumeration;
2. square-root branch monodromy with distinguished eigenvalue `-1`;
3. a synthetic `SO(3)` loop whose `Spin(3)=SU(2)` lift runs from `I` to `-I`;
4. `A1-sauzin-normalization-v0` wall-crossing data;
5. polarization and provenance/hash-chain checks.

Run locally:

```bash
python experiments/catalan_mu2/catalan_mu2_harness.py \
  --N 10 \
  --output ledgers/catalan_mu2/sample_ledger.json \
  --validate
```

The harness validates the Catalan instance only. It does not prove P vs NP or the full Lawful Morphology framework.
