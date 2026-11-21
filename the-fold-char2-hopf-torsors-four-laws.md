# Fppf torsors for all four Fold Hopf structures (G-4)

Let k be a field of characteristic two. For n=1,2, the standard fppf exact sequences give
\[
H^1_{\mathrm{fppf}}(k,\alpha_{2^n})\cong k/k^{2^n},
\qquad
H^1_{\mathrm{fppf}}(k,\mu_{2^n})
\cong k^\times/(k^\times)^{2^n}.
\]
For alpha, use
\[
0\to\alpha_{2^n}\to\mathbb G_a
\xrightarrow{F^n}\mathbb G_a^{(2^n)}\to0
\]
and \(H^1(k,\mathbb G_a)=0\). For mu, use the fppf Kummer sequence
\[
1\to\mu_{2^n}\to\mathbb G_m
\xrightarrow{(\cdot)^{2^n}}\mathbb G_m\to1
\]
and \(\operatorname{Pic}(k)=0\).

Since H^1 of a product of commutative group schemes is the product of the H^1 groups, the four Fold group laws have the following torsor classes.

## 1. The four cohomology sets

\[
\begin{array}{c|c}
G & H^1_{\mathrm{fppf}}(k,G)\\
\hline
\alpha_4\times\alpha_2 &
(k/k^4)\times(k/k^2)\\
\mu_4\times\alpha_2 &
(k^\times/(k^\times)^4)\times(k/k^2)\\
\alpha_4\times\mu_2 &
(k/k^4)\times(k^\times/(k^\times)^2)\\
\mu_4\times\mu_2 &
(k^\times/(k^\times)^4)\times(k^\times/(k^\times)^2)
\end{array}
\]

The parameters are independent in the two factors. In particular, the four Hopf structures have different natural torsor-classification functors, even though their coordinate algebras are all isomorphic to k[x,z]/(x^4,z^2).

## 2. Explicit torsor algebras

Representatives can be written as follows.

- For alpha_4 x alpha_2, choose a,b in k and use
  \[
  B=k[u,v]/(u^4-a,\ v^2-b),
  \]
  with additive coaction \(u\mapsto u\otimes1+1\otimes x\), \(v\mapsto v\otimes1+1\otimes z\).

- For mu_4 x alpha_2, choose a in k^× and b in k and use
  \[
  B=k[t,v]/(t^4-a,\ v^2-b),
  \]
  with multiplicative coaction \(t\mapsto t\otimes(1+x)\) and additive coaction \(v\mapsto v\otimes1+1\otimes z\).

- For alpha_4 x mu_2, choose a in k and b in k^× and use
  \[
  B=k[u,s]/(u^4-a,\ s^2-b),
  \]
  with additive coaction on u and multiplicative coaction \(s\mapsto s\otimes(1+z)\).

- For mu_4 x mu_2, choose a,b in k^× and use
  \[
  B=k[t,s]/(t^4-a,\ s^2-b),
  \]
  with the two multiplicative coactions.

Each is finite faithfully flat of rank eight over k and is a torsor under the indicated product group scheme. The parameters are taken modulo fourth powers or squares exactly as in the table.

## 3. Perfect and imperfect fields

If k is perfect, both Frobenius maps on k and on k^× are surjective, so all four H^1 sets are trivial. Every torsor under these fixed group schemes is then trivial.

If k is imperfect, the quotient groups can be nonzero. For example, over k=F_2(t), the class of t is not a square and hence is not a fourth power. It gives nontrivial additive and multiplicative torsor classes in the corresponding factors.

These are torsors under the four fixed group schemes. They do not classify all forms of the group schemes themselves, all twists, or all Hopf structures on the underlying algebra.
