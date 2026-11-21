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
