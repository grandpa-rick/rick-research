"""Day 112: Verification of (T-a) 1D degree bound.

Statement (T-a): deg_a Q_{2R}(a, b, c) <= R for all R >= 1.

Where Q_{2R}(a, b, c) = h_{2R}(a, b, c) / [(a+3)_{c-1-2R} (b+2)_{c-1-2R}]
and h_{2R}(a, b, c) = sum_{j=0}^{2R} (-1)^{2R-j} C(2R, j) H_c(a, b, j)
and H_c(a, b, j) = (a+3)_{c-1-j} (b+2)_{c-1-j} * (ds_j / V).

Mechanism: (T-a) via alternating-sum finite-difference annihilation.

STEP 1: Verify deg_a(ds_j / V) <= j for all j (fixed c).

STEP 2: Verify that for each d in [0, 2R], the coefficient
        [a^{c-1-d}] H_c(a, b, j) (a polynomial in b) has, at each fixed
        b-monomial slot, j-degree <= d.

STEP 3: By Lemma A (finite-difference annihilation): the alternating sum
        Sum_{j} (-1)^{2R-j} C(2R,j) [a^{c-1-d}] H_c(., j)  vanishes for d < 2R.
        So deg_a h_{2R} <= c - 1 - 2R.

STEP 4: Since h_{2R} = (a+3)_{c-1-2R} (b+2)_{c-1-2R} * Q_{2R}, and (a+3)_{c-1-2R}
        has a-degree exactly c-1-2R, dividing gives deg_a Q_{2R} <= 0.
        WAIT - this contradicts empirical deg_a Q_{2R} = R (empirically observed).

Hmm, so either
  (a) empirical deg_a Q_{2R} = R (from Day 111), and my finite-difference
      argument is TOO STRONG and gives deg = 0 which contradicts;
  (b) or the sub-claim "j-deg <= d" is actually LARGER than d;
  (c) etc.

Let me RESAMPLE carefully with fresh code (fixing a bug where dsV was
precomputed at one c value but reused at another).

Direct approach: for each (R, c), compute Q_{2R} and h_{2R} FROM SCRATCH at
that c value. Then verify deg_a Q_{2R} = R and deg_a h_{2R} = c - R - 1.
"""
import sys
import time
from collections import defaultdict
from itertools import combinations
from math import comb

import sympy as sp
from sympy import symbols, factor, expand, simplify, Poly, cancel, binomial, factorial, Integer

a, b, c = symbols('a b c')
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
    """ds_j as polynomial in (a, b, c)."""
    xs = (x1, x2, x3)
    total = Integer(0)
    for mu, kap in tables[j]:
        ks = [mu[col] + (2 - col) for col in range(3)]
        rows = [[fall(xs[i], ks[col]) for col in range(3)] for i in range(3)]
        total += kap * det3(rows)
    return expand(total)


def compute_dsV_symbolic(J, tables, cache):
    """Compute ds_j/V symbolically in (a, b, c). Cache is mutable dict."""
    V = ds_symbolic(0, tables)
    if 0 not in cache:
        cache['V'] = V
    for j in range(J + 1):
        if j in cache:
            continue
        dsj = ds_symbolic(j, tables)
        q, r = sp.div(Poly(dsj, [a, b, c]), Poly(V, [a, b, c]))
        assert r.as_expr() == 0
        cache[j] = q.as_expr()


def H_c_symbolic_at(j, cv, dsV_sym_cache):
    """H_c(a, b, j) at c = cv (integer), a, b symbolic.
    Uses dsV symbolic in (a, b, c), then substitutes c = cv."""
    L = cv - j - 1
    if L < 0:
        raise ValueError(f"L < 0")
    poch_a = rise(a + 3, L)
    poch_b = rise(b + 2, L)
    dsjV_cv = dsV_sym_cache[j].subs(c, cv)
    return expand(poch_a * poch_b * dsjV_cv)


