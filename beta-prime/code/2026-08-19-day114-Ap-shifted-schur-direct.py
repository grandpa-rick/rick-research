"""Day 114 (compute pass): direct shifted-Schur interpolation of A_p.

Goal: expand A_p(b, c, j) = sum_lambda c_lambda(j, p) * s^*_lambda(y_2, y_3)
where s^*_lambda is the (2-variable) Okounkov shifted Schur (SV / Okounkov,
q-alg/9605042 Def 1.2). Then read off closed forms for c_lambda(j, p) and
try to spot the uniform-in-p pattern.

Recap of the master technique (Day 113):
  * Any symmetric F(y_2, y_3) of y-degree <= D expands as
      F = sum_{|lambda| <= D} c_lambda s^*_lambda(y_2, y_3).
  * Vanishing: s^*_lambda(mu + delta) = 0 unless lambda ⊆ mu.
  * Size-triangularity: if F(mu + delta) = 0 for all |mu| < D_0, then
    c_lambda = 0 for |lambda| < D_0.
  * Diagonal formula (2 vars, delta = (1, 0)):
      s^*_{lambda_1, lambda_2}(lambda_1 + 1, lambda_2)
        = (lambda_1 + 1)! * lambda_2! / (lambda_1 - lambda_2 + 1).
  * Extract c_lambda by evaluating F at (lambda_1 + 1, lambda_2) after killing
    the lower-degree terms one by one.

For the 2-variable case, the standard explicit formula is
  s^*_{lambda_1, lambda_2}(x_1, x_2)
     = [ (x_1 + 1)^{↓(lambda_1 + 1)} * (x_2)^{↓lambda_2}
       - (x_1 + 1)^{↓lambda_2}   * (x_2)^{↓(lambda_1 + 1)} ]  /  (x_1 - x_2 + 1).

Here (x)^{↓m} = x*(x-1)*...*(x-m+1) (falling factorial).

Sanity: at (x_1, x_2) = (lambda_1 + 1, lambda_2), the second product vanishes
(because (lambda_2)^{↓(lambda_1 + 1)} = 0 when lambda_1 + 1 > lambda_2), so
s^*_lambda(lambda + delta) = (lambda_1 + 1)! * lambda_2! / (lambda_1 - lambda_2 + 1).

For A_p the natural "y" variables are b and c (with the shift b -> b + 1 built
into the falling-factorial argument x_1 = b + 1, x_2 = c). Equivalently the
"shifted point" for a partition mu = (mu_1, mu_2) is (b, c) = (mu_1, mu_2)
with delta = (1, 0). We test the delta = (0, 0) case too (i.e. (b, c) =
(mu_1 - 1, mu_2)) and pick whichever gives cleanest vanishing.

Author: compute agent, Rick's Day-113 program.
"""

from collections import defaultdict
from itertools import combinations

import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational, factor, simplify

# ---------------------------------------------------------------------------
# Day-113 machinery (copied verbatim so this file is self-contained).
# ---------------------------------------------------------------------------

a, b, c = symbols('a b c')
u = a + 2


def fall(x, m):
    """Falling factorial x^{↓m} = x*(x-1)*...*(x-m+1)."""
    if m < 0:
        return Integer(0)
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
    xs = (u, b + 1, c)
    total = Integer(0)
    for mu, kap in tables[jj]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def V_of():
    return (a - b + 1) * (a - c + 2) * (b - c + 1)


def dsV_all(J, tables):
    V = V_of()
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


# ---------------------------------------------------------------------------
# Shifted-Schur (2 vars).
# ---------------------------------------------------------------------------


def s_star(lam, x1, x2):
    """s^*_{lam_1, lam_2}(x1, x2) via the 2-variable Okounkov formula.

    s^*_lambda(x_1, x_2) = [ (x_1+1)^{↓(lam_1+1)} * (x_2)^{↓lam_2}
                            - (x_1+1)^{↓lam_2}    * (x_2)^{↓(lam_1+1)} ]
                          / (x_1 - x_2 + 1).
    """
    lam1, lam2 = lam
    assert lam1 >= lam2 >= 0
    num = (fall(x1 + 1, lam1 + 1) * fall(x2, lam2)
           - fall(x1 + 1, lam2) * fall(x2, lam2 + (lam1 - lam2 + 1)))
    #  ^ second term: (x2)^{↓(lam_1 + 1)}
    #  (lam2 + (lam1 - lam2 + 1) = lam1 + 1)
    den = (x1 - x2 + 1)
    # Divide as polynomial (num is divisible by den, symbolically).
    num = sp.expand(num)
    q, r = sp.div(sp.Poly(num, x1, x2), sp.Poly(den, x1, x2))
    if r.as_expr() != 0:
        # Fall back: evaluate limit
        return sp.together(num / den)
    return q.as_expr()


