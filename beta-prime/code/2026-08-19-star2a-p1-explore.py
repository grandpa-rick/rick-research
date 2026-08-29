"""Explore A_1 structure to find a closed form.

Working hypotheses to test:
  (H1) A_1(b, c, j) = (b+c-2)^{↓ (j-2)} * f(b, c, j) where f is low-degree.
  (H2) A_1(b, c, j) = (b+c)^{↓ j} * g(b, c, j) / h(b, c, j) for some rational.
  (H3) A_1 = A_0 * (correction rational).

The p=0 collapse is:
    Q_j(b) * A_0 = (b+2)_{c-1-j} * (b+c)^{↓ j} = (b+2)_{c-1}.

For p=1, if we can write
    Q_j(b) * A_1 = (b+2)_{c-3} * R_1
i.e., Q_j(b) * A_1 has FIVE fewer b-factors than Q_j * A_0.

Note: (b+2)_{c-1-j} has (c-1-j) factors. So A_1 must contribute (j-2) factors
of shape (b+2+i) times a poly of b-degree 2 in R_1 for the divisibility to
work out (deg_b LHS = c-1-j + deg_b A_1 = c-3 + deg_b R_1 = c-3+2 = c-1, so
deg_b A_1 must be j).

Actually deg_b A_1 = j? Let's check that first.
"""

import time
from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, Integer

a, b, c = symbols('a b c')
x1, x2, x3 = a + 2, b + 1, c


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def rise(x, L):
    p = Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


def bt(M):
    def vs(mu):
        L = len(mu) + 2
        bb = list(mu) + [0] * (L - len(mu))
        r = []
        for p in combinations(range(L), 2):
            n = bb.copy()
            for i in p:
                n[i] += 1
            ok = True
            for i in range(L - 1):
                if n[i] < n[i + 1]:
                    ok = False
                    break
            if not ok:
                continue
            while n and n[-1] == 0:
                n.pop()
            if len(n) > 3:
                continue
            r.append(tuple(n))
        return r

    cu = defaultdict(int)
    cu[()] = 1
    T = {0: [((0, 0, 0), 1)]}
    for j in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[j] = rs
    return T


