"""Day 116 — Attack B: weighted-degree filtration on S_j.

Setup (Day 109/115):
    u = a + 2
    xs = (u, b+1, c) = (a+2, b+1, c)
    For each partition mu appearing in bt(j) with multiplicity kap:
        rows[i][col] = fall(xs[i], mu[col] + (2 - col))   for i, col in {0,1,2}
        ds_j += kap * det3(rows)
    V(a, b, c) = (a - b + 1)(a - c + 2)(b - c + 1)
    S_j(a, b, c) := ds_j / V.

Define A_p := [a^{j - p}] S_j. Empirically deg_pi A_p = p (verified in Day 115).

Attack B claim: weighted degree wdeg with weights
        wdeg(a) = 1, wdeg(pi) = 1, wdeg(sigma) = 0
satisfies wdeg(S_j) <= j after rewriting S_j in variables (a, pi, sigma).

If TRUE: extracting [a^{j-p}] drops a-degree by (j-p) and leaves a polynomial in
(pi, sigma) with pi-degree <= j - (j-p) = p, closing OQ-DEG-PI-A_P-BOUND.

But note: S_j is a polynomial in (a, b, c), NOT twisted-symmetric in general.
The twist symmetry only applies to the a-coefficients A_p.  So we cannot directly
convert S_j to (a, pi, sigma).  What we CAN do:

    Approach 1: extract each A_p := [a^{j-p}] S_j; check A_p in (pi, sigma).
    Approach 2: extract by A-coefficient and check A_p wdeg <= p (weight pi=1, sigma=0).

The direct approach for "S_j in (a, pi, sigma)" only makes sense if every
A_p happens to be a polynomial in (pi, sigma).  It is (by twist symmetry Rmk R2).

So the check is: for each j, for each p, compute A_p in (pi, sigma) and verify
deg_pi A_p <= p.  This is the same as Day 115's (C) check.

TO GENUINELY TEST Attack B we need a DIFFERENT approach: derive the pi-degree
bound STRUCTURALLY from the determinantal formula for ds_j.  Here we:

    (a) recompute the empirical result Attack B needs to explain;
    (b) check whether ds_j has a natural weighted degree in (a, b, c) with weights
        (1, 1, 1) on (a, b, c) --> that gives wdeg ds_j <= 2j + 3 (row degrees), and
        wdeg V = 3, so wdeg S_j <= 2j.  Not sharp enough.
    (c) try weights (1, 2, 2) on (a, b, c) so wdeg(pi=(b+1)c) = wdeg(b) + wdeg(c) = 4,
        wdeg(sigma) = 2.  Doesn't cleanly give what we want.
    (d) try weights (1, 1, 1) but WITH a two-variable analysis in (a, sigma, pi)
        after twist symmetry ==> works only on the A_p, not S_j.

The RIGHT weighted-degree formulation: define wdeg for MONOMIALS m = a^A b^B c^C by
        wdeg(m) := A + max(B, C)
which is the (a, "b or c") weighted degree.  Then note that in (pi, sigma) with
pi = bc + c, sigma = b + c + 1:
    pi has b-degree 1 and c-degree 1, so max is 1.
    sigma has b-degree 1 and c-degree 1, max is 1.
So a monomial pi^k sigma^d has wdeg = k + d in the (b, c) part... hmm not quite.

The cleanest way: weight by (a, b, c) --> (1, 1, 0), so weight of pi = 1 (since
pi = (b+1)c, the DEGREE OF PI IN B is 1, but pi is a polynomial in b, c).
Ah, actually the weights (1, 1, 0) means wdeg(monomial a^A b^B c^C) = A + B.
Then in (pi, sigma), pi has b-degree 1 and c-degree 1 (leading term bc);
so wdeg(pi) = 1.  sigma = b+c+1 has b-degree 1 and c-degree 0 or 0 and 1;
maximum wdeg of any monomial of sigma is 1.  So (1, 1, 0) DOES NOT give sigma weight 0
uniformly, only the (constant + c)-part is weight 0; the b-part is weight 1.

Similarly (1, 0, 1) makes sigma have both weights.

Rick's suggested weighting: wdeg(a, pi, sigma) = (1, 1, 0) IN (a, pi, sigma) VARIABLES.
This is well-defined ON polynomials in (a, pi, sigma) only.  Since A_p IS such
a polynomial (twist-symmetric), we can talk about its wdeg.  For S_j we CANNOT
without extending sigma to a full basis element, unless every A_p is (pi, sigma).

CONCLUSION: to attack B, verify:
    (E1) for each j <= 6 and each p, A_p is a polynomial in (pi, sigma).
    (E2) deg_pi A_p <= p (this is (C)).
    (E3) Try to prove (E2) directly from ds_j structure.

For (E3): the natural weighted-degree filtration.  Assign weights (1, 1, 0, 1) to
variables (a, b, c, ...) with WEIGHT ONLY on a and b BUT also a c on the c^k inside pi.
Doesn't clean up because sigma still has a b-piece.

Actually the RIGHT filtration is: bihomogeneous degree in (a, y) where y = b + 1
(so u = a + 2 = (a) + 2 shift, y = (b) + 1 shift, treat c as its own variable).
xs = (u, y, c) = (a + 2, b + 1, c) has a-degree 1 in slot 0, b-degree 1 in slot 1, c-degree 1 in slot 2.

FILTRATION CLAIM (Attack B refined): Consider the DIAGONAL a-weight and c-weight jointly.
Since row i uses only x_i, and column col has "size" k_col = mu[col] + (2 - col),
row 0 has weight sum k_0+k_1+k_2 IN a alone in the determinant (with some cross-term structure).

Actually the very clean claim: the a-degree of ds_j equals row 0 contribution:
    deg_a ds_j = max_mu (k_0 for mu) = max_mu (mu[0] + 2).
Similarly deg_b ds_j uses row 1 --> max_mu(k_1) = max_mu(mu[0] + 1) (col 0 gives largest k for row 1).
Wait no: fall(b+1, k_col) has b-degree k_col regardless of column.  So the b-degree
of row 1 entry (1, col) is k_col.  Similarly c-degree of row 2 entry (2, col) is k_col.
In the determinant, we PICK ONE ENTRY PER ROW AND COL: so summing k over columns
= k_0 + k_1 + k_2 = mu[0] + mu[1] + mu[2] + 3 = |mu| + 3 = 2j + 3.  Uniform!

But this counts:  a-deg + b-deg + c-deg <= 2j + 3 for ds_j.
V has a-deg=1, b-deg=1, c-deg=1, total deg 3.  So S_j = ds_j/V has
    (a-deg + b-deg + c-deg)_max <= 2j.

Now for A_p := [a^{j-p}] S_j: we have a-part fixed at j-p; the remaining
(b-deg + c-deg) <= 2j - (j - p) = j + p.  This is bound (A) of Day 115. Good.

To get pi-degree bound: we need to control b-degree AND c-degree of A_p separately,
or use twist symmetry.  Let's check MORE carefully: does deg_b A_p + deg_c A_p give
enough?  deg_b A_p <= j (bound B), so pi = (b+1)c has 1 b-degree per pi, so pi^k
has b-degree = k.  If A_p has deg_b <= j, then pi^k * (stuff in sigma) contribution
to deg_b is >= k (since sigma has 1 b-degree too).  This alone doesn't force k <= p.

Let me just RUN the verification and see the empirical picture, THEN attempt the theory.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer

a, b, c = symbols('a b c')
u_expr = a + 2
sig, pi_v = symbols('sigma pi')


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


def ds_symbolic(jj, tables):
    xs = (u_expr, b + 1, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def V_of():
    return (a - b + 1) * (a - c + 2) * (b - c + 1)


def S_of(jj, tables):
    dsj = ds_symbolic(jj, tables)
    V = V_of()
    q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
    assert r.as_expr() == 0, f"j={jj}: V does not divide ds_j"
    return q.as_expr()


def extract_A_p(S, jj, p):
    if jj - p < 0:
        return Integer(0)
    pab = Poly(S, a, b, c)
    result = Integer(0)
    for monom, cf in pab.terms():
        da, db, dc = monom
        if da == jj - p:
            result += cf * b ** db * c ** dc
    return expand(result)


def to_pi_sigma(F):
    """Rewrite F(b, c) in variables (pi=(b+1)c, sigma=b+c+1) if possible."""
    z = symbols('_z_pi_sig_')
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


def wdeg_pi_sigma(F_ps, w_pi=1, w_sig=0):
    """Weighted degree of F_ps (polynomial in pi, sigma) with given weights."""
    if F_ps == 0:
        return -1
    P = sp.Poly(F_ps, pi_v, sig)
    m = -1
    for monom, cf in P.terms():
        if cf == 0:
            continue
        k, d = monom
        w = w_pi * k + w_sig * d
        if w > m:
            m = w
    return m


def wdeg_abc(F, w_a=1, w_b=1, w_c=0):
    """Weighted degree of F in (a, b, c) with given integer weights."""
    if F == 0:
        return -1
    P = sp.Poly(F, a, b, c)
    m = -1
    for monom, cf in P.terms():
        if cf == 0:
            continue
        da, db, dc = monom
        w = w_a * da + w_b * db + w_c * dc
        if w > m:
            m = w
    return m


u_var, y_var = symbols('u y')
e1_v, e2_v, e3_v = symbols('e1 e2 e3')


def to_elem_uyc(F):
    """Rewrite a symmetric polynomial F(u, y, c) in (e1, e2, e3)."""
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


def S_in_uyc(jj, tables):
    dsj = ds_symbolic(jj, tables)
    dsj_uyc = expand(dsj.subs([(a, u_var - 2), (b, y_var - 1)]))
    V_uyc = (u_var - y_var) * (u_var - c) * (y_var - c)
    q, r = sp.div(Poly(dsj_uyc, u_var, y_var, c), Poly(V_uyc, u_var, y_var, c))
    assert r.as_expr() == 0
    return q.as_expr()


def main():
    J = 6
    print(f"Building shifted-Schur tables up to j = {J} ...")
    tables = bt(J)
    print("Table sizes:", {jj: len(tables[jj]) for jj in range(J + 1)})

    print("\n" + "=" * 78)
    print("STEP 1: Compute S_j for j = 0..J symbolically")
    print("=" * 78)
    Ss = {}
    for jj in range(J + 1):
        S = S_of(jj, tables)
        Ss[jj] = S
        pS = sp.Poly(S, a, b, c) if S != 0 else None
        deg_a = pS.degree(a) if pS is not None and pS.total_degree() >= 0 else -1
        deg_b = pS.degree(b) if pS is not None and pS.total_degree() >= 0 else -1
        deg_c = pS.degree(c) if pS is not None and pS.total_degree() >= 0 else -1
        tot = pS.total_degree() if pS is not None else -1
        print(f"  j={jj}: S_j has deg_a={deg_a}, deg_b={deg_b}, deg_c={deg_c}, "
              f"total_deg={tot}")

    print("\n" + "=" * 78)
    print("STEP 2: Check monomial-level weighted degree of S_j in (a, b, c)")
    print("        Various weightings to explore Attack B.")
    print("=" * 78)
    for jj in range(J + 1):
        S = Ss[jj]
        w110 = wdeg_abc(S, 1, 1, 0)
        w101 = wdeg_abc(S, 1, 0, 1)
        w111 = wdeg_abc(S, 1, 1, 1)
        w120 = wdeg_abc(S, 1, 2, 0)  # weight b as pi
        w_max = wdeg_abc(S, 1, 1, 0) if wdeg_abc(S, 1, 1, 0) >= wdeg_abc(S, 1, 0, 1) else wdeg_abc(S, 1, 0, 1)
        print(f"  j={jj}: wdeg(1,1,0)={w110}, wdeg(1,0,1)={w101}, "
              f"wdeg(1,1,1)={w111}, wdeg(1,2,0)={w120}")

    print("\n" + "=" * 78)
    print("STEP 3: Extract A_p and check deg_pi in (pi, sigma) variables")
    print("        This is the EMPIRICAL FACT Attack B needs to explain.")
    print("=" * 78)
    all_ok = True
    for jj in range(J + 1):
        S = Ss[jj]
        for p in range(jj + 1):
            A = extract_A_p(S, jj, p)
            if A == 0:
                continue
            A_ps = to_pi_sigma(A)
            if A_ps is None:
                print(f"  j={jj}, p={p}: A_p NOT in (pi, sigma)!")
                all_ok = False
                continue
            deg_pi = wdeg_pi_sigma(A_ps, 1, 0)
            deg_sig = wdeg_pi_sigma(A_ps, 0, 1)
            tot_ps = wdeg_pi_sigma(A_ps, 1, 1)
            check = "OK" if deg_pi <= p else "FAIL"
            print(f"  j={jj}, p={p}: A_p deg_pi={deg_pi} [<={p} {check}], "
                  f"deg_sig={deg_sig}, total_pi_sig={tot_ps}")
            if deg_pi > p:
                all_ok = False
    print(f"\nEMPIRICAL (C) [deg_pi A_p <= p]: {'PASS' if all_ok else 'FAIL'}")

    print("\n" + "=" * 78)
    print("STEP 4: THE Attack B TEST — try to rewrite S_j in (a, pi, sigma).")
    print("        Since S_j itself is NOT twist-symmetric, we treat this")
    print("        by extracting each a-coeff and rewriting in (pi, sigma).")
    print("        Attack B: wdeg(S_j) <= j with weights (a=1, pi=1, sigma=0).")
    print("=" * 78)
    attackB_ok = True
    for jj in range(J + 1):
        S = Ss[jj]
        max_w = -1
        max_info = None
        for p in range(jj + 1):
            A = extract_A_p(S, jj, p)
            if A == 0:
                continue
            A_ps = to_pi_sigma(A)
            if A_ps is None:
                print(f"  j={jj}, p={p}: A_p not in (pi, sigma) — Attack B undefined!")
                attackB_ok = False
                continue
            deg_pi = wdeg_pi_sigma(A_ps, 1, 0)
            if deg_pi < 0:
                continue
            # a-degree is (jj - p); pi weight 1; sigma weight 0
            w = (jj - p) + deg_pi
            if w > max_w:
                max_w = w
                max_info = (p, deg_pi)
        check = "OK" if max_w <= jj else "FAIL"
        print(f"  j={jj}: max wdeg(a=1,pi=1,sig=0) = {max_w}  [<={jj}  {check}] "
              f"achieved at (p={max_info[0] if max_info else '-'}, "
              f"deg_pi={max_info[1] if max_info else '-'})")
        if max_w > jj:
            attackB_ok = False
    print(f"\nATTACK B EMPIRICAL: {'HOLDS' if attackB_ok else 'FAILS'}")

    print("\n" + "=" * 78)
    print("STEP 5: Analyze S_j row-by-row degree structure in (a, b, c)")
    print("        This informs whether a structural proof of Attack B exists.")
    print("=" * 78)
    # For each mu in bt(j), print k_col vector and det degree info
    for jj in range(min(J + 1, 4)):
        print(f"\n  j = {jj}:")
        for mu, kap in tables[jj]:
            ks = tuple(mu[col] + (2 - col) for col in range(3))
            # row i has entries with x_i-degree = k_col; determinant picks one
            # entry per row per col, so a-deg of any term = k_perm(0), b-deg = k_perm(1),
            # c-deg = k_perm(2), for perm a permutation of columns.
            # sum k_col over any perm = k_0 + k_1 + k_2 = |mu| + 3 = 2j + 3.
            print(f"     mu={mu} (|mu|={sum(mu)}), k={ks}, sum_k={sum(ks)}, kap={kap}")

    # Sanity: check that deg_a + deg_b + deg_c of ds_j <= 2j + 3 for each MONOMIAL.
    print("\n" + "=" * 78)
    print("STEP 6: Verify per-monomial wdeg(1,1,1) on ds_j <= 2j + 3, on S_j <= 2j")
    print("=" * 78)
    for jj in range(J + 1):
        dsj = ds_symbolic(jj, tables)
        w_ds = wdeg_abc(dsj, 1, 1, 1)
        w_S = wdeg_abc(Ss[jj], 1, 1, 1)
        c1 = "OK" if w_ds <= 2 * jj + 3 else "FAIL"
        c2 = "OK" if w_S <= 2 * jj else "FAIL"
        print(f"  j={jj}: wdeg(1,1,1) ds_j = {w_ds} [<={2*jj+3} {c1}], "
              f"S_j = {w_S} [<={2*jj} {c2}]")

    print("\n" + "=" * 78)
    print("STEP 7: KEY DISCOVERY — S_j is SYMMETRIC in (u, y, c) = (a+2, b+1, c)")
    print("        because V = (u-y)(u-c)(y-c) is the Vandermonde in (u, y, c).")
    print("        Expand S_j in elementary symmetric functions e1, e2, e3.")
    print("        Structural Attack B claim: c_{i1,i2,i3} = 0 unless i1 + i2 + 2*i3 <= j.")
    print("=" * 78)
    struct_ok = True
    for jj in range(J + 1):
        S_uyc = S_in_uyc(jj, tables)
        # Sanity check symmetry
        sym_check1 = sp.simplify(
            S_uyc - S_uyc.subs([(u_var, y_var), (y_var, u_var)], simultaneous=True))
        sym_check2 = sp.simplify(
            S_uyc - S_uyc.subs([(u_var, c), (c, u_var)], simultaneous=True))
        assert sym_check1 == 0 and sym_check2 == 0, f"j={jj}: NOT symmetric in u,y,c"

        S_elem = to_elem_uyc(S_uyc)
        P_elem = Poly(S_elem, e1_v, e2_v, e3_v)
        max_w = -1
        max_info = None
        for m, cf in P_elem.terms():
            if cf == 0:
                continue
            i1, i2, i3 = m
            w = i1 + i2 + 2 * i3
            if w > max_w:
                max_w = w
                max_info = (i1, i2, i3, cf)
        ok = max_w <= jj
        if not ok:
            struct_ok = False
        print(f"  j={jj}: symmetric in u,y,c: True.  Max e-wdeg (1,1,2) = {max_w} "
              f"[<={jj}  {'OK' if ok else 'FAIL'}]  leader: {max_info}")

    print(f"\nSTRUCTURAL Attack B CLAIM (e-basis wdeg): "
          f"{'HOLDS' if struct_ok else 'FAILS'}")

    print("\n" + "=" * 78)
    print("STEP 8: Test whether individual factorial Schur s*_mu satisfies wdeg <= j.")
    print("        (Would give term-by-term proof; if fails, need sum-level identity.)")
    print("=" * 78)
    from sympy import expand as _expand
    term_ok = True
    for jj in range(min(J + 1, 6)):
        for mu, kap in tables[jj]:
            xs = (u_var, y_var, c)
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
            num = det3(rows)
            V_uyc = (u_var - y_var) * (u_var - c) * (y_var - c)
            q, r = sp.div(Poly(num, u_var, y_var, c), Poly(V_uyc, u_var, y_var, c))
            assert r.as_expr() == 0
            s_star = q.as_expr()
            s_elem = to_elem_uyc(s_star)
            P = Poly(s_elem, e1_v, e2_v, e3_v)
            max_w = -1
            for m, cf in P.terms():
                if cf == 0:
                    continue
                i1, i2, i3 = m
                w = i1 + i2 + 2 * i3
                if w > max_w:
                    max_w = w
            ok = max_w <= jj
            if not ok:
                term_ok = False
                print(f"  j={jj}, mu={mu}, kap={kap}: s*_mu has e-wdeg {max_w} > {jj}  VIOLATION")
            else:
                print(f"  j={jj}, mu={mu}, kap={kap}: s*_mu has e-wdeg {max_w} <= {jj}  ok")

    print(f"\nTERM-BY-TERM WDEG BOUND: "
          f"{'HOLDS (would give trivial proof!)' if term_ok else 'FAILS (need cancellation)'}")


if __name__ == "__main__":
    main()
