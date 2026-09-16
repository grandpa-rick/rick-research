"""Analyze P_4 coefficients as q-integer products.

Recall pattern from a=3 (P_3):
  P_3(r) = [r+2][r+1] q^2 - t·[2]·[r-1][r+1] q + t^3 [r-2][r-1]
  q^2: [r+1][r+2]
  q^1 / -t: [2] [r-1][r+1]
  q^0 / t^3: [r-2][r-1]

Prediction for P_4 (using shift r+*, a-relative):
  Meta-shape: coeff of q^{l-1-j} times t^{binom(j+1,2)}
  For P_4 (l=4), j=0,1,2,3, t-exponents 0, 1, 3, 6.
  P_4(r,a=4) should be built from [r+*-4] terms (a=4 uses [r+2-a]=[r-2], etc.).

For a=3 P_3 [r-1][r+1][r+2] appear (up-to shift).
For a=4 P_4: expected some cubic-in-t [r+*] factors on each q coeff.

Extract coefficients numerically at r=4, 5 and try to fit.
"""

import sympy as sp
q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))

# Data: P_4(q,t;r) coefficients we computed
# For r=4:
P4_r4 = {
    3: (t + 1)*(t**2 - t + 1)*(t**2 + t + 1)*(t**4 + t**3 + t**2 + t + 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1),
    2: -t*(t + 1)*(t**2 - t + 1)*(t**2 + t + 1)**3*(t**4 + t**3 + t**2 + t + 1),
    1: t**3*(t + 1)*(t**2 + t + 1)**2*(t**4 + t**3 + t**2 + t + 1),
    0: -t**6*(t + 1)*(t**2 + t + 1),
}
# For r=5:
P4_r5 = {
    3: (t + 1)**2*(t**2 + 1)*(t**4 + 1)*(t**2 - t + 1)*(t**2 + t + 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1),
    2: -t*(t + 1)**2*(t**2 + 1)*(t**2 - t + 1)*(t**2 + t + 1)**2*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1),
    1: t**3*(t + 1)**2*(t**2 + 1)*(t**2 - t + 1)*(t**2 + t + 1)**3,
    0: -t**6*(t + 1)**2*(t**2 + 1)*(t**2 + t + 1),
}


# Verify: try candidate ansätze inspired by a=3.

# Ansatz for P_4 (a=4): natural cubic [r+*-4] factors:
# P_4 = q^3 · [r+1][r+2][r+3]/[3] - t·q^2·? + t^3 q ? - t^6 ?
# where [r+*] shifts are (r+1,r+2,r+3) for the "top" cubic, then drop by 3 each.

# From a=3 P_3: coeffs = [r+2][r+1] q^2 - t[2][r-1][r+1] q + t^3 [r-2][r-1]
# with prefactor [r+3]/[3]. Full: c_0^(3) = (q-1)/q^3 · [r+3]/([2][3]) · P_3
# For a=4 with prefactor [r+4]/([2][3][4]):
# By analogy try:
# q^3 coeff: [r+1][r+2][r+3]/[3]  (top cubic in [r+*])
# q^2 coeff (divide by -t): [r-1][r+1][r+2]·(some [k])
# q^1 coeff (divide by t^3): [r-2][r-1][r+2]·(some)?
# q^0 coeff (divide by -t^6): [r-3][r-2][r-1]·(1)?  (bottom cubic, all lowered by 3)

# Try minimal ansatz:
# Q3(r) = [r+1][r+2][r+3]/[3]  (already q-Gaussian ~ [r+3 choose 3]_t · [3])
# Actually let's guess parallel to a=3:
#   D_2 = [r+1][r+2]/[2]    (a=3, matches [r+3 choose 2]_t = [r+1][r+2]/[2])
#   D_1 = [r-1][r+1]         (a=3 middle, has [2] factor pulled out)
#   D_0 = [r-2][r-1]         (a=3 bottom cubic degree)
#
# For a=4 by analogy:
#   D_3(r) = [r+1][r+2][r+3]/([2][3])   (top q-Gaussian binom(r+3,3)_t)
#   D_2(r) = [r-1][r+1][r+2] ·? / ?
#   D_1(r) = [r-2][r-1][r+1] · ? / ?
#   D_0(r) = [r-3][r-2][r-1]/([2][3])

# Let's check at r=4:
print("=== Test candidate cubic q-integer factors at r=4 ===")
for r in [4, 5]:
    print(f"\n--- r={r} ---")
    for label, expr in [
        ("[r+1][r+2][r+3]/([2][3])", qint(r+1)*qint(r+2)*qint(r+3)/(qint(2)*qint(3))),
        ("[r-1][r+1][r+2]", qint(r-1)*qint(r+1)*qint(r+2)),
        ("[r-1][r+1][r+2]/[2]", qint(r-1)*qint(r+1)*qint(r+2)/qint(2)),
        ("[r-2][r-1][r+1]", qint(r-2)*qint(r-1)*qint(r+1)),
        ("[r-2][r-1][r+1]/[3]", qint(r-2)*qint(r-1)*qint(r+1)/qint(3)),
        ("[r-3][r-2][r-1]/([2][3])", qint(r-3)*qint(r-2)*qint(r-1)/(qint(2)*qint(3))),
        ("[r-3][r-2][r-1]", qint(r-3)*qint(r-2)*qint(r-1)),
    ]:
        v = sp.simplify(expr)
        print(f"  {label:40s} = {sp.factor(v)}")
    print("  Actual P_4 coeffs:")
    P4 = P4_r4 if r == 4 else P4_r5
    for degq in [3, 2, 1, 0]:
        val = sp.factor(sp.simplify(P4[degq]))
        # Divide by ±t^{binom(...)}
        tpow = {3: 0, 2: 1, 1: 3, 0: 6}[degq]
        sign = 1 if degq in (3, 1) else -1
        norm = sp.factor(sp.simplify(P4[degq] * sign / t**tpow))
        print(f"    q^{degq}, /±t^{tpow}: {norm}")


# Compare ratios directly at r=4:
print("\n=== Direct ratios at r=4 ===")
r = 4
for degq, tpow, sign in [(3, 0, 1), (2, 1, -1), (1, 3, 1), (0, 6, -1)]:
    print(f"\n--- q^{degq} coefficient (/{sign:+d}·t^{tpow}) ---")
    coeff_norm = sp.simplify(P4_r4[degq] * sign / t**tpow)
    for label, expr in [
        ("[r+1][r+2][r+3]/([2][3])", qint(r+1)*qint(r+2)*qint(r+3)/(qint(2)*qint(3))),
        ("[r-1][r+1][r+2]/[2]", qint(r-1)*qint(r+1)*qint(r+2)/qint(2)),
        ("[r-1][r+1][r+2]", qint(r-1)*qint(r+1)*qint(r+2)),
        ("[r-2][r-1][r+1]", qint(r-2)*qint(r-1)*qint(r+1)),
        ("[r-2][r-1][r+1]/[3]", qint(r-2)*qint(r-1)*qint(r+1)/qint(3)),
        ("[r-3][r-2][r-1]", qint(r-3)*qint(r-2)*qint(r-1)),
        ("[r-3][r-2][r-1]/([2][3])", qint(r-3)*qint(r-2)*qint(r-1)/(qint(2)*qint(3))),
    ]:
        v = sp.simplify(expr)
        if v == 0:
            continue
        ratio = sp.simplify(coeff_norm / v)
        print(f"  ratio to {label} = {sp.factor(ratio)}")
