# G-4f — Arithmetic of the quaternion boundary over imperfect fields

Let k have characteristic two and let G_lambda be the mixed Hopf group
`0 -> mu_2 -> G_lambda -> alpha_4 -> 0` with parameter lambda in k.
Its fppf boundary is
[
\delta_\lambda:k/k^4\longrightarrow \operatorname{Br}(k)[2],
\qquad [a]\longmapsto [Q(a,\lambda)].
]
For lambda nonzero, the quaternion algebra has symbol presentation
[
Q(a,\lambda)\simeq[a\lambda,\lambda)_2.
]
The boundary factors through k/k^2. Its vanishing criterion is
[
\delta_\lambda([a])=0
\quad\Longleftrightarrow\quad
\exists c,d\in k:\ c^2+a d^2+d=\lambda.
]
This equation also constructs the lift torsor explicitly; see
`the-fold-char2-mixed-torsor-models.md`.

## 1. The image

For lambda nonzero, multiplication by lambda is a bijection of the additive
field k. Hence the image is exactly the set of quaternion classes
[
\operatorname{im}(\delta_\lambda)
=\{[b,\lambda)_2:b\in k\}
\subseteq\operatorname{Br}(k)[2].
]
Here `[b,lambda)_2` denotes the characteristic-two symbol algebra generated
by i,j with i^2+i=b, j^2=lambda, and jij^{-1}=i+1. This is a subgroup because
the boundary is a homomorphism of fppf cohomology groups. The formula is an
image description, not a claim that the parameterization by b is injective.

If lambda is a square, every symbol in this image is split, so the boundary
is zero. If lambda is nonzero and nonsquare, the image can be nonzero.

For lambda=0 the extension is split and the boundary is identically zero.

## 2. A nonzero class over a rational function field

Take
[
k=\mathbb F_2(s,t),\qquad \lambda=s,\qquad a=t.
]
Then
[
\delta_s([t])=[st,s)_2.
]
The splitting criterion would require
[
c^2+t d^2+d=s.
]
Multiplying by t and setting y=td gives
[
y^2+y=t(s+c^2).
]
Use the t-adic valuation at infinity, normalized by v(t)=-1, with residue
field F_2(s).

If v(c)<0, then v(s+c^2)=2v(c), so
v(t(s+c^2))=-1+2v(c), an odd negative integer. If v(c)>=0, the residue
of s+c^2 is nonzero: when v(c)>0 it is s, and when v(c)=0 it is
s+\bar c^2, which cannot vanish because s is not a square in F_2(s).
Thus v(t(s+c^2))=-1, again odd and negative.

But for any y with v(y)<0, v(y^2+y)=2v(y) is even and negative; if
v(y)>=0, then v(y^2+y)>=0. The displayed equation is impossible.
Therefore [st,s)_2 is nonzero in Br(k), and [t] is not in the boundary
kernel.

This is an exact valuation proof, not a numerical or symbolic sample.

## 3. Behavior under field extensions

For any extension L/k, the boundary commutes with scalar extension:
[
\delta_{\lambda,L}([a])=
\operatorname{res}_{L/k}(\delta_{\lambda,k}([a])).
]
If lambda becomes a square in L, then every symbol [a lambda,lambda)_2
splits over L, so the entire boundary map over L is zero.

In particular, adjoining sqrt(lambda) kills all these quaternion
obstructions. This is a sufficient splitting extension; it need not be
minimal for an individual class.

For purely transcendental extensions, a nonzero Brauer class remains
nonzero under restriction. Thus the class [st,s)_2 remains nonzero after
adjoining independent transcendental variables to F_2(s,t).

## 4. Exact kernel and image questions still open

The exact kernel over a general imperfect field is
[
\ker\delta_\lambda=
\{[a]\in k/k^2:
\exists c,d\in k,\ c^2+a d^2+d=\lambda\},
]
viewed inside k/k^4 by Frobenius factorization. This criterion is explicit,
but a field-uniform description in terms of valuations, norm groups, or
differential invariants remains open.

Useful next cases:
1. k=F_2(s,t) with lambda=s: classify all a for which the equation has a
   solution, not only the class a=t.
2. Finite purely inseparable extensions adjoining lambda^(1/2^n), and
   extensions that do not make lambda square.
3. One-variable function fields over imperfect coefficient fields, where
   valuations can detect nontrivial symbols.
4. Relate the kernel equation to the norm subgroup for the Artin-Schreier
   extension defined by b^2+b=a lambda, and determine when this gives a
   practical arithmetic classification.

## 5. Scope

This note computes the image description and gives a nonzero rational
function field example. It does not claim a complete classification of the
kernel for F_2(s,t), nor a complete classification over all imperfect fields.


## 6. Exact kernel parameterization for F₂(s,t), lambda=s

