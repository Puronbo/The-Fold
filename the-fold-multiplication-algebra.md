# UF-016 — Complete Multiplication Algebra of the Fold

## 1. Objective

UF-015 decomposed the analytic coordinate ring of the cone
\[
X:\ z^2=x^4+y^4
\]
as a free rank-eight module over its invariant analytic ring. UF-016 determines its multiplication structure exactly.

Put
\[
p=x^2+y^2,\qquad q=x^2y^2=(p^2-z^2)/2,\qquad A=\mathbb K\{p,z\}.
\]
Then the local analytic coordinate algebra has the presentation
\[
\boxed{R\cong A\{x,y\}/(x^2+y^2-p,\ x^2y^2-q).}
\]
Equivalently, using polynomial notation for the finite free algebra over the local coefficient ring, \(R\cong A[x,y]/(...)\). The two relations are a complete intersection and define the eight-point generic D4 orbit fiber.

## 2. A convenient multiplication basis

Use the ordered \(A\)-basis
\[
\mathcal B=(1,x,y,xy,x^2,x^2y,x^3,x^3y).
\]
The reduction rules are
\[
y^2=p-x^2,\qquad x^4=px^2-q.
\]
They reduce every monomial uniquely to an A-linear combination of the eight basis elements. Uniqueness follows from the free rank-eight result in UF-015.

## 3. Exact multiplication operators

Let \(M_x,M_y\) be multiplication by x and y. Their columns are the coordinates of the products with the corresponding ordered basis element. In the ordered basis above,

\[
M_x=
\begin{pmatrix}
0&0&0&0&0&0&-q&0\\
1&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&-q\\
0&0&1&0&0&0&0&0\\
0&1&0&0&0&0&p&0\\
0&0&0&1&0&0&0&p\\
0&0&0&0&1&0&0&0\\
0&0&0&0&0&1&0&0
\end{pmatrix}
\]

and

\[
M_y=
\begin{pmatrix}
0&0&p&0&0&q&0&0\\
0&0&0&p&0&0&0&q\\
1&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&-1&0&0&0&0&0\\
0&0&0&0&1&0&0&0\\
0&0&0&-1&0&0&0&0\\
0&0&0&0&0&0&1&0
\end{pmatrix}.
\]

The column convention is \(M_x e_j=[x e_j]_{\mathcal B}\), and likewise for \(M_y\). In particular, the table can be read directly as
\[
\begin{array}{c|cc}
b&xb&yb\\\hline
1&x&y\\
x&x^2&xy\\
y&xy&p-x^2\\
xy&x^2y&px-x^3\\
x^2&x^3&x^2y\\
x^2y&x^3y&q\\
x^3&px^2-q&x^3y\\
x^3y&px^2y-qy&qx
\end{array}
\]

## 4. Algebra relations and completeness

The matrices satisfy
\[
\boxed{M_xM_y=M_yM_x,}
\]
\[
\boxed{M_x^2+M_y^2=pI_8,}
\]
\[
\boxed{M_x^2M_y^2=qI_8.}
\]
They also satisfy
\[
M_x^4-pM_x^2+qI_8=0.
\]

These relations are exactly the defining relations of the finite free A-algebra. Conversely, every product of basis elements is obtained by applying a word in \(M_x,M_y\) to the unit vector \(e_1\). Therefore the two multiplication operators determine the entire multiplication table, all structure constants, and the complete A-algebra.

The multiplication representation is faithful: if an element acts as zero by multiplication, applying it to the unit gives that element itself, hence it is zero.

## 5. Character multiplication

For one-dimensional characters, multiplication obeys the group law:
\[
R_\chi R_\psi\subseteq R_{\chi\psi}.
\]
The character group is \(C_2\times C_2\). The covariant component E obeys the ordinary tensor-product rules
\[
E\otimes\chi\cong E
\]
for every one-dimensional character, and
\[
E\otimes E\cong
\mathbf1\oplus\chi_{-+}\oplus\chi_{--}\oplus\chi_{+-}.
\]
These representation rules constrain the multiplication maps, while the matrices above determine their exact coefficients in A.

## 6. Spectral interpretation: a careful distinction

At a fixed point \((p,z)\) of the quotient, the matrices specialize to ordinary \(8\times8\) commuting matrices. Their simultaneous eigenvalues describe the coordinate pairs \((x,y)\) in the corresponding fiber, counted with algebraic multiplicity.

The characteristic polynomial of \(M_x\) is
\[
\det(TI-M_x)=(T^2-x^2)(T^2-y^2)
=T^4-pT^2+q.
\]
Likewise,
\[
\det(TI-M_y)=T^4-pT^2+q.
\]
The joint eigenvalue pairs satisfy
\[
X^2+Y^2=p,\qquad X^2Y^2=q.
\]
Thus the joint spectrum reconstructs the D4 orbit fiber. At the singular vertex the fiber is nonreduced; repeated eigenvalues and failure of simultaneous diagonalizability carry information about the singularity. The eigenvalue interpretation is therefore exact on the generic fiber, while the scheme-theoretic algebra is essential at the singular fiber.

This is a precise spectral statement. It does not imply that the eigenvalues are prime numbers or that an independent prime-number theorem follows.

## 7. Theorem UF-016.1

**The complete multiplication algebra theorem.** The analytic coordinate ring R is a free rank-eight A-module with ordered basis \(\mathcal B\). Its multiplication is completely and faithfully represented by the commuting operators \(M_x,M_y\) above. These satisfy the three defining scalar relations and generate every multiplication map of R.

Consequently, the entire algebraic structure is determined by two commuting matrices over the invariant analytic ring.

## 8. Next research questions

1. Compute the discriminant of the finite map \(X\to X/D_4\) from the trace pairing and compare it with the reflection arrangement.
2. Analyze the nilpotent/Jordan structure of the specialized multiplication operators at the cone vertex and along the quotient discriminant.
3. Determine whether the joint spectral scheme gives a useful invariant for comparing different Fold singularities.
4. Extend the multiplication-operator construction to other finite symmetry groups, including cases where the invariant-ring extension is not free.

The exact multiplication algebra is established here. The discriminant and broader spectral classification are subsequent problems, not assumed conclusions.
