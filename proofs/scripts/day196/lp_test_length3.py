"""
Day 196: Test Length-Preservation (LP) conjecture at length 3.

LP: For any partition lambda, e_lambda^{*}(X) := e_{lambda_1} * ... * e_{lambda_l}
     lies in span{e_mu(X) : ell(mu) <= ell(lambda)}.

For length-2, LP is the Support-Preservation (SP) conjecture.
For length-3, LP predicts e_{(a,b,c)}^{*} is 3-row-supported.

We test the simplest nontrivial length-3 case: e_1 * e_1 * e_2 at m=5, n=4.

Method:
  e_1 * e_1 * e_2 = t^{-0} * e_1(Y) * (e_1(Y) * e_2(X))
    = e_1(Y) * ((1-q^{-1})[3]_t e_3(X) + q^{-1} e_1(X) e_2(X))   [by Thm 3.12]
    = (1-q^{-1})[3]_t * (e_1(Y) * e_3(X))
       + q^{-1} * (e_1(Y) * (e_1(X) e_2(X)))
    = (1-q^{-1})[3]_t * ((1-q^{-1})[4]_t e_4 + q^{-1} e_1 e_3)
       + q^{-1} * e_1(Y) . (e_1 e_2)

The first term is (1-q^{-1})^2 [3]_t [4]_t e_4 + q^{-1}(1-q^{-1})[3]_t e_1 e_3.
Support: {(4), (3,1)} = length <= 2.

The second term q^{-1} e_1(Y) . (e_1 e_2) is the interesting piece — it should be
computable directly via the AHA action.

At n=4, partitions are (4), (3,1), (2,2), (2,1,1), (1,1,1,1). We expect e_1*e_1*e_2
to have support in {(4), (3,1), (2,2), (2,1,1)} (length <= 3), NOT (1,1,1,1).

Actually, better plan: just compute e_1(Y) e_1(Y) e_2(Y) . 1 via AHA, then expand
in e-basis, and check that (1,1,1,1) coefficient is zero.

t^{-binom(1,2) - binom(1,2) - binom(2,2)} = t^{-1} (since binom(1,2)=0, binom(2,2)=1)
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


def compute_e1_star_e1_star_e2(m):
    """Compute e_1 * e_1 * e_2 in Hikita's *-product.

    e_1 * e_1 * e_2 has:
      lambda = (2, 1, 1),  ell(lambda) = 3,  sum binom(lambda_i, 2) = 0+0+1 = 1
      mathfrak_q(e_(2,1,1)(Y)) = t^1 (e_2 * e_1 * e_1) [note: * is commutative]
      So e_2 * e_1 * e_1 = t^{-1} * e_(2,1,1)(Y) . 1

    Alternatively:
      e_1 * e_1 * e_2 = e_1 * e_1 * e_2
      = mathfrak_q^{-1} of (LHS) is... just work directly:

    Concretely: e_1(Y) e_1(Y) e_2(Y) . 1 = mathfrak_q(e_1 e_1 e_2 (Y)) = t^1 (e_1*e_1*e_2)
    So e_1 * e_1 * e_2 = t^{-1} * (e_1(Y) e_1(Y) e_2(Y)) . 1
                      = t^{-1} * e_2(Y) . (e_1(Y) . (e_1(Y) . 1))
    """
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    # Start with 1
    F = sp.Integer(1)
    # Apply e_1(Y) .
    e1Y_F = sp.Integer(0)
    for i in range(1, m+1):
        e1Y_F = sp.expand(e1Y_F + Y_apply(F, i))
    print(f"[m={m}] e_1(Y) . 1: #terms = {len(sp.Add.make_args(e1Y_F))}")

    # Apply e_1(Y) again
    e1Y_e1Y_F = sp.Integer(0)
    # Need each Y_i . e1Y_F
    for i in range(1, m+1):
        e1Y_e1Y_F = sp.expand(e1Y_e1Y_F + Y_apply(e1Y_F, i))
    print(f"[m={m}] e_1(Y)^2 . 1: #terms = {len(sp.Add.make_args(e1Y_e1Y_F))}")

    # Apply e_2(Y):  sum over i<j of Y_i Y_j . (result so far)
    # But since Y's commute and we've already applied e_1(Y)^2, we can compute:
    # e_2(Y) = 1/2 (e_1(Y)^2 - p_2(Y)), i.e., apply e_2(Y) directly.
    # Actually simpler: e_2(Y) = sum_{i<j} Y_i Y_j.  Compute one Y at a time.

    # First compute Y_j . e1Y_e1Y_F for each j.
    Yj_result = {}
    for j in range(1, m+1):
        Yj_result[j] = Y_apply(e1Y_e1Y_F, j)

    # Sum: e_2(Y) . e1Y_e1Y_F = sum_{i<j} Y_i . (Y_j . e1Y_e1Y_F)
    total = sp.Integer(0)
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            piece = Y_apply(Yj_result[j], i)
            total = sp.expand(total + piece)

    # total = e_2(Y) e_1(Y)^2 . 1
    # But we want e_2(Y) e_1(Y) e_1(Y) . 1 = e_1(Y) e_1(Y) e_2(Y) . 1 (commute)
    # Since Y's commute in H_m, any ordering gives the same result.
    # And mathfrak_q(e_{(2,1,1)}(Y)) = t^1 (e_2 * e_1 * e_1) = t (e_1 * e_1 * e_2)
    # But e_2(Y) e_1(Y) e_1(Y) ≠ e_{(2,1,1)}(Y). The latter is a symmetric poly.
    # e_2(Y) * e_1(Y)^2 = e_2 * e_1^2 (as polynomials in Y) = e_{2,1,1}(Y) in Lambda(Y).
    # YES! e_{(2,1,1)}(Y) = e_2(Y) * e_1(Y) * e_1(Y) (ordinary product).
    # So total = e_{(2,1,1)}(Y) . 1 = mathfrak_q(e_{(2,1,1)}(Y)) = t^1 (e_1 * e_1 * e_2).
    # Thus e_1 * e_1 * e_2 = t^{-1} * total.

    star_result = sp.expand(total / t)
    print(f"[m={m}] e_1 * e_1 * e_2: #terms in expanded form = {len(sp.Add.make_args(star_result))}")

    # Expand in e-basis of Lambda^(m), degree n=4
    if m < 4:
        print(f"WARNING: m={m} < 4, need m >= 4 to see all partitions.")

    expansion = expand_symmetric_in_e_basis(star_result, m, 4)
    return expansion


def main():
    print("=" * 72)
    print("Day 196 LP test: e_1 * e_1 * e_2 at m=5, n=4")
    print("=" * 72)
    print("Prediction (LP): e_1*e_1*e_2 supported on partitions of length <= 3,")
    print("i.e., coefficient on (1,1,1,1) should be ZERO.")
    print()

    for m in [5]:
        print(f"--- m = {m} ---")
        expansion = compute_e1_star_e1_star_e2(m)
        print()
        print(f"e_1 * e_1 * e_2 in e-basis (m={m}):")
        for lam, c in expansion.items():
            cs = sp.simplify(c)
            length = len(lam)
            marker = "  <-- LENGTH 4!" if length == 4 else ""
            print(f"  ell={length}  e_{lam}: {sp.factor(cs)}{marker}")

        print()
        # Verify LP
        coef_1111 = expansion.get((1, 1, 1, 1), sp.Integer(0))
        coef_1111_simp = sp.simplify(coef_1111)
        print(f"KEY CHECK: coefficient on (1,1,1,1) = {sp.factor(coef_1111_simp)}")
        if coef_1111_simp == 0:
            print("VERDICT: LP HOLDS (length-preservation preserved at length 3).")
        else:
            print("VERDICT: LP FAILS (length-preservation broken at length 3).")


if __name__ == "__main__":
    main()
