# G-EP55 — Minimal-chain annihilator complements

G-EP55 introduces `tools/minimal_chain_decoupling_completion.py`. It retains
the minimal-chain bases from G-EP52 and computes simultaneous annihilator
spaces for possible complementary basis vectors.

For the domain complement, candidates lie in the common kernel of the left
chain rows applied to both pencil coefficient matrices. For the codomain
complement, candidate covectors annihilate both coefficient images of the
right-chain domain. A greedy exact basis-extension check determines whether
these candidate spaces can complete the fixed chain bases.

When both extensions exist, the tool constructs S and T, computes SQT and
SKT, and explicitly checks that both off-diagonal blocks vanish. When an
extension fails, it reports which side failed and makes no impossibility claim
about other complements, other chain bases, or general strict equivalence.

This is a constructive sufficient method, not a universal splitting theorem.
It does not certify regularity of the bottom-right block. All arithmetic is
exact over the supplied prime field.

Tests cover exact nullspace equations, the zero-chain regular case, and a
mixed singular fixture. The mixed test accepts either a verified positive
construction or a clearly reported limitation of this fixed-basis strategy.
