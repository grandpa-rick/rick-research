"""Additional diagnostics for the h-side/ω tests.

Given that:
- At q=1: D_{(2)} e_r = h_2 · e_r (ordinary product)   [confirmed]
- h_2(Y) . e_r (raw, no norm) does NOT match D_{(2)} e_r   [confirmed]

Check:
1. What does h_2(Y) . e_r become at q=1 or t=1? Maybe it's a different operator.
2. For Part B, is ω supposed to also swap q<->t? In Macdonald theory, ω_{q,t} = ω ∘ (q<->t).
   Test: ω(e_a ⋆_(q,t) e_r) [with q<->t swap on the LHS's parameters] = h_a ⋆_(q,t) h_r ?
   Equivalently: ω(e_a ⋆_(t,q) e_r) = h_a ⋆_(q,t) h_r.

3. What if the h-side operator is e_a(Y^{-1}) (or dually h_a(Y^{-1})) — related by Cherednik
   duality? Very speculative; skip unless there's a hint.
"""

import sympy as sp
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from D_a_vs_e_a_Y import (
    q, t,
    build_action,
    e_r_X,
    partitions_of,
    poly_to_p_basis,
    apply_D_m_to_polynomial,
)

from h_side_and_omega import (
    apply_h2_Y,
    apply_e2_Y,
    omega_on_p_basis,
    diff_p_basis,
    all_zero,
)


def h_r_X(m_, r_):
    vars_ = sp.symbols(f'X1:{m_+1}')
    if r_ == 0:
        return sp.Integer(1)
    result = sp.Integer(0)
    def gen(start, remaining, current):
        nonlocal result
        if remaining == 0:
            term = sp.Integer(1)
            for v in current:
                term *= v
            result = result + term
            return
        for i in range(start, m_):
            current.append(vars_[i])
            gen(i, remaining - 1, current)
            current.pop()
    gen(0, r_, [])
    return sp.expand(result)


def test_h2Y_at_q1(r, m):
    """What is h_2(Y) . e_r at q=1?"""
    print(f"\n=== h_2(Y).e_r at q=1, r={r}, m={m} ===")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    h2Y_er = apply_h2_Y(er, m)
    h2Y_er_q1 = sp.expand(h2Y_er.subs(q, 1))
    lhs_p = poly_to_p_basis(h2Y_er_q1, list(X), r + 2)
    # Compare to h_2 · e_r (ordinary)
    def h2(vars_):
        s = sp.Integer(0)
        for i in range(len(vars_)):
            for j in range(i, len(vars_)):
                s = s + vars_[i] * vars_[j]
        return sp.expand(s)
    h2X = h2(list(X))
    h2_er = sp.expand(h2X * er)
    rhs_p = poly_to_p_basis(h2_er, list(X), r + 2)
    print(f"  h_2(Y).e_{r} at q=1:")
    for lam, c in lhs_p.items():
        print(f"    p_{lam}: {sp.factor(sp.cancel(c))}")
    print(f"  h_2·e_{r} (ordinary):")
    for lam, c in rhs_p.items():
        print(f"    p_{lam}: {sp.factor(sp.cancel(c))}")
    # Check if lhs / rhs is constant per component
    print(f"  Ratio lhs/rhs per p_λ:")
    for lam in partitions_of(r + 2):
        a = lhs_p.get(lam, sp.Integer(0))
        b = rhs_p.get(lam, sp.Integer(0))
        if a == 0 and b == 0:
            print(f"    p_{lam}: 0/0")
        elif b == 0:
            print(f"    p_{lam}: lhs={sp.factor(a)}, rhs=0")
        else:
            r_ = sp.simplify(sp.cancel(a / b))
            print(f"    p_{lam}: {sp.factor(r_)}")


def test_h2Y_at_t1(r, m):
    """What is h_2(Y) . e_r at t=1?"""
    print(f"\n=== h_2(Y).e_r at t=1, r={r}, m={m} ===")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    h2Y_er = apply_h2_Y(er, m)
    h2Y_er_t1 = sp.expand(h2Y_er.subs(t, 1))
    lhs_p = poly_to_p_basis(h2Y_er_t1, list(X), r + 2)
    print(f"  h_2(Y).e_{r} at t=1:")
    for lam, c in lhs_p.items():
        print(f"    p_{lam}: {sp.factor(sp.cancel(c))}")


def test_D2_at_t1(r, m):
    print(f"\n=== D_(2) e_r at t=1, r={r}, m={m} ===")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    D2_er = apply_D_m_to_polynomial(er, 2, list(X), r)
    D2_er_t1 = sp.expand(D2_er.subs(t, 1))
    p = poly_to_p_basis(D2_er_t1, list(X), r + 2)
    print(f"  D_(2) e_{r} at t=1:")
    for lam, c in p.items():
        print(f"    p_{lam}: {sp.factor(sp.cancel(c))}")


def test_e2_star_er_at_q1(r, m):
    """What is e_2 ⋆ e_r at q=1? Should be e_2 · e_r ordinary."""
    print(f"\n=== e_2 ⋆ e_r at q=1, r={r}, m={m} ===")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    star = apply_e2_Y(er, m)
    star = sp.expand(star / t)  # t^{-1} normalization
    star_q1 = sp.expand(star.subs(q, 1))
    p = poly_to_p_basis(star_q1, list(X), r + 2)
    # Ordinary e_2 · e_r
    e2X = e_r_X(m, 2)
    ord_p = poly_to_p_basis(sp.expand(e2X * er), list(X), r + 2)
    print(f"  e_2 ⋆ e_{r} at q=1 vs e_2·e_r ordinary:")
    for lam in partitions_of(r + 2):
        a = p.get(lam, sp.Integer(0))
        b = ord_p.get(lam, sp.Integer(0))
        print(f"    p_{lam}: star|q=1 = {sp.factor(sp.cancel(a))}, e_2·e_r = {sp.factor(sp.cancel(b))}, diff = {sp.factor(sp.cancel(a - b))}")