def Q_2R_at(cv, twoR, dsV_sym_cache):
    h = Integer(0)
    for j in range(twoR + 1):
        sign = (-1) ** (twoR - j)
        cf = binomial(twoR, j)
        h += sign * cf * H_c_symbolic_at(j, cv, dsV_sym_cache)
    h = expand(h)
    L = cv - 1 - twoR
    if L < 0:
        return None, None
    denom = expand(rise(a + 3, L) * rise(b + 2, L))
    Q = expand(cancel(h / denom))
    check = expand(Q * denom - h)
    assert check == 0
    return h, Q


def a_coef_layer(H, a_power):
    """Extract coefficient of a^{a_power} in H, as polynomial in b."""
    if H == 0:
        return Integer(0)
    pab = Poly(H, a, b)
    result = Integer(0)
    for (da, db), cf in pab.terms():
        if da == a_power:
            result += cf * b ** db
    return result


def j_degree_of_samples(samples):
    if all(sp.simplify(s[1]) == 0 for s in samples):
        return -1
    n = len(samples)
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
            if D == 0 or sp.simplify(sol[D]) != 0:
                return D
    return None


# =====================================================================
# STEP 1: a-degree of ds_j/V
# =====================================================================
def step1_verify_dsV_a_degree(dsV_sym_cache, J_max):
    P("\n" + "=" * 72)
    P("STEP 1: a-degree of ds_j/V (symbolic in c) — expect <= j.")
    P("=" * 72)
    ok = True
    for j in range(J_max + 1):
        dsV = dsV_sym_cache[j]
        if dsV == 0:
            P(f"  j={j}: ds_j/V = 0")
            continue
        # a-degree of a polynomial in (a, b, c). Take max a-degree.
        pabc = Poly(dsV, [a, b, c])
        adeg = 0
        for monom, cf in pabc.terms():
            if cf != 0 and monom[0] > adeg:
                adeg = monom[0]
        expected = j
        status = "OK" if adeg <= j else "!!VIOLATION!!"
        if adeg > j:
            ok = False
        P(f"  j={j}: a-deg = {adeg} (expect <= j = {expected}) [{status}]")
    return ok


# =====================================================================
# STEP 2: j-degree of a-layers of H_c
# =====================================================================
def step2_verify_a_layer_j_degree(cv, dsV_sym_cache, R_max):
    """For each d in [0, 2*R_max], look at [a^{c-1-d}] H_c(a, b, j)
    (a polynomial in b with c-fixed at cv).
    For each monomial in b, coefficient is a polynomial in j. Report its j-degree.
    Claim: j-degree <= d.
    """
    P("\n" + "=" * 72)
    P(f"STEP 2: j-degree of a-layer [a^(c-1-d)] H_c(a,b,j) at c={cv}")
    P(f"        for d = 0, 1, ..., {2 * R_max}. Claim: j-degree <= d.")
    P("=" * 72)

    twoR_max = 2 * R_max
    slack = 3
    J_max = min(twoR_max + slack, cv - 1)
    P(f"Sampling j in [0, {J_max}] for polynomial-in-j fits.")

    Hcache = {}
    for jv in range(J_max + 1):
        Hcache[jv] = H_c_symbolic_at(jv, cv, dsV_sym_cache)

    per_d_max_jdeg = {}
    violations_per_d = {}
    all_ok = True
    for d in range(twoR_max + 1):
        a_power = cv - 1 - d
        if a_power < 0:
            continue
        b_slots_present = set()
        for jv in range(J_max + 1):
            L = a_coef_layer(Hcache[jv], a_power)
            if L == 0:
                continue
            pb = Poly(L, b)
            for (db,), cf in pb.terms():
                b_slots_present.add(db)

        max_jdeg = -1
        violations = 0
        details = []
        for bslot in sorted(b_slots_present):
            samples = []
            for jv in range(J_max + 1):
                L = a_coef_layer(Hcache[jv], a_power)
                if L == 0:
                    samples.append((jv, Integer(0)))
                else:
                    pb = Poly(L, b)
                    cf = Integer(0)
                    for (db,), c_ in pb.terms():
                        if db == bslot:
                            cf = c_
                            break
                    samples.append((jv, cf))
            jd = j_degree_of_samples(samples)
            details.append((bslot, jd))
            if jd is not None and jd > max_jdeg:
                max_jdeg = jd
            if jd is not None and jd > d:
                violations += 1
                all_ok = False
        per_d_max_jdeg[d] = max_jdeg
        violations_per_d[d] = violations
        status = "OK" if violations == 0 else f"!!{violations} VIOLATIONS!!"
        P(f"  d = {d}: a-power = {a_power}. b-slots: {len(b_slots_present)}. "
          f"max j-deg = {max_jdeg} (expect <= d = {d}) [{status}]")

    return per_d_max_jdeg, violations_per_d, all_ok


