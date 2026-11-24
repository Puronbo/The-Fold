# Recursive power feedback: tower bounds and temporal convexity

## G-EP205 — A tower sandwich for exponent feedback

Consider the integer recurrence, for a fixed integer base n >= 2,

\[
x_0=n,\qquad x_{t+1}=n^{x_t+1}.
\]

Let the base-n power tower and base-n-squared power tower be defined by

\[
T_0=U_0=n,\qquad T_{t+1}=n^{T_t},\qquad
U_{t+1}=(n^2)^{U_t}.
\]

Then, for every integer t >= 1,

\[
\boxed{T_t < x_t \le U_t.}
\]

### Proof

At t=1,
\[
T_1=n^n<n^{n+1}=x_1
\]
and, since n+1 <= 2n,
\[
x_1=n^{n+1}\le n^{2n}=(n^2)^n=U_1.
\]

Assume T_t < x_t <= U_t. The map z -> n^{z+1} is strictly increasing, so
\[
x_{t+1}=n^{x_t+1}>n^{T_t}=T_{t+1}.
\]
Also x_t >= n >= 2, hence x_t+1 <= 2x_t <= 2U_t. Therefore
\[
x_{t+1}=n^{x_t+1}\le n^{2U_t}=(n^2)^{U_t}=U_{t+1}.
\]
Induction proves the claim.

This sandwiches the feedback recurrence between towers of the same height, with bases n and n^2. It is a rigorous growth-scale comparison, not a claim that the recurrence equals either tower.

## G-EP206 — Strict temporal convexity

For every t >= 0, x_t >= 2 and
\[
x_{t+1}=n^{x_t+1}\ge 2^{x_t+1}>2x_t.
\]
The last inequality follows from 2^{x_t}>x_t for integer x_t >= 2.

Consequently, for every t >= 1,
\[
\boxed{x_{t+1}-2x_t+x_{t-1}>0.}
\]
Indeed x_{t+1}>2x_t and x_{t-1}>0. Thus the sequence is strictly discretely convex: its first differences are strictly increasing.

This is stronger than merely proving that x_t is increasing or unbounded.

## G-EP207 — Exact operator-order gap

Let P_n(x)=n^x and T(x)=x+1. Then
\[
(P_n\circ T)(x)-(T\circ P_n)(x)
=n^{x+1}-(n^x+1)
=(n-1)n^x-1.
\]
For integers n >= 2 and x >= 1 this is strictly positive. Hence increment-before-exponentiation strictly dominates exponentiation-before-increment on this domain.

With the commutator convention [T,P_n]=T o P_n - P_n o T, the commutator is
\[
[T,P_n](x)=1-(n-1)n^x<0.
\]
The sign depends on the stated convention; the underlying order comparison does not.

## Logarithmic coordinate

Writing y_t=log_n(x_t) gives the exact identity
\[
y_{t+1}=x_t+1=n^{y_t}+1.
\]
This coordinate change makes the outer power visible as a one-level exponential recurrence. It does not make the sequence small: y_t itself grows rapidly.

## Scope and caveats

- The tower sandwich is proved for integer n >= 2 and integer t >= 1.
- The temporal convexity statement is exact for all t >= 1.
- The operator-order inequality is stated for integer n >= 2, x >= 1.
- None of these statements classifies arbitrary self-modifying operators or all possible growth hierarchies.
- These are analytic results for the recursive-power branch; they do not by themselves establish a new theorem about finite-field composition excess.

