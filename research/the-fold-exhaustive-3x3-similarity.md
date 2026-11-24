# G-EP153: Exhaustive 3×3 similarity-orbit audit over F₂

This milestone exhaustively checks all 512 matrices in \(M_3(\mathbb F_2)\). It uses test-local arithmetic to compute the characteristic polynomial
\[
\chi_A(t)=t^3-\operatorname{tr}(A)t^2+
(c_{12}+c_{13}+c_{23})t-\det(A),
\]
where \(c_{ij}=a_{ii}a_{jj}-a_{ij}a_{ji}\), and compares it with the production profile.

For each matrix, all eight vectors are tested for cyclicity by checking whether \([v,Av,A^2v]\) has nonzero determinant. The result is compared with the profile's one-invariant-factor condition. The test also checks that the product of the reported invariant factors equals the independently computed characteristic polynomial.

Finally, it enumerates all 168 elements of \(GL(3,\mathbb F_2)\). For one representative of each invariant-factor profile, it computes the complete conjugacy orbit \(P^{-1}AP\), then checks exact equality between that orbit and the entire profile fibre among the 512 matrices. This exercises both cyclic and noncyclic operators, including repeated elementary-divisor structure.

The exhaustive claim is restricted to dimension three over \(\mathbb F_2\). It is finite regression evidence for the production rational-canonical profile, not a proof for larger dimensions or fields and not a new production similarity algorithm.
