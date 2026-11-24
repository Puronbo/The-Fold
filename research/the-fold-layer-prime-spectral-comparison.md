# G-EP18 — layer-level prime spectral comparisons

## Interface

The new `tools/layer_spectral_comparison.py` accepts an explicit nested mapping:
```python
snapshots[snapshot_name][layer_name][projection_name] = matrix
```
It deliberately does not infer layer names or tensor roles from arbitrary checkpoint naming conventions.

For square projections, it computes G-EP17 prime-indexed characteristic-factor and Frobenius-orbit profiles. For rectangular projections, it reports modular rank only; a characteristic polynomial is not defined for a non-square matrix.

## Three distinct comparisons

For projections in the same layer and snapshot, each prime receives pairwise comparisons of:

1. modular rank;
2. Frobenius orbit-degree histogram;
3. exact irreducible-factor profile (including factor coefficients and multiplicities).

Across snapshots, it compares each named layer/projection at each prime with the first snapshot in insertion order. The report explicitly labels the reference snapshot.

## Synthetic test

The tests use identity and quarter-turn matrices, which both have rank two at every tested prime, while their orbit profiles differ over (mathbb F_3) and (mathbb F_7). A rectangular MLP-shaped projection confirms the rank-only path. Snapshot comparisons are checked separately.

Run:
```bash
python -m unittest tests.test_layer_spectral_comparison -v
```

## Interpretation and limits

G-EP18 makes the measurements layer-aware; it does not establish that the measurements are useful. The tool compares the matrices exactly after finite-field quantization. Prime, scale, and quantization policy can change the result. Matching algebraic profiles do not imply matching model functions, activations, logits, or task performance.

The next empirical test requires real checkpoint snapshots. A meaningful evaluation should compare G-EP18 against rank-only and conventional spectral summaries, measure stability under small checkpoint changes, and relate each diagnostic to an independent task or validation metric. Until then, all evidence is algebraic and synthetic.
