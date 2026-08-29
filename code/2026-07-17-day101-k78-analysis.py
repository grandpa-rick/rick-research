"""Day 101 BONUS — check whether k=7, k=8 close via the same trivial route as k=5, k=6.

For k=8:
  v_2(Q_8) = v_2(c(c-3)(c-2)(c-1)) + v_2(S_8) = 3 + e + v_2(S_8).
  S_8 = 16 * P_hat_8, so v_2(S_8) >= 4.
  Reduced target: X_8(m) = β - D_anchor - 2 v_2(L!) with L = 4m-7 = 4(m-2)+1.

For k=7:
  v_2(Q_7) = v_2(c(c-4)(c-3)(c-2)(c-1)) = 4 + e + v_2(S_7).
  S_7 = -8 * P_hat_7, so v_2(S_7) >= 3.
  L = 4m-6.
"""
def v2(n):
    if n == 0: return 10**9
    v = 0
    while n % 2 == 0:
        n //= 2; v += 1
    return v
def s2(n): return bin(n).count('1') if n > 0 else 0
def car(x, y): return s2(x)+s2(y)-s2(x+y)

# Compute X_k(m) for k=7, k=8 to see the target structure
print("X_k(m) tables for k=7, 8 (target for v_2(Q_k) + carries):")
print("m   c    L7   L8   X7    X8")
for m in range(2, 20):
    c = 4*m + 2
    beta_minus_D = 8*m + 1 - 2*s2(m) - v2(m)
    L7 = c - 1 - 7  # = 4m - 6
    L8 = c - 1 - 8  # = 4m - 7
    v2Lf7 = L7 - s2(L7)
    v2Lf8 = L8 - s2(L8)
    X7 = beta_minus_D - 2*v2Lf7
    X8 = beta_minus_D - 2*v2Lf8
    print(f"{m:2d}  {c:3d}  {L7:3d}  {L8:3d}  {X7:3d}   {X8:3d}")

# For k=8: c-prefactor gives 3 + e, plus v_2(S_8) >= 4. So carries + 7 + e >= X_8.
# Compute (X_8 - 7 - e) required carries.
print()
print("Required carries for k=8: X_8 - 7 - e:")
print("m   c   e   X8   need_carries")
for m in range(2, 20):
    c = 4*m + 2
    e = v2(m)
    L8 = c - 1 - 8
    beta_minus_D = 8*m + 1 - 2*s2(m) - v2(m)
    X8 = beta_minus_D - 2*(L8 - s2(L8))
    need = X8 - 7 - e
    print(f"{m:2d}  {c:3d}  {e}   {X8:3d}   {need}")

# Similarly for k=7: 4 + e + v_2(S_7) >= X_7 - carries. With v_2(S_7) >= 3:
# carries + 7 + e >= X_7.
print()
print("Required carries for k=7: X_7 - 7 - e:")
print("m   c   e   X7   need_carries")
for m in range(2, 20):
    c = 4*m + 2
    e = v2(m)
    L7 = c - 1 - 7
    beta_minus_D = 8*m + 1 - 2*s2(m) - v2(m)
    X7 = beta_minus_D - 2*(L7 - s2(L7))
    need = X7 - 7 - e
    print(f"{m:2d}  {c:3d}  {e}   {X7:3d}   {need}")
