#!/usr/bin/env python3
"""UF-010: parity, multiplicity, singularity, and disconnected-support checks.

This is a finite reference checker, not a solver for arbitrary analytic-germ
principality. Local principality and odd-support complement connectivity are
explicit inputs. The companion note states the global analytic theorem.
"""
from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from math import sin, pi
from typing import Iterable, Mapping, Sequence

Covector = tuple[int, int]
Point = tuple[float, float]


@dataclass(frozen=True)
class DivisorComponent:
    name: str
    multiplicity: int
    homology: tuple[int, int]
    locally_principal: bool = True

    def __post_init__(self):
        if self.multiplicity <= 0 or any(v not in (0, 1) for v in self.homology):
            raise ValueError("use positive multiplicities and a mod-2 homology pair")


def classify_divisor(components: Sequence[DivisorComponent], odd_support_disconnects: bool) -> dict:
    """Corollary 3.7 parity criterion for a locally finite effective divisor."""
    odd = [c for c in components if c.multiplicity % 2]
    if not odd:
        return {"principal": True, "case": "all-even", "odd_names": (),
                "mod2_class": (0, 0), "reason": "positive even divisors have positive analytic equations"}
    cls = tuple(sum(c.homology[j] for c in odd) % 2 for j in (0, 1))
    local = all(c.locally_principal for c in components)
    zero = cls == (0, 0)
    ok = local and zero and odd_support_disconnects
    failures = []
    if not local: failures.append("component ideal not locally principal")
    if not zero: failures.append("odd-support mod-2 class nonzero")
    if not odd_support_disconnects: failures.append("complement of odd support connected")
    return {"principal": ok, "case": "odd/mixed", "odd_names": tuple(c.name for c in odd),
            "mod2_class": cls, "reason": "all conditions hold" if ok else "; ".join(failures)}


