"""Fit P_j as a polynomial in j (with (b,c) as symbols) — hoping to find a
closed form for A_1.

Working hypothesis: A_1(b, c, j) = (b+c-2)^{↓(j-2)} * P_j(b, c)
where P_j is (b,c)-polynomial of joint degree 3, with coefficients that are
polynomial in j.
"""

import time
from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, factor, expand, Poly, Integer, Rational, cancel, simplify

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


def P_j_at(jj, dsV_cache):
    A1 = extract_A_p(jj, 1, dsV_cache)
    L = jj - 2
    div = Integer(1)
    for i in range(L):
        div *= (b + c - 2 - i)
    if L == 0:
        return A1
    q, r = sp.div(Poly(A1, b, c), Poly(div, b, c))
    assert r.as_expr() == 0
    return q.as_expr()


def main():
    J = 10
    print(f"Building tables up to j = {J}...")
    tables = bt(J)
    print("Computing ds_j/V...")
    dsV_cache = dsV_all(J, tables)

    # Extract P_j for j = 2..J. Each P_j is a (b,c)-polynomial. Get its
    # (b,c)-monomial expansion, and fit each coefficient as a polynomial in j.
    print("\n" + "=" * 72)
    print(f"Extract P_j(b,c) for j = 2..{J}")
    print("=" * 72)
    Pjs = {}
    for jj in range(2, J + 1):
        Pjs[jj] = expand(P_j_at(jj, dsV_cache))
        print(f"  P_{jj} = {Pjs[jj]}")

    # Also include j = 1: A_1 = b*c + b + 2*c, doesn't have (b+c-2)^↓(j-2) prefactor
    # for j = 1 that prefactor is (b+c-2)^{↓-1} which is 1/(b+c-1)... so P_1 formula
    # may or may not extend. Skip j = 1 for now.

    # Collect all (b, c)-monomials appearing.
    all_bc_slots = set()
    for jj in Pjs:
        pab = Poly(Pjs[jj], b, c)
        for (db, dc), cf in pab.terms():
            all_bc_slots.add((db, dc))

    all_bc_slots = sorted(all_bc_slots)
    print(f"\n  (b,c)-slots appearing in P_j: {all_bc_slots}")

    # For each slot, get coefficient as function of j.
    print("\n" + "=" * 72)
    print("Fit each (b,c)-coefficient of P_j as a polynomial in j")
    print("=" * 72)
    fit_report = {}
    for slot in all_bc_slots:
        db, dc = slot
        samples = []
        for jj in sorted(Pjs.keys()):
            pab = Poly(Pjs[jj], b, c)
            cf = Integer(0)
            for (db2, dc2), c_ in pab.terms():
                if (db2, dc2) == slot:
                    cf = c_
                    break
            samples.append((jj, cf))
        # Fit polynomial in j.
        n = len(samples)
        # Try degrees 0, 1, 2, ...
        fit_poly = None
        fit_deg = None
        for D in range(n):
            rows = []
            yy = []
            for (jv, yv) in samples[:D + 1]:
                rows.append([jv ** i for i in range(D + 1)])
                yy.append(yv)
            M = sp.Matrix(rows)
            y = sp.Matrix(yy)
            try:
                sol = M.solve(y)
            except Exception:
                continue
            ok = True
            for (jv, yv) in samples[D + 1:]:
                pred = sum(sol[i] * jv ** i for i in range(D + 1))
                if sp.simplify(pred - yv) != 0:
                    ok = False
                    break
            if ok:
                fit_deg = D
                fit_poly = sum(sol[i] * j_sym ** i for i in range(D + 1))
                if D > 0 and sp.simplify(sol[D]) == 0:
                    continue
                break
        fit_report[slot] = (fit_deg, fit_poly, samples)
        print(f"  slot b^{db} c^{dc}: j-degree = {fit_deg},  coeff(j) = {sp.expand(fit_poly)}")

    # Assemble closed form for P_j
    print("\n" + "=" * 72)
    print("Assembled closed form P_j(b, c, j)")
    print("=" * 72)
    Pj_closed = Integer(0)
    for slot, (fd, fp, _) in fit_report.items():
        db, dc = slot
        Pj_closed += fp * b**db * c**dc
    Pj_closed = expand(Pj_closed)
    print(f"  P_j(b,c,j) = {Pj_closed}")
    print(f"  Factored:   {sp.factor(Pj_closed)}")

    # Cross-check with actual values.
    for jj in sorted(Pjs.keys()):
        pred = Pj_closed.subs(j_sym, jj)
        actual = Pjs[jj]
        diff = sp.simplify(pred - actual)
        print(f"    j = {jj}: closed = actual? {diff == 0}")

    # Now, assemble the CLOSED FORM for A_1(b, c, j) = (b+c-2)^{↓(j-2)} * P_j.
    # (b+c-2)^{↓(j-2)} = (b+c-2)(b+c-3)...(b+c-j+1), which for j = 1 has
    # length -1 (interpret as 1/(b+c-1)) and for j = 2 has length 0 (= 1).
    #
    # This closed form only holds for j >= 2. For j = 1, A_1(b, c, 1) = b*c + b + 2*c
    # separately.

    # Let's next reformulate the divisibility we need.
    #
    # We want: (b+2)_{c-1-j} * A_1(b, c, j) = (b+2)_{c-3} * R_1(b, c, j).
    # Substituting A_1 = (b+c-2)^{↓(j-2)} * P_j:
    #   (b+2)_{c-1-j} * (b+c-2)^{↓(j-2)} * P_j = (b+2)_{c-3} * R_1.
    # We can rewrite (b+c-2)^{↓(j-2)} = (b+c-j+1)(b+c-j+2)...(b+c-2).
    # These are the shifts a+r for r = c-j+1, ..., c-2, so in Pochhammer
    # form: (b+c-j+1)^{↑(j-2)} which is (b+ (c-j+1))_{j-2} in rising Pochhammer.
    # And (b+2)_{c-1-j} = (b+2)(b+3)...(b+c-j). This is the product over the
    # segment 2 <= r <= c-j-1... let me re-derive.
    #
    # (b+2)_{L} = (b+2)(b+3)...(b+L+1) [L factors, rising Pochhammer].
    # So (b+2)_{c-1-j} = (b+2)(b+3)...(b+c-j) [factors b+2 through b+c-j].
    # (b+c-2)^{↓(j-2)} = (b+c-2)(b+c-3)...(b+c-j+1) [factors b+c-j+1 through b+c-2].
    #
    # Concatenating in ORDER: (b+2)(b+3)...(b+c-j) then (b+c-j+1)...(b+c-2).
    # This equals (b+2)(b+3)...(b+c-2) = (b+2)_{c-3}.  !!!
    #
    # So (b+2)_{c-1-j} * (b+c-2)^{↓(j-2)} = (b+2)_{c-3}.
    #
    # Therefore Q_j(b) * A_1(b, c, j) = (b+2)_{c-3} * P_j(b, c, j)
    # DIRECTLY, with R_1 = P_j.
    #
    # And P_j has j-degree (per b-slot) BY OUR FIT above.
    #
    # This is exactly the (⋆⋆-a'')_{p=1} bound. Provided we can prove:
    #   (I) A_1(b, c, j) = (b+c-2)^{↓(j-2)} * P_j(b, c, j),  [closed form]
    #   (II) P_j(b, c, j) is polynomial in j of (b-slot) degree <= 2.
    #
    # Both follow from the closed form P_j = <the fit above>.
    print("\n" + "=" * 72)
    print("CORE CLAIM: (b+2)_{c-1-j} * (b+c-2)^{↓(j-2)} = (b+2)_{c-3}")
    print("=" * 72)
    for cv in [8, 12, 15, 20]:
        for jv in range(1, min(cv - 2, 8)):
            lhs = Integer(1)
            for i in range(cv - 1 - jv):
                lhs *= (b + 2 + i)
            if jv - 2 >= 0:
                for i in range(jv - 2):
                    lhs *= (b + cv - 2 - i)
            rhs = Integer(1)
            for i in range(cv - 3):
                rhs *= (b + 2 + i)
            eq = sp.simplify(lhs - rhs)
            status = "OK" if eq == 0 else f"!!MISMATCH! {eq}"
            print(f"  c={cv}, j={jv}: {status}")
            if eq != 0:
                break

    # Report per-b-slot j-degree of P_j (which becomes R_1)
    print("\n" + "=" * 72)
    print("R_1(b, c, j) = P_j(b, c, j): per-b-slot j-degrees (grouped over c)")
    print("=" * 72)
    b_slot_jd = {}
    for slot, (fd, fp, _) in fit_report.items():
        db, dc = slot
        if db not in b_slot_jd or fd > b_slot_jd[db]:
            b_slot_jd[db] = fd
    for db in sorted(b_slot_jd.keys()):
        print(f"  b^{db}: max j-degree over c-slots = {b_slot_jd[db]}")
    max_over_all = max(b_slot_jd.values()) if b_slot_jd else -1
    print(f"\n  Overall max per-b-slot j-degree = {max_over_all}")
    print(f"  Claim (⋆⋆-a''_{{p=1}}): expect <= 2.  {'PASS' if max_over_all <= 2 else 'FAIL'}")


if __name__ == "__main__":
    main()
