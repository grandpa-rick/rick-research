"""(T) total-degree bound investigation — Day 111.

Target: (T) — Q_{2R}(a, b, c) has total (a, b)-degree <= 2R.

Verified empirically at R=2,3,4 (Day 110 note). This script:

  Part A. Compute Q_{2R} for R = 2, 3, (4, 5 if feasible) and extract:
          - a-deg, b-deg, total (a,b)-deg
          - top-(a,b)-degree part (as poly in a,b with c-coefs).

  Part B. Ansatz-difference check.
          Q_{2R}(a,b,c) - sum_{k=0}^{R} tilde_P_R^{(k)}(c) * (a+2)^k_falling * (b+1)^k_falling
          Is this identically zero (as polynomial in a, b, c)?

          Using Day-108 LC formula:
              LC(tilde_P_R^{(k)}) = (-1)^k C(2R,k) C(2R-k,k) k!

  Part C. Structural: extract H_c(a,b,j) top-(a,b)-degree component.
          Is it j-independent? If yes, alternating sum kills it -> deg drops.

  Symbolic computation: keep c symbolic where possible (uses ds_j/V symbolic
  in a, b, c). Concrete-c fits are the fallback.
"""
import sys
import time
from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, binomial, factorial

a, b, c = symbols('a b c')
x1, x2, x3 = a + 2, b + 1, c

OUT = []
def P(*s):
    line = ' '.join(str(x) for x in s)
    print(line, flush=True)
    OUT.append(line)


def fall(x, m):
    p = sp.Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def rise(x, L):
    p = sp.Integer(1)
    for i in range(L):
        p *= (x + i)
    return p


def det3(rows):
    (a11, a12, a13), (a21, a22, a23), (a31, a32, a33) = rows
    return (a11*(a22*a33 - a23*a32)
            - a12*(a21*a33 - a23*a31)
            + a13*(a21*a32 - a22*a31))


def bt(M):
    """Partition tables S_j with kappa multiplicities."""
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
    total = sp.Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def total_deg_ab(expr):
    if expr == 0:
        return -1
    pab = Poly(expr, a, b)
    max_td = 0
    for monom, coef in pab.terms():
        if coef == 0:
            continue
        td = sum(monom)
        if td > max_td:
            max_td = td
    return max_td


def a_deg(expr):
    if expr == 0:
        return -1
    return Poly(expr, a).degree()


def b_deg(expr):
    if expr == 0:
        return -1
    return Poly(expr, b).degree()


def top_ab_part(expr, tdeg):
    """Extract terms whose (a+b)-degree equals tdeg, as poly in a,b w/ c-coeffs."""
    if expr == 0:
        return sp.Integer(0)
    pab = Poly(expr, a, b)
    top = sp.Integer(0)
    for monom, coef in pab.terms():
        (da, db) = monom
        if da + db == tdeg:
            top += coef * a**da * b**db
    return expand(top)


# ---- Part A / C: symbolic (in c) pipeline via H_c ----
# The pipeline expression Q_{2R}(a, b, c) equals
#   h_{2R}(a, b, c) / [(a+3)_{c-1-2R} (b+2)_{c-1-2R}]
# but the Pochhammer lengths depend on integer c. To keep c symbolic, we
# work in the substitution c = c_val (integer) and observe polynomial-in-c
# behavior via multiple c-values, extracting Q top-degree parts.
#
# For the ANSATZ check, we can just build the ansatz symbolically (with
# tilde_P closed forms in c) and compare at multiple c-values.

def H_c_at(j, cv, dsV_cache):
    """H_c(a, b, j) at c = cv, symbolic a, b."""
    L = cv - j - 1
    if L < 0:
        raise ValueError(f"L < 0 at c={cv}, j={j}")
    poch_a = rise(a + 3, L)
    poch_b = rise(b + 2, L)
    dsjV_cv = dsV_cache[j].subs(c, cv)
    return expand(poch_a * poch_b * dsjV_cv)


def Q_2R_at(cv, twoR, dsV_cache):
    """Q_{2R}(a, b, cv)."""
    h = sp.Integer(0)
    for j in range(twoR + 1):
        sign = (-1) ** (twoR - j)
        coef = binomial(twoR, j)
        h += sign * coef * H_c_at(j, cv, dsV_cache)
    h = expand(h)
    L = cv - 1 - twoR
    if L < 0:
        return None
    denom = expand(rise(a + 3, L) * rise(b + 2, L))
    Q = expand(cancel(h / denom))
    check = expand(Q * denom - h)
    assert check == 0, f"Q*denom != h at cv={cv}"
    return Q


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
        P(f"  j={j}: total (a,b,c)-deg = {Poly(dsV_cache[j], [a, b, c]).total_degree()}, "
          f"(a,b)-deg = {tdeg_ab}  ({time.time()-t0:.2f}s)")
    return tables, dsV_cache


