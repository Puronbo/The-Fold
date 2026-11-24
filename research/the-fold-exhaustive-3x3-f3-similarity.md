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


## Quartic irreducible-factor comparison (G-EP157)

The regression exhausts all p⁴ monic quartics over F_p for p in {2, 3}. Each polynomial is factored, and the returned monic irreducible factors with multiplicities are multiplied back to verify exact reconstruction. The test also checks the exact irreducible inventory sizes in degrees one through four: p, (p²−p)/2, (p³−p)/3, and (p⁴−p²)/4.

A concrete field-dependent quartic pattern is the presence of all three distinct monic linear irreducibles with one of them repeated. It occurs over F₃, which has three elements and hence three monic linear irreducibles, but not over F₂, which has only two. This result is exhaustive for monic quartics over these two fields only.


## Quartic pattern growth with field size (G-EP158)

This regression exhausts every monic quartic over F₂, F₃, and F₅. For each polynomial it reconstructs the input from the factorizer's monic irreducible factors and multiplicities, and checks the irreducible inventory counts in degrees one through four.

The observed factorization-pattern catalog strictly grows across these fields. Over F₃, three distinct linear irreducibles can occur with one repeated, and two distinct irreducible quadratics can occur as separate factors; neither pattern is possible over F₂, which has only two monic linear irreducibles and only one monic irreducible quadratic. Over F₅, four distinct linear factors become possible. The assertions concern degree/multiplicity patterns, not coefficient-wise identification of polynomials between fields, and the exhaustive scope is limited to the three fields and degree four.


## Quartic pattern stabilization (G-EP159)

The regression exhausts all monic quartics over F₂, F₃, F₅, and F₇. It verifies factor reconstruction and the irreducible inventory counts in degrees one through four. The degree/multiplicity pattern catalogue grows strictly from F₂ to F₃ and from F₃ to F₅, then the catalogues over F₅ and F₇ agree exactly.

This stabilization concerns only degree/multiplicity shapes for degree-four polynomials. The actual irreducible polynomial inventories differ between F₅ and F₇, as expected from their different coefficient fields. Thus it is not a coefficient-wise or factor-identity equivalence and does not establish stabilization for degrees above four.


## Quintic factor-pattern threshold experiment (G-EP160)

This regression exhausts all monic quintics over F₂, F₃, F₅, and F₇. For every polynomial, it verifies exact reconstruction from monic irreducible factors and multiplicities, and checks the exact irreducible inventory counts in degrees one through five.

The degree/multiplicity pattern catalogues grow from F₂ to F₃ and from F₃ to F₅, then agree over F₅ and F₇. The actual irreducible polynomial inventories remain field-dependent. This is evidence for stabilization by field size five in degree five, not a general theorem for all degrees or all finite fields.


## Sextic factor-pattern threshold experiment (G-EP161)

The test exhausts all monic sextics over F₂, F₃, and F₇: 64, 729, and 117,649 polynomials respectively. It reconstructs every input from the factorizer output and checks the exact irreducible inventory counts in degrees one through six.

The complete degree/multiplicity catalogue contains 34 shapes and is attained over F₇; the catalogues over F₂ and F₃ are strict subsets. The limiting shape consists of six distinct linear factors, requiring at least six distinct monic linear irreducibles. Thus the smallest prime field that can realize the complete degree-six shape catalogue is F₇. This is a finite degree-six result; it does not establish a general threshold formula for arbitrary degrees.


## F₅ sextic comparison (G-EP162)

G-EP162 exhausts all 15,625 monic sextics over F₅. It verifies exact reconstruction and the degree-one-through-six irreducible inventory counts. The shape with six distinct linear factors is absent, while examples with five distinct linear factors (one repeated) and four distinct linears plus an irreducible quadratic occur. This supplies the missing intermediate prime-field comparison between F₃ and F₇ in G-EP161; it remains a finite degree-six experiment.


## Polynomial factor API edge cases (G-EP163)

The regression covers scalar-unit reporting for nonmonic inputs, coefficient reduction modulo the prime, nonzero constants (empty nonconstant factor list), rejection of empty and zero polynomials, and rejection of composite moduli. It also checks the characteristic-three identity (x^3+1=(x+1)^3), including the reported multiplicity three. This validates selected API contracts and edge cases; it is not a proof of factorization correctness for arbitrary degrees.


## Exhaustive irreducibility cross-check (G-EP164)

For every monic polynomial of degrees one through four over F₂, F₃, and F₅ (930 inputs total), the test compares the Rabin-style irreducibility predicate with an independently observed factorizer criterion: exactly one factor, equal to the original monic polynomial, with multiplicity one. Agreement is finite-domain regression evidence across these fields and degrees, not a universal proof.


## Quintic irreducibility cross-check (G-EP165)

The same predicate-versus-factorizer comparison is extended to all 3,400 monic quintics over F₂, F₃, and F₅. Together with G-EP164, this gives exhaustive cross-check coverage for every monic polynomial of degrees one through five over those three prime fields. It remains a finite regression result.


## Sextic irreducibility cross-check (G-EP166)

G-EP166 exhaustively compares the irreducibility predicate with the factorizer's one-factor criterion for all 64 monic sextics over F₂ and all 729 over F₃. This extends the degree-one-through-five comparison from G-EP164 and G-EP165 to degree six over the two smaller prime fields. It is finite regression evidence, not a general proof.


## Degree-seven irreducibility cross-check (G-EP167)

G-EP167 compares the irreducibility predicate with factorizer output for every monic degree-seven polynomial over F₂ (128 inputs) and F₃ (2,187 inputs). This extends the finite comparison through degree seven over these two fields. It is regression evidence over the stated finite domain, not a universal proof.


## Degree-eight irreducibility cross-check (G-EP168)

G-EP168 compares the irreducibility predicate with factorizer output for every monic degree-eight polynomial over F₂ (256 inputs) and F₃ (6,561 inputs). This extends the finite-domain comparison through degree eight over these fields; it is regression evidence, not a universal proof.
