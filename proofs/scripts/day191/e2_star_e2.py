"""
Day 191 PROVE: Compute e_2(X) * e_2(X) in Hikita's *-product on Lambda_{q,t}.

Approach: work in Q_{q,t}[X_1, ..., X_m] with the level-one polynomial rep
of the affine Hecke algebra H_m (Hikita 2503.23597 sec 2.5).

Key formulas (Hikita 2.9 + 2.11):
  T_i . F = t s_i(F) + (t - 1) (F - s_i(F))/(1 - X_i/X_{i+1})     [i=1..m-1]
  Pi . F(X_1,...,X_m) = X_1 * F(X_2, ..., X_m, q^{-1} X_1)
  X_{m+1} = q^{-1} X_1  and  X_0 = q X_m
  Y_i = t^{m-i} T_{i-1} ... T_1 Pi T_{m-1}^{-1} ... T_i^{-1}  (i=1..m)

Key relations:
  e_a(X) *_H e_b(X) = q^{-1}_(m)(e_a) . e_b(X)
                    = t^{-a(a-1)/2} e_a(Y_1,...,Y_m) . e_b(X)

So e_2 * e_2 = t^{-1} e_2(Y) . e_2(X), where e_2(Y) = sum_{i<j} Y_i Y_j.

Since e_2(Y) is central in H_m, the result is symmetric in X.

We compute for m=4 and m=5, expand in e_lambda-basis of the symmetric
polynomials of degree 4, verify stability, and check q=1 -> ordinary product.
"""

import sympy as sp
from itertools import combinations, product

q, t = sp.symbols('q t')

def qint(n):
    return sum(t**i for i in range(n))


def build_action(m):
    """Build T_i, T_i^{-1}, Pi actions and Y_i actions in Q_{q,t}[X_1, ..., X_m].
       We work in Q(q,t)[X_1, ..., X_m]  (positive powers only for polynomial
       inputs).  Since Pi introduces q^{-1}, we need X to be a polynomial in
       variables carrying no q-poles other than through coefficients.

       All actions are represented as functions Poly -> Poly.
    """
    X = sp.symbols(f'X1:{m+1}')

    def _norm_X_index(i):
        """Return (variable, q_scale) for X_i where i is any integer.
           X_{i+km} = q^{-k} X_i (Hikita 2.1).  So X_i = q^{-k} X_{i mod m},
           where k = i // m (using 1-based indexing: idx 1..m).
        """
        # convert to 1-based: given i, find j in 1..m and k such that
        # i = j + k*m
        j = ((i - 1) % m) + 1
        k = (i - j) // m
        return X[j-1], q ** (-k)

    def si_apply(F, i):
        """Apply s_i to F.  For i in 1..m-1: swap X_i, X_{i+1}.
           For i=0: s_0(F) = X_1 X_0^{-1} * F(X_0, X_2, ..., X_{m-1}, X_{m+1})
                          = q^{-1} X_1 X_m^{-1} * F(q X_m, X_2, ..., X_{m-1}, q^{-1} X_1).
           But we only need i=1..m-1 for T_i, so let's implement that.
        """
        if i < 1 or i >= m:
            raise ValueError("si_apply supports i=1..m-1")
        subs = {X[i-1]: X[i], X[i]: X[i-1]}
        return sp.expand(F.xreplace(subs))

    def Ti_apply(F, i):
        """T_i . F for i=1..m-1."""
        F = sp.expand(F)
        sF = si_apply(F, i)
        diff = sp.expand(F - sF)
        # (F - s_i F) / (1 - X_i/X_{i+1}) = X_{i+1} * (F - s_i F) / (X_{i+1} - X_i)
        # F - s_i F is divisible by (X_i - X_{i+1}).
        quot = sp.cancel(diff / (X[i-1] - X[i]))     # (F-sF)/(X_i - X_{i+1})
        # 1 / (1 - X_i/X_{i+1}) = X_{i+1}/(X_{i+1} - X_i) = -X_{i+1}/(X_i - X_{i+1})
        result = t * sF + (t - 1) * (-X[i]) * quot
        return sp.expand(result)

    def Ti_inv_apply(F, i):
        """T_i^{-1} . F for i=1..m-1.
           T_i^{-1} . F = s_i F + (1 - t^{-1}) * (X_i/X_{i+1} F - s_i F)/(1 - X_i/X_{i+1})
                       = s_i F + (1 - t^{-1}) * X_i * (F - X_{i+1}^{-1} X_i s_i F)/...
           Simpler: from (T_i - t)(T_i + 1) = 0, T_i^{-1} = (1/t)*T_i - (t-1)/t (as operator).
           Wait let's re-derive: (T_i - t)(T_i + 1) = 0 gives T_i^2 = (t-1) T_i + t.
           So T_i * T_i = (t-1) T_i + t*I, i.e., I = T_i^2/t - (t-1) T_i / t
              I = T_i (T_i - (t-1))/t = (T_i - (t-1))/t * T_i
           So T_i^{-1} = (T_i - (t-1))/t = T_i / t - (t-1)/t.
        """
        Ti_F = Ti_apply(F, i)
        return sp.expand(Ti_F / t - (t - 1) / t * F)

    def Pi_apply(F):
        """Pi . F = X_1 * F(X_2, ..., X_m, q^{-1} X_1)."""
        # substitute X_1 -> X_2, X_2 -> X_3, ..., X_{m-1} -> X_m, X_m -> q^{-1} X_1
        # need simultaneous substitution
        subs = {X[i]: X[i+1] for i in range(m-1)}
        subs[X[m-1]] = q**(-1) * X[0]
        Fshift = sp.expand(F.xreplace(subs))
        return sp.expand(X[0] * Fshift)

    def Y_apply(F, i):
        """Y_i . F for i in 1..m.  Y_i = t^{m-i} T_{i-1} ... T_1 Pi T_{m-1}^{-1} ... T_i^{-1}."""
        # First apply T_{m-1}^{-1} T_{m-2}^{-1} ... T_i^{-1} (rightmost first: T_i^{-1} applied first)
        # Reading Y_i left to right: t^{m-i} * T_{i-1} * ... * T_1 * Pi * T_{m-1}^{-1} * ... * T_i^{-1}
        # Applied to F: we start from the right.  First apply T_i^{-1}, then T_{i+1}^{-1}, ..., T_{m-1}^{-1}.
        G = F
        for j in range(i, m):   # T_i^{-1}, T_{i+1}^{-1}, ..., T_{m-1}^{-1}  (m-i terms)
            G = Ti_inv_apply(G, j)
        # Now Pi
        G = Pi_apply(G)
        # Then T_1, T_2, ..., T_{i-1}
        for j in range(1, i):
            G = Ti_apply(G, j)
        # Finally multiply by t^{m-i}
        return sp.expand(t**(m - i) * G)

    return X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply


