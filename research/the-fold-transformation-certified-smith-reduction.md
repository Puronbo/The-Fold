# G-EP28 — Transformation-certified polynomial Smith reduction

G-EP28 makes the regular polynomial-matrix reduction constructive. For the pencil
\[
P(t)=Q+tK\in\mathbb F_p[t]^{m\times n},
\]
the routine `polynomial_smith_transform(q,k,p)` constructs polynomial matrices
\[
U(t),\quad V(t),\quad D(t)=U(t)P(t)V(t)
\]
where (D(t)) is diagonal and its successive nonzero diagonal entries divide the next ones.

## Construction and certificate

The algorithm uses polynomial Euclidean row and column operations over the exact prime field: swaps, adding polynomial multiples of one row/column to another, and scaling a row by a nonzero field element. Each operation is unimodular. The full operation log is returned alongside explicit (U,V,D).

The result independently recomputes (U P V) and checks equality with (D), diagonality, and successive divisibility. The operation log certifies that both transforms are products of unimodular elementary operations; no floating-point arithmetic is used.

## Important boundary

This is a Smith form of the polynomial matrix (Q+tK). It is **not** a Kronecker canonical decomposition of the pencil under constant strict equivalence. In particular, Smith form alone does not expose the left/right minimal-index blocks; those remain separately described by G-EP25–G-EP27. Nor does this routine yet construct a full set of polynomial transformations that isolates regular and singular Kronecker blocks in one canonical pencil form.

The routine is intended for small dense pencils and exact arithmetic over (mathbb F_p[t]). Transformation matrices can grow in degree and size; the operation log is therefore retained for auditability.

## Tests

Tests cover regular, rectangular singular, nontrivial Euclidean-reduction, zero, and explicit-transformation cases.
