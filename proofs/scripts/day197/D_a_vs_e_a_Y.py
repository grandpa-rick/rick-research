"""Day 197 PROVE — Route-2 attack: check whether D'Adderio et al.'s Negut operator
D_{(2)} from arXiv:2608.14836 coincides with Hikita's e_2(Y) action on the level-1
polynomial rep of the affine Hecke algebra.

Reference for D_{(m)} (Thm 4.3, p.12 of 2608.14836):

    D_{(m)} F[X] = (-1)^m <z^m> Exp[-zX] F[X + M/z],       M = (1-q)(1-t).

This is an operator on the symmetric-function algebra Lambda.

Reference for e_a(Y) (Rick's Days 191-196 framework):

    e_a(Y) . f(X_1,...,X_m) acts on symmetric polynomials in m variables via the
    Cherednik operators Y_i built from T_i^{-1} and the affine cycle Pi.
    Then e_a *_H e_r =  t^{-a(a-1)/2}  e_a(Y) . e_r(X).

Since D_{(m)} is written on Lambda and e_a(Y) is written on Lambda_m, the fair
comparison is: convert e_2(Y).e_r(X_1,...,X_m) to the power-sum basis (thus to
an element of Lambda), and compare with D_{(2)} e_r[X] in the power-sum basis.

We compute p_lambda-coefficients using specialization at test points t_1,...,t_N
with N = a+r large enough. The plethystic operator Exp[-zX] F[X + M/z] is
handled by expanding F in the p-basis, applying X -> X + M/z as
p_k -> p_k + (M/z)^k, and multiplying by Exp[-zX] = sum_{n>=0} h_n[-zX].
For small deg n = a + r we only need finitely many h_n terms.

Test:  f = e_r(x_1,...,x_m) for m = 3 and r in {1, 2}.
       a = 2 (so total deg = 3 or 4).
"""

import sympy as sp
from itertools import combinations
from sympy.combinatorics.partitions import IntegerPartition

q, t = sp.symbols('q t')
z = sp.symbols('z')


# ---------------- Hikita side: e_a(Y) via T_i, Pi ---------------- #

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


def apply_e2_Y(F, m):
    """e_2(Y) . F = sum_{i<j} Y_i Y_j . F  (Y_i commute)."""
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    Yj = {}
    for j in range(1, m + 1):
        Yj[j] = Y_apply(F, j)
    total = sp.Integer(0)
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            total = sp.expand(total + Y_apply(Yj[j], i))
    return total


# ---------------- Symmetric-function machinery on Lambda ---------------- #

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


def p_lambda_in_vars(lam, vars_):
    """Power-sum p_lambda in the given variables."""
    def p_k(k):
        return sum(v**k for v in vars_)
    r = sp.Integer(1)
    for a in lam:
        r *= p_k(a)
    return sp.expand(r)


def poly_to_p_basis(F, vars_, deg):
    """Expand a symmetric polynomial F of homogeneous degree deg in vars_
    into the p-basis. Returns dict lam -> coeff."""
    F = sp.expand(F)
    parts = partitions_of(deg)
    # Choose a monomial for each partition to read off a coeff: the sorted
    # monomial x_1^{lam_1} x_2^{lam_2} ... .  For symmetric polys this pins
    # down the m-basis coefficient, but we want p-basis. Better: build the
    # transition matrix from p_lambda to that monomial basis, then invert.
    if len(vars_) < deg:
        raise ValueError("Need len(vars) >= deg for a faithful p-basis test.")
    # canonical partition-shaped monomial
    canonicals = []
    for lam in parts:
        mon = sp.Integer(1)
        for i, a in enumerate(lam):
            mon *= vars_[i]**a
        canonicals.append(mon)
    Fpoly = sp.Poly(F, *vars_)
    b_vec = sp.Matrix([Fpoly.coeff_monomial(sp.Poly(mon, *vars_).monoms()[0])
                       for mon in canonicals])
    A_rows = []
    for lam in parts:
        pl = p_lambda_in_vars(lam, vars_)
        pl_poly = sp.Poly(pl, *vars_)
        row = [pl_poly.coeff_monomial(sp.Poly(mon, *vars_).monoms()[0])
               for mon in canonicals]
        A_rows.append(row)
    A = sp.Matrix(A_rows).T
    coeffs = A.solve(b_vec)
    return {lam: sp.cancel(coeffs[i]) for i, lam in enumerate(parts)}


