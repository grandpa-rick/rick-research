"""
Day 196: Test DS at length 4 with lambda=(1,1,1,1) at n=4.

lambda = (1,1,1,1) has n(lambda) = 0 + 1 + 2 + 3 = 6. So leading coefficient
q^{-6} predicted for e_(1,1,1,1)^*.

DS: support in {mu : mu >= (1,1,1,1)} = all partitions of 4 (bottom of dominance).
So DS trivial here, but tests the q^{-n(lambda)} leading coeff conjecture.
"""
import sympy as sp
from itertools import combinations

q, t = sp.symbols('q t')


def build_action(m):
    X = sp.symbols(f'X1:{m+1}')

    def si_apply(F, i):
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


def dominates(mu, lam):
    if sum(mu) != sum(lam):
        return False
    partial_mu = 0
    partial_lam = 0
    L = max(len(mu), len(lam))
    for i in range(L):
        partial_mu += mu[i] if i < len(mu) else 0
        partial_lam += lam[i] if i < len(lam) else 0
        if partial_mu < partial_lam:
            return False
    return True


def n_stat(lam):
    """Macdonald n-statistic: n(lambda) = sum_i (i-1) * lambda_i."""
    return sum((i) * l for i, l in enumerate(lam))  # i is 0-indexed, so (i-1) with 1-indexed = i with 0-indexed


def e_lambda_X(m, lam):
    result = sp.Integer(1)
    for p in lam:
        result *= e_r_X(m, p)
    return sp.expand(result)


def expand_symmetric_in_e_basis(F, m, n):
    X = sp.symbols(f'X1:{m+1}')
    parts = partitions_of(n)
    if m < n:
        raise ValueError(f"Need m >= n; got m={m}, n={n}")
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


def compute_e_star_product(m, factors):
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    F = sp.Integer(1)
    scalar_factor = sp.Integer(1)
    for f in factors:
        scalar_factor = scalar_factor * t**(-f*(f-1)/2)
        subsets = list(combinations(range(1, m+1), f))
        new_F = sp.Integer(0)
        for I in subsets:
            piece = F
            for i in I:
                piece = Y_apply(piece, i)
            new_F = sp.expand(new_F + piece)
        F = new_F
    star_result = sp.expand(scalar_factor * F)
    return star_result


def main():
    # Test 1: lambda=(1,1,1,1) at n=4
    print("=" * 72)
    print("Day 196 length-4 test: e_1^{*4} at m=4, n=4 (lambda=(1,1,1,1))")
    print("=" * 72)
    lam = (1, 1, 1, 1)
    print(f"lambda = {lam}, n(lambda) = {n_stat(lam)}")
    print(f"Predicted leading coefficient: q^{{-{n_stat(lam)}}}")
    print()

    m = 4
    star_result = compute_e_star_product(m, [1, 1, 1, 1])
    print(f"[m={m}] #terms in expanded form = {len(sp.Add.make_args(star_result))}")

    expansion = expand_symmetric_in_e_basis(star_result, m, 4)
    print()
    print(f"e_1^{{*4}} in e-basis (m={m}):")
    for mu, c in expansion.items():
        cs = sp.simplify(c)
        dom = "DOMINATES" if dominates(mu, lam) else "does not dominate"
        print(f"  {dom:22} e_{mu}: {sp.factor(cs)}")

    coef_lambda = sp.simplify(expansion.get(lam, sp.Integer(0)))
    n_l = n_stat(lam)
    pred = q**(-n_l)
    diff = sp.simplify(coef_lambda - pred)
    print()
    print(f"Coefficient of e_lambda={lam}: {sp.factor(coef_lambda)}")
    print(f"Predicted (q^{{-n(lambda)}}) = q^{{-{n_l}}} = {pred}")
    print(f"Difference: {diff}")

    print()
    print("=" * 72)
    print("Day 196 length-4 DS test: e_1^{*3} * e_2 at m=5, n=5 (lambda=(2,1,1,1))")
    print("=" * 72)
    lam = (2, 1, 1, 1)
    print(f"lambda = {lam}, n(lambda) = {n_stat(lam)}")
    print(f"Predicted leading coefficient: q^{{-{n_stat(lam)}}}")

    parts = partitions_of(5)
    dominating = [mu for mu in parts if dominates(mu, lam)]
    not_dominating = [mu for mu in parts if not dominates(mu, lam)]
    print(f"Partitions dominating lambda (DS predicts support): {dominating}")
    print(f"Partitions NOT dominating (DS predicts zero coeff): {not_dominating}")
    print()

    m = 5
    star_result = compute_e_star_product(m, [1, 1, 1, 2])
    expansion = expand_symmetric_in_e_basis(star_result, m, 5)
    print()
    print(f"e_1*e_1*e_1*e_2 in e-basis (m={m}):")
    for mu, c in expansion.items():
        cs = sp.simplify(c)
        dom = "DOMINATES" if dominates(mu, lam) else "does not dominate"
        pred_zero = "" if dominates(mu, lam) else " <-- DS predicts ZERO"
        print(f"  {dom:22} e_{mu}: {sp.factor(cs)}{pred_zero}")

    print()
    print("Checking DS...")
    ds_holds = True
    for mu in not_dominating:
        c = sp.simplify(expansion.get(mu, sp.Integer(0)))
        print(f"e_{mu} coefficient = {sp.factor(c)}")
        if c != 0:
            ds_holds = False

    coef_lambda = sp.simplify(expansion.get(lam, sp.Integer(0)))
    n_l = n_stat(lam)
    pred = q**(-n_l)
    diff = sp.simplify(coef_lambda - pred)
    print()
    print(f"Coefficient of e_lambda={lam}: {sp.factor(coef_lambda)}")
    print(f"Predicted (q^{{-n(lambda)}}) = q^{{-{n_l}}}")
    print(f"Difference: {sp.factor(diff)}")

    if ds_holds:
        print("VERDICT: DS HOLDS at length 4.")
    else:
        print("VERDICT: DS FAILS at length 4.")


if __name__ == "__main__":
    main()
