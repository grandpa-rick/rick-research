"""Day 98 PROVE — Full D_★ table for anchor (0, (c-2)/4) at k=0..6.

For each c ≡ 2 mod 4 in a wide range, compute:
    v_2(h_k^{(c)}(0, (c-2)/4)) for k = 0..6 via catalog
    D_★_k(c) = β(c) - v_2(h_k)
    D_★(c) = max_k D_★_k  (this is the corner-derived D from anchor + k∈[0,6])

Then compare to D_emp(c) (from digit-sum formula, for reference).

Rick's honesty: D_emp is what we're trying to PROVE. So we compare in Phase 4.
"""
import json
from sympy import symbols, sympify

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


def main():
    a, b, c = symbols('a b c')
    Q = load_catalog()

    # c ≡ 2 mod 8 (m even in c = 4m+2): m = 2, 4, 6, 8, 10, ..., 30
    print("=" * 100)
    print("D_★_k(c) table at anchor (0, (c-2)/4) for c ≡ 2 mod 8")
    print("=" * 100)

    K_MAX = 6
    print(f"{'m':>3} {'c':>3} {'β':>4}  " + "  ".join(f"v_2(h_{k})" for k in range(K_MAX + 1))
          + f"  {'min_v':>5} {'D_★':>4}")
    print("-" * 100)

    per_c = []
    for m in range(2, 33, 2):  # m even → c ≡ 2 mod 8
        c_val = 4 * m + 2
        kappa = m
        beta_c = beta(c_val)
        vs = []
        for k in range(K_MAX + 1):
            if k > c_val - 3:
                vs.append(None)
                continue
            L = c_val - 1 - k
            p1 = rising(3, L)
            p2 = rising(kappa + 2, L)
            Qk = int(Q[k].subs({a: 0, b: kappa, c: c_val}))
            h = p1 * p2 * Qk
            vs.append(v2(h))
        finite = [v for v in vs if v is not None]
        min_v = min(finite)
        D_star = beta_c - min_v
        line = f"{m:>3} {c_val:>3} {beta_c:>4}  "
        for v in vs:
            line += f"{v if v is not None else '-':>8}  "
        line += f"{min_v:>5} {D_star:>4}"
        print(line)
        per_c.append({'m': m, 'c': c_val, 'beta': beta_c, 'v2_h_by_k': vs,
                      'min_v': min_v, 'D_star': D_star})

    # Compare to D_pred = 1 + s_2(m-1) for c = 4m+2.
    print("\n" + "=" * 100)
    print("D_★ vs D_pred = 1 + s_2(m-1) [PHASE 4: SEALED comparison]")
    print("=" * 100)
    print(f"{'m':>3} {'c':>3} {'D_★':>4} {'D_pred':>7} {'match':>7}")
    print("-" * 40)
    matches = 0
    total = 0
    for r in per_c:
        D_pred = 1 + s2(r['m'] - 1)
        match = "✓" if r['D_star'] == D_pred else "✗"
        if r['D_star'] == D_pred:
            matches += 1
        total += 1
        print(f"{r['m']:>3} {r['c']:>3} {r['D_star']:>4} {D_pred:>7} {match:>7}")
        r['D_pred'] = D_pred
        r['match'] = (r['D_star'] == D_pred)

    print(f"\nMatches: {matches}/{total}")

    out = {
        'note': 'D_★ at anchor (0, (c-2)/4) via catalog Q_k for c ≡ 2 mod 8, m=2..32.',
        'K_MAX': K_MAX,
        'per_c': per_c,
    }
    with open('/home/agent/projects/code/2026-07-16-anchor-Dstar-table.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print("Saved /home/agent/projects/code/2026-07-16-anchor-Dstar-table.json")


if __name__ == '__main__':
    main()