# ω-conjugacy with (q,t)-swap variant
def part_B_qt_swap(a, r, m):
    """Test whether ω(e_a ⋆_(t,q) e_r) = h_a ⋆_(q,t) h_r,
    i.e., we swap q<->t on the LHS before applying ω.
    """
    print(f"\n=== Part B with q<->t swap on LHS: a={a}, r={r}, m={m} ===")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    deg = a + r

    # LHS: e_a ⋆_(t,q) e_r  -- swap q and t
    star_er = apply_e2_Y(er, m)
    star_er = sp.expand(star_er / t)  # t^{-1} normalization
    # swap q <-> t
    q_, t_ = sp.symbols('q_ t_')
    swapped = star_er.subs({q: q_, t: t_}, simultaneous=True).subs({q_: t, t_: q}, simultaneous=True)
    swapped = sp.expand(swapped)
    swapped_p = poly_to_p_basis(swapped, list(X), deg)
    omega_lhs_p = omega_on_p_basis(swapped_p)

    # RHS: h_a ⋆ h_r with same t^{-1} normalization
    hr = h_r_X(m, r)
    ha_hr = apply_h2_Y(hr, m)
    ha_hr = sp.expand(ha_hr / t)
    rhs_p = poly_to_p_basis(ha_hr, list(X), deg)

    diffs = diff_p_basis(omega_lhs_p, rhs_p, deg)
    print(f"  Differences ω(LHS with q<->t) - RHS:")
    for lam, d in diffs.items():
        print(f"    p_{lam}: {sp.factor(d)}")
    print(f"  MATCH: {all_zero(diffs)}")
    if not all_zero(diffs):
        # Print pointwise ratio
        print(f"  Pointwise ratio RHS / ω(LHS-swapped):")
        for lam in partitions_of(deg):
            a_ = omega_lhs_p.get(lam, sp.Integer(0))
            b_ = rhs_p.get(lam, sp.Integer(0))
            if a_ == 0 and b_ == 0:
                print(f"    p_{lam}: 0/0")
            elif a_ == 0:
                print(f"    p_{lam}: lhs=0, rhs={sp.factor(sp.cancel(b_))}")
            else:
                r_ = sp.simplify(sp.cancel(b_ / a_))
                print(f"    p_{lam}: {sp.factor(r_)}")


def macdonald_omega_qt(p_dict):
    """ω_{q,t}: p_k -> (-1)^{k-1} (1-q^k)/(1-t^k) p_k.  (Standard Macdonald involution.)"""
    result = {}
    for lam, c in p_dict.items():
        sign = sp.Integer(1)
        factor = sp.Integer(1)
        for a in lam:
            sign *= (-1) ** (a - 1)
            factor *= (1 - q**a) / (1 - t**a)
        result[lam] = sp.simplify(sign * factor * c)
    return result


def part_B_omega_qt(a, r, m):
    """Test whether ω_{q,t}(e_a ⋆ e_r) = h_a ⋆ h_r (using Macdonald ω_{q,t})."""
    print(f"\n=== Part B with Macdonald ω_{{q,t}}: a={a}, r={r}, m={m} ===")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    deg = a + r

    star_er = apply_e2_Y(er, m)
    star_er = sp.expand(star_er / t)
    star_p = poly_to_p_basis(star_er, list(X), deg)
    omega_lhs_p = macdonald_omega_qt(star_p)

    hr = h_r_X(m, r)
    ha_hr = apply_h2_Y(hr, m)
    ha_hr = sp.expand(ha_hr / t)
    rhs_p = poly_to_p_basis(ha_hr, list(X), deg)

    print(f"  ω_qt(LHS) in p-basis:")
    for lam, c in omega_lhs_p.items():
        print(f"    p_{lam}: {sp.factor(sp.cancel(c))}")
    print(f"  RHS in p-basis:")
    for lam, c in rhs_p.items():
        print(f"    p_{lam}: {sp.factor(sp.cancel(c))}")

    diffs = diff_p_basis(omega_lhs_p, rhs_p, deg)
    print(f"  Differences:")
    for lam, d in diffs.items():
        print(f"    p_{lam}: {sp.factor(d)}")
    print(f"  MATCH: {all_zero(diffs)}")


if __name__ == "__main__":
    print("=" * 78)
    print("DIAGNOSTICS")
    print("=" * 78)

    # 1. h_2(Y).e_r at q=1 vs h_2·e_r
    for r in [1, 2]:
        test_h2Y_at_q1(r, max(3, 2 + r))

    # 2. e_2 ⋆ e_r at q=1 — should equal ordinary product
    for r in [1, 2]:
        test_e2_star_er_at_q1(r, max(3, 2 + r))

    # 3. h_2(Y) at t=1 — should be simpler
    for r in [1, 2]:
        test_h2Y_at_t1(r, max(3, 2 + r))
        test_D2_at_t1(r, max(3, 2 + r))

    # 4. ω-conjugacy with q<->t swap
    print("\n" + "=" * 78)
    print("ω-conjugacy variants")
    print("=" * 78)
    for r in [1, 2]:
        part_B_qt_swap(2, r, max(3, 2 + r))

    # 5. Macdonald ω_{q,t}
    for r in [1, 2]:
        part_B_omega_qt(2, r, max(3, 2 + r))
