"""Day 98 PROVE — Closed form for v_2(h_k(0, (c-2)/4, c)) for k = 4, 5, 6.

Combines:
  (i) Q_k(0, (c-2)/4, c) factored form from catalog.
  (ii) AMM Pochhammer valuations at (a+3)_L = (3)_L and (b+2)_L = ((c+6)/4)_L.
  (iii) Simplification for c ≡ 2 mod 8 (m = (c-2)/4 even, i.e., m = 2n).

Derives symbolic formulas for D_★_k(c) := β(c) - v_2(h_k^{(c)}(0, (c-2)/4)).
Verifies against numerical data.

SEALED: no reference to D_pred = 1 + s_2(m-1) formula in derivation.
"""
import json
from sympy import symbols, sympify, expand, factor, S


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


def load_catalog_Q():
    with open("/home/agent/projects/code/2026-07-11-Qk-catalog.json") as f:
        cat = json.load(f)
    a, b, c = symbols('a b c')
    Q = {}
    for k in range(6):
        Q[k] = sympify(cat['Q_k_low_k'][str(k)])
    Q[6] = sympify(cat['Q_k_extended']['6']['poly_expanded'])
    return Q


def D_star_k_predicted(k, m):
    """Closed-form prediction for D_★_k(c) at c = 4m+2 (m even),
    derived symbolically. Below are the closed forms for k = 4, 5, 6.
    """
    if k == 4:
        # D_★_k4 = 3 + s_2(5m-2) - s_2(m+1)
        return 3 + s2(5*m - 2) - s2(m + 1)
    elif k == 5:
        # D_★_k5 = 2 - v_2(m) + s_2(5m-3) - s_2(m+1)
        return 2 - v2(m) + s2(5*m - 3) - s2(m + 1)
    elif k == 6:
        # D_★_k6 = 4 - s_2(4m+1) - 2·v_2(m) + s_2(4m-3) + s_2(5m-4) - s_2(m+1)
        # We can simplify s_2(4m+1) = s_2(m) + 1, s_2(4m-3) = s_2(4(m-1)+1) = s_2(m-1) + 1
        # so = 4 - s_2(m) - 1 - 2v_2(m) + s_2(m-1) + 1 + s_2(5m-4) - s_2(m+1)
        # Rick's honest form:
        return (4 - s2(4*m + 1) - 2*v2(m) + s2(4*m - 3) + s2(5*m - 4) - s2(m + 1))
    else:
        return None


def main():
    a, b, c = symbols('a b c')
    Q = load_catalog_Q()

    print("=" * 90)
    print("Closed forms for D_★_k(c) at anchor (0, (c-2)/4), c = 4m+2, m even")
    print("=" * 90)
    print()
    print("k=4: D_★_k4 = 3 + s_2(5m-2) - s_2(m+1)")
    print("k=5: D_★_k5 = 2 - v_2(m) + s_2(5m-3) - s_2(m+1)")
    print("k=6: D_★_k6 = 4 - s_2(4m+1) - 2·v_2(m) + s_2(4m-3) + s_2(5m-4) - s_2(m+1)")
    print()

    # Numerical verification: derive D_★_k(c) via
    #     β(c) - [v_2((3)_{c-1-k}) + v_2(((c+6)/4)_{c-1-k}) + v_2(Q_k(0, (c-2)/4, c))]
    # and compare to formula.
    print("=" * 90)
    print("Verification: numeric D_★_k(c) vs formula, c ≡ 2 mod 8")
    print("=" * 90)
    print(f"{'m':>3} {'c':>4}"
          + " || " + " ".join(f"D_★_k{k}(num)/formula" for k in [4, 5, 6]))
    print("-" * 90)

    mismatches = []
    for m in range(2, 33, 2):
        c_val = 4 * m + 2
        kappa = m
        beta_c = beta(c_val)
        row = f"{m:>3} {c_val:>4}"
        for k in [4, 5, 6]:
            L = c_val - 1 - k
            p1 = rising(3, L)
            p2 = rising(kappa + 2, L)
            Qk = int(Q[k].subs({a: 0, b: kappa, c: c_val}))
            h = p1 * p2 * Qk
            v = v2(h)
            D_num = beta_c - v
            D_form = D_star_k_predicted(k, m)
            match = "✓" if D_num == D_form else "✗"
            row += f" || {D_num:>3}/{D_form:>3} {match}"
            if D_num != D_form:
                mismatches.append((m, c_val, k, D_num, D_form))
        print(row)

    if mismatches:
        print(f"\nMISMATCHES: {mismatches}")
    else:
        print(f"\nAll D_★_k formulas verified for m ∈ [2, 32], k ∈ [4, 6].")

    # Now the KEY question: SEALED comparison against D_pred = 1 + s_2(m-1).
    # (D_pred is the digit-sum formula for c ≡ 2 mod 8.)
    print("\n" + "=" * 90)
    print("SEALED: max over k∈{4,5,6} of D_★_k vs D_pred = 1 + s_2(m-1)")
    print("=" * 90)
    print(f"{'m':>3} {'c':>4} {'D_★_k4':>7} {'D_★_k5':>7} {'D_★_k6':>7}"
          + f" {'max':>4} {'D_pred':>7} {'match':>6}")
    print("-" * 60)
    matches = 0
    total = 0
    fail_c = []
    for m in range(2, 33, 2):
        c_val = 4 * m + 2
        Ds = [D_star_k_predicted(k, m) for k in [4, 5, 6]]
        Dmax = max(Ds)
        Dpred = 1 + s2(m - 1)
        match = "✓" if Dmax == Dpred else "✗"
        print(f"{m:>3} {c_val:>4} {Ds[0]:>7} {Ds[1]:>7} {Ds[2]:>7} {Dmax:>4} {Dpred:>7} {match:>6}")
        if Dmax == Dpred:
            matches += 1
        else:
            fail_c.append((m, c_val, Dmax, Dpred))
        total += 1
    print(f"\nMatches: {matches}/{total}")
    if fail_c:
        print(f"Failures (need higher k): {fail_c}")


if __name__ == '__main__':
    main()
