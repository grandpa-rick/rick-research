"""Day 94 CODE — Distinct-min witness checks for β'(14)=21 and β'(15)=19.

Predictions from digit-sum formula (Day 93):
  β'(14) = 21 EXACT (formula: 1 + s_2(2) = 2, β(14) - 2 = 23 - 2 = 21)
  β'(15) = 19 EXACT (formula: 4 + 2·s_2(2) = 6, β(15) - 6 = 25 - 6 = 19)

Method: distinct-min sum rule (SCP).
  For each candidate witness (a*, b*, j*=k*):
    - Compute per-summand v_2(h_k^{(c)}(a*, b*) * C(k*, k)) for k = 0..k*
    - If v_2 at k=k* is strictly smaller than all others => v_2(H_c) = that value
    - Cross-check by computing H_c directly and taking v_2.

For c=14 the LB catalog achievers (small (a,b)) come from the report:
  candidates: (0, 0), (2, 0) at k* = 6-11 (multiple k tied at 21)
For c=15 the achiever is (6, 7) at k = 7 (unique minimum).

Pipeline: extract h_k^{(c)}(a, b) as bivariate polynomial via extract_h_k
sampling with a >= b >= c, then evaluate at small (a, b).
"""
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, Matrix, Rational, expand, factor, lambdify

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)

extract_h_k = mod.extract_h_k
build_e2_tables = mod.build_e2_tables


