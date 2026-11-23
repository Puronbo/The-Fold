# G-EP14 — sensitivity audit for finite-field weight fingerprints

## Question

A finite-field fingerprint depends on the prime and on the real-to-integer quantization scale. Before interpreting any fingerprint as a signal about a trained model, we need a repeatable way to ask a narrower question:

**Does the exported signature remain the same across specified snapshots, quantization scales, and primes?**

G-EP14 adds `tools/transformer_sensitivity.py`, which compares caller-supplied weight snapshots under each requested prime/scale pair.

## Method

The first named snapshot is the reference. For each configuration, the tool:

1. exports each matrix using the G-EP13 conversion `round(scale * weight) mod p`;
2. computes exact rank over F_p;
3. optionally, for square matrices only, computes the complete spectral fingerprint and compares irreducible factorization plus Jordan block partitions for base-field and extension-field eigenvalue classes;
4. reports exact equality with the reference signature.

The same shape is required for all snapshots. Rectangular matrices are supported for rank-only comparisons. Full spectral comparisons reject rectangular input rather than silently projecting it.

## Interpretation

A `stable_vs_reference` value of true means only that the selected discrete finite-field signature is exactly equal for that particular prime and scale. It does **not** establish that two neural networks compute the same function, have similar behavior, or have equal predictive quality. A false result means the selected fingerprint changed; it does not by itself mean the model changed meaningfully.

Stability is configuration-specific. Agreement at one prime and scale does not imply agreement at another. The utility does not choose a prime, scale, perturbation magnitude, or snapshot naming convention on the user's behalf.

## Reproducible synthetic checks

The test suite includes:
- a small square identity matrix and a nearby rounded snapshot with unchanged fingerprint;
- a changed eigenvalue whose square spectral signature differs;
- rectangular snapshots with equal rank and a rank-drop example;
- multiple primes/scales and invalid shape/configuration checks.

These are controlled software tests, not experiments on trained transformer checkpoints. No empirical claim about neural-network usefulness follows.

## Next empirical step

A real evaluation should extract several checkpoints from a known model and record layer names, tensor shapes, dtypes, quantization metadata, and training steps. It should compare the finite-field reports with conventional diagnostics such as real-valued singular values, norms, and validation behavior. The protocol should include multiple primes/scales and repeated checkpoints, and should report false-positive/false-negative rates before claiming the fingerprints detect meaningful training changes.
