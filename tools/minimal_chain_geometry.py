"""Exact geometry checks for polynomial minimal-vector coefficient chains.

This module measures the subspaces forced by right and left minimal bases.
It deliberately does not claim that these subspaces alone split off a mixed
regular summand or construct a Kronecker decomposition.
"""
from __future__ import annotations

from typing import Sequence

from tools.pencil_nullspace_certificate import rectangular_pencil_nullspace_certificate
from tools.rectangular_pencil import _validate_pair
from tools.spectral_fingerprint import rank_mod


def _transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def _column_matrix(vectors, dimension):
    return [
        [int(vectors[j][i]) for j in range(len(vectors))]
        for i in range(dimension)
    ]


def _chain_vectors(side, dimension):
    vectors = []
    for generator in side["generators"]:
        vectors.extend(
            [list(map(int, coefficient)) for coefficient
             in generator["coefficients_low_degree_first"]]
        )
    return vectors


def minimal_chain_geometry_certificate(
    q: Sequence[Sequence[int]], k: Sequence[Sequence[int]], p: int, *,
    max_degree: int = 8, max_minors: int = 2000,
) -> dict:
    """Certify ranks of right-chain domain vectors and left-chain covectors.

    Right polynomial generators contribute coefficient vectors in the domain.
    Left generators are computed on the transposed pencil and contribute
    coefficient covectors on the codomain. The reported ranks are exact over
    F_p. A full-rank chain family is a certified independent family, not by
    itself a proof of a mixed block decomposition.
    """
    rows, cols = _validate_pair(q, k, p)
    certificate = rectangular_pencil_nullspace_certificate(
        q, k, p, max_degree=max_degree, max_minors=max_minors
    )
    right_vectors = _chain_vectors(certificate["right"], cols)
    left_covectors = _chain_vectors(certificate["left"], rows)

    right_matrix = _column_matrix(right_vectors, cols)
    left_matrix = [list(v) for v in left_covectors]
    right_rank = rank_mod(right_matrix, p)
    left_rank = rank_mod(left_matrix, p) if left_matrix else 0

    right_expected = sum(
        generator["degree"] + 1 for generator in certificate["right"]["generators"]
    )
    left_expected = sum(
        generator["degree"] + 1 for generator in certificate["left"]["generators"]
    )
    right_independent = right_rank == len(right_vectors)
    left_independent = left_rank == len(left_covectors)

    return {
        "schema": "the-fold-minimal-chain-geometry-v1",
        "field": f"F_{p}",
        "shape": [rows, cols],
        "right_domain_chain": {
            "vector_count": len(right_vectors),
            "expected_from_minimal_indices": right_expected,
            "rank": right_rank,
            "independent": right_independent,
            "full_domain_span": right_rank == cols,
        },
        "left_codomain_cochain": {
            "covector_count": len(left_covectors),
            "expected_from_minimal_indices": left_expected,
            "rank": left_rank,
            "independent": left_independent,
            "full_codomain_cospan": left_rank == rows,
        },
        "profile_certificate_complete": certificate["complete"],
        "both_chain_families_independent": right_independent and left_independent,
        "interpretation": (
            "Ranks certify independence of the recovered minimal-chain "
            "coefficient families. They do not establish complementary "
            "regular subspaces, cross-chain compatibility, or a strict-"
            "equivalence decomposition."
        ),
        "nullspace_certificate": certificate,
    }
