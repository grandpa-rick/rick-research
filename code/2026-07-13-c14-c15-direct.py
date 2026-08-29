"""Day 94 CODE — Direct witness check for β'(14)=21 and β'(15)=19.

Uses Q_k catalog directly to evaluate h_k^{(c)}(a, b) = (a+3)_L (b+2)_L Q_k(a, b, c)
at any (a, b). For k <= 6 uses the closed-form Q_k. For k = 7, ..., c-1 extracts
h_k^{(c)}(a, b) as bivariate polynomial via extract_h_k pipeline (a >= b >= c
samples), then evaluates at small (a, b).

For each candidate witness (a*, b*, k*), computes:
  H_{c}(a*, b*, k*) = sum_{k=0}^{k*} h_k^{(c)}(a*, b*) * C(k*, k)
and reports v_2(H) and per-summand v_2.
"""
import json
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, Matrix, Rational, expand, sympify, lambdify

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


def load_Q_catalog():
    with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json') as f:
        d = json.load(f)
    a, b, c = symbols('a b c')
    Q = {}
    for k_str, poly_str in d['Q_k_low_k'].items():
        Q[int(k_str)] = sympify(poly_str)
    for k_str, entry in d['Q_k_extended'].items():
        if entry is None:
            continue
        Q[int(k_str)] = sympify(entry['poly_expanded'])
    return Q


def hk_from_catalog(Q_k_abc, c_val, k, a_val, b_val):
    """Compute h_k^{(c=c_val)}(a_val, b_val) via Q_k catalog."""
    L = c_val - 1 - k
    if L < 0:
        return None
    a_s, b_s, c_s = symbols('a b c')
    Qval = int(Q_k_abc.subs({a_s: a_val, b_s: b_val, c_s: c_val}))
    poch_a = rising_fact(a_val + 3, L)
    poch_b = rising_fact(b_val + 2, L)
    return poch_a * poch_b * Qval


def extract_hk_bivariate(c_val, k_target, verbose=False):
    """Extract h_k^{(c=c_val)}(a, b) as bivariate polynomial via extract_h_k
    sampling. Returns a callable (a, b) -> int via lambdified poly."""
    print(f"  [extracting h_{{k={k_target}}} for c={c_val}...]", flush=True)
    t0 = time.time()
    tables = build_e2_tables(max_j=k_target + 2)
    # Need enough samples for total-deg ~ 2*(c-1-k_target) + poly-in-a-b in Q_k.
    # Sample width w gives w(w+1)/2 samples. h_k has total degree 2(c-1-k)+
    # (deg of Q_k). For safety use enough samples for deg ~ 2c.
    max_deg = 2 * (c_val - 1)
    # Need > (max_deg+1)(max_deg+2)/2 monomials.
    N_needed = (max_deg + 1) * (max_deg + 2) // 2 + 20
    # width w, samples w(w+1)/2 -> w ~ sqrt(2 N_needed)
    w = int((2 * N_needed) ** 0.5) + 5
    if verbose:
        print(f"    max_deg = {max_deg}, target samples = {N_needed}, width = {w}")
    a_s, b_s = symbols('a b')
    samples = []
    for a in range(c_val, c_val + w):
        for b in range(c_val, a + 1):
            hks = extract_h_k(a, b, c_val, k_target, tables)
            if hks is None:
                continue
            samples.append((a, b, hks[k_target]))
            if len(samples) >= N_needed + 30:
                break
        if len(samples) >= N_needed + 30:
            break
    if verbose:
        print(f"    collected {len(samples)} samples in {time.time()-t0:.1f}s", flush=True)
    if not samples:
        return None
    # Fit
    for D in range(max_deg + 1):
        monomials = [(da, db) for da in range(D + 1) for db in range(D + 1 - da)]
        N = len(monomials)
        if len(samples) < N + 3:
            continue
        rows = []
        yvals = []
        # Only use first N + 20 samples to speed rref
        use_samples = samples[:N + 20]
        for (av, bv, yv) in use_samples:
            rows.append([av ** da * bv ** db for (da, db) in monomials])
            yvals.append(yv)
        t1 = time.time()
        M = Matrix(rows)
        y = Matrix(yvals)
        aug = M.row_join(y)
        rref, pivots = aug.rref()
        if verbose:
            print(f"    D={D}: rref {time.time()-t1:.1f}s, pivots={len(pivots)}/{N+1}", flush=True)
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
        # Verify against ALL samples
        bad = False
        for (av, bv, yv) in samples:
            got = poly.subs({a_s: av, b_s: bv})
            if got != yv:
                bad = True
                break
        if bad:
            continue
        print(f"    fit at deg {D} ({N} monomials, {len(samples)} samples). "
              f"Total time: {time.time()-t0:.1f}s", flush=True)
        return poly
    print(f"  [extraction FAILED for k={k_target}, c={c_val}]", flush=True)
    return None


