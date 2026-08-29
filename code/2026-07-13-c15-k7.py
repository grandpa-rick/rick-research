"""Extract h_7^{(15)}(a, b) as bivariate poly and confirm β'(15) = 19.

Report says k*=7 is UNIQUE argmin for LB=19 at c=15. Achiever candidate (a, b) = (6, 7).
"""
import json
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, sympify, expand, Matrix, Rational, lambdify

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
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def rising_fact(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= (x + i)
    return p


def fit_bivariate(samples, deg_bound=32):
    a_s, b_s = symbols('a b')
    for D in range(deg_bound + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 3:
            continue
        rows = []
        yvals = []
        use = samples[:N + 20]
        for (av, bv, yv) in use:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        t1 = time.time()
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        print(f"    D={D}: rref in {time.time()-t1:.1f}s, pivots={len(pivots)}/{N+1}", flush=True)
        if (aug.cols - 1) in pivots:
            continue
        if len(pivots) != N:
            continue
        sol = [rref[pivots.index(i), aug.cols - 1] for i in range(N)]
        if any(not isinstance(c, Rational) or c.q != 1 for c in sol):
            continue
        poly = 0
        for (da, db), c in zip(monomials, sol):
            poly += int(c) * a_s ** da * b_s ** db
        poly = expand(poly)
        # verify full set
        bad = False
        for (av, bv, yv) in samples:
            got = poly.subs({a_s: av, b_s: bv})
            if got != yv:
                bad = True
                break
        if bad:
            print(f"    verify FAILED at D={D}", flush=True)
            continue
        return poly, D
    return None, None


def extract_h7_at_c15():
    c_val = 15
    k_target = 7
    L = c_val - 1 - k_target  # = 7
    # Total degree of h_k in (a,b): 2L + Q_k deg. For k=7 unknown, generous bound.
    # From higher-k extractions: k=7 deg was 18 in previous run. Let's use 25.
    max_deg = 20
    print(f"Extract h_{{k=7}}^{{(c=15)}}(a, b), L={L}, target max_deg={max_deg}", flush=True)
    t0 = time.time()
    tables = build_e2_tables(max_j=k_target + 2)
    print(f"  tables in {time.time()-t0:.1f}s", flush=True)
    # Need > monomials for deg 20 = (21)(22)/2 = 231. Sample width w: w(w+1)/2 >= 250.
    # w ~ 23. Take w=25 to be safe.
    w = 25
    samples = []
    t0 = time.time()
    for a in range(c_val, c_val + w):
        for b in range(c_val, a + 1):
            hks = extract_h_k(a, b, c_val, k_target, tables)
            if hks is None:
                continue
            samples.append((a, b, hks[k_target]))
    print(f"  {len(samples)} samples in {time.time()-t0:.1f}s", flush=True)
    print("  fitting...", flush=True)
    poly, D = fit_bivariate(samples, deg_bound=max_deg)
    if poly is None:
        print("  FIT FAILED", flush=True)
        return None
    print(f"  FIT: deg {D}, total time {time.time()-t0:.1f}s", flush=True)
    return poly


def load_Q_catalog():
    with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json') as f:
        d = json.load(f)
    a_s, b_s, c_s = symbols('a b c')
    Q = {}
    for k_str, poly_str in d['Q_k_low_k'].items():
        Q[int(k_str)] = sympify(poly_str)
    for k_str, entry in d['Q_k_extended'].items():
        if entry is None:
            continue
        Q[int(k_str)] = sympify(entry['poly_expanded'])
    return Q


def main():
    print("=" * 74)
    print("c = 15, extract h_7 and check β'(15) = 19 via witness")
    print("=" * 74, flush=True)

    Q_catalog = load_Q_catalog()

    # Build k=0..6 evaluators from catalog.
    a_s, b_s, c_s = symbols('a b c')
    evs = {}
    for k in range(7):
        L = 15 - 1 - k
        Q_ab = expand(Q_catalog[k].subs(c_s, 15))
        fQ = lambdify((a_s, b_s), Q_ab, "math")
        def mk(fQ_b, L_b):
            def hk(a, b):
                return rising_fact(a + 3, L_b) * rising_fact(b + 2, L_b) * int(fQ_b(a, b))
            return hk
        evs[k] = mk(fQ, L)

    # Extract h_7^{(15)}
    print("\nExtracting h_7^{(15)}...", flush=True)
    poly7 = extract_h7_at_c15()
    if poly7 is None:
        print("EXTRACTION FAILED. Abort.")
        return
    f7 = lambdify((a_s, b_s), poly7, "math")
    def hk7(a, b):
        return int(f7(a, b))
    evs[7] = hk7

    # Cross-check: h_7^{(15)}(15, 15) via extraction vs via poly evaluation
    tables = build_e2_tables(max_j=9)
    hks_check = extract_h_k(15, 15, 15, 7, tables)
    print(f"\n[cross-check] h_7^{{(15)}}(15, 15)")
    print(f"  poly7 eval: {hk7(15, 15)}")
    print(f"  extract:    {hks_check[7] if hks_check else None}")
    print(f"  match: {hk7(15, 15) == hks_check[7]}", flush=True)

    # Check the named achiever (6, 7, k*=7)
    def compute_H(a, b, k_star):
        total = 0
        for k in range(k_star + 1):
            total += Cn(k_star, k) * evs[k](a, b)
        return total

    print("\n" + "=" * 74)
    print("Witness checks with k* = 7")
    print("=" * 74)
    for (a, b) in [(6, 7), (7, 6), (0, 1), (1, 0), (2, 3), (0, 3), (3, 0),
                    (1, 2), (2, 1), (4, 3), (5, 6), (6, 1), (1, 6)]:
        if (a + b) % 2 != 15 % 2:
            continue
        total = compute_H(a, b, 7)
        v = v2(total)
        per_k = [v2(Cn(7, k) * evs[k](a, b)) for k in range(8)]
        carrier_v = per_k[7]
        others = per_k[:7]
        distinct = all(o > carrier_v for o in others)
        print(f"  (a,b)=({a},{b}), k*=7: H = {total}")
        print(f"    v_2(H) = {v}   per-k v_2: {per_k}   distinct-min: {distinct}")

    # Full scan with k* in 0..7
    print("\n" + "=" * 74)
    print("Scan c=15, (a,b) in [0, 32)^2, k* in [0, 7]")
    print("=" * 74)
    per_kstar = {}
    for k_star in range(8):
        best_v = float('inf')
        best_ab = None
        t0 = time.time()
        for a in range(32):
            for b in range(32):
                if (a + b) % 2 != 15 % 2:
                    continue
                total = compute_H(a, b, k_star)
                v = v2(total)
                if v < best_v:
                    best_v = v
                    best_ab = (a, b)
        per_kstar[k_star] = (best_v, best_ab)
        print(f"    k*={k_star}: min v_2(H) = {best_v} at (a,b)={best_ab}  [{time.time()-t0:.1f}s]", flush=True)

    min15 = min(v for v, _ in per_kstar.values())
    argmin15 = [k for k, (v, _) in per_kstar.items() if v == min15]
    print(f"\n[c=15 scan] min v_2(H_15) = {min15} at k* ∈ {argmin15}")
    print(f"  predicted β'(15) = 19   =>   "
          f"{'MATCH: FORMULA CORRECT' if min15 == 19 else ('BELOW' if min15 < 19 else 'ABOVE')}")


if __name__ == "__main__":
    main()