The splitting equation is
[
c^2+a d^2+d=s.
]
Since s is not a square in k, d cannot be zero. Put r=d^{-1}. Solving for a gives
[
a=s r^2+r+(cr)^2.
]
Thus the square class of a is [s r²+r]. Conversely, for any r in k×,
choose d=r^{-1}, c=0, and a=s r²+r; then the splitting equation holds.
Therefore
[
\boxed{\ker\delta_s
=\{[s r^2+r]\in k/k^2:r\in k^\times\}.}
]
Equivalently this is the image of the additive polynomial
L_s(r)=s r²+r, modulo k². The parameterization is invariant under changing
a by a square: such a change is absorbed into c² in the splitting equation.
It gives the entire kernel as a subset of k/k², though it does not yet give
a simpler intrinsic description of the image subspace or its quotient.

The class [t] is not in this image, by the valuation obstruction in Section 2.

## 7. G-4h — Coefficient criterion over the square subfield

Put
\[
K=k^2=\mathbb F_2(S,T),\qquad S=s^2,\quad T=t^2,
\]
so that \(K^2=k^4=\mathbb F_2(S^2,T^2)\). Every class in \(k/K\) has a unique expression
\[
[a]=\alpha s+\beta t+\gamma st,\qquad \alpha,\beta,\gamma\in K.
\]
Write \(r=r_0+r_1s+r_2t+r_3st\), with \(r_i\in K\). Since
\[
r^2=r_0^2+S r_1^2+T r_2^2+ST r_3^2\in K,
\]
the coefficient vector of \(sr^2+r\) modulo \(K\) is
\[
(r_1+r^2,\ r_2,\ r_3)
\]
in the basis \(s,t,st\). Therefore \([a]\) belongs to the boundary kernel precisely when there are \(r_0,r_1\in K\) with
\[
\beta=r_2,\quad\gamma=r_3,\quad
\alpha=r_1+r_0^2+S r_1^2+T\beta^2+ST\gamma^2.
\]
The Frobenius map \(K\to K^2\) is onto. Eliminating \(r_0\) gives the one-variable criterion
\[
\boxed{
[a]\in\ker\delta_s
\iff
\exists u\in K:\ 
\alpha+T\beta^2+ST\gamma^2+u+Su^2\in K^2.
}
\]
This is an exact equivalence: the discarded term is \(r_0^2\), and every element of \(K^2\) has a square root in \(K\).

There is also an Artin--Schreier form. Put
\[
A=\alpha+T\beta^2+ST\gamma^2,\qquad q=Su.
\]
Multiplication by \(S\) shows that the criterion is equivalent to
\[
\boxed{\exists q\in K:\quad q^2+q+SA\in S K^2.}
\]
Thus the full kernel membership question is reduced to an Artin--Schreier coset test over \(K=\mathbb F_2(S,T)\). This does not yet evaluate that test in closed form for arbitrary rational functions \(\alpha,\beta,\gamma\); in particular, it is not a claim that the image is a \(K\)-linear subspace.


## 8. G-4i — intrinsic additive quotient for the boundary image

Retain \(K=\mathbb F_2(S,T)=k^2\), with \(S=s^2\), \(T=t^2\). For
\([a]=\alpha s+\beta t+\gamma st\in k/K\), define
\[
A(a)=\alpha+T\beta^2+ST\gamma^2\in K.
\]
The expression is additive in \([a]\). The G-4h coefficient criterion says
\[
[a]\in\ker\delta_s
\iff A(a)\in K^2+L_S(K),\qquad
L_S(u)=u+Su^2.
\]
Consequently the map
\[
\Psi:k/K\longrightarrow K/(K^2+L_S(K)),\qquad
[a]\longmapsto[A(a)]
\]
is a well-defined surjective additive homomorphism: for every \(A\in K\),
\(\Psi([As])=[A]\). Its kernel is exactly \(\ker\delta_s\). The first
isomorphism theorem therefore gives the exact image structure
\[
\boxed{\operatorname{im}(\delta_s)\cong
K/(K^2+\{u+Su^2:u\in K\})}
\]
as additive groups (equivalently, \(\mathbb F_2\)-vector spaces).

Equivalently every image class has a representative symbol
\([AS,s)_2\), with two parameters giving the same class precisely when
their difference lies in \(K^2+L_S(K)\). This is an intrinsic quotient
presentation, not a dimension computation: determining the dimension or a
basis of this quotient remains open. The class \(\delta_s([t])\) corresponds
to the coset of \(T\), which is nonzero by the valuation argument in §2.


## 9. G-4j — infinite-dimensionality of the quaternion-boundary image

