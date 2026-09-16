"""Sanity: check D_{(1)} vs e_1(Y) with star normalization (t^0 for a=1)."""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day197')
from D_a_vs_e_a_Y import (
    build_action, e_r_X, apply_D_m_to_polynomial, poly_to_p_basis,
    partitions_of, q, t
)
import sympy as sp

def apply_e1_Y(F, m):
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    total = sp.Integer(0)
    for i in range(1, m + 1):
        total = sp.expand(total + Y_apply(F, i))
    return total

for r in [1, 2]:
    m = max(3, 1 + r)
    X = sp.symbols(f'X1:{m+1}')
    e_r = e_r_X(m, r)
    print(f"\n=== m={m}, r={r}, D_(1) vs e_1(Y) ===")

    lhs = apply_e1_Y(e_r, m)
    lhs = sp.expand(lhs)  # star norm for a=1: t^0
    lhs_p = poly_to_p_basis(lhs, list(X), r + 1)

    rhs = apply_D_m_to_polynomial(e_r, 1, list(X), r)
    rhs = sp.expand(rhs)
    rhs_p = poly_to_p_basis(rhs, list(X), r + 1)

    parts = partitions_of(r + 1)
    match = True
    for lam in parts:
        lc = sp.simplify(sp.cancel(lhs_p.get(lam, 0)))
        rc = sp.simplify(sp.cancel(rhs_p.get(lam, 0)))
        d = sp.simplify(sp.cancel(lc - rc))
        print(f"  p_{lam}: Hikita={sp.factor(lc)},  D'Adderio={sp.factor(rc)},  diff={sp.factor(d)}")
        if d != 0:
            match = False
    print(f"  MATCH (raw, star norm t^0): {match}")

    # Try D_(1) at q=1 sanity: should give h_1[X] * e_r
    print(f"  D_(1) e_{r} at q=1:")
    for lam, c in rhs_p.items():
        cs = sp.simplify(c.subs(q, 1))
        print(f"    p_{lam}: {sp.factor(cs)}")
