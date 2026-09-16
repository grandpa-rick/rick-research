"""Final tests: swap q<->t, and try D_(m) F with F converted using q->1/q, t->1/t
(dual-Macdonald plethystic conventions differ; Hikita may use inverse conventions)."""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day197')
from D_a_vs_e_a_Y import (
    build_action, e_r_X, apply_D_m_to_polynomial, apply_e2_Y,
    poly_to_p_basis, partitions_of, q, t
)
import sympy as sp

def compare_swap(m, r, swap_qt=False, invert_q=False, invert_t=False, extra_scale=1):
    X = sp.symbols(f'X1:{m+1}')
    e_r = e_r_X(m, r)
    lhs = sp.expand(apply_e2_Y(e_r, m) / t)  # include star normalization t^{-1}
    lhs_p = poly_to_p_basis(lhs, list(X), r + 2)
    rhs = sp.expand(apply_D_m_to_polynomial(e_r, 2, list(X), r))
    rhs_p = poly_to_p_basis(rhs, list(X), r + 2)

    parts = partitions_of(r + 2)
    match = True
    for lam in parts:
        lc = lhs_p.get(lam, sp.Integer(0)) * extra_scale
        if swap_qt:
            lc = lc.subs({q: sp.Symbol('__tmp__'), t: q}).subs(sp.Symbol('__tmp__'), t)
        if invert_q:
            lc = lc.subs(q, 1/q)
        if invert_t:
            lc = lc.subs(t, 1/t)
        rc = rhs_p.get(lam, sp.Integer(0))
        d = sp.simplify(sp.cancel(lc - rc))
        print(f"    p_{lam}: diff={sp.factor(d)}")
        if d != 0:
            match = False
    print(f"  MATCH: {match}")
    return match

for r in [1, 2]:
    m = max(3, 2 + r)
    print(f"\n=== m={m}, r={r} ===")

    print(f"\n[Test 1] Swap q<->t on Hikita side, star norm t^{{-1}}:")
    compare_swap(m, r, swap_qt=True)

    print(f"\n[Test 2] Hikita q->1/q on top of star norm:")
    compare_swap(m, r, invert_q=True)

    print(f"\n[Test 3] Hikita q->1/q AND t->1/t (full duality):")
    compare_swap(m, r, invert_q=True, invert_t=True)

    print(f"\n[Test 4] Hikita with extra (-1)^r or (-1)^{{a+r}}:")
    compare_swap(m, r, extra_scale=(-1)**(2+r))
