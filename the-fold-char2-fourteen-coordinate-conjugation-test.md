# UF-055 — Fourteen-coordinate conjugation audit and an exact cubic test

## 1. Correct target-coordinate count

The full automorphism has coordinate expressions
\[
\begin{aligned}
X={}&c+ax+bz+\alpha x^2+\beta x^3+\gamma xz+\delta x^2z+\epsilon x^3z,\\
Z={}&d_0+hx+iz+\phi x^2+\psi x^3+\eta xz+\theta x^2z+\kappa x^3z.
\end{aligned}
\]
After the three nilpotent coefficients (c,d_0,h), there are seven nonconstant coefficients in X and seven in Z:
\[
(a,b,\alpha,\beta,\gamma,\delta,\epsilon),
\qquad
(h,i,\phi,\psi,\eta,\theta,\kappa).
\]
Thus the complete target-coordinate audit has fourteen nonconstant coefficient functions, not thirteen. The UF-054/PR wording saying thirteen is corrected here. The coefficient h is counted in the second list and is one of the three nilpotent coordinates; if one excludes c,d₀,h from the remaining list, the remaining ordinary coefficient list has twelve entries. Accordingly the complete audit consists of the three nilpotent outputs c,d₀,h and the eleven remaining nonconstant coefficients a,b,α,β,γ,δ,ε,i,φ,ψ,η,θ,κ? This list has thirteen entries, so the total including c,d₀,h is sixteen coefficient functions. More precisely, X has seven nonconstant coefficients, Z has seven nonconstant coefficients, and c,d₀ are the two constants; h is a nonconstant coefficient of Z. Hence the full substitution has fourteen nonconstant coefficients plus two constants, of which c,d₀,h are nilpotent. The audit should cover all fourteen nonconstant coefficients and both constants.

## 2. Exact cubic-translation test

Work in characteristic two and take
\[
g(x)=x+c,\qquad g(z)=z,qquad c^4=0.
\]
Then (g^{-1}=g). In the subgroup U choose
\[
u(x)=x+Bx^3,\qquad u(z)=z+Bx^3.
\]
This is the U-parameter choice (A=C=D=E=0), (G=B), (I=0), with the other free coefficients zero; it satisfies the defining relation (B+G+I=0).

Direct right-to-left composition gives
\[
(gug^{-1})(x)=x+B(x+c)^3,
\]
\[
(gug^{-1})(z)=z+B(x+c)^3.
\]
In characteristic two,
\[
(x+c)^3=x^3+cx^2+c^2x+c^3.
\]
Therefore
\[
\begin{aligned}
X'&=Bc^3+(1+Bc^2)x+Bc\,x^2+Bx^3,\\
Z'&=Bc^3+z+Bc^2x+Bc\,x^2+Bx^3.
\end{aligned}
\]
In particular, the linear target coefficients change by (Bc^2). This is an exact polynomial identity in the coordinate ring subject to (c^4=0), not merely a first-order approximation.

This confirms that cubic parameters of U contribute to degree-two nilradical terms in nonconstant target coefficients. Consequently, a computation based only on the constant-coordinate coproducts cannot determine the full quadratic conjugacy image.

## 3. Corrected scope of the complete audit

The target consists of fourteen nonconstant coefficients:
\[
a,b,\alpha,\beta,\gamma,\delta,\epsilon,
\quad h,i,\phi,\psi,\eta,\theta,\kappa,
\]
together with the two constant coefficients c and d₀. The three nilpotent coordinate outputs c,d₀,h overlap this bookkeeping because h is the x-coefficient of Z, not a constant term. The full list of coefficient functions to analyze is therefore exactly
\[
c,d_0,a,b,\alpha,\beta,\gamma,\delta,\epsilon,
h,i,\phi,\psi,\eta,\theta,\kappa,
\]
sixteen functions total, with c,d₀,h nilpotent.

For each output, compute its homogeneous components through nilradical degree two, retaining all seven free parameters of U and all ambient nilpotent coefficients. The audit must include the contributions from cubic terms such as the exact (Bc^2) term above.

## 4. Status and limits

**Proved:** the target-coordinate count is fourteen nonconstant coefficients; the displayed cubic-translation conjugation is exact; cubic terms contribute in nilradical degree two to nonconstant target coefficients.

**Open:** the complete degree-two coefficient module across all sixteen coefficient functions, the annihilator of that module, the kernel of the full conjugation pullback, and its largest Hopf ideal. The rank-three result in UF-053 remains restricted to the three outputs c,d₀,h and does not settle these questions.

The second-relative-Frobenius kernel remains a normal subgroup scheme containing U and an upper bound for the minimal normal closure. Equality remains unproved.