# =====================================================================
# STEP 3: verify (T-a) directly
# =====================================================================
def step3_verify_Ta(dsV_sym_cache):
    P("\n" + "=" * 72)
    P("STEP 3: Direct check — deg_a Q_{2R} at multiple (R, c)")
    P("=" * 72)
    results = []
    for R in [1, 2, 3, 4]:
        twoR = 2 * R
        for cv in [twoR + 2, twoR + 3, twoR + 5]:
            try:
                h, Q = Q_2R_at(cv, twoR, dsV_sym_cache)
                if Q is None:
                    continue
                h_adeg = Poly(h, a).degree() if h != 0 else -1
                Q_adeg = Poly(Q, a).degree() if Q != 0 else -1
                Q_bdeg = Poly(Q, b).degree() if Q != 0 else -1
                denom_adeg = cv - 1 - twoR
                expected_h_adeg = cv - R - 1
                status_h = "OK" if h_adeg == expected_h_adeg else f"?? (expected {expected_h_adeg})"
                status_Q = "OK" if Q_adeg <= R else "!!VIOLATION!!"
                P(f"  R = {R}, c = {cv}: deg_a h_{{2R}} = {h_adeg} [{status_h}], "
                  f"deg_a Q = {Q_adeg} (expect <= R = {R}) [{status_Q}], deg_b Q = {Q_bdeg}")
                results.append((R, cv, h_adeg, Q_adeg, Q_bdeg))
            except Exception as e:
                P(f"  R = {R}, c = {cv}: EXCEPTION: {e}")
    return results


# =====================================================================
# STEP 4: layer-by-layer verification of h_{2R} a-degree
# =====================================================================
def step4_verify_h_layer_vanishing(dsV_sym_cache, R, cv):
    P("\n" + "=" * 72)
    P(f"STEP 4: h_{{2R}} a-layer vanishing at R = {R}, c = {cv}")
    P("=" * 72)

    twoR = 2 * R
    h, Q = Q_2R_at(cv, twoR, dsV_sym_cache)
    if h is None:
        P("  L < 0, skip")
        return
    h_adeg = Poly(h, a).degree()
    P(f"  h_{{2R}} has a-degree {h_adeg}")
    P(f"  Expected drop from top c-1 = {cv - 1}: {cv - 1 - h_adeg}")
    for d in range(cv):
        a_power = cv - 1 - d
        if a_power < 0:
            break
        L = a_coef_layer(h, a_power)
        vanishes = (L == 0)
        adeg_or = "vanishes" if vanishes else f"nonzero (b-poly of deg {Poly(L, b).degree()})"
        marker = "[vanish]" if vanishes else "[NONZERO]"
        P(f"    d = {d}: a-power = {a_power}: {adeg_or} {marker}")


