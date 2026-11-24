# G-EP154: Exhaustive 3×3 similarity-orbit audit over F₃

This milestone exhaustively examines all \(3^9=19,683\) matrices in \(M_3(\mathbb F_3)\). Test-local arithmetic computes the characteristic polynomial from the trace, principal 2×2 minors, and determinant. The product of production invariant factors is checked against that independent polynomial.

For every matrix, the test enumerates all 27 vectors and checks cyclicity through the determinant of \([v,Av,A^2v]\). This predicate is compared with the production profile's one-invariant-factor condition.

The test enumerates all \(|GL(3,\mathbb F_3)|=11,232\) invertible basis matrices. For every invariant-factor profile represented in the exhaustive matrix space, it computes the complete conjugacy orbit of a representative and checks exact equality with the profile fibre. Thus both containment directions are checked over the entire 3×3 matrix space.

The exhaustive claim is restricted to dimension three over \(\mathbb F_3\). It is finite regression evidence, not a theorem for larger dimensions or fields and not a new production similarity algorithm.
