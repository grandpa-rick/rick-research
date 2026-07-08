"""Verify the derived closed form for D(c) = beta(c) - beta'(c) at c=4..10.

Formula (conjectural — assumes D1 for odd c, (E) beta'(4k)=beta(4k) for k>=1,
and D2 beta'(4k+2)=beta(4k+2)-1-v_2(k)):

  D(4k)   = 0
  D(4k+1) = 4 + 2 v_2(k)   for k >= 1
  D(4k+2) = 1 + v_2(k)     for k >= 1
  D(4k+3) = 4 + v_2(k)     for k >= 1

Equivalently:
  beta'(c) = beta(c) - D(c),  beta(c) = 2(c-1) - s_2(c-1).
"""


def s2(n):
    return bin(n).count("1")


def v2(n):
    if n == 0:
        return float("inf")
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def beta(c):
    return 2 * (c - 1) - s2(c - 1)


def D_closed(c):
    if c < 4:
        return None
    q, r = divmod(c, 4)
    if r == 0:
        return 0
    if q < 1:
        return None
    if r == 1:
        return 4 + 2 * v2(q)
    if r == 2:
        return 1 + v2(q)
    if r == 3:
        return 4 + v2(q)


def beta_prime_closed(c):
    D = D_closed(c)
    if D is None:
        return None
    return beta(c) - D


# Clio's empirical data
CLIO = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14}


print("c  | beta(c) | beta'(c) empirical | beta'(c) closed form | D(c) | match")
print("-" * 78)
for c in range(4, 18):
    bp_pred = beta_prime_closed(c)
    bp_emp = CLIO.get(c, None)
    D = D_closed(c)
    match = "yes" if bp_emp is None or bp_pred == bp_emp else "NO"
    print(
        f"{c:2d} | {beta(c):7d} | {str(bp_emp):18s} | {bp_pred:20d} | {D:4d} | {match}"
    )


# Sanity: Delta beta(c) = 1 + v_2(c-1)
print("\nSanity: Delta beta(c) - (1 + v_2(c-1)) for c=2..17:")
for c in range(2, 18):
    lhs = beta(c) - beta(c - 1)
    rhs = 1 + v2(c - 1)
    ok = "OK" if lhs == rhs else "FAIL"
    print(f"  c={c:2d}: Delta beta = {lhs}, 1 + v_2({c-1}) = {rhs}  {ok}")


# 4-period identity check
print("\n4-period identity: beta'(4(k+1)) - beta'(4k) = 7 + v_2(k)")
for k in range(1, 5):
    lhs = beta_prime_closed(4 * (k + 1)) - beta_prime_closed(4 * k)
    rhs = 7 + v2(k)
    print(f"  k={k}: LHS={lhs}, 7 + v_2({k})={rhs}  {'OK' if lhs == rhs else 'FAIL'}")


# Sum constraint check
print("\nSum constraint: Delta beta'(4k+2) + Delta beta'(4k+4) = 9 + 2 v_2(k)")
for k in range(1, 5):
    d2 = beta_prime_closed(4 * k + 2) - beta_prime_closed(4 * k + 1)
    d4 = beta_prime_closed(4 * k + 4) - beta_prime_closed(4 * k + 3)
    lhs = d2 + d4
    rhs = 9 + 2 * v2(k)
    print(f"  k={k}: Delta beta'({4*k+2}) + Delta beta'({4*k+4}) = {d2}+{d4}={lhs}, 9+2v_2({k})={rhs}  {'OK' if lhs == rhs else 'FAIL'}")


# D1 check
print("\nD1: Delta beta'(c) = 1 - max(2, v_2(c-1)) for odd c >= 5")
for c in range(5, 18, 2):
    lhs = beta_prime_closed(c) - beta_prime_closed(c - 1)
    rhs = 1 - max(2, v2(c - 1))
    print(f"  c={c:2d}: Delta beta' = {lhs}, 1 - max(2, v_2({c-1})) = {rhs}  {'OK' if lhs == rhs else 'FAIL'}")
