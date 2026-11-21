# UF-030 — Modular stability of the D16 Lie algebra and its commutator

## Scope and coefficient rings

Let \(\mathfrak u\) be the seven-dimensional characteristic-zero Lie algebra of UF-028, with coordinates \((a,b,c,d,e,u,v)\), and let \(Z=\langle U,V\rangle\) be its two-dimensional center. UF-029 identifies its D16 action over a characteristic-zero field containing \(\sqrt2\).

This note separates three questions that must not be conflated:

1. whether a finite-group representation is semisimple;
2. whether its irreducible summands are defined over the chosen ground field;
3. whether the integral alternating bracket retains its rank after reduction.

The displayed orthogonal D16 matrices contain \(1/2\) and \(1/\sqrt2\). They define a representation over characteristic-zero fields containing \(\sqrt2\), and over algebraically closed fields of odd characteristic after choosing a square root of 2. They do **not**, by themselves, define an integral representation over \(\mathbb Z\) that can simply be reduced modulo 2. Accordingly, the characteristic-two bracket calculation below is a statement about the integral structure-constant map, not a claim that the particular orthogonal D16 action of UF-029 has been specialized to characteristic two.

## Theorem 1 — Odd-characteristic semisimplicity

Let \(k\) be an algebraically closed field of characteristic \(p\ne2\). The D16 representation on \(\mathfrak u_k\) obtained from the UF-029 matrices is semisimple and has decomposition
\[
\boxed{\mathfrak u_k\simeq E_1\oplus E_2\oplus\chi\oplus E_3.}
\]
Here the generator \(r\) has eigenvalue pairs
\[
E_1:\{\zeta_8,\zeta_8^{-1}\},\quad
E_2:\{\zeta_8^2,\zeta_8^{-2}\},\quad
E_3:\{\zeta_8^3,\zeta_8^{-3}\},
\]
and \(\chi(r)=-1,\chi(s)=1\).

**Proof.** Since \(p\nmid |D_{16}|=16\), Maschke's theorem gives semisimplicity. In an algebraic closure, the eighth roots of unity are available. For odd \(p\), the polynomial \(T^8-1\) has no repeated roots, so the three inverse eigenvalue pairs above remain distinct. The explicit invariant subspaces from UF-029 therefore remain pairwise non-isomorphic and retain their dimensions. Their dimensions sum to seven. \(\square\)

Thus, among prime characteristics in which this D16 representation is defined by the displayed normalized matrices, there is no odd-prime semisimplicity exception.

## Ground-field splitting

Over a non-algebraically-closed field of odd characteristic, the geometric decomposition above need not be a decomposition into absolutely split summands over that field. The relevant character fields are:

- \(E_1\) and \(E_3\): traces of \(r\) involve \(\sqrt2\);
- \(E_2\): traces of \(r\) involve \(0\), while its eigenvalues require \(i=\sqrt{-1}\).

Consequently, whether these representations are realized in the same split form over the ground field depends on whether 2 and -1 are squares there. This is a field-of-definition issue, not a failure of Maschke semisimplicity. Over an algebraic closure, the decomposition in Theorem 1 is uniform for every odd prime.

## Theorem 2 — The integral commutator map is universally surjective

Use the integral structure constants of UF-028 to define
\[
B:\Lambda^2\mathbb Z^5\longrightarrow\mathbb Z^2,
\]
where the five noncentral coordinates are \((a,b,c,d,e)\), and the target coordinates are \((u,v)\). Its components are
\[
\begin{aligned}
B_u&=a_1d_2-a_2d_1+2(b_1c_2-b_2c_1)-b_1e_2+b_2e_1,\\
B_v&=-a_1c_2+a_2c_1+2(a_1e_2-a_2e_1)-b_1d_2+b_2d_1.
\end{aligned}
\]
The Smith normal form of its \(2\times10\) matrix is
\[
\boxed{\operatorname{SNF}(B)=\operatorname{diag}(1,1).}
\]
In particular, for every field \(k\), including characteristic two, the reduced map \(B_k:\Lambda^2 k^5\to k^2\) is surjective.

**Proof.** Every matrix entry is divisible by 1, so the first determinantal divisor is 1. The columns corresponding to \(a\wedge d\) and \(a\wedge c\) form a \(2\times2\) minor with determinant \(\pm1\). Hence the second determinantal divisor is also 1. The Smith invariant factors are therefore \((1,1)\), and the map has rank two after reduction modulo every prime. \(\square\)

The use of \(a\wedge d\) and \(a\wedge c\) is important: the coefficient 2 in some other entries does not create an exceptional prime.

## Theorem 3 — The center of the reduced alternating algebra remains two-dimensional

For the reduced two-step alternating algebra defined by \(B_k\), the radical of the bracket on the five-dimensional quotient is zero in every characteristic. Thus its center is exactly the designated two-dimensional target \(Z_k\), and its derived algebra is also \(Z_k\).

**Proof.** If \((a,b,c,d,e)\) brackets to zero with every vector, test successively against the five coordinate basis vectors. The coefficient-one pairings include
\[
(a,d)\mapsto B_u,\quad (a,c)\mapsto -B_v,\quad
(b,e)\mapsto -B_u,\quad (b,d)\mapsto -B_v,
\]
and the remaining pairings \((b,c)\mapsto 2B_u\), \((a,e)\mapsto2B_v\). The coefficient-one relations force each of \(a,b,c,d,e\) to vanish; this remains true in characteristic two. Surjectivity from Theorem 2 identifies the derived algebra with all of \(Z_k\). \(\square\)

This is a statement about the reduction of the integral alternating bracket. In characteristic two, alternating and skew-symmetric forms must be distinguished: the bracket remains alternating because it is defined on \(\Lambda^2\), even though minus signs equal plus signs.

## Conclusions and limits

1. **Semisimplicity:** the only prime dividing \(|D_{16}|\) is 2. Every odd-characteristic D16 representation is semisimple.
2. **Geometric decomposition:** over an algebraic closure of any odd characteristic, the four summands in UF-029 remain distinct and multiplicity-free.
3. **Ground-field form:** splitting over a nonclosed field can vary with square roots of 2 and -1; this is not a new modular eigenprime.
4. **Bracket rank:** the integral commutator map has Smith invariants \((1,1)\), so no prime, including 2, lowers its rank.
5. **Characteristic two caution:** the normalized orthogonal D16 matrices of UF-029 do not furnish a direct integral reduction at 2. A separate integral model of the group action is required before asserting a characteristic-two D16-module decomposition.

The project-local term “modular eigenprime” should therefore be used only after specifying an integral group module and a comparison rule for its reductions. For the bracket map itself, there is no exceptional prime. For the D16 module, all odd primes are uniform geometrically; characteristic two remains outside the present normalized model rather than being a proved reduction of it.

## Reproducibility

Run:

`python3 tools/fold_d16_modular_stability.py`

The verifier checks the integer bracket matrix, its unit minor, surjectivity modulo a range of primes, and the radical of the five-dimensional quotient bracket by exact arithmetic.

## Follow-up

**UF-030-A.** Construct an integral D16-stable lattice (or prove an obstruction to one compatible with the chosen normalization), then classify its reduction in characteristic two. This is the missing prerequisite for a genuine characteristic-two modular decomposition of the UF-029 representation.
