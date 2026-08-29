"""Analyze per-mu structure of A_1 = [a^{j-1}] S_j.

We know S_j = sum_{mu in S_j} kappa_mu * s*_mu(a+2, b+1, c).
The top-a coefficient [a^{j}] S_j = A_0 comes only from mu with mu_1 = j
(this gives the (b+c)^{↓j} formula via shifted-Schur combinatorics).

For [a^{j-1}] S_j = A_1, contributions come from:
  (i)  partitions with mu_1 = j (contributing the [a^{j-1}] of their s*_mu);
  (ii) partitions with mu_1 = j - 1 (contributing the [a^{j-1}] = top of theirs).

Let's identify these two subsets of S_j:
  In S_j, mu_1 <= j always (Lemma 1 claim).
  Partitions with mu_1 = j: these are (j, mu_2, mu_3) where the walk always
    adds a cell to row 1. Since we start at empty and do j vertical 2-strips
    each adding at most 1 cell to row 1, and mu_1 = j means EVERY strip added
    to row 1, then the OTHER cell of each 2-strip went to either row 2 or row 3.
    So mu_2 + mu_3 = j, with (mu_2, mu_3) counting the number of times we
    "went to row 2" or "went to row 3" over j steps.
  Partitions with mu_1 = j - 1: exactly one strip did NOT add to row 1;
    that strip added cells to (row 2, row 3). The other j - 1 strips added
    to row 1 and either row 2 or row 3.
"""

import time
from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, Rational

a, b, c = symbols('a b c')
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


def V_of():
    return (a - b + 1) * (a - c + 2) * (b - c + 1)


def s_star_mu(mu):
    """Compute s*_mu(a+2, b+1, c) = det[(y_i)_↓ mu_j+3-j] / V."""
    V = V_of()
    xs = (x1, x2, x3)
    ks = [mu[col] + (2 - col) for col in range(3)]
    rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
    d = expand(det3(rows))
    q, r = sp.div(Poly(d, [a, b, c]), Poly(V, [a, b, c]))
    assert r.as_expr() == 0
    return q.as_expr()


def a_coef(expr, ap):
    """Extract [a^ap] of a polynomial in (a, b, c) as poly in (b, c)."""
    pabc = Poly(expr, a, b, c)
    result = Integer(0)
    for monom, cf in pabc.terms():
        da, db, dc = monom
        if da == ap:
            result += cf * b**db * c**dc
    return expand(result)


def kappa_check_all(J):
    """List partitions in S_j and their kappa values."""
    T = bt(J)
    for jj in range(J + 1):
        print(f"\n j = {jj}: partitions in S_j:")
        for mu, kap in T[jj]:
            print(f"    mu = {mu}: kappa = {kap}")


def main():
    J = 8
    print("Building tables...")
    T = bt(J)

    print("\nList mu with mu_1 = j (i.e., top-row-maxed):")
    for jj in range(1, J + 1):
        print(f"\n j = {jj}:")
        for mu, kap in T[jj]:
            if mu[0] == jj:
                print(f"    mu = {mu}: kappa = {kap}")

    print("\nList mu with mu_1 = j - 1:")
    for jj in range(1, J + 1):
        print(f"\n j = {jj}:")
        for mu, kap in T[jj]:
            if mu[0] == jj - 1:
                print(f"    mu = {mu}: kappa = {kap}")

    # For j = 1..5, compute contribution of each subset:
    print("\n" + "=" * 72)
    print("Contribution split: A_1_top (from mu_1 = j) vs A_1_next (from mu_1 = j-1)")
    print("=" * 72)
    for jj in range(1, 6):
        # Contribution from mu_1 = j
        top_ctb = Integer(0)
        next_ctb = Integer(0)
        for mu, kap in T[jj]:
            if mu[0] == jj:
                s_mu = s_star_mu(mu)
                contrib = kap * a_coef(s_mu, jj - 1)
                top_ctb += contrib
            elif mu[0] == jj - 1:
                s_mu = s_star_mu(mu)
                # [a^{j-1}] of s*_mu with mu_1 = j-1 = top-a coefficient of s*_mu
                contrib = kap * a_coef(s_mu, jj - 1)
                next_ctb += contrib
        print(f"\n  j = {jj}:")
        print(f"    from mu_1 = j:   {expand(top_ctb)}")
        print(f"    from mu_1 = j-1: {expand(next_ctb)}")
        total = expand(top_ctb + next_ctb)
        print(f"    total = {factor(total)}")

    # Now, focus on mu with mu_1 = j. These have the shape (j, mu_2, mu_3) with
    # mu_2 + mu_3 = j (since |mu| = 2j).
    # kappa_mu counts vertical-2-strip walks from empty to (j, mu_2, mu_3) where
    # every strip adds one cell to row 1.
    # If mu_2 + mu_3 = j and mu_1 = j:
    #   at each step, we're adding (1, ?, ?) where the second ? is in row 2 or row 3.
    # But it's a vertical 2-strip: exactly two cells, all in distinct rows.
    # So at each step we add one to row 1 and one to either row 2 or row 3.
    # If we do this k_2 times to row 2 and k_3 = j - k_2 times to row 3, then
    # mu_2 must equal k_2 and mu_3 must equal k_3.
    # BUT: for it to be a valid Young diagram at every step, we need column
    # constraints. Specifically, cells added to row 3 must be in columns <= mu_2 at
    # that time.
    # Actually: the additions to row 2 happen at positions (2, 1), (2, 2), ..., (2, k_2)
    # in order. Additions to row 3 happen at positions (3, 1), ..., (3, k_3). For
    # each step, we need the current shape after addition to be a valid partition.
    # Since row 3 is added at column-position <= current row 2, we need at every step
    # (current row 3) <= (current row 2). So we need at every step to have added
    # more to row 2 than to row 3 (weakly). This is a lattice-path constraint.
    #
    # Number of walks = number of lattice paths (with steps R2 or R3) of length j
    # such that #R2 = mu_2, #R3 = mu_3, and at every prefix #R2 >= #R3.
    # This is Catalan-type! It's the number of ballot sequences, given by
    # binomial(j, mu_3) * (mu_2 - mu_3 + 1) / (mu_2 + 1) (ballot number).
    #
    # Or equivalently: (j)! / (mu_2! mu_3!) * (mu_2 - mu_3 + 1) / (mu_2 + 1)
    #                = C(j, mu_3) * (mu_2 + 1 - mu_3) / (mu_2 + 1).
    #
    # Let's verify from the kappa output above.
    print("\n" + "=" * 72)
    print("Verify kappa for mu_1 = j is ballot number")
    print("=" * 72)
    from math import comb
    for jj in range(1, J + 1):
        for mu, kap in T[jj]:
            if mu[0] == jj:
                mu2, mu3 = mu[1], mu[2]
                # Ballot number: C(j, mu3) * (mu2 - mu3 + 1) / (mu2 + 1)
                if mu2 + 1 == 0:
                    ballot = "N/A"
                else:
                    ballot = comb(jj, mu3) * (mu2 - mu3 + 1) // (mu2 + 1)
                    # But we need mu2 - mu3 + 1 > 0 (else no walk).
                match = "MATCH" if kap == ballot else "MISMATCH"
                print(f"    j={jj}, mu={mu}: kappa={kap}, ballot={ballot}  [{match}]")


if __name__ == "__main__":
    main()
