# G-EP13 — transformer weight export and finite-field diagnostics

## Purpose

This milestone adds a small, optional adapter from neural-network layer weights
to the exact prime-field routines developed in G-EP6–G-EP12. It is an
interoperability experiment, not a claim that finite-field fingerprints are
invariants or useful predictors of a model's behavior.

The adapter is in `tools/transformer_adapter.py`. It has no NumPy or PyTorch
dependency. Tensor-like values are accepted through the conventional
`detach().cpu().tolist()` protocol, while ordinary nested sequences work
directly.

## Explicit conversion

For a finite real weight entry (w), scale (s>0), and prime (p), the
exported field element is

[
  [w]_{p,s} = \operatorname{round}(s w) \bmod p.
]

Python's built-in `round` is round-to-nearest with ties-to-even. The adapter
records the prime, scale, shape, rounding policy, and the fact that conversion
is lossy. Non-finite values, ragged arrays, nonpositive scales, and
non-prime moduli are rejected.

This map is not canonical: changing (s), (p), precision, or rounding policy
can change the exported matrix. Floating-point quantization followed by
reduction modulo (p) can erase distinctions and should not be interpreted
as preserving real-valued spectra, norms, singular values, or model function.

## Correct treatment of layer shape

Transformer linear layers commonly have rectangular weight matrices
(W\in\mathbb R^{m\times n}). Such a matrix is a linear map between
different vector spaces, not an endomorphism when (m\ne n). Therefore:

- `analyze_weight_matrix` supports rectangular matrices and reports exact
  rank over the chosen finite field.
- `analyze_square_weight_operator` rejects rectangular input and runs the
  automatic characteristic-factor/Jordan fingerprint only for square
  exported matrices.

The adapter does not silently truncate, pad, or project a rectangular matrix
to make it square. Square attention projections may be inspected as operators
when their input/output spaces have the same declared basis; that basis
interpretation remains the caller's responsibility.

## Minimal use

```python
from tools.transformer_adapter import (
    analyze_weight_matrix,
    analyze_square_weight_operator,
)

# A rectangular projection: rank is well-defined.
report = analyze_weight_matrix(layer_weight, prime=101, scale=1000)

# Only for a genuinely square operator in a declared common basis:
spectral = analyze_square_weight_operator(square_weight, prime=101, scale=1000)
```

The first example's keyword is `p` in the current API:

```python
report = analyze_weight_matrix(layer_weight, p=101, scale=1000)
```

## Evidence and limits

Tests cover the tensor-like protocol without importing a framework, rectangular
rank, ties-to-even rounding, metadata, invalid inputs, and a small square
Jordan example. This establishes adapter correctness on controlled examples;
it does not establish predictive value, robustness, or usefulness on trained
transformers.

A meaningful empirical study would need actual model checkpoints, a declared
weight extraction convention, several primes and scales, repeated runs across
layers/checkpoints, and comparisons against simple baselines. It should measure
sensitivity to small perturbations and quantization choices before making any
claim that a fingerprint tracks learning or model structure. Integer or
quantized checkpoints are preferable when available because they avoid an
additional floating-point rounding step, although reduction modulo (p) is
still a lossy map.

Large matrices remain a practical limitation: full characteristic
factorization/Jordan analysis is intended as an exact reference path for
manageable square matrices, not as a production-scale transformer profiler.
