"""Interpolation-style proof strategy for A_1 closed form.

The closed form claim:
  A_1(b, c, j) = (b+c-2)^{↓(j-2)} * P_j(b, c, j)   for integer j >= 2,
where P_j(b, c, j) = (j/2) * [(b+c)(2bc + 3b + 5c - 3) - j*(b² + 4bc + c² - b + c)].

STRATEGY: What we need to show, for each fixed b and c symbolic, is that
BOTH sides are polynomials in j (of some degree D) and match at D+1 values.

Note: RHS is manifestly a polynomial in j of degree (j-2) + 2 = j... but that's
NOT a fixed-degree polynomial in j. The claim doesn't make sense as a polynomial
identity in j at fixed (b, c) because both sides are polynomials in j WHOSE
DEGREE DEPENDS ON j (i.e., they're not polynomial in j at all — the number of
factors depends on j).

HMMMM. Let's think again.

Actually per-b-slot per-c-slot analysis is fine. Fix a specific (b^u, c^v) slot.
Then LHS coefficient is [b^u c^v] A_1(b, c, j), viewed as function of j.
And RHS coefficient is [b^u c^v] ((b+c-2)^↓{j-2} * P_j).

Since (b+c-2)^↓{j-2} = prod_{k=0}^{j-3} (b + c - 2 - k), for j >= 2, this is a
polynomial in (b, c) of TOTAL degree j - 2 (and each factor is linear in (b,c)).

Then [b^u c^v] of this product * P_j: since P_j has total (b,c)-degree 3,
we get contributions to slot (b^u c^v) with u + v <= (j - 2) + 3 = j + 1.
Sum b-deg = j... hmm.

Let me try a different lens. Consider the CHANGE-of-basis: write A_1 as a
formal sum in monomials (b+c)^{↓k} * (elementary polys) — the "hypergeometric"
basis.

Actually the CLEANEST way: I can VERIFY the closed form for j = 1, 2, ..., 20
which is enough to conjecture it, then prove it by an inductive-in-j argument.

Better: derive it from the shifted-Schur structure directly. Let me try.

The claim:
  [a^{j-1}] S_j(a, b, c) = (b+c-2)^{↓(j-2)} * P_j(b, c, j)

where S_j = sum_{mu in S_j} kappa_mu * s*_mu(a+2, b+1, c).

s*_mu is a shifted-Schur function. Its (a, b, c)-expansion satisfies certain
recursions.
"""

# Instead of a full proof, let's write out what we know and check the closed
# form matches ALL the way up to j = 15 for further empirical confidence.

import time
from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, Rational

a, b, c, j_sym = symbols('a b c j')
x1, x2, x3 = a + 2, b + 1, c


def fall(x, m):
    p = Integer(1)
    for i in range(m):
        p *= (x - i)
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


def ds_symbolic(jj, tables):
    xs = (x1, x2, x3)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def dsV_all(J, tables):
    V = ds_symbolic(0, tables)
    cache = {}
    for jj in range(J + 1):
        dsj = ds_symbolic(jj, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0
        cache[jj] = q.as_expr()
    return cache


def extract_A_p(jj, p, dsV_cache):
    S = dsV_cache[jj]
    if jj - p < 0:
        return Integer(0)
    pab = Poly(S, a, b, c)
    result = Integer(0)
    for monom, cf in pab.terms():
        da, db, dc = monom
        if da == jj - p:
            result += cf * b**db * c**dc
    return expand(result)


def A1_closed(jj):
    """Closed form for A_1(b, c, j) at fixed integer j."""
    prefactor = Integer(1)
    for k in range(jj - 2):
        prefactor *= (b + c - 2 - k)
    Pj = (Rational(1, 2) * jj * (
        2*b**2*c - b**2*jj + 3*b**2
        + 2*b*c**2 - 4*b*c*jj + 8*b*c + b*jj - 3*b
        - c**2*jj + 5*c**2 - c*jj - 3*c
    ))
    if jj == 1:
        # special: (b+c-2)^{↓-1} means 1/(b+c-1). closed form yields P_1/(b+c-1).
        return sp.cancel(Pj / (b + c - 1))
    return expand(prefactor * Pj)


def main():
    J = 15
    print(f"Building tables to j = {J}...")
    t0 = time.time()
    tables = bt(J)
    print(f"  {time.time() - t0:.1f}s")
    print(f"Computing ds_j/V symbolically...")
    dsV_cache = dsV_all(J, tables)
    print(f"  {time.time() - t0:.1f}s total")

    print("\n" + "=" * 72)
    print(f"Verify A_1 closed form for j = 1..{J}")
    print("=" * 72)
    all_ok = True
    for jj in range(1, J + 1):
        actual = extract_A_p(jj, 1, dsV_cache)
        pred = A1_closed(jj)
        diff = expand(actual - pred)
        status = "OK" if diff == 0 else f"!! DIFF={diff}"
        print(f"  j = {jj}: {status}")
        if diff != 0:
            all_ok = False
    print(f"\n {'PASS' if all_ok else 'FAIL'}")


if __name__ == "__main__":
    main()
