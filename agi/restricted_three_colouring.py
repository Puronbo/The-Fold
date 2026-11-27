"""Exact dynamic programming for 3-colourability on supplied width-3 decompositions.

Reference implementation for the restricted P1/NP1 research note. The
supplied decomposition is validated before the finite-state DP is run.
"""
from __future__ import annotations

from itertools import product
from typing import Iterable, Sequence


class InvalidInstance(ValueError):
    """The graph/decomposition encoding is not a valid restricted instance."""


def _normalise_edges(n: int, edges: Iterable[tuple[int, int]]) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    for edge in edges:
        if len(edge) != 2:
            raise InvalidInstance("each graph edge must have two endpoints")
        u, v = edge
        if not (0 <= u < n and 0 <= v < n):
            raise InvalidInstance("edge endpoint outside the vertex set")
        if u == v:
            raise InvalidInstance("self-loops are excluded from this graph model")
        result.add((min(u, v), max(u, v)))
    return result


def validate_decomposition(
    n: int,
    edges: Iterable[tuple[int, int]],
    bags: Sequence[Sequence[int]],
    tree_edges: Iterable[tuple[int, int]],
) -> tuple[set[tuple[int, int]], list[set[int]]]:
    """Validate a tree decomposition with bags of size at most four."""
    if n < 0:
        raise InvalidInstance("vertex count must be nonnegative")
    if not bags:
        raise InvalidInstance("a decomposition must contain at least one bag")

    graph_edges = _normalise_edges(n, edges)
    normal_bags: list[set[int]] = []
    for bag in bags:
        values = list(bag)
        if len(values) > 4:
            raise InvalidInstance("bag size exceeds four (treewidth bound 3)")
        if len(set(values)) != len(values):
            raise InvalidInstance("a bag contains a duplicate vertex")
        if any(v < 0 or v >= n for v in values):
            raise InvalidInstance("bag contains a vertex outside the graph")
        normal_bags.append(set(values))

    t = len(normal_bags)
    adjacency = [set() for _ in range(t)]
    seen_tree_edges: set[tuple[int, int]] = set()
    for u, v in tree_edges:
        if not (0 <= u < t and 0 <= v < t) or u == v:
            raise InvalidInstance("invalid decomposition-tree edge")
        edge = (min(u, v), max(u, v))
        if edge in seen_tree_edges:
            raise InvalidInstance("duplicate decomposition-tree edge")
        seen_tree_edges.add(edge)
        adjacency[u].add(v)
        adjacency[v].add(u)

    visited: set[int] = set()
    stack = [0]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        stack.extend(adjacency[node] - visited)
    if len(visited) != t or len(seen_tree_edges) != t - 1:
        raise InvalidInstance("decomposition index graph is not a tree")

    if set().union(*normal_bags) != set(range(n)):
        raise InvalidInstance("some graph vertex is absent from all bags")
    for u, v in graph_edges:
        if not any(u in bag and v in bag for bag in normal_bags):
            raise InvalidInstance("some graph edge is not covered by a bag")

    for vertex in range(n):
        occurrences = {i for i, bag in enumerate(normal_bags) if vertex in bag}
        start = next(iter(occurrences))
        reached = {start}
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbour in (adjacency[node] & occurrences) - reached:
                reached.add(neighbour)
                stack.append(neighbour)
        if reached != occurrences:
            raise InvalidInstance("running-intersection property fails")

    return graph_edges, adjacency


def is_three_colourable(
    n: int,
    edges: Iterable[tuple[int, int]],
    bags: Sequence[Sequence[int]],
    tree_edges: Iterable[tuple[int, int]],
) -> bool:
    """Decide 3-colourability using at most 81 states per decomposition bag."""
    graph_edges, adjacency = validate_decomposition(n, edges, bags, tree_edges)
    t = len(bags)
    normal_bags = [tuple(bag) for bag in bags]

    parent = [-1] * t
    order: list[int] = []
    stack = [0]
    parent[0] = 0
    while stack:
        node = stack.pop()
        order.append(node)
        for child in adjacency[node]:
            if child != parent[node]:
                parent[child] = node
                stack.append(child)

    children = [[] for _ in range(t)]
    for node in range(1, t):
        children[parent[node]].append(node)

    feasible: list[set[tuple[int, ...]]] = [set() for _ in range(t)]
    for node in reversed(order):
        bag = normal_bags[node]
        positions = {vertex: i for i, vertex in enumerate(bag)}
        local_edges = [
            (positions[u], positions[v])
            for u, v in graph_edges
            if u in positions and v in positions
        ]
        for state in product(range(3), repeat=len(bag)):
            if any(state[i] == state[j] for i, j in local_edges):
                continue
            compatible_with_all_children = True
            for child in children[node]:
                child_bag = normal_bags[child]
                child_positions = {vertex: i for i, vertex in enumerate(child_bag)}
                shared = set(bag) & set(child_bag)
                if not any(
                    all(
                        state[positions[vertex]] == child_state[child_positions[vertex]]
                        for vertex in shared
                    )
                    for child_state in feasible[child]
                ):
                    compatible_with_all_children = False
                    break
            if compatible_with_all_children:
                feasible[node].add(state)

    return bool(feasible[0])


def verify_three_colouring(
    n: int, edges: Iterable[tuple[int, int]], colours: Sequence[int]
) -> bool:
    """Polynomial-time certificate verifier for a proposed 3-colouring."""
    graph_edges = _normalise_edges(n, edges)
    if len(colours) != n or any(colour not in (0, 1, 2) for colour in colours):
        return False
    return all(colours[u] != colours[v] for u, v in graph_edges)
