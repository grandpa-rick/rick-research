"""Day 98 CODE Task 4 — direct H_20 evaluation at witness candidates.

Diagnostic: probe H_20(a, b, k*) at (a, b, k*) triples to see the min
v_2 achieved. This adjudicates the tension between:
  - digit-sum formula prediction: β'(20) = 34 (D(20) = s_2(5) - 1 = 1)
  - corner-first LB predictions at various k
  - Day 97 CODE finding: interior (2, 4) beats corner by 1 at k=11 for c=20

Because extract_h_k(a, b, c, k) requires a >= b >= c (template constraint),
we can't directly evaluate at (a=30, b=0, c=20). Solution: fit Q_k^{(c=20)}
via the Pochhammer-normalized bivariate fit, then use
  h_k^{(c)}(a, b) = (a+3)_L * (b+2)_L * Q_k^{(c)}(a, b)   with L = c-1-k.
This closed form works for ANY (a, b).
"""
import json
import time
from importlib import util
from math import factorial

import sympy as sp

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)


def v2(n):
    if n == 0:
        return None
    n = abs(int(n))
    v = 0
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def Cn(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k)) if 0 <= k <= n else 0


def T_of(c):
    T = 1
    while T <= c - 2:
        T *= 2
    return T


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def sample_and_fit_Qk(c_val, k_target, tables):
    L = c_val - 1 - k_target
    if L < 0:
        return None
    bd = 2 * (k_target // 2)
    max_deg_try = bd + 4
    max_monos = (max_deg_try + 1) * (max_deg_try + 2) // 2
    num_pts_target = max_monos + 20
    samples = []
    a = c_val
    while len(samples) < num_pts_target and a < c_val + 60:
        for b in range(c_val, a + 1):
            hks = hkfit.extract_h_k(a, b, c_val, k_target, tables)
            if hks is None:
                continue
            if k_target >= len(hks):
                continue
            y = hks[k_target]
            denom = rising_fact(a + 3, L) * rising_fact(b + 2, L)
            if denom == 0:
                continue
            if y % denom != 0:
                return None
            samples.append((a, b, y // denom))
        a += 1

    a_sym, b_sym = sp.symbols('a b')
    for D in range(bd + 4 + 1):
        nm = (D + 1) * (D + 2) // 2
        if len(samples) < nm + 3:
            continue
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        rows = []
        yvals = []
        for (av, bv, yv) in samples:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        M = sp.Matrix(rows)
        y = sp.Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != nm:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(nm)]
        poly = 0
        for (da, db), coef in zip(monomials, sol):
            poly += coef * a_sym ** da * b_sym ** db
        poly = sp.expand(poly)
        ok = True
        for (av, bv, yv) in samples:
            if poly.subs({a_sym: av, b_sym: bv}) != yv:
                ok = False
                break
        if not ok:
            continue
        return poly
    return None


def h_k_from_Q(a, b, c_val, k, Q_ab):
    a_sym, b_sym = sp.symbols('a b')
    L = c_val - 1 - k
    Qv = int(Q_ab.subs({a_sym: a, b_sym: b}))
    pa = rising_fact(a + 3, L)
    pb = rising_fact(b + 2, L)
    return pa * pb * Qv


def H_c(a, b, c_val, k_star, Q_cache):
    """H_c(a, b, k*) = sum_{k=0..k*} C(k*, k) h_k^{(c)}(a, b)."""
    total = 0
    per_k_terms = []
    for k in range(k_star + 1):
        Q_ab = Q_cache.get(k)
        if Q_ab is None:
            return None, None
        hk = h_k_from_Q(a, b, c_val, k, Q_ab)
        c_bin = Cn(k_star, k)
        term = c_bin * hk
        total += term
        per_k_terms.append((k, c_bin, hk, term))
    return total, per_k_terms


def main():
    print("=" * 78)
    print("Day 98 (2026-07-16) — H_20 direct evaluation at witness candidates")
    print("=" * 78)

    c_val = 20
    T = T_of(c_val)
    print(f"c = {c_val}, T = {T}, natural shell [0, 2T)^2 = [0, {2*T})^2")
    print(f"v_2(c-i) i=1..5: {[v2(c_val - i) for i in range(1, 6)]}")
    print()
    print("Predictions:")
    print("  digit-sum: β'(20) = 34")
    print("  β(20) = 2·19 - s_2(19) = 38 - 3 = 35")
    print("  Day 97: h_11^(20) at (2,4) beats corner by 1")

    # Fit Q_k for k in [0, 15]
    print("\n-- Fitting Q_k^(20) for k in [0, 15] --")
    Q_cache = {}
    for k in range(0, 16):
        t0 = time.time()
        tables = hkfit.build_e2_tables(max_j=k + 2)
        try:
            Q_ab = sample_and_fit_Qk(c_val, k, tables)
        except Exception as e:
            print(f"  k={k}: fit exception: {e}")
            Q_ab = None
        if Q_ab is None:
            print(f"  k={k}: fit FAILED")
            continue
        Q_cache[k] = Q_ab
        print(f"  k={k}: fit OK ({time.time() - t0:.1f}s)")

    # Witness cases: (a, b, k*, label)
    cases = []
    # Corner (T-2, 0) at various k*
    for k_star in [1, 3, 5, 7, 9, 11, 13, 15]:
        cases.append((T - 2, 0, k_star, f'C1_(T-2,0)_kstar={k_star}'))
        cases.append((0, 0, k_star, f'C4_(0,0)_kstar={k_star}'))
    # Interior (2, 4) — Day 97 finding
    for k_star in [1, 3, 5, 7, 9, 11, 13, 15]:
        cases.append((2, 4, k_star, f'interior_(2,4)_kstar={k_star}'))
    # Other small interior
    for k_star in [11, 13, 15]:
        cases.append((2, 8, k_star, f'interior_(2,8)_kstar={k_star}'))
        cases.append((4, 4, k_star, f'interior_(4,4)_kstar={k_star}'))
        cases.append((4, 8, k_star, f'interior_(4,8)_kstar={k_star}'))

    print(f"\n-- Scanning {len(cases)} witness candidates --")
    results = []
    for (a, b, k_star, label) in cases:
        parity_ok = ((a + b) % 2 == c_val % 2)
        if not parity_ok:
            print(f"  {label:>35} (a,b,k*)=({a:>2},{b:>2},{k_star:>2}) parity NO-SKIP")
            results.append({'label': label, 'a': a, 'b': b, 'k_star': k_star,
                            'parity_ok': False, 'v_H': None})
            continue
        H, per_k = H_c(a, b, c_val, k_star, Q_cache)
        if H is None:
            print(f"  {label:>35} extraction failed")
            continue
        v_H = v2(H) if H != 0 else None
        per_k_v2 = [v2(term[3]) for term in per_k]
        min_per_k = min((v for v in per_k_v2 if v is not None), default=None)
        # Check distinct-min at carrier k*
        distinct_carrier = None
        if k_star < len(per_k_v2):
            carrier_v = per_k_v2[k_star]
            others = [v for i, v in enumerate(per_k_v2) if i != k_star and v is not None]
            distinct_carrier = (
                carrier_v is not None
                and all(o > carrier_v for o in others)
            )
        print(f"  {label:>35} (a,b,k*)=({a:>2},{b:>2},{k_star:>2}) "
              f"v_H={v_H!s:>4} min_per_k={min_per_k!s:>4} distinct={distinct_carrier}")
        results.append({
            'label': label, 'a': a, 'b': b, 'k_star': k_star,
            'parity_ok': True, 'H': str(H), 'v_H': v_H,
            'per_k_v2': per_k_v2, 'min_per_k': min_per_k,
            'distinct_carrier': distinct_carrier,
        })

    print("\n" + "=" * 78)
    print("AGGREGATE — min v_2(H_20) over attempted witnesses")
    print("=" * 78)
    valid = [r for r in results if r.get('v_H') is not None and r.get('parity_ok')]
    if not valid:
        print("  no valid witnesses")
        return
    min_v = min(r['v_H'] for r in valid)
    print(f"  min v_2(H_20) seen = {min_v}")
    min_v_records = [r for r in valid if r['v_H'] == min_v]
    print(f"  Achieved by:")
    for r in min_v_records:
        print(f"    {r['label']:>40}  (a,b,k*)=({r['a']},{r['b']},{r['k_star']})  "
              f"v_H = {r['v_H']}  distinct = {r['distinct_carrier']}")

    print()
    if min_v < 34:
        print(f"  ⇒ DIGIT-SUM FALSIFIED at c=20: found v_2(H_20) = {min_v} < 34")
    elif min_v == 34:
        print(f"  ⇒ DIGIT-SUM CONSISTENT: min v_2(H_20) = 34 = digit-sum prediction")
    else:
        print(f"  ⇒ min v_2(H_20) = {min_v} > 34: both predictions may be conservative")

    print("\n" + "=" * 78)
    print("Interior (2, 4) v_2 progression across k*:")
    print("=" * 78)
    for k_star in [1, 3, 5, 7, 9, 11, 13, 15]:
        r = next((rr for rr in results if rr.get('a') == 2 and rr.get('b') == 4
                  and rr.get('k_star') == k_star and rr.get('v_H') is not None), None)
        if r:
            print(f"  k*={k_star:>2}: v_2(H_20) = {r['v_H']:>3}, "
                  f"per-k v_2 = {r['per_k_v2']}")

    print("\n" + "=" * 78)
    print("Corner (T-2, 0) = (30, 0) v_2 progression across k*:")
    print("=" * 78)
    for k_star in [1, 3, 5, 7, 9, 11, 13, 15]:
        r = next((rr for rr in results if rr.get('a') == 30 and rr.get('b') == 0
                  and rr.get('k_star') == k_star and rr.get('v_H') is not None), None)
        if r:
            print(f"  k*={k_star:>2}: v_2(H_20) = {r['v_H']:>3}, "
                  f"per-k v_2 = {r['per_k_v2']}")

    out = {
        'note': 'Day 98 direct H_20 evaluation at witness candidates',
        'date': '2026-07-16',
        'c': c_val,
        'T': T,
        'v2_c_minus_i': [v2(c_val - i) for i in range(1, 6)],
        'min_v_H_seen': min_v,
        'results': results,
        'digit_sum_predicted': 34,
        'digit_sum_falsified': min_v < 34,
    }
    outpath = '/home/agent/projects/code/2026-07-16-H20-scan.json'
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {outpath}")


if __name__ == "__main__":
    main()
