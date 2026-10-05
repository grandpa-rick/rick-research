"""Extend Day 191 computation:
   1. Verify e_2 * e_2 formula at m=5.
   2. Compute e_2 * e_3 at m=5, m=6 to find the general Pieri e_2 * e_r pattern.
"""

import sympy as sp
from itertools import combinations, product

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
    """Compute e_a(X) * e_r(X) = t^{-a(a-1)/2} e_a(Y) . e_r(X)."""
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    erX = e_r_X(m, r)
    if verbose:
        print(f"[m={m}] Computing e_{a}(Y) . e_{r}(X) ...")

    # For a=2: e_2(Y) = sum_{i<j} Y_i Y_j
    if a == 2:
        # First compute Y_j . e_r(X) for each j
        Yj_er = {}
        for j in range(1, m + 1):
            Yj_er[j] = Y_apply(erX, j)
            if verbose:
                print(f"  Y_{j} . e_{r}(X) done, #terms = {len(sp.Add.make_args(Yj_er[j]))}")
        # Then sum_{i<j} Y_i . Y_j . e_r
        total = sp.Integer(0)
        for i in range(1, m+1):
            for j in range(i+1, m+1):
                total = sp.expand(total + Y_apply(Yj_er[j], i))
                if verbose:
                    print(f"  (i,j)=({i},{j}): #terms in total = {len(sp.Add.make_args(total))}")
    elif a == 1:
        total = sp.Integer(0)
        for i in range(1, m+1):
            total = sp.expand(total + Y_apply(erX, i))
    else:
        raise NotImplementedError

    tw = t ** (-a*(a-1)//2)
    star = sp.expand(tw * total)
    n = a + r
    if verbose:
        print(f"[m={m}] e_{a} * e_{r} computed. Expanding in e_lambda-basis of deg {n}...")
    expansion = expand_symmetric_in_e_basis(star, m, n)
    return expansion


def print_expansion(expansion, title):
    print(f"\n{title}")
    print("-" * 70)
    for lam, c in expansion.items():
        cs = sp.simplify(c)
        print(f"  e_{lam}: {sp.factor(cs)}")


def main():
    # 1. Verify e_2 * e_2 at m=5
    print("=" * 72)
    print("VERIFICATION: e_2 * e_2 stability from m=4 to m=5")
    print("=" * 72)
    exp5 = compute_ea_star_er(2, 2, 5, verbose=False)
    print_expansion(exp5, "e_2 * e_2 at m=5:")

    # Expected from m=4:
    expected_e4 = (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**2
    expected_e31 = (q - 1)*(t + 1)/q**2
    expected_e22 = 1/q**2
    print("\nComparing to m=4 result:")
    print(f"  e_(4,) diff: {sp.simplify(exp5[(4,)] - expected_e4)}")
    print(f"  e_(3,1) diff: {sp.simplify(exp5[(3,1)] - expected_e31)}")
    print(f"  e_(2,2) diff: {sp.simplify(exp5[(2,2)] - expected_e22)}")
    print(f"  e_(2,1,1): {sp.simplify(exp5.get((2,1,1), 0))}")
    print(f"  e_(1,1,1,1): {sp.simplify(exp5.get((1,1,1,1), 0))}")


if __name__ == "__main__":
    main()