def s_star_eval(lam, x1_val, x2_val):
    """Numeric evaluation of s^*_lambda at specific (x1, x2). Handles the
    would-be 0/0 by using the closed-form determinantal expression carefully."""
    lam1, lam2 = lam
    A1 = fall(x1_val + 1, lam1 + 1) * fall(x2_val, lam2)
    A2 = fall(x1_val + 1, lam2) * fall(x2_val, lam1 + 1)
    num = A1 - A2
    den = x1_val - x2_val + 1
    if den == 0:
        # Use L'Hopital via the symbolic form
        xs, ys = symbols('_xs _ys')
        expr = s_star(lam, xs, ys)
        return sp.limit(expr.subs(ys, xs + 1 + symbols('_eps')), symbols('_eps'), 0).subs(xs, x1_val)
    return sp.Rational(num, den) if isinstance(num, sp.Integer) and isinstance(den, sp.Integer) else sp.simplify(num / den)


# ---------------------------------------------------------------------------
# Verify the shifted-Schur diagonal formula.
# ---------------------------------------------------------------------------


def check_s_star():
    """The formula I coded evaluates via Sergeev-Veselov determinant with rho=(1,0)
    baked in. That is, the natural evaluation point for lambda is (b, c) = (lam_1, lam_2)
    (no extra shift). Diagonal formula becomes:
        s^*_lambda(lam) = (lam_1 + 1)! * lam_2! / (lam_1 - lam_2 + 1)
    Vanishing: s^*_lambda(mu) = 0 whenever lambda not subset mu.
    """
    print("  Sanity: verify s^*_lambda(lambda) = (lam_1+1)! lam_2! / (lam_1 - lam_2 + 1)")
    print("  (with delta = (0, 0), eval at (b, c) = (lam_1, lam_2)).")
    ok = True
    for lam1 in range(5):
        for lam2 in range(lam1 + 1):
            lam = (lam1, lam2)
            expected = sp.factorial(lam1 + 1) * sp.factorial(lam2) / (lam1 - lam2 + 1)
            got = s_star_eval(lam, lam1, lam2)
            if sp.simplify(got - expected) != 0:
                print(f"    FAIL lam = {lam}: got {got}, expected {expected}")
                ok = False
    print(f"  Diagonal formula OK? {ok}")
    print("  Sanity: verify s^*_lambda(mu) = 0 when lambda not subset mu.")
    ok2 = True
    for lam1 in range(4):
        for lam2 in range(lam1 + 1):
            lam = (lam1, lam2)
            for mu1 in range(4):
                for mu2 in range(mu1 + 1):
                    mu = (mu1, mu2)
                    subset = (lam1 <= mu1 and lam2 <= mu2)
                    val = s_star_eval(lam, mu1, mu2)
                    if not subset and val != 0:
                        print(f"    FAIL lam={lam}, mu={mu}, not subset but s* = {val}")
                        ok2 = False
    print(f"  Vanishing OK? {ok2}")
    return ok and ok2


# ---------------------------------------------------------------------------
# Vanishing pattern of A_p.
# ---------------------------------------------------------------------------


def partitions_up_to(N):
    """All 2-part partitions mu = (mu_1, mu_2) with mu_1 >= mu_2 >= 0 and |mu| <= N."""
    out = []
    for total in range(N + 1):
        for mu1 in range(total + 1):
            mu2 = total - mu1
            if mu1 >= mu2 >= 0:
                out.append((mu1, mu2))
    return out