def e_r_X(m, r):
    """r-th elementary symmetric polynomial in X_1, ..., X_m."""
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
    """Return list of partitions of n as tuples (lambda_1 >= ... >= lambda_l)."""
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
    """Product of e_{lambda_i}(X_1,...,X_m)."""
    result = sp.Integer(1)
    for p in lam:
        result *= e_r_X(m, p)
    return sp.expand(result)


def expand_symmetric_in_e_basis(F, m, n):
    """F is a symmetric polynomial of total degree n in X_1,...,X_m.
       Return dict lam -> coefficient in Q(q,t) such that F = sum coeff * e_lam(X_1..X_m).
       Requires m >= n so all partitions of n have nonzero e_lam(X_1..X_m).
       Matching monomials: for each partition, pick canonical monomial x_1^{lam_1} ... x_l^{lam_l}.
    """
    X = sp.symbols(f'X1:{m+1}')
    parts = partitions_of(n)
    if m < n:
        raise ValueError("Need m >= n.")
    # For each partition, choose canonical monomial x_1^lam_1 * x_2^lam_2 * ... * x_l^lam_l
    canonicals = []
    for lam in parts:
        mon = sp.Integer(1)
        for i, p in enumerate(lam):
            mon *= X[i]**p
        canonicals.append(mon)
    # Compute e_lam matrix
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


def compute_e2_star_e2(m):
    """Compute e_2 * e_2 in Lambda_{q,t}^{(m)} using Hikita's *-product.

       e_2(X) * e_2(X) = t^{-1} * e_2(Y_1,...,Y_m) . e_2(X_1,...,X_m).
       Return dict lam -> coefficient (in Q(q,t)).
    """
    X, Ti_apply, Ti_inv_apply, Pi_apply, Y_apply = build_action(m)
    e2X = e_r_X(m, 2)
    # Compute e_2(Y) . e_2(X) = sum_{i<j} Y_i Y_j . e_2(X)
    # = sum_{i<j} Y_i . (Y_j . e_2(X))
    print(f"[m={m}] Computing Y_j . e_2(X) for j=1..{m} ...")
    Yj_e2 = {}
    for j in range(1, m + 1):
        Yj_e2[j] = Y_apply(e2X, j)
        print(f"  Y_{j} . e_2(X) computed; #terms = {len(sp.Add.make_args(Yj_e2[j]))}")
    print(f"[m={m}] Computing Y_i . (Y_j . e_2(X)) for i<j and summing ...")
    total = sp.Integer(0)
    count = 0
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            # We want Y_i Y_j . e_2(X).  Y_i Y_j = Y_j Y_i (they commute), so
            # apply Y_j first, then Y_i.  Equivalent to apply Y_i to Yj_e2[j].
            piece = Y_apply(Yj_e2[j], i)
            total = sp.expand(total + piece)
            count += 1
            print(f"  (i,j)=({i},{j}) done; running total #terms = {len(sp.Add.make_args(total))}")
    # total = e_2(Y) . e_2(X); multiply by t^{-1}
    star = sp.expand(total / t)
    print(f"[m={m}] e_2 * e_2 computed as polynomial in X_1..X_{m}.  #terms = {len(sp.Add.make_args(star))}")
    # Expand in e-basis of Lambda^{(m)}, using partitions of 4.
    # Total degree should be 4.  If m < 4, some partitions of 4 vanish; we still
    # need m >= 4 for full information.
    if m < 4:
        print(f"  WARNING: m={m} < 4, so not all partitions of 4 are represented.")
    expansion = expand_symmetric_in_e_basis(star, m, 4)
    return expansion


def main():
    print("=" * 72)
    print("Day 191 PROVE: e_2(X) * e_2(X) in Hikita's *-product on Lambda_{q,t}")
    print("=" * 72)

    for m in [4]:  # start with m=4
        print(f"\n--- m = {m} ---")
        expansion = compute_e2_star_e2(m)
        print(f"\ne_2 * e_2 in e-basis (m={m}):")
        for lam, c in expansion.items():
            cs = sp.simplify(c)
            print(f"  e_{lam}: {sp.factor(cs)}")
            # Also print in simple form
            print(f"    = {sp.expand(cs)}")


if __name__ == "__main__":
    main()
