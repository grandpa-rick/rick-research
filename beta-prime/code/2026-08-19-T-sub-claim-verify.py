"""Day 112: Verification of Sub-claim (**) for (T) total-degree bound.

Sub-claim (**): Consider H_c(a,b,j) = (a+3)_{c-1-j} (b+2)_{c-1-j} * (ds_j/V).
This is a polynomial in (a, b) of total degree 2(c-1) (top).
Expand by (a,b)-total-degree "layers": layer at total (a,b)-degree c-1-d ... wait,
top degree is 2(c-1), so layer at total (a,b)-degree 2(c-1) - d is "layer d down".
The coefficient of each specific monomial a^i b^{k} with i + k = 2(c-1) - d,
viewed as a function of j (with c fixed), is a polynomial in j of degree <= d.

Consequence: alternating sum sum_{j=0}^{2R} (-1)^{2R-j} C(2R, j) * (this coef)
vanishes for all d < 2R (finite differences of order 2R kill polys of degree < 2R).
So h_{2R} has (a, b)-degree at most 2(c-1) - 2R = 2c - 2 - 2R.
Dividing by (a+3)_{c-1-2R}(b+2)_{c-1-2R} (which has (a,b)-degree 2(c-1-2R) = 2c-2-4R)
gives Q_{2R} with (a,b)-degree at most 2R.

STRATEGY: fix c = C_0 (a specific large integer, say 25) so all Pochhammer factors
are actually integer-length. For each R in {2, 3, 4, 5}, for each j = 0, ..., 2R,
compute H_c(a, b, j) as a polynomial in a, b (integer c). Group monomials by
total (a,b)-degree; for each fixed monomial slot (i, k) with i + k = 2(c-1) - d,
record the value of the coefficient. Then, varying j = 0, ..., 2R (or a wider
range), fit that as a polynomial in j and report the j-degree.

We report the j-degree of every slot (d, i) for d in 0..2R (and up to some slack).
Expected: j-degree <= d.

For robustness we do this at c = 15 and c = 20, and compare.
"""
import sys
import time
from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, binomial, factorial, Integer

a, b, c = symbols('a b c')
jsym = symbols('j')
x1, x2, x3 = a + 2, b + 1, c

OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


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
    """Partition tables S_j with kappa multiplicities (Day 108-111 recipe)."""
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


