"""Day 169 Step 16 — Compute L_{-1} as closed form: L = -SOURCE / L_op.

SOURCE = collection of all non-L contributions to δ=2 equation.

L_op multiplier = 3 R_3 H^2 + 2 R_2 H + R_1 = 2 R_3 H^2 + R_2 H = H(2 R_3 H + R_2)
using top-diagonal identity R_3 H^2 + R_2 H + R_1 = 0.

Alternatively L_op = derivative of top-diagonal quadratic in H with respect to H.
"""

import sympy as sp

T, E1, E2 = sp.symbols('T E1 E2')
s, p = E1, E2

# Setup H, K, R_3, R_2, R_1

Y = sp.symbols('Y')
H = E2 * Y / T  # H = p Y / T

R3 = -T**2 + 2*s*T**3 + (4*p - s**2) * T**4
R2 = 1 - 3*s*T + (3*s**2 - 4*p) * T**2 + (4*p*s - s**3) * T**3
R1 = -p + 2*p*s*T + (4*p**2 - p*s**2) * T**2

# L-op multiplier:
L_mult = 3*R3*H**2 + 2*R2*H + R1

# Verify equals 2 R_3 H^2 + R_2 H using top-eq R_3 H^2 + R_2 H + R_1 = 0
diff = sp.expand(L_mult - (2*R3*H**2 + R2*H))
# Reduce mod Y^2 = ...
Y2_sub = (Y - T - T*E1*Y)/(T*E2)
def reduce_Y(expr, max_iter=30):
    e = sp.expand(expr)
    for _ in range(max_iter):
        pp = sp.Poly(e, Y) if Y in e.free_symbols else None
        if pp is None or pp.degree() < 2:
            break
        e = sp.expand(e.subs(Y**2, Y2_sub))
    return e

diff_reduced = reduce_Y(sp.expand(diff * T**2))  # multiply by T^2 to clear denominator
print(f"L_mult - (2 R_3 H^2 + R_2 H) reduced: {diff_reduced}")

# Now SOURCE = all non-L contributions to δ=2 equation. Collect from earlier enumeration.
# The equation: L_mult * L + SOURCE = 0 => L = -SOURCE / L_mult.

# SOURCE contributions (non-L):
# From P_3 G'' (H'' terms only):
#   T^2 * (-1) * H'' + T^3 * (2s) * H'' + T^4 * (4p - s^2) * H''
#   = R_3(T) * H''
# From P_3 (3 GG') e=0 (H H'):
#   T^3 * 6 * 3 * H H' = 18 T^3 H H'
# From P_3 (3 GG') e=1 (H K' + K H'):
#   T^2 * (-1) * 3 * (H K' + K H') + T^3 * (2s) * 3 * (...) + T^4 * (4p - s^2) * 3 * (...)
#   = 3 R_3(T) (H K' + K H')
# From P_3 G^3 e=1 (3 H^2 K):
#   T^3 * 6 * 3 H^2 K = 18 T^3 H^2 K
# From P_3 G^3 e=0 (H^3):
#   T^4 * 1 * H^3 = T^4 H^3
# From P_3 G^3 e=2 non-L (3 H K^2):
#   T^2 * (-1) * 3 H K^2 + T^3 * (2s) * 3 H K^2 + T^4 * (4p - s^2) * 3 H K^2
#   = 3 R_3(T) H K^2
# From P_2 G' e=0 (H'):
#   T^1 * (-11) * H' + T^2 * (14s) * H' + T^3 * (-3s^2 + 12p) * H'
# From P_2 G' e=1 (K'):
#   T^0 * 1 * K' + T^1 * (-3s) * K' + T^2 * (3s^2 - 4p) * K' + T^3 * (-s^3 + 4ps) * K'
#   = R_2(T) * K'
# From P_2 G^2 e=0 (H^2):
#   T^2 * 23 * H^2 + T^3 * s * H^2
# From P_2 G^2 e=1 (2 H K):
#   T^1 * (-11) * 2 H K + T^2 * (14s) * 2 H K + T^3 * (-3s^2 + 12p) * 2 H K
# From P_2 G^2 e=2 non-L (K^2):
#   T^0 * 1 * K^2 + T^1 * (-3s) * K^2 + T^2 * (3s^2 - 4p) * K^2 + T^3 * (-s^3 + 4ps) * K^2
#   = R_2(T) * K^2
# From P_1 G e=0 (H):
#   T^0 * 1 * H + T^1 * (12s) * H + T^2 * (-s^2 + 5p) * H
# From P_1 G e=1 (K):
#   T^0 * (-s) * K + T^1 * (2s^2 + 10p) * K + T^2 * (-s^3 + 4ps) * K

