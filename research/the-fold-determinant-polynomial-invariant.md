# G-EP149: Homogeneous determinant-polynomial covariance for 2×2 pencils

For a 2×2 pencil pair, compute the homogeneous quadratic
\[
\det(xQ+yK)=c_{20}x^2+c_{11}xy+c_{02}y^2
\]
using a test-local coefficient formula. If \(Q'=SQT\) and \(K'=SKT\) for common invertible constant matrices, then
\[
\det(xQ'+yK')=\det(S)\det(T)\det(xQ+yK).
\]
Thus the coefficient triple is a projective invariant of constant strict equivalence.

Over F₂, F₃, and F₅, a positive control applies nonidentity invertible left/right shears to a 2×2 pencil. The existing production strict-equivalence auditor verifies both matrix identities, while the test-local determinant calculation checks the exact predicted scalar covariance.

A negative control compares \((I_2,I_2)\) with \((I_2,K_*)\). Over F₂, \(K_*\) is the invertible companion matrix \(\begin{pmatrix}0&1\\1&1\end{pmatrix}\); over F₃ and F₅ it is \(\operatorname{diag}(1,2)\). Both coefficient matrices in both pairs are invertible, so their individual coefficient ranks agree. Their homogeneous determinant coefficient triples are not proportional: the leading \(x^2\) coefficient is one in both, but another coefficient differs. Since any common strict-equivalence transforms can only multiply the whole polynomial by one nonzero scalar, no such transforms can relate these two pairs.

This is an exact invariant and obstruction for the stated 2×2 finite-field fixtures. It does not claim that the determinant polynomial is a complete invariant for strict equivalence, nor does it provide a general witness-discovery or classification algorithm.
