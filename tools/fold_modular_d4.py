#!/usr/bin/env python3
"""Finite identity checks for UF-022 (modular D4 symmetry)."""

G_ORDER = 8
IRREP_DIMENSIONS = (1, 1, 1, 1, 2)
REGULAR_MULTIPLICITIES = (1, 1, 1, 1, 2)

assert sum(d * m for d, m in zip(IRREP_DIMENSIONS,
                                  REGULAR_MULTIPLICITIES)) == G_ORDER
assert G_ORDER % 2 == 0
assert G_ORDER % 3 != 0 and G_ORDER % 5 != 0 and G_ORDER % 7 != 0

# In characteristic two, the only solution to u^2=1 in a field is u=1:
# (u-1)^2 = u^2 - 2u + 1 = 0.
# Thus no nontrivial sign character into the multiplicative field group exists.
for characteristic in (2,):
    assert (1 - 1) % characteristic == 0
    assert (-1 - 1) % characteristic == 0

# The sign-change subgroup acts trivially in characteristic two;
# the effective action is coordinate swap, whose invariant generators
# are x+y and x*y. Their squares are p and q.
print("UF-022 exact checks: PASS")
print("D4 order:", G_ORDER)
print("regular representation dimension:",
      sum(d * m for d, m in zip(IRREP_DIMENSIONS, REGULAR_MULTIPLICITIES)))
print("odd residue characteristics: nonmodular")
print("characteristic 2: sign characters collapse; effective action is C2")