# Let me code this up:

# Assume H, K are known series. Define generating polynomials for the source.

# Multi-form: express SOURCE in terms of Y, q, and derivatives.
# H = E_2 Y / T, so H' = E_2 (Y'/T - Y/T^2) = E_2 (Y' T - Y)/T^2
# H'' can be computed similarly.
# K = K_0 + q'/q where K_0 = [E_2 Y(2q+1) + E_1 q]/q^2, easier as series.
# K' similarly.

# I'll do this symbolically in T. Use series expansions (numerical).

# Define series:
def Y_series(N):
    Ys = [sp.S(0)]*(N+1)
    for n in range(1, N+1):
        acc = sp.S(0)
        if n-1 == 0: acc += 1
        acc += s * Ys[n-1]
        for k in range(n):
            acc += p * Ys[k] * Ys[n-1-k]
        Ys[n] = sp.expand(acc)
    return Ys

def q_series(N):
    q2 = [sp.S(0)]*(N+1)
    q2[0] = 1; q2[1] = -2*s; q2[2] = s**2 - 4*p
    q = [sp.S(0)]*(N+1); q[0] = 1
    for n in range(1, N+1):
        s0 = q2[n] if n <= 2 else sp.S(0)
        for k in range(1, n):
            s0 -= q[k]*q[n-k]
        q[n] = s0/2
    return q

def series_mul(f, g, N):
    return [sum(f[k]*g[n-k] for k in range(n+1)) for n in range(N+1)]
def series_inv(f, N):
    inv = [sp.S(0)]*(N+1); inv[0] = 1/f[0]
    for n in range(1, N+1):
        s0 = sp.S(0)
        for k in range(1, n+1):
            s0 -= f[k]*inv[n-k]
        inv[n] = s0/f[0]
    return inv
def series_deriv(f, N):
    return [(k+1)*f[k+1] if k+1 <= N and k+1 < len(f) else sp.S(0) for k in range(N+1)]
def series_shift(f, k):
    """Return T^k * f, i.e., [T^m] = f[m-k] for m >= k else 0."""
    return [sp.S(0)]*k + list(f)
def series_scal(f, c):
    return [c*x for x in f]
def series_add(*fs):
    N0 = max(len(f) for f in fs)
    return [sum((f[k] if k < len(f) else sp.S(0)) for f in fs) for k in range(N0)]

N = 15
Ys = Y_series(N)
qs = q_series(N)
q_p_ser = series_deriv(qs, N-1)
q2s = series_mul(qs, qs, N-1)
q2_inv_s = series_inv(q2s, N-1)
q_inv_s = series_inv(qs, N-1)

# H series: [T^m] H = E_2 Y_{m+1}
H_ser = [p * Ys[m+1] for m in range(N)]

# H' series: [T^m] H' = (m+1) H[m+1]
H_p_ser = series_deriv(H_ser, N-2)

# H'' series
H_pp_ser = series_deriv(H_p_ser, N-3)

# K series
two_q_plus_1 = [2*qs[n] + (1 if n==0 else 0) for n in range(N)]
E2Y = [p * Ys[n] for n in range(N)]
num_K0 = series_mul(E2Y, two_q_plus_1, N-1)
E1q = [s*qs[n] for n in range(N)]
num_K0 = [num_K0[n] + E1q[n] for n in range(N-1)]
K0_ser = series_mul(num_K0, q2_inv_s, N-2)
q_over_q_ser = series_mul(q_p_ser, q_inv_s, N-2)
K_ser = [K0_ser[m] + q_over_q_ser[m] for m in range(N-2)]

# K'
K_p_ser = series_deriv(K_ser, N-3)

# HK, HH', H^2, H^3, H^2 K, H K^2, K^2, KK'
N0 = 10
def cap(f, N):
    return f[:N+1] if len(f) > N+1 else f + [sp.S(0)]*(N+1-len(f))

Ht = cap(H_ser, N0)
Hpt = cap(H_p_ser, N0)
Hppt = cap(H_pp_ser, N0)
Kt = cap(K_ser, N0)
Kpt = cap(K_p_ser, N0)

HK = series_mul(Ht, Kt, N0)
HH_p = series_mul(Ht, Hpt, N0)
H2 = series_mul(Ht, Ht, N0)
H3 = series_mul(H2, Ht, N0)
H2K = series_mul(H2, Kt, N0)
K2 = series_mul(Kt, Kt, N0)
HK2 = series_mul(Ht, K2, N0)
HKp = series_mul(Ht, Kpt, N0)
KHp = series_mul(Kt, Hpt, N0)
HKp_KHp = [HKp[m] + KHp[m] for m in range(N0+1)]  # H K' + K H'
KKp = series_mul(Kt, Kpt, N0)

