# G-EP43 — rational primary decomposition

## Result

For a finite-dimensional operator (A) over (mathbb F_p), factor its
characteristic polynomial into distinct monic irreducibles (f). The primary
subspaces are

[
V_f=\ker(f(A)^n).
]

The primary decomposition theorem gives (V=\bigoplus_f V_f). The new
routine computes each kernel by exact modular row reduction, concatenates
their bases, and verifies that the resulting coordinate matrix is invertible
and that the conjugated operator is block diagonal across the components.

## Implementation

`tools/rational_primary_decomposition.py` exposes
`rational_primary_decomposition(matrix, p)`. It returns component
polynomials, dimensions, basis columns, the change-of-basis matrix, the
transformed operator, component offsets, and explicit verification flags.

The implementation uses existing characteristic-polynomial factorization,
polynomial evaluation, modular nullspace, and matrix inversion routines.

## What this establishes—and what it does not

This is a structural reduction for the shared-chart case: an operator can
now be separated into its irreducible-primary pieces over the original
finite field. It does **not** yet construct cyclic generators within a
primary component, nor does it solve arbitrary noncyclic strict-equivalence
witnesses. The next step is to split each primary module into its elementary
divisor cyclic summands and construct intertwiners summand-by-summand.

## Tests

The tests cover distinct linear factors, a repeated linear primary factor,
and a quadratic irreducible component over (mathbb F_3).
