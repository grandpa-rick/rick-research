"""Day 87 - Final verification of Delta beta'(5) = -1.

Confirms:
  (A) v_2(H_5(a,b,j)) >= 3 for all (a,b,j) via term-wise bounds on Clio's h_k.
  (B) H_5(3,0,2) = 88200, v_2 = 3.  Achieves the bound.
  (C) v_2(H_4(a,b,j)) >= 4 for all (a,b,j) with a+b even, via term-wise bounds
      on the extracted h_k^{(4)}.
  (D) H_4(5,5,3) = 179280, v_2 = 4.  Achieves the bound.
"""
from math import factorial


def v2(n):
    if n == 0: return float('inf')
    n = abs(int(n))
    r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r


def C(n, k):
    if k < 0 or k > n: return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


# ---------------------- H_5 (Clio's explicit) ----------------------
def h5_coeffs(a, b):
    return [
        (a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5),          # h_0
        -20*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4),                   # h_1
        -10*(a+3)*(a+4)*(b+2)*(b+3)*(a*b + a + 2*b - 22),          # h_2
        360*(a+3)*(b+2)*(a*b + a + 2*b - 2),                       # h_3
        240*(a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a + 2*b*b - 34*b - 24),  # h_4
        -7200*(a*b + b - 2),                                       # h_5
        -7200*(a*b - a - 6),                                       # h_6
        100800,                                                    # h_7
        201600,                                                    # h_8
    ]


def H5(a, b, j):
    hs = h5_coeffs(a, b)
    return sum(hs[k] * C(j, k) for k in range(9))


# ---------------------- H_4 (extracted h_k^{(4)}) ----------------------
def h4_coeffs(a, b):
    return [
        (a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4),                          # h_0
        -12*(a+3)*(a+4)*(b+2)*(b+3),                                   # h_1
        -8*(a+3)*(b+2)*(a*b + a + 2*b - 7),                            # h_2
        144*(a*b + a + 2*b + 1),                                        # h_3
        144*(a*b + b - 4),                                              # h_4
        -1440,                                                          # h_5
        120*(a*a*b - 2*a*a + a*b*b - 11*a*b + 18*a - b*b + 10*b - 40),  # h_6
    ]


def H4(a, b, j):
    hs = h4_coeffs(a, b)
    return sum(hs[k] * C(j, k) for k in range(7))


def verify_h5_LB():
    """Verify that each h_k^{(5)}(a,b) has v_2 >= B_k with B_k >= 3 for all (a,b).

    Term-wise bounds (from the constants and structural arguments):
        h_0: v_2 >= 6  (v_2(4!) for 4 consec ints, twice)
        h_1: v_2 >= 4  (v_2(20) = 2, plus 3 consec on each side >= 1 each)
        h_2: v_2 >= 3  (v_2(10) = 1, plus 2 consec on each side >= 1 each)
        h_3: v_2 >= 3  (v_2(360) = 3)
        h_4: v_2 >= 4  (v_2(240) = 4)
        h_5: v_2 >= 5  (v_2(7200) = 5)
        h_6: v_2 >= 5  (v_2(7200) = 5)
        h_7: v_2 = 6   (v_2(100800) = 6)
        h_8: v_2 = 7   (v_2(201600) = 7)
    """
    print("=" * 60)
    print("Verify h_k^{(5)}(a,b) LB — all (a,b) unrestricted (no parity)")
    print("=" * 60)
    bounds = {0: 6, 1: 4, 2: 3, 3: 3, 4: 4, 5: 5, 6: 5, 7: 6, 8: 7}
    fails = {k: [] for k in range(9)}
    for a in range(0, 30):
        for b in range(0, 30):
            hs = h5_coeffs(a, b)
            for k in range(9):
                if hs[k] == 0:
                    continue
                v = v2(hs[k])
                if v < bounds[k]:
                    fails[k].append((a, b, hs[k], v))
    for k in range(9):
        n_fails = len(fails[k])
        marker = "PASS" if n_fails == 0 else f"FAIL ({n_fails})"
        print(f"  h_{k}: v_2 >= {bounds[k]}?  {marker}")
        for f in fails[k][:2]:
            print(f"    example: (a,b)=({f[0]},{f[1]}), val={f[2]}, v_2={f[3]}")


def verify_h5_min_at_302():
    print("=" * 60)
    print("Verify H_5(3, 0, 2) = 88200, v_2 = 3")
    print("=" * 60)
    h = H5(3, 0, 2)
    print(f"  H_5(3, 0, 2) = {h}, v_2 = {v2(h)}")
    assert h == 88200
    assert v2(h) == 3