def Cn(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def v2(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def fit_bivariate_poly(samples, deg_bound=32):
    a_s, b_s = symbols('a b')
    for D in range(deg_bound + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 3:
            continue
        rows = []
        yvals = []
        for (av, bv, yv) in samples:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != N:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        ok = True
        for c in sol:
            if not isinstance(c, Rational) or c.q != 1:
                ok = False
                break
        if not ok:
            continue
        poly = 0
        for (da, db), c in zip(monomials, sol):
            poly += int(c) * a_s ** da * b_s ** db
        poly = expand(poly)
        bad = False
        for (av, bv, yv) in samples:
            got = poly.subs({a_s: av, b_s: bv})
            if got != yv:
                bad = True
                break
        if bad:
            continue
        return poly, D
    return None, None


def extract_hk_polys(c_val, jmax, arange, brange=None, min_samples=None):
    """Extract h_k^{(c)}(a, b) as sympy polys for k = 0..jmax.

    Sampling range: a in [arange[0], arange[1]), b in [c, a] (b >= c).
    """
    print(f"\n[extract] h_k^{{(c={c_val})}}(a,b) for k=0..{jmax}, "
          f"a in [{arange[0]},{arange[1]}), b in [{c_val}, a+1]")
    tables = build_e2_tables(max_j=jmax + 2)
    per_k = {k: [] for k in range(jmax + 1)}
    if brange is None:
        brange = (c_val, None)
    t0 = time.time()
    n_ok = 0
    for a in range(arange[0], arange[1]):
        bmin, bmax = brange
        bhi = a + 1 if bmax is None else min(a + 1, bmax + 1)
        for b in range(bmin, bhi):
            hks = extract_h_k(a, b, c_val, jmax, tables)
            if hks is None:
                continue
            for k, y in enumerate(hks):
                per_k[k].append((a, b, y))
            n_ok += 1
    dt = time.time() - t0
    print(f"          {n_ok} samples in {dt:.1f}s")

    result = {}
    for k in range(jmax + 1):
        samples = per_k[k]
        if min_samples is not None and len(samples) < min_samples:
            print(f"  k={k}: skip (only {len(samples)} samples)")
            continue
        t1 = time.time()
        poly, D = fit_bivariate_poly(samples, deg_bound=32)
        dt1 = time.time() - t1
        if poly is None:
            print(f"  k={k}: no polynomial fit  [{dt1:.1f}s]")
        else:
            result[k] = poly
            print(f"  k={k}: deg <= {D}   [{dt1:.1f}s]   #samples = {len(samples)}")
    return result


def verify_witness(hk_polys, a_star, b_star, k_star, c_val):
    a_s, b_s = symbols('a b')
    summands = []
    total = 0
    for k in range(k_star + 1):
        if k not in hk_polys:
            summands.append((k, None, None, None, None))
            continue
        val = int(hk_polys[k].subs({a_s: a_star, b_s: b_star}))
        weight = Cn(k_star, k)
        contrib = weight * val
        total += contrib
        summands.append((k, val, weight, contrib, v2(contrib)))
    v_total = v2(total) if total != 0 else float('inf')
    carrier = summands[k_star]
    carrier_v = carrier[4] if carrier[4] is not None else None
    others = [s[4] for i, s in enumerate(summands) if i != k_star and s[4] is not None]
    if others and carrier_v is not None:
        ok = all(v > carrier_v for v in others)
    else:
        ok = None
    return total, v_total, summands, ok, carrier_v


def scan_witness(hk_polys, c_val, k_range=None, ab_range=32):
    """Scan (a, b, k*) triples for the minimum v_2(H_c) directly."""
    a_s, b_s = symbols('a b')
    parity = c_val % 2
    if k_range is None:
        k_range = sorted(hk_polys.keys())
    # Pre-lambdify for speed
    funcs = {k: lambdify((a_s, b_s), hk_polys[k], "math") for k in k_range}
    best = None
    per_kstar_best = {}
    for k_star in k_range:
        min_v_here = float('inf')
        best_ab = None
        for a in range(ab_range):
            for b in range(ab_range):
                if (a + b) % 2 != parity:
                    continue
                total = 0
                bad = False
                for k in range(k_star + 1):
                    if k not in funcs:
                        bad = True
                        break
                    try:
                        val = int(funcs[k](a, b))
                    except Exception:
                        bad = True
                        break
                    total += Cn(k_star, k) * val
                if bad:
                    continue
                v = v2(total)
                if v < min_v_here:
                    min_v_here = v
                    best_ab = (a, b)
                if best is None or v < best[3]:
                    best = (a, b, k_star, v)
        per_kstar_best[k_star] = (min_v_here, best_ab)
    return best, per_kstar_best


def report_case(c_val, jmax, arange, beta_prime_pred, achiever_candidates,
                scan_ab_range=32):
    print("\n" + "=" * 74)
    print(f"CASE: c = {c_val}, β'({c_val}) predicted = {beta_prime_pred}")
    print("=" * 74)

    hk_polys = extract_hk_polys(c_val, jmax, arange, brange=(c_val, None),
                                min_samples=30)
    if not hk_polys:
        print("  NO POLYS EXTRACTED — abort")
        return None

    print(f"\n[polys extracted for k in {sorted(hk_polys.keys())}]")

    # (i) Try specific achiever candidates.
    print(f"\n[direct check] achiever candidates for c={c_val}:")
    for (a_star, b_star, k_star) in achiever_candidates:
        if k_star not in hk_polys:
            print(f"  (a*,b*,k*)=({a_star},{b_star},{k_star}): k* not in poly cache")
            continue
        total, v_tot, summands, ok, carrier_v = verify_witness(
            hk_polys, a_star, b_star, k_star, c_val)
        note = "OK distinct-min" if ok else ("NOT distinct-min" if ok is False else "?")
        print(f"  (a*,b*,k*)=({a_star},{b_star},{k_star}): "
              f"H = {total},  v_2(H) = {v_tot}, "
              f"carrier v_2 = {carrier_v}   [{note}]")
        # Show per-k v_2:
        vs = [s[4] for s in summands]
        print(f"       per-k v_2: {vs}")

    # (ii) Scan for global min v_2(H_c) over (a, b, k*) grid.
    print(f"\n[scan] over (a, b) in [0, {scan_ab_range})^2 and "
          f"k* in {sorted(hk_polys.keys())}:")
    t0 = time.time()
    best, per_kstar = scan_witness(hk_polys, c_val, ab_range=scan_ab_range)
    dt = time.time() - t0
    print(f"       scan complete in {dt:.1f}s")
    print(f"       per-k* min v_2(H):")
    for k_star, (v, ab) in sorted(per_kstar.items()):
        print(f"         k*={k_star:>2}: min v_2 = {v}   at {ab}")
    if best is not None:
        a_star, b_star, k_star, v = best
        print(f"\n       GLOBAL MIN v_2(H_{c_val}) = {v}  at (a*,b*,k*)=({a_star},{b_star},{k_star})")

        # Verify distinct-min at global min:
        total, v_tot, summands, ok, carrier_v = verify_witness(
            hk_polys, a_star, b_star, k_star, c_val)
        note = "OK distinct-min" if ok else ("NOT distinct-min" if ok is False else "?")
        print(f"\n       Distinct-min at global min: {note}")
        print(f"       H_{c_val} = {total}")
        print(f"       Per-k breakdown:")
        for s in summands:
            k, val, weight, contrib, v_ = s
            marker = "  <-- CARRIER" if k == k_star else ""
            print(f"         k={k:>2}: h_k = {val},  C({k_star},{k})={weight},  v_2(contrib) = {v_}{marker}")
    return best


def main():
    print("=" * 74)
    print("Day 94 CODE — Distinct-min witness checks for β'(14), β'(15)")
    print("=" * 74)

    # For c=14: shell parity a+b even. LB catalog mentions (0, 0), (2, 0) among achievers.
    # jmax must reach at least the argmin_k. Report said "many" k tied at LB=21.
    # We need to extract up to k=13 (c-1=13) but the sample cost grows fast.
    # A good balance: jmax=11 (drops last two k).
    # For (0,0), (2,0), (0,2), (2,2), scan k=0..jmax.
    achievers_14 = []
    for a in [0, 2]:
        for b in [0, 2]:
            if (a + b) % 2 != 14 % 2:  # need even
                continue
            for k in [6, 7, 8, 9, 10, 11]:
                achievers_14.append((a, b, k))

    result_14 = report_case(
        c_val=14, jmax=11,
        arange=(14, 36),  # 22 a-values, giving many (a,b) samples
        beta_prime_pred=21,
        achiever_candidates=achievers_14,
        scan_ab_range=16,  # 16x16 = 128 (a+b even) triples per k*
    )

    # For c=15: shell parity a+b odd. Achiever candidate (a,b)=(6,7) at k*=7.
    achievers_15 = [(6, 7, 7), (7, 6, 7)]
    result_15 = report_case(
        c_val=15, jmax=11,
        arange=(15, 38),
        beta_prime_pred=19,
        achiever_candidates=achievers_15,
        scan_ab_range=16,
    )

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    if result_14:
        _, _, _, v14 = result_14
        pred14_ok = (v14 == 21)
        print(f"  c=14: scan-min v_2 = {v14},  predicted 21,  {'MATCH' if pred14_ok else ('BELOW' if v14 < 21 else 'ABOVE')}")
    if result_15:
        _, _, _, v15 = result_15
        pred15_ok = (v15 == 19)
        print(f"  c=15: scan-min v_2 = {v15},  predicted 19,  {'MATCH' if pred15_ok else ('BELOW' if v15 < 19 else 'ABOVE')}")


if __name__ == "__main__":
    main()
