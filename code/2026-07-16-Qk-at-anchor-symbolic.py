"""Day 98 PROVE — Symbolic Q_k(0, (c-2)/4, c) for k = 0..6.

For c ≡ 2 mod 4, substitute a = 0, b = (c-2)/4 into catalog Q_k.
Report factored form. Then compute v_2 numerically at c ∈ {10, 18, 26, 34, 42, 50, 58, 66}
and try to fit a c-uniform closed form.

Then combine with (3)_{c-1-k} and ((c+6)/4)_{c-1-k} Pochhammer valuations
via AMM to derive v_2(h_k^{(c)}(0, (c-2)/4)) c-uniformly.

SEALED against empirical D(c). Only compare in Phase 4.
"""
import json
from sympy import symbols, sympify, expand, factor, Rational, simplify, collect, Poly


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


def load_catalog():
    with open(CATALOG_PATH) as f:
        cat = json.load(f)
    Q = {}
    for k in range(6):
        Q[k] = sympify(cat['Q_k_low_k'][str(k)])
    Q[6] = sympify(cat['Q_k_extended']['6']['poly_expanded'])
    return Q


def main():
    a, b, c = symbols('a b c')
    m = symbols('m', integer=True, nonnegative=True)  # c = 4m + 2
    Q = load_catalog()

    print("=" * 78)
    print("Q_k(0, (c-2)/4, c) — symbolic evaluation at interior anchor")
    print("SEALED against empirical D(c)")
    print("=" * 78)

    Q_at_anchor_sub_m = {}
    for k in range(7):
        Qk = Q[k]
        # Substitute a = 0, b = (c-2)/4.
        Qk0 = Qk.subs({a: 0, b: (c - 2) / 4})
        # Then substitute c = 4m + 2.
        Qk_m = Qk0.subs({c: 4 * m + 2})
        Qk_m_simp = expand(Qk_m)
        Qk_m_fact = factor(Qk_m_simp)
        Q_at_anchor_sub_m[k] = (Qk_m_simp, Qk_m_fact)

        # Report.
        print(f"\n--- k = {k} ---")
        print(f"  Q_k(0, (c-2)/4, c) with c = 4m + 2:")
        print(f"    expanded: {Qk_m_simp}")
        print(f"    factored: {Qk_m_fact}")

    # Numeric verification: evaluate at m = 2 (c=10), 4 (c=18), 6 (c=26),
    # 8 (c=34), 10 (c=42), 12 (c=50), 14 (c=58), 16 (c=66).
    print("\n" + "=" * 78)
    print("Numeric v_2(Q_k(0, (c-2)/4, c)) at c = 4m + 2 for various m")
    print("=" * 78)
    m_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    row_hdr = "  m | c  | " + " | ".join(f"Q_{k}" for k in range(7))
    print(row_hdr)
    print("  " + "-" * (len(row_hdr) - 2))
    Q_vals = {}
    for m_val in m_list:
        c_val = 4 * m_val + 2
        vals = []
        for k in range(7):
            val = int(Q_at_anchor_sub_m[k][0].subs(m, m_val))
            v = v2(val) if val != 0 else None
            vals.append(v)
            Q_vals.setdefault(k, []).append((m_val, c_val, val, v))
        row = f"  {m_val:>2} | {c_val:>2} | " + " | ".join(
            f"{v:>3}" if v is not None else "  0" for v in vals)
        print(row)

    # Now try to identify a closed form for v_2(Q_k(0, (c-2)/4, c))
    # in terms of m for each k.
    print("\n" + "=" * 78)
    print("v_2(Q_k(0, (c-2)/4, c)) as function of m — closed form hunt")
    print("=" * 78)
    for k in range(7):
        vs = [v for (mv, cv, val, v) in Q_vals[k]]
        print(f"\nk = {k}:  v_2 = {vs}")
        # try simple formulas
        # Reference: v_2(m), v_2(m+1), v_2(m-1), s_2(m), etc.
        m_vals_list = [mv for (mv, cv, val, v) in Q_vals[k]]
        for label, fn in [
            ('v_2(m)', lambda mv: v2(mv)),
            ('v_2(m+1)', lambda mv: v2(mv + 1)),
            ('v_2(m-1)', lambda mv: v2(mv - 1)),
            ('s_2(m)', lambda mv: s2(mv)),
            ('s_2(m-1)', lambda mv: s2(mv - 1)),
            ('v_2(m)+v_2(m-1)', lambda mv: v2(mv) + (v2(mv-1) if mv > 1 else 0)),
        ]:
            candidates = []
            for (mv, cv, val, v) in Q_vals[k]:
                if mv == 0:
                    continue
                candidates.append(v - fn(mv))
            if candidates and len(set(candidates)) == 1:
                print(f"  MATCH: v_2(Q_{k}(0, (c-2)/4, c)) = {label} + {candidates[0]} const")

    # Save.
    out = {
        'note': 'Q_k(0, (c-2)/4, c) symbolic form and numeric v_2 for k=0..6.',
        'per_k': {},
    }
    for k in range(7):
        out['per_k'][k] = {
            'symbolic_expanded_in_m': str(Q_at_anchor_sub_m[k][0]),
            'symbolic_factored': str(Q_at_anchor_sub_m[k][1]),
            'v2_by_m': [{'m': mv, 'c': cv, 'val': str(val), 'v2': v}
                        for (mv, cv, val, v) in Q_vals[k]],
        }
    with open('/home/agent/projects/code/2026-07-16-Qk-at-anchor-symbolic.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print("\nSaved /home/agent/projects/code/2026-07-16-Qk-at-anchor-symbolic.json")


if __name__ == '__main__':
    main()