# =====================================================================
# STEP 5: Actual j-degrees per d
# =====================================================================
def step5_actual_j_degrees(cv, dsV_sym_cache, R_max):
    P("\n" + "=" * 72)
    P(f"STEP 5: Full profile: max j-deg per a-layer d, c = {cv}")
    P("=" * 72)
    slack = 3
    J_max = min(2 * R_max + slack, cv - 1)
    Hcache = {}
    for jv in range(J_max + 1):
        Hcache[jv] = H_c_symbolic_at(jv, cv, dsV_sym_cache)

    max_d = min(cv - 1, 2 * R_max + 4)
    row = []
    for d in range(max_d + 1):
        a_power = cv - 1 - d
        if a_power < 0:
            break
        b_slots_present = set()
        for jv in range(J_max + 1):
            L = a_coef_layer(Hcache[jv], a_power)
            if L == 0:
                continue
            pb = Poly(L, b)
            for (db,), cf in pb.terms():
                b_slots_present.add(db)
        max_jdeg = -1
        for bslot in sorted(b_slots_present):
            samples = []
            for jv in range(J_max + 1):
                L = a_coef_layer(Hcache[jv], a_power)
                if L == 0:
                    samples.append((jv, Integer(0)))
                else:
                    pb = Poly(L, b)
                    cf = Integer(0)
                    for (db,), c_ in pb.terms():
                        if db == bslot:
                            cf = c_
                            break
                    samples.append((jv, cf))
            jd = j_degree_of_samples(samples)
            if jd is not None and jd > max_jdeg:
                max_jdeg = jd
        row.append((d, max_jdeg))
        P(f"  d = {d}: max j-deg over b-slots = {max_jdeg}")
    return row


# =====================================================================
# STEP 6: refined sub-claim (⋆⋆-a'')
# =====================================================================
def step6_verify_refined_subclaim(dsV_sym_cache):
    """Verify (⋆⋆-a''): For each p >= 0,
        (b+2)_{c-1-j} * [a^{j-p}] S_j(a, b, c) = (b+2)_{c-1-2p} * R_p(b, c, j)
    where R_p is a polynomial with j-degree <= 2p per b-slot (for fixed c).

    Test at multiple c values.
    """
    P("\n" + "=" * 72)
    P("STEP 6: Refined sub-claim (⋆⋆-a''): Q_j * A_p / (b+2)_{c-1-2p} has")
    P("        j-degree <= 2p per b-slot.")
    P("=" * 72)
    all_ok = True
    for CV in [12, 15, 18]:
        P(f"\n  c = {CV}:")
        for pp in range(5):
            R_p_per_j = {}
            for j in range(pp, min(CV - 1, 8) + 1):
                S = dsV_sym_cache[j].subs(c, CV)
                pab = Poly(S, a, b)
                Ap = Integer(0)
                for (da, db), cf in pab.terms():
                    if da == j - pp:
                        Ap += cf * b ** db
                L = CV - 1 - j
                if L < 0:
                    continue
                Qj = Integer(1)
                for i in range(L):
                    Qj *= (b + 2 + i)
                prod = expand(Qj * Ap)
                divlen = CV - 1 - 2 * pp
                if divlen < 0:
                    continue
                Q_targ = Integer(1)
                for i in range(divlen):
                    Q_targ *= (b + 2 + i)
                try:
                    quot, rem = sp.div(Poly(prod, b), Poly(Q_targ, b))
                    if rem == 0:
                        R_p_per_j[j] = quot.as_expr()
                    else:
                        R_p_per_j[j] = 'NON-DIV'
                        all_ok = False
                except Exception:
                    R_p_per_j[j] = 'ERR'
            if any(isinstance(v, str) for v in R_p_per_j.values()):
                P(f"    p = {pp}: FAIL divisibility")
                all_ok = False
                continue
            all_bs = set()
            for jv, R in R_p_per_j.items():
                if R == 0:
                    continue
                pbR = Poly(R, b)
                for (db,), cf in pbR.terms():
                    all_bs.add(db)
            max_jd = -1
            for bs in sorted(all_bs):
                samples = []
                for j in sorted(R_p_per_j.keys()):
                    R = R_p_per_j[j]
                    if R == 0:
                        samples.append((j, Integer(0)))
                        continue
                    pbR = Poly(R, b)
                    cf = Integer(0)
                    for (db,), c_ in pbR.terms():
                        if db == bs:
                            cf = c_
                            break
                    samples.append((j, cf))
                jd = j_degree_of_samples(samples)
                if jd is not None and jd > max_jd:
                    max_jd = jd
            status = "OK" if max_jd <= 2 * pp else "!!VIOLATION!!"
            if max_jd > 2 * pp:
                all_ok = False
            P(f"    p = {pp}: R_p max j-deg per b-slot = {max_jd} "
              f"(expect <= 2p = {2 * pp}) [{status}]")
    return all_ok