def ds(j, tables):
    xs = (x1, x2, x3)
    total = Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def compute_dsV_up_to(J):
    P(f"Building partition tables up to j = {J}...")
    t0 = time.time()
    tables = bt(J)
    P(f"  built in {time.time() - t0:.2f}s")

    dsV_cache = {}
    V = ds(0, tables)
    P(f"V = ds_0 = {factor(V)}")
    P(f"\nComputing ds_j/V for j = 0..{J} (symbolic in a,b,c):")
    for j in range(J + 1):
        t0 = time.time()
        dsj = ds(j, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0, f"ds_{j}/V not divisible"
        dsV_cache[j] = q.as_expr()
        pab = Poly(dsV_cache[j], a, b)
        tdeg_ab = max((sum(m) for m, cf in pab.terms() if cf != 0), default=0)
        pabc = Poly(dsV_cache[j], [a, b, c])
        tdeg_abc = pabc.total_degree() if dsV_cache[j] != 0 else 0
        P(f"  j={j}: total (a,b,c)-deg = {tdeg_abc}, (a,b)-deg = {tdeg_ab}"
          f"  ({time.time()-t0:.2f}s)")
    return tables, dsV_cache


def compute_dsV_at_c(J, cv):
    """Alternative: substitute c = cv EARLY, do division in Q[a,b]. Much faster."""
    P(f"Building partition tables up to j = {J}...")
    t0 = time.time()
    tables = bt(J)
    P(f"  built in {time.time() - t0:.2f}s")

    dsV_at_c = {}
    # V at c = cv:
    V_symb = ds(0, tables)
    V_cv = expand(V_symb.subs(c, cv))
    P(f"V at c={cv}: {factor(V_cv)}")
    P(f"\nComputing ds_j/V at c={cv} for j = 0..{J}:")
    xs_cv = (a + 2, b + 1, Integer(cv))
    for j in range(J + 1):
        t0 = time.time()
        total = Integer(0)
        for mu, kap in tables[j]:
            ks = [mu[col] + (2 - col) for col in range(3)]
            rows = [[fall(xs_cv[i], ks[col]) for col in range(3)] for i in range(3)]
            total += kap * det3(rows)
        dsj_cv = expand(total)
        # divide by V_cv in Q[a, b]
        if dsj_cv == 0:
            dsV_at_c[j] = Integer(0)
        else:
            q, r = sp.div(Poly(dsj_cv, [a, b]), Poly(V_cv, [a, b]))
            assert r.as_expr() == 0, f"ds_{j}/V not divisible at c={cv}"
            dsV_at_c[j] = q.as_expr()
        pab = Poly(dsV_at_c[j], a, b) if dsV_at_c[j] != 0 else None
        tdeg_ab = max((sum(m) for m, cf in pab.terms() if cf != 0), default=0) if pab else 0
        P(f"  j={j}: (a,b)-deg = {tdeg_ab}  ({time.time()-t0:.2f}s)")
    return tables, dsV_at_c


# ------------------------------------------------------------------------
# H_c at integer c, symbolic a, b
# ------------------------------------------------------------------------
def H_c_at(j, cv, dsV_cache_at_c):
    """H_c(a, b, j) at c = cv (integer), symbolic a, b.
    dsV_cache_at_c[j] is already substituted at c = cv (a poly in a, b only)."""
    L = cv - j - 1
    if L < 0:
        raise ValueError(f"L < 0 at c={cv}, j={j}")
    poch_a = rise(a + 3, L)
    poch_b = rise(b + 2, L)
    dsjV_cv = dsV_cache_at_c[j]
    return expand(poch_a * poch_b * dsjV_cv)


def layer_coeffs(H, tot_deg):
    """Return dict {(i, k) : coef} for monomials a^i b^k with i + k = tot_deg."""
    if H == 0:
        return {}
    pab = Poly(H, a, b)
    out = {}
    for monom, coef in pab.terms():
        (da, db) = monom
        if da + db == tot_deg:
            out[(da, db)] = coef
    return out


def j_degree_of_samples(samples):
    """Given list of (j_val, y_val), fit polynomial in j and return its degree.

    Uses exact rational fit. Returns -1 if all samples zero. Otherwise returns
    the smallest D such that a polynomial of degree D matches all samples.
    """
    # Filter out samples with y=0 to detect the true polynomial degree, but
    # we need all samples matched.
    if all(s[1] == 0 for s in samples):
        return -1
    n = len(samples)
    # Try D = 0, 1, ..., n-1.
    for D in range(n):
        # Fit a polynomial of degree D through the first D+1 samples,
        # check if it matches the rest.
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
        # Check remaining samples.
        ok = True
        for (jv, yv) in samples[D + 1:]:
            pred = sum(sol[i] * jv ** i for i in range(D + 1))
            if sp.simplify(pred - yv) != 0:
                ok = False
                break
        if ok:
            # And check that the leading coefficient is nonzero (so degree truly D).
            if D == 0 or sp.simplify(sol[D]) != 0:
                return D
            # else it was really degree < D — but we would have caught that
            # at smaller D. So this shouldn't happen given the loop order.
    return None  # doesn't fit — should not happen with enough samples


# =====================================================================
# Sub-claim (**) verification
# =====================================================================
def verify_sub_claim(R, cv, dsV_cache, extra_j_slack=2):
    """For each d = 0, 1, ..., 2R + extra_j_slack, look at the (a, b)-layer
    of H_c(a, b, j) at total degree TOP - d, where TOP = 2(c-1).
    For each monomial slot (i, k) with i + k = TOP - d, extract coef as a
    function of j = 0, 1, ..., 2R + extra_j_slack + something and fit as
    a polynomial in j. Report the j-degree per (d, i) slot.

    Expected: j-degree <= d.
    """
    P("\n" + "=" * 72)
    P(f"Sub-claim (**) verification: R = {R}, c = {cv}")
    P("=" * 72)

    twoR = 2 * R
    TOP = 2 * (cv - 1)
    # We need j values 0, 1, ..., 2R, but to fit a polynomial in j of
    # potentially large degree we need extra samples. Fit degree up to
    # 2R + slack. So we take j = 0, 1, ..., 2R + slack.
    #
    # For j > c - 1, L < 0 so H_c isn't defined; but we require c >= 2R + 2
    # so L = c - 1 - j >= 0 for j <= c - 1. That gives many samples.
    #
    # To robustly detect j-degree up to ~ 2R + slack we take J_max = 2R + slack + slack.
    J_max = min(twoR + 2 * extra_j_slack + 4, cv - 1)
    P(f"Sampling j in [0, {J_max}] to fit poly-in-j up to degree ~ {J_max}.")
    P(f"TOP = 2(c-1) = {TOP}. Layers d in [0, {twoR + extra_j_slack}].")

    # Compute H_c(a, b, j) for each j.
    Hcache = {}
    for jv in range(J_max + 1):
        t0 = time.time()
        Hcache[jv] = H_c_at(jv, cv, dsV_cache)
        # No print — too much output.

    # For each d in [0, 2R + extra_j_slack], gather coeffs as functions of j.
    results = {}  # (d, i, k) -> (j-degree, samples)
    for d in range(twoR + extra_j_slack + 1):
        tot_deg = TOP - d
        # Slots (i, k) with i + k = tot_deg, i in [0, min(tot_deg, some bound)]
        # We need a, b individually bounded. But a^i * b^k with i in [0, tot_deg].
        # Actually top (a, b)-degree can be as low as 0 in a and as high as tot_deg in a.
        # We only test slots that ever appear (nonzero at some j).
        slot_present = set()
        slot_samples = defaultdict(list)  # (i, k) -> [(j, coef)]
        for jv in range(J_max + 1):
            H = Hcache[jv]
            slots = layer_coeffs(H, tot_deg)
            for (i, k), cf in slots.items():
                slot_present.add((i, k))
        # Now collect samples for each slot, even if 0 (since 0 might mean
        # the polynomial vanishes at that j).
        for (i, k) in sorted(slot_present, reverse=True):
            for jv in range(J_max + 1):
                slots = layer_coeffs(Hcache[jv], tot_deg)
                cf = slots.get((i, k), Integer(0))
                slot_samples[(i, k)].append((jv, cf))

        # For each slot, fit j-degree
        max_jdeg_in_layer = -1
        layer_details = []
        for (i, k) in sorted(slot_present, reverse=True):
            samples = slot_samples[(i, k)]
            jd = j_degree_of_samples(samples)
            layer_details.append((i, k, jd))
            if jd is not None and jd > max_jdeg_in_layer:
                max_jdeg_in_layer = jd
            results[(d, i, k)] = (jd, samples)

        # Report per layer
        status = "OK" if max_jdeg_in_layer <= d else "!!VIOLATION!!"
        P(f"\n  d = {d}: layer (a,b)-deg = {tot_deg}. "
          f"max j-deg over slots = {max_jdeg_in_layer} (expect <= d = {d}) [{status}]")
        # Show detail: (i, k) -> jdeg
        # Group by j-degree buckets for compactness
        by_jdeg = defaultdict(list)
        for (i, k, jd) in layer_details:
            by_jdeg[jd].append((i, k))
        for jd in sorted(by_jdeg.keys(), key=lambda x: (x is None, x)):
            slots_here = by_jdeg[jd]
            slot_repr = ', '.join(f"({i},{k})" for (i, k) in slots_here[:6])
            more = f", +{len(slots_here) - 6} more" if len(slots_here) > 6 else ""
            P(f"      j-deg = {jd}: {len(slots_here)} slots [{slot_repr}{more}]")

    return results


# =====================================================================
# Verify ds_j/V (a,b)-degree bound = 2j
# =====================================================================
def verify_dsV_ab_degree(dsV_cache_at_c, J_max):
    """Confirm (a,b)-degree of ds_j/V is <= 2j (in fact exactly 2j for j >= 1)."""
    P("\n" + "=" * 72)
    P("Sanity: (a,b)-degree of ds_j/V (at c fixed)")
    P("=" * 72)
    for j in range(J_max + 1):
        dsV = dsV_cache_at_c[j]
        if dsV == 0:
            P(f"  j={j}: ds_j/V = 0")
            continue
        pab = Poly(dsV, a, b)
        tdeg = max((sum(m) for m, cf in pab.terms() if cf != 0), default=-1)
        expected = 2 * j
        status = "OK" if tdeg <= 2 * j else "!!"
        P(f"  j={j}: (a,b)-deg = {tdeg} (expect <= 2j = {expected}) [{status}]")


# =====================================================================
# Also verify Sub-claim (**) for ds_j/V directly (finer version)
# =====================================================================
def verify_dsV_layer_jdegree(dsV_cache_at_c, R, cv, extra_slack=3):
    """For ds_j/V at c = cv fixed, the layer at (a,b)-degree 2j - r should have
    coefficients that are polynomials in j of degree <= r.

    Wait — this is subtle. The (a,b)-degree of ds_j/V DEPENDS on j (it's <= 2j).
    So "layer at (a,b)-degree 2j - r" is a MOVING TARGET as j varies. We can't
    compare directly across j like the H_c version.

    Alternative: for each (i, k) fixed, coef of a^i b^k in ds_j/V (at c = cv)
    is a polynomial in j of some degree. Question: how does that degree grow
    as (i, k) varies, and does it match the (**) prediction?

    (**) sub-claim: layer at (a,b)-total = 2j - r in ds_j/V has j-degree <= r.
    So slot (i, k) with i + k = 2j - r has j-degree <= r = 2j - (i + k).
    But j varies! For fixed (i, k), as j increases from ceil((i+k)/2) upward,
    the "r" value is r = 2j - (i + k), which itself grows with j. So the
    j-degree bound "2j - (i+k)" grows unboundedly.

    So statement is really: for fixed r >= 0, the top-degree part in a,b of
    ds_j/V minus the r-th shell gives a polynomial in (a, b, j) whose j-degree
    in each layer is bounded by r.

    That is: for each r, define P_r(a, b, j) := [layer (a,b)-deg = 2j - r of ds_j/V].
    Then P_r is a polynomial in (a, b, j) of j-degree <= r (as a polynomial in j
    with coefficients in (a, b)-monomials).

    We test this. For each j, extract the layer at (a,b)-degree 2j - r. Then
    compare across j.
    """
    P("\n" + "=" * 72)
    P(f"Verify ds_j/V shell layer j-degree at c = {cv}")
    P(f"For each r in [0, {2 * R + extra_slack}], j varies")
    P("=" * 72)

    twoR = 2 * R
    J_max = min(twoR + 2 * extra_slack + 4, cv - 1)
    dsV_at_c = dsV_cache_at_c  # already at c = cv

    for r in range(2 * R + extra_slack + 1):
        # For each j, the layer at (a,b)-deg = 2j - r; only makes sense for j >= ceil(r/2)
        min_j = (r + 1) // 2  # ensures 2j - r >= 0 and layer possibly nonempty
        # Actually we want 2j - r >= 0 => j >= r/2 => j >= ceil(r/2).
        # And we need j >= 1 for layers to be sensible (j=0 has ds_0/V = 1).
        j_range = list(range(max(min_j, 0), J_max + 1))
        if len(j_range) < 3:
            P(f"  r = {r}: too few j samples ({len(j_range)}), skip.")
            continue

        # For each j, extract the layer at 2j - r. Slots (i, k) with i + k = 2j - r.
        # But slots differ across j! We need to track slots as (i, k).
        # Only slots (i, k) common to all j (or at least present at multiple j)
        # can be tracked.
        # Alternative: pick specific i values, say i = 0, 1, ..., r (small).
        # For slot (i, 2j - r - i), coef varies with j because k depends on j.
        # This makes cross-j comparison hard.
        #
        # BETTER: parameterize by (r, delta) where delta = k - (top-b for that r-shell)?
        # Actually the RIGHT thing is: for each shell r, define
        #     phi_r(alpha, beta, j) := coef of a^alpha b^beta in [layer (a,b)-deg=2j-r of ds_j/V]
        # with alpha in [0, 2j - r]. But alpha + beta = 2j - r.
        # As j varies, beta = 2j - r - alpha varies. So the natural variable is not (i, k)
        # but rather... some slot-in-shell coordinate.
        #
        # But wait: for fixed alpha (small), beta grows linearly in j. So the "slot" is
        # really a function on shells parameterized by alpha.
        #
        # Let's just record: for each alpha in [0, ..., min(2j-r for all j)], take
        # the coef of a^alpha b^{2j-r-alpha} at each j. Fit as poly in j.
        # The claim is that this poly has j-degree <= r.
        # But actually this claim needs care — the coef DEPENDS on which b^power we take,
        # and different powers give different polynomials!
        #
        # Rick's Sub-claim (**) says: the layer AT (a,b)-total = 2j - r has coefficients
        # (as functions of j) that are polynomials of j-degree <= r. Since the layer is
        # a polynomial in (a, b), and "coefficient" here should mean the coefficient of
        # each monomial in that layer, viewed as a function of j (with c fixed).
        #
        # So: pick specific monomials a^i b^k. For each such (i, k), compute at each j
        # the coefficient. This coefficient is nonzero only for j such that i + k <= 2j
        # (i.e., the layer at 2j-r for some r <= 2j - i - k reaches this monomial).
        # For j large, this monomial is well inside ds_j/V. The claim is about the
        # TOP layer of ds_j/V, which is different.
        #
        # OK: I'll do it the intuitive way. For a fixed (i, k) with i + k = 2j0 - r for
        # some reference j0, we can't compare across j directly. So let's use the
        # H_c approach as the canonical test: coefficients of a^i b^k in H_c(a,b,j)
        # at fixed monomial slot vary with j as polynomials — that's the main test.
        #
        # But we can ALSO do the following for ds_j/V: pick "diagonal" slot alpha for
        # each j: coef of a^{alpha} b^{2j - r - alpha}. Fit vs j.
        #
        # This is a heuristic. Let's do it.
        min_span = min(2 * jv - r for jv in j_range if 2 * jv - r >= 0)
        if min_span < 0:
            continue
        max_alpha = min(min_span, 3)  # small alpha
        for alpha in range(max_alpha + 1):
            samples = []
            for jv in j_range:
                k_needed = 2 * jv - r - alpha
                if k_needed < 0:
                    continue
                slots = layer_coeffs(dsV_at_c[jv], 2 * jv - r)
                cf = slots.get((alpha, k_needed), Integer(0))
                samples.append((jv, cf))
            if len(samples) < 2:
                continue
            jd = j_degree_of_samples(samples)
            status = "OK" if (jd is not None and jd <= r) else ("empty" if jd == -1 else "!!")
            P(f"  r = {r}, alpha = {alpha}: j-deg (slot a^{alpha} b^{{2j-r-alpha}}) = {jd}"
              f" (expect <= r = {r}) [{status}]")


# =====================================================================
# Alternative "cheap" proof exploration
# =====================================================================
def explore_alternative(dsV_cache_at_c):
    """
    Alternative approach: check the top part of (ds_j/V) in (a,b), which is
    the Schur specialization at mu = (j, j, 0): s^*_{(j,j,0)}(a+2, b+1, c).
    """
    P("\n" + "=" * 72)
    P("Exploration: structure of top (a,b) part of ds_j/V (at c fixed)")
    P("=" * 72)
    for jv in range(1, 6):
        dsV = dsV_cache_at_c[jv]
        # Compute (a,b)-top part at symbolic c
        pab = Poly(dsV, a, b)
        max_td = max((sum(m) for m, cf in pab.terms() if cf != 0), default=0)
        top = Integer(0)
        for monom, coef in pab.terms():
            (da, db) = monom
            if da + db == max_td:
                top += coef * a ** da * b ** db
        P(f"  j = {jv}: (a,b)-top-deg = {max_td} = 2j = {2*jv}? {max_td == 2*jv}")
        P(f"    top: {factor(expand(top))}")


# =====================================================================
# MAIN
# =====================================================================
def main():
    P("=" * 72)
    P("Day 112: Sub-claim (**) verification for (T) total-degree bound")
    P("=" * 72)

    # Choose c = 25 to give a healthy TOP = 2(c-1) = 48. Need c-1 >= J_max.
    # For R=5 with slack=2 we sample j up to 2*5 + 2*2 + 4 = 18.
    C_VAL = 25

    J_max = 2 * 5 + 2 * 2 + 4  # covers R = 5, extra_slack = 2
    tables, dsV_at_c = compute_dsV_at_c(J_max, C_VAL)

    # Sanity
    verify_dsV_ab_degree(dsV_at_c, J_max)

    # Explore structure
    explore_alternative(dsV_at_c)

    # Verify sub-claim (**) for R = 2, 3, 4, 5
    all_results = {}
    for R in [2, 3, 4, 5]:
        t0 = time.time()
        slack = 2
        try:
            res = verify_sub_claim(R, C_VAL, dsV_at_c, extra_j_slack=slack)
            all_results[R] = res
        except Exception as e:
            P(f"  R = {R} EXCEPTION: {e}")
            import traceback
            P(traceback.format_exc())
            all_results[R] = None
        P(f"  ...time R = {R}: {time.time() - t0:.1f}s")

    # ALSO do the ds_j/V shell test
    verify_dsV_layer_jdegree(dsV_at_c, 4, C_VAL, extra_slack=3)

    # Summary
    P("\n\n" + "=" * 72)
    P("SUMMARY: Sub-claim (**) status")
    P("=" * 72)
    for R in [2, 3, 4, 5]:
        res = all_results.get(R)
        if res is None:
            P(f"  R = {R}: FAILED (exception)")
            continue
        # Aggregate max j-deg per d.
        by_d = defaultdict(int)
        violations = 0
        total_slots = 0
        for (d, i, k), (jd, _) in res.items():
            total_slots += 1
            eff_jd = jd if (jd is not None and jd >= 0) else 0
            by_d[d] = max(by_d[d], eff_jd)
            if jd is not None and jd > d:
                violations += 1
        maxd = max(by_d.keys()) if by_d else 0
        P(f"  R = {R}: {total_slots} slots checked. "
          f"per-d max j-deg: {[by_d[d] for d in range(maxd + 1)]}. "
          f"violations (jd > d): {violations}")

    out_path = "/home/agent/projects/beta-prime/code/2026-08-19-T-sub-claim-verify.txt"
    with open(out_path, 'w') as f:
        f.write('\n'.join(OUT))
    P(f"\nSaved log to {out_path}")


if __name__ == "__main__":
    main()