def verify_h4_LB():
    """Verify that each h_k^{(4)}(a,b) has v_2 >= 4 for all (a,b) with a+b even.
    """
    print("=" * 60)
    print("Verify h_k^{(4)}(a,b) LB with a+b even")
    print("=" * 60)
    # Term-wise bounds — all >= 4 to give total v_2(H_4) >= 4
    bounds = {0: 4, 1: 4, 2: 4, 3: 4, 4: 4, 5: 5, 6: 4}
    fails = {k: [] for k in range(7)}
    for a in range(0, 30):
        for b in range(0, 30):
            if (a + b) % 2 != 0:
                continue
            hs = h4_coeffs(a, b)
            for k in range(7):
                if hs[k] == 0:
                    continue
                v = v2(hs[k])
                if v < bounds[k]:
                    fails[k].append((a, b, hs[k], v))
    for k in range(7):
        n_fails = len(fails[k])
        marker = "PASS" if n_fails == 0 else f"FAIL ({n_fails})"
        print(f"  h_{k}: v_2 >= {bounds[k]}?  {marker}")
        for f in fails[k][:2]:
            print(f"    example: (a,b)=({f[0]},{f[1]}), val={f[2]}, v_2={f[3]}")


def verify_h4_min_at_553():
    print("=" * 60)
    print("Verify H_4(5, 5, 3) = 179280, v_2 = 4")
    print("=" * 60)
    h = H4(5, 5, 3)
    print(f"  H_4(5, 5, 3) = {h}, v_2 = {v2(h)}")
    assert h == 179280
    assert v2(h) == 4


def verify_h4_wider_min():
    """Brute-force min v_2(H_4) with a+b even, wide (a,b,j) range."""
    print("=" * 60)
    print("Brute-force min v_2(H_4(a,b,j)) with a+b even")
    print("=" * 60)
    minv = float('inf')
    achievers = []
    for a in range(0, 25):
        for b in range(0, 25):
            if (a + b) % 2 != 0:
                continue
            for j in range(0, 15):
                h = H4(a, b, j)
                if h == 0:
                    continue
                v = v2(h)
                if v < minv:
                    minv = v
                    achievers = [(a, b, j, h)]
                elif v == minv:
                    achievers.append((a, b, j, h))
    print(f"  min v_2(H_4) = {minv}")
    print(f"  # achievers: {len(achievers)}")
    for a, b, j, h in achievers[:6]:
        print(f"    (a,b,j)=({a},{b},{j}): H_4 = {h}, v_2 = {v2(h)}")


def verify_h5_wider_min():
    print("=" * 60)
    print("Brute-force min v_2(H_5(a,b,j))")
    print("=" * 60)
    minv = float('inf')
    achievers = []
    for a in range(0, 25):
        for b in range(0, 25):
            for j in range(0, 15):
                h = H5(a, b, j)
                if h == 0:
                    continue
                v = v2(h)
                if v < minv:
                    minv = v
                    achievers = [(a, b, j, h)]
                elif v == minv:
                    achievers.append((a, b, j, h))
    print(f"  min v_2(H_5) = {minv}")
    print(f"  # achievers: {len(achievers)}")
    for a, b, j, h in achievers[:6]:
        print(f"    (a,b,j)=({a},{b},{j}): H_5 = {h}, v_2 = {v2(h)}")


def mod2_check_h4():
    """Verify by modular arithmetic that certain factors are even under a+b even."""
    print("=" * 60)
    print("Mod-2 checks on polynomial factors")
    print("=" * 60)
    # h_6 factor P(a,b) = a²b - 2a² + ab² - 11ab + 18a - b² + 10b - 40
    # Mod 2: a²b + ab² + ab + b² = ab(a+b) + b(a+b) = (a+b)(ab+b) = (a+b)·b·(a+1)
    # If a+b even, this is 0.
    all_ok = True
    for a in range(0, 20):
        for b in range(0, 20):
            if (a + b) % 2 != 0:
                continue
            P = a*a*b - 2*a*a + a*b*b - 11*a*b + 18*a - b*b + 10*b - 40
            if P % 2 != 0:
                print(f"  MOD-2 FAIL: P(a={a},b={b}) = {P}")
                all_ok = False
    if all_ok:
        print("  P(a,b) is even for all a+b even in [0,20]. Confirmed.")


if __name__ == "__main__":
    verify_h5_LB()
    verify_h5_wider_min()
    verify_h5_min_at_302()
    print()
    verify_h4_LB()
    verify_h4_wider_min()
    verify_h4_min_at_553()
    mod2_check_h4()