# =====================================================================
# MAIN
# =====================================================================
def main():
    P("=" * 72)
    P("Day 112: (T-a) 1D degree bound verification")
    P("=" * 72)

    C_VAL = 15
    R_MAX = 4
    J_MAX = min(2 * R_MAX + 3, C_VAL - 1)

    P(f"Building partition tables up to j = {J_MAX}...")
    t0 = time.time()
    tables = bt(J_MAX)
    P(f"  built in {time.time() - t0:.2f}s")

    P(f"Computing ds_j/V symbolically in (a, b, c), j = 0..{J_MAX}...")
    dsV_cache = {}
    compute_dsV_symbolic(J_MAX, tables, dsV_cache)
    P(f"  done in {time.time() - t0:.2f}s total.")

    step1_ok = step1_verify_dsV_a_degree(dsV_cache, J_MAX)
    P(f"\nSTEP 1 result: {'PASS' if step1_ok else 'FAIL'}")

    per_d_max_jdeg, violations_per_d, step2_ok = step2_verify_a_layer_j_degree(
        C_VAL, dsV_cache, R_MAX)
    P(f"\nSTEP 2 result: {'PASS' if step2_ok else 'FAIL'}")
    P(f"  Per-d max j-deg: {[per_d_max_jdeg.get(d, '-') for d in range(2 * R_MAX + 1)]}")
    P(f"  Per-d violations: {[violations_per_d.get(d, '-') for d in range(2 * R_MAX + 1)]}")

    step3_results = step3_verify_Ta(dsV_cache)

    for R in [2, 3]:
        cv = 2 * R + 2
        if cv <= C_VAL:
            step4_verify_h_layer_vanishing(dsV_cache, R, cv)

    row = step5_actual_j_degrees(C_VAL, dsV_cache, R_MAX)
    P(f"\nActual j-degrees per d at c = {C_VAL}: {row}")

    # STEP 6: refined sub-claim (⋆⋆-a'')
    step6_ok = step6_verify_refined_subclaim(dsV_cache)

    P("\n" + "=" * 72)
    P("SUMMARY")
    P("=" * 72)
    P(f"STEP 1 (deg_a ds_j/V <= j): {'PASS' if step1_ok else 'FAIL'}")
    P(f"STEP 2 (a-layer j-deg <= d, TOO STRONG): {'PASS' if step2_ok else 'FAIL (expected — actual is 2d)'}")
    if step3_results:
        all_step3_pass = all(qad <= r for (r, cv, hd, qad, qbd) in step3_results)
        P(f"STEP 3 (deg_a Q <= R): {'PASS' if all_step3_pass else 'FAIL'}")
    P(f"STEP 6 (refined (⋆⋆-a''): Q_j*A_p / (b+2)_{{c-1-2p}} has j-deg <= 2p per b-slot): "
      f"{'PASS' if step6_ok else 'FAIL'}")

    out_path = "/home/agent/projects/beta-prime/code/2026-08-19-Ta-verify.txt"
    with open(out_path, 'w') as f:
        f.write('\n'.join(OUT))
    P(f"\nSaved log to {out_path}")


if __name__ == "__main__":
    main()
