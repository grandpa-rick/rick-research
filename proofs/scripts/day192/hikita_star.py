"""Day 192 PROVE — Hikita ⋆-product framework for e_a ⋆ e_r, a in {1,2,3}.

Extends Day 191 framework (compute_general.py) to a = 3.

Key identity (Hikita 2503.23597, Prop 3.10 corollary + Thm 3.12 setup):
   e_a(X) *_H F(X)  =  t^{-a(a-1)/2}  e_a(Y_1, ..., Y_m) . F(X)

For a = 3:
   e_3(Y) = sum_{i<j<k} Y_i Y_j Y_k   (Y's commute; symmetric in Y).
   So e_3(X) * e_r(X) = t^{-3} sum_{i<j<k} Y_i Y_j Y_k . e_r(X).

Since Y's commute, we can compute
   Yk_er[k] := Y_k . e_r(X)
   Ymid_er[j,k] := Y_j . Yk_er[k]    (j < k)
and then
   total = sum_{i<j<k} Y_i . Ymid_er[j,k].
"""

import sympy as sp
from itertools import combinations

q, t = sp.symbols('q t')


def qint(n):
    return sum(t**i for i in range(n))


def build_action(m):
    X = sp.symbols(f'X1:{m+1}')

    def si_apply(F, i):
        if i < 1 or i >= m:
            raise ValueError
        subs = {X[i-1]: X[i], X[i]: X[i-1]}
        return sp.expand(F.xreplace(subs))

    def Ti_apply(F, i):
        F = sp.expand(F)
        sF = si_apply(F, i)
        diff = sp.expand(F - sF)
        quot = sp.cancel(diff / (X[i-1] - X[i]))
        result = t * sF + (t - 1) * (-X[i]) * quot
        return sp.expand(result)

    def Ti_inv_apply(F, i):
        Ti_F = Ti_apply(F, i)
        return sp.expand(Ti_F / t - (t - 1) / t * F)

    def Pi_apply(F):
        subs = {X[i]: X[i+1] for i in range(m-1)}
        subs[X[m-1]] = q**(-1) * X[0]
        Fshift = sp.expand(F.xreplace(subs))
        return sp.expand(X[0] * Fshift)

    def Y_apply(F, i):
        G = F
        for j in range(i, m):
            G = Ti_inv_apply(G, j)
        G = Pi_apply(G)
        for j in range(1, i):
            G = Ti_apply(G, j)
        return sp.expand(t**(m - i) * G)

    return X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply


def e_r_X(m, r):
    X = sp.symbols(f'X1:{m+1}')
    if r == 0:
        return sp.Integer(1)
    if r > m:
        return sp.Integer(0)
    result = sp.Integer(0)
    for combo in combinations(X, r):
        term = sp.Integer(1)
        for v in combo:
            term *= v
        result += term
    return sp.expand(result)


def partitions_of(n):
    result = []
    def rec(remaining, max_part, current):
        if remaining == 0:
            result.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 0, -1):
            current.append(p)
            rec(remaining - p, p, current)
            current.pop()
    rec(n, n, [])
    return result


def e_lambda_X(m, lam):
    result = sp.Integer(1)
    for p in lam:
        result *= e_r_X(m, p)
    return sp.expand(result)


def expand_symmetric_in_e_basis(F, m, n):
    X = sp.symbols(f'X1:{m+1}')
    parts = partitions_of(n)
    if m < n:
        raise ValueError("Need m >= n.")
    canonicals = []
    for lam in parts:
        mon = sp.Integer(1)
        for i, p in enumerate(lam):
            mon *= X[i]**p
        canonicals.append(mon)
    Fpoly = sp.Poly(F, *X)
    b_vec = []
    for mon in canonicals:
        b_vec.append(Fpoly.coeff_monomial(sp.Poly(mon, *X).monoms()[0]))
    b_vec = sp.Matrix(b_vec)
    A_rows = []
    for lam in parts:
        el = e_lambda_X(m, lam)
        el_poly = sp.Poly(el, *X)
        row = [el_poly.coeff_monomial(sp.Poly(mon, *X).monoms()[0]) for mon in canonicals]
        A_rows.append(row)
    A = sp.Matrix(A_rows).T
    coeffs = A.solve(b_vec)
    result = {}
    for i, lam in enumerate(parts):
        c = sp.cancel(coeffs[i])
        result[lam] = c
    return result


def compute_ea_star_er(a, r, m, verbose=True):
    """Compute e_a(X) ⋆ e_r(X) = t^{-a(a-1)/2} e_a(Y) . e_r(X), a in {1,2,3}."""
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    erX = e_r_X(m, r)
    if verbose:
        print(f"[m={m}] Computing e_{a}(Y) . e_{r}(X) ...")

    if a == 1:
        total = sp.Integer(0)
        for i in range(1, m+1):
            total = sp.expand(total + Y_apply(erX, i))
            if verbose:
                print(f"  Y_{i} done. #terms total = {len(sp.Add.make_args(total))}")
    elif a == 2:
        Yj_er = {}
        for j in range(1, m + 1):
            Yj_er[j] = Y_apply(erX, j)
        total = sp.Integer(0)
        for i in range(1, m+1):
            for j in range(i+1, m+1):
                total = sp.expand(total + Y_apply(Yj_er[j], i))
            if verbose:
                print(f"  i={i} done. #terms total = {len(sp.Add.make_args(total))}")
    elif a == 3:
        Yk_er = {}
        for k in range(1, m + 1):
            Yk_er[k] = Y_apply(erX, k)
            if verbose:
                print(f"  Y_{k}.e_{r} done. #terms = {len(sp.Add.make_args(Yk_er[k]))}")
        # Compute pairwise: Yj_Yk_er[j,k] = Y_j . Y_k . e_r for j < k
        Yjk_er = {}
        for k in range(1, m + 1):
            for j in range(1, k):
                Yjk_er[(j, k)] = Y_apply(Yk_er[k], j)
                if verbose:
                    print(f"  Y_{j} Y_{k}.e_{r} done. #terms = {len(sp.Add.make_args(Yjk_er[(j,k)]))}")
        # Now sum i < j < k of Y_i . Y_j . Y_k . e_r
        total = sp.Integer(0)
        count = 0
        for k in range(1, m + 1):
            for j in range(1, k):
                for i in range(1, j):
                    piece = Y_apply(Yjk_er[(j, k)], i)
                    total = sp.expand(total + piece)
                    count += 1
                    if verbose:
                        print(f"  (i,j,k)=({i},{j},{k}) done [{count}]; running #terms = {len(sp.Add.make_args(total))}")
    else:
        raise NotImplementedError

    tw = t ** sp.Rational(-a * (a - 1), 2)
    star = sp.expand(tw * total)
    n = a + r
    if verbose:
        print(f"[m={m}] e_{a} ⋆ e_{r} computed. Expanding in e_lambda-basis of deg {n}...")
    expansion = expand_symmetric_in_e_basis(star, m, n)
    return expansion


def print_expansion(expansion, title):
    print(f"\n{title}")
    print("-" * 70)
    for lam, c in expansion.items():
        cs = sp.simplify(c)
        print(f"  e_{lam}: {sp.factor(cs)}")


def sanity_q1(expansion, expected_lam):
    """At q=1, ⋆-product should give the ordinary product, so only e_{expected_lam} should survive with coeff 1."""
    results = {}
    for lam, c in expansion.items():
        cs = sp.simplify(c.subs(q, 1))
        results[lam] = cs
    return results
