# Stage 27 — Orbit–stabilizer reconstruction and selector information

## From a two-choice fold to a finite group action

A Fold involution gives each orbit at most two states. Once a representative
is chosen, one Boolean selector distinguishes the representative from its
folded partner. A general finite group action can have larger orbits, so a
Boolean selector is no longer sufficient in general.

Let a finite group \(G\) act on a state space \(X\). For a selected
representative \(x\), define

\[
G\cdot x=\{g\cdot x:g\in G\},\qquad
\operatorname{Stab}_G(x)=\{g\in G:g\cdot x=x\}.
\]

The quotient observation identifies all states in \(G\cdot x\). To
reconstruct the particular state, the selector must identify an orbit
member, not a particular group element.

## Orbit–stabilizer theorem

For a finite group action,

\[
|G\cdot x|=\frac{|G|}{|\operatorname{Stab}_G(x)|}.
\]

**Reason.** Two group elements \(g_1,g_2\) produce the same state exactly
when \(g_2^{-1}g_1\in\operatorname{Stab}_G(x)\). Thus the elements
producing any one orbit state form a coset of the stabilizer. These cosets
partition \(G\), each has size \(|\operatorname{Stab}_G(x)|\), and
there are \(|G\cdot x|\) distinct orbit states.

This identifies the selector redundancy exactly: each state in the orbit
has \(|\operatorname{Stab}_G(x)|\) group-element selectors that produce
it. Stabilizer elements are not additional observable states.

## Selector capacity

If the orbit contains \(m\) states, any exact selector needs at least
\(m\) distinct values. A fixed-width binary encoding therefore needs

\[
b_{\min}=\lceil\log_2 m\rceil
\]

bits. A singleton orbit needs zero bits; a two-state orbit needs one bit;
a three-state orbit needs two fixed-width bits. The ideal information
content \(\log_2 m\) need not be an integer and is not the same as a
fixed-width code length.

If, separately, the orbit members are assigned equal normalized shares,
each receives \(1/m\). The two-member case is the familiar

\[
\frac{n}{n+n}=\frac12\qquad(n\ne0).
\]

This equal-share normalization is not the selector bit count: \(1/m\)
measures a share, while \(\lceil\log_2 m\rceil\) measures the fixed-width
binary capacity needed to distinguish the orbit members.

For a finite permutation group, the module agi/symmetry_actions.py now
computes an OrbitReconstructionProfile for every state. It reports the orbit size,
stabilizer, group size, selector redundancy, and exact minimum fixed-width
bit count. The implementation checks the orbit–stabilizer identity for
each state and rejects transformation collections that are not groups.

## Examples

- **Two-state swap:** \(|G|=2\), stabilizer size \(1\), orbit size \(2\);
  one selector bit recovers either state.
- **Three-state cyclic action:** \(|G|=3\), stabilizer size \(1\), orbit
  size \(3\); two fixed-width bits distinguish the three states.
- **Three vertices under all permutations:** \(|G|=6\), stabilizer size
  \(2\), orbit size \(3\). Two group elements produce each particular
  vertex, but only three distinct selector outcomes are needed.
- **A fixed state under a two-element group:** orbit size \(1\), stabilizer
  size \(2\); no selector bit is needed because every group element leaves
  that state unchanged.

## Connection to the quotient chart

The quotient class determines the orbit, not the particular member. A
representative section plus an orbit-member selector reconstructs a state.
For a group action, choosing a group element is one possible encoding, but
it is redundant by the stabilizer. The right-coset space \(G/\operatorname{Stab}_G(x)\) is the natural
selector space for the left-action convention used here. This is a coset
space, not necessarily a quotient group: the stabilizer need not be normal.

The existing Lean Fold development proves the two-element involution case.
The new Python profile generalizes the finite computational audit to
explicit permutation groups. It is not yet a Lean formalization of arbitrary
group actions.

## Scope and limits

The computation assumes a finite set of states and an explicitly supplied
finite set of distinct permutations containing identity and closed under
composition. It analyzes that permutation group, a faithful representation
of the acting group. It does not infer an action from raw data, establish
symmetry in a physical system, or prove claims about arbitrary infinite
groups. The orbit–stabilizer statement itself is a standard finite-group
theorem; the repository contribution here is its application to selector
redundancy and reconstruction accounting.