def ds_symbolic(j, tables):
    xs = (x1, x2, x3)
    total = Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def dsV_all(J, tables):
    V = ds_symbolic(0, tables)
    cache = {}
    for j in range(J + 1):
        dsj = ds_symbolic(j, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0
        cache[j] = q.as_expr()
    return cache


def extract_A_p(j, p, dsV_cache):
    S = dsV_cache[j]
    if j - p < 0:
        return Integer(0)
    pab = Poly(S, a, b, c)
    result = Integer(0)
    for monom, cf in pab.terms():
        da, db, dc = monom
        if da == j - p:
            result += cf * b**db * c**dc
    return expand(result)


def per_mu_a_coef(j, p, mu_target, tables):
    """[a^{j-p}] of the SINGLE-partition contribution of mu_target to S_j:
       kappa_mu * s^*_mu(a+2, b+1, c) = kappa_mu * det[...] / V.
    Return this as poly in (b, c).
    """
    V = ds_symbolic(0, tables)
    xs = (x1, x2, x3)
    for mu, kap in tables[j]:
        if mu == mu_target:
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
            det_val = expand(kap * det3(rows))
            q, r = sp.div(Poly(det_val, [a, b, c]), Poly(V, [a, b, c]))
            assert r.as_expr() == 0
            s_mu = q.as_expr()
            # extract [a^{j-p}] coefficient
            pab = Poly(s_mu, a, b, c)
            result = Integer(0)
            for monom, cf in pab.terms():
                da, db, dc = monom
                if da == j - p:
                    result += cf * b**db * c**dc
            return expand(result)
    return Integer(0)


def main():
    J = 8
    print(f"Building tables up to j = {J}...")
    t0 = time.time()
    tables = bt(J)
    print(f"  built in {time.time()-t0:.2f}s")

    print(f"Computing ds_j/V symbolically...")
    dsV_cache = dsV_all(J, tables)
    print(f"  done in {time.time()-t0:.2f}s total.")

    print("\n" + "=" * 72)
    print("A_1 explicit + factored + deg_b")
    print("=" * 72)
    for j in range(1, J + 1):
        A1 = extract_A_p(j, 1, dsV_cache)
        deg_b_A1 = Poly(A1, b).degree() if A1 != 0 else -1
        deg_c_A1 = Poly(A1, c).degree() if A1 != 0 else -1
        print(f"\n j = {j}:  deg_b A_1 = {deg_b_A1}, deg_c A_1 = {deg_c_A1}")
        A1_f = sp.factor(A1)
        print(f"   A_1 factored = {A1_f}")

    # Per-mu contributions for small j
    print("\n" + "=" * 72)
    print("Per-mu contribution to A_1 = [a^{j-1}] S_j")
    print("=" * 72)
    for j in range(2, 6):
        print(f"\n j = {j}:")
        A1_total = extract_A_p(j, 1, dsV_cache)
        A1_check = Integer(0)
        for mu, kap in tables[j]:
            contrib = per_mu_a_coef(j, 1, mu, tables)
            if contrib != 0:
                A1_check += contrib
                print(f"    mu = {mu}, kappa = {kap}:  [a^{j-1}] contribution = {sp.factor(contrib)}")
        assert sp.simplify(A1_total - A1_check) == 0

    # A_0 (for comparison)
    print("\n" + "=" * 72)
    print("A_0 = (b+c)^{↓j} for comparison")
    print("=" * 72)
    for j in range(1, 6):
        A0 = extract_A_p(j, 0, dsV_cache)
        A0_f = sp.factor(A0)
        expected = fall(b + c, j)
        print(f"  j = {j}: A_0 = {A0_f},  (b+c)^↓j = {sp.factor(expected)},  match = {sp.simplify(A0 - expected) == 0}")

    # Try: A_1 - (some multiple of A_0) ?
    print("\n" + "=" * 72)
    print("Try: is A_1 / [(b+c-2)^{↓(j-2)}] a polynomial of small (b,c)-degree?")
    print("=" * 72)
    for j in range(2, 7):
        A1 = extract_A_p(j, 1, dsV_cache)
        # (b+c-2)^{↓(j-2)} = (b+c-2)(b+c-3)...(b+c-j+1), of length j-2
        L = j - 2
        if L < 0:
            continue
        div = Integer(1)
        for i in range(L):
            div *= (b + c - 2 - i)
        try:
            q, r = sp.div(Poly(A1, b, c), Poly(div, b, c))
            if r.as_expr() == 0:
                Q = q.as_expr()
                Q_f = sp.factor(Q)
                deg_b_Q = Poly(Q, b).degree() if Q != 0 else -1
                deg_c_Q = Poly(Q, c).degree() if Q != 0 else -1
                print(f"  j = {j}: A_1 / (b+c-2)^↓{L} = {Q_f}  (deg_b {deg_b_Q}, deg_c {deg_c_Q})")
            else:
                print(f"  j = {j}: does NOT divide, remainder = {r.as_expr()}")
        except Exception as e:
            print(f"  j = {j}: ERROR {e}")

    # Another try: A_1 / (b+c)^{↓(j-1)}? or similar
    print("\n" + "=" * 72)
    print("Try: is A_1 / (b+c)^{↓(j-1)} a polynomial?")
    print("=" * 72)
    for j in range(2, 7):
        A1 = extract_A_p(j, 1, dsV_cache)
        L = j - 1
        div = Integer(1)
        for i in range(L):
            div *= (b + c - i)
        try:
            q, r = sp.div(Poly(A1, b, c), Poly(div, b, c))
            if r.as_expr() == 0:
                Q = q.as_expr()
                Q_f = sp.factor(Q)
                print(f"  j = {j}: A_1 / (b+c)^↓{L} = {Q_f}")
            else:
                print(f"  j = {j}: does NOT divide")
        except Exception:
            pass

    # Try: A_1 * some prefactor = (b+c-1)^{↓(j-1)} * quadratic ?
    # From the observed j=3: A_1 = 3c(b+1)(b+c-3)(b+c-2)
    # (b+c-2)(b+c-3) = (b+c-2)^↓2, quadratic prefactor is 3c(b+1).
    # For j=4: A_1 = 2 * (b+c-3)(b+c-2) * (2b²c - b² + 2bc² - 8bc + b + c² - 7c)
    # (b+c-3)(b+c-2) = (b+c-2)^↓2, quadratic in (b,c) prefactor.
    # For j=5: A_1 = 5(b+c-4)(b+c-3)(b+c-2) * (b²c - b² + bc² - 6bc + b - 4c)
    # (b+c-4)(b+c-3)(b+c-2) = (b+c-2)^↓3, cubic prefactor.
    # So A_1 = c_j * (b+c-2)^↓{j-2} * P_j(b,c) where deg P_j <= (b+c)-degree 2?
    #
    # Let's extract that P_j:
    print("\n" + "=" * 72)
    print("Extract P_j from A_1 = c_j * (b+c-2)^↓{j-2} * P_j")
    print("=" * 72)
    from sympy import Rational
    for j in range(2, 8):
        A1 = extract_A_p(j, 1, dsV_cache)
        L = j - 2
        div = Integer(1)
        for i in range(L):
            div *= (b + c - 2 - i)
        try:
            q, r = sp.div(Poly(A1, b, c), Poly(div, b, c))
            if r.as_expr() == 0:
                Q = q.as_expr()
                deg_b_Q = Poly(Q, b).degree() if Q != 0 else -1
                deg_c_Q = Poly(Q, c).degree() if Q != 0 else -1
                print(f"\n  j = {j}: P_j has (deg_b={deg_b_Q}, deg_c={deg_c_Q})")
                print(f"    P_j = {sp.expand(Q)}")
                print(f"    P_j factored = {sp.factor(Q)}")
        except Exception:
            pass


if __name__ == "__main__":
    main()
