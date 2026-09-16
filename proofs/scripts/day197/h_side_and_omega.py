"""Day 197 rescue-test — h-side Pieri and ω-conjugacy of Hikita ⋆.

Primary hypothesis (D_{(a)} = e_a(Y)) was refuted: D_{(a)} is the h-side Pieri,
Rick's ⋆ is the e-side Pieri.

Two rescue routes:

Hypothesis A: D_{(a)} f = h_a ⋆_Hikita f, defined as t^{?} h_a(Y) . f, with h_a(Y)
computed via Newton's identity: h_2(Y) = (p_1(Y)^2 + p_2(Y)) / 2.

Hypothesis B: ω is a ⋆-morphism: ω(f ⋆ g) = ω(f) ⋆ ω(g). Test on small samples.

Reuses D_{(m)} implementation and p-basis machinery from D_a_vs_e_a_Y.py.
"""

import sympy as sp
from itertools import combinations

# Import from the sibling script
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from D_a_vs_e_a_Y import (
    q, t,
    build_action,
    e_r_X,
    partitions_of,
    p_lambda_in_vars,
    poly_to_p_basis,
    apply_D_m_to_polynomial,
    M,
)


# ---------------- h_a(Y) via Newton's identity ---------------- #

def apply_p1_Y(F, m):
    """p_1(Y) . F = sum_i Y_i . F."""
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    total = sp.Integer(0)
    for i in range(1, m + 1):
        total = sp.expand(total + Y_apply(F, i))
    return total


def apply_p2_Y(F, m):
    """p_2(Y) . F = sum_i Y_i . Y_i . F."""
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    total = sp.Integer(0)
    for i in range(1, m + 1):
        YiF = Y_apply(F, i)
        YiYiF = Y_apply(YiF, i)
        total = sp.expand(total + YiYiF)
    return total


def apply_e2_Y(F, m):
    """e_2(Y) . F = sum_{i<j} Y_i Y_j . F."""
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    Yj_F = {}
    for j in range(1, m + 1):
        Yj_F[j] = Y_apply(F, j)
    total = sp.Integer(0)
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            total = sp.expand(total + Y_apply(Yj_F[j], i))
    return total


def apply_h2_Y(F, m):
    """h_2(Y) . F = (p_1(Y)^2 + p_2(Y)) / 2 . F = (e_1(Y)^2 + p_2(Y)) / 2 . F.

    Equivalently: h_2 = e_1^2 - e_2 + e_1^2*0 ... let's use Newton:
      p_1 = e_1, so p_1^2 = e_1^2.
      h_2 = (p_1^2 + p_2)/2 = (e_1^2 + p_2)/2.
    But also h_2 = e_1^2 - e_2 + ... no, better identity:
      h_2 - e_2 = sum_i Y_i^2 = p_2.
      Actually: e_1^2 = h_2 + e_2 - e_2 ... let me just be careful.
      In Λ: h_2 = e_1^2 - e_2 (for two-variable identity? no).

    General Newton: n h_n = sum_{k=1}^{n} h_{n-k} p_k, so
      2 h_2 = h_1 p_1 + h_0 p_2 = p_1^2 + p_2.
    Thus h_2(Y) = (p_1(Y)^2 + p_2(Y)) / 2.

    p_1(Y)^2 . F = p_1(Y) . (p_1(Y) . F).
    """
    p1p1F = apply_p1_Y(apply_p1_Y(F, m), m)
    p2F = apply_p2_Y(F, m)
    return sp.expand((p1p1F + p2F) / 2)


def apply_h_lambda_Y(lam, F, m):
    """Apply h_{lam_1} h_{lam_2} ... (Y) to F, for lam a partition (increasing multiset)."""
    G = F
    for a in lam:
        if a == 1:
            G = apply_p1_Y(G, m)  # h_1 = p_1
        elif a == 2:
            G = apply_h2_Y(G, m)
        else:
            raise NotImplementedError(f"h_{a}(Y) not implemented.")
    return G


# ---------------- ω involution on symmetric functions ---------------- #

def omega_on_p_basis(p_dict):
    """ω acts on p_k by (-1)^{k-1}. So on p_lambda, ω = prod (-1)^{lam_i - 1} = (-1)^{|lam| - ell(lam)}."""
    result = {}
    for lam, c in p_dict.items():
        sign = sp.Integer(1)
        for a in lam:
            sign *= (-1) ** (a - 1)
        result[lam] = sign * c
    return result


