"""
Day 196: Test LP at length 3 with lambda=(3,1,1) at n=5.

Compute e_1 * e_1 * e_3 in e-basis. Prediction (LP): support in length <= 3
partitions, i.e., zero coefficient on (2,1,1,1) and (1,1,1,1,1).
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
            raise ValueError(f"si_apply supports i=1..m-1, got i={i}")
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
    """Compute (e_{factors[0]} * e_{factors[1]} * ... * e_{factors[-1]}) at m variables.

    Uses mathfrak_q: e_lambda(Y) . 1 = t^{sum binom(lambda_i, 2)} * (star product of e_{lambda_i}).
    So star product = t^{-sum binom(l,2)} * (prod e_{l}(Y)) . 1.
    We commute Y's (they commute) and apply one e_r(Y) at a time.
    """
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)

    # Compute prod e_{f}(Y) . 1 by applying each e_{f}(Y) in sequence
    F = sp.Integer(1)
    scalar_factor = sp.Integer(1)
    for f in factors:
        scalar_factor = scalar_factor * t**(-f*(f-1)/2)
        # Apply e_f(Y) . F
        # e_f(Y) = sum over |I|=f of prod_{i in I} Y_i
        # Compute by summing over all size-f subsets
        subsets = list(combinations(range(1, m+1), f))
        new_F = sp.Integer(0)
        for I in subsets:
            # Apply Y_{I[0]} . Y_{I[1]} . ... F
            piece = F
            for i in I:
                piece = Y_apply(piece, i)
            new_F = sp.expand(new_F + piece)
        F = new_F
        print(f"  after e_{f}(Y) applied: #terms = {len(sp.Add.make_args(F))}")

    # Multiply by scalar_factor
    star_result = sp.expand(scalar_factor * F)
    return star_result


def main():
    print("=" * 72)
    print("Day 196 LP test at length 3: e_1 * e_1 * e_3 at m=6, n=5")
    print("=" * 72)
    print("Prediction (LP): support in length <= 3 partitions of 5.")
    print("Partitions of 5: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1^5)")
    print("LP predicts: zero coefficient on (2,1,1,1) and (1,1,1,1,1) (length 4, 5).")
    print()

    m = 6
    star_result = compute_e_star_product(m, [1, 1, 3])
    print(f"[m={m}] e_1*e_1*e_3: total #terms in expanded form = {len(sp.Add.make_args(star_result))}")

    print()
    print("Expanding in e-basis...")
    expansion = expand_symmetric_in_e_basis(star_result, m, 5)
    print()
    print(f"e_1 * e_1 * e_3 in e-basis (m={m}):")
    for lam, c in expansion.items():
        cs = sp.simplify(c)
        length = len(lam)
        marker = f"  <-- LENGTH {length}" if length >= 4 else ""
        print(f"  ell={length}  e_{lam}: {sp.factor(cs)}{marker}")

    print()
    all_zero = True
    for lam, c in expansion.items():
        if len(lam) >= 4:
            simp = sp.simplify(c)
            print(f"e_{lam} coefficient (should be 0 if LP holds): {sp.factor(simp)}")
            if simp != 0:
                all_zero = False

    if all_zero:
        print("VERDICT: LP HOLDS at length 3 for lambda=(3,1,1).")
    else:
        print("VERDICT: LP FAILS at length 3.")


if __name__ == "__main__":
    main()
