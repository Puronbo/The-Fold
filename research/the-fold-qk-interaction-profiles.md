# G-EP19 — relational finite-field profiles for Q/K projections

## The two products are not interchangeable

Assume equal-shaped projection matrices (Q,K\in\mathbb Z^{d_o\times d_i}), after the existing explicit quantization step.

There are two natural square products:
[
G_o=QK^T\in\mathbb Z^{d_o\times d_o},\qquad
G_i=Q^TK\in\mathbb Z^{d_i\times d_i}.
]
They act on different spaces and generally have different dimensions and spectra.

With row-vector input activations (X\in\mathbb R^{n\times d_i}), and projected activations (XQ^T), (XK^T), the pre-softmax score matrix is
[
(XQ^T)(XK^T)^T=X(Q^TK)X^T.
]
Thus (G_i) is the input-space bilinear form appearing between activations. (G_o) is the corresponding output-space product. Neither product alone is the attention score matrix; the activations (X) are still required.

## Implementation

`tools/qk_interaction.py` computes both products with exact integer arithmetic and then profiles them over each selected prime. It also profiles Q and K individually when they are square. Rectangular Q/K are supported as long as their shapes match; both interaction products remain square.

The routine intentionally does not run softmax or evaluate a model forward pass. It does not assume that finite-field quantization preserves real-valued attention.

## Tests

`tests/test_qk_interaction.py` checks:
- both products and the row-vector attention identity on a square fixture;
- rectangular projections producing square products of different dimensions;
- exact ranks and Frobenius profiles over multiple primes;
- invalid shape and prime-list handling.

Run:
```bash
python -m unittest tests.test_qk_interaction -v
```

## Interpretation

This is a relational diagnostic: it measures an interaction derived jointly from Q and K, rather than treating each projection independently. It may contain information not visible in their separate ranks or characteristic factors, but no such incremental value has yet been established empirically.

The next meaningful test should compare real trained checkpoints and controlled perturbations, then ask whether (Q^TK) profiles are more stable or informative than Q/K profiles and ordinary real-valued singular-value or covariance summaries. Even an exact match of finite-field profiles does not imply equal attention scores, because the full computation also depends on X, softmax, scaling, masks, and subsequent layers.
