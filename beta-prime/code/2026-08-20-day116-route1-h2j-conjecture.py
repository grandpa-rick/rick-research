"""Day 116 — Route 1: Test conjecture S_j == (h_2^*)^j (or small variant).

Setup from Day 116 Attack B report:
  S_j(u, y, c) := sum_mu kap_mu * s^*_mu(u, y, c),   (u, y, c) := (a+2, b+1, c)

where s^*_mu is the factorial Schur (descending falling-factorial convention):
  s^*_mu(x_1,...,x_n) = det[ fall(x_i, mu_j + n - j) ] / det[ fall(x_i, n - j) ]
                     = det[ fall(x_i, mu_j + n - j) ] / V(x)

and V(x) = prod_{i<j}(x_i - x_j) is the Vandermonde.

Attack B ranked #1 next test: is S_j = h_2^{*j}(u, y, c)?
Here h_2^* := s^*_{(2)}.

We compute h_2^{*j} for j=0..4 and compare to S_j.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer

a, b, c = symbols('a b c')
u_var, y_var = symbols('u y')


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11 * (a22 * a33 - a23 * a32)
            - a12 * (a21 * a33 - a23 * a31)
            + a13 * (a21 * a32 - a22 * a31))


def bt(M):
    """Reproduce Attack B's bt(): iterated (h_2 Pieri-like) branching."""
    def vs(mu):
        L = len(mu) + 2
        bb = list(mu) + [0] * (L - len(mu))
        r = []
        for pp in combinations(range(L), 2):
            n = bb.copy()
            for i in pp:
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
    for jj in range(1, M + 1):
        nx = defaultdict(int)
        for mu, cc in cu.items():
            for nu in vs(mu):
                nx[nu] += cc
        cu = nx
        rs = []
        for mu, cc in sorted(cu.items(), reverse=True):
            pd = tuple(list(mu) + [0] * (3 - len(mu)))
            rs.append((pd, cc))
        T[jj] = rs
    return T


def V_uyc(xs):
    """Vandermonde in xs = (x0, x1, x2)."""
    x0, x1, x2 = xs
    return (x0 - x1) * (x0 - x2) * (x1 - x2)


def factorial_schur(mu, xs):
    """s^*_mu(xs) in Attack B's convention:
       det[ fall(x_i, mu[col] + (2 - col)) ] / V(xs).
       xs is a tuple of 3 variables.
    """
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    num = det3(rows)
    V = V_uyc(xs)
    vars_ = list(xs)
    q, r = sp.div(Poly(num, *vars_), Poly(V, *vars_))
    assert r.as_expr() == 0, f"V does not divide numerator for mu={mu}"
    return q.as_expr()


