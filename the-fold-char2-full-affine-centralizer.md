# UF-058 — The full affine centralizer of the seven-dimensional subgroup

## 1. Setup

Work in characteristic two over a commutative base algebra. Let
[
C=k[x,z]/(x^4,z^2)
]
and let (U) be the seven-dimensional subgroup whose elements are
[
egin{aligned}
u(x)&=x+Ax^2+Bx^3+Cxz+Dx^2z+Ex^3z,\\
u(z)&=z+Axz+Gx^3+(B+G)x^2z+Jx^3z.
end{aligned}
]
The coefficients (A,B,C,D,E,G,J) are arbitrary base-algebra parameters.

Consider the full affine automorphism family
[
g(x)=c+ax+bz,qquad g(z)=d+hx+iz,
]
with
[
c^4=d^2=h^2=0,qquad Delta=ai-bhin R^	imes.
]
The determinant-open automorphism scheme has (a) a unit: since (bh) is nilpotent and (ai=Delta+bh) in characteristic two, (ai) is a unit.

## 2. Theorem UF-058

**The full determinant-open affine subgroup centralizes (U):**
[
oxed{gug^{-1}=uquad	ext{for every affine }g	ext{ above and every }uin U.}
]

In particular, the mixed coefficient product (ch) does not occur in any of the sixteen target coefficient functions on this affine conjugation family. This is an exact group-scheme statement over the coefficient algebra, not merely a statement about field-valued points.

## 3. Proof by factorization

Separate the translation and linear parts. Write (g=T_{(c,d)}circ M), where
[
M=egin{pmatrix}a&b\\h&iend{pmatrix}.
]
Since (a) is a unit, in characteristic two there is an exact factorization
[
egin{pmatrix}a&b\\h&iend{pmatrix}
=
egin{pmatrix}1&0\\h/a&1end{pmatrix}
egin{pmatrix}a&b\\0&i+hb/aend{pmatrix}.
]
The lower-right entry (j=i+hb/a) is a unit because (aj=ai+bh=Delta).

Each factor centralizes (U):

1. **Translations and lower-triangular affine maps.** These are precisely contained in the family of UF-057, which was checked by exact substitution. Thus (T_{(c,d)}) and the lower-triangular factor centralize (U).
2. **Upper-triangular linear maps.** Let
   [
   v(x)=ax+bz,qquad v(z)=jz,
   ]
   with (a,j) units. Its inverse is
   [
   v^{-1}(x)=a^{-1}x+rac{b}{aj}z,qquad v^{-1}(z)=j^{-1}z.
   ]
   Substituting these expressions into the two coordinate polynomials for (u), then applying (v), and reducing in (k[x,z]/(x^4,z^2)) in characteristic two gives
   [
   egin{aligned}
   (vuv^{-1})(x)&=x+Ax^2+Bx^3+Cxz+Dx^2z+Ex^3z,\\
   (vuv^{-1})(z)&=z+Axz+Gx^3+(B+G)x^2z+Jx^3z.
   end{aligned}
   ]
   These are exactly (u(x)) and (u(z)). The cancellations use (2=0), (z^2=0), and (x^4=0); no restriction on (A,B,C,D,E,G,J) is imposed.

The centralizer of a subgroup is closed under composition. Therefore the product of the translation, lower-triangular, and upper-triangular factors centralizes (U), proving the theorem for every affine (g) in the determinant-open family.

## 4. Consequences and scope

- The off-diagonal coefficient (b) in (g(x)) does not break the centralizer phenomenon.
- No affine conjugate of (U) in this full affine family supplies a nontrivial coefficient direction. In particular, (ch) is absent from all target-coordinate variations on this family.
- This does **not** settle the full universal conjugation problem: ambient automorphisms with quadratic and cubic terms remain outside the affine subgroup.
- It does not compute the scheme-theoretic conjugacy-image kernel or its largest Hopf ideal, and it does not prove equality of the minimal normal closure with the second-Frobenius candidate.

## 5. Reproducibility boundary

The proof reduces the general affine case to the triangular calculation UF-057 and the upper-triangular substitution displayed above. All identities are polynomial identities over arbitrary characteristic-two coefficient algebras subject to the stated nilpotence and unit conditions. A finite symbolic check can verify the upper-triangular expansion, but the factorization is the structural proof.

**Next problem UF-059:** allow the first nonlinear ambient coefficients in (g), beginning with quadratic perturbations of (g(x)) and (g(z)), and determine the first nonlinear stratum on which conjugation ceases to be trivial. Continue to track all sixteen target coefficient functions separately from the orbit-image ideal and its Hopf core.
