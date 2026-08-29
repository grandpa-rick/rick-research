"""Extend the check: verify [E_3^k T^b] X pattern for k = 1..6, various b near 3k-1.
Look for the FULL structure of zeros and non-zeros."""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day143_invariant')
from check_other_diagonals import compute_X_at, extract_diag_offset

B_MAX = 18
print(f"Computing X at (U,V)=(0,0) with B_MAX = {B_MAX}")
X = compute_X_at(0, 0, B_MAX)

# For each k, print [E_3^k T^b] for b = 2k, 2k+1, ..., B_MAX-1
from sympy import Poly, symbols, Integer
T, E3 = symbols('T E3')
Xp = Poly(X, T)

print("\n=== [E_3^k T^b] X at (U,V)=(0,0) — look for zero patterns ===")
print("     Rows: k. Columns: T-power b.  '·' = 0, non-zero shown.")
K_MAX = 6

# Header
b_range = list(range(2, B_MAX))
header = "k \\ b" + "".join(f"  {b:>4}" for b in b_range)
print(header)
for k in range(1, K_MAX + 1):
    line = f" {k}   "
    for b in b_range:
        c = Xp.coeff_monomial(T**b)
        cE = Poly(c, E3).coeff_monomial(E3**k)
        if cE == 0:
            line += "    ·  "
        else:
            # show sign
            s = "-" if cE < 0 else "+"
            line += f"    {s}  "
    print(line)

print("\n=== Explicit values near diagonal T^{3k-1} ===")
for k in range(1, K_MAX + 1):
    print(f"\nk={k}: (diagonal T^{3*k-1})")
    for b in range(max(2, 2*k), min(B_MAX, 3*k + 2)):
        c = Xp.coeff_monomial(T**b)
        cE = Poly(c, E3).coeff_monomial(E3**k)
        marker = "  ← DIAG" if b == 3*k - 1 else ("  ← ZERO" if b == 3*k - 2 else "")
        print(f"  [E_3^{k} T^{b}] X = {cE}{marker}")