class HkEvaluator:
    """Evaluate h_k^{(c)}(a, b) at any (a, b) using catalog Q_k or extraction."""
    def __init__(self, c_val, k_max, Q_catalog):
        self.c = c_val
        self.k_max = k_max
        self.Q_catalog = Q_catalog
        self.poly_cache = {}  # k -> lambdified fn OR None if extract failed
        self.direct_Q = {}  # k -> Q_k(a, b) (sympy) if from catalog
        a_s, b_s = symbols('a b')
        for k in range(k_max + 1):
            if k in Q_catalog:
                # Use catalog: precompute Q_k(a, b) at c = c_val
                a_sym, b_sym, c_sym = symbols('a b c')
                Q_ab = expand(Q_catalog[k].subs(c_sym, c_val))
                self.direct_Q[k] = Q_ab
                fQ = lambdify((a_s, b_s), Q_ab, "math")
                L = c_val - 1 - k
                def make_hk(fQ_bound, L_bound):
                    def hk(a, b):
                        Qv = int(fQ_bound(a, b))
                        pa = rising_fact(a + 3, L_bound)
                        pb = rising_fact(b + 2, L_bound)
                        return pa * pb * Qv
                    return hk
                self.poly_cache[k] = make_hk(fQ, L)
            else:
                # Extract h_k as bivariate polynomial
                poly = extract_hk_bivariate(c_val, k, verbose=True)
                if poly is None:
                    self.poly_cache[k] = None
                else:
                    f_poly = lambdify((a_s, b_s), poly, "math")
                    def make_direct(f_bound):
                        def hk(a, b):
                            return int(f_bound(a, b))
                        return hk
                    self.poly_cache[k] = make_direct(f_poly)

    def eval(self, a, b, k):
        f = self.poly_cache.get(k)
        if f is None:
            return None
        return f(a, b)


def check_witness(evaluator, c_val, a_star, b_star, k_star, label=""):
    print(f"\n[witness] {label}: (a*,b*,k*)=({a_star},{b_star},{k_star}), c={c_val}", flush=True)
    summands = []
    total = 0
    for k in range(k_star + 1):
        hk = evaluator.eval(a_star, b_star, k)
        if hk is None:
            print(f"    k={k}: h_k evaluation FAILED")
            summands.append((k, None, None, None, None))
            continue
        weight = Cn(k_star, k)
        contrib = weight * hk
        total += contrib
        summands.append((k, hk, weight, contrib, v2(contrib)))
    v_total = v2(total)
    carrier = summands[k_star]
    carrier_v = carrier[4] if carrier[4] is not None else None
    others = [s[4] for i, s in enumerate(summands) if i != k_star and s[4] is not None]
    if others and carrier_v is not None:
        ok = all(x > carrier_v for x in others)
        min_other = min(others)
    else:
        ok = None
        min_other = None
    print(f"    H_{c_val} = {total}", flush=True)
    print(f"    v_2(H) = {v_total},  carrier v_2 = {carrier_v},  distinct-min: {ok}", flush=True)
    print(f"    per-k v_2: {[s[4] for s in summands]}", flush=True)
    return total, v_total, ok, carrier_v, summands


def scan_kstar_min(evaluator, c_val, k_star, ab_max=32):
    """Scan (a, b) for smallest v_2(H_c) at fixed k*."""
    parity = c_val % 2
    best_v = float('inf')
    best_ab = None
    for a in range(ab_max):
        for b in range(ab_max):
            if (a + b) % 2 != parity:
                continue
            total = 0
            bad = False
            for k in range(k_star + 1):
                hk = evaluator.eval(a, b, k)
                if hk is None:
                    bad = True
                    break
                total += Cn(k_star, k) * hk
            if bad:
                continue
            v = v2(total)
            if v < best_v:
                best_v = v
                best_ab = (a, b)
    return best_v, best_ab


