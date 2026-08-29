"""FAST version: witness check using Q_k catalog only (k <= 6).

Given the report says argmin_k for c=14 LB=21 is "many" — including low k —
we expect that k*=5 or k*=6 (both in catalog) will achieve v_2 = 21 at some
achiever (a*, b*).

For c=15 the report says argmin k*=7 UNIQUELY. So we need to extract h_7^{(15)}.
But we can still do a lower-bound check: if k*=6 gives v_2 = 20 at witness,
and k*=7 gives v_2 = 19 exact, then β'(15) ≤ 19.

Strategy:
  (i) Fast scan c=14 with k <= 6 catalog. If min v_2(H) = 21, DONE, β'(14)=21.
  (ii) For c=15, evaluate at named achiever (a,b)=(6,7) with k*=7 (need extract h_7).
"""
import json
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, sympify, expand, lambdify

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)


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
    a_s, b_s, c_s = symbols('a b c')
    Q = {}
    for k_str, poly_str in d['Q_k_low_k'].items():
        Q[int(k_str)] = sympify(poly_str)
    for k_str, entry in d['Q_k_extended'].items():
        if entry is None:
            continue
        Q[int(k_str)] = sympify(entry['poly_expanded'])
    return Q


def make_hk_evaluators(c_val, k_max, Q_catalog):
    """Returns dict k -> callable (a, b) -> int giving h_k^{(c=c_val)}(a, b)."""
    a_s, b_s, c_s = symbols('a b c')
    evs = {}
    for k in range(k_max + 1):
        if k not in Q_catalog:
            continue  # skip
        L = c_val - 1 - k
        if L < 0:
            continue
        Q_ab = expand(Q_catalog[k].subs(c_s, c_val))
        fQ = lambdify((a_s, b_s), Q_ab, "math")
        def make_hk(fQ_bd, L_bd):
            def hk(a, b):
                Qv = int(fQ_bd(a, b))
                pa = rising_fact(a + 3, L_bd)
                pb = rising_fact(b + 2, L_bd)
                return pa * pb * Qv
            return hk
        evs[k] = make_hk(fQ, L)
    return evs


def compute_H(evs, a, b, k_star):
    """H_c(a, b, j=k_star) = sum_{k=0..k_star} h_k(a, b) * C(k_star, k)."""
    total = 0
    for k in range(k_star + 1):
        if k not in evs:
            return None
        total += Cn(k_star, k) * evs[k](a, b)
    return total


def check_and_report(evs, c_val, a, b, k_star, label=""):
    print(f"  {label}: (a,b,k*)=({a},{b},{k_star})", flush=True)
    total = compute_H(evs, a, b, k_star)
    if total is None:
        print("    -- k not in catalog, skip", flush=True)
        return None
    v = v2(total)
    per_k = []
    for k in range(k_star + 1):
        if k not in evs:
            per_k.append(None)
            continue
        contrib = Cn(k_star, k) * evs[k](a, b)
        per_k.append(v2(contrib))
    print(f"    H = {total}", flush=True)
    print(f"    v_2(H) = {v}   per-k v_2: {per_k}", flush=True)
    carrier_v = per_k[k_star]
    others = [x for i, x in enumerate(per_k) if i != k_star and x is not None]
    distinct = all(x > carrier_v for x in others) if others else None
    print(f"    carrier v_2 = {carrier_v}, distinct-min: {distinct}", flush=True)
    return v, distinct, carrier_v


def scan_min(evs, c_val, k_star, ab_max=32):
    parity = c_val % 2
    best_v = float('inf')
    best_ab = None
    for a in range(ab_max):
        for b in range(ab_max):
            if (a + b) % 2 != parity:
                continue
            total = compute_H(evs, a, b, k_star)
            if total is None:
                continue
            v = v2(total)
            if v < best_v:
                best_v = v
                best_ab = (a, b)
    return best_v, best_ab