# =====================================================================
# PART A — total-degree of Q_{2R}(a,b,c)
# =====================================================================

def part_A_analysis(R, dsV_cache, cv_list):
    """For each cv in cv_list, compute Q_{2R}(a,b,cv), report degrees,
    extract top-ab-degree part."""
    P("\n" + "=" * 72)
    P(f"PART A: R = {R}, 2R = {2*R}. Q_{{2R}}(a,b,c) at c in {cv_list}")
    P("=" * 72)

    twoR = 2 * R
    tops = []  # (cv, top-ab-degree, top-part expr in a,b)
    for cv in cv_list:
        t0 = time.time()
        Q = Q_2R_at(cv, twoR, dsV_cache)
        if Q is None:
            P(f"  c = {cv}: L < 0 skip")
            continue
        da = a_deg(Q)
        db = b_deg(Q)
        dtot = total_deg_ab(Q)
        top = top_ab_part(Q, dtot)
        tops.append((cv, dtot, top))
        P(f"  c = {cv:2d}: a-deg={da}, b-deg={db}, total(a,b)-deg={dtot}, "
          f"({time.time()-t0:.2f}s)")
        P(f"         top_{{(a,b)}}(Q) = {expand(top)}")

    return tops


# =====================================================================
# PART B — ANSATZ DIFFERENCE CHECK
# =====================================================================
#
# tilde_P_R^{(k)} closed forms:
#   k = 0: P_0(c) = c(c-2R) * prod_{j=1..2R-1} (c-j)^2  (Day 109)
#   k = 1: P_1(c) = -2R(2R-1) * c * (c-1)^{↓(2R-2)} * (c-2)^{↓(2R-2)}  (Day 110)
#   k = R: P_R(c) = (-1)^R (2R)!  (leading term of ansatz, from LC formula)
#   general k: we know LC(tilde_P_R^{(k)}) = (-1)^k C(2R,k) C(2R-k,k) k!
#
# For R = 2:
#   k=0: c(c-4)(c-3)^2(c-2)^2(c-1)^2
#   k=1: -12 c(c-1)(c-2)^2(c-3)  [from R_1 formula: -2R(2R-1) = -12]
#   k=2: 12 c(c-1)  [Day 108 empirical / from R2-f2-verify]
#
# For R = 3:
#   k=0: c(c-6) prod_{j=1..5} (c-j)^2
#   k=1: -30 c(c-1)(c-2)^2(c-3)^2(c-4)^2(c-5)
#   k=2: [Day 108 empirical — need to fit or lookup]
#   k=3: [Day 108 empirical — need to fit or lookup]

def P0_of_R(R):
    p = c * (c - 2 * R)
    for j in range(1, 2 * R):
        p *= (c - j) ** 2
    return expand(p)


def P1_of_R(R):
    """tilde_P_R^{(1)}(c) = -2R(2R-1) c (c-1)^{↓ 2R-2} (c-2)^{↓ 2R-2}."""
    if R < 1:
        return sp.Integer(0)
    L = 2 * R - 2
    if L < 0:
        L = 0
    fall1 = sp.Integer(1)
    for i in range(L):
        fall1 *= (c - 1 - i)
    fall2 = sp.Integer(1)
    for i in range(L):
        fall2 *= (c - 2 - i)
    return expand(-2 * R * (2 * R - 1) * c * fall1 * fall2)


def falling(x, m):
    p = sp.Integer(1)
    for i in range(m):
        p *= (x - i)
    return p


