"""VERIFY the CLOSED FORM for c_0^(3)(r) discovered on Day 193.

CONJECTURE: c_0^(3)(r) = (q-1)/q^3 · [r+3]/([2][3]) · ([r+1][r+2] q² - t[2][r-1][r+1] q + t³[r-2][r-1])

Equivalently, with D^(3)(r) = c_0 · q^3/(q-1) = D_2 q² - t D_1 q + t³ D_0:
  D_2(r) = [r+1][r+2][r+3]/([2][3])  (= q-Gaussian binom(r+3,3)_t)
  D_1(r) = [r-1][r+1][r+3]/[3]
  D_0(r) = [r-2][r-1][r+3]/([2][3])

Verify on r=3, 4, 5.
"""

import sympy as sp
q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))

# Day 192 data
data_c0 = {
    3: (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    4: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    5: (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
}


def closed_form_c0(r):
    """Conjectured c_0^(3)(r) closed form."""
    prefactor = qint(r+3) / (qint(2) * qint(3))
    inner = (qint(r+1) * qint(r+2) * q**2
             - t * qint(2) * qint(r-1) * qint(r+1) * q
             + t**3 * qint(r-2) * qint(r-1))
    return (q - 1) / q**3 * prefactor * inner


print("Verifying c_0^(3)(r) closed form:")
print("=" * 70)
for r in [3, 4, 5]:
    actual = sp.simplify(data_c0[r])
    conjecture = sp.simplify(closed_form_c0(r))
    diff = sp.simplify(actual - conjecture)
    status = "PASS" if diff == 0 else "FAIL"
    print(f"\nr = {r}: diff = {diff}   [{status}]")
    if diff != 0:
        print(f"  Actual:     {sp.factor(sp.simplify(actual))}")
        print(f"  Conjecture: {sp.factor(sp.simplify(conjecture))}")

print("\n\n" + "=" * 70)
print("Prediction for r=6:")
print("=" * 70)
r = 6
conj = closed_form_c0(r)
print(f"c_0^(3)(6) = {sp.factor(sp.simplify(conj))}")
print()
D_pred = sp.expand(conj * q**3 / (q-1))
Dp = sp.Poly(D_pred, q)
print(f"D_2(6) [q^2 coeff] = {sp.factor(Dp.nth(2))}")
print(f"D_1(6) [q^1 coeff / (-t)] = {sp.factor(-Dp.nth(1)/t)}")
print(f"D_0(6) [q^0 coeff / t^3] = {sp.factor(Dp.nth(0)/t**3)}")

# Sanity: verify formulas
print("\nSanity checks for formulas:")
for r in [3, 4, 5, 6]:
    G_r = qint(r+1)*qint(r+2)*qint(r+3)/(qint(2)*qint(3))
    D1_r = qint(r-1)*qint(r+1)*qint(r+3)/qint(3)
    D0_r = qint(r-2)*qint(r-1)*qint(r+3)/(qint(2)*qint(3))
    print(f"\nr={r}: ")
    print(f"  G(r) = {sp.factor(sp.simplify(G_r))}")
    print(f"  D_1(r) = {sp.factor(sp.simplify(D1_r))}")
    print(f"  D_0(r) = {sp.factor(sp.simplify(D0_r))}")

# Sanity: at t=1
print("\n\nSanity at t=1:")
print("  D_0(r)|_{t=1} = (r-2)(r-1)(r+3)/6:")
for r in [3, 4, 5, 6, 7]:
    D0_r = qint(r-2)*qint(r-1)*qint(r+3)/(qint(2)*qint(3))
    val = sp.simplify(D0_r.subs(t, 1))
    expected = (r-2)*(r-1)*(r+3)/6
    print(f"  r={r}: {val} (expected {expected})")
