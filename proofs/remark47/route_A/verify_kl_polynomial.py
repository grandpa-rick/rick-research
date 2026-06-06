"""
Independent verification: compute KL^{B_2}_{λ^♯,μ^♯}(q,t) directly from
the W-alternating Kostant-partition formula, and confirm:

  KL = sum_{w in W} (-1)^{ℓ(w)} K_{q,t}(w·λ - μ)

For each pair (λ, μ), this should equal what Aug~ produces from
fixed-point counts.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47')

from fractions import Fraction
from collections import defaultdict
from aug_tilde_B2 import (
    weyl_B2,
    all_kostant_partitions_B2,
    bidegree_of_partition,
    RHO_B2,
)


def compute_kl_qt_BGG(lam, mu):
    """Compute KL^{B_2}_{λ^♯,μ^♯}(q,t) from the alternating sum."""
    tilde_a = tuple(int(lam[i] + RHO_B2[i]) for i in range(2))
    b = tuple(int(mu[i] + RHO_B2[i]) for i in range(2))

    weyl = weyl_B2()
    coeffs = defaultdict(int)
    for w_func, length, label in weyl:
        wa = w_func(tilde_a)
        beta_w = tuple(wa[i] - b[i] for i in range(2))
        if beta_w[0] < 0:
            continue
        sign = -1 if length % 2 else 1
        pis = all_kostant_partitions_B2(beta_w)
        for pi in pis:
            bd = bidegree_of_partition(pi)
            coeffs[bd] += sign
    # Filter zeros
    coeffs = {k: v for k, v in coeffs.items() if v != 0}
    return coeffs


def poly_str(coeffs):
    if not coeffs:
        return "0"
    return " + ".join(f"{c}*q^{i}*t^{j}" for (i, j), c in sorted(coeffs.items()))


if __name__ == "__main__":
    F = Fraction
    pairs = [
        ((F(3, 2), F(1, 2)), (F(1, 2), F(1, 2)), "λ=(3/2,1/2), μ=(1/2,1/2)"),
        ((F(5, 2), F(1, 2)), (F(1, 2), F(1, 2)), "λ=(5/2,1/2), μ=(1/2,1/2)"),
        ((F(5, 2), F(3, 2)), (F(1, 2), F(1, 2)), "λ=(5/2,3/2), μ=(1/2,1/2)"),
        ((F(3, 2), F(3, 2)), (F(3, 2), F(1, 2)), "λ=(3/2,3/2), μ=(3/2,1/2)"),
        ((F(7, 2), F(3, 2)), (F(3, 2), F(1, 2)), "λ=(7/2,3/2), μ=(3/2,1/2)"),
    ]
    for lam, mu, name in pairs:
        coeffs = compute_kl_qt_BGG(lam, mu)
        print(f"{name}: KL = {poly_str(coeffs)}")
        # Check non-negativity
        if all(v >= 0 for v in coeffs.values()):
            print(f"  ✓ all coefficients ≥ 0")
        else:
            print(f"  ✗ NEGATIVE COEFFICIENT(S)")
        print()