def fit_Pk_from_slices(k_target, R, dsV_cache, cv_list, prev_Pks):
    """Extract tilde_P_R^{(k_target)}(c) by slicing Q_{2R} at (a, b) chosen
    appropriately and inverting via the ansatz. We use the following approach:

    Ansatz: Q_{2R}(a, b, c) = sum_{k=0}^{R} P_k(c) (a+2)_{↓k} (b+1)_{↓k}

    Choose (a, b) = (m - 2, m - 1) for m = 0, 1, ..., R. Then
      (a+2)_{↓k} |_{a = m-2} = m^{↓k} = m(m-1)...(m-k+1) = m!/(m-k)!  for k <= m
                             = 0 for k > m
    Same for (b+1)_{↓k} at b = m-1: m^{↓k}.

    So Q_{2R}(m-2, m-1, c) = sum_{k=0}^{m} P_k(c) * (m^{↓k})^2.

    In particular, at m = k_target: knowing P_0, ..., P_{k_target - 1} lets
    us solve for P_{k_target}(c):
        P_{k_target}(c) * (k_target!)^2 = Q_{2R}(k_target - 2, k_target - 1, c) -
                                          sum_{k < k_target} P_k(c) * (k_target^{↓k})^2

    We evaluate this at each cv, then fit a polynomial in c.
    """
    if k_target < 0:
        return sp.Integer(0)
    m = k_target
    a_val = m - 2
    b_val = m - 1
    twoR = 2 * R

    samples = []  # (cv, value of P_{k_target}(cv))
    for cv in cv_list:
        Q = Q_2R_at(cv, twoR, dsV_cache)
        if Q is None:
            continue
        Qval = Q.subs({a: a_val, b: b_val})
        # subtract known lower-P contributions
        contrib = sp.Integer(0)
        for k_lower, P_k in enumerate(prev_Pks):
            mfall = 1
            for i in range(k_lower):
                mfall *= (m - i)
            contrib += P_k.subs(c, cv) * mfall ** 2
        denom = 1
        for i in range(k_target):
            denom *= (k_target - i)  # k_target!
        denom = denom ** 2
        num = Qval - contrib
        assert (num / denom).is_rational or True  # allow polynomial evaluation
        # Should be exact integer division
        try:
            val = sp.simplify(num / denom)
        except Exception:
            val = num / denom
        samples.append((cv, sp.nsimplify(val)))

    # Now fit as polynomial in c. Total (a,b)-degree considerations say
    # tilde_P_R^{(k)} has c-degree <= 2(2R - k) (since each falling factor
    # (c-1)^{↓ 2R-2} has c-degree 2R-2, times c gives 2R-1, but multiplied
    # in ansatz total gives 4R - 2k, we'll fit up to 4R).
    max_deg = 4 * R + 2
    if len(samples) < max_deg + 1:
        P(f"    warning: only {len(samples)} samples, need >= {max_deg + 1}")

    # Try increasing degrees, take first that fits with holdout verification
    for D in range(max_deg + 1):
        if len(samples) < D + 2:
            break
        # Use first D+1 to fit, remaining to verify
        fit_s = samples[:D + 1]
        chk_s = samples[D + 1:]
        rows = []
        yy = []
        for cv, val in fit_s:
            rows.append([cv**i for i in range(D + 1)])
            yy.append(val)
        M = sp.Matrix(rows)
        y = sp.Matrix(yy)
        aug = M.row_join(y)
        rref, piv = aug.rref()
        if (aug.cols - 1) in piv:
            continue
        if len(piv) != D + 1:
            continue
        sol = [rref[piv.index(i), aug.cols - 1] for i in range(D + 1)]
        poly = sum(sol[i] * c**i for i in range(D + 1))
        poly = expand(poly)
        ok = True
        for (cv, val) in chk_s:
            if sp.simplify(poly.subs(c, cv) - val) != 0:
                ok = False
                break
        if ok:
            return poly
    return None


