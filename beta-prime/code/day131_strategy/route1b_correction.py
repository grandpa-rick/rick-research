"""Route 1 continued: Analyze the E3-correction in the recursion
   tops[b+1] = (E2 - b*E1) * tops[b] + E3 * X_b
"""
import sys, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, e1_u, e2_u, e3_u,
                                 E1, E2, E3)
from sympy import expand, Poly, Integer, factor, simplify, diff, Rational

# Compute tops
tops = {}
for b in range(0, 7):
    psi_u = Psi_direct(e2_u**b) if b > 0 else Psi_direct(Integer(1))
    psi_e = sym_to_ebasis_direct(psi_u)
    tops[b] = top_weight_part(psi_e, b)
    print(f"tops[{b}] computed.")

# Compute X_b = (tops[b+1] - (E2 - b*E1)*tops[b]) / E3
print("\nCorrection X_b := (tops[b+1] - (E2 - b*E1)*tops[b]) / E3")
X = {}
for b in range(0, 6):
    diff_expr = expand(tops[b+1] - (E2 - b*E1)*tops[b])
    q, r = Poly(diff_expr, E3).div(Poly(E3, E3))
    if r.as_expr() != 0:
        print(f"  b={b}: NOT divisible by E3! remainder = {r.as_expr()}")
    else:
        X[b] = q.as_expr()
        print(f"  X_{b} = {X[b]}")
        print(f"    factored: {factor(X[b])}")

# X_b has (1,1,2)-weight b-1 (since (E2-b*E1)*tops[b] has weight b+1 and we divided by E3).
# Look for a pattern: is X_b = D(tops[b]) for some fixed differential operator D of weight -1?
# Wait, X_b has weight b+1 - 2 = b-1, and tops[b] has weight b. So D should have weight -1.
#
# Actually let's revisit: X_b = ? in terms of tops[b].
# tops[0] = 1, X_0 = -3. So X_0 has weight -1 -- but wait, tops[0] has weight 0.
# So X_0 has weight -1? Then it can't be polynomial in E's. But X_0 = -3, weight 0.
# Hmm. Recompute: tops[1] - (E2 - 0*E1)*tops[0] = (E2 - E1) - E2 = -E1. Divide by E3?
# NOT divisible! Let me check.

# Actually, wait, "divisible by E3" only if only E3-containing terms. Let me re-run above:
