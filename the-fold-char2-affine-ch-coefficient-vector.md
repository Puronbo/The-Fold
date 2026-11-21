# UF-059 — The mixed ch coefficient across the affine target coordinates

## 1. The decisive affine slice

Work in characteristic two with
[
C=k[x,z]/(x^4,z^2).
]
Let the seven-parameter subgroup U be
[
egin{aligned}
u(x)&=x+Ax^2+Bx^3+Cxz+Dx^2z+Ex^3z,\\
u(z)&=z+Axz+Gx^3+(B+G)x^2z+Jx^3z.
end{aligned}
]
Consider the affine family
[
g(x)=x+c+bz,qquad g(z)=z+hx,
]
where (c^4=h^2=0), and b is unrestricted. Its determinant is (1+bh), which is a unit because ((bh)^2=0). The inverse is
[
g^{-1}(x)=(1+bh)(x+c+bz),qquad
g^{-1}(z)=(1+bh)(h(x+c)+z).
]
Indeed, in characteristic two, ((1+bh)^2=1).

## 2. Composition convention

For algebra automorphisms represented by their images of x and z, compute the conjugate in the order
[
xlongmapsto g^{-1}(x)longmapsto u(g^{-1}(x))longmapsto
g(u(g^{-1}(x))),
]
and likewise for z. This order is essential; it corrects the reversed-substitution error documented in UF-058.

Write the conjugate as
[
egin{aligned}
X'&=c'+a'x+b'z+alpha'x^2+eta'x^3+gamma'xz+delta'x^2z+epsilon'x^3z,\\
Z'&=d'+h'x+i'z+phi'x^2+psi'x^3+eta'xz+	heta'x^2z+kappa'x^3z.
end{aligned}
]
There are sixteen target coefficient functions: fourteen nonconstant coefficients and the two constants.

## 3. Theorem UF-059 — exact ch coefficient vector

Expand the correctly ordered conjugation in the coefficient algebra
[
k[b,A,B,C,D,E,G,J,c,h]/(c^4,h^2)
]
and reduce the coordinate polynomials modulo (x^4=z^2=0). The coefficient of the monomial (ch) in the sixteen target coefficient functions is as follows:
[
egin{array}{c|c@{qquad}c|c}
a'&Ab+C & b'&Ab^2+Cb\\
alpha'&Bb+Gb^2 & eta'&E+Jb\\
delta'&Eb+Jb^2 & h'&A\\
i'&Ab+C & phi'&B+Gb\\
psi'&J & 	heta'&E+Jb
end{array}
]
The coefficient of (ch) is zero in
[
c',d',gamma',epsilon',eta',kappa'.
]
Thus ten of the sixteen target coefficient functions detect the mixed class on this affine slice, while six do not.

In particular, setting b=0 gives the especially simple exact witness
[
h'=Ach.
]
For the U-element with only A nonzero, the complete conjugate is
[
egin{aligned}
X'&=x+Ax^2+Ac^2,\\
Z'&=z+Axz+Acz+Ach,x+Ac^2h.
end{aligned}
]
This independently confirms the coefficient (A) of ch in h'.

## 4. Proof method and exactness

The inverse displayed in Section 1 is substituted first. Then u is applied to the resulting polynomials by replacing x and z with u(x) and u(z). Finally g is applied by replacing x with x+c+bz and z with z+hx. All calculations are carried out in characteristic two and reduced by
[
x^4=z^2=c^4=h^2=0.
]
Extracting the coefficient of (x^r z^s) in each output and then the coefficient of (ch) gives the table in Section 3. The table is an exact polynomial identity over the parameter ring, not an approximation modulo higher nilradical powers.

The computation is restricted to the affine slice (a=i=1,d=0). It proves that ch is detected by the full affine conjugation family, but it does not yet give every coefficient of the full determinant-open affine coaction.

## 5. Consequences and next problem

1. The mixed class ch is genuinely visible in the conjugacy family; it is not killed by the triangular restriction.
2. The detection is distributed across ten target coefficients, not only the nilpotent output h'.
3. The coefficient table is not itself the scheme-theoretic orbit-image ideal. The coefficient module, its annihilator, the kernel of the universal conjugation pullback, and the largest Hopf ideal contained in that kernel are distinct objects.
4. UF-056 and UF-057 centralizer assertions are withdrawn by the UF-058 composition-order correction.

**Open UF-060:** compute the full determinant-open affine coaction with arbitrary a,b,d,h,i,c and (Delta=ai-bh) invertible, and determine the complete coefficient module in the sixteen target functions. Then compute its annihilator and compare the resulting orbit-image kernel with the second-Frobenius candidate before taking the Hopf core.