def main():
    print("=" * 74)
    print("Day 94 CODE — FAST witness check for β'(14), β'(15) (catalog only)")
    print("=" * 74, flush=True)

    Q_catalog = load_Q_catalog()
    print(f"Q_k catalog: k ∈ {sorted(Q_catalog.keys())}", flush=True)

    # ============ c = 14 ============
    print("\n" + "=" * 74)
    print("c = 14, β(14) = 23, PREDICTED β'(14) = 21", flush=True)
    print("=" * 74, flush=True)

    t0 = time.time()
    evs14 = make_hk_evaluators(14, 6, Q_catalog)
    print(f"Evaluators built in {time.time()-t0:.1f}s, k in {sorted(evs14.keys())}", flush=True)

    # Named achievers: (0,0), (2,0) (from report). Also try (0,2), (2,2), etc.
    print("\n[named achiever checks]", flush=True)
    for a in [0, 2, 4]:
        for b in [0, 2, 4]:
            if (a + b) % 2 != 14 % 2:
                continue
            for k_star in range(7):
                check_and_report(evs14, 14, a, b, k_star, "c=14")

    # Scan
    print("\n[scan] c=14, ab in [0, 32)^2, k* in [0, 6]:", flush=True)
    per_kstar_14 = {}
    for k_star in range(7):
        t0 = time.time()
        v, ab = scan_min(evs14, 14, k_star, ab_max=32)
        print(f"    k*={k_star}: min v_2(H) = {v} at (a,b)={ab}   [{time.time()-t0:.1f}s]", flush=True)
        per_kstar_14[k_star] = (v, ab)

    min14 = min(v for v, _ in per_kstar_14.values())
    argmin14 = [k for k, (v, _) in per_kstar_14.items() if v == min14]
    print(f"\n[c=14 catalog-only scan] min v_2(H_14) = {min14} at k* ∈ {argmin14}", flush=True)

    # ============ c = 15 ============
    print("\n" + "=" * 74)
    print("c = 15, β(15) = 25, PREDICTED β'(15) = 19", flush=True)
    print("=" * 74, flush=True)

    t0 = time.time()
    evs15 = make_hk_evaluators(15, 6, Q_catalog)
    print(f"Evaluators built in {time.time()-t0:.1f}s, k in {sorted(evs15.keys())}", flush=True)

    # First check without k=7. The formula predicts min at k*=7 with LB=19.
    # If we scan only k*<=6, we may see min at 20 (LB from k<=6 might be higher).
    print("\n[named achiever checks — catalog only]", flush=True)
    for a in [6, 7, 8]:
        for b in [5, 6, 7, 8]:
            if (a + b) % 2 != 15 % 2:
                continue
            for k_star in range(7):
                check_and_report(evs15, 15, a, b, k_star, "c=15")

    print("\n[scan] c=15, ab in [0, 32)^2, k* in [0, 6] (catalog only):", flush=True)
    per_kstar_15 = {}
    for k_star in range(7):
        t0 = time.time()
        v, ab = scan_min(evs15, 15, k_star, ab_max=32)
        print(f"    k*={k_star}: min v_2(H) = {v} at (a,b)={ab}   [{time.time()-t0:.1f}s]", flush=True)
        per_kstar_15[k_star] = (v, ab)

    min15 = min(v for v, _ in per_kstar_15.values())
    argmin15 = [k for k, (v, _) in per_kstar_15.items() if v == min15]
    print(f"\n[c=15 catalog-only scan] min v_2(H_15) = {min15} at k* ∈ {argmin15}", flush=True)

    print("\n" + "=" * 74)
    print("SUMMARY (catalog only, k <= 6):")
    print("=" * 74)
    print(f"  c=14: catalog-scan min v_2 = {min14}   predicted 21")
    print(f"  c=15: catalog-scan min v_2 = {min15}   predicted 19")
    print("\n  Note: c=15 UNIQUE argmin is k=7 per report; catalog-only")
    print("        gives at best k<=6 which may show >= 20.")


if __name__ == "__main__":
    main()