Let
\[
Q=K/(K^2+L_S(K)),\qquad K=\mathbb F_2(S,T),\quad
L_S(u)=u+Su^2.
\]
Use the valuation at \(T=\infty\), whose residue field is
\(\kappa=\mathbb F_2(S)\). Every element of the denominator with a pole
at infinity has even pole order. To see this, write it as
\[
z^2+u+Su^2.
\]
If \(u\) has pole order \(n>0\), then \(Su^2\) has pole order \(2n\),
strictly larger than the pole order of \(u\). The two even-order terms
\(z^2\) and \(Su^2\), if they have equal pole order, cannot cancel:
cancellation of leading coefficients would give
\(S=(\bar z/\bar u)^2\) in \(\kappa\), impossible because \(S\) is
not a square in \(\mathbb F_2(S)\). If their pole orders differ, the
larger even order survives. If \(u\) has no pole, then only \(z^2\)
can contribute a pole, and its order is even. Thus every nonzero
denominator element with a pole has even pole order.

Every nonzero finite \(\mathbb F_2\)-linear combination of
\[
T,\ T^3,\ T^5,\ T^7,\ldots
\]
has odd pole order at infinity. No such combination belongs to the
denominator. Their classes are therefore linearly independent in \(Q\),
so
\[
\boxed{\dim_{\mathbb F_2}Q=\infty.}
\]
By G-4i this proves
\[
\boxed{\dim_{\mathbb F_2}\operatorname{im}(\delta_s)=\infty.}
\]
More explicitly, the independent image classes are represented by
\([S T^{2n+1},s)_2\), for \(n\ge0\), since they correspond under the
G-4i quotient isomorphism to \([T^{2n+1}]\in Q\). Equivalently they are
the boundary values \(\delta_s([sT^{2n+1}])\). This proves infinite
rank, not a basis or a complete normal form for the quotient.


## 10. G-4k — exact countable dimension and finite-place independent family

The valuation argument of G-4j applies at every place \(v_a=v_{T-a}\),
for \(a\in\mathbb F_2(S)\). The residue field is
\(\mathbb F_2(S)\), in which \(S\) is not a square. For a denominator
element \(d=z^2+u+Su^2\), if \(u\) has a pole of order \(m>0\) at
\(v_a\), then \(Su^2\) has pole order \(2m\), strictly exceeding
the pole order \(m\) of \(u\). Its leading term cannot cancel with
that of \(z^2\), since such cancellation would make \(S\) a square
in the residue field. If \(u\) is regular, any pole comes from \(z^2\)
and has even order. Hence every denominator element has either no pole
or an even pole order at each \(v_a\).

It follows that
\[
\left\{(T-a)^{-(2n+1)}:
a\in\mathbb F_2(S),\ n\ge0\right\}
\]
is linearly independent in \(Q=K/(K^2+L_S(K))\): in a finite
nontrivial linear combination, choose a place \(v_a\) that occurs;
the largest odd pole order at that place survives, whereas all other
terms are regular there. It cannot equal a denominator element.

The indexing set is countably infinite, and \(K=\mathbb F_2(S,T)\)
is countable. Therefore
\[
\boxed{\dim_{\mathbb F_2}Q=\aleph_0
=\dim_{\mathbb F_2}\operatorname{im}(\delta_s).}
\]
Under G-4i the corresponding independent boundary representatives are
\[
\left[S(T-a)^{-(2n+1)},s\right)_2.
\]
This establishes the exact vector-space dimension, but does not give a
canonical basis or a reduction algorithm for arbitrary rational functions.


## 11. G-4l — separable-place parity obstruction

Let \(F=\mathbb F_2(S)\), \(K=F(T)\), and let \(P\in F[T]\) be monic,
irreducible, and separable. Its residue field
\(E_P=F[T]/(P)\) is finite separable over F. Since \(S\) is nonsquare
in F, adjoining \(\sqrt S\) is a nontrivial purely inseparable
extension. A finite separable extension cannot contain this element;
therefore S remains nonsquare in \(E_P\).

For \(d=z^2+u+Su^2\), consider the P-adic valuation. If u has a pole
of order m, then \(Su^2\) has pole order 2m; if z has a pole of order
n, then \(z^2\) has pole order 2n. If these orders tie, cancellation
of their leading coefficients would imply that S is a square in
\(E_P\), impossible. If they do not tie, the larger even pole order
survives. If u is regular, any pole comes from z² and is even. Thus
every denominator element has either no pole or even pole order at P.

Choose an F2-basis of E_P and polynomial representatives r(T) of
degree less than deg(P). For all such representatives and all n≥0,
the classes
\[
r(T)/P^{2n+1}
\]
are jointly linearly independent in Q, as P ranges over the monic
separable irreducibles. For a finite relation, choose a P occurring
in it and the largest n with nonzero coefficient at that P. The
corresponding residue coefficient is nonzero by basis independence,
so the relation has an odd pole order at P. Terms indexed by other
irreducibles are regular at P, and denominator elements cannot have
that odd pole order.

This refines the rational-place family in G-4k. It is still an
independent family, not a complete basis or a reduction algorithm
for Q.
