# G-EP154: Exhaustive 3×3 similarity-orbit audit over F₃

This milestone exhaustively examines all \(3^9=19,683\) matrices in \(M_3(\mathbb F_3)\). Test-local arithmetic computes the characteristic polynomial from the trace, principal 2×2 minors, and determinant. The product of production invariant factors is checked against that independent polynomial.

For every matrix, the test enumerates all 27 vectors and checks cyclicity through the determinant of \([v,Av,A^2v]\). This predicate is compared with the production profile's one-invariant-factor condition.

The test enumerates all \(|GL(3,\mathbb F_3)|=11,232\) invertible basis matrices. For every invariant-factor profile represented in the exhaustive matrix space, it computes the complete conjugacy orbit of a representative and checks exact equality with the profile fibre. Thus both containment directions are checked over the entire 3×3 matrix space.

The exhaustive claim is restricted to dimension three over \(\mathbb F_3\). It is finite regression evidence, not a theorem for larger dimensions or fields and not a new production similarity algorithm.


## Cross-field comparison (G-EP155)

The companion regression enumerates all 512 matrices over F₂ and all 19,683 matrices over F₃, recording invariant-factor profiles and their degree shapes. It compares degree shapes independently of coefficient tuples: the represented degree patterns agree, while polynomial coefficients are interpreted as residues in their own base field. In particular, coefficient 2 occurs in normalized F₃ profiles and cannot occur in F₂ profiles.

This is not a coefficient-wise field identification. The same integer tuple in two profile records does not by itself assert that the corresponding polynomials have the same algebraic behavior, and irreducibility is field-dependent. The test establishes only the stated finite-dimensional comparison over F₂ and F₃.


## Cubic irreducible-factor comparison (G-EP156)

Every monic cubic over a field is the characteristic polynomial of its companion matrix. The regression therefore enumerates all monic cubics over F₂ and F₃, factors each with the exact finite-field factorizer, and multiplies the returned irreducible factors (with multiplicities) back to the original polynomial.

The factorization degree/multiplicity shapes are almost, but not entirely, the same. Both fields admit a triple linear factor, a repeated linear factor times a distinct linear factor, a linear times an irreducible quadratic, and an irreducible cubic. F₃ additionally admits three distinct linear factors; F₂ cannot, because it has only two monic linear irreducibles. The actual monic irreducible inventories are field-dependent. Their counts in degrees one, two, and three are respectively p, (p²−p)/2, and (p³−p)/3.

This is a complete enumeration of monic cubics over the two stated fields, not a claim about higher-degree polynomials or an identification of polynomial coefficients across fields.
