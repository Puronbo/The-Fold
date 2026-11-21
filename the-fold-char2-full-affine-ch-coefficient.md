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