def ds_symbolic_uyc(jj, tables):
    xs = (u_var, y_var, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def S_of_uyc(jj, tables):
    """S_j in (u, y, c) variables directly."""
    dsj = ds_symbolic_uyc(jj, tables)
    V = V_uyc((u_var, y_var, c))
    q, r = sp.div(Poly(dsj, u_var, y_var, c), Poly(V, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def main():
    J = 4
    print(f"Building shifted-Schur tables up to j = {J} ...")
    tables = bt(J)
    for jj in range(J + 1):
        print(f"  j={jj}: {tables[jj]}")

    xs = (u_var, y_var, c)
    V = V_uyc(xs)

    print("\n" + "=" * 78)
    print("STEP 1: Compute h_2^* = s^*_{(2)}(u, y, c) using Attack B's convention.")
    print("=" * 78)
    h2_star = factorial_schur((2, 0, 0), xs)
    print(f"h_2^*(u,y,c) = {h2_star}")
    print(f"expanded = {expand(h2_star)}")

    # Also compute the ordinary h_2:
    h2_ord = u_var * y_var + u_var * c + y_var * c + u_var**2 + y_var**2 + c**2
    # Wait, h_2 = sum_{i<=j} x_i x_j = e_1^2/2 + ... no:
    # h_2(x_1,...,x_n) = sum_{i<=j} x_i x_j
    h2_ord = sum(x*y for i, x in enumerate(xs) for j, y in enumerate(xs) if i <= j)
    print(f"\nOrdinary h_2(u,y,c) = {expand(h2_ord)}")
    print(f"\nDifference h_2^* - h_2 = {expand(h2_star - h2_ord)}")

    print("\n" + "=" * 78)
    print("STEP 2: Compute S_j and (h_2^*)^j for j=0..4 and compare.")
    print("=" * 78)

    results = {}
    for jj in range(J + 1):
        S_j = S_of_uyc(jj, tables)
        h2j = expand(h2_star ** jj)
        diff = expand(S_j - h2j)
        equal = (diff == 0)
        results[jj] = (S_j, h2j, diff, equal)
        print(f"\n--- j = {jj} ---")
        print(f"  S_j vs h_2^{{*j}} EQUAL? {equal}")
        if not equal:
            print(f"  S_j - h_2^*^j = {diff}")

    print("\n" + "=" * 78)
    print("STEP 3: If not equal, check RATIO and small variants.")
    print("=" * 78)

    for jj in range(1, J + 1):
        S_j, h2j, diff, equal = results[jj]
        if equal:
            continue
        # Try ratio
        try:
            q, r = sp.div(Poly(S_j, u_var, y_var, c),
                          Poly(h2j, u_var, y_var, c))
            if r.as_expr() == 0:
                print(f"  j={jj}: S_j / (h_2^*)^j = {q.as_expr()}")
            else:
                print(f"  j={jj}: h_2^*^j does NOT divide S_j "
                      f"(remainder degree = {r.total_degree()})")
        except Exception as e:
            print(f"  j={jj}: division error {e}")

        # Ratio in the other direction
        try:
            q, r = sp.div(Poly(h2j, u_var, y_var, c),
                          Poly(S_j, u_var, y_var, c))
            if r.as_expr() == 0:
                print(f"  j={jj}: (h_2^*)^j / S_j = {q.as_expr()}")
        except Exception:
            pass

    print("\n" + "=" * 78)
    print("STEP 4: Compare kappa_mu coefficients to Kostka numbers K_{mu,(2^j)}.")
    print("        The expansion h_2^j = sum_mu K_{mu,(2^j)} s_mu in ORDINARY Schurs.")
    print("        If kappa_mu match, then S_j = 'shifted analogue of h_2^j'.")
    print("=" * 78)

    # Directly compute (h_2)^j in ordinary Schurs and compare kappa_mu.
    # Use ordinary Schur polynomials in 3 variables.
    def ord_schur(mu, xs):
        """Ordinary Schur polynomial s_mu(xs) via Jacobi–Trudi bialternant.
           s_mu = det[x_i^{mu_j + n - 1 - j}] / V(x).
        """
        n = 3
        rows = [[xs[i]**(mu[col] + n - 1 - col) for col in range(n)]
                for i in range(n)]
        num = det3(rows)
        V = V_uyc(xs)
        vars_ = list(xs)
        q, r = sp.div(Poly(num, *vars_), Poly(V, *vars_))
        assert r.as_expr() == 0
        return q.as_expr()

    for jj in range(J + 1):
        h2_ord_j = expand(h2_ord ** jj)
        # Expand h_2_ord^j in ordinary Schurs by peeling off leading monomials.
        # For 3 variables, partitions of 2j with at most 3 parts.
        parts = [p for p in tables[jj]]  # candidate mus from bt
        # Kostka expansion: h_2^j = sum_mu K_{mu,(2^j)} s_mu
        # We'll do it via row-reduction of the leading monomial.
        F = h2_ord_j
        kostka = {}
        while True:
            F = expand(F)
            if F == 0:
                break
            P = Poly(F, *xs)
            if P.total_degree() < 0:
                break
            leading = sorted(P.terms(), reverse=True)[0]
            monom, cf = leading
            # For s_mu with mu = (m0, m1, m2) descending, leading monomial is x0^m0 x1^m1 x2^m2.
            mu = tuple(monom)
            if not (mu[0] >= mu[1] >= mu[2]):
                print(f"    !! non-partition leading monomial {mu} coef {cf}")
                break
            s_mu = ord_schur(mu, xs)
            kostka[mu] = cf
            F = expand(F - cf * s_mu)

        print(f"\n  j = {jj}:  ordinary h_2^j Schur expansion:")
        for mu, k in sorted(kostka.items(), reverse=True):
            print(f"     mu={mu}: coef = {k}")
        print(f"  Attack B's kappa_mu (from bt table):")
        for mu, k in tables[jj]:
            print(f"     mu={mu}: kap = {k}")

        # Compare
        match = True
        all_mus = set(kostka.keys()) | set(mu for mu, _ in tables[jj])
        for mu in sorted(all_mus, reverse=True):
            kap = dict(tables[jj]).get(mu, 0)
            kk = kostka.get(mu, 0)
            if kap != kk:
                match = False
                print(f"     MISMATCH at mu={mu}: kappa={kap}, K_Kostka={kk}")
        print(f"  MATCH? {match}")

    print("\n" + "=" * 78)
    print("STEP 5: The DEFINITIVE test — is S_j == (e_2^*)^j?")
    print("        Attack B's kappa_mu are supported on partitions of 2j with")
    print("        at most 3 parts and first part <= j.  This is EXACTLY the")
    print("        Pieri-rule support for iterated multiplication by e_2, not h_2.")
    print("        So conjecture: S_j = (e_2^*)^j where e_2^* = s^*_{(1,1)}.")
    print("=" * 78)

    e2_star = factorial_schur((1, 1, 0), xs)
    e2_ord = u_var * y_var + u_var * c + y_var * c
    print(f"e_2^*(u,y,c) = {expand(e2_star)}")
    print(f"e_2(u,y,c)   = {expand(e2_ord)}")
    print(f"e_2^* - e_2  = {expand(e2_star - e2_ord)}")

    for jj in range(J + 1):
        S_j = S_of_uyc(jj, tables)
        e2j = expand(e2_star ** jj)
        diff = expand(S_j - e2j)
        equal = (diff == 0)
        print(f"  j={jj}: S_j == (e_2^*)^j?  {equal}")
        if not equal:
            # try constant multiple / lower order
            try:
                q, r = sp.div(Poly(S_j, u_var, y_var, c),
                              Poly(e2j, u_var, y_var, c))
                if r.as_expr() == 0:
                    print(f"    S_j / (e_2^*)^j = {q.as_expr()}")
                else:
                    print(f"    diff = {diff}")
            except Exception:
                print(f"    diff = {diff}")

    print("\n" + "=" * 78)
    print("STEP 6: Compare kappa_mu to ordinary Schur expansion of (e_2)^j.")
    print("        (e_2)^j = sum_mu K_{mu', (2^j)} s_mu  (transpose Kostka).")
    print("=" * 78)

    def ord_schur(mu, xs):
        n = 3
        rows = [[xs[i]**(mu[col] + n - 1 - col) for col in range(n)]
                for i in range(n)]
        num = det3(rows)
        V = V_uyc(xs)
        vars_ = list(xs)
        q, r = sp.div(Poly(num, *vars_), Poly(V, *vars_))
        assert r.as_expr() == 0
        return q.as_expr()

    for jj in range(J + 1):
        e2j = expand(e2_ord ** jj)
        # Expand in Schurs by leading-monomial peel.
        F = e2j
        expansion = {}
        while True:
            F = expand(F)
            if F == 0:
                break
            P = Poly(F, *xs)
            if P.total_degree() < 0:
                break
            leading = sorted(P.terms(), reverse=True)[0]
            monom, cf = leading
            mu = tuple(monom)
            if not (mu[0] >= mu[1] >= mu[2]):
                print(f"    !! non-partition leading monomial {mu} coef {cf}")
                break
            s_mu = ord_schur(mu, xs)
            expansion[mu] = cf
            F = expand(F - cf * s_mu)

        print(f"\n  j = {jj}: ordinary (e_2)^j Schur expansion:")
        for mu, k in sorted(expansion.items(), reverse=True):
            print(f"     mu={mu}: coef = {k}")
        print(f"  Attack B's kappa_mu:")
        for mu, k in tables[jj]:
            print(f"     mu={mu}: kap = {k}")

        match = True
        all_mus = set(expansion.keys()) | set(mu for mu, _ in tables[jj])
        for mu in sorted(all_mus, reverse=True):
            kap = dict(tables[jj]).get(mu, 0)
            kk = expansion.get(mu, 0)
            if kap != kk:
                match = False
                print(f"     MISMATCH mu={mu}: kap={kap}, K'={kk}")
        print(f"  MATCH? {match}")

    print("\n" + "=" * 78)
    print("STEP 7: Top-degree comparison.  s^*_mu = s_mu + lower.  So")
    print("        LeadingDeg(S_j) = sum_mu kap_mu s_mu = (e_2)^j.")
    print("        Verify: top-degree-2j part of S_j equals (e_2)^j.")
    print("=" * 78)
    for jj in range(J + 1):
        S_j = S_of_uyc(jj, tables)
        e2j_ord = expand(e2_ord ** jj)
        # Get top-degree part of S_j (degree 2j).
        top = Integer(0)
        P = Poly(S_j, u_var, y_var, c) if S_j != 0 else None
        if P is not None:
            for m, cf in P.terms():
                if sum(m) == 2 * jj:
                    top += cf * u_var**m[0] * y_var**m[1] * c**m[2]
        top = expand(top)
        equal = (expand(top - e2j_ord) == 0)
        print(f"  j={jj}: top-degree {2*jj} of S_j == (e_2)^j?  {equal}")
        if not equal:
            print(f"    top(S_j) = {top}")
            print(f"    (e_2)^j  = {e2j_ord}")

    print("\n" + "=" * 78)
    print("STEP 8: For deg_pi bound: use e-basis wdeg with wdeg(e_1)=1, wdeg(e_2)=2,")
    print("        wdeg(e_3)=2 (Attack B's structural claim in step 7 of its output).")
    print("        Since sum kap_mu s_mu = e_2^j, and e_2^j has e-degree j in e_2,")
    print("        the structural bound is:")
    print("        S_j is 'e_2^j + lower shifted corrections' in e-basis.")
    print("=" * 78)


if __name__ == "__main__":
    main()
