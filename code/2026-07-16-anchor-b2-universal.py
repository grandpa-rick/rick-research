"""Day 98 PROVE — Test: is (a, b) = (0, 2) with k ∈ {4, 5, 6} the UNIVERSAL
interior anchor for c ≡ 2 mod 8?

Compute D_★_k(c) at (0, 2) for k = 4, 5, 6 via catalog Q_k.
Compare to D_pred = 1 + s_2(m-1).
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

    print("=" * 92)
    print("Test: universal anchor (0, 2) for c ≡ 2 mod 8")
    print("=" * 92)
    print(f"{'m':>3} {'c':>4}"
          + " || " + "".join(f"  v_2(h_{k}(0,2))" for k in range(7))
          + f" || {'min_v':>5}  {'D_(0,2)':>8}  {'D_pred':>7}  {'match':>6}")
    print("-" * 130)
    matches = 0
    total = 0
    for m in range(2, 33, 2):
        c_val = 4 * m + 2
        beta_c = beta(c_val)
        vs = []
        for k in range(7):
            if k > c_val - 3:
                vs.append(None)
                continue
            L = c_val - 1 - k
            p1 = rising(3, L)
            p2 = rising(4, L)  # b=2, so (b+2)_L = (4)_L
            Qk = int(Q[k].subs({a: 0, b: 2, c: c_val}))
            h = p1 * p2 * Qk
            vs.append(v2(h))
        finite = [v for v in vs if v is not None]
        min_v = min(finite)
        D02 = beta_c - min_v
        D_pred = 1 + s2(m - 1)
        match = "✓" if D02 == D_pred else "✗"
        if match == "✓":
            matches += 1
        total += 1
        line = f"{m:>3} {c_val:>4}"
        line += " || " + "".join(f"  {v:>10}" if v is not None else "  --" for v in vs)
        line += f" || {min_v:>5}  {D02:>8}  {D_pred:>7}  {match:>6}"
        print(line)

    print(f"\n(0, 2) anchor: {matches}/{total} match D_pred")

    # Also compare to (0, (c-2)/4) principal:
    print("\n\n=== BOTH anchors: (0, 2) principal-check vs (0, (c-2)/4) ===")
    print(f"{'m':>3} {'c':>4} {'D_(0,2)':>8} {'D_(0,κ)':>8} {'D_pred':>7}")
    for m in range(2, 33, 2):
        c_val = 4 * m + 2
        beta_c = beta(c_val)
        # (0, 2)
        vs_02 = []
        for k in range(7):
            if k > c_val - 3:
                continue
            L = c_val - 1 - k
            p1 = rising(3, L); p2 = rising(4, L)
            Qk = int(Q[k].subs({a: 0, b: 2, c: c_val}))
            vs_02.append(v2(p1 * p2 * Qk))
        # (0, κ)
        kappa = m
        vs_0k = []
        for k in range(7):
            if k > c_val - 3:
                continue
            L = c_val - 1 - k
            p1 = rising(3, L); p2 = rising(kappa + 2, L)
            Qk = int(Q[k].subs({a: 0, b: kappa, c: c_val}))
            vs_0k.append(v2(p1 * p2 * Qk))
        D02 = beta_c - min(vs_02)
        D0k = beta_c - min(vs_0k)
        Dpred = 1 + s2(m - 1)
        print(f"{m:>3} {c_val:>4} {D02:>8} {D0k:>8} {Dpred:>7}")


if __name__ == '__main__':
    main()