# ---------------- D'Adderio side: D_{(m)} on Lambda ---------------- #
# D_{(m)} F[X] = (-1)^m <z^m> Exp[-zX] F[X + M/z], M = (1-q)(1-t).

M = (1 - q) * (1 - t)


def h_n_in_vars(n, vars_):
    """h_n(vars). n=0 -> 1."""
    if n == 0:
        return sp.Integer(1)
    # sum over multisets of size n from vars
    r = sp.Integer(0)
    def gen(start, remaining, current):
        nonlocal r
        if remaining == 0:
            term = sp.Integer(1)
            for v in current:
                term *= v
            r = r + term
            return
        for i in range(start, len(vars_)):
            current.append(vars_[i])
            gen(i, remaining - 1, current)
            current.pop()
    gen(0, n, [])
    return sp.expand(r)


def apply_D_m_to_polynomial(F_poly, m_op, vars_, deg_F):
    """Compute D_{(m_op)} applied to a symmetric polynomial F_poly of homogeneous
    degree deg_F in vars_.

    Strategy: convert F to p-basis, apply the operator symbolically at the p-level:
        Exp[-zX] = sum_{n>=0} h_n[-zX] p-expanded  -->  h_n(-z * vars).
        F[X + M/z] : substitute p_k -> p_k(vars_) + (M/z)^k in the p-expansion of F.
        Multiply the two (they are elements of Lambda[[z, z^{-1}]] on the vars),
        take coefficient of z^{m_op}, multiply by (-1)^{m_op}.

    Result: a symmetric polynomial in vars_ of homogeneous degree deg_F + m_op.
    """
    # Step 1: F in p-basis
    F_p = poly_to_p_basis(F_poly, vars_, deg_F)

    # Step 2: F[X + M/z].  p_k -> (sum vars^k) + (M/z)^k.
    def pk_shifted(k):
        return sum(v**k for v in vars_) + (M / z)**k

    F_shifted = sp.Integer(0)
    for lam, c in F_p.items():
        if c == 0:
            continue
        term = c
        for a in lam:
            term = term * pk_shifted(a)
        F_shifted = F_shifted + term
    F_shifted = sp.expand(F_shifted)
    # Now F_shifted is a Laurent polynomial in z with symmetric-poly coefficients.

    # Step 3: Exp[-zX] = sum_{n>=0} h_n[-zX] = sum_{n>=0} h_n(-z*vars).
    #         = sum_{n>=0} (-z)^n h_n(vars).
    # We need to expand up to the degree in z^{-1} appearing in F_shifted,
    # so that z^{m_op} coefficient survives.
    #
    # Maximum negative power of z in F_shifted is up to deg_F (since each p_k
    # contributes (M/z)^k with k <= deg_F).
    # So z^{m_op} = z^{m_op - n} * z^n comes from n = m_op + (neg power in F_shifted).
    # We need n up to m_op + deg_F.
    N_max = m_op + deg_F
    Exp_series = sp.Integer(0)
    for n in range(N_max + 1):
        Exp_series = Exp_series + (-z)**n * h_n_in_vars(n, vars_)

    # Step 4: multiply, clear negative z-powers, extract coefficient of z^{m_op}.
    # Max negative power of z in F_shifted is deg_F.
    product = sp.expand(Exp_series * F_shifted)
    # Multiply by z^{deg_F} to make it a polynomial in z; then take coeff of z^{m_op + deg_F}.
    cleared = sp.expand(product * z**deg_F)
    prod2 = sp.Poly(cleared, z)
    target_power = m_op + deg_F
    if target_power > prod2.degree():
        coeff = sp.Integer(0)
    else:
        coeff = prod2.coeff_monomial(z**target_power)

    result = sp.expand((-1)**m_op * coeff)
    return result


# ---------------- Main comparison ---------------- #