def part_B_ansatz_check(R, dsV_cache, cv_list):
    """
    Build ansatz sum, compare to Q_{2R}(a, b, c) at each cv in cv_list.
    Report: is diff = 0?
    """
    P("\n" + "=" * 72)
    P(f"PART B: Ansatz-difference check at R = {R}")
    P("=" * 72)

    twoR = 2 * R
    P(f"\nBuilding tilde_P_R^(k)(c) closed forms for R = {R}:")
    P_ks = []
    # k = 0: from Day 109
    P_0 = P0_of_R(R)
    P(f"  P_R^(0)(c) = {factor(P_0)}")
    P_ks.append(P_0)
    # k = 1: from Day 110
    P_1 = P1_of_R(R)
    P(f"  P_R^(1)(c) = {factor(P_1)}")
    P_ks.append(P_1)

    # k = 2..R: fit from Q slices
    for kt in range(2, R + 1):
        P(f"  Fitting P_R^({kt})(c) via slice (a,b) = ({kt-2}, {kt-1})...")
        Pk = fit_Pk_from_slices(kt, R, dsV_cache, cv_list, P_ks)
        if Pk is None:
            P(f"    FAILED to fit")
            return None
        P(f"    P_R^({kt})(c) = {factor(Pk)}")
        # Check leading coefficient against Day 108 formula
        deg_Pk = Poly(Pk, c).degree()
        lc = Poly(Pk, c).LC()
        expected_lc = ((-1)**kt) * comb(2*R, kt) * comb(2*R - kt, kt) * factorial(kt)
        P(f"    deg_c = {deg_Pk}, LC = {lc}, expected LC = {expected_lc}, "
          f"match? {lc == expected_lc}")
        P_ks.append(Pk)

    # Now check ansatz: Q_{2R}(a, b, cv) ?= sum_{k=0}^{R} P_k(cv) * (a+2)_{↓k}(b+1)_{↓k}
    P(f"\nCheck ansatz identity at each c in {cv_list}:")
    all_zero = True
    for cv in cv_list:
        Q = Q_2R_at(cv, twoR, dsV_cache)
        if Q is None:
            continue
        ansatz = sp.Integer(0)
        for k, Pk in enumerate(P_ks):
            ansatz += Pk.subs(c, cv) * falling(a + 2, k) * falling(b + 1, k)
        diff = expand(Q - ansatz)
        is_zero = (diff == 0)
        if not is_zero:
            all_zero = False
            # Report some info
            dtd = total_deg_ab(diff)
            P(f"  c = {cv:2d}: diff NONZERO! total (a,b)-deg = {dtd}")
            P(f"           first few diff terms: {str(diff)[:200]}")
        else:
            P(f"  c = {cv:2d}: diff = 0  (ansatz holds identically)")

    P(f"\nAnsatz identity Q_{{2R}} == sum_k P_k * (a+2)_↓k (b+1)_↓k holds at all "
      f"tested c? {all_zero}")
    if all_zero:
        P(">>> The ansatz appears IDENTICALLY TRUE.")
        P(">>> This means (T) is trivially implied by the ansatz (top-degree = 2R "
          "comes from k=R term, all others have degree <= 2R-2 or 2R).")
    return {'P_ks': P_ks, 'ansatz_true': all_zero}


