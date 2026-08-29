"""Day 101 — analysis of the k=4 case for G3.

We proved: S_4(A, B, 4m+2) = 12·A·(A-1)·B·(B-1) - 32·m²·(4m-1)·[6·A·B + (2m-1)(4m-1)(4m+1)]
                          with A = a+2, B = b+1.

Let f_1 = 12·(a+1)(a+2)·b·(b+1) and f_2 = 32·m²·(4m-1)·[6(a+2)(b+1) + (2m-1)(4m-1)(4m+1)].
Then S_4 = f_1 - f_2, v_2(f_2) = 5 + 2e (exactly), v_2(f_1) ≥ 4 on shell.

Target inequality: carries_a + carries_b + v_2(S_4) ≥ 6 + e.

We split:
- Case B: v_2(f_1) >= 5 + 2e. Then v_2(S_4) >= 5 + 2e; need carries >= 1 - e. Trivial for e>=1;
  for e=0 need carries >= 1, which holds from shell parity (bit 0 chain).
- Case A: v_2(f_1) < 5 + 2e. Then v_2(S_4) = v_2(f_1). Need carries + v_2(f_1) >= 6 + e.

This script:
1. Verifies the S_4 factorisation numerically.
2. Verifies the target inequality holds over a large grid.
3. Prints exact tightness — where R = carries + v_2(S_4) - (6+e) = 0.
4. Tests the split (Case A vs Case B).
5. Explores whether carries + T1 >= 4 + e holds in Case A of Case E and Case O.
"""

def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v

def s2(n):
    return bin(n).count('1') if n > 0 else 0

def carries(x, y):
    return s2(x) + s2(y) - s2(x + y)


def v2_S4_direct(a, b, c):
    """Compute S_4 directly."""
    A = a + 2
    B = b + 1
    term1 = 12 * (a+1) * (a+2) * b * (b+1)
    m = (c - 2) // 4
    term2 = 32 * m**2 * (4*m - 1) * (6 * (a+2) * (b+1) + (2*m - 1) * (4*m - 1) * (4*m + 1))
    return term1 - term2


def v2_h4_direct(a, b, c):
    """Compute v_2 of h_4^{(c)}(a, b) via Q_4 and Pochhammers."""
    L = c - 1 - 4
    if L < 0: return None
    # v_2 of pochhammer (a+3)_L using AMM = v_2(L!) + carries(a+2, L)
    v2_Lfact = L - s2(L)
    v2_pocha = v2_Lfact + carries(a + 2, L)
    v2_pochb = v2_Lfact + carries(b + 1, L)
    # v_2 of Q_4 = v_2(c(c-1)) + v_2(S_4)
    v2_cc = v2(c) + v2(c - 1)
    S = v2_S4_direct(a, b, c)
    if S == 0:
        return None
    v2_Q = v2_cc + v2(S)
    return v2_pocha + v2_pochb + v2_Q


def target_v2_h4(c):
    """Target: β(c) − D_anchor(c) = 8m + 1 − 2·s_2(m) − v_2(m), m = (c-2)/4."""
    m = (c - 2) // 4
    return 8 * m + 1 - 2 * s2(m) - v2(m)


print("=" * 78)
print("Day 101 — k=4 G3 verification")
print("=" * 78)

# Verify inequality over large grid
fails = 0
oks = 0
tight_count = 0
case_A_count = 0
case_B_count = 0
worst_slack = 10**9
worst_config = None

for m in range(1, 30):
    c = 4 * m + 2
    target = target_v2_h4(c)
    e = v2(m)
    for a in range(0, 32):
        for b in range(0, 32):
            if (a + b) % 2 != 0:
                continue
            v = v2_h4_direct(a, b, c)
            if v is None:
                continue
            slack = v - target
            if slack < 0:
                fails += 1
                if fails <= 5:
                    print(f"  FAIL: m={m}, a={a}, b={b}: v={v}, target={target}, slack={slack}")
                continue
            oks += 1
            if slack == 0:
                tight_count += 1
            if slack < worst_slack:
                worst_slack = slack
                worst_config = (m, a, b, v, target)
            # Determine case
            f1 = 12 * (a+1) * (a+2) * b * (b+1)
            v_f1 = v2(f1) if f1 != 0 else 10**9
            if v_f1 >= 5 + 2*e:
                case_B_count += 1
            else:
                case_A_count += 1

print(f"  Grid: m in [1, 29], (a, b) in [0, 32)^2 shell (a+b even)")
print(f"  Total: {oks} pass, {fails} fail; {tight_count} tight (slack=0)")
print(f"  Case A (v_2(f_1) < 5+2e): {case_A_count} samples")
print(f"  Case B (v_2(f_1) >= 5+2e): {case_B_count} samples")
print(f"  Worst slack: {worst_slack} at (m, a, b, v, target) = {worst_config}")

# Now focus on Case A: verify carries + T1 >= 4 + e (Case E) or same (Case O)
print()
print("=" * 78)
print("Case A analysis: carries_a + carries_b + T_1 >= 4 + e?")
print("=" * 78)

case_A_slacks = []
for m in range(1, 30):
    c = 4 * m + 2
    L = 4 * m - 3
    e = v2(m)
    for a in range(0, 32):
        for b in range(0, 32):
            if (a + b) % 2 != 0:
                continue
            f1 = 12 * (a+1) * (a+2) * b * (b+1)
            v_f1 = v2(f1) if f1 != 0 else 10**9
            if v_f1 >= 5 + 2*e:  # skip Case B
                continue
            # Case A: T_1 = v_f1 - 2
            T1 = v_f1 - 2
            ca = carries(a + 2, L)
            cb = carries(b + 1, L)
            req = 4 + e - T1
            slack = ca + cb - req
            case_A_slacks.append((m, a, b, e, T1, ca, cb, req, slack))

case_A_slacks.sort(key=lambda x: x[-1])
worst = case_A_slacks[:8]
print("  Worst 8 Case A slacks (ca + cb + T_1 - (4 + e)):")
for row in worst:
    print(f"    m={row[0]:3d}, a={row[1]:3d}, b={row[2]:3d}, e={row[3]}, T_1={row[4]}, "
          f"ca={row[5]}, cb={row[6]}, req={row[7]}, slack={row[8]}")

# Print stats
slacks = [row[-1] for row in case_A_slacks]
print(f"  Case A: {len(slacks)} samples; min slack = {min(slacks)}, max = {max(slacks)}")
