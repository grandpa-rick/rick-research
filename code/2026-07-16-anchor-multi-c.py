"""Day 98 PROVE — Anchor evaluation at (0, (c-2)/4) for k=0..6, multiple c.

Purpose: Quick sanity check using catalog Q_k (k=0..6) at the interior
anchor (a*, b*) = (0, (c-2)/4) for c ∈ {10, 18, 26, 34, 42}.

Reports v_2(h_k(0, (c-2)/4, c)) for each (c, k) pair, decomposed as:
    v_2(h_k) = v_2((3)_L) + v_2((κ+2)_L) + v_2(Q_k(0, κ, c))
where κ = (c-2)/4 and L = c-1-k.

This does NOT confirm the anchor at c ≥ 18 for k* > 6 — only checks the
low-k regime and shows the trend.
"""
import json
from sympy import symbols, sympify, Integer, factor

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


def rising(x, n):
    if n <= 0:
        return 1
    p = 1
    for i in range(n):
        p *= x + i
    return p


def load_catalog():
    with open(CATALOG_PATH) as f:
        cat = json.load(f)
    a, b, c = symbols('a b c')
    Q = {}
    for k in range(6):
        Q[k] = sympify(cat['Q_k_low_k'][str(k)])
    # k=6 factored form
    Q[6] = sympify(cat['Q_k_extended']['6']['poly_expanded'])
    return Q


def beta(c):
    """β(c) = 2(c-1) - s_2(c-1)."""
    v = 0
    n = c - 1
    while n:
        v += n & 1
        n >>= 1
    return 2 * (c - 1) - v


def main():
    a, b, c = symbols('a b c')
    Q = load_catalog()

    C_LIST = [10, 18, 26, 34, 42]

    print("=" * 78)
    print("Interior anchor (0, (c-2)/4) evaluation via catalog Q_k, k=0..6")
    print("=" * 78)
    print(f"β(c) closed form = 2(c-1) - s_2(c-1)")
    print()

    all_results = {}
    for c_val in C_LIST:
        kappa = (c_val - 2) // 4
        assert (c_val - 2) % 4 == 0, f"c={c_val} not ≡ 2 mod 4"
        beta_c = beta(c_val)
        print(f"\n--- c = {c_val}, κ = (c-2)/4 = {kappa}, β(c) = {beta_c} ---")
        print(f"  Anchor: (a*, b*) = (0, {kappa})")
        print(f"  Predicted k* = (c-2)/2 = {(c_val - 2) // 2}, L* = c/2 = {c_val // 2}")

        # Compute for each k = 0..6.
        rows = []
        for k in range(7):
            if k > c_val - 3:
                continue
            L = c_val - 1 - k
            # (a+3)_L at a=0 = (3)_L
            p1 = rising(3, L)
            # (b+2)_L at b=κ = (κ+2)_L
            p2 = rising(kappa + 2, L)
            # Q_k at (0, κ, c)
            Qk_val = int(Q[k].subs({a: 0, b: kappa, c: c_val}))
            h_val = p1 * p2 * Qk_val
            v2_p1 = v2(p1)
            v2_p2 = v2(p2)
            v2_Q = v2(Qk_val)
            v2_h = v2(h_val)
            rows.append({
                'k': k, 'L': L, 'p1': p1, 'p2': p2, 'Q': Qk_val, 'h': h_val,
                'v2_p1': v2_p1, 'v2_p2': v2_p2, 'v2_Q': v2_Q, 'v2_h': v2_h,
            })
            print(f"  k={k:>2}: L={L:>2}, v_2((3)_L)={v2_p1:>3}, "
                  f"v_2(({kappa+2})_L)={v2_p2:>3}, v_2(Q_k)={v2_Q:>3}, "
                  f"v_2(h_k)={v2_h}")

        vs = [r['v2_h'] for r in rows if r['v2_h'] is not None]
        min_v = min(vs) if vs else None
        argmin = [r['k'] for r in rows if r['v2_h'] == min_v]
        print(f"  min over k=0..6: v_2 = {min_v} at k = {argmin}")
        print(f"  β(c) − min_v = {beta_c - min_v if min_v is not None else 'N/A'}")

        all_results[c_val] = rows

    # Save.
    out = {
        'note': 'Anchor v_2 at (0, (c-2)/4) for k=0..6 via catalog Q_k.',
        'anchor_formula': '(a*, b*) = (0, (c-2)/4); k* = (c-2)/2; L* = c/2',
        'per_c': {str(k): v for k, v in all_results.items()},
    }
    out_path = '/home/agent/projects/code/2026-07-16-anchor-multi-c.json'
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {out_path}")


if __name__ == '__main__':
    main()
