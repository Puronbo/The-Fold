# UF-017 — The Fold discriminant and spectral geometry

## 1. Setup

Let A=Q{p,z}, q=(p²-z²)/2, and R=A[x,y]/(x²+y²-p, x²y²-q). Use the ordered A-basis (1,x,y,xy,x²,x²y,x³,x³y). Define B(a,b)=Tr_R/A(ab).

## 2. Exact trace matrix

\[
B=\begin{pmatrix}
8&0&0&0&4p&0&0&0\\
0&4p&0&0&0&0&4p^2-8q&0\\
0&0&4p&0&0&8q&0&0\\
0&0&0&8q&0&0&0&4pq\\
4p&0&0&0&4p^2-8q&0&0&0\\
0&0&8q&0&0&4pq&0&0\\
0&4p^2-8q&0&0&0&0&-8pq+4p(p^2-q)&0\\
0&0&0&4pq&0&0&0&4p^2q-8q^2
\end{pmatrix}.
\]
Its entries are B_ij=Tr(M_bi M_bj).

## 3. Discriminant theorem

**Theorem UF-017.1.** In this basis,
\[
\boxed{\det B=2^{16}q^4(p^2-4q)^4.}
\]
The discriminant ideal is generated, up to a unit, by [q(p²−4q)]⁴. Substituting q=(p²−z²)/2 gives
\[
65536\left(\frac{p^2-z^2}{2}\right)^4(2z^2-p^2)^4.
\]

The reduced branch components are q=0 and p²−4q=0. Their source preimages are x²y²=0 and (x²−y²)²=0, respectively: the four D4 reflection lines x=0, y=0, x−y=0, x+y=0.

The exponent four is the exponent in this rank-eight trace determinant; it is not the multiplicity of each individual reflection line in the source Jacobian. A basis change multiplies the determinant by the square of a unit.

## 4. Quotient Jacobian

For p=x²+y² and q=x²y²,
\[
J=\det\frac{\partial(p,q)}{\partial(x,y)}
=4xy(x^2-y^2),\qquad J^2=16q(p^2-4q).
\]
Thus the branch divisor is exactly the image of the reflection arrangement, and in fact, in this basis, det(B)=J⁸ exactly after pullback: 2¹⁶q⁴(p²−4q)⁴=[16q(p²−4q)]⁴.

## 5. Spectral meaning and limitations

Away from the discriminant the finite algebra is étale and its geometric fiber consists of eight distinct points, the generic D4 orbit. The trace pairing is then nondegenerate. On the discriminant the trace form degenerates and the fiber is ramified or nonreduced.

The trace determinant records the degeneracy locus, not the full nilpotent/Jordan structure. That requires the specialized multiplication matrices or the local algebra. No claim about primes or eigenprimes follows from this calculation.

## 6. Verification

The script tools/fold_discriminant_trace.py constructs the multiplication matrices over Q[p,q], forms all 64 trace-pairing entries, computes the determinant, and checks the Jacobian identity. It requires SymPy.

## 7. Follow-up problems

1. Determine local algebra lengths and Jordan types along each branch component and at their intersection.
2. Compare discriminant valuation with ramification indices on generic points of each branch component.
3. Extend the trace-discriminant calculation to other finite reflection groups and non-free invariant extensions.
4. Test which combinations of trace form, multiplication spectrum, and local algebra distinguish analytically inequivalent Fold singularities.
