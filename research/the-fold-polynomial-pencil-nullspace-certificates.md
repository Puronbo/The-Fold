# G-EP27 — Polynomial nullspace certificates for matrix pencils

For a pencil \(P(t)=Q+tK\) over \(\mathbb F_p[t]\), G-EP25 recovered left and right minimal indices from bounded-degree polynomial-kernel nullities. G-EP27 strengthens that count-based result by constructing explicit polynomial kernel generators and checking that their shifts span every bounded-degree kernel that was examined.

## Construction

For each degree bound \(d\), the coefficient-convolution matrix represents
\[
P(t)(x_0+x_1t+\cdots+x_dt^d)=0.
\]
An exact modular nullspace basis is computed. Previously selected generators are multiplied by all powers \(1,t,\ldots,t^{d-\epsilon_i}\) that fit the degree bound. New generators are selected as a vector-space complement to the span of those shifts.

Each generator is returned as coefficient vectors in low-degree-first order. The implementation multiplies it by \(Q+tK\) coefficient-by-coefficient and verifies the product is identically zero. At every bound it also checks that the shifts of the constructed generators span the entire bounded-degree kernel, by comparing exact dimensions.

## API

`rectangular_pencil_nullspace_certificate(q, k, p, max_degree=8, max_minors=2000)`

The result contains explicit right and left polynomial generators, their degrees, zero-product checks, bounded-kernel span checks, and an overall completeness flag. A zero minimal index is represented by a nonzero constant common-kernel vector.

## What the certificate means

If the right and left generator counts equal the normal-rank deficiencies and every bounded-degree span check passes, the output certifies bases for the polynomial right and left nullspaces, with the recovered minimal indices. The normal-rank computation is exact and comes from the polynomial Smith routine. The degree cap is explicit: if not all generators have appeared by the cap, the result remains incomplete.

This adds auditable witnesses to the minimal-index data; it still does not construct unimodular transformation matrices or an explicit Kronecker canonical decomposition. The polynomial-minor computation inherits G-EP24's combinatorial budget and is intended for small dense pencils. Arithmetic is exact over the selected prime field.

## Tests

Tests cover simultaneous left/right singular blocks, multiple right generators with equal degree, zero minimal indices, a too-small degree cap, and a regular pencil with no polynomial nullspace generators.
