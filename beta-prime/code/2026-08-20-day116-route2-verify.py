"""Day 116 — Route 2: Partition-point interpolation for deg_pi A_p <= p.

We attempt to CLOSE the atomic gap (C) using the (u, y, c) symmetric structure
of S_j (Attack B's key discovery) plus a clean [u^{j-p}] extraction argument.

Setup recap:
    u := a + 2,  y := b + 1
    S_j is S_3-symmetric in (u, y, c)  ==>  S_j in Q[e_1, e_2, e_3]
    e_1 = u + y + c = u + sigma
    e_2 = uy + uc + yc = u*sigma + pi   (where pi := yc, sigma := y + c)
    e_3 = uyc = u*pi

Empirical bound (Attack B step 7, j <= 6):
    S_j = sum_{i_1+i_2+2 i_3 <= j} c_{i_1,i_2,i_3}(j) e_1^{i_1} e_2^{i_2} e_3^{i_3}     (StructB)

CENTRAL OBSERVATION for Route 2. Expand:
    e_1^{i_1} e_2^{i_2} e_3^{i_3}
    = (u + sigma)^{i_1} (u sigma + pi)^{i_2} (u pi)^{i_3}
    = u^{i_3} pi^{i_3} * sum_{alpha, beta}
         C(i_1, alpha) C(i_2, beta)
         u^{alpha+beta} sigma^{i_1-alpha+beta} pi^{i_2-beta}
    = sum_{alpha, beta} C(i_1, alpha) C(i_2, beta)
         u^{alpha+beta+i_3} sigma^{i_1-alpha+beta} pi^{i_2-beta+i_3}

Each such monomial has (u-deg, pi-deg, sigma-deg) = (alpha+beta+i_3, i_2-beta+i_3, i_1-alpha+beta).

CLAIM: (StructB) implies, for every monomial arising in the (u, pi, sigma) expansion of S_j,
    (u-deg) + (pi-deg) <= j.

Proof: (u-deg) + (pi-deg) = (alpha + beta + i_3) + (i_2 - beta + i_3) = alpha + i_2 + 2 i_3
                          <= i_1 + i_2 + 2 i_3 <= j.

Now u = a + 2, so extracting [a^{j-p}] from S_j = P(u, pi, sigma) is equivalent to
extracting [a^{j-p}] from P(a + 2, pi, sigma). For any monomial u^k pi^q sigma^d:
    [a^{j-p}] u^k = C(k, j-p) * 2^{k-(j-p)}   (nonzero iff k >= j-p).

So A_p = sum_{monomials u^k pi^q sigma^d in S_j, k >= j-p}
         C(k, j-p) 2^{k-(j-p)} pi^q sigma^d.

Every contributing monomial has k + q <= j (by StructB via the CLAIM above),
so if k >= j-p, then q <= j - k <= j - (j-p) = p.  Hence deg_pi A_p <= p.  QED.

The proof reduces (C) to (StructB): "S_j in Q[e_1, e_2, e_3] with weight
i_1 + i_2 + 2 i_3 <= j".  Structurally proving (StructB) is the remaining task.

This script:
    STEP 1: Verify (StructB) empirically for j <= J_MAX (extend Attack B to J=8).
    STEP 2: Verify the KEY CLAIM above per-monomial: every monomial in e_1^i1 e_2^i2 e_3^i3
            has (u-deg) + (pi-deg) <= i_1 + i_2 + 2 i_3.
    STEP 3: Verify the extraction preserves the bound: [a^{j-p}] applied to
            S_j = sum c_{i} e_1^i1 e_2^i2 e_3^i3 yields A_p with deg_pi <= p.
    STEP 4: Double-check by extracting A_p directly and computing deg_pi.
    STEP 5: Investigate the STRUCTURAL bound (StructB) via ds_j formula.
            Try recursion on j via horizontal 2-strips.

If all four checks pass, we have a CONDITIONAL proof of (C) modulo (StructB).
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product

import sympy as sp
from sympy import binomial, expand, Integer, Poly, symbols

# ---------------------------------------------------------------------------
# Symbolic variables
# ---------------------------------------------------------------------------
a, b, c = symbols('a b c')
u_var, y_var = symbols('u y')
sig, pi_v = symbols('sigma pi')
e1_v, e2_v, e3_v = symbols('e1 e2 e3')

u_expr = a + 2

# ---------------------------------------------------------------------------
# Building blocks (borrowed from attackB script)
# ---------------------------------------------------------------------------


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
    """2-strip lattice building; returns dict jj -> list of (mu (padded to len 3), kappa)."""
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


def ds_symbolic_in_abc(jj, tables):
    xs = (u_expr, b + 1, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def V_of_abc():
    return (a - b + 1) * (a - c + 2) * (b - c + 1)


def S_in_abc(jj, tables):
    dsj = ds_symbolic_in_abc(jj, tables)
    V = V_of_abc()
    q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
    assert r.as_expr() == 0
    return q.as_expr()


def S_in_uyc(jj, tables):
    xs = (u_var, y_var, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    V_uyc = (u_var - y_var) * (u_var - c) * (y_var - c)
    q, r = sp.div(Poly(total, u_var, y_var, c), Poly(V_uyc, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def to_elem_uyc(F):
    """Rewrite a symmetric polynomial F(u_var, y_var, c) in (e1_v, e2_v, e3_v)."""
    F = expand(F)
    result = Integer(0)
    while True:
        F = expand(F)
        P = Poly(F, u_var, y_var, c)
        if P.total_degree() < 0 or P.as_expr() == 0:
            break
        terms = sorted(P.terms(), reverse=True)
        (dm, cf) = terms[0]
        du, dy, dc = dm
        if not (du >= dy >= dc):
            return None
        result += cf * e1_v ** (du - dy) * e2_v ** (dy - dc) * e3_v ** dc
        sub = cf * (u_var + y_var + c) ** (du - dy) * (
            u_var * y_var + u_var * c + y_var * c) ** (dy - dc) * (
            u_var * y_var * c) ** dc
        F = expand(F - sub)
    return result


# ---------------------------------------------------------------------------
# STEP 1: Verify (StructB) empirically for j <= J_MAX.
# ---------------------------------------------------------------------------

def step1_verify_structB(tables, J_MAX):
    print("=" * 78)
    print("STEP 1: Verify (StructB): S_j = sum c_{i1,i2,i3} e_1^i1 e_2^i2 e_3^i3")
    print("        with i_1 + i_2 + 2 i_3 <= j.  Extend Attack B check to J_MAX.")
    print("=" * 78)
    ok_all = True
    for jj in range(J_MAX + 1):
        S_uyc = S_in_uyc(jj, tables)
        # Symmetry sanity checks
        sym1 = sp.simplify(S_uyc - S_uyc.subs(
            [(u_var, y_var), (y_var, u_var)], simultaneous=True))
        sym2 = sp.simplify(S_uyc - S_uyc.subs(
            [(u_var, c), (c, u_var)], simultaneous=True))
        assert sym1 == 0 and sym2 == 0, f"j={jj}: S_j not symmetric in u,y,c"
        S_elem = to_elem_uyc(S_uyc)
        P = Poly(S_elem, e1_v, e2_v, e3_v)
        max_w = -1
        violators = []
        for m, cf in P.terms():
            if cf == 0:
                continue
            i1, i2, i3 = m
            w = i1 + i2 + 2 * i3
            if w > max_w:
                max_w = w
            if w > jj:
                violators.append((i1, i2, i3, cf))
        ok = (max_w <= jj) and not violators
        print(f"  j={jj}: #terms={len(P.terms())}, max wdeg(1,1,2) = {max_w}"
              f"  [<= {jj}  {'OK' if ok else 'FAIL'}]"
              f"{'  violators: ' + str(violators) if violators else ''}")
        if not ok:
            ok_all = False
    print(f"\nSTEP 1 status: {'PASS' if ok_all else 'FAIL'}\n")
    return ok_all


# ---------------------------------------------------------------------------
# STEP 2: Per-monomial claim in the (u, pi, sigma) expansion of e_1^i1 e_2^i2 e_3^i3.
# ---------------------------------------------------------------------------

def step2_check_e_expansion_bound(I_MAX):
    print("=" * 78)
    print("STEP 2: Verify per-monomial claim:")
    print("        expanding e_1^i1 e_2^i2 e_3^i3 in (u, pi, sigma),")
    print("        every monomial has (u-deg) + (pi-deg) <= i_1 + i_2 + 2 i_3.")
    print("=" * 78)
    # e_1 = u + sigma
    # e_2 = u*sigma + pi
    # e_3 = u*pi
    u_var2 = symbols('U')
    prod = None
    all_ok = True
    for i1, i2, i3 in product(range(I_MAX + 1), repeat=3):
        if i1 + i2 + 2 * i3 > I_MAX + 3:
            continue  # keep it tractable
        expr = (u_var2 + sig) ** i1 * (u_var2 * sig + pi_v) ** i2 * (u_var2 * pi_v) ** i3
        expr = expand(expr)
        P = Poly(expr, u_var2, pi_v, sig)
        max_upi = -1
        for m, cf in P.terms():
            if cf == 0:
                continue
            k, q, d = m
            w = k + q
            if w > max_upi:
                max_upi = w
        # Predicted bound: i_1 + i_2 + 2 i_3
        pred = i1 + i2 + 2 * i3
        ok = max_upi <= pred
        if not ok:
            all_ok = False
            print(f"  FAIL: (i1,i2,i3)=({i1},{i2},{i3}) -> max u+pi-deg = {max_upi}, "
                  f"pred <= {pred}")
    print(f"\nSTEP 2 status: {'PASS' if all_ok else 'FAIL'} (over I_MAX={I_MAX})\n")
    return all_ok


# ---------------------------------------------------------------------------
# STEP 3: [a^{j-p}] extraction preserves (u-deg) + (pi-deg) <= j filtration.
#
# Argument: on any polynomial P(u, pi, sigma), extracting [a^{j-p}] under u = a+2
# gives sum_{u^k terms in P} C(k, j-p) 2^{k-(j-p)} * (rest).
# Only monomials with k >= j-p contribute; their pi-degree is at most
# (u+pi-deg) - k <= j - (j-p) = p.  So deg_pi A_p <= p.
#
# This step verifies: for each j <= J_MAX and each p, we compute A_p in the
# "double bookkeeping" scheme (from the (StructB) expansion, extract [a^{j-p}])
# and verify deg_pi <= p.  Also compare with A_p obtained from the direct
# (a, b, c) computation.
# ---------------------------------------------------------------------------

def extract_A_p_from_S_abc(S_abc, jj, p):
    if jj - p < 0:
        return Integer(0)
    P = Poly(S_abc, a, b, c)
    r = Integer(0)
    for m, cf in P.terms():
        da, db, dc = m
        if da == jj - p:
            r += cf * b ** db * c ** dc
    return expand(r)


def to_pi_sigma(F):
    """Rewrite F(b, c) in (pi_v = (b+1)c, sig = b+c+1) if possible."""
    if F == 0:
        return Integer(0)
    z = symbols('_z_')
    Fz = expand(F.subs([(b, z - 1), (c, sig - z)]))
    Pz = sp.Poly(Fz, z)
    D = Pz.degree() if Pz.total_degree() >= 0 else 0
    coefs = [Pz.coeff_monomial(z ** i) for i in range(D + 1)]
    while len(coefs) > 2:
        top = coefs[-1]
        d = len(coefs) - 1
        if top == 0:
            coefs.pop()
            continue
        coefs[d - 1] = sp.expand(coefs[d - 1] + sig * top)
        coefs[d - 2] = sp.expand(coefs[d - 2] - pi_v * top)
        coefs.pop()
    while len(coefs) < 2:
        coefs.append(Integer(0))
    if sp.simplify(coefs[1]) != 0:
        return None
    return sp.expand(coefs[0])


def extract_A_p_via_structB(tables, jj, p):
    """Compute A_p in (pi, sigma) via the (u, pi, sigma) expansion of S_j."""
    # Recompute S_j in (u, pi, sigma) by first getting S_j in (u, y, c),
    # substituting y + c = sigma, yc = pi.
    # We use the (e1, e2, e3) expansion for cleanness:
    S_uyc = S_in_uyc(jj, tables)
    S_elem = to_elem_uyc(S_uyc)
    # substitute e1 -> u + sigma, e2 -> u sigma + pi, e3 -> u pi
    U = symbols('U')
    expr = S_elem.subs([
        (e1_v, U + sig),
        (e2_v, U * sig + pi_v),
        (e3_v, U * pi_v),
    ])
    expr = expand(expr)
    # Now substitute U -> a + 2 and extract [a^{jj-p}].
    expr_a = expand(expr.subs(U, a + 2))
    Pa = Poly(expr_a, a)
    result = Pa.coeff_monomial(a ** (jj - p))
    return expand(result)


def step3_verify_route2_argument(tables, J_MAX):
    print("=" * 78)
    print("STEP 3: [a^{j-p}] extraction from (StructB) expansion:")
    print("        verify deg_pi A_p <= p and match against direct A_p.")
    print("=" * 78)
    all_ok = True
    for jj in range(J_MAX + 1):
        S_abc = S_in_abc(jj, tables)
        for p in range(jj + 1):
            # A_p via Route 2 (extract from (u, pi, sigma) form)
            A_route2 = extract_A_p_via_structB(tables, jj, p)
            # A_p directly (from S_abc, extract a^{jj-p}, then rewrite in pi,sigma)
            A_direct = extract_A_p_from_S_abc(S_abc, jj, p)
            A_direct_ps = to_pi_sigma(A_direct) if A_direct != 0 else Integer(0)
            # Simplify and compare
            diff = sp.simplify(A_route2 - A_direct_ps)
            if diff != 0:
                print(f"  j={jj}, p={p}: A_p route2 != A_p direct !")
                print(f"    route2 = {A_route2}")
                print(f"    direct = {A_direct_ps}")
                all_ok = False
                continue
            # Check deg_pi
            if A_route2 == 0:
                deg_pi = -1
            else:
                Pp = Poly(A_route2, pi_v, sig)
                deg_pi = -1
                for m, cf in Pp.terms():
                    if cf == 0:
                        continue
                    k, d = m
                    if k > deg_pi:
                        deg_pi = k
            ok = deg_pi <= p
            if not ok:
                all_ok = False
            print(f"  j={jj}, p={p}: A_p matches direct? YES, deg_pi = {deg_pi} "
                  f"[<= {p}  {'OK' if ok else 'FAIL'}]")
    print(f"\nSTEP 3 status: {'PASS' if all_ok else 'FAIL'}\n")
    return all_ok


# ---------------------------------------------------------------------------
# STEP 4: Sanity of the coefficient-level derivation.
# For each (i1, i2, i3) with i1+i2+2 i3 <= j, extract [a^{j-p}] of
# (a+2+sigma)^i1 (a+2)*sigma+pi)^i2 ((a+2) pi)^i3, and confirm deg_pi <= p.
# ---------------------------------------------------------------------------

def step4_check_extraction_per_e_monomial(J_MAX):
    print("=" * 78)
    print("STEP 4: For each (i1, i2, i3) with i1+i2+2 i3 <= j <= J_MAX, and each p:")
    print("        [a^{j-p}] of e1^i1 e2^i2 e3^i3 (with e_k in (a, pi, sigma)) has")
    print("        deg_pi <= p.")
    print("=" * 78)
    all_ok = True
    for jj in range(J_MAX + 1):
        for i1, i2, i3 in product(range(jj + 1), repeat=3):
            if i1 + i2 + 2 * i3 > jj:
                continue
            expr = (a + 2 + sig) ** i1 * ((a + 2) * sig + pi_v) ** i2 * ((a + 2) * pi_v) ** i3
            expr = expand(expr)
            Pe = Poly(expr, a)
            for p in range(jj + 1):
                if jj - p < 0:
                    continue
                cf = Pe.coeff_monomial(a ** (jj - p))
                if cf == 0:
                    continue
                Pcf = Poly(expand(cf), pi_v, sig)
                deg_pi = -1
                for m, coef in Pcf.terms():
                    if coef == 0:
                        continue
                    k, d = m
                    if k > deg_pi:
                        deg_pi = k
                if deg_pi > p:
                    all_ok = False
                    print(f"  FAIL: j={jj}, (i1,i2,i3)=({i1},{i2},{i3}), p={p}: "
                          f"deg_pi = {deg_pi} > {p}")
    print(f"\nSTEP 4 status: {'PASS' if all_ok else 'FAIL'}\n")
    return all_ok


# ---------------------------------------------------------------------------
# STEP 5: Investigate (StructB) structural proof strategy: check the coefficient
# table pattern; and test whether S_j satisfies a recursion.
# ---------------------------------------------------------------------------

def step5_explore_structB(tables, J_MAX):
    print("=" * 78)
    print("STEP 5: (StructB) structural exploration — print e-basis coefficient tables.")
    print("        Look for patterns / recursion in j.")
    print("=" * 78)
    tables_e = {}
    for jj in range(J_MAX + 1):
        S_uyc = S_in_uyc(jj, tables)
        S_elem = to_elem_uyc(S_uyc)
        P = Poly(S_elem, e1_v, e2_v, e3_v)
        d = {}
        for m, cf in P.terms():
            if cf == 0:
                continue
            i1, i2, i3 = m
            d[(i1, i2, i3)] = cf
        tables_e[jj] = d
        print(f"\n  j = {jj}:  (i1, i2, i3) -> c_{{...}}(j)   [wdeg = i1+i2+2 i3]")
        for k in sorted(d.keys(), key=lambda t: (-(t[0] + t[1] + 2 * t[2]),
                                                 -t[0], -t[1], -t[2])):
            i1, i2, i3 = k
            w = i1 + i2 + 2 * i3
            print(f"    ({i1}, {i2}, {i3})  w={w}:  {d[k]}")
    # A test: check whether "leading in wdeg" coefficient at wdeg = j
    # has a nice closed form (e.g., (-1)^j j! * (i1=j) coefficient).
    print("\n  Leading e_1^j coefficient of S_j:")
    for jj in range(J_MAX + 1):
        d = tables_e[jj]
        lc = d.get((jj, 0, 0), 0)
        print(f"    j={jj}: c_{{{jj},0,0}} = {lc}")


# ---------------------------------------------------------------------------
# STEP 6: Attempt structural proof of (StructB) via recursion on j.
# S_{j} arises from ds_j / V.  Under the u,y,c presentation, ds_j is
# alt-symmetric (a determinant), so ds_j = V * S_j with S_j symmetric.
# Try: S_{j+1} = D(S_j) for some operator D that preserves the wdeg filtration.
# ---------------------------------------------------------------------------

def step6_recursion_test(tables, J_MAX):
    print("=" * 78)
    print("STEP 6: Try to identify a recursion S_{j+1} = D(S_j) preserving")
    print("        the wdeg(i_1 + i_2 + 2 i_3) filtration.")
    print("=" * 78)
    # Compute S_j in e-basis
    tables_e = {}
    for jj in range(J_MAX + 1):
        S_uyc = S_in_uyc(jj, tables)
        S_elem = to_elem_uyc(S_uyc)
        P = Poly(S_elem, e1_v, e2_v, e3_v)
        d = {}
        for m, cf in P.terms():
            if cf == 0:
                continue
            d[m] = cf
        tables_e[jj] = d

    # Hypothesis: S_{j+1} = (e_1^2 - e_2 + shift) * S_j + ...
    # We check by writing S_{j+1} - c * f * S_j for various f and see if wdeg drops.
    # We just print S_{j+1} - h_2^*(u,y,c) * S_j:
    # h_2(u,y,c) = e_1^2 - e_2 (elem->power sum -> h_2 = e_1^2 - e_2 not exactly)
    # Actually h_2 = sum x_i x_j + sum x_i^2 = e_1^2 - e_2.
    print("\n  Test hypothesis: S_{j+1} = (e_1^2 - e_2) * S_j + lower-wdeg stuff")
    print("  where h_2(u,y,c) = e_1^2 - e_2 for e_i = e_i(u,y,c).\n")
    for jj in range(J_MAX):
        S_j = sum(cf * e1_v ** m[0] * e2_v ** m[1] * e3_v ** m[2]
                  for m, cf in tables_e[jj].items())
        S_jp1 = sum(cf * e1_v ** m[0] * e2_v ** m[1] * e3_v ** m[2]
                    for m, cf in tables_e[jj + 1].items())
        h2_S_j = expand((e1_v ** 2 - e2_v) * S_j)
        diff = expand(S_jp1 - h2_S_j)
        Pdiff = Poly(diff, e1_v, e2_v, e3_v)
        max_w = -1
        for m, cf in Pdiff.terms():
            if cf == 0:
                continue
            i1, i2, i3 = m
            w = i1 + i2 + 2 * i3
            if w > max_w:
                max_w = w
        # if max_w <= j-1 or so, we win; if max_w = j+1, no progress; if diff=0, WOW.
        print(f"  j={jj} -> j+1={jj+1}: S_{{j+1}} - h_2 * S_j has max wdeg = {max_w}")
    # Show also raw kappa_mu = number of horizontal 2-strip paths landing at mu
    # (Rick's conjecture: sum kap_mu s_mu = h_2^j).
    # For a quick check: compute sum kap_mu s_mu(u,y,c) and compare with h_2^j.
    print("\n  Test kappa conjecture: sum_mu kap_mu s_mu(u,y,c) =? h_2(u,y,c)^j")
    from sympy import factor
    for jj in range(J_MAX + 1):
        # s_mu(u,y,c) = ordinary Schur = det[x_i^{mu_j + 3 - j}] / Vandermonde
        xs = (u_var, y_var, c)
        V_uyc = (u_var - y_var) * (u_var - c) * (y_var - c)
        total = Integer(0)
        for mu, kap in tables[jj]:
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[xs[i] ** ks[col] for col in range(3)] for i in range(3)]
            num = det3(rows)
            q, r = sp.div(Poly(num, u_var, y_var, c), Poly(V_uyc, u_var, y_var, c))
            assert r.as_expr() == 0
            total += kap * q.as_expr()
        total = expand(total)
        h2 = u_var ** 2 + y_var ** 2 + c ** 2 + u_var * y_var + u_var * c + y_var * c
        # h_2(u,y,c) = h_2 (complete homog sum) = e_1^2 - e_2 for 3 vars? Let's double-check
        # h_2 = sum x_i^2 + sum_{i<j} x_i x_j.  In elems: p_1 = e_1, p_2 = e_1^2 - 2 e_2.
        # h_2 = (p_1^2 + p_2)/2 = (e_1^2 + e_1^2 - 2 e_2)/2 = e_1^2 - e_2.  OK, so h_2 = e_1^2 - e_2.
        rhs = expand(h2 ** jj)
        diff = expand(total - rhs)
        print(f"    j={jj}: sum kap_mu s_mu(u,y,c) - h_2(u,y,c)^j = "
              f"{'0  ✓' if diff == 0 else 'NONZERO'}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    J_MAX = 7  # extend Attack B (which used 6) by one
    print(f"Building 2-strip lattice tables up to j = {J_MAX} ...")
    tables = bt(J_MAX)
    print("Table sizes:", {jj: len(tables[jj]) for jj in range(J_MAX + 1)})
    print()

    passed = {}
    passed['STEP1'] = step1_verify_structB(tables, J_MAX)
    passed['STEP2'] = step2_check_e_expansion_bound(I_MAX=6)
    passed['STEP3'] = step3_verify_route2_argument(tables, J_MAX)
    passed['STEP4'] = step4_check_extraction_per_e_monomial(J_MAX=6)
    step5_explore_structB(tables, min(J_MAX, 4))
    step6_recursion_test(tables, min(J_MAX, 5))

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    for k, v in passed.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    print()
    if all(passed.values()):
        print("ROUTE 2 argument STEPS 1-4 all verified empirically.")
        print("Conclusion: (StructB) IMPLIES (C) — proof is clean and airtight.")
        print("Remaining task: PROVE (StructB) structurally.")
    else:
        print("Some steps failed — Route 2 argument has a gap.")


if __name__ == "__main__":
    main()
