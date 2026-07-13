"""Day 93 — Extend Δ_k^{(c)} catalog to c ∈ {12, 13, 14, 15, 16, 17}.

Purpose: test predictions of the piecewise-floor formula for β'(c).
Formula predicts:
  β'(12) = 18, β'(13) = 16, β'(14) = 20, β'(15) = 19, β'(16) = 25, β'(17) = 23.

Approach: extend the existing catalog (Day 90/91) using
  - Q_k(a, b, c) catalog for k = 0..6 (symbolic in c, evaluate at c_val).
  - h_k extraction pipeline for k = 7..(c-1).

For each (c, k), compute Δ_k^{(c)} = min v_2(Q_k(a, b, c)) over
Pochmin locus in shell. Then LB_k^{(c)} = 2·v_2((c-1-k)!) + Δ_k.

Structural β'(c) prediction: min_k LB_k^{(c)}. If this matches the
piecewise formula prediction, that's structural confirmation
(pending SCP distinct-min verification, which comes for free if
min_k LB_k is unique argmin).
"""

import json
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, sympify, expand, Matrix, Rational

# Load pipeline for k>=7 extraction.
spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)


def v2_int(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    v = 0
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def load_Q_catalog():
    d = json.load(open('/home/agent/projects/code/2026-07-11-Qk-catalog.json'))
    a, b, c = symbols('a b c')
    Q = {}
    for k_str, poly_str in d['Q_k_low_k'].items():
        Q[int(k_str)] = sympify(poly_str)
    for k_str, entry in d['Q_k_extended'].items():
        if entry is None:
            continue
        Q[int(k_str)] = sympify(entry['poly_expanded'])
    return Q


def poly_at_c(Q_kabc, c_val):
    a, b, c = symbols('a b c')
    return expand(Q_kabc.subs(c, c_val))


def rising_fact(x, n):
    if n <= 0: return 1
    p = 1
    for i in range(n): p *= (x + i)
    return p


def extract_hk_bivariate(c_val, k_target, verbose=False):
    """Extract h_{k_target}^{(c=c_val)}(a, b) as bivariate polynomial via
    fitting on pipeline samples with a >= b >= c."""
    tables = hkfit.build_e2_tables(max_j=k_target + 2)
    w = max(2 * c_val + 5, 25)
    samples = []
    a_s, b_s = symbols('a b')
    for a in range(c_val, c_val + w):
        for b in range(c_val, a + 1):
            hks = hkfit.extract_h_k(a, b, c_val, k_target, tables)
            if hks is None: continue
            samples.append((a, b, hks[k_target]))
    if not samples:
        return None
    if verbose:
        print(f"    [ extract hk c={c_val},k={k_target}: {len(samples)} samples ]")
    max_deg = 2 * (c_val - 1)
    for D in range(max_deg + 1):
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
        for cc in sol:
            if not isinstance(cc, Rational) or cc.q != 1:
                ok = False
                break
        if not ok:
            continue
        poly = 0
        for (da, db), cc in zip(monomials, sol):
            poly += int(cc) * a_s ** da * b_s ** db
        poly = expand(poly)
        bad = False
        for (av, bv, yv) in samples:
            if poly.subs({a_s: av, b_s: bv}) != yv:
                bad = True
                break
        if bad: continue
        return poly
    return None


def Q_k_at_c_from_hk(c_val, k_target, verbose=False):
    hk_ab = extract_hk_bivariate(c_val, k_target, verbose=verbose)
    if hk_ab is None: return None
    a_s, b_s = symbols('a b')
    L = c_val - 1 - k_target
    if L < 0: return None
    poch_a = rising_fact(a_s + 3, L)
    poch_b = rising_fact(b_s + 2, L)
    denom = expand(poch_a * poch_b)
    from sympy import div, cancel
    q, r = div(hk_ab, denom, domain='QQ')
    if r != 0:
        candidate = cancel(hk_ab / denom)
        if expand(candidate * denom) == hk_ab:
            return expand(candidate)
        return None
    return expand(q)


def compute_delta(Q_ab, c_val, k, search_T=8, verbose=False):
    L = c_val - 1 - k
    if L < 0: return None, []
    parity = c_val % 2
    a_s, b_s = symbols('a b')
    from sympy import lambdify
    f = lambdify((a_s, b_s), Q_ab, modules='math')
    N = 1 << search_T
    # Poch-min: (a+2) & L == 0, (b+1) & L == 0.
    valid_a = [x - 2 for x in range(N) if (x & L) == 0 and x - 2 >= 0]
    valid_b = [x - 1 for x in range(N) if (x & L) == 0 and x - 1 >= 0]
    if verbose:
        print(f"    L={L}, |valid_a|={len(valid_a)}, |valid_b|={len(valid_b)}")
    min_v = float('inf')
    achievers = []
    for a in valid_a:
        for b in valid_b:
            if (a + b) % 2 != parity:
                continue
            try:
                val = int(f(a, b))
            except Exception:
                continue
            v = v2_int(val)
            if v < min_v:
                min_v = v
                achievers = [(a, b, v)]
            elif v == min_v and len(achievers) < 5:
                achievers.append((a, b, v))
            if min_v == 0:
                break
        if min_v == 0:
            break
    return min_v, achievers


def main():
    print("=" * 74)
    print("Day 93 — Δ_k^{(c)} catalog extension for c ∈ [12..17]")
    print("=" * 74)

    Q_catalog = load_Q_catalog()

    # Piecewise formula predictions
    def D_pred(c):
        if c % 2 == 1: return 4 + 2 * ((c - 1) // 8)
        elif c % 4 == 0: return (c - 4) // 8
        else: return 1 + (c - 6) // 4

    def beta(c):
        s2 = bin(c-1).count('1')
        return 2 * (c - 1) - s2

    def bp_pred(c):
        return beta(c) - D_pred(c)

    # Load existing catalog
    with open('/home/agent/projects/code/2026-07-12-Delta-k-c-catalog.json') as f:
        old_catalog = json.load(f)
    new_data = {}
    for k, v in old_catalog['data'].items():
        new_data[k] = v

    c_range = list(range(12, 18))  # 12, 13, 14, 15, 16, 17

    for c_val in c_range:
        print(f"\n{'=' * 74}")
        print(f"c = {c_val}, shell parity a+b ≡ {c_val % 2}, "
              f"formula predicts β'({c_val}) = {bp_pred(c_val)} "
              f"(β={beta(c_val)}, D={D_pred(c_val)})")
        print("=" * 74)
        # k goes 0..c-1 (clean regime).
        # For k >= 7 use extraction pipeline (slow).
        max_k_pipeline = min(c_val - 1, 12)  # cap at k=12 to avoid excessive compute
        for k in range(max_k_pipeline + 1):
            L = c_val - 1 - k
            if L < 0:
                continue
            v2Lfact = v2_int(factorial(L)) if L > 0 else 0
            t0 = time.time()
            if k in Q_catalog:
                Q_ab = poly_at_c(Q_catalog[k], c_val)
                src = "catalog"
            else:
                Q_ab = Q_k_at_c_from_hk(c_val, k, verbose=True)
                src = "extract"
                if Q_ab is None:
                    print(f"  k={k}: L={L}, EXTRACTION FAILED, skip.")
                    new_data[f"c{c_val},k{k}"] = {
                        'Delta': None, 'achievers': [], 'L': L,
                        'v2Lfact': v2Lfact, 'LB': None,
                        'status': 'extraction_failed',
                    }
                    continue
            search_T = 8 if L >= 4 else 10
            delta, ach = compute_delta(Q_ab, c_val, k, search_T=search_T)
            dt = time.time() - t0
            LB = 2 * v2Lfact + delta if delta is not None else None
            ach_str = ", ".join(f"({a},{b},v2={v})" for a, b, v in ach[:3])
            print(f"  k={k:>2}: L={L:>2}, v_2(L!)={v2Lfact:>2}, Δ={delta}, "
                  f"LB = 2·{v2Lfact} + {delta} = {LB}  ({src}, {dt:.1f}s)")
            print(f"          achievers: {ach_str}")
            new_data[f"c{c_val},k{k}"] = {
                'Delta': delta,
                'achievers': [list(x) for x in ach[:5]],
                'L': L,
                'v2Lfact': v2Lfact,
                'LB': LB,
                'status': 'ok',
                'source': src,
            }

    # Summary
    print("\n" + "=" * 74)
    print("SUMMARY: min_k LB_k^{(c)} for c ∈ [12..17]")
    print("=" * 74)
    print(f"{'c':>3} {'β':>4} {'D_pred':>7} {'β_pred':>7} {'min_k LB':>10} {'argmin_k':>10} {'match':>7}")
    for c_val in c_range:
        lbs = []
        for k in range(c_val):
            key = f"c{c_val},k{k}"
            if key in new_data and new_data[key].get('LB') is not None:
                lbs.append((new_data[key]['LB'], k))
        if not lbs:
            print(f"{c_val:>3}   no LBs")
            continue
        min_lb = min(x[0] for x in lbs)
        argmin = [k for lb, k in lbs if lb == min_lb]
        formula_pred = bp_pred(c_val)
        match = min_lb == formula_pred
        print(f"{c_val:>3} {beta(c_val):>4} {D_pred(c_val):>7} {formula_pred:>7} "
              f"{min_lb:>10} {str(argmin):>10} {'YES' if match else 'NO':>7}")

    # Save
    out = {
        'note': 'Δ_k^{(c)} catalog extended to c ∈ [12..17], Day 93.',
        'definition': old_catalog['definition'],
        'LB_formula': old_catalog['LB_formula'],
        'source_Q_catalog': old_catalog['source_Q_catalog'],
        'data': new_data,
    }
    with open('/home/agent/projects/code/2026-07-13-Delta-k-c-catalog-extended.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved /home/agent/projects/code/2026-07-13-Delta-k-c-catalog-extended.json")


if __name__ == "__main__":
    main()
