# UF-015 — Complete D4 Representation Decomposition of the Analytic Cone

## Research question

UF-014 classified all scalar semi-invariants for the four one-dimensional characters of \(D_4\). The remaining irreducible representation is the two-dimensional representation \(E\). This note decomposes the entire convergent analytic coordinate ring of

\[
X=\{z^2=x^4+y^4\}
\]

as a module over its invariant analytic ring, gives explicit covariant generators, and proves that the list is complete.

Throughout, \(D_4\) acts by

\[
r(x,y,z)=(-y,x,z),\qquad s(x,y,z)=(y,x,z),
\]

and \(p=x^2+y^2\), \(q=x^2y^2\).

## 1. The invariant coefficient ring

Set

\[
A=\mathbb K\{p,z\},\qquad \mathbb K=\mathbb R\text{ or }\mathbb C.
\]

The signed-permutation action on \((x,y)\) has invariant analytic ring

\[
\mathbb K\{x,y\}^{D_4}=\mathbb K\{p,q\}.
\]

On the cone,

\[
z^2=p^2-2q,\qquad q=(p^2-z^2)/2.
\]

Consequently,

\[
\boxed{\mathcal O_{X,0}^{D_4}=A.}
\]

## 2. The eight-element analytic module basis

The reflection-group invariant theorem says that \(\mathbb K\{x,y\}\) is free of rank \(|D_4|=8\) over \(\mathbb K\{p,q\}\). A homogeneous basis is

\[
\mathcal B=
\{1,\ x,\ y,\ xy,\ x^2-y^2,\ xy^2,\ x^2y,\ xy(x^2-y^2)\}.
\]

One direct way to see the basis degrees is to reduce modulo \((p,q)\). Since \(p=x^2+y^2=0\) and \(q=x^2y^2=0\), one gets \(y^2=-x^2\) and \(x^4=0\). The quotient has basis

\[
1,\ x,\ y,\ xy,\ x^2,\ x^2y,\ x^3,\ x^3y,
\]

which is exactly the image of \(\mathcal B\), up to nonzero scalar factors and order. The degrees are \(0,1,1,2,2,3,3,4\), the \(D_4\) coinvariant degrees.

The cone ring is obtained by the analytic base change \(q=(p^2-z^2)/2\). Thus the same eight elements form a free \(A\)-basis of \(\mathcal O_{X,0}\):

\[
\boxed{\mathcal O_{X,0}=\bigoplus_{b\in\mathcal B} A\,b.}
\]

In particular, the quotient map \(X\to X/D_4\) is finite flat of degree eight at the level of these analytic local rings.

## 3. The four scalar character summands

The four scalar generators are exactly those established in UF-014:

\[
\Delta_{++}=1,\quad
\Delta_{-+}=xy,\quad
\Delta_{--}=x^2-y^2,\quad
\Delta_{+-}=xy(x^2-y^2).
\]

Their modules are

\[
A,\quad Axy,\quad A(x^2-y^2),\quad Axy(x^2-y^2).
\]

These are four of the eight \(A\)-basis elements.

## 4. The two-dimensional covariants

Let

\[
\rho(r)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\rho(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Define

\[
V_1=\begin{pmatrix}x\\y\end{pmatrix},
\qquad
V_3=\begin{pmatrix}xy^2\\x^2y\end{pmatrix}.
\]

A direct substitution gives, for both \(i=1,3\),

\[
V_i(rq)=\rho(r)V_i(q),\qquad
V_i(sq)=\rho(s)V_i(q).
\]

Thus each is an \(E\)-valued analytic covariant. The two copies are independent over \(A\): their four scalar components \(x,y,xy^2,x^2y\) are distinct members of the free basis \(\mathcal B\).

Every \(E\)-valued analytic covariant \(F=(f_1,f_2)^T\), satisfying \(F(gq)=\rho(g)F(q)\), therefore has a unique expression

\[
\boxed{F=A_1(p,z)V_1+A_3(p,z)V_3}
\]

with \(A_1,A_3\in A\).

This proves not only that the two covariants exist, but that they generate all analytic covariants of this representation.

## 5. Main theorem

### Theorem UF-015.1 — Complete analytic \(D_4\)-module decomposition

As an \(A=\mathbb K\{p,z\}\)-module with \(D_4\)-action,

\[
\boxed{
\mathcal O_{X,0}
\cong
A\otimes
\left(
\mathbf 1\oplus\chi_{-+}\oplus\chi_{--}\oplus\chi_{+-}
\oplus E\oplus E
\right).
}
\]

Equivalently, its eight explicit \(A\)-basis elements are

\[
\boxed{
1,\ xy,\ x^2-y^2,\ xy(x^2-y^2),\
x,\ y,\ xy^2,\ x^2y.
}
\]

The scalar character summands are precisely UF-014. The remaining four basis elements form two copies of the unique two-dimensional irreducible representation. No additional analytic representation types or covariant generators occur.

The decomposition is unique because the displayed elements are an \(A\)-basis. It is a decomposition of modules/representations, not a decomposition of the ring as a product: multiplication couples the summands and remains subject to \(z^2=x^4+y^4\).

## 6. Character and Hilbert-series check

Assign weights \(\deg x=\deg y=1\), \(\deg z=\deg p=2\). Since \(A\) has Hilbert series \(1/(1-t^2)^2\), the eight basis degrees give

\[
H_{\mathcal O_X}(t)
=\frac{1+2t+2t^2+2t^3+t^4}{(1-t^2)^2}.
\]

The numerator factors as

\[
1+2t+2t^2+2t^3+t^4
=(1+t)(1+t+t^2+t^3).
\]

This agrees with the hypersurface Hilbert series

\[
\frac{1-t^4}{(1-t)^2(1-t^2)}
=\frac{1+t^2}{(1-t)^2}.
\]

The two-dimensional isotypic component has \(A\)-basis degrees \(1,1,3,3\), hence Hilbert series

\[
H_E(t)=\frac{2t+2t^3}{(1-t^2)^2}.
\]

As a representation, it consists of two copies of \(E\), not four copies: each copy has two scalar components.

## 7. Scope and the next algebra problem

UF-015 completes the additive analytic representation decomposition. It does **not** yet give a minimal multiplication table or a presentation of the invariant algebra action by structure constants. Those are the natural next tasks:

1. Compute all products of the eight basis elements and reduce them uniquely to \(A\)-linear combinations of the basis.
2. Extract a minimal presentation of \(\mathcal O_{X,0}\) as an \(A\)-algebra, including the cone relation.
3. Determine the multiplication maps between the four scalar characters and the two \(E\)-covariant copies.
4. Extend the construction to other finite reflection groups and to non-reflection symmetry actions where freeness can fail.

The first task is algorithmic and can be completed exactly; the fourth is a broader generalization problem.

## 8. UF-015 conclusions

- The full analytic coordinate ring is free of rank eight over the invariant analytic ring.
- The four scalar character modules are the UF-014 modules.
- The two-dimensional representation occurs with multiplicity two.
- Explicit covariant generators are \(V_1=(x,y)\) and \(V_3=(xy^2,x^2y)\).
- Every analytic \(E\)-covariant is a unique invariant-analytic linear combination of these two.
- The decomposition is complete for convergent real- or complex-analytic germs at the cone vertex.

**Conclusion.** The representation-theoretic decomposition of the entire analytic coordinate ring of the original \(D_4\)-symmetric cone is now explicit and complete. The next unresolved algebraic layer is its multiplication structure, not the existence of further representation generators.