def main():
    print("=" * 74)
    print("Day 94 CODE — Direct witness check for β'(14), β'(15)")
    print("=" * 74, flush=True)

    Q_catalog = load_Q_catalog()
    print(f"Q_k catalog: k ∈ {sorted(Q_catalog.keys())}", flush=True)

    # ==============
    # c = 14
    # ==============
    print("\n" + "=" * 74)
    print("c = 14, β(14) = 23, predicted β'(14) = 21 (D=2)", flush=True)
    print("=" * 74, flush=True)

    # Build evaluator for k = 0..6 (catalog) and k=7 (extraction).
    # Achievers: report mentions (0,0), (2,0) — both even, matches shell.
    # Since c=14 has "many" argmin k, we need k >= 6 achievers at LB=21.
    # Let's include k=7 via extraction and stop there.
    k_max_14 = 7
    print(f"\nBuilding HkEvaluator with k_max={k_max_14}...", flush=True)
    t0 = time.time()
    ev14 = HkEvaluator(14, k_max_14, Q_catalog)
    print(f"  built in {time.time()-t0:.1f}s", flush=True)

    # Check achievers named in report
    for (a, b, k_star) in [(0, 0, 5), (0, 0, 6), (0, 0, 7),
                            (2, 0, 5), (2, 0, 6), (2, 0, 7),
                            (0, 2, 5), (0, 2, 6), (0, 2, 7),
                            (2, 2, 5), (2, 2, 6), (2, 2, 7)]:
        check_witness(ev14, 14, a, b, k_star, f"c=14 achiever")

    # Scan to find global min v_2(H_14):
    print("\n[scan] c=14, over (a,b) in [0, 16)^2 (a+b even), k* in [0, 7]:", flush=True)
    per_kstar = {}
    for k_star in range(k_max_14 + 1):
        t0 = time.time()
        v, ab = scan_kstar_min(ev14, 14, k_star, ab_max=16)
        print(f"    k*={k_star}: min v_2(H) = {v} at (a,b)={ab}   [{time.time()-t0:.1f}s]", flush=True)
        per_kstar[k_star] = (v, ab)

    min_v_14 = min(v for v, _ in per_kstar.values())
    argmin_14 = [k for k, (v, _) in per_kstar.items() if v == min_v_14]
    print(f"\n[c=14 result] global scan min v_2(H_14) = {min_v_14} at k* ∈ {argmin_14}", flush=True)
    print(f"  predicted β'(14) = 21   =>   {'MATCH' if min_v_14 == 21 else ('UNDER' if min_v_14 < 21 else 'OVER')}", flush=True)

    # ==============
    # c = 15
    # ==============
    print("\n" + "=" * 74)
    print("c = 15, β(15) = 25, predicted β'(15) = 19 (D=6)", flush=True)
    print("=" * 74, flush=True)

    # Report says argmin k=7 uniquely, achiever (a,b)=(6,7). Since we need k=7,
    # extract.
    k_max_15 = 7
    print(f"\nBuilding HkEvaluator with k_max={k_max_15}...", flush=True)
    t0 = time.time()
    ev15 = HkEvaluator(15, k_max_15, Q_catalog)
    print(f"  built in {time.time()-t0:.1f}s", flush=True)

    # Named achiever from dream journal: (6, 7) at k*=7. Both a+b odd (matches shell).
    for (a, b, k_star) in [(6, 7, 7), (7, 6, 7), (7, 8, 7), (8, 7, 7),
                             (6, 7, 6), (6, 7, 5)]:
        check_witness(ev15, 15, a, b, k_star, f"c=15 achiever")

    # Scan
    print("\n[scan] c=15, over (a,b) in [0, 16)^2 (a+b odd), k* in [0, 7]:", flush=True)
    per_kstar15 = {}
    for k_star in range(k_max_15 + 1):
        t0 = time.time()
        v, ab = scan_kstar_min(ev15, 15, k_star, ab_max=16)
        print(f"    k*={k_star}: min v_2(H) = {v} at (a,b)={ab}   [{time.time()-t0:.1f}s]", flush=True)
        per_kstar15[k_star] = (v, ab)

    min_v_15 = min(v for v, _ in per_kstar15.values())
    argmin_15 = [k for k, (v, _) in per_kstar15.items() if v == min_v_15]
    print(f"\n[c=15 result] global scan min v_2(H_15) = {min_v_15} at k* ∈ {argmin_15}", flush=True)
    print(f"  predicted β'(15) = 19   =>   {'MATCH' if min_v_15 == 19 else ('UNDER' if min_v_15 < 19 else 'OVER')}", flush=True)

    # Summary
    print("\n" + "=" * 74)
    print("SUMMARY")
    print("=" * 74)
    print(f"  c=14: scan min v_2 = {min_v_14}   predicted 21   =>   "
          f"{'FORMULA CORRECT' if min_v_14 == 21 else ('formula OVERSHOOTS' if min_v_14 < 21 else 'formula UNDERSHOOTS (v_2 > predicted)')}")
    print(f"  c=15: scan min v_2 = {min_v_15}   predicted 19   =>   "
          f"{'FORMULA CORRECT' if min_v_15 == 19 else ('formula OVERSHOOTS' if min_v_15 < 19 else 'formula UNDERSHOOTS (v_2 > predicted)')}")


if __name__ == "__main__":
    main()
