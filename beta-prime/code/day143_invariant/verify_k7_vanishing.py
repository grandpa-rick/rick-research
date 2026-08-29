"""Verify [E_3^7 T^b] X = 0 for b = 14, 15, 16, 17, 18, 19 at (U,V)=(0,0). B_MAX=21."""
import sys, os, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day142_angle4_ode')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day143_invariant')
from check_other_diagonals import compute_X_at
from sympy import symbols, Poly

T, E3 = symbols('T E3')

B_MAX = 21
print(f"Computing X at (U,V)=(0,0) with B_MAX = {B_MAX}...")
X = compute_X_at(0, 0, B_MAX)
Xp = Poly(X, T)

# For k=7, expect vanishing 2*7=14 ≤ b < 3*7-1=20, i.e. b=14..19
print("\nk=7 slice: [E_3^7 T^b] X for b = 14..20")
for b in range(14, 21):
    c = Xp.coeff_monomial(T**b)
    cE = Poly(c, E3).coeff_monomial(E3**7)
    tag = "← DIAG (a_7)" if b == 20 else ""
    status = "OK" if (b == 20) == (cE != 0) else "UNEXPECTED"
    print(f"  b={b}: value = {cE}  {tag}  [{status}]")

# Also for k=6, verify at higher b too
print("\nk=6 slice check: b = 12..17")
for b in range(12, 18):
    c = Xp.coeff_monomial(T**b)
    cE = Poly(c, E3).coeff_monomial(E3**6)
    tag = "← DIAG (a_6)" if b == 17 else ""
    print(f"  b={b}: value = {cE}  {tag}")