# =====================================================================
# PART C — top-degree structure of H_c(a,b,j)
# =====================================================================
def part_C_structural(R, dsV_cache, cv):
    """Extract top-(a,b)-degree parts of H_c(a,b,j) for j=0..2R.
    Look for j-independent structure.

    H_c(a,b,j) = (a+3)_{c-1-j} (b+2)_{c-1-j} * (ds_j/V)

    In (a, b), (a+3)_{L} has a-degree L, top-part in a is a^L.
    Similarly (b+2)_{L} has b-degree L, top part in b is b^L.
    (ds_j/V) has some (a,b)-degree we can measure.

    top_{(a,b)}(H_c(a,b,j)) has (a,b)-degree = 2L + deg_{(a,b)}(ds_j/V)
                                             = 2(c-1-j) + D_j
    where D_j is (a,b)-degree of ds_j/V.

    For total degree of Q_{2R} to be 2R, need alternating sum of top parts
    to cancel down through many degrees.
    """
    P("\n" + "=" * 72)
    P(f"PART C: Top-(a,b)-degree of H_c(a,b,j) at c = {cv}, R = {R}, 2R = {2*R}")
    P("=" * 72)

    twoR = 2 * R
    # For each j = 0..2R, compute top-ab-degree part of H_c(a,b,j) at c = cv.
    H_tops = []
    H_polys = []
    for j in range(twoR + 1):
        L = cv - 1 - j
        if L < 0:
            P(f"  j = {j}: L = {L} < 0, skip")
            continue
        H = H_c_at(j, cv, dsV_cache)
        H = expand(H)
        tdeg = total_deg_ab(H)
        D_j = total_deg_ab(dsV_cache[j].subs(c, cv))  # (a,b)-deg of ds_j/V at c
        top = top_ab_part(H, tdeg)
        H_tops.append((j, tdeg, top))
        H_polys.append((j, H))
        P(f"  j = {j}: (a,b)-deg(H) = {tdeg}, (a,b)-deg(ds_j/V) = {D_j}, "
          f"L = {L}, 2L + D_j = {2*L + D_j}")

    # Check: is top part of H_c(a,b,j) j-INDEPENDENT?
    # (After factoring out the common leading form.)
    # top_{(a,b)}(H_c(a,b,j)) = coeff * a^{L_j + p_j} * b^{L_j + q_j}
    # where the (a+3)_L contributes a^L and (ds_j/V)|_top gives leading form
    # in a, b, c. We look at the top form as a poly in a, b (with c-coefs).

    P(f"\nTop parts:")
    top_forms = []
    for (j, tdeg, top) in H_tops:
        top_forms.append((j, tdeg, top))
        # Report just the top form (already in top).
        # Show reduced structure: as polynomial in a and b.
        pab = Poly(top, a, b)
        monoms = pab.terms()
        # Sort by (da, db) desc
        monoms_sorted = sorted(monoms, key=lambda m: (m[0][0], m[0][1]), reverse=True)
        top_lead_monom, top_lead_coef = monoms_sorted[0]
        P(f"  j = {j}: top has {len(monoms)} monomials, lead {top_lead_monom} coef = {top_lead_coef}")

    # Check whether all top parts have SAME (a,b)-degree
    tdegs = [tdeg for (_, tdeg, _) in H_tops]
    if len(set(tdegs)) > 1:
        P(f"\n  top (a,b)-degrees differ across j: {tdegs}")
        P(f"  So h_{{2R}} = alternating sum will have deg = max = {max(tdegs)}.")

    # Alternating sum of top parts at the top degree of the SUM's h_{2R}:
    # But h_{2R} degree is max of H degrees. The top of h_{2R} at that degree
    # comes only from H's that achieve the max.
    max_tdeg = max(tdegs)
    # For each j with tdeg = max_tdeg, take the top part and combine
    P(f"\nAlternating sum of top parts (at the max degree, then descending):")
    # We compute the top degrees of h_{2R} = sum_j (-1)^{2R-j} C(2R,j) H_c(a,b,j)
    # by repeatedly stripping top-degree.
    h = sp.Integer(0)
    for (j, H) in H_polys:
        sign = (-1) ** (twoR - j)
        cf = binomial(twoR, j)
        h += sign * cf * H
    h = expand(h)
    h_tdeg = total_deg_ab(h)
    L_final = cv - 1 - twoR
    denom_ab_deg = 2 * L_final  # (a+3)_{L} has a-deg L; product has a-deg L, b-deg L.
    Q_expected_tdeg = h_tdeg - denom_ab_deg
    P(f"  h_{{2R}} at c = {cv}: (a,b)-deg = {h_tdeg}")
    P(f"  denominator (a+3)_{{{L_final}}} (b+2)_{{{L_final}}}: (a,b)-deg = "
      f"{denom_ab_deg} (but denom is a * b factored — Q's deg is h_deg - denom_deg "
      f"IF exact division).")
    P(f"  Q_{{2R}}(a,b,c) at c = {cv}: (a,b)-deg = {h_tdeg - denom_ab_deg} (predicted)")
    P(f"  Target: 2R = {twoR}")
    ratio = h_tdeg - denom_ab_deg
    if ratio == twoR:
        P(f"  MATCHES 2R = {twoR}: (T) verified at c = {cv}, R = {R}.")
    else:
        P(f"  MISMATCH: predicted {ratio} != 2R = {twoR}")

    # How much cancellation happens?
    # max H_c(a,b,j) tdeg = 2(c-1) + max_j D_j
    max_H_tdeg = max(tdegs)
    max_D = max(total_deg_ab(dsV_cache[j].subs(c, cv)) for j in range(twoR + 1)
                if cv - 1 - j >= 0)
    max_H_predicted = 2 * (cv - 1) + max_D  # only for j = 0 which has L = c-1
    P(f"\n  Max H_c(a,b,j) (a,b)-deg = {max_H_tdeg}")
    P(f"  Sum cancels down to h_deg = {h_tdeg}, "
      f"a cancellation of {max_H_tdeg - h_tdeg}.")
    P(f"  Then division by denom drops another {denom_ab_deg} degrees to get Q_{{2R}}.")
    P(f"  Net Q_{{2R}} (a,b)-deg = {h_tdeg - denom_ab_deg} = 2R = {twoR}? "
      f"{h_tdeg - denom_ab_deg == twoR}")

    return {'H_tops': H_tops, 'Q_deg': h_tdeg - denom_ab_deg}


# =====================================================================
# MAIN
# =====================================================================