# R_3(T) as a series
R3_coefs = [sp.S(0), sp.S(0), -1, 2*s, 4*p - s**2] + [sp.S(0)]*(N0-3)
R2_coefs = [1, -3*s, 3*s**2 - 4*p, 4*p*s - s**3] + [sp.S(0)]*(N0-2)
R1_coefs = [-p, 2*p*s, 4*p**2 - p*s**2] + [sp.S(0)]*(N0-1)

R3s = cap(R3_coefs, N0)
R2s = cap(R2_coefs, N0)

# Compute R_3 H'' (series)
R3_Hpp = series_mul(R3s, Hppt, N0)

# 18 T^3 H H' (contribution from P_3 * 3 * GG' e=0)
T3_HHp = series_shift(HH_p, 3)
T3_HHp = cap(T3_HHp, N0)
c_T3_HHp = series_scal(T3_HHp, 18)

# 3 R_3(T) (H K' + K H')
Rat3_HK_stuff = series_mul(R3s, HKp_KHp, N0)
c_3R3 = series_scal(Rat3_HK_stuff, 3)

# 18 T^3 H^2 K (P_3 G^3 e=1)
T3_H2K = series_shift(H2K, 3)
T3_H2K = cap(T3_H2K, N0)
c_18T3_H2K = series_scal(T3_H2K, 18)

# T^4 H^3 (P_3 G^3 e=0)
T4_H3 = series_shift(H3, 4)
T4_H3 = cap(T4_H3, N0)

# 3 R_3(T) H K^2 (P_3 G^3 e=2 non-L)
c_3R3_HK2 = series_scal(series_mul(R3s, HK2, N0), 3)

# P_2 G' e=0 (H'): T (-11) H' + T^2 14s H' + T^3 (-3s^2 + 12p) H'
P2_Gp_e0 = series_add(
    series_scal(series_shift(Hpt, 1), -11),
    series_scal(series_shift(Hpt, 2), 14*s),
    series_scal(series_shift(Hpt, 3), -3*s**2 + 12*p),
)
P2_Gp_e0 = cap(P2_Gp_e0, N0)

# R_2 K' (P_2 G' e=1)
R2_Kp = series_mul(R2s, Kpt, N0)

# P_2 G^2 e=0: T^2 * 23 * H^2 + T^3 * s * H^2 = (23 T^2 + s T^3) H^2
P2_G2_e0 = series_add(
    series_scal(series_shift(H2, 2), 23),
    series_scal(series_shift(H2, 3), s),
)
P2_G2_e0 = cap(P2_G2_e0, N0)

# P_2 G^2 e=1 (2 H K): -11 T * 2 H K + 14 s T^2 * 2 H K + (-3s^2 + 12p) T^3 * 2 H K
c_2HK = series_scal(HK, 2)
P2_G2_e1 = series_add(
    series_scal(series_shift(c_2HK, 1), -11),
    series_scal(series_shift(c_2HK, 2), 14*s),
    series_scal(series_shift(c_2HK, 3), -3*s**2 + 12*p),
)
P2_G2_e1 = cap(P2_G2_e1, N0)

# R_2 K^2 (P_2 G^2 e=2 non-L)
R2_K2 = series_mul(R2s, K2, N0)

# P_1 G e=0 (H): T^0 * 1 * H + T^1 * 12s * H + T^2 * (-s^2 + 5p) * H
P1_G_e0 = series_add(
    Ht,
    series_scal(series_shift(Ht, 1), 12*s),
    series_scal(series_shift(Ht, 2), -s**2 + 5*p),
)
P1_G_e0 = cap(P1_G_e0, N0)

# P_1 G e=1 (K): T^0 * (-s) * K + T^1 * (2s^2 + 10p) * K + T^2 * (-s^3 + 4ps) * K
P1_G_e1 = series_add(
    series_scal(Kt, -s),
    series_scal(series_shift(Kt, 1), 2*s**2 + 10*p),
    series_scal(series_shift(Kt, 2), -s**3 + 4*p*s),
)
P1_G_e1 = cap(P1_G_e1, N0)

