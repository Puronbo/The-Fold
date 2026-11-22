# UF-060 — The full determinant-open affine ch coefficient

## 1. Full affine family

Work in characteristic two in
\[
C=k[x,z]/(x^4,z^2).
\]
Let
\[
\begin{aligned}
u(x)&=x+Ax^2+Bx^3+Cxz+Dx^2z+Ex^3z,\\
u(z)&=z+Axz+Gx^3+(B+G)x^2z+Jx^3z
\end{aligned}
\]
be the general element of U. Let
\[
g(x)=c+ax+bz,\qquad g(z)=d+hx+iz,
\]
where (a,i) are units and (c^4=d^2=h^2=0). The determinant is (Delta=ai+bh) in characteristic two. Since (bh) is square-zero, (ai) is a unit, so write
\[
r=a^{-1},\qquad t=i^{-1}.
\]
Then
\[
\Delta^{-1}=rt+bhr^2t^2,
\]
because ((bhrt)^2=0).

## 2. Correct composition

For algebra automorphisms represented by their images, the conjugate is evaluated in the order
\[
g^{-1}\quad\text{then }u\quad\text{then }g.
\]
Equivalently, compute (g(u(g^{-1}(x)))) and (g(u(g^{-1}(z)))). This order is essential; UF-058 records the correction of earlier reversed-substitution calculations.

Let
\[
X_g=c+ax+bz,\qquad Z_g=d+hx+iz.
\]
The inverse is
\[
g^{-1}(x)=\Delta^{-1}(i(x+c)+b(z+d)),\qquad
g^{-1}(z)=\Delta^{-1}(h(x+c)+a(z+d)).
\]
Applying u to these expressions and then g gives the conjugated outputs. Reduce in the ring with
\[
x^4=z^2=c^4=d^2=h^2=0.
\]

## 3. Theorem UF-060 — exact full-affine ch coefficient

Define
\[
L=Abt+C,\qquad M=B+Ed+Gbt+Jbdt,\qquad N=E+Jbt.
\]
Write
\[
\begin{aligned}
X'&=c'+a'x+b'z+\alpha'x^2+\beta'x^3+\gamma'xz+\delta'x^2z+\epsilon'x^3z,\\
Z'&=d'+h'x+i'z+\phi'x^2+\psi'x^3+\eta'xz+\theta'x^2z+\kappa'x^3z.
\end{aligned}
\]
Then the coefficient of the monomial ch in the conjugated coordinate polynomials is
\[
\boxed{
\begin{aligned}
[ch]X'={}&bd r^2tL+rLx+br^2Lz
          +btM x^2+aN x^3+bN x^2z,\\
[ch]Z'={}&drtL+Atx+rLz
          +atM x^2+Ja^2t x^3+aN x^2z.
\end{aligned}}
\]
In particular, the coefficient table across all sixteen target functions is
\[
\begin{array}{c|c@{\qquad}c|c}
c'&bd r^2tL & d'&drtL\\
a'&rL & b'&br^2L\\
\alpha'&btM & \phi'&atM\\
\beta'&aN & \psi'&Ja^2t\\
\delta'&bN & \theta'&aN\\
h'&At & i'&rL
\end{array}
\]
and
\[
[ch]\gamma'=[ch]\epsilon'=[ch]\eta'=[ch]\kappa'=0.
\]
Thus twelve of the sixteen target coefficient functions detect ch throughout the full determinant-open affine family; the four displayed zero components do not.

## 4. Checks and specializations

- Setting (a=i=1), (d=0) gives the UF-059 affine-slice table.
- Setting (b=0), (a=i=1), (d=0) gives ([ch]h'=A), hence (h'=Ach) in the A-only example.
- The determinant inverse is exact: ((rt+bhr^2t^2)(ai+bh)=1), using (ar=it=1) and (h^2=0).

The calculation is exact over the universal coefficient ring with the stated relations; it is not a truncation modulo a higher nilradical power. The coefficient ([ch]) means extraction of the monomial c h in the unique truncated monomial expansion.

## 5. Scope and next problem

This theorem determines the full affine family's (ch)-component, not its complete coefficient module. Other nilradical monomials (including (c^2,cd,ch,dh,c^2d,ldots)) can contribute additional independent directions. The coefficient module, its annihilator, the kernel of the universal conjugation pullback, and the largest Hopf ideal contained in that kernel remain distinct calculations.

**Open UF-061:** compute every nilradical monomial coefficient in all sixteen target functions for the full determinant-open affine family, determine the resulting coefficient module and annihilator, and compare the orbit-image kernel with the second-Frobenius candidate before computing its Hopf core.


## 6. UF-063 — Exact degeneracy locus of the mixed (ch) direction

The coefficient vector in Theorem UF-060 vanishes in all sixteen target coordinates if and only if
[
oxed{A=C=J=E=0,qquad B+Gbt=0.}
]
Here (a,t=i^{-1}) are units and
[
L=Abt+C,quad M=B+Ed+Gbt+Jbdt,quad N=E+Jbt.
]

**Proof.** If the coefficient vector vanishes, its (x)-coefficient in ([ch]X') gives (rL=0), hence (L=0). Its (x)-coefficient in ([ch]Z') gives (At=0), hence (A=0), and therefore (C=0). The (x^3)-coefficient in ([ch]Z') is (Ja^2t), so (J=0). The (x^2z)-coefficient in ([ch]Z') is (aN), so (N=0), hence (E=0). The (x^2)-coefficient in ([ch]Z') is (atM), so (M=0), which now reads (B+Gbt=0). Conversely, these five equations make (L=M=N=A=J=0), and every entry in the UF-060 coefficient table vanishes.

Thus the mixed (ch) direction is detected away from this explicit closed parameter locus and is invisible on it. This is a statement about one coefficient vector only; it does not compute the full coefficient module, the universal orbit-image kernel, or its Hopf core.


## 7. UF-064 — Corrected first-order nilpotent coefficient map

Let \(\mathfrak n=(c,d,h)\), with \(c^4=d^2=h^2=0\), and put \(t=i^{-1}\) and \(Q=Ab+Ci\). Define
\[
R=Di^2+Gb^2+Gbi.
\]
Extracting coefficients from the exact composition \(g(u(g^{-1}(-)))\), and reducing modulo \(\mathfrak n^2\), gives the following complete table. Entries are coefficients of the indicated nilpotent monomial in the target coordinate coefficient; omitted entries are zero.

\[
\begin{array}{c|ccc}
\text{coefficient in }X' &[c]&[d]&[h]\\ \hline
c'&0&0&0\\
a'&0&tQ&0\\
b'&Q/a&btQ/a&0\\
\alpha'&at(Bi+Gb)&at(Bb+Di+Gb)&C\\
\beta'&0&a^2t(Ei+Jb)&at^2R\\
\gamma'&0&0&0\\
\delta'&a(Ei+Jb)&abt(Ei+Jb)&bt^2R\\
\epsilon'&0&0&0
\end{array}
\qquad
\begin{array}{c|ccc}
\text{coefficient in }Z' &[c]&[d]&[h]\\ \hline
d'&0&0&0\\
h'&0&Aat&0\\
i'&A&Abt&0\\
\phi'&Ga^2t&a^2t(B+G)&0\\
\psi'&0&Ja^3t&Ga^2t^2(b+i)\\
\eta'&0&0&C\\
\theta'&Ja^2&Ja^2bt&at^2R\\
\kappa'&0&0&Ea^2
\end{array}
\]

For example, the coefficient of \(d\) in the \(x\)-coefficient of \(Z'\) is \(Aat\), while the coefficient of \(c\) there is zero. Thus the earlier UF-064 table had misplaced first-order contributions and incorrectly asserted that \(X'\) had no linear terms. The table above supersedes that earlier table.

The generic-rank-three conclusion remains valid. In the rows \(i'\) (the \(z\)-coefficient of \(Z'\)), \(h'\) (the \(x\)-coefficient of \(Z'\)), and \(\alpha'\) (the \(x^2\)-coefficient of \(X'\)), the \((c,d,h)\)-minor is
\[
\det\begin{pmatrix}
A&Abt&0\\
0&Aat&0\\
at(Bi+Gb)&at(Bb+Di+Gb)&C
\end{pmatrix}=A^2atC.
\]
Since \(a,t\) are units, the first-order map has rank three on the open locus \(AC\ne0\).

