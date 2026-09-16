"""
Day 196: Test Dominance-Support (DS) conjecture at lambda=(2,2,1) at n=5.

DS: e_lambda^{*}(X) is in span{e_mu(X) : mu >= lambda in dominance order}.

For lambda=(2,2,1), partitions of 5 dominating (2,2,1):
  {(5), (4,1), (3,2), (3,1,1), (2,2,1)}
Partitions NOT dominating (should have zero coefficient in DS):
  {(2,1,1,1), (1,1,1,1,1)}
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
    """Return True if mu >= lam in dominance order (partition of same n)."""
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
        print(f"  after e_{f}(Y) applied: #terms = {len(sp.Add.make_args(F))}")

    star_result = sp.expand(scalar_factor * F)
    return star_result


def main():
    print("=" * 72)
    print("Day 196 DS test: e_2 * e_2 * e_1 at m=6, n=5 (lambda=(2,2,1))")
    print("=" * 72)
    lam = (2, 2, 1)
    print(f"lambda = {lam}")
    parts = partitions_of(5)
    dominating = [mu for mu in parts if dominates(mu, lam)]
    not_dominating = [mu for mu in parts if not dominates(mu, lam)]
    print(f"Partitions dominating lambda (DS predicts support): {dominating}")
    print(f"Partitions NOT dominating (DS predicts zero coeff): {not_dominating}")
    print()

    m = 6
    star_result = compute_e_star_product(m, [2, 2, 1])
    print(f"[m={m}] e_2*e_2*e_1: total #terms = {len(sp.Add.make_args(star_result))}")
    print()

    print("Expanding in e-basis...")
    expansion = expand_symmetric_in_e_basis(star_result, m, 5)
    print()
    print(f"e_2 * e_2 * e_1 in e-basis (m={m}):")
    for mu, c in expansion.items():
        cs = sp.simplify(c)
        length = len(mu)
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
    if ds_holds:
        print("VERDICT: DS HOLDS for lambda=(2,2,1). Dominance-support triangularity confirmed.")
    else:
        print("VERDICT: DS FAILS.")


if __name__ == "__main__":
    main()