# Total SOURCE (all non-L contributions):
SOURCE = series_add(
    R3_Hpp,           # P_3 G'' e=0
    c_T3_HHp,         # P_3 * 3 GG' e=0
    c_3R3,            # P_3 * 3 GG' e=1
    c_18T3_H2K,       # P_3 G^3 e=1
    T4_H3,            # P_3 G^3 e=0
    c_3R3_HK2,        # P_3 G^3 e=2 non-L
    P2_Gp_e0,         # P_2 G' e=0
    R2_Kp,            # P_2 G' e=1
    P2_G2_e0,         # P_2 G^2 e=0
    P2_G2_e1,         # P_2 G^2 e=1
    R2_K2,            # P_2 G^2 e=2 non-L
    P1_G_e0,          # P_1 G e=0
    P1_G_e1,          # P_1 G e=1
)
SOURCE = cap(SOURCE, N0)

# L-op = 3 R_3 H^2 + 2 R_2 H + R_1 (in series form)
# = 2 R_3 H^2 + R_2 H (using top-diagonal identity)
R1s = cap(R1_coefs, N0)
L_op_ser = series_add(
    series_scal(series_mul(R3s, H2, N0), 3),
    series_scal(series_mul(R2s, Ht, N0), 2),
    R1s,
)
L_op_ser = cap(L_op_ser, N0)
print("L-op series first coeffs:")
for m in range(min(N0+1, 6)):
    print(f"  [T^{m}] L_op = {sp.expand(L_op_ser[m])}")

# Alternative: 2 R_3 H^2 + R_2 H
L_op_alt = series_add(
    series_scal(series_mul(R3s, H2, N0), 2),
    series_mul(R2s, Ht, N0),
)
L_op_alt = cap(L_op_alt, N0)
print("\nAlternative L-op = 2 R_3 H^2 + R_2 H first coeffs:")
for m in range(min(N0+1, 6)):
    print(f"  [T^{m}] alt = {sp.expand(L_op_alt[m])}")

# Verify equality
print("\nDifference of two L-op expressions:")
for m in range(N0+1):
    d = sp.expand(L_op_ser[m] - L_op_alt[m])
    print(f"  [T^{m}] diff = {d}")

# Print SOURCE for reference
print("\nSOURCE first coeffs:")
for m in range(min(N0+1, 6)):
    print(f"  [T^{m}] SOURCE = {sp.expand(SOURCE[m])}")

# L = -SOURCE / L_op. Compute -SOURCE / L_op as series.
# But L_op has [T^0] = -p (from R_1 constant term), so L_op is invertible if we treat as series.
# Actually L_op[0] = -p ≠ 0.
# Wait: L_op[0] = 3 * R_3[0] * H^2[0] + 2 * R_2[0] * H[0] + R_1[0]
# R_3[0] = 0, R_2[0] = 1, R_1[0] = -p, H[0] = p (since Y_1 = 1, so H[0] = p*1 = p). Hmm wait H[0] = p*Y_1 = p.
# So L_op[0] = 0 + 2 * 1 * p + (-p) = p ≠ 0.
# Hmm let me re-compute. R_2[0] = 1. Then 2 R_2 H at T^0 = 2 * 1 * p = 2p. R_1[0] = -p. Sum = p.
# So L_op[0] = p. Invertible in Q(p)((T)).

# Compute L = -SOURCE / L_op
L_op_inv = series_inv([sp.expand(x) for x in L_op_ser], N0)
neg_SOURCE = series_scal(SOURCE, -1)
L_from_formula = series_mul(neg_SOURCE, L_op_inv, N0)

# Compare with actual L_{-1}[m] from step 11
L_actual = [
    sp.S(0), sp.S(0),
    -10*p,
    -49*s*p,
    -145*s**2*p - 95*p**2,
    -335*s**3*p - 658*s*p**2,
    -665*s**4*p - 2611*s**2*p**2 - 644*p**3,
    -1190*s**5*p - 7784*s**3*p**2 - 5758*s*p**3,
    -1974*s**6*p - 19362*s**4*p**2 - 28638*s**2*p**3 - 3777*p**4,
    -3090*s**7*p - 42420*s**5*p**2 - 104550*s**3*p**3 - 41360*s*p**4,
    -4620*s**8*p - 84546*s**6*p**2 - 312510*s**4*p**3 - 247225*s**2*p**4 - 20416*p**5,
]

print("\n--- Comparison: L = -SOURCE/L_op vs actual L_{-1} ---")
for m in range(min(N0+1, len(L_actual))):
    computed = sp.expand(L_from_formula[m])
    actual = sp.expand(L_actual[m])
    diff = sp.expand(computed - actual)
    print(f"  m={m}: computed={computed}, diff={diff} {'OK' if diff==0 else '**MISMATCH**'}")
