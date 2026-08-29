"""
TEST 5: Asymptotic. Fit b_k ~ C · r^k · k^α · (k!)^β.
"""
from sympy import Rational, log, N, symbols, Matrix, factorial
from math import log as mlog, factorial as mfact

b = [3, 27, 417, 7851, 164124, 3661389, 85384566]  # k=1..7

print("k, b_k, b_{k+1}/b_k, log(b_k), log(b_k)/k, b_k^(1/k)")
for i in range(len(b)):
    k = i+1
    ratio = float(b[i+1]/b[i]) if i+1 < len(b) else None
    lb = mlog(b[i])
    print(f"  k={k}  b={b[i]:>12}  ratio={ratio}  ln(b)={lb:.4f}  ln(b)/k={lb/k:.4f}  b^(1/k)={b[i]**(1/k):.4f}")

# Ratio: 9, 15.44, 18.83, 20.90, 22.31, 23.32
# Growing slowly — consistent with r^k · k^α (not k!)
# If b_k ~ C r^k k^α, then b_{k+1}/b_k → r as k→∞ but with correction (1+1/k)^α
# The ratio isn't stabilizing yet. Try fitting log form.

# Model: log b_k = log C + k log r + α log k + β log(k!)
# 4 unknowns, 7 equations — least squares fit.
# Use exact rational log via numpy floats.
import numpy as np
ks = np.array([1,2,3,4,5,6,7], dtype=float)
logb = np.array([mlog(x) for x in b])

# Try three models:
# (M1) log b = log C + k log r + α log k
X1 = np.column_stack([np.ones(7), ks, np.log(ks)])
coefs1, res1, _, _ = np.linalg.lstsq(X1, logb, rcond=None)
print(f"\nModel: log b = A + B·k + α·log k")
print(f"  A={coefs1[0]:.4f} (C={np.exp(coefs1[0]):.4f}), B={coefs1[1]:.4f} (r={np.exp(coefs1[1]):.4f}), α={coefs1[2]:.4f}")
print(f"  residuals: {logb - X1 @ coefs1}")

# (M2) log b = A + B·k + α·log k + β·log(k!)
logfact = np.array([mlog(mfact(k)) for k in ks.astype(int)])
X2 = np.column_stack([np.ones(7), ks, np.log(ks), logfact])
coefs2, _, _, _ = np.linalg.lstsq(X2, logb, rcond=None)
print(f"\nModel: log b = A + B·k + α·log k + β·log(k!)")
print(f"  A={coefs2[0]:.4f}, B={coefs2[1]:.4f}, α={coefs2[2]:.4f}, β={coefs2[3]:.4f}")
print(f"  residuals: {logb - X2 @ coefs2}")

# (M3) log b = A + B·k + α·log k only, using last 4 points
X3 = X1[3:]
coefs3, _, _, _ = np.linalg.lstsq(X3, logb[3:], rcond=None)
print(f"\nModel (last 4 pts): log b = A + B·k + α·log k")
print(f"  A={coefs3[0]:.4f} (C={np.exp(coefs3[0]):.4f}), B={coefs3[1]:.4f} (r={np.exp(coefs3[1]):.4f}), α={coefs3[2]:.4f}")

# Interpret r as growth constant. Compare to (27)^{1/2} = 5.196 or e^π etc.
print("\nGuesses for r:")
r_est = np.exp(coefs1[1])
print(f"  r_M1 ≈ {r_est:.6f}")
print(f"  27 ≈ 27; 27^0.5 ≈ 5.196; 27^(1/3) ≈ 3; 3√3·something?")
print(f"  Ratio_last = b_7/b_6 = {b[6]/b[5]:.6f}")
print(f"  Ratio_last squared = {(b[6]/b[5])**2:.6f}")

# The ratio 23.32, 22.31, 20.90, 18.83, 15.44, 9 suggests linear in k asymptotically:
# ratio ≈ r · (1 + α/k + O(1/k²)) if b_k ~ C r^k k^α
# So r·(1+α/k+O(1/k²)) → r as k→∞ and (ratio_k - ratio_{k-1}) ≈ -r·α/k² ...
# Actually 23.32 - 22.31 = 1.01 — still growing linearly! Suggests β>0 (has k!)
# Because if b_k ~ C r^k k! then ratio_{k+1}/ratio_k = r·(k+1) which grows linearly.

# Test: b_{k+1}/b_k vs k
print("\nb_{k+1}/b_k / k:")
for i in range(len(b)-1):
    k = i+1
    ratio = b[i+1]/b[i]
    print(f"  k={k}: ratio/k = {ratio/k:.6f}")

# Consistent with something?

# Try: (b_{k+1}/b_k) fit to a + b/k or a + b·k?
print("\nFit b_{k+1}/b_k = A + B·k?")
ks_r = np.array([1,2,3,4,5,6], dtype=float)
rs = np.array([b[i+1]/b[i] for i in range(6)])
X = np.column_stack([np.ones(6), ks_r])
c, _, _, _ = np.linalg.lstsq(X, rs, rcond=None)
print(f"  A={c[0]:.4f}, B={c[1]:.4f}, residuals: {rs - X @ c}")

print("\nFit b_{k+1}/b_k = A + B/k?")
X = np.column_stack([np.ones(6), 1/ks_r])
c, _, _, _ = np.linalg.lstsq(X, rs, rcond=None)
print(f"  A={c[0]:.4f}, B={c[1]:.4f}, residuals: {rs - X @ c}")

print("\nFit log(b_{k+1}/b_k) = A + B·log(k)?")
X = np.column_stack([np.ones(6), np.log(ks_r)])
c, _, _, _ = np.linalg.lstsq(X, np.log(rs), rcond=None)
print(f"  A={c[0]:.4f}, B={c[1]:.4f}, so ratio ~ e^A · k^B = {np.exp(c[0]):.4f} · k^{c[1]:.4f}")