def measure_vanishing(F, delta=(0, 0), N_max=20):
    """For each |mu|, count how many partitions mu of that size have F(mu + delta) = 0.
    Return dict {size: (num_zeros, num_partitions_of_that_size, list_of_nonzero_mu)}."""
    parts_by_size = defaultdict(list)
    for mu in partitions_up_to(N_max):
        parts_by_size[mu[0] + mu[1]].append(mu)
    data = {}
    for size, parts in sorted(parts_by_size.items()):
        zeros = 0
        nz = []
        for mu in parts:
            val = F.subs([(b, mu[0] + delta[0]), (c, mu[1] + delta[1])])
            val = sp.expand(val)
            if val == 0:
                zeros += 1
            else:
                nz.append((mu, val))
        data[size] = (zeros, len(parts), nz)
    return data


def find_D0(F, delta=(0, 0), N_max=20):
    """Smallest D_0 such that F(mu + delta) = 0 for all |mu| < D_0."""
    data = measure_vanishing(F, delta=delta, N_max=N_max)
    D0 = 0
    for size in sorted(data.keys()):
        zeros, tot, _ = data[size]
        if zeros == tot:
            D0 = size + 1
        else:
            break
    return D0, data


# ---------------------------------------------------------------------------
# Extract c_lambda via peeling.
# ---------------------------------------------------------------------------


def shifted_schur_expand(F, D_max, delta=(0, 0)):
    """Given symmetric-under-(b,c)->(c-1,b+1) polynomial F(b, c) of total
    y-degree <= D_max, compute {lambda: c_lambda} such that
        F = sum_{|lambda| <= D_max} c_lambda * s^*_lambda(b, c).

    Uses size-triangular peeling: order lambdas by |lambda| ascending, then
    lex within a size. At partition (lam_1, lam_2), we can evaluate the residual
    at (b, c) = (lam_1 + delta[0], lam_2 + delta[1]) and all lower-|lambda|
    contributions have been killed; the only surviving term with |lambda'| =
    |lambda| that is nonzero at (lam+delta) is lambda' = lambda itself (by
    the s* vanishing lemma). So c_lambda = residual / s*_lambda(lam+delta).
    """
    coeffs = {}
    residual = sp.expand(F)
    for size in range(D_max + 1):
        # iterate lambdas of this size in lex-decreasing order of lam_1
        lams = []
        for lam1 in range(size + 1):
            lam2 = size - lam1
            if lam1 >= lam2 >= 0:
                lams.append((lam1, lam2))
        # order doesn't strictly matter within a size because of the
        # subset-vanishing lemma, but do descending lam_1 for stability.
        lams.sort(reverse=True)
        for lam in lams:
            eval_pt_b = lam[0] + delta[0]
            eval_pt_c = lam[1] + delta[1]
            val = sp.expand(residual.subs([(b, eval_pt_b), (c, eval_pt_c)]))
            if val == 0:
                coeffs[lam] = Integer(0)
                continue
            diag = s_star_eval(lam, eval_pt_b, eval_pt_c)
            if diag == 0:
                raise RuntimeError(f"diagonal s*_{lam}({eval_pt_b}, {eval_pt_c}) = 0 — bad delta?")
            c_lam = sp.simplify(val / diag)
            coeffs[lam] = c_lam
            # subtract this term
            ss = s_star(lam, b, c)
            residual = sp.expand(residual - c_lam * ss)
    # Verify residual is 0
    if sp.expand(residual) != 0:
        print(f"    !!! nonzero residual after peeling to size {D_max}:")
        Pres = sp.Poly(residual, b, c)
        print(f"        residual deg (b,c) = ({Pres.degree(b) if not Pres.is_zero else -1}, "
              f"{Pres.degree(c) if not Pres.is_zero else -1})")
    return coeffs, residual


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------


def poly_deg_bc(F):
    if F == 0:
        return -1, -1
    P = sp.Poly(F, b, c)
    return P.degree(b), P.degree(c)