# ---------------- Convert p-basis back to polynomial in m vars ---------------- #

def p_basis_to_poly(p_dict, vars_):
    """Given {lam: coeff}, return the symmetric polynomial in vars_."""
    total = sp.Integer(0)
    for lam, c in p_dict.items():
        if c == 0:
            continue
        total = total + c * p_lambda_in_vars(lam, vars_)
    return sp.expand(total)


# ---------------- Diff utility ---------------- #

def diff_p_basis(A, B, deg):
    """Return {lam: A[lam] - B[lam]} for all partitions of deg."""
    diffs = {}
    for lam in partitions_of(deg):
        a = A.get(lam, sp.Integer(0))
        b = B.get(lam, sp.Integer(0))
        d = sp.simplify(sp.cancel(a - b))
        diffs[lam] = d
    return diffs


def all_zero(diffs):
    return all(d == 0 for d in diffs.values())


# ---------------- Part A: h_2 ⋆ e_r vs D_{(2)} e_r ---------------- #

def part_A_test(r, m, star_norm_exp=None, verbose=True):
    """Compute h_2(Y) . e_r(X), optionally rescale by t^{star_norm_exp}, and compare
    with D_{(2)} e_r in p-basis.
    """
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    deg = r + 2

    if verbose:
        print(f"\n--- Part A: r={r}, m={m}, star_norm t^{star_norm_exp} ---")

    # LHS: h_2(Y) . e_r(X)
    h2Y_er = apply_h2_Y(er, m)
    if star_norm_exp is not None:
        h2Y_er = sp.expand(t ** star_norm_exp * h2Y_er)
    lhs_p = poly_to_p_basis(h2Y_er, list(X), deg)

    # RHS: D_{(2)} e_r
    D2_er = apply_D_m_to_polynomial(er, 2, list(X), r)
    rhs_p = poly_to_p_basis(D2_er, list(X), deg)

    if verbose:
        print(f"\nh_2(Y) . e_{r}(X) in p-basis:")
        for lam, c in lhs_p.items():
            print(f"  p_{lam}: {sp.factor(sp.cancel(c))}")
        print(f"\nD_(2) e_{r} in p-basis:")
        for lam, c in rhs_p.items():
            print(f"  p_{lam}: {sp.factor(sp.cancel(c))}")

    diffs = diff_p_basis(lhs_p, rhs_p, deg)
    if verbose:
        print(f"\nDifferences (LHS - RHS):")
        for lam, d in diffs.items():
            print(f"  p_{lam}: {sp.factor(d)}")
    ok = all_zero(diffs)
    if verbose:
        print(f"MATCH: {ok}")
    return ok, diffs, lhs_p, rhs_p


def part_A_renorm_sweep(r, m):
    """Sweep q^i t^j rescaling to see if h_2(Y).e_r matches D_{(2)} e_r after rescale."""
    print(f"\n### Part A renorm sweep: r={r}, m={m} ###")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    deg = r + 2
    h2Y_er = apply_h2_Y(er, m)
    lhs_p_raw = poly_to_p_basis(h2Y_er, list(X), deg)
    D2_er = apply_D_m_to_polynomial(er, 2, list(X), r)
    rhs_p = poly_to_p_basis(D2_er, list(X), deg)

    # Check: is rhs_p a monomial-in-q,t rescaling of lhs_p_raw?
    best = None
    best_score = -1
    for qk in range(-4, 5):
        for tk in range(-4, 5):
            scale = q**qk * t**tk
            ok = True
            score = 0
            for lam in partitions_of(deg):
                a = lhs_p_raw.get(lam, sp.Integer(0)) * scale
                b = rhs_p.get(lam, sp.Integer(0))
                d = sp.simplify(sp.cancel(a - b))
                if d == 0:
                    score += 1
                else:
                    ok = False
            if ok:
                print(f"  ** EXACT MATCH at q^{qk} t^{tk} **")
                return (qk, tk, True)
            if score > best_score:
                best_score = score
                best = (qk, tk)
    print(f"  No exact monomial rescaling. Best: q^{best[0]} t^{best[1]} with {best_score}/{len(partitions_of(deg))} zero diffs")

    # Also print pointwise ratio at each partition to diagnose
    print(f"  Pointwise ratio (D_(2)e_r) / (h_2(Y).e_r):")
    for lam in partitions_of(deg):
        a = lhs_p_raw.get(lam, sp.Integer(0))
        b = rhs_p.get(lam, sp.Integer(0))
        if a == 0 and b == 0:
            print(f"    p_{lam}: 0/0")
        elif a == 0:
            print(f"    p_{lam}: rhs={sp.factor(sp.cancel(b))}, lhs=0")
        else:
            ratio = sp.simplify(sp.cancel(b / a))
            print(f"    p_{lam}: {sp.factor(ratio)}")
    return (best[0], best[1], False)