def main():
    P("=" * 72)
    P("(T) Total-degree bound investigation — Day 111")
    P("Target: Q_{2R}(a, b, c) has total (a, b)-degree <= 2R.")
    P("=" * 72)

    # Determine J_max: for R = 5 we'd want j up to 10. Let's start with R = 4.
    J = 10  # max j across our tests
    tables, dsV_cache = compute_dsV_up_to(J)

    all_results = {}

    # PART A: total-degree of Q_{2R} for R = 2, 3, 4, 5
    P("\n\n" + "#" * 72)
    P("# PART A: Total (a,b)-degree of Q_{2R}(a,b,c) for R = 2, 3, 4, 5")
    P("#" * 72)

    A_results = {}
    for R in [2, 3, 4, 5]:
        # cv_list: need c > 2R + 1 for L = c - 1 - 2R >= 1 (positive denom).
        cv_list = [2 * R + 2, 2 * R + 3, 2 * R + 4]
        try:
            t0 = time.time()
            tops = part_A_analysis(R, dsV_cache, cv_list)
            P(f"  ...total time R = {R}: {time.time() - t0:.1f}s")
            A_results[R] = tops
        except Exception as e:
            P(f"  R = {R} EXCEPTION: {e}")
            import traceback
            P(traceback.format_exc())
            A_results[R] = None

    all_results['A'] = A_results

    # PART B: Ansatz-difference check for R = 2, 3
    P("\n\n" + "#" * 72)
    P("# PART B: Ansatz-difference check for R = 2, 3")
    P("#" * 72)

    B_results = {}
    for R in [2, 3]:
        # Need enough cv values to fit each P_k(c). P_k has c-degree at most 4R - 2k
        # so worst case 4R for k=0. Use 4R + 5 samples starting at 2R + 2.
        n_samples = 4 * R + 5
        cv_list = [2 * R + 2 + i for i in range(n_samples)]
        try:
            t0 = time.time()
            res = part_B_ansatz_check(R, dsV_cache, cv_list)
            P(f"  ...total time R = {R}: {time.time() - t0:.1f}s")
            B_results[R] = res
        except Exception as e:
            P(f"  R = {R} EXCEPTION: {e}")
            import traceback
            P(traceback.format_exc())
            B_results[R] = None

    all_results['B'] = B_results

    # PART C: structural — top-degree of H_c(a,b,j)
    P("\n\n" + "#" * 72)
    P("# PART C: Structural analysis of H_c(a,b,j) top degrees")
    P("#" * 72)

    C_results = {}
    for R in [2, 3, 4]:
        cv = 2 * R + 2
        try:
            t0 = time.time()
            res = part_C_structural(R, dsV_cache, cv)
            P(f"  ...total time R = {R}: {time.time() - t0:.1f}s")
            C_results[R] = res
        except Exception as e:
            P(f"  R = {R} EXCEPTION: {e}")
            import traceback
            P(traceback.format_exc())
            C_results[R] = None

    all_results['C'] = C_results

    # FINAL SUMMARY
    P("\n\n" + "=" * 72)
    P("FINAL SUMMARY")
    P("=" * 72)

    P("\nPART A: total (a,b)-degree of Q_{2R}")
    for R in [2, 3, 4, 5]:
        tops = A_results.get(R)
        if tops is None:
            P(f"  R = {R}: FAILED")
            continue
        for (cv, tdeg, top) in tops:
            match = "OK" if tdeg == 2 * R else f"MISMATCH (expected {2*R})"
            P(f"  R = {R}, c = {cv}: total (a,b)-deg = {tdeg}  [{match}]")

    P("\nPART B: Ansatz identity check")
    for R in [2, 3]:
        res = B_results.get(R)
        if res is None:
            P(f"  R = {R}: FAILED")
            continue
        P(f"  R = {R}: ansatz identically true? {res['ansatz_true']}")

    P("\nPART C: top-degree cancellation")
    for R in [2, 3, 4]:
        res = C_results.get(R)
        if res is None:
            P(f"  R = {R}: FAILED")
            continue
        P(f"  R = {R}: Q_{{2R}} (a,b)-deg = {res['Q_deg']} (target 2R = {2*R})")

    out_path = "/home/agent/projects/beta-prime/code/2026-08-19-T-bound-investigation.txt"
    with open(out_path, 'w') as f:
        f.write('\n'.join(OUT))
    P(f"\nSaved log to {out_path}")


if __name__ == "__main__":
    main()