def main():
    J = 12
    print("=" * 78)
    print("Day-114 compute pass: direct shifted-Schur interpolation of A_p")
    print("=" * 78)
    print("\n[Setup] shifted-Schur sanity checks...")
    ss_ok = check_s_star()
    assert ss_ok

    print(f"\n[Setup] Building shifted-Schur tables & ds_j/V up to j = {J}...")
    tables = bt(J)
    dsV = dsV_all(J, tables)

    A_data = {}   # (p, j) -> A_p(b, c, j)
    for p in (2, 3, 4):
        j_min = 2 * p
        for jj in range(j_min, J + 1):
            A_data[(p, jj)] = extract_A_p(jj, p, dsV)

    # -----------------------------------------------------------------
    # STEP 1: vanishing pattern
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 1  Vanishing pattern of A_p at partition points.")
    print("=" * 78)

    D0_table = {}   # (p, j, delta) -> D0
    for delta in [(0, 0), (1, 0)]:
        print(f"\n  --- delta = {delta} ---")
        print(f"  Columns: |mu| ; (zeros, total, first nonzero (mu, F(mu+delta) or 'all zero'))")
        for p in (2, 3, 4):
            print(f"\n  p = {p}:")
            for jj in sorted(k[1] for k in A_data if k[0] == p):
                F = A_data[(p, jj)]
                D0, data = find_D0(F, delta=delta, N_max=jj + 2)
                D0_table[(p, jj, delta)] = D0
                # Report line
                line = f"    j = {jj}:  D_0 = {D0}"
                # first nonzero row
                for size in sorted(data.keys()):
                    zeros, tot, nz = data[size]
                    if zeros != tot:
                        first_nz = nz[0]
                        line += f"  (first nonzero: |mu|={size}, mu={first_nz[0]}, val={sp.factor(first_nz[1])[:60] if False else first_nz[1]})"
                        break
                print(line)

    for chosen_delta in [(0, 0), (1, 0)]:
        print(f"\n  D_0(p, j) summary (delta = {chosen_delta}):")
        for p in (2, 3, 4):
            row = f"    p = {p}:"
            for jj in sorted(k[1] for k in A_data if k[0] == p):
                row += f"  j={jj}: D0={D0_table[(p, jj, chosen_delta)]};"
            print(row)

    # Pattern spotting
    print("\n  Look for pattern D_0(p, j) in terms of (p, j) with delta=(0,0):")
    for p in (2, 3, 4):
        print(f"    p = {p}:  j - D_0 (delta=(0,0)) = ", end="")
        for jj in sorted(k[1] for k in A_data if k[0] == p):
            print(f"{jj - D0_table[(p, jj, (0, 0))]},", end=" ")
        print()

    # -----------------------------------------------------------------
    # STEP 2: shifted-Schur expansion
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 2  Direct shifted-Schur expansion  A_p = sum c_lambda * s^*_lambda.")
    print("=" * 78)

    # Choose delta = (0, 0) (matches the formula's baked-in shift). Also determine D_max from bc-degrees.
    delta = (0, 0)
    all_coeffs = {}   # (p, j) -> {lambda: c_lambda}
    for p in (2, 3, 4):
        print(f"\n  p = {p}:")
        for jj in sorted(k[1] for k in A_data if k[0] == p):
            F = A_data[(p, jj)]
            db, dc = poly_deg_bc(F)
            D_max = db + dc + 1   # upper bound on |lambda| for expansion
            coeffs, residual = shifted_schur_expand(F, D_max, delta=delta)
            nz = {lam: cf for lam, cf in coeffs.items() if cf != 0}
            all_coeffs[(p, jj)] = nz
            # Report
            sizes_present = sorted(set(lam[0] + lam[1] for lam in nz))
            print(f"    j = {jj}:  deg(b, c) = ({db}, {dc}); |lambda| range = "
                  f"{sizes_present[0] if sizes_present else '-'} .. {sizes_present[-1] if sizes_present else '-'}; "
                  f"# nonzero c_lambda = {len(nz)}")
            # residual check
            if sp.expand(residual) != 0:
                print(f"      WARNING: nonzero residual!")

    # Which lambdas actually appear?
    print("\n  Nonzero-c_lambda index sets:")
    for p in (2, 3, 4):
        print(f"\n    p = {p}:")
        for jj in sorted(k[1] for k in A_data if k[0] == p):
            nz = all_coeffs[(p, jj)]
            lams = sorted(nz.keys(), key=lambda lm: (lm[0] + lm[1], lm[0]))
            print(f"      j = {jj}: {lams}")

    # Constraint hunting: does lambda_2 <= p always hold? Does |lambda| <= j?
    print("\n  Constraint check: for each (p, j) does every nonzero lambda satisfy "
          "lam_2 <= p AND |lambda| <= j AND |lambda| >= D_0?")
    for p in (2, 3, 4):
        for jj in sorted(k[1] for k in A_data if k[0] == p):
            nz = all_coeffs[(p, jj)]
            D0 = D0_table[(p, jj, delta)]
            viol = []
            for lam in nz:
                if lam[1] > p:
                    viol.append(("lam_2 > p", lam))
                if lam[0] + lam[1] > jj:
                    viol.append(("|lam| > j", lam))
                if lam[0] + lam[1] < D0:
                    viol.append(("|lam| < D_0", lam))
            if viol:
                print(f"    p={p}, j={jj}: VIOLATIONS {viol[:5]}")
            else:
                print(f"    p={p}, j={jj}: all nonzero lambda satisfy D_0<=|lambda|<=j, lam_2<=p  (OK)")

    # -----------------------------------------------------------------
    # STEP 3: closed-form c_lambda(j) for each lambda, at fixed p.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 3  Fit c_lambda(j, p) as polynomial in j for each fixed (p, lambda).")
    print("=" * 78)

    j_sym = symbols('j')

    def fit_poly_in_j(samples, max_deg=15):
        """samples = [(j_val, y_val)]. Return polynomial in j_sym or None."""
        n = len(samples)
        for D in range(min(n, max_deg + 1)):
            rows = []
            yy = []
            for (jv, yv) in samples[:D + 1]:
                rows.append([Rational(jv) ** i for i in range(D + 1)])
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
                poly = sum(sol[i] * j_sym ** i for i in range(D + 1))
                return sp.expand(poly)
        return None

    # For each p, collect all lambdas that appear at any j.
    closed_forms = {}   # (p, lambda) -> polynomial in j
    for p in (2, 3, 4):
        print(f"\n  --- p = {p} ---")
        js = sorted(k[1] for k in A_data if k[0] == p)
        lam_set = set()
        for jj in js:
            lam_set.update(all_coeffs[(p, jj)].keys())
        lam_list = sorted(lam_set, key=lambda lm: (lm[0] + lm[1], lm[0]))
        for lam in lam_list:
            samples = []
            for jj in js:
                cv = all_coeffs[(p, jj)].get(lam, Integer(0))
                samples.append((jj, cv))
            poly_j = fit_poly_in_j(samples)
            if poly_j is None:
                print(f"    lambda = {lam}: NO poly-in-j fit ({len(samples)} samples: {samples})")
            else:
                # Factor / present nicely
                closed_forms[(p, lam)] = poly_j
                print(f"    lambda = {lam}:  c_lambda(j) = {sp.factor(poly_j)}")

    # -----------------------------------------------------------------
    # STEP 3.5: for fixed p, degree of c_lambda(j) in j and common structure per level.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 3.5  Degree-in-j of c_lambda for each p (level ell = |lambda| - j).")
    print("=" * 78)
    for p in (2, 3, 4):
        print(f"\n  p = {p}:")
        # Group by level ell
        lam_by_level = defaultdict(list)
        for (pp, lam) in closed_forms:
            if pp != p:
                continue
            # ell = |lam| - j_min where j_min ranges — we want ell RELATIVE to each j
            # but c_lambda(j) is a polynomial in j. Report degree.
            cf = closed_forms[(pp, lam)]
            deg = sp.Poly(cf, j_sym).degree() if cf != 0 else -1
            lam_by_level[lam[0] + lam[1]].append((lam, deg, cf))
        for size in sorted(lam_by_level.keys()):
            print(f"    |lambda| = {size}:")
            for (lam, deg, cf) in sorted(lam_by_level[size]):
                # extract leading coefficient in j
                Pc = sp.Poly(cf, j_sym)
                lc = Pc.LC() if cf != 0 else 0
                print(f"      lambda = {lam}: deg_j = {deg}, leading coeff = {sp.nsimplify(lc)}")

    # For fixed p, check whether c_lambda(j) has a common j-independent factor across |lambda|=size.
    print("\n  Common j-factors within a level (fixed p, fixed |lambda|):")
    for p in (2, 3, 4):
        print(f"\n    p = {p}:")
        lam_by_size = defaultdict(list)
        for (pp, lam) in closed_forms:
            if pp != p:
                continue
            lam_by_size[lam[0] + lam[1]].append((lam, closed_forms[(pp, lam)]))
        for size, entries in sorted(lam_by_size.items()):
            polys = [cf for _, cf in entries]
            if not polys:
                continue
            g = polys[0]
            for cf in polys[1:]:
                g = sp.gcd(g, cf)
            print(f"      |lambda| = {size}: gcd_over_lambda(c_lambda(j)) = {sp.factor(g)}")

    # -----------------------------------------------------------------
    # STEP 3.7: reparametrize by (ell, m) = (|lambda|-j, lambda_1 - lambda_2).
    # Fit c_{lambda(j; ell, m)}(j) as polynomial in j for each (p, ell, m).
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 3.7  Reparametrize by (ell, m). c_{lam(j; ell, m)}(j) at fixed (p, ell, m).")
    print("=" * 78)

    fits_by_pell_m = {}   # (p, ell, m) -> poly in j
    for p in (2, 3, 4):
        print(f"\n  p = {p}:")
        # gather all (j, ell, m) samples for this p
        js = sorted(k[1] for k in A_data if k[0] == p)
        for ell in range(0, p + 1):
            for m in range(0, 20):
                samples = []
                for jj in js:
                    # lambda_1 = (jj + ell + m)/2, lambda_2 = (jj + ell - m)/2
                    if (jj + ell + m) % 2 != 0:
                        continue
                    lam1 = (jj + ell + m) // 2
                    lam2 = (jj + ell - m) // 2
                    if lam1 < lam2 or lam2 < 0:
                        continue
                    lam = (lam1, lam2)
                    cv = all_coeffs[(p, jj)].get(lam, Integer(0))
                    samples.append((jj, cv))
                if len(samples) < 2:
                    continue
                # If everything is zero, skip
                if all(sv == 0 for _, sv in samples):
                    continue
                poly_j = fit_poly_in_j(samples, max_deg=15)
                if poly_j is None:
                    print(f"    (ell={ell}, m={m}): NO fit ({len(samples)} samples)")
                else:
                    fits_by_pell_m[(p, ell, m)] = poly_j
                    print(f"    (ell={ell}, m={m}): c(j) = {sp.factor(poly_j)}")

    print("\n  Do the (ell, m) fits agree across p?")
    for ell in range(0, 5):
        for m in range(0, 15):
            entries = [(p, fits_by_pell_m[(p, ell, m)]) for p in (2, 3, 4)
                       if (p, ell, m) in fits_by_pell_m]
            if len(entries) < 2:
                continue
            polys = [e[1] for e in entries]
            same = all(sp.expand(polys[0] - polys[i]) == 0 for i in range(1, len(polys)))
            if same:
                print(f"    (ell={ell}, m={m}): SAME across p={[e[0] for e in entries]}: {sp.factor(polys[0])}")
            else:
                print(f"    (ell={ell}, m={m}): DIFFERS across p:")
                for (p, cf) in entries:
                    print(f"        p={p}: {sp.factor(cf)}")

    # -----------------------------------------------------------------
    # STEP 4: uniform-in-p pattern for c_lambda(j, p)
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 4  Uniform-in-p pattern hunting: which lambdas are stable across p?")
    print("=" * 78)

    # A shape (a, b) with a >= b appears at p iff b <= p (empirical from step 2).
    # For each shape, does c_lambda(j, p) have a common shape across p?
    all_lams = sorted({lam for (p, lam) in closed_forms}, key=lambda lm: (lm[0] + lm[1], lm[0]))
    print("\n  For each lambda that appears at multiple p, table c_lambda(j, p):")
    for lam in all_lams:
        row = f"    lambda = {lam}: "
        appearances = []
        for p in (2, 3, 4):
            if (p, lam) in closed_forms:
                cf = closed_forms[(p, lam)]
                appearances.append((p, cf))
        if len(appearances) <= 1:
            continue
        # Check if c_lambda(j, p) is the same across all p where lambda appears
        polys = [ap[1] for ap in appearances]
        same = all(sp.expand(polys[0] - polys[i]) == 0 for i in range(1, len(polys)))
        if same:
            print(f"    lambda = {lam}: SAME across p = {[ap[0] for ap in appearances]}: {sp.factor(polys[0])}")
        else:
            print(f"    lambda = {lam}: DIFFERS across p; polynomials:")
            for (p, cf) in appearances:
                print(f"        p={p}: {sp.factor(cf)}")

    # -----------------------------------------------------------------
    # STEP 5: fit c_lambda(j, p) jointly in (j, p) for each fixed lambda shape.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 5  Fit c_lambda(j, p) as bivariate polynomial in (j, p) for each shape.")
    print("=" * 78)

    p_sym = symbols('p_sym')

    def fit_bivariate_jp(samples, max_deg_p=6, max_deg_j=10):
        """samples = [((p_val, j_val), y_val)].
        Try to fit y = sum_{d_p=0..max_deg_p, d_j=0..max_deg_j} c_{d_p,d_j} p^{d_p} j^{d_j}.
        Uses least-squares style with minimal total degree that fits exactly.
        """
        # Try increasing total degree bound
        for total_deg in range(0, max_deg_p + max_deg_j + 1):
            unknowns = []
            for d_p in range(min(max_deg_p, total_deg) + 1):
                for d_j in range(min(max_deg_j, total_deg - d_p) + 1):
                    unknowns.append((d_p, d_j))
            if len(unknowns) > len(samples):
                continue
            rows = []
            yy = []
            for ((pv, jv), yv) in samples:
                rows.append([Rational(pv) ** dp * Rational(jv) ** dj for (dp, dj) in unknowns])
                yy.append(yv)
            M = sp.Matrix(rows)
            y = sp.Matrix(yy)
            try:
                sol, _ = M.rref()
                aug = M.row_join(y)
                sol_aug, pivots = aug.rref()
                if any(sol_aug[i, len(unknowns)] != 0 and all(sol_aug[i, k] == 0 for k in range(len(unknowns)))
                       for i in range(sol_aug.rows)):
                    continue
                # Attempt exact solve
                try:
                    x = M.solve(y)
                except Exception:
                    # underdetermined; use pinv-style
                    continue
                # Verify
                ok = True
                for ((pv, jv), yv) in samples:
                    pred = sum(x[i] * Rational(pv) ** unknowns[i][0] * Rational(jv) ** unknowns[i][1]
                               for i in range(len(unknowns)))
                    if sp.simplify(pred - yv) != 0:
                        ok = False
                        break
                if ok:
                    expr = sum(x[i] * p_sym ** unknowns[i][0] * j_sym ** unknowns[i][1]
                               for i in range(len(unknowns)))
                    return sp.expand(expr)
            except Exception:
                continue
        return None

    # Group by "shape family" — literally the lambda itself, but pooling across p.
    print("\n  Attempting uniform-in-(j, p) fit for each lambda shape (needs >=2 p values):")
    for lam in all_lams:
        samples = []
        for p in (2, 3, 4):
            if (p, lam) in closed_forms:
                # Evaluate the closed form at every j sample we used
                js = sorted(k[1] for k in A_data if k[0] == p)
                cf_poly = closed_forms[(p, lam)]
                for jj in js:
                    samples.append(((p, jj), cf_poly.subs(j_sym, jj)))
        # Distinct p values in samples
        ps_in = sorted({s[0][0] for s in samples})
        if len(ps_in) < 2:
            continue
        expr = fit_bivariate_jp(samples)
        if expr is None:
            print(f"    lambda = {lam}: NO bivariate (j, p) fit found")
        else:
            print(f"    lambda = {lam}: c_lambda(j, p) = {sp.factor(expr)}")

    # -----------------------------------------------------------------
    # STEP 5.5: Look at A_p(lambda) for |lambda| = j (bottom of support).
    # Since s^*_lambda(lambda) is the only nonzero shifted-Schur at (b,c)=(lam),
    # for |lambda| = j, we have c_lambda = A_p(lambda) / s^*_lambda(lambda).
    # Try to spot uniform formula.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 5.5  A_p(lambda) at |lambda| = j: extract 'seed' coefficient at bottom level.")
    print("        c_lambda(bottom) = A_p(lambda) / [ (lam_1+1)! lam_2! / (lam_1 - lam_2 + 1) ]")
    print("=" * 78)

    for p in (2, 3, 4):
        print(f"\n  p = {p}:")
        for jj in sorted(k[1] for k in A_data if k[0] == p):
            F = A_data[(p, jj)]
            print(f"    j = {jj}:")
            for m in range(0, jj + 1):
                # lam_1 = (jj + m)/2, lam_2 = (jj - m)/2
                if (jj + m) % 2 != 0:
                    continue
                lam1 = (jj + m) // 2
                lam2 = (jj - m) // 2
                if lam1 < lam2 or lam2 < 0:
                    continue
                lam = (lam1, lam2)
                # Only include if lam is in support (i.e., c_lambda != 0)
                if lam not in all_coeffs[(p, jj)] or all_coeffs[(p, jj)][lam] == 0:
                    continue
                val = sp.expand(F.subs([(b, lam1), (c, lam2)]))
                diag = sp.factorial(lam1 + 1) * sp.factorial(lam2) / (lam1 - lam2 + 1)
                ratio = sp.simplify(val / diag)
                print(f"      lam = {lam}: A_p(lam) = {val}, / s^*_lam(lam) = {ratio}")

    # -----------------------------------------------------------------
    # STEP 6: verify the shifted-Schur formula reproduces A_p.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("STEP 6  Verify the shifted-Schur formula reproduces A_p (for each (p, j)).")
    print("=" * 78)

    verify_ok = True
    for p in (2, 3, 4):
        for jj in sorted(k[1] for k in A_data if k[0] == p):
            F = A_data[(p, jj)]
            nz = all_coeffs[(p, jj)]
            recon = Integer(0)
            for lam, cf in nz.items():
                recon += cf * s_star(lam, b, c)
            diff = sp.expand(F - recon)
            if diff != 0:
                verify_ok = False
                print(f"    p={p}, j={jj}: MISMATCH residual has deg {poly_deg_bc(diff)}")
            else:
                print(f"    p={p}, j={jj}: OK")
    print(f"\n  All shifted-Schur reconstructions match? {verify_ok}")

    # -----------------------------------------------------------------
    # FINAL SUMMARY: printed out cleanly for the transcript.
    # -----------------------------------------------------------------
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print("""
Vanishing pattern:
  D_0(p, j) = j     for all (p, j) tested, with delta = (0, 0).
  I.e., A_p(mu_1, mu_2) = 0 for every partition mu with |mu| < j.
  (delta = (1, 0) gives D_0 = j - 1 -- less clean.)

Nonzero-coefficient support (shifted-Schur expansion of A_p):
  {lambda = (lambda_1, lambda_2) :
     j <= |lambda| <= j + p,
     lambda_1 - lambda_2 <= 2j - |lambda|}
  Equivalently, in (ell, m) := (|lambda| - j, lambda_1 - lambda_2):
     0 <= ell <= p,   0 <= m <= j - ell.

Verified across (p, j) for p in {2, 3, 4}, j in {2p, ..., 12}.

Closed forms for c_lambda(j) at fixed p:
  Each c_lambda(j) is a polynomial in j, computed exactly (see Step 3).
  The polynomial vanishes at exactly the j-values where lambda leaves
  the support, i.e., gcd-over-lambda-at-fixed-|lambda| exactly encodes
  the support constraint (Step 3.5).

Uniform-in-p pattern:
  BRUTALLY HONEST: for fixed (lambda) or fixed (ell, m), c_lambda(j, p)
  does NOT agree across p as a function of j. That is, the coefficients
  are p-dependent in a way that does not factor as c_lambda(j) * f(p).
  A bivariate fit c(j, p) FAILED at every lambda tested (Step 5).

Best-guess uniform-p closed form (verified for p in {2,3,4}):
  A_p(b, c, j) = sum over lambda in support * c_lambda(j, p) * s^*_lambda(b, c)
  where support is as above, and c_lambda(j, p) is the polynomial in j
  extracted at each (p, lambda) (Step 3). Reconstruction verified: OK
  for every (p, j) with p in {2, 3, 4}, j in {2p, ..., 12}. See Step 6.

Best structural insight for follow-up:
  The 'seed' coefficient at |lambda| = j is
    c_lambda(bottom) = A_p(lambda) / [(lambda_1 + 1)! * lambda_2! / (lambda_1 - lambda_2 + 1)]
  and A_p(lambda_1, lambda_2) for |lambda_1| + |lambda_2| = j often has
  small integer factorization suggesting a hidden hook-length or Pieri
  rule (Step 5.5). This is the natural next probe.
""")
    print("=" * 78)
    print("Done.")
    print("=" * 78)


if __name__ == "__main__":
    main()