# ---------------- Part B: ω-conjugacy test ---------------- #

def part_B_test(a, r, m, verbose=True):
    """Test whether ω(e_a ⋆ e_r) = h_a ⋆ h_r, where ⋆ = t^{-a(a-1)/2} e_a(Y)-action.

    LHS: compute e_a(Y).e_r(X), star-normalize with t^{-a(a-1)/2}, expand in p-basis, apply ω.
    RHS: define h_a ⋆ h_r analogously — but the star normalization for h_a is ambiguous.
         Test with SAME normalization t^{-a(a-1)/2} first.
    """
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    deg = a + r

    if verbose:
        print(f"\n--- Part B: a={a}, r={r}, m={m} ---")

    # LHS: e_a(Y) . e_r(X), star-normalize, ω on p-basis
    if a == 2:
        star_er = apply_e2_Y(er, m)
    else:
        raise NotImplementedError
    tw = t ** (-a * (a - 1) // 2)  # t^{-1} for a=2
    star_er = sp.expand(tw * star_er)
    star_er_p = poly_to_p_basis(star_er, list(X), deg)
    omega_lhs_p = omega_on_p_basis(star_er_p)

    # RHS: need h_a(Y) . h_r(X). First compute h_r(X) in the m variables.
    # h_r = sum over multisets of size r of prod of vars.
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

    hr = h_r_X(m, r)
    # h_a(Y) . h_r(X)
    if a == 2:
        ha_hr = apply_h2_Y(hr, m)
    else:
        raise NotImplementedError
    ha_hr = sp.expand(tw * ha_hr)
    rhs_p = poly_to_p_basis(ha_hr, list(X), deg)

    if verbose:
        print(f"\nω(e_{a} ⋆ e_{r}) in p-basis:")
        for lam, c in omega_lhs_p.items():
            print(f"  p_{lam}: {sp.factor(sp.cancel(c))}")
        print(f"\nh_{a} ⋆ h_{r}  in p-basis:")
        for lam, c in rhs_p.items():
            print(f"  p_{lam}: {sp.factor(sp.cancel(c))}")

    diffs = diff_p_basis(omega_lhs_p, rhs_p, deg)
    if verbose:
        print(f"\nDifferences (ω(LHS) - RHS):")
        for lam, d in diffs.items():
            print(f"  p_{lam}: {sp.factor(d)}")
    ok = all_zero(diffs)
    if verbose:
        print(f"MATCH: {ok}")
    return ok, diffs, omega_lhs_p, rhs_p


def part_B_renorm_sweep(a, r, m):
    """If direct match fails, try q^i t^j rescaling to see how close ω-conjugacy is."""
    print(f"\n### Part B renorm sweep: a={a}, r={r}, m={m} ###")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    deg = a + r

    star_er = apply_e2_Y(er, m)
    tw = t ** (-a * (a - 1) // 2)
    star_er = sp.expand(tw * star_er)
    star_er_p = poly_to_p_basis(star_er, list(X), deg)
    omega_lhs_p = omega_on_p_basis(star_er_p)

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

    hr = h_r_X(m, r)
    ha_hr = apply_h2_Y(hr, m)
    ha_hr = sp.expand(tw * ha_hr)
    rhs_p = poly_to_p_basis(ha_hr, list(X), deg)

    best = None
    best_score = -1
    for qk in range(-4, 5):
        for tk in range(-4, 5):
            scale = q**qk * t**tk
            ok = True
            score = 0
            for lam in partitions_of(deg):
                A = omega_lhs_p.get(lam, sp.Integer(0)) * scale
                B = rhs_p.get(lam, sp.Integer(0))
                d = sp.simplify(sp.cancel(A - B))
                if d == 0:
                    score += 1
                else:
                    ok = False
            if ok:
                print(f"  ** EXACT MATCH at q^{qk} t^{tk} **")
                return (qk, tk, True)
            if score > best_score:
                best_score = score
                best = (qk, tk)
    print(f"  No exact monomial rescaling. Best: q^{best[0]} t^{best[1]} with {best_score}/{len(partitions_of(deg))} zero diffs")
    # Pointwise ratio
    print(f"  Pointwise ratio RHS / ω(LHS):")
    for lam in partitions_of(deg):
        a_ = omega_lhs_p.get(lam, sp.Integer(0))
        b_ = rhs_p.get(lam, sp.Integer(0))
        if a_ == 0 and b_ == 0:
            print(f"    p_{lam}: 0/0")
        elif a_ == 0:
            print(f"    p_{lam}: lhs=0, rhs={sp.factor(sp.cancel(b_))}")
        else:
            ratio = sp.simplify(sp.cancel(b_ / a_))
            print(f"    p_{lam}: {sp.factor(ratio)}")
    return (best[0], best[1], False)


# ---------------- Sanity: at q=1, verify D_{(2)}(e_r) = h_2 · e_r (ordinary product) ---------------- #

def sanity_q1(r, m):
    """At q=1, D_{(2)}(e_r) should equal h_2 * e_r (ordinary Hall product)."""
    print(f"\n--- Sanity check: at q=1, D_(2) e_{r} = h_2 · e_{r}? (m={m}) ---")
    X = sp.symbols(f'X1:{m+1}')
    er = e_r_X(m, r)
    deg = r + 2

    D2_er = apply_D_m_to_polynomial(er, 2, list(X), r)
    D2_er_q1 = sp.expand(D2_er.subs(q, 1))
    D2_p_q1 = poly_to_p_basis(D2_er_q1, list(X), deg)

    # h_2 in vars
    def h2(vars_):
        s = sp.Integer(0)
        for i in range(len(vars_)):
            for j in range(i, len(vars_)):
                s = s + vars_[i] * vars_[j]
        return sp.expand(s)
    h2X = h2(list(X))
    h2_er = sp.expand(h2X * er)
    h2_er_p = poly_to_p_basis(h2_er, list(X), deg)

    print("D_(2) e_r at q=1 vs h_2 · e_r (ordinary):")
    for lam in partitions_of(deg):
        a = D2_p_q1.get(lam, sp.Integer(0))
        b = h2_er_p.get(lam, sp.Integer(0))
        # Substitute q=1 in b too (only t remains)
        a_s = sp.simplify(a)
        b_s = sp.simplify(b)
        diff = sp.simplify(sp.cancel(a_s - b_s))
        print(f"  p_{lam}: D_(2)|q=1 = {sp.factor(a_s)}, h_2·e_r = {sp.factor(b_s)}, diff = {sp.factor(diff)}")


# ---------------- Main ---------------- #

if __name__ == "__main__":
    print("=" * 78)
    print("Day 197 rescue-test — h-side Pieri & ω-conjugacy of Hikita ⋆")
    print("=" * 78)

    # ---- Sanity check first: at q=1, D_{(2)} = h_2· ---- #
    print("\n" + "=" * 78)
    print("SANITY: at q=1, D_(2) e_r = h_2 · e_r (ordinary Hall product)?")
    print("=" * 78)
    for r in [1, 2]:
        sanity_q1(r, max(3, 2 + r))

    # ---- Part A: h_2(Y) . e_r vs D_{(2)} e_r ---- #
    print("\n" + "=" * 78)
    print("PART A: is D_{(2)} = h_2 ⋆_Hikita ?")
    print("       (i.e., D_{(2)}(e_r) = t^{?} h_2(Y).e_r  for some normalization?)")
    print("=" * 78)
    for r in [1, 2]:
        m = max(3, 2 + r)
        # First try WITHOUT any t normalization
        ok, diffs, lhs_p, rhs_p = part_A_test(r, m, star_norm_exp=None)
        if not ok:
            # Try with same t^{-1} normalization as e_2 ⋆
            print(f"\n  Trying t^{-1} normalization (as in e_2 ⋆):")
            ok2, _, _, _ = part_A_test(r, m, star_norm_exp=-1)
            if not ok2:
                # Try full monomial sweep
                part_A_renorm_sweep(r, m)

    # ---- Part B: ω-conjugacy ---- #
    print("\n" + "=" * 78)
    print("PART B: is ω a ⋆-morphism?")
    print("       Test: ω(e_2 ⋆ e_r) ?= h_2 ⋆ h_r")
    print("=" * 78)
    for r in [1, 2]:
        m = max(3, 2 + r)
        ok, diffs, olhs_p, rhs_p = part_B_test(2, r, m)
        if not ok:
            part_B_renorm_sweep(2, r, m)

    print("\n" + "=" * 78)
    print("DONE")
    print("=" * 78)
