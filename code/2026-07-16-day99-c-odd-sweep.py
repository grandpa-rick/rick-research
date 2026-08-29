"""Day 99 PROVE Phase 2 — Interior anchor sweep for c odd.

Compute v_2(H_c(a, b, j)) for c ∈ {11, 13}, (a, b) ∈ [0, 15]^2, j ∈ [0, c-1].
Report:
- (a*, b*, j*, k*) minimising v_2
- Argmin family / lattice pattern
- Shift Δa, Δb from corner
- Best k inside j*

If a clean anchor (a*, b*) with k* emerges, register as hunch A2.
"""
import json
from sympy import symbols, sympify
from math import comb


CATALOG_PATH = "/home/agent/projects/code/2026-07-11-Qk-catalog.json"


def v2(n):
    n = int(n)
    if n == 0:
        return None
    n = abs(n)
    v = 0
    while (n & 1) == 0:
        n >>= 1
        v += 1
    return v


def s2(n):
    n = int(n)
    v = 0
    while n:
        v += n & 1
        n >>= 1
    return v


def rising(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= x + i
    return p


def beta(c):
    return 2 * (c - 1) - s2(c - 1)


def load_catalog():
    with open(CATALOG_PATH) as f:
        cat = json.load(f)
    a, b, c = symbols('a b c')
    Q = {}
    for k in range(6):
        Q[k] = sympify(cat['Q_k_low_k'][str(k)])
    Q[6] = sympify(cat['Q_k_extended']['6']['poly_expanded'])
    return Q


A, B, C = symbols('a b c')
Q_SYM = load_catalog()

# Note: We only have k ≤ 6 in the catalog. For c=11, we need k up to c-1=10.
# We use catalog for k ≤ 6 and note the truncation.


def h_k(a_val, b_val, c_val, k):
    """Compute h_k^{(c)}(a, b) = (a+3)_L * (b+2)_L * Q_k(a, b, c)."""
    if k > 6:
        return None  # need extended catalog
    L = c_val - 1 - k
    if L < 0:
        return 0
    p1 = rising(a_val + 3, L)
    p2 = rising(b_val + 2, L)
    Qk = int(Q_SYM[k].subs({A: a_val, B: b_val, C: c_val}))
    return p1 * p2 * Qk


def H_c(a_val, b_val, c_val, j):
    """H_c(a, b, j) = sum_{k=0}^{j} C(j, k) h_k^{(c)}(a, b)."""
    total = 0
    for k in range(0, min(j, 6) + 1):
        hk = h_k(a_val, b_val, c_val, k)
        if hk is None:
            return None  # missing catalog entry
        total += comb(j, k) * hk
    # If j > 6, we're missing terms — but for c=11, j ≤ 10 and we need k up to 6.
    # If j > 6, missing terms are C(j, k) h_k for k ∈ {7, ..., j}.
    if j > 6:
        return None
    return total


def sweep_c(c_val, a_max=15, b_max=15):
    print(f"\n{'=' * 78}")
    print(f"c = {c_val}, β(c) = {beta(c_val)}")
    print(f"{'=' * 78}")
    print(f"Sweeping (a, b, j) in [0, {a_max}] x [0, {b_max}] x [0, 6]")
    print("(j capped at 6 since Q_k catalog only has k ≤ 6)")

    results = []
    for j in range(0, 7):
        for a_val in range(0, a_max + 1):
            for b_val in range(0, b_max + 1):
                Hv = H_c(a_val, b_val, c_val, j)
                if Hv is None or Hv == 0:
                    continue
                v = v2(Hv)
                results.append({'a': a_val, 'b': b_val, 'j': j, 'v2': v})

    if not results:
        print("No valid H_c values computed.")
        return None

    # Global min
    min_v = min(r['v2'] for r in results)
    print(f"\nGlobal min v_2 = {min_v} = β - {beta(c_val) - min_v}")

    # All argmins
    argmins = [r for r in results if r['v2'] == min_v]
    print(f"Number of (a, b, j) argmins: {len(argmins)}")
    print(f"First 20 argmins:")
    for r in sorted(argmins, key=lambda r: (r['j'], r['a'], r['b']))[:20]:
        print(f"  (a={r['a']:>2}, b={r['b']:>2}, j={r['j']}, v_2={r['v2']})")

    # Top per j
    print(f"\nMinimum per j:")
    for j in range(7):
        by_j = [r for r in results if r['j'] == j]
        if not by_j:
            continue
        mn = min(r['v2'] for r in by_j)
        argmn = [r for r in by_j if r['v2'] == mn]
        print(f"  j = {j}: min v_2 = {mn}, count = {len(argmn)}, first 5: "
              f"{[(r['a'], r['b']) for r in sorted(argmn, key=lambda r: (r['a'], r['b']))[:5]]}")

    # For each achiever (a*, b*, j*), look at k breakdown inside H_c
    print(f"\nk-breakdown for first 3 argmins (v_2(C(j*,k) h_k(a*, b*, c)) per k):")
    for r in sorted(argmins, key=lambda r: (r['j'], r['a'], r['b']))[:3]:
        a_val, b_val, j_val = r['a'], r['b'], r['j']
        breakdown = []
        for k in range(0, j_val + 1):
            hk = h_k(a_val, b_val, c_val, k)
            if hk == 0:
                breakdown.append((k, '0', None))
            else:
                Chk = comb(j_val, k) * hk
                breakdown.append((k, comb(j_val, k), v2(Chk) if Chk != 0 else None))
        print(f"  (a={a_val}, b={b_val}, j={j_val}):")
        for k, C_jk, v in breakdown:
            print(f"    k={k}: C({j_val},{k})={C_jk}, v_2(C*h_k) = {v}")

    return {
        'c': c_val,
        'beta': beta(c_val),
        'min_v2': min_v,
        'argmins': argmins,
        'k_breakdown_top3': [(r['a'], r['b'], r['j']) for r in
                             sorted(argmins, key=lambda r: (r['j'], r['a'], r['b']))[:3]]
    }


def main():
    all_results = {}
    for c_val in [11, 13, 15]:
        # Also try c = 15 to see if pattern extends
        r = sweep_c(c_val, a_max=15, b_max=15)
        all_results[c_val] = r

    with open('/home/agent/projects/code/2026-07-16-day99-c-odd-sweep.json', 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print("\nSaved.")


if __name__ == '__main__':
    main()
