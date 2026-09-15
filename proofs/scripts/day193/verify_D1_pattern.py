"""Verify Rick's conjectured pattern for D_1(r) [coefficient of q^1 in D^(3)(r)].

Conjecture: -A_1(r) = coeff of q in c_0^(3)(r) * q^3/(q-1) is
    -A_1(r) = t * [r-1]_t * [r+1]_t * [r+3]_t / [3]_t

Verify for r = 3, 4, 5.

Also verify overall low-j Day 192 formulas symbolically.
"""

import sympy as sp
q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))

# Day 192 data for c_0^(3)(r):
data_c0 = {
    3: (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    4: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    5: (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
}

print("Verifying D_1(r) conjecture:")
print("=" * 70)
for r, c0 in data_c0.items():
    D = sp.expand(c0 * q**3 / (q - 1))
    Dp = sp.Poly(D, q)
    D2 = Dp.nth(2)
    D1 = Dp.nth(1)
    D0 = Dp.nth(0)

    print(f"\nr = {r}:")
    print(f"  D_2 = coeff of q^2 = {sp.factor(D2)}")
    print(f"  D_1 = coeff of q^1 = {sp.factor(D1)}")
    print(f"  D_0 = coeff of q^0 = {sp.factor(D0)}")

    # Check D_2 = G(r) = [r+1][r+2][r+3]/([2][3])
    G_r = qint(r+1)*qint(r+2)*qint(r+3)/(qint(2)*qint(3))
    G_r = sp.simplify(G_r)
    diff = sp.simplify(D2 - G_r)
    print(f"  D_2 - G(r) = {diff}   [G(r) = {sp.factor(G_r)}]")

    # Check D_1 = -t * [r-1][r+1][r+3]/[3]
    conj_D1 = -t * qint(r-1) * qint(r+1) * qint(r+3) / qint(3)
    conj_D1 = sp.simplify(conj_D1)
    diff1 = sp.simplify(D1 - conj_D1)
    print(f"  D_1 - conj = {diff1}   [conj: -t[{r-1}][{r+1}][{r+3}]/[3] = {sp.factor(conj_D1)}]")

    # Print D_0 for pattern hunting
    print(f"  D_0/t^3 = {sp.factor(sp.simplify(D0/t**3))}")

print("\n\n" + "=" * 70)
print("Testing D_0(r) hypotheses:")
print("=" * 70)

for r, c0 in data_c0.items():
    D = sp.expand(c0 * q**3 / (q - 1))
    Dp = sp.Poly(D, q)
    D0 = Dp.nth(0)
    D0_over_t3 = sp.simplify(D0/t**3)

    print(f"\nr = {r}, D_0/t^3 = {sp.factor(D0_over_t3)}")

    # Hypothesis 1: [r-1][r+3][r+1]/([2][3])
    h1 = qint(r-1)*qint(r+1)*qint(r+3)/(qint(2)*qint(3))
    diff = sp.simplify(D0_over_t3 - h1)
    print(f"  H1: [r-1][r+1][r+3]/([2][3]) = {sp.factor(sp.simplify(h1))}; diff = {sp.simplify(diff)}")

    # Hypothesis 2: [r-2][r+3]/[3] * something
    # Hypothesis: symmetric across... let's try [r-2][r][r+3]/[3]
    h2 = qint(max(r-2, 0))*qint(r)*qint(r+3)/qint(3)
    diff2 = sp.simplify(D0_over_t3 - h2)
    print(f"  H2: [r-2][r][r+3]/[3] = {sp.factor(sp.simplify(h2))}; diff = {sp.simplify(diff2)}")