This computes exactly the \(\mathfrak n/\mathfrak n^2\) layer only. It does not determine the quadratic and higher nilpotent layers, the full coefficient module, the universal orbit-image kernel, or its Hopf core.


## 8. UF-065 — Complete quadratic nilpotent layer

For compactness put
\[
Q=Ab+Ci,\quad R=Di^2+Gb^2+Gbi,\quad
S=Ei+Jb,\quad T=Bb+Di+Gb.
\]
The coefficient vectors of the four degree-two nilpotent monomials
\(c^2,cd,ch,dh\), across all sixteen target coefficients, are as follows. Entries not shown are zero.

\[
\begin{array}{c|cccc}
X'&[c^2]&[cd]&[ch]&[dh]\\ \hline
c'&A/a&Q/(ai)&0&0\\
a'&t(Bi+Gb)&0&Q/(ai)&bQ/(ai^2)\\
b'&R/(ai)&0&bQ/(a^2i)&b^2Q/(a^2i^2)\\
\alpha'&0&atS&bt^2(Bi+Gb)&bt^2T\\
\beta'&0&0&atS&abt^2S\\
\gamma'&S&0&0&0\\
\delta'&0&0&btS&b^2t^2S\\
\epsilon'&0&0&0&0
\end{array}
\]

\[
\begin{array}{c|cccc}
Z'&[c^2]&[cd]&[ch]&[dh]\\ \hline
d'&0&A t&0&0\\
h'&Gat&0&At&Q t^2\\
i'&B+G+Gbt&0&Q/(ai)&bQ/(ai^2)\\
\phi'&0&Ja^2t&at^2(Bi+Gb)&at^2T\\
\psi'&0&0&Ja^2t&a^2t^2S\\
\eta'&Ja&0&0&0\\
\theta'&0&0&atS&abt^2S\\
\kappa'&0&0&0&Ea^2
\end{array}
\]

