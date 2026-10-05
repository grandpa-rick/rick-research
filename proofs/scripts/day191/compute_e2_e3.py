"""Compute e_2 * e_r for r = 1, 2, 3 to find the general e_2 * e_r Pieri pattern.

We already have:
  e_2 * e_2 = (1+t^2)(1-q^{-1})([3]_t - t/q) e_4 + q^{-1}(1-q^{-1})[2]_t e_{3,1} + q^{-2} e_{2,2}

Compute:
  e_2 * e_1 = ? (should equal e_1 * e_2 by commutativity of *)
     e_1 * e_2 = (1-q^{-1})[3]_t e_3 + q^{-1} e_1 e_2 by Thm 3.12
  e_2 * e_3 = ?
"""

import sympy as sp
from itertools import combinations

q, t = sp.symbols('q t')


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


def compute_e2_star_er(r, m):
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    erX = e_r_X(m, r)
    print(f"[m={m}, r={r}] Y_j . e_{r}(X) ...")
    Yj_er = {}
    for j in range(1, m + 1):
        Yj_er[j] = Y_apply(erX, j)
    print(f"  All Y_j . e_{r}(X) done.")
    total = sp.Integer(0)
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            total = sp.expand(total + Y_apply(Yj_er[j], i))
        print(f"  i={i} done; #terms in total = {len(sp.Add.make_args(total))}")
    star = sp.expand(total / t)
    n = 2 + r
    print(f"  Expanding in e-basis of deg {n} ...")
    return expand_symmetric_in_e_basis(star, m, n)


def print_expansion(expansion, title):
    print(f"\n{title}")
    print("-" * 70)
    for lam, c in expansion.items():
        cs = sp.simplify(c)
        print(f"  e_{lam}: {sp.factor(cs)}")


def main():
    # e_2 * e_3 at m=5 (need m >= 5 for all partitions of 5)
    print("=" * 72)
    print("Compute e_2 * e_3 at m=5")
    print("=" * 72)
    exp = compute_e2_star_er(3, 5)
    print_expansion(exp, "e_2 * e_3 in e-basis (m=5):")

    # Also print numerator/denominator so we can spot the pattern
    print("\n---- Attempt to identify pattern ----")
    # Print in form (q-1)^a * poly(t,q) / q^b
    for lam, c in exp.items():
        cs = sp.simplify(c)
        # try to factor out (q-1)
        for power in range(3, -1, -1):
            quo = sp.simplify(cs / (q-1)**power)
            if quo.equals(sp.simplify(cs / (q-1)**power)) and (q-1)**power != 1:
                # check divisibility
                test = sp.simplify(cs - (q-1)**power * quo)
                if test == 0:
                    print(f"  e_{lam} = (q-1)^{power} * ({sp.factor(quo)})")
                    break
        else:
            print(f"  e_{lam} = {sp.factor(cs)}")


if __name__ == "__main__":
    main()
