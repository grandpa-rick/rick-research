"""Day 90/91 CODE — Direct shell-min of v_2(h_k^{(c)}(a, b)) without
Poch-min restriction. Complements 2026-07-12-Delta-k-c-catalog.py by
handling the parity-mismatch cases (Δ = inf due to empty Poch-min ∩ shell).

For each (c, k), compute
    LB_k^{(c)} := min_{(a,b) ∈ SHELL, [0, 2^T)^2} v_2(h_k^{(c)}(a, b)).

Uses Q_k catalog + Pochhammer product to evaluate h_k directly.
For k ≥ 7, uses extracted bivariate polynomials.

Output: code/2026-07-12-hk-shell-min-output.txt
Merged into: code/2026-07-12-Delta-k-c-catalog.json (adds 'LB_direct' field).
"""
import json
import sys
import time
from importlib import util
from math import factorial

from sympy import symbols, sympify, expand, lambdify, Poly

spec = util.spec_from_file_location(
    "hkfit", "/home/agent/projects/code/2026-07-10-hk-three-var-fit.py"
)
hkfit = util.module_from_spec(spec)
spec.loader.exec_module(hkfit)

spec2 = util.spec_from_file_location(
    "dcat", "/home/agent/projects/code/2026-07-12-Delta-k-c-catalog.py"
)
dcat = util.module_from_spec(spec2)
spec2.loader.exec_module(dcat)


def v2_int(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    v = 0
    while n & 1 == 0:
        n >>= 1
        v += 1
    return v


def build_hk_bivariate(c_val, k, Q_catalog):
    """Return h_k^{(c=c_val)}(a, b) as a sympy poly in (a, b).

    Uses Q_k catalog if available; else extracts via pipeline.
    """
    a_s, b_s = symbols('a b')
    L = c_val - 1 - k
    if L < 0:
        return None
    if k in Q_catalog:
        Q_ab = dcat.poly_at_c(Q_catalog[k], c_val)
        poch_a = dcat.rising_fact(a_s + 3, L)
        poch_b = dcat.rising_fact(b_s + 2, L)
        return expand(poch_a * poch_b * Q_ab)
    else:
        # Extract h_k directly.
        return dcat.extract_hk_bivariate(c_val, k)


def shell_min_v2(hk_ab, c_val, search_T=8):
    """min_{(a,b) shell, [0, 2^T)^2} v_2(h_k(a,b))."""
    a_s, b_s = symbols('a b')
    f = lambdify((a_s, b_s), hk_ab, modules='math')
    parity = c_val % 2
    N = 1 << search_T
    min_v = float('inf')
    achievers = []
    for a in range(N):
        for b in range(N):
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
    return min_v, achievers


def main():
    print("=" * 74)
    print("Day 90/91 CODE — Direct shell-min of v_2(h_k^{(c)}(a,b))")
    print("=" * 74)

    Q_catalog = dcat.load_Q_catalog()
    print(f"Q_k available for k ∈ {sorted(Q_catalog.keys())}")

    # Load existing Δ catalog to merge
    catalog_path = '/home/agent/projects/code/2026-07-12-Delta-k-c-catalog.json'
    with open(catalog_path) as f:
        cat_full = json.load(f)
    cat_data = cat_full['data']

    lb_direct = {}
    c_range = list(range(5, 12))
    for c_val in c_range:
        print(f"\n{'=' * 60}")
        print(f"c = {c_val}, shell a+b ≡ {c_val % 2}")
        print(f"{'=' * 60}")
        for k in range(c_val):
            t0 = time.time()
            hk = build_hk_bivariate(c_val, k, Q_catalog)
            if hk is None:
                print(f"  k={k}: h_k build FAILED")
                continue
            search_T = 8 if k <= 5 else 7
            lb, ach = shell_min_v2(hk, c_val, search_T=search_T)
            dt = time.time() - t0
            # existing Δ result
            key = f"c{c_val},k{k}"
            existing = cat_data.get(key, {})
            delta = existing.get('Delta')
            lb_pochmin = existing.get('LB')
            ach_str = ", ".join(f"({a},{b},v2={v})" for a, b, v in ach[:3])
            match = "" if lb_pochmin == lb else f"  [DIFF from Poch-min LB={lb_pochmin}]"
            print(f"  k={k}: LB_direct = {lb}   [{dt:.1f}s]{match}")
            print(f"       achievers: {ach_str}")
            lb_direct[key] = {
                'LB_direct': lb,
                'achievers_direct': [list(x) for x in ach[:5]],
                'search_T': search_T,
            }

    # Merge back into catalog
    for k, v in lb_direct.items():
        cat_data[k].update(v)
    cat_full['note_v2'] = 'Extended with LB_direct = min v_2(h_k) over shell in [0, 2^search_T)^2.'
    with open(catalog_path, 'w') as f:
        json.dump(cat_full, f, indent=2, default=str)
    print(f"\nMerged into {catalog_path}")

    # Summary table
    print("\n" + "=" * 74)
    print("SUMMARY: LB_direct (min v_2(h_k^{(c)}) over shell)")
    print("=" * 74)
    header = "  c\\k |" + "".join(f"{k:>7d}" for k in range(11))
    print(header)
    print("  " + "-" * (len(header) - 2))
    for c_val in c_range:
        row = f"  {c_val:>3d} |"
        for k in range(11):
            key = f"c{c_val},k{k}"
            if key in lb_direct:
                v = lb_direct[key]['LB_direct']
                s = str(v) if v != float('inf') else "inf"
            else:
                s = "-"
            row += f"{s:>7s}"
        print(row)

    print("\nmin_k LB_direct per c (predicted β'(c)):")
    for c_val in c_range:
        vals = [lb_direct[f"c{c_val},k{k}"]['LB_direct']
                for k in range(c_val)
                if f"c{c_val},k{k}" in lb_direct]
        vals_finite = [v for v in vals if v != float('inf')]
        if not vals_finite:
            print(f"  c={c_val}: no data")
            continue
        m = min(vals_finite)
        argmin = [k for k in range(c_val)
                  if lb_direct.get(f"c{c_val},k{k}", {}).get('LB_direct') == m]
        print(f"  c={c_val}: min LB_direct = {m} at k* ∈ {argmin}")


if __name__ == "__main__":
    main()