def dual_bipartite(vertices: Iterable[int], edges: Iterable[tuple[int, int]]) -> bool:
    """Bipartite test for a face-dual multigraph; self-loops fail."""
    vs = tuple(vertices)
    vset = set(vs)
    adj = {v: [] for v in vs}
    for u, v in edges:
        if u not in vset or v not in vset:
            raise ValueError("edge endpoint not in graph")
        adj[u].append(v); adj[v].append(u)
    colour = {}
    for root in vs:
        if root in colour: continue
        colour[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                want = 1-colour[u]
                if v not in colour:
                    colour[v] = want; q.append(v)
                elif colour[v] != want:
                    return False
    return True


def parallel_loop_dual(n: int):
    """Face dual of n parallel essential circles: C_n; n=1 gives a loop."""
    if n < 1: raise ValueError("n must be positive")
    return tuple(range(n)), tuple((i, (i+1) % n) for i in range(n))


def torus_parity_vector(families: Sequence[tuple[Covector, float, int]]) -> tuple[int, int]:
    """Return sum(m*n) mod 2; zero iff the sine product descends to T^2."""
    return (sum(n[0]*m for n, _c, m in families) % 2,
            sum(n[1]*m for n, _c, m in families) % 2)


def _gcd(a: int, b: int) -> int:
    while b: a, b = b, a % b
    return abs(a)


def torus_product(x: Point, families: Sequence[tuple[Covector, float, int]]) -> float:
    """Exact analytic sine product for affine rational crease circles on T^2."""
    if torus_parity_vector(families) != (0, 0):
        raise ValueError("odd divisor class is nonzero; product is antiperiodic")
    value = 1.0
    used = set()
    for (a, b), c, m in families:
        if (a, b) == (0, 0) or _gcd(abs(a), abs(b)) != 1 or m <= 0:
            raise ValueError("normal must be primitive and multiplicity positive")
        c %= 1.0
        if a < 0 or (a == 0 and b < 0):
            key = ((-a, -b), round((-c) % 1.0, 12))
        else:
            key = ((a, b), round(c, 12))
        if key in used: raise ValueError("duplicate affine crease circle")
        used.add(key)
        value *= sin(pi*(a*x[0] + b*x[1] - c))**m
    return value


def local_vanishing_order(component_orders: Sequence[int], multiplicities: Sequence[int]) -> int:
    """For unit*product(f_i**m_i), return sum(m_i*ord(f_i))."""
    if not component_orders or len(component_orders) != len(multiplicities):
        raise ValueError("matching nonempty lists required")
    if any(x <= 0 for x in (*component_orders, *multiplicities)):
        raise ValueError("orders and multiplicities must be positive")
    return sum(a*b for a, b in zip(component_orders, multiplicities))


def multiplicities_invariant(m: Mapping[str, int], permutation: Mapping[str, str]) -> bool:
    """A group element preserves a weighted divisor only if m is constant on orbits."""
    if set(m) != set(permutation) or set(m) != set(permutation.values()): return False
    return all(m[k] == m[permutation[k]] for k in m)


def verify() -> dict[str, int]:
    pair = [DivisorComponent("x=0",1,(0,1)), DivisorComponent("x=1/2",1,(0,1))]
    assert classify_divisor(pair, True)["principal"]
    assert not classify_divisor([pair[0]], False)["principal"]

    triple = [DivisorComponent(f"x={i}/3",1,(0,1)) for i in range(3)]
    triple_result = classify_divisor(triple, True)
    assert not triple_result["principal"] and triple_result["mod2_class"] == (0,1)

    four = [DivisorComponent(f"x={i}/4",1,(0,1)) for i in range(4)]
    assert classify_divisor(four, True)["principal"]
    assert classify_divisor([DivisorComponent("double loop",2,(0,1))],False)["principal"]
    mixed = pair + [DivisorComponent("even loop x=1/4",2,(0,1))]
    assert classify_divisor(mixed, True)["principal"]
    bad_local = [DivisorComponent("singular nonprincipal",1,(0,1),False),pair[1]]
    assert not classify_divisor(bad_local, True)["principal"]

    dual_checks = 0
    for n, expected in {1:False,2:True,3:False,4:True,6:True}.items():
        v,e = parallel_loop_dual(n)
        assert dual_bipartite(v,e) is expected
        dual_checks += 1

    pair_formula = (((1,0),0.0,1),((1,0),0.5,1))
    double_formula = (((1,0),0.0,2),)
    mixed_formula = (((1,0),0.0,1),((1,0),0.5,1),((1,0),0.25,2))
    high_odd = (((1,0),0.0,3),((1,0),0.5,5))
    bad_three = (((1,0),0.0,1),((1,0),1/3,1),((1,0),2/3,1))
    for fam in (pair_formula,double_formula,mixed_formula,high_odd):
        assert torus_parity_vector(fam) == (0,0)
    assert torus_parity_vector(bad_three) == (1,0)
    assert local_vanishing_order((1,1),(3,5)) == 8
    assert local_vanishing_order((2,),(3,)) == 6  # cusp germ y^2-x^3, weight 3
    assert local_vanishing_order((1,1),(1,1)) == 2  # node xy

    samples=((.137,.271),(.193,.347),(.311,.127),(.227,.419))
    periodic=nonzero=0
    for fam in (pair_formula,double_formula,mixed_formula,high_odd):
        for x,y in samples:
            value=torus_product((x,y),fam)
            assert abs(value)>1e-9
            nonzero+=1
            for k in range(-2,3):
                assert abs(torus_product((x+k,y),fam)-value)<1e-9
                assert abs(torus_product((x,y+k),fam)-value)<1e-9
                periodic+=2

    zero_checks=0
    for y in (.13,.37,.81):
        for x in (0.0,.5):
            assert abs(torus_product((x,y),pair_formula))<1e-10
            zero_checks+=1
        for x in (0.0,.5,.25):
            assert abs(torus_product((x,y),mixed_formula))<1e-10
            zero_checks+=1
        for x in (0.0,.5):
            assert abs(torus_product((x,y),high_odd))<1e-10
            zero_checks+=1
        assert abs(torus_product((0.0,y),double_formula))<1e-10
        zero_checks+=1

    swap={"x=0":"x=1/2","x=1/2":"x=0"}
    assert multiplicities_invariant({"x=0":1,"x=1/2":1},swap)
    assert not multiplicities_invariant({"x=0":1,"x=1/2":3},swap)
    return {"weighted_divisor_cases":7,"parallel_loop_duals":dual_checks,
            "torus_periodicity_checks":periodic,"exact_zero_samples":zero_checks,
            "generic_nonzero_samples":nonzero,"local_order_examples":3,
            "component_permutation_checks":2}


def main() -> None:
    print("UF-010 weighted-divisor parity classification")
    examples={
        "one odd essential loop":classify_divisor([DivisorComponent("single",1,(0,1))],False),
        "two odd parallel loops":classify_divisor([
            DivisorComponent("x=0",1,(0,1)),DivisorComponent("x=1/2",1,(0,1))],True),
        "three odd parallel loops":classify_divisor([
            DivisorComponent(str(i),1,(0,1)) for i in range(3)],True),
        "one even essential loop":classify_divisor([DivisorComponent("double",2,(0,1))],False),
    }
    for name,result in examples.items():
        print(name,"=> principal:",result["principal"],"mod2:",result["mod2_class"],"reason:",result["reason"])
    print("verification:",verify())


if __name__=="__main__":
    main()