The \([ch]\)-columns reproduce UF-060 exactly, providing an internal cross-check against the independently derived full mixed coefficient. The degree-two coefficient vectors are generically independent. Indeed, the minor using the four \(X'\)-rows \((c',a',b',\alpha')\), with columns \((c^2,cd,ch,dh)\), is
\[
\frac{bQ^2TR}{a^3i^5}
\]
in characteristic two. It is nonzero on the dense open locus \(bQTR\ne0\), so the quadratic associated-graded coefficient map has generic rank four.

This result concerns the degree-two layer \(\mathfrak n^2/\mathfrak n^3\) only. It does not imply that the full coefficient module has rank seven: interactions with higher layers and relations among coefficient functions still require separate analysis.


## 9. UF-066 — Cubic, quartic, and top nilpotent layers

Put
\[
S=Ea+Jb,\qquad W=Da^2+Gab+Gb^2.
\]
The following tables give the coefficients of the degree-three, degree-four, and degree-five monomials in the sixteen target coefficient functions. The target basis is
\[
1,x,z,x^2,x^3,xz,x^2z,x^3z.
\]
All calculations take place in characteristic two, with \(a,i\) invertible and
\(c^4=d^2=h^2=0\). Entries not displayed are zero.

### Degree three

For columns \(c^3,c^2d,c^2h,cdh\), the \(X'\)-coefficient table is
\[
\begin{array}{c|cccc}
X'&[c^3]&[c^2d]&[c^2h]&[cdh]\\ \hline
1&(Ba+Gb)/a^3&(Da^2+Gab+Gb^2)/(a^3i)&(Ab+Ca)/(a^2i)&b(Ab+Ca)/(a^2i^2)\\
x&0&S/(a^3i)&W/(a^4i)&0\\
z&S/(a^3i)&0&bW/(a^4i^2)&0\\
x^2&0&0&0&bS/(a^4i^2)\\
x^3&0&0&0&0\\
xz&0&0&bS/(a^4i^2)&0\\
x^2z&0&0&0&0\\
x^3z&0&0&0&0
\end{array}
\]
and the \(Z'\)-coefficient table is
\[
\begin{array}{c|cccc}
Z'&[c^3]&[c^2d]&[c^2h]&[cdh]\\ \hline
1&Gi/a^3&(Ba+Ga+Gb)/a^3&0&(Ab+Ca)/(a^2i)\\
x&0&J/a^3&G(a+b)/a^4&0\\
z&J/a^3&0&W/(a^4i)&0\\
x^2&0&0&0&S/(a^4i)\\
x^3&0&0&0&0\\
xz&0&0&S/(a^4i)&0\\
x^2z&0&0&0&0\\
x^3z&0&0&0&0
\end{array}
\]

The four degree-three vectors are generically independent. The minor on the first four \(X'\)-rows \((1,x,z,x^2)\), with columns \((c^3,c^2d,c^2h,cdh)\), is
\[
\frac{bS^2}{a^{13}i^5}P_3,
\]
where
\[
\begin{aligned}
P_3={}&AEa^2b+A Jab^2+BDa^2b+BGab^2+BGb^3\\
&+CEa^3+CJa^2b+D^2a^3+DGab^2+G^2ab^2+G^2b^3.
\end{aligned}
\]
This is a nonzero polynomial (for example, its \(CEa^3\) term cannot cancel identically), so this layer has generic rank four.

### Degree four

For columns \(c^3d,c^3h,c^2dh\), the \(X'\)-coefficient table is
\[
\begin{array}{c|ccc}
X'&[c^3d]&[c^3h]&[c^2dh]\\ \hline
1&S/(a^3i)&W/(a^4i)&bW/(a^4i^2)\\
x&0&0&bS/(a^4i^2)\\
z&0&bS/(a^4i^2)&0\\
x^2&0&0&0\\
x^3&0&0&0\\
xz&0&0&0\\
x^2z&0&0&0\\
x^3z&0&0&0
\end{array}
\]
and the \(Z'\)-coefficient table is
\[
\begin{array}{c|ccc}
Z'&[c^3d]&[c^3h]&[c^2dh]\\ \hline
1&J/a^3&G(a+b)/a^4&W/(a^4i)\\
x&0&0&S/(a^4i)\\
z&0&S/(a^4i)&0\\
x^2&0&0&0\\
x^3&0&0&0\\
xz&0&0&0\\
x^2z&0&0&0\\
x^3z&0&0&0
\end{array}
\]
The minor on the first three \(X'\)-rows \((1,x,z)\) is
\[
\frac{b^2S^3}{a^{11}i^5},
\]
so the degree-four layer has generic rank three.

### Degree five

The only monomial is \(c^3dh\). Its coefficient vector is
\[
\begin{array}{c|cc}
\text{target}&X'&Z'\\ \hline
1&bS/(a^4i^2)&S/(a^4i)\\
x&0&0\\z&0&0\\x^2&0&0\\x^3&0&0\\xz&0&0\\x^2z&0&0\\x^3z&0&0
\end{array}
\]
Thus this final layer has generic rank one.

### Associated-graded rank profile

Combining UF-064, UF-065, and the present calculation gives
\[
\operatorname{rank}_{\mathrm{gen}}
\left(
\mathfrak n^j/\mathfrak n^{j+1}
\longrightarrow
\text{target coefficient space}
\right)
=(3,4,4,3,1),\quad 1\le j\le5.
\]
These ranks equal the dimensions of the corresponding graded pieces of
\(k[c,d,h]/(c^4,d^2,h^2)\). The open conditions can be met simultaneously:
the degree-one minor requires \(AC\ne0\), the degree-two minor requires
\(bQTR\ne0\), and the degree-three through degree-five minors are nonzero
when \(bS P_3\ne0\). Hence all five layer ranks hold on a common dense open
subset of the parameter space.

This is a layer-by-layer associated-graded statement. It does **not** identify
the rank of the unfiltered coefficient module, prove that the full
orbit-image ideal is generated by these coefficients, or determine the
largest Hopf ideal contained in that orbit-image ideal. Those remain separate
questions (UF-061/UF-062B/UF-062C).


## 10. UF-067 — Generic full rank of the unfiltered nilpotent coefficient matrix

Let the fifteen nonconstant monomials of
\[
T=k[c,d,h]/(c^4,d^2,h^2)
\]
be ordered as
\[
(c,d,h,\ c^2,cd,ch,dh,\ c^3,c^2d,c^2h,cdh,\
c^3d,c^3h,c^2dh,\ c^3dh).
\]
Form the \(16\times15\) matrix \(M\) whose columns are their coefficient
vectors in the sixteen target coordinates of \((X',Z')\), using the
target basis \((1,x,z,x^2,x^3,xz,x^2z,x^3z)\) in each coordinate.
The entries are rational functions in \(a,b,i,A,B,C,D,E,G,J\), with
\(a,i\) inverted, and are reduced in characteristic two.

### Exact finite-field specialization certificate

A single nonzero maximal minor proves that the generic rank is fifteen.
For a reproducible certificate, specialize the ten parameters, in the order
\((a,b,i,A,B,C,D,E,G,J)\), to
\[
(\mathtt{d9},\mathtt{c5},\mathtt{c3},\mathtt{d7},
\mathtt{14},\mathtt{84},\mathtt{f8},\mathtt{cf},
\mathtt{9b},\mathtt{f4})
\]
in the field
\[
\mathbb F_{256}=\mathbb F_2[u]/(u^8+u^4+u^3+u^2+1),
\]
where each two-digit hexadecimal entry denotes its polynomial-basis byte.
Both \(a\) and \(i\) are nonzero. Delete the row corresponding to the
\(x^3z\)-coefficient of \(X'\), and retain the other fifteen rows. The
determinant of the resulting \(15\times15\) matrix is
\[
\mathtt{4a}\in\mathbb F_{256}^{\times}.
\]
Thus this maximal minor is not the zero rational function. Since there are
only fifteen columns, the generic rank is exactly
\[
\boxed{\operatorname{rank}_{k(a,b,i,A,B,C,D,E,G,J)} M=15.}
\]

This finite-field specialization is a certificate of nonvanishing, not a
claim that the parameter values describe a generic geometric point over the
original ground field. The computation uses the exact conjugation formulas
of Sections 2–3, expands in the truncated polynomial ring, reduces integer
coefficients modulo two, and then evaluates in the displayed finite field.
The specialization avoids all denominator poles.

### Consequence and limitation

At the generic point of the determinant-open reduced parameter space, the
fifteen nonconstant nilpotent monomials are linearly detected by the sixteen
target coefficient functions: the full unfiltered coefficient matrix has
rank fifteen. This strengthens the layer-by-layer profile of UF-064–UF-066;
it rules out a generic linear dependence between different nilpotent degrees.

It does **not** by itself identify the scheme-theoretic orbit-image ideal
\(J_{\rm orb}\), prove that its extension to the universal coordinate ring
is generated by these fifteen coefficient directions, or determine the
largest Hopf ideal contained in \(J_{\rm orb}\). Those require the
coefficient algebra relations and the coproduct-stability calculation, and
remain open under UF-061/UF-062B/UF-062C.


## 11. UF-068 — Local splitting of the full coefficient map

Let R be the characteristic-two parameter ring in a,b,i,A,B,C,D,E,G,J with a and i inverted, and let M be the 16-by-15 matrix of Section 10. Regard M as the matrix of
\[
\Phi:R^{15}\longrightarrow R^{16}.
\]
The UF-067 specialization proves that the maximal minor \(\delta\) obtained by deleting the \(X'\)-row for the \(x^3z\)-coefficient is a nonzero element of R: its value at the displayed \(\mathbb F_{256}\)-point is \(\mathtt{4a}\). Thus \(D(\delta)\) is a nonempty dense principal open subset of the integral parameter space.

On \(R_\delta\), the selected 15 rows give an invertible square matrix. After permuting rows, write
\[
M=\begin{pmatrix}M_0\\v\end{pmatrix},\qquad \det(M_0)=\delta\in R^\times_\delta.
\]
The map \(\Phi_\delta\) is therefore a split injection: projection to the selected 15 coordinates followed by \(M_0^{-1}\) is a left inverse. Consequently
\[
\operatorname{coker}(\Phi_\delta)\cong R_\delta
\]
is free of rank one. In particular, the coefficient directions form a direct summand of the 16-dimensional target coefficient module on this chart.

**Precise scope.** This is a local statement about the linear map whose columns are the coefficient vectors of the fifteen nonconstant monomials. It does not say that a coefficient module is an ideal, that it is closed under multiplication or coproduct, or that its generators cut out the scheme-theoretic image. In particular, it does not compute \(J_{\rm orb}=\ker(\mathrm{Conj}^*)\) or its largest contained Hopf ideal. Those require the algebra relations among all pulled-back coordinate functions and a separate Hopf-core calculation. The result supplies a convenient dense chart for that future calculation, with a rank-one residual target direction.

**Next task UF-069.** On the chart \(D(\delta)\), compute the multiplication relations among the pulled-back target coefficient functions and then the induced coproduct on the resulting coefficient algebra. Determine whether the rank-one cokernel direction is preserved, mixed with the fifteen-dimensional image, or annihilated by the orbit-image relations. Do not infer Hopf stability from the split-injection statement alone.


## 12. UF-069 — The unique residual linear relation

Order the rows of the 16-by-15 matrix M as in Section 10, and let row r be the omitted \(X'\)-coordinate row (the \(x^3z\)-coefficient). Write
\[
M=\begin{pmatrix}M_0\\v\end{pmatrix},\qquad \det(M_0)=\delta.
\]
On \(D(\delta)\), the matrix \(M_0\) is invertible. Define the normalized row covector
\[
\ell=(vM_0^{-1},1).
\]
In characteristic two this satisfies \(\ell M=0\). It spans the left kernel: if \((w,s)M=0\), then \(wM_0+sv=0\), so \(w=svM_0^{-1}\), and hence \((w,s)=s\ell\). Therefore the left kernel is free of rank one on this chart, with the displayed normalized generator.

For each of the sixteen target coefficient functions write its nilpotent expansion as
\[
f_j=f_j^{(0)}+\sum_{m\ne1}M_{jm}m,
\]
where m runs over the fifteen nonconstant monomials in \(c,d,h\), and \(f_j^{(0)}\) is the constant term in that nilpotent algebra. The identity \(\ell M=0\) gives
\[
\boxed{\sum_{j=1}^{16}\ell_jf_j=\sum_{j=1}^{16}\ell_jf_j^{(0)}.}
\]
Thus there is exactly one normalized linear combination of the sixteen target functions whose nilpotent dependence cancels, and all fifteen nilpotent coefficient directions are otherwise independent over the localized parameter ring.

**Scope warning.** The coefficients \(\ell_j\) lie in the localized parameter ring \(R_\delta\), not necessarily in the image subalgebra generated over k by the \(f_j\). The displayed identity is therefore a relation in the \(R_\delta\)-module spanned by these functions; it is not automatically a polynomial relation in the k-algebra generated by them. It does not compute the multiplication ideal of the image algebra, \(J_{\rm orb}\), or its largest contained Hopf ideal. This distinction is essential for the next step.

**Next task UF-070.** Determine which elements of \(R_\delta\) needed to form \(M_0^{-1}\) are themselves in the image algebra (or can be eliminated), and compute the actual k-algebra generated by the pulled-back target coordinates. Only after that algebra is identified should its coproduct and Hopf core be computed.


## 13. UF-070 — Exact elimination presentation of the affine-conjugator coefficient algebra

Let
\[
\mathcal R=k[a,b,i,A,B,C,D,E,G,J,a^{-1},i^{-1},c,d,h]
 /(c^4,d^2,h^2),
\]
where \(a,b,i,c,d,h\) are the affine conjugator coordinates and \(A,B,C,D,E,G,J\) are the seven coordinates on \(U\). Let \(f_1,\ldots,f_{16}\in\mathcal R\) be the sixteen target coefficient functions of the affine-conjugator family, in the fixed order of Section 10. Define
\[
\theta:k[Y_1,\ldots,Y_{16}]\longrightarrow\mathcal R,
\qquad Y_j\longmapsto f_j.
\]
Then the coordinate algebra of the scheme-theoretic image of this affine-conjugator coefficient map is exactly
\[
\boxed{\mathcal A_{\rm aff}=k[f_1,\ldots,f_{16}]
\cong k[Y_1,\ldots,Y_{16}]/\ker\theta.}
\]
This is an auxiliary coefficient-image algebra for the three-parameter affine conjugator family. It is not the full universal conjugation image for \(G\times U\to G\), whose conjugator ranges over the entire automorphism group scheme. It is also not the parameter ring \(\mathcal R\), nor the \(\mathcal R\)-module generated by the sixteen functions. Its relations can inform the full problem, but cannot replace the full-coordinate calculation of \(J_{\rm orb}\).

### Elimination realization

Inside \(\mathcal R[Y_1,\ldots,Y_{16}]\), form the graph ideal
\[
I_\theta=(Y_1-f_1,\ldots,Y_{16}-f_{16}).
\]
The kernel is its contraction:
\[
\boxed{\ker\theta=I_\theta\cap k[Y_1,\ldots,Y_{16}].}
\]
Thus an exact Gröbner/elimination computation can be performed in a polynomial ring by adjoining inverse variables \(a',i'\), imposing \(aa'-1=ii'-1=0\), and eliminating all source variables \(a,i,a',i',b,A,B,C,D,E,G,J,c,d,h\). The relations \(c^4=d^2=h^2=0\) must remain in the elimination ideal. This gives a finite, explicit presentation target for UF-070; no claim is made here that the resulting elimination ideal has already been computed.

### Dense-chart invariance

Let \(\delta\) be the nonzero maximal minor from UF-067. The algebra \(\mathcal R\) is free over the integral Laurent-polynomial parameter ring in \(a,i\) and the remaining reduced coordinates, with basis \(c^r d^s h^t\) for \(0\le r\le3\), \(s,t\in\{0,1\}\). Since \(\delta\) is nonzero in that integral base, multiplication by \(\delta\) is injective on \(\mathcal R\). Hence \(\mathcal R\to\mathcal R_\delta\) is injective. It follows that
\[
\ker(k[Y]\xrightarrow{\theta}\mathcal R)
=\ker(k[Y]\xrightarrow{\theta_\delta}\mathcal R_\delta).
\]
Therefore passing to the UF-068/069 dense chart does not change the scheme-theoretic image ideal of this affine-conjugator coefficient map. It may simplify the calculation, but it does not turn the parameter-ring-linear relation \(\ell\cdot f=\ell\cdot f^{(0)}\) into a polynomial relation over \(k\): membership of its coefficients in \(\mathcal A_{\rm aff}\) remains a separate question.

**Consequence.** UF-070 now has a precise algebraic target for the affine-conjugator coefficient family: compute the elimination ideal \(I_\theta\cap k[Y]\), or equivalently give generators and relations for \(k[f_1,\ldots,f_{16}]\). The full orbit-image ideal
\[
J_{\rm orb}=\ker\bigl(O(G)\longrightarrow O(G)\otimes O(U)\bigr)
\]
and its largest contained Hopf ideal still require the full universal conjugator and are not computed by this affine slice. No equality with the second-Frobenius candidate is inferred.


## 14. UF-071 — The two-copy coproduct test for the affine-slice image

The affine-linear conjugators
\[
g(x)=c+ax+bz,\qquad g(z)=d+hx+iz,
\quad c^4=d^2=h^2=0,\quad ai+bh\in R^\times
\]
form a subgroup scheme \(G_{\rm aff}\subset G\). Indeed, composing two affine-linear substitutions again gives affine-linear images, and the invertible linear coefficient matrix has an affine-linear inverse. The relations \(c^4=d^2=h^2=0\) are preserved under composition in characteristic two; the inverse is again an automorphism and hence satisfies the same relations. Since \(bh\) is nilpotent, invertibility of \(ai+bh\) is equivalent to invertibility of \(a\) and \(i\).

Let
\[
\Psi:G_{\rm aff}\times U\longrightarrow G,\qquad
(g,u)\longmapsto gug^{-1},
\]
and let
\[
I_{\rm aff}=\ker\bigl(O(G)\xrightarrow{\Psi^*}
O(G_{\rm aff})\otimes O(U)\bigr).
\]
This is the ideal of the affine-conjugator image studied by UF-060–UF-070. It is distinct from the full orbit-image ideal \(J_{\rm orb}\), where \(G_{\rm aff}\) is replaced by all of \(G\).

### Exact subgroup criterion

The affine-conjugator image is a closed subgroup scheme if and only if \(I_{\rm aff}\) is a Hopf ideal. In particular, the coproduct condition is
\[
\boxed{
\Delta(I_{\rm aff})\subseteq
I_{\rm aff}\otimes O(G)+O(G)\otimes I_{\rm aff}.
}
\]
The counit and antipode conditions must also hold. This is a criterion, not a claim that the image is a subgroup.

To test it computationally, introduce two independent source pairs
\[
(g_1,u_1),\quad(g_2,u_2)\in G_{\rm aff}\times U
\]
and evaluate the product
\[
(g_1u_1g_1^{-1})(g_2u_2g_2^{-1}).
\]
The resulting sixteen target coefficient functions must be reduced modulo the sum of the two copies of the image ideal. A shared conjugator, or the special product \(g(u_1u_2)g^{-1}\), does not test closure under multiplication of two arbitrary image points.

Equivalently, if \(F\in I_{\rm aff}\) is a target-coordinate relation, the coproduct test is whether
\[
F\bigl((g_1u_1g_1^{-1})(g_2u_2g_2^{-1})\bigr)=0
\]
in the tensor product of the two independent source coordinate algebras. This is the two-copy substitution/elimination problem that must follow the one-copy elimination of UF-070.

### Consequence for the normal-closure problem

Even a successful Hopf test for \(I_{\rm aff}\) would only identify the subgroup generated by affine-conjugator images. It would not by itself compute the normal closure under the full group scheme \(G\). The full problem still requires the full conjugator and the largest Hopf ideal contained in
\[
J_{\rm orb}=\ker\bigl(O(G)\to O(G)\otimes O(U)\bigr).
\]
No subgroup assertion, equality with the second-Frobenius candidate, or computation of either Hopf core is made here.

**Open UF-072.** Compute the one-copy affine-slice elimination ideal \(I_{\rm aff}\), then perform the two-independent-copy substitution to test the coproduct condition. If it fails, determine the largest Hopf ideal contained in \(I_{\rm aff}\); separately compare that result with the full universal Hopf core.


## 15. UF-072A — Nilradical and dimension bound for the affine-slice image

Retain the source algebra and map from Section 13:
\[
\mathcal R=k[a,a^{-1},b,i,i^{-1},A,B,C,D,E,G,J,c,d,h]/(c^4,d^2,h^2),
\qquad \mathcal A_{\rm aff}=k[f_1,\ldots,f_{16}]\subseteq\mathcal R.
\]
Let
\[
B_{\rm red}=k[a,a^{-1},b,i,i^{-1},A,B,C,D,E,G,J],
\quad T=k[c,d,h]/(c^4,d^2,h^2),
\quad \mathfrak n=(c,d,h)\subset T.
\]
Then \(\mathcal R=B_{\rm red}\otimes_kT\), \(\mathfrak n^6=0\), and \(\mathcal R/\mathfrak n\mathcal R\cong B_{\rm red}\), a reduced integral domain. Define
\[
\mathcal N=\mathcal A_{\rm aff}\cap\mathfrak n\mathcal R.
\]
The restriction of the quotient map \(\mathcal R\to B_{\rm red}\) to \(\mathcal A_{\rm aff}\) has kernel exactly \(\mathcal N\), so
\[
\mathcal A_{\rm aff}/\mathcal N\hookrightarrow B_{\rm red}.
\]
Moreover, every element of \(\mathcal N\) lies in \(\mathfrak n\mathcal R\), hence \(\mathcal N^6=0\). Conversely, if an element of \(\mathcal A_{\rm aff}\) is nilpotent, its image in the reduced ring \(B_{\rm red}\) is zero, so it belongs to \(\mathcal N\). Therefore \(\mathcal N\) is exactly the nilradical of \(\mathcal A_{\rm aff}\), and
\[
\boxed{\operatorname{Nil}(\mathcal A_{\rm aff})^6=0,\qquad
\mathcal A_{\rm aff,red}\hookrightarrow B_{\rm red},\qquad
\dim\mathcal A_{\rm aff}\leq10.}
\]
The dimension bound follows because \(B_{\rm red}\) is a Laurent-polynomial ring in ten variables and integral extensions are not being assumed: the reduced image is a finitely generated subalgebra of this ten-dimensional domain, so its transcendence degree (and Krull dimension) is at most ten. A nilpotent ideal does not change Krull dimension.

**Scope.** This proves the nilpotence exponent bound and dimension upper bound for the auxiliary affine-conjugator image algebra. It does not compute its defining elimination ideal, establish a matching dimension lower bound, test the two-copy coproduct, or identify the full universal Hopf core. In particular, the generic rank-15 coefficient-matrix result concerns nilpotent directions over the parameter ring and does not imply that the image algebra has dimension 15.

**Next UF-072C.** Compute the reduced image map obtained by setting \(c=d=h=0\), determine its Jacobian rank and exact reduced image ideal, then lift the calculation through the nilpotent filtration \(\mathcal N/\mathcal N^2,\ldots,\mathcal N^5\). Only after this one-copy algebra is explicit should the independent two-copy coproduct test be run.


## 16. UF-072B — Exact reduced affine-slice image

Set \(c=d=h=0\). The affine conjugator is then
\[
g(x)=ax+bz,\qquad g(z)=iz,\qquad a,i\in k^\times.
\]
Its inverse sends \(x\mapsto a^{-1}x+ba^{-1}i^{-1}z\) and \(z\mapsto i^{-1}z\). For the general element \(u\in U\), substitution in characteristic two gives the identity
\[
\boxed{g\circ u\circ g^{-1}=u.}
\]
In particular the sixteen target coefficients, in the ordered basis \((1,x,z,x^2,x^3,xz,x^2z,x^3z)\) for each output, reduce to
\[
(0,1,0,A,B,C,D,E;\ 0,0,1,0,G,A,B+G,J).
\]
Therefore the image of the reduced parameter map is generated by exactly the seven independent coordinates \(A,B,C,D,E,G,J\). More formally, the reduction homomorphism from the affine-slice image algebra to the reduced source parameter ring has image
\[
\boxed{\mathcal A_{\rm aff,red}=k[A,B,C,D,E,G,J].}
\]
It follows that
\[
\boxed{\dim\mathcal A_{\rm aff}=7,}
\]
not merely the previous upper bound ten. The seven displayed generators are algebraically independent because they are distinct polynomial coordinates in the reduced source ring. Equivalently, the reduced coefficient map has Jacobian rank exactly seven: its seven nonconstant target entries are the seven parameter coordinates themselves, and every other entry is constant or zero.

**Proof check.** The identity is obtained by applying \(g^{-1}\), then \(u\), then \(g\), reducing with \(x^4=z^2=0\), and using characteristic two. In the intermediate expansion, terms with coefficients 2, 4, or 6 vanish; the remaining target coefficients are exactly the tuple above. This computation is over the universal Laurent-polynomial ring \(k[a^{\pm1},b,i^{\pm1},A,B,C,D,E,G,J]\), not just a numerical specialization.

**Scope.** This determines the reduced image algebra and the Krull dimension of the full affine-slice image algebra, since nilpotent ideals do not change dimension. It does not determine the nilpotent thickening \(\mathcal N\), its successive quotients, the one-copy elimination generators, or the two-independent-copy coproduct test. In particular, the fact that every reduced affine conjugator centralizes \(U\) does not imply that the full nonreduced affine-conjugator image is a subgroup: the nilpotent translation directions \(c,d,h\) still contribute.

**Next UF-072C.** Compute \(\mathcal N/\mathcal N^2,\ldots,\mathcal N^5\) as modules over \(k[A,B,C,D,E,G,J]\), determine the multiplication among these layers, and then test the coproduct using two independent affine conjugators.


## 17. UF-072C — Nine generators for the nilpotent thickening

Write the sixteen target coefficient functions as (X_1,X_x,X_z,X_{x^2},X_{x^3},X_{xz},X_{x^2z},X_{x^3z}) and (Z_1,Z_x,Z_z,Z_{x^2},Z_{x^3},Z_{xz},Z_{x^2z},Z_{x^3z}), in the ordered basis used above. By UF-072B their reductions are
[
(0,1,0,A,B,C,D,E; 0,0,1,0,G,A,B+G,J).
]
Choose seven lifts
[
s_A=X_{x^2},quad s_B=X_{x^3},quad s_C=X_{xz},quad
s_D=X_{x^2z},quad s_E=X_{x^3z},quad
s_G=Z_{x^3},quad s_J=Z_{x^3z}.
]
Their reductions are the seven independent polynomial coordinates. Hence
[
S=k[s_A,s_B,s_C,s_D,s_E,s_G,s_J]cong k[A,B,C,D,E,G,J].
]
In particular, the map (S	omathcal A_{m aff}/mathcal N) is an isomorphism.

Define the remaining nine corrected coefficients
[
egin{array}{lll}
n_1=X_1,&n_2=X_x-1,&n_3=X_z,\
n_4=Z_1,&n_5=Z_x,&n_6=Z_z-1,\
n_7=Z_{x^2},&n_8=Z_{xz}-s_A,&
n_9=Z_{x^2z}-s_B-s_G.
end{array}
]
Each has zero reduction, so lies in (mathcal N). Conversely, (mathcal A_{m aff}) is generated by the sixteen target coefficients; the displayed seven lifts and nine corrections recover all sixteen. Modulo the ideal ((n_1,ldots,n_9)), the resulting algebra is exactly (S), whose map to the reduced image is an isomorphism. Therefore
[
oxed{mathcal N=(n_1,ldots,n_9)mathcal A_{m aff}.}
]

Every (n_j) lies in ((c,d,h)mathcal R). In characteristic two, every element of this source ideal has fourth power zero: the fourth-power map is additive, and each positive-degree monomial in (c,d,h) has fourth power zero under (c^4=d^2=h^2=0). Thus
[
oxed{n_j^4=0quad(1le jle9).}
]
It follows that (mathcal A_{m aff}) is a finite (S)-module, generated by the monomials (n_1^{e_1}cdots n_9^{e_9}) with (0le e_j<4). The stronger ambient bound (mathcal N^6=0) from UF-072A also applies.

The first associated-graded layer therefore has the exact presentation
[
oxed{mathcal N/mathcal N^2cong S^9/K_1,}
]
where (K_1) is the (S)-submodule of relations among the nine classes ([n_j]). The UF-064 first-order coefficient table gives their images in
[
(c,d,h)mathcal R/(c,d,h)^2mathcal R
cong B_{m red}^{,3},
]
but computing the full kernel (K_1) requires eliminating the Laurent parameters (a,b,i) over (S). The parameter-ring generic rank-three result in UF-064 is not, by itself, that elimination.

**What is established.** The reduced base is a polynomial ring in seven variables; the nilradical is generated by nine explicit fourth-nilpotent elements; and the whole image algebra is finite over that reduced base.

**Still open.** The relation module (K_1), the higher multiplication maps between (mathcal N^r/mathcal N^{r+1}), an explicit one-copy elimination ideal, and the two-independent-copy coproduct test. In particular, finite generation and nilpotence do not imply that the affine-slice image is a subgroup scheme.


## 18. UF-072D — First-order kernel bound for the nilpotent relation module

Use the nine generators (n_1,ldots,n_9) of Section 17 and the polynomial subalgebra (S). Set
[
t=i^{-1},quad Q=Ab+Ci,quad R=Di^2+Gb^2+Gbi,quad
S_0=Ei+Jb,quad T=Bb+Di+Gb.
]
The nine generators are, in order,
[
egin{array}{lll}
n_1=X_1,&n_2=X_x-1,&n_3=X_z,\
n_4=Z_1,&n_5=Z_x,&n_6=Z_z-1,\
n_7=Z_{x^2},&n_8=Z_{xz}-s_A,&
n_9=Z_{x^2z}-s_B-s_G.
end{array}
]
Subtracting the UF-064 first-order expansions gives their coefficient vectors in the ordered source basis ((c,d,h)):
[
egin{array}{c|ccc}
 & [c]&[d]&[h]\hline
n_1&0&0&0\
n_2&0&tQ&0\
n_3&Q/a&btQ/a&0\
n_4&0&0&0\
n_5&0&Aat&0\
n_6&A&Abt&0\
n_7&Ga^2t&a^2t(B+G)&0\
n_8&at(Bi+Gb)&atT&0\
n_9&Ja^2&Ja^2bt+a^2tS_0+Ja^3t&Ga^2t^2(b+i)
end{array}
]
For (n_8), the (h)-terms in (Z_{xz}) and (s_A=X_{x^2}) cancel. For (n_9), the (h)-terms from (Z_{x^2z}) and (s_B=X_{x^3}) cancel, leaving the displayed (h)-term from subtracting (s_G=Z_{x^3}).

Let (K=k(A,B,C,D,E,G,J)=operatorname{Frac}(S)). The seven nonzero vectors (n_2,n_3,n_5,n_6,n_7,n_8,n_9) are linearly independent over (K) in (K(a,b,i)^3). To verify this, first the (h)-coordinate forces the coefficient of (n_9) to vanish. The (a^{-1})-part of the (c)-coordinate then forces the coefficient of (n_3) to vanish; the (a^2)-part forces that of (n_7) to vanish. The remaining (c)-coordinate has the nonzero (aB) term from (n_8), forcing its coefficient to vanish. The remaining (a/i) term in the (d)-coordinate forces the coefficient of (n_5) to vanish. The constant (c)-coordinate then forces the coefficient of (n_6) to vanish, and finally the (d)-coordinate forces the coefficient of (n_2) to vanish. These coefficient extractions are valid in the Laurent polynomial field (K(a,b,i)); (A,B,C,G) are nonzero elements of (K).

It follows that the (S)-linear first-order map
[
S^9longrightarrow
igl((c,d,h)mathcal R/(c,d,h)^2mathcal Rigr)
]
has kernel exactly (Se_1oplus Se_4). Let
[
K_1=kerigl(S^9	omathcal N/mathcal N^2igr).
]
Any relation modulo (mathcal N^2) must have zero first-order source expansion, since (mathcal N^2subseteq(c,d,h)^2mathcal R). Hence
[
oxed{K_1subseteq Se_1oplus Se_4.}
]

**Critical distinction.** The reverse inclusion has not been proved. The fact that (n_1,n_4) have no linear source terms only puts them in (mathcal Ncap(c,d,h)^2mathcal R); it does not show that they lie in (mathcal N^2). Thus UF-072D bounds the possible relation module to at most the two constant-coordinate generators, but does not yet determine whether either generator vanishes in (mathcal N/mathcal N^2).

**Next UF-072E.** Compare the quadratic source expansions of (n_1,n_4) with products of the first-order generators. Determine whether (n_1,n_4inmathcal N^2), and if so compute the exact coefficients of those product expressions. This is the remaining first-layer relation test before moving to the higher filtration and two-copy coproduct.


## 19. UF-072E — The first nilpotent layer is free of rank nine

Retain the nine generators (n_1,ldots,n_9), the polynomial subalgebra (S), and the first-order coefficient table of Section 18. Section 18 showed that any relation in
[
K_1=ker(S^9longrightarrowmathcal N/mathcal N^2)
]
must be supported on the two basis vectors (e_1,e_4). We now show that neither of these two generators belongs to (mathcal N^2).

Specialize the source parameter ring by (b=C=0), retaining (a,i) as independent Laurent variables and (A,B,D,E,G,J) as independent reduced coordinates. Under this specialization (Q=Ab+Ci=0). The (c)-coefficients of the nine first-order generators are
[
0, 0, 0, 0, 0, A, Ga^2/i, aB, Ja^2.
]
Thus every (c^2)-coefficient of a product of two first-order generators is an (S)-linear combination of Laurent monomials whose (a)-exponents belong to ({0,1,2,3,4}). The UF-065 quadratic table gives
[
[c^2]n_1=A/a.
]
Its (a)-exponent is (-1), so it cannot be such a combination. Since the degree-two source component of an element of (mathcal N^2) is generated by products of first-order components, this proves
[
n_1
otinmathcal N^2.
]

For (n_4), the specialized first-order (d)-coefficients are
[
0, 0, 0, 0, Aa/i, 0, a^2(B+G)/i, aD, Ea^2+Ja^3/i.
]
Every first-order (c)-coefficient has (a)-exponent at least zero, and every first-order (d)-coefficient has (a)-exponent at least one. Therefore every (cd)-coefficient of a product of first-order generators has (a)-exponent at least one. But the UF-065 table gives
[
[cd]n_4=A/i,
]
with (a)-exponent zero. Hence
[
n_4
otinmathcal N^2.
]

The specialization is legitimate for detecting non-membership: an identity over (S) expressing either generator as an element of (mathcal N^2) would remain an identity after this base specialization. Moreover, because every generator lies in the source nilpotent ideal, the degree-two component of (mathcal N^2) is generated precisely by products of their degree-one source components; generators with zero linear component cannot contribute in degree two.

Combining these two non-membership results with the UF-072D bound (K_1subseteq Se_1oplus Se_4) gives
[
oxed{K_1=0,qquad mathcal N/mathcal N^2cong S^9.}
]
Thus the nine explicit nilradical generators form a free (S)-basis of the conormal layer.

**Scope.** This determines the first associated-graded layer only. It does not determine the relations in (mathcal N^2/mathcal N^3) or higher layers, the full one-copy elimination ideal, or the independent two-copy coproduct. The nine generators are not thereby proved algebraically independent in the whole image algebra; they are independent modulo (mathcal N^2).


## 20. UF-072F — Rank and kernel of the quadratic initial multiplication map

Let (L_jin K(a,b,i)^3) denote the degree-one source vector of (n_j), with
(K=operatorname{Frac}(S)). By Section 18, the nonzero vectors are
(L_2,L_3,L_5,L_6,L_7,L_8,L_9); (L_1=L_4=0).
The degree-two source space has basis
[
(c^2,cd,ch,dh),
]
since (d^2=h^2=0). For two degree-one vectors
(u=(u_c,u_d,u_h)) and (v=(v_c,v_d,v_h)), their product vector is
[
uodot v=
(u_cv_c, u_cv_d+u_dv_c, u_cv_h+u_hv_c, u_dv_h+u_hv_d).
]
All signs are plus because the characteristic is two.

Consider the (K)-linear map
[
mu_2:operatorname{Sym}^2_K
  langle L_2,L_3,L_5,L_6,L_7,L_8,L_9angle_{m formal}
  longrightarrow K(a,b,i)^4
]
sending the formal pair (n_rn_s) to (L_rodot L_s). Its domain has 28 standard pair generators. To compute its exact rank, clear the common Laurent denominator (a^2i^3) from all four coordinates of all 28 product vectors, expand in the Laurent monomials in (a,b,i), and regard each coefficient as an element of the rational function field (K). The resulting coefficient matrix has 4 coordinate blocks and 39 distinct Laurent monomials in its support. Exact Gaussian elimination over (K=mathbb F_2(A,B,C,D,E,G,J)) gives
[
oxed{operatorname{rank}_K(mu_2)=24,qquad
dim_Kker(mu_2)=4.}
]

With pair generators ordered lexicographically from
[
(2,2),(2,3),(2,5),(2,6),ldots,(9,9),
]
the 24 pivot columns are indexed by
[
egin{gathered}
(2,3),(2,6),(2,7),(2,8),(2,9),\
(3,3),(3,6),(3,7),(3,8),(3,9),\
(5,6),(5,7),(5,8),(5,9),\
(6,6),(6,7),(6,8),(6,9),\
(7,7),(7,8),(7,9),(8,8),(8,9),(9,9).
end{gathered}
]
A basis of the kernel is
[
(2,2),qquad (2,5),qquad (5,5),qquad
(2,6)+(3,5).
]
Equivalently, the four quadratic initial relations are
[
L_2^2=0,quad L_2L_5=0,quad L_5^2=0,quad
L_2L_6+L_3L_5=0.
]
The first three come from (L_2,L_5) being pure (d)-directions and (d^2=0). For the last relation, both products have the same (cd)-coordinate:
[
(L_2odot L_6)_{cd}=tQcdot A
=rac{AQ}{i}
=rac Qacdotrac{Aa}{i}
=(L_3odot L_5)_{cd}.
]

**Interpretation and limitation.** The 24 is the dimension over (K) of the image of the *degree-two initial multiplication map* generated by the seven nonzero linear forms. It is not yet a computation of (mathcal N^2/mathcal N^3): the products involving (n_1) or (n_4), whose first-order terms vanish, can begin in degree three or higher and may still contribute to that quotient. Nor do the four displayed initial relations assert exact identities among the full (n_j) in (mathcal A_{m aff}). Determining those higher terms, and the full relation module over (S) rather than over its fraction field, remains open.

**Correction to the informal count in the preceding research note:** the degree-two source layer has dimension four, with basis ((c^2,cd,ch,dh)), not ten. The number 45 counts all pair products of nine generators; only 28 of those have potentially nonzero degree-two initial terms.



## 21. UF-072G — Cubic obstructions: corrected calculation

Use the first-order vectors (L_j) and quadratic source components (Q_j) from Sections 18 and 20. The degree-three source layer has basis
[
(c^3,c^2d,c^2h,cdh).
]
For two generators, the degree-three term is (L_rQ_s+Q_rL_s), computed in the truncated source algebra.

The full expansions of (n_2=X_x-1) and (n_5=Z_x) have only source monomials among
[
d, c^2, ch, dh, c^2d, c^2h, c^2dh.
]
Each has square zero under (c^4=d^2=h^2=0). Since Frobenius is additive in characteristic two,
[
oxed{n_2^2=n_5^2=0}
]
as exact identities in the source algebra and hence in the affine image algebra.

**Correction to the previous version.** Direct multiplication of the UF-064/UF-065 components gives
[
oxed{
operatorname{in}_3(n_2n_5)
=left(0,rac{a(AB+CG)}{i},0,0ight).
}
]
The (cdh)-coordinate is zero: its two contributions are both (AQ/i^2) and cancel in characteristic two. The previously recorded nonzero (cdh)-coordinate was an arithmetic error.

For the other quadratic initial relation, the computation gives
[
oxed{
operatorname{in}_3(n_2n_6+n_3n_5)
=left(
AB+CG, AD+BC+CG,rac{AQ(a+1)}{ai},rac{AbQ(a+1)}{ai^2}
ight).
}
]
All coordinates are ordered as ((c^3,c^2d,c^2h,cdh)).

A fresh finite-field check of the cubic initial multiplication map is recorded in the companion certificate
[`certificates/uf072g_cubic_specialization.py`](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072g_cubic_specialization.py).
It uses
[
mathbb F_{256}=mathbb F_2[u]/(u^8+u^4+u^3+u^2+1)
]
and the specialization
[
(a,b,i,A,B,C,D,E,G,J)
=(mathtt{d9},mathtt{c5},mathtt{c3},mathtt{d7},
mathtt{14},mathtt{84},mathtt{f8},mathtt{cf},
mathtt{9b},mathtt{f4}).
]
The 84 triple products of the seven nonzero first-order generators have specialized coefficient-matrix rank 60. Appending the corrected vector (operatorname{in}_3(n_2n_5)) leaves the rank at 60; appending (operatorname{in}_3(n_2n_6+n_3n_5)) raises it to 61; appending both also gives rank 61. These are exact finite-field ranks, reproducible by the companion script.

**Scope.** The specialization certifies the displayed ranks at this parameter point, and therefore gives lower bounds for the corresponding generic ranks. It does not by itself prove the exact generic rank over (K=operatorname{Frac}(S)), nor does it establish that either product represents a nonzero class in the generic fiber of (mathcal N^2/mathcal N^3). In particular, the earlier claim that two independent generic classes had been proved is withdrawn. The exact generic cubic relation module and the full quotient (mathcal N^2/mathcal N^3) remain open.


## 22. UF-072H — Exact generic cubic initial ranks

Let K=F_2(A,B,C,D,E,G,J). Rebuild the cubic initial multiplication map from the seven nonzero first-order vectors L_2,L_3,L_5,L_6,L_7,L_8,L_9, retaining Laurent variables a,b,i as independent monomial exponents. There are 84 triple-product columns. Their support occupies 228 source/Laurent rows, with 96 distinct Laurent exponent triples across the four source-degree coordinates. After adjoining the two test vectors, the common row set has 236 rows.

Exact elimination over the rational-function field K gives
\[
\boxed{\operatorname{rank}_K(\mu_3)=60.}
\]
Adjoining the corrected cubic vector
\[
\operatorname{in}_3(n_2n_5)=(0,a(AB+CG)/i,0,0)
\]
leaves the rank equal to 60. Adjoining
\[
\operatorname{in}_3(n_2n_6+n_3n_5)=
(AB+CG,\ AD+BC+CG,\ AQ(a+1)/(ai),\ AbQ(a+1)/(ai^2))
\]
raises it to 61. Adjoining both also gives rank 61. Thus the first corrected vector belongs to the generic K-span of cubic triple-product initial terms, whereas the second does not.

The computation is reproducible with SymPy using [certificates/uf072h_generic_cubic_rank.py](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072h_generic_cubic_rank.py). It constructs the Laurent coefficient matrix explicitly and converts it to the exact field F_2(A,B,C,D,E,G,J) before rank computation. Its output is 84 triple columns, 228 source/Laurent rows, and ranks 60, 60, 61, 61 for the base map, plus the corrected n_2n_5 vector, plus the mixed vector, and plus both, respectively.

**Consequence.** The generic cubic initial calculation establishes exactly one new direction from the two corrected quadratic-kernel combinations. It does not compute the full N^2/N^3, because products involving n_1,n_4 can begin in degree three or later, and it does not give an integral S-module presentation. The one-copy elimination ideal and two-copy Hopf criterion remain separate tasks.


## 23. UF-072I — Degree-three classes from all pair products

The degree-three source terms of products involving the two generators with zero linear part can be computed from the UF-065 quadratic terms and the UF-072D linear vectors. Write
[
q_1=(A/a)c^2+left(Ab/(ai)+C/aight)cd,qquad
q_4=(A/i)cd.
]
For each (jin{2,3,5,6,7,8,9}), the cubic initial terms are
[
operatorname{in}_3(n_1n_j)=q_1L_j,qquad
operatorname{in}_3(n_4n_j)=q_4L_j,
]
with multiplication in (k[a^{pm1},b,i^{pm1}][c,d,h]/(c^4,d^2,h^2)).

Exact elimination over (K=mathbb F_2(A,B,C,D,E,G,J)) gives:
[
egin{array}{c|c}
	ext{initial vectors included}&	ext{rank}\hline
	ext{84 triple products}&60\
	ext{plus the 14 }n_1n_j,n_4n_j	ext{ cubic terms}&70\
	ext{plus corrected }operatorname{in}_3(n_2n_5)&70\
	ext{plus also }operatorname{in}_3(n_2n_6+n_3n_5)&71
end{array}
]
The ten new pivot columns from the fourteen (n_1,n_4) products are
[
n_1n_2,n_1n_3,n_1n_5,n_1n_6,n_1n_7,n_1n_8,n_1n_9,
n_4n_7,n_4n_8,n_4n_9.
]
The mixed quadratic-kernel combination contributes one further independent class. The corrected (n_2n_5) vector contributes none. The full pivot list and rank calculation are reproducible in [certificates/uf072i_degree3_pair_product_rank.py](https://github.com/Puronbo/The-Fold/blob/research/universal-fold-invariant/certificates/uf072i_degree3_pair_product_rank.py).

Thus the degree-three part of the associated filtration of (mathcal N^2/mathcal N^3), after tensoring with (K), has dimension 11: ten classes from products involving (n_1,n_4), and one from (n_2n_6+n_3n_5). Together with the 24-dimensional degree-two part from UF-072F, the first two graded pieces contribute
[
24+11=35
]
generic dimensions.

**Scope.** This is not yet the full dimension of ((mathcal N^2/mathcal N^3)otimes_S K). Products (n_1^2,n_1n_4,n_4^2) begin in source degree four, and quartic/higher terms of the other pair products can also survive. The exact higher filtration layers and integral (S)-module presentation remain open.


## 24. UF-072J — The remaining constant-generator pair product

The two generators (n_1,n_4) have no source-degree-one terms. Hence every monomial in either source expansion has total ((c,d,h))-degree at least two. In the truncated algebra
[
T=k[c,d,h]/(c^4,d^2,h^2),
]
the square of every monomial of degree at least two is zero. Frobenius is additive in characteristic two, so the full identities are
[
oxed{n_1^2=n_4^2=0.}
]

Their quadratic initial terms from UF-065 are
[
q_1=rac Aa c^2+rac{Ab+Ci}{ai}cd,qquad
q_4=rac Ai cd.
]
Therefore the first nonzero candidate term of their product is
[
oxed{
operatorname{in}_4(n_1n_4)=q_1q_4
=rac{A^2}{ai}c^3d.
}
]
The second product term vanishes because it contains (d^2). The monomial (c^3d) is nonzero in (T), so (n_1n_4) is nonzero in the source algebra.

**Open membership test.** This does not yet prove that (n_1n_4) survives in (mathcal N^2/mathcal N^3): an element of (mathcal N^3) can have source-degree-four initial term. The next calculation must determine the degree-four initial image of (mathcal N^3), including triple products with one of (n_1,n_4), syzygies among cubic triple-product initial terms, and products of four first-order generators. The full quotient is still not determined.



## UF-072K — Degree-four initial image of N^3: specialization bounds

The degree-four initial image of \(\mathcal N^3\) must include three types of columns:
(1) the degree-four parts of triple products of the seven generators with nonzero
linear terms, obtained by inserting one quadratic correction;
(2) products of \(n_1\) or \(n_4\) with any pair of those seven generators;
and (3) all fourfold products of the seven first-order generators. The third
family is required because \(\mathcal N^3\) is an ideal, not merely the
\(S\)-span of the 84 triple products.

The resulting matrix has 350 columns (84 + 56 + 210) and 470 source/Laurent
rows. The candidate target is
\[
\operatorname{in}_4(n_1n_4)=A^2a^{-1}i^{-1}c^3d.
\]
Over \(\mathbb F_{256}=\mathbb F_2[u]/(u^8+u^4+u^3+u^2+1)\), three
specializations of \((A,B,C,D,E,G,J)\) give rank 176 for the 350-column
matrix and rank 177 after adjoining the target. The tuples are
\[
(d7,14,84,f8,cf,9b,f4),\quad
(31,72,a4,5b,e1,93,c7),\quad
(a1,3d,6f,e3,55,b2,19).
\]
These exact specialization ranks prove generic lower bounds 176 and 177
for the two respective matrices. They do **not** yet prove that the generic
rank of the 350-column matrix is at most 176; consequently they do not yet
prove \(n_1n_4\notin\mathcal N^3\). The exact generic rank comparison
remains open.

Reproducible finite-field certificate:
\texttt{certificates/uf072k_degree4_specialization.py}.
