"""
Study free cumulants κ_n = -6, -90, -2238, -67470, -2254392, -80319438, -2990084436

Factor and look for patterns.
"""
from sympy import factorint, Rational

kappa = [-6, -90, -2238, -67470, -2254392, -80319438, -2990084436]

print("κ_n factorizations:")
for k in kappa:
    print(f"  {k} = -{factorint(-k)}")

# Ratios
print("\nκ_{n+1}/κ_n:")
for i in range(len(kappa)-1):
    r = Rational(kappa[i+1], kappa[i])
    print(f"  {r} ≈ {float(r):.4f}")

# Try κ_n / (-6): 1, 15, 373, 11245, ...
print("\nκ_n / (-6):")
for k in kappa:
    print(f"  {k/(-6)}")

# Try κ_n · something to match sequences
# Note κ_1 = -6 = -2·3 = 2·m_1/2. And m_1 = -6 = -2·3 = -2·b_1. So κ_1 = m_1.

# Compare to a_k: -3, -18, -255, -4620, -94500, -2078802, -48005802
# 2 · a_k = -6, -36, -510, -9240, -189000, -4157604, -96011604
# 4 · a_k = -12, -72, ...
# κ_n vs 2a_n:
# n=1: κ=-6, 2a=-6. MATCH.
# n=2: κ=-90, 2a=-36. no
# n=3: κ=-2238, 2a=-510. no

# Compare to b_k · const:
# b_k =        3,       27,     417,    7851,   164124,  3661389, 85384566
# κ_n / (-30): 0.2,     3,      74.6,   2249,   75146.4, 2677314.6, ...
# not clean.

# Try if κ_n is derivative-related.
