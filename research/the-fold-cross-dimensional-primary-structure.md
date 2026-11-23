# G-EP22 — cross-dimensional primary-module comparison

Two matrices of different dimensions cannot be similar, so equality of rational canonical forms is not the right comparison. A useful alternative is to compare their primary components over the same prime field.

For each monic irreducible factor (f\in\mathbb F_p[x]), the rational canonical profile supplies its primary dimension and elementary-divisor block sizes. G-EP22 compares two such decompositions without requiring equal matrix dimensions.

For each common irreducible factor, it reports:

- primary dimensions in each operator;
- the shared primary dimension, defined as the minimum of those two dimensions;
- exact common elementary-divisor multiplicities, requiring both the same factor and the same block exponent.

The aggregate primary-dimension overlap measures how much dimension lies in matching irreducible primary components. The stricter elementary-divisor overlap measures how much dimension lies in exactly matching blocks. Both are normalized by the smaller operator's dimension.

## Important distinctions

A shared irreducible factor only means that both operators have a primary component associated with the same polynomial over the chosen field. It does not mean that the operators are similar, have the same dimension, or act similarly in a neural network.

Primary-dimension overlap can be positive even when block structures differ. For example, a single nilpotent block of size two and two nilpotent blocks of size one have the same (x)-primary dimension, but no elementary divisor (x^e) in common.

These descriptors depend on the prime: irreducible factors can split or combine after changing fields. Comparisons must use the same prime and the same coefficient convention.

## Implementation

- `tools/primary_structure.py`: `compare_primary_structure(A, B, p)`.
- `tests/test_primary_structure.py`: different dimensions with common support, equal primary dimension but different block partitions, disjoint primary support, and invalid modulus.

The comparison reuses the exact rational-canonical engine. It is dense and intended as a research diagnostic, not a production-scale embedding similarity metric.

## Neural-network relevance

This gives a mathematically precise way to compare square operators of different dimensions, including square projections from different layers. Rectangular matrices still need separate treatment (for example, rank and module structure of induced maps); they are not silently padded or converted into square operators.

No evidence is yet established that primary-module overlap predicts attention behavior, model quality, or semantic similarity. Such a claim would require real checkpoint datasets, controlled baselines, and independent task metrics.
