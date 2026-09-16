"""Continued P_4 analysis: find factors for each q-coefficient.

From r=4 analysis:
  q^0 / -t^6 = [r-3][r-2][r-1]        (checks at r=4)

Let's check that this holds at r=5, and hunt for the other three coeffs.
"""

import sympy as sp
q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))

P4_r4 = {
    3: (t + 1)*(t**2 - t + 1)*(t**2 + t + 1)*(t**4 + t**3 + t**2 + t + 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1),
    2: -t*(t + 1)*(t**2 - t + 1)*(t**2 + t + 1)**3*(t**4 + t**3 + t**2 + t + 1),
    1: t**3*(t + 1)*(t**2 + t + 1)**2*(t**4 + t**3 + t**2 + t + 1),
    0: -t**6*(t + 1)*(t**2 + t + 1),
}
P4_r5 = {
    3: (t + 1)**2*(t**2 + 1)*(t**4 + 1)*(t**2 - t + 1)*(t**2 + t + 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1),
    2: -t*(t + 1)**2*(t**2 + 1)*(t**2 - t + 1)*(t**2 + t + 1)**2*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1),
    1: t**3*(t + 1)**2*(t**2 + 1)*(t**2 - t + 1)*(t**2 + t + 1)**3,
    0: -t**6*(t + 1)**2*(t**2 + 1)*(t**2 + t + 1),
}


def show_ratios(r, coeffs):
    tpows = {3: 0, 2: 1, 1: 3, 0: 6}
    signs = {3: 1, 2: -1, 1: 1, 0: -1}
    normed = {}
    for degq in [3, 2, 1, 0]:
        normed[degq] = sp.simplify(coeffs[degq] * signs[degq] / t**tpows[degq])
    return normed

norm_r4 = show_ratios(4, P4_r4)
norm_r5 = show_ratios(5, P4_r5)

# Test hypothesis: for each q-degree, the coefficient factors as a product of [r+*] terms and a "constant" polynomial in t.
# By analogy to a=3:
#   q^2 / +1 = [r+1][r+2]           (both [r+*], no constants except denominator [2] in prefactor... wait)
# Actually a=3 P_3 = q^2·[r+1][r+2] - t·q·[2][r-1][r+1] + t^3·[r-2][r-1]

# So an a=3-analog for a=4 P_4:
#   q^3 · A(r)  where A(r) is cubic q-integer product with lead [r+3]
#   q^2 · -t · B(r) where B(r) is cubic with lead [r+2] and has [2] or [3] factor
#   q^1 · +t^3 · C(r) where C(r) is cubic with lead [r+1] and has more
#   q^0 · -t^6 · D(r) where D(r) is cubic bottom.

# a=3 shape summarized:
#   D_2(r) = [r+1][r+2]  (top pair)
#   D_1(r) = [2][r-1][r+1]  (middle pair × [2])
#   D_0(r) = [r-2][r-1]   (bottom pair)
# For a=4 by analogy, insert an extra [r-1] type factor (cubic instead of quadratic):
#   E_3(r) = [r+1][r+2][r+3]/[3] ?  (cubic q-Gaussian style)
#     — but for a=3 the top D_2 is [r+1][r+2] = [r+2]!/[2]·[r]!... hmm, actually D_2 = binom(r+2,2)_t · [2]  (× [2])
#   Actually [r+1][r+2]/[2] = binom(r+2, 2)_t is the q-Gaussian. But in D_2 we have unnormalized [r+1][r+2].
#
# Let's try:
#   E_3(r) = [r+1][r+2][r+3] / [3]   (this is [3] · binom(r+3, 3)_t / ... hmm)
#     Actually [r+1][r+2][r+3] / ([2][3]) = binom(r+3, 3)_t is the q-Gaussian.
#     But E_3 = [r+1][r+2][r+3]/[3]  =  [2] · binom(r+3, 3)_t.

# Test at r=4:
print("=== Test hypothesis: P_4 coefficients as [r+*] cubic products ===")
for r in [4, 5]:
    norms = norm_r4 if r == 4 else norm_r5
    print(f"\n--- r={r} ---")
    for degq in [3, 2, 1, 0]:
        print(f"  q^{degq} normalized: {sp.factor(norms[degq])}")
    print()

# Analogy: shift pattern for a=3 D_j:
#   D_2 has [r+1][r+2]     (indices +1, +2)
#   D_1 has [r-1][r+1]     (indices -1, +1)
#   D_0 has [r-2][r-1]     (indices -2, -1)
# For a=4 might have:
#   E_3 has [r+1][r+2][r+3]           (+1, +2, +3)
#   E_2 has [r-1][r+1][r+2]           (-1, +1, +2)?  or [r-1][r][r+2] etc.
#   E_1 has [r-2][r-1][r+1]           (-2, -1, +1)?
#   E_0 has [r-3][r-2][r-1]           (-3, -2, -1)
# with extra q-integer factors from Pochhammer-like [2], [3]

# For a=3 D_1 has [2] factor. Maybe for a=4:
#   E_2 has [3] or [2] factor
#   E_1 has more
# So try ansatz: E_j = [const q-int] · [r+shift_1][r+shift_2][r+shift_3]

print("\n=== Try [r+*] cubic ansätze at both r=4 and r=5 ===")
candidates = [
    # (label, expression_generator)
    ("[r+1][r+2][r+3]", lambda r: qint(r+1)*qint(r+2)*qint(r+3)),
    ("[r+1][r+2][r+3]/[3]", lambda r: qint(r+1)*qint(r+2)*qint(r+3)/qint(3)),
    ("[r+1][r+2][r+3]/([2][3])", lambda r: qint(r+1)*qint(r+2)*qint(r+3)/(qint(2)*qint(3))),
    # E_2 candidates (cubic with drop of 3 from top)
    ("[r-1][r+1][r+2]", lambda r: qint(r-1)*qint(r+1)*qint(r+2)),
    ("[r-1][r+1][r+2]·[3]", lambda r: qint(r-1)*qint(r+1)*qint(r+2)*qint(3)),
    ("[r-1][r+1][r+2]·[2]", lambda r: qint(r-1)*qint(r+1)*qint(r+2)*qint(2)),
    ("[r+2][r-1][r]", lambda r: qint(r+2)*qint(r-1)*qint(r)),
    # E_1 candidates
    ("[r-2][r-1][r+1]", lambda r: qint(r-2)*qint(r-1)*qint(r+1)),
    ("[r-2][r-1][r+1]·[3]", lambda r: qint(r-2)*qint(r-1)*qint(r+1)*qint(3)),
    ("[r-2][r-1][r+1]·[2]", lambda r: qint(r-2)*qint(r-1)*qint(r+1)*qint(2)),
    ("[r-2][r-1][r+2]", lambda r: qint(r-2)*qint(r-1)*qint(r+2)),
    # E_0 candidates
    ("[r-3][r-2][r-1]", lambda r: qint(r-3)*qint(r-2)*qint(r-1)),
]

for degq in [3, 2, 1, 0]:
    print(f"\n--- q^{degq} coeff (normalized by sign·t^tpow) ---")
    for label, gen in candidates:
        v4 = sp.simplify(gen(4))
        v5 = sp.simplify(gen(5))
        if v4 == 0 or v5 == 0:
            continue
        r4 = sp.simplify(norm_r4[degq] / v4)
        r5 = sp.simplify(norm_r5[degq] / v5)
        # If both ratios equal, this is a candidate factor
        if sp.simplify(r4 - r5) == 0:
            print(f"  MATCH  {label}:  ratio = {sp.factor(r4)}")
