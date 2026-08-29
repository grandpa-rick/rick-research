"""Day 98 PROVE — At failure case c=58 (also c=82, 90, 114, 122),
sweep b along a=0 to find the ACTUAL argmin of v_2(h_k(0, b, c))
over k ∈ [0, 6] and b ∈ [0, 2T-2].

If a different b (not (c-2)/4) achieves lower v_2 at some k ≤ 6,
that's the interior anchor for that c.
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


def T_shell(c):
    """Smallest 2^t > c - 2."""
    t = 1
    while (1 << t) <= c - 2:
        t += 1
    return 1 << t


def main():
    a, b, c = symbols('a b c')
    Q = load_catalog()

    # For each failure c, sweep b at a=0 for k=0..6.
    failure_cs = [58, 82, 90, 114, 122]
    print("=" * 90)
    print("Anchor sweep at a=0, various b, for failure c values")
    print("=" * 90)

    results = {}
    for c_val in failure_cs:
        beta_c = beta(c_val)
        T_val = T_shell(c_val)
        # For c ≡ 2 mod 8, parity a+b even (matching c=even).
        # At a=0, b must be even.
        print(f"\n--- c = {c_val}, β(c) = {beta_c}, T = {T_val} ---")
        print(f"    principal anchor: (0, {(c_val - 2) // 4})")

        best = (None, None, None, None)  # (b, k, v, "b - kappa")
        rows = []
        for b_val in range(0, 2 * T_val, 2):
            for k in range(7):
                if k > c_val - 3:
                    continue
                L = c_val - 1 - k
                p1 = rising(3, L)
                p2 = rising(b_val + 2, L)
                Qk = int(Q[k].subs({a: 0, b: b_val, c: c_val}))
                if Qk == 0:
                    continue
                h = p1 * p2 * Qk
                v = v2(h)
                if v is None:
                    continue
                if best[2] is None or v < best[2]:
                    best = (b_val, k, v, b_val - (c_val - 2) // 4)
                rows.append({'b': b_val, 'k': k, 'v2_h': v})

        b_star, k_star, v_star, delta_b = best
        D_star = beta_c - v_star
        print(f"    argmin over (b, k): (b, k) = ({b_star}, {k_star}), v_2 = {v_star}")
        print(f"    D_★ = β - min = {D_star}")
        print(f"    b_star - κ = {delta_b}")

        # Distribution of top few.
        rows.sort(key=lambda r: r['v2_h'])
        print(f"    Top 8 (b, k) with lowest v_2:")
        for r in rows[:8]:
            print(f"      (b={r['b']:>3}, k={r['k']}), v_2 = {r['v2_h']}")

        results[c_val] = {
            'beta': beta_c, 'T': T_val,
            'best': {'b': b_star, 'k': k_star, 'v2': v_star,
                     'D_star': D_star, 'delta_b': delta_b},
            'top_bk': rows[:15],
        }

    with open('/home/agent/projects/code/2026-07-16-anchor-sweep-a0.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print("\nSaved /home/agent/projects/code/2026-07-16-anchor-sweep-a0.json")


if __name__ == '__main__':
    main()