def compare(m, r, renorm_qk=0, renorm_tk=0, include_star_norm=True, verbose=True):
    X = sp.symbols(f'X1:{m+1}')
    e_r = e_r_X(m, r)

    if verbose:
        print(f"\n=== m={m}, r={r} (include_star_norm={include_star_norm}) ===")
        print(f"e_{r}(X) = {e_r}")

    # Hikita side: e_2 * e_r = t^{-1} e_2(Y) . e_r(X)  (star normalization)
    lhs_Hikita = apply_e2_Y(e_r, m)
    if include_star_norm:
        # a=2 gives t^{-a(a-1)/2} = t^{-1}
        lhs_Hikita = sp.expand(lhs_Hikita / t)
    else:
        lhs_Hikita = sp.expand(lhs_Hikita)
    lhs_Hikita_p = poly_to_p_basis(lhs_Hikita, list(X), r + 2)

    if verbose:
        print(f"\nHikita e_2(Y).e_{r}(X)  in p-basis:")
        for lam, c in lhs_Hikita_p.items():
            cs = sp.factor(sp.cancel(c))
            print(f"  p_{lam}: {cs}")

    # D'Adderio side: D_{(2)} e_r (viewed as symmetric function via specialization to m vars)
    rhs_D = apply_D_m_to_polynomial(e_r, 2, list(X), r)
    rhs_D = sp.expand(rhs_D)
    rhs_D_p = poly_to_p_basis(rhs_D, list(X), r + 2)

    if verbose:
        print(f"\nD_(2) e_{r}  in p-basis (evaluated in {m} vars):")
        for lam, c in rhs_D_p.items():
            cs = sp.factor(sp.cancel(c))
            print(f"  p_{lam}: {cs}")

    # Renormalize Hikita side by q^{renorm_qk} * t^{renorm_tk}
    scale = q**renorm_qk * t**renorm_tk

    diffs = {}
    match_all = True
    parts = partitions_of(r + 2)
    for lam in parts:
        lhs_c = lhs_Hikita_p.get(lam, sp.Integer(0)) * scale
        rhs_c = rhs_D_p.get(lam, sp.Integer(0))
        d = sp.simplify(sp.cancel(lhs_c - rhs_c))
        diffs[lam] = d
        if d != 0:
            match_all = False

    if verbose:
        print(f"\nDifference (scale q^{renorm_qk} t^{renorm_tk} * Hikita  -  D'Adderio):")
        for lam, d in diffs.items():
            print(f"  p_{lam}: {sp.factor(d)}")
        print(f"MATCH: {match_all}")

    return match_all, diffs, lhs_Hikita_p, rhs_D_p


def try_renormalizations(m, r):
    print(f"\n### RENORMALIZATION SWEEP for m={m}, r={r} ###")
    best = None
    best_score = None
    for qk in range(-4, 5):
        for tk in range(-4, 5):
            match, diffs, lh, rh = compare(m, r, qk, tk, verbose=False)
            score = sum(1 for d in diffs.values() if d == 0)
            if match:
                print(f"  ** EXACT MATCH at q^{qk} t^{tk} **")
                return (qk, tk, True, diffs)
            if best is None or score > best_score:
                best_score = score
                best = (qk, tk, diffs)
    qk, tk, diffs = best
    print(f"  Best near-miss: q^{qk} t^{tk}, {best_score}/{len(diffs)} zero diffs")
    print(f"  Residual diffs at best:")
    for lam, d in diffs.items():
        print(f"    p_{lam}: {sp.factor(d)}")
    return (qk, tk, False, diffs)


if __name__ == "__main__":
    # Primary test: m=3, r=1 and r=2
    print("=" * 70)
    print("Day 197 PROVE - D_{(2)} vs e_2(Y) on Hikita level-1 rep")
    print("=" * 70)

    for r in [1, 2]:
        # Need m >= a+r = 2+r for faithful p-basis test
        m = max(3, 2 + r)
        # Try with star normalization (Rick's convention includes t^{-1} for a=2)
        match, diffs, _, _ = compare(m, r, include_star_norm=True)
        if not match:
            print(f"\nRaw comparison FAILED for m={m}, r={r}. Trying renormalizations (with star norm)...")
            try_renormalizations(m, r)
        # Also try without star normalization
        print(f"\n--- Now without star normalization ---")
        match2, diffs2, _, _ = compare(m, r, include_star_norm=False)
