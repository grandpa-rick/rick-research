"""Day 99 PROVE G1 — Q_j(0, 2, c) closed forms for j in {0, 1, 2, 3, 5, 6}.

Goal: prove single-carrier SCP at (a, b) = (0, 2), j = 4, k = 4 for all
c ≡ 2 mod 4, c ≥ 6. Need Q_j(0, 2, c) closed form for j != 4.

Then evaluate:
    v_2(h_j^{(c)}(0, 2)) = v_2(Q_j(0, 2, c)) + v_2((3)_{c-1-j}) + v_2((4)_{c-1-j})

at c = 4m + 2, and compare to
    v_2(h_4^{(c)}(0, 2)) = 8m + 1 - 2 s_2(m) - v_2(m).

The C(4, k) prefactor v_2 is (0, 2, 1, 2, 0) for k = 0..4.

We want:  v_2(C(4, k)) + v_2(h_k(0, 2, c)) > v_2(h_4(0, 2, c))
i.e.  strict inequality for k in {0, 1, 2, 3}.
"""
import json
from sympy import symbols, sympify, expand, factor, Poly, simplify, Rational

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
    m = symbols('m')

    Q = load_catalog()

    print("=" * 78)
    print("Q_j(0, 2, c) — symbolic evaluation at anchor (a, b) = (0, 2)")
    print("=" * 78)

    Q_at_02_of_c = {}
    Q_at_02_of_m = {}
    for k in range(7):
        Qk = Q[k]
        Qk02 = expand(Qk.subs({a: 0, b: 2}))
        Qk02_f = factor(Qk02)
        Qk02_m = expand(Qk02.subs({c: 4*m + 2}))
        Qk02_m_f = factor(Qk02_m)
        Q_at_02_of_c[k] = Qk02
        Q_at_02_of_m[k] = Qk02_m
        print(f"\n--- k = {k} ---")
        print(f"  Q_k(0, 2, c) = {Qk02}")
        print(f"           factored = {Qk02_f}")
        print(f"  Q_k(0, 2, 4m+2) = {Qk02_m}")
        print(f"           factored = {Qk02_m_f}")

    # Numeric v_2 of Q_k(0, 2, 4m+2) for m in various ranges
    print("\n" + "=" * 78)
    print("v_2(Q_k(0, 2, 4m+2)) for m = 1..20 (c = 6..82)")
    print("=" * 78)
    header = f"  m | c   | " + " | ".join(f"Q_{k}" for k in range(7))
    print(header)
    print("  " + "-" * (len(header) - 2))
    Q_v2 = {k: [] for k in range(7)}
    for m_val in range(1, 21):
        c_val = 4*m_val + 2
        row_vs = []
        for k in range(7):
            val = int(Q_at_02_of_m[k].subs(m, m_val))
            v = v2(val)
            Q_v2[k].append((m_val, c_val, val, v))
            row_vs.append(v)
        row = f"  {m_val:>2} | {c_val:>3} | " + " | ".join(
            f"{str(v) if v is not None else '0':>4}" for v in row_vs)
        print(row)

    # Save
    out = {
        'note': 'Day 99: Q_k(0, 2, c) at anchor. c = 4m+2.',
        'per_k': {}
    }
    for k in range(7):
        out['per_k'][k] = {
            'Q_k_at_a0_b2': str(Q_at_02_of_c[k]),
            'Q_k_at_a0_b2_sub_c_4m2': str(Q_at_02_of_m[k]),
            'Q_k_at_a0_b2_sub_c_4m2_factored': str(factor(Q_at_02_of_m[k])),
            'v2_by_m': [{'m': mv, 'c': cv, 'val': str(val), 'v2': v}
                        for (mv, cv, val, v) in Q_v2[k]],
        }
    with open('/home/agent/projects/code/2026-07-16-day99-Qj-at-02.json', 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print("\nSaved.")


if __name__ == '__main__':
    main()
