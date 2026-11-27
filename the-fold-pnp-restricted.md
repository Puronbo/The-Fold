# Restricted P vs NP track: a precise first equality

## Status

This note fixes a **working interpretation** of the user's notation

\[
P\ne NP,\qquad P_1=NP_1.
\]

The unrestricted statement \(P\ne NP\) is open. The symbols \(P_1\) and \(NP_1\) are not standard complexity-class notation, so they must be defined before an equality can be proved.

For this first restricted result, \(P_1\) and \(NP_1\) name the deterministic and nondeterministic acceptance languages for one explicitly restricted decision task. They do **not** mean that all deterministic and nondeterministic polynomial-time languages become equal on an arbitrary restricted universe.

## 1. The restricted instance family

An instance is a pair \((G,\mathcal T)\), where:

- \(G=(V,E)\) is a finite, undirected, loop-free graph;
- \(\mathcal T\) is a supplied tree decomposition of \(G\);
- every bag of \(\mathcal T\) contains at most four vertices (treewidth at most 3).

The encoding includes the graph and the decomposition. Its length is \(N\). The decomposition is part of the input, not something the algorithm is required to discover.

A valid tree decomposition satisfies:

1. every vertex occurs in at least one bag;
2. every edge has both endpoints together in some bag;
3. for each vertex, the bags containing it form a connected subtree.

Invalid encodings are rejected. The restricted decision task asks whether \(G\) has a proper 3-colouring.

Let \(L_1\) be the set of valid encodings in this family whose graph is 3-colourable.

## 2. The two acceptance languages

Define:

- \(P_1\): encodings accepted by the deterministic dynamic-programming algorithm below;
- \(NP_1\): encodings for which there exists a certificate consisting of a 3-colouring of \(V\), accepted by the polynomial-time edge-checking verifier.

The intended theorem is

\[
\boxed{P_1=NP_1=L_1.}
\]

This is an equality of the two procedures' accepted-instance sets for this fixed restricted task. It is **not** the general class equality \(P=NP\).

## 3. Deterministic dynamic programming

Root the supplied decomposition tree. For each bag \(B_t\), enumerate its at most \(3^4=81\) assignments \(c:B_t\to\{0,1,2\}\).

A state \(c\) is feasible at node \(t\) when:

1. it is proper on every graph edge whose endpoints both lie in \(B_t\);
2. for every child \(u\) of \(t\), there is a feasible state \(d\) at \(u\) such that
   \[
   c|_{B_t\cap B_u}=d|_{B_t\cap B_u}.
   \]

The algorithm accepts exactly when the root has at least one feasible state. Empty bags and disconnected graphs are allowed; the decomposition tree can be rooted componentwise or connected by an empty root.

### Correctness invariant

For every node \(t\), a bag assignment is feasible if and only if it extends to a proper 3-colouring of all vertices appearing in the subtree rooted at \(t\), subject to the prescribed colours on \(B_t\).

**Soundness.** Compatible child colourings agree with the parent assignment on intersections. The connectedness condition for each vertex ensures that a vertex shared across multiple descendant bags cannot acquire inconsistent colours. Every graph edge is contained in some bag, where the local properness check enforces different endpoint colours. Thus a feasible root state yields a proper colouring of all of \(G\).

**Completeness.** Given a proper colouring of \(G\), restrict it to every bag. Every restriction is locally proper, and adjacent bags agree on their intersection. Induction from leaves to root shows that each restricted assignment is feasible. Hence the root has a feasible state.

Therefore the deterministic algorithm accepts exactly the 3-colourable valid instances.

## 4. Polynomial running time

Each bag has at most 81 states. For each decomposition-tree edge, compatibility can be checked by comparing at most 81 parent states with at most 81 child states. The work per tree edge is therefore bounded by a constant independent of the input size. Validation of the decomposition and local edge constraints is polynomial in the supplied encoding length.

Thus the algorithm runs in \(O(N)\) time after ordinary linear-time or polynomial-time encoding validation (a conservative implementation may use a higher polynomial bound without changing the result). In particular, \(L_1\in P\).

The nondeterministic verifier guesses one of three colours for each vertex and checks every edge. It runs in polynomial time, so \(L_1\in NP\).

Since both procedures accept exactly \(L_1\),

\[
P_1=L_1=NP_1.
\]

## 5. What this establishes — and what it does not

**Established by the argument above, once the implementation follows the stated recurrence:**

- the restricted 3-colourability task with a supplied width-at-most-3 decomposition is in deterministic polynomial time;
- its polynomial-time certificate verifier and deterministic algorithm have the same acceptance set;
- the restricted equality is independent of any assumption about unrestricted \(P\) versus \(NP\).

**Not established:**

- \(P\ne NP\);
- \(P=NP\);
- equality of all deterministic and nondeterministic complexity classes on arbitrary restricted families;
- a polynomial-time algorithm for 3-colourability on unrestricted graphs;
- a proof that finding a width-at-most-3 decomposition is easy for arbitrary graphs (the decomposition is supplied and validated).

The restriction is genuinely structural. It bounds the bag size, making the dynamic-programming state space constant. Removing that bound changes the complexity analysis.

## 6. Formalization plan

The Lean development should separate the proof into independently auditable pieces:

1. finite graph and tree-decomposition definitions;
2. validation of vertex coverage, edge coverage, and running intersection;
3. finite bag-colouring states;
4. the bottom-up feasibility recurrence;
5. the subtree-extension invariant;
6. soundness and completeness of the root test;
7. a cost recurrence bounded by a polynomial in the encoded input size;
8. equivalence with the certificate verifier.

A proof of logical correctness alone is not a complexity proof. The Lean model must include an explicit size measure and a bound on the number of operations, or be paired with a verified cost semantics.

## 7. Research boundary

The restricted equality is a valid small theorem target. It offers a test case for the repository's abstraction and verification machinery: a structural restriction reduces the search space while preserving the answer.

The unrestricted separation target remains open. No bridge from this restricted family to all of \(P\) and \(NP\) is supplied here. Any proposed bridge must be proved without assuming the desired separation or equality.
