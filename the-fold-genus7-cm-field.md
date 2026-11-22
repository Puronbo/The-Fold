# G-28 — CM real subfield of the genus-seven simple factor

## Input

The genus-seven curve's Weil polynomial factors as
\[
P_C(T)=(1+2T^2)^2(1+2T+2T^2)Q(T),
\]
where
\[
Q(T)=1+4T+6T^2+4T^3+2T^4+8T^5+24T^6+32T^7+16T^8.
\]
The monic Frobenius polynomial of the four-dimensional factor is
\[
F(X)=X^8Q(1/X)
=X^8+4X^7+6X^6+4X^5+2X^4+8X^3+24X^2+32X+16.
\]
G-27 proves that F is irreducible over Q. Its roots are Weil 2-numbers.

## Reciprocal symmetry and real generator

Direct coefficient comparison gives
\[
X^8F(2/X)=16F(X).
\]
For a root \(\pi\), the conjugate root is therefore \(2/\pi\). Put
\[
\beta=\pi+2/\pi.
\]
Eliminating X from F(X)=0 and X²−βX+2=0 gives
\[
\operatorname{Res}_X(F(X),X^2-YX+2)
=16g(Y)^2,
\]
where
\[
g(Y)=Y^4+4Y^3-2Y^2-20Y-14.
\]
The identity is certified by certificates/g28_cm_real_subfield.py: reduce F(X) to A(Y)X+B(Y) modulo X²−YX+2, then take the quadratic norm 2A²+YAB+B².

Modulo 3,
\[
g(Y)\equiv Y^4+Y^3+Y^2+Y+1=\Phi_5(Y).
\]
Since the order of 3 in (Z/5Z)^× is 4, Phi_5 is irreducible over F_3, so g is irreducible over Q. Hence [Q(β):Q]=4. The polynomial discriminant is
\[
\operatorname{disc}(g)=4352=2^8\cdot17.
\]
This is the discriminant of the displayed polynomial, not yet a claim about the full ring-of-integers discriminant.

## CM and endomorphism consequence

For a Weil q-number π with no real embeddings, the standard Weil-number characterization says that Q(π) is a CM field and that Q(π+q/π) is its maximal totally real subfield. Here q=2, and the irreducible degree-eight F gives [Q(π):Q]=8. Thus
\[
Q(\pi)^+=Q(\pi+2/\pi),
\qquad [Q(\pi)^+:Q]=4.
\]
The extension is quadratic and totally imaginary over the displayed totally real quartic field.

Because the characteristic polynomial is irreducible (not a nontrivial power), Honda–Tate theory gives the simple fourfold's endomorphism algebra over F_2 as the field Q(π), rather than a noncommutative division algebra. This identifies its CM field and maximal real subfield explicitly.

## Scope

Established: the resultant identity, irreducibility of g, degree-four real subfield, polynomial discriminant, and CM-field identification. Not established: the integral basis of Q(β), its field discriminant, the relative discriminant of the CM quadratic extension, or the Galois group/normal closure of either field.

## References

- K. Eisenträger, Honda–Tate theory, Theorem 4.1 and the Weil-number discussion: https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/a/166357/files/2023/06/hondatate.pdf
- Isogeny Classes of Abelian Varieties over Finite Fields in the LMFDB, Lemma 2.2 (Weil numbers and maximal real subfields): https://par.nsf.gov/servlets/purl/10327895
