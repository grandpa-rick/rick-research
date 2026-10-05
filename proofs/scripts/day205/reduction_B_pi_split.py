"""
Day 205, Step B:  pi = X_1 * rho_q where rho_q F := F(X_2,...,X_m, q^{-1}X_1) is a
RING HOMOMORPHISM.  Hence
  (B1) X_1 pi(FG) = pi(F) pi(G)                              [any F, G]
  (B2) pi(e_r) = X_1 e_r(tail) + q^{-1} X_1^2 e_{r-1}(tail)   [r >= 1]
  (B3) pi(e_r e_1) = X_1 f h + q^{-1} X_1^2 (f + g h) + q^{-2} X_1^3 g,
       f = e_r(tail), g = e_{r-1}(tail), h = e_1(tail).
Checked r = 1..6, m = 2..r+3 (includes m < r+2, where e_r(tail) may vanish).
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day205')
from reduction_engine import *

ok = True
for r in range(1, 8):
    for m in range(2, r + 5):
        if m > 10: continue
        X1 = var(m, 1)
        f, g, h = e_tail(m, r), e_tail(m, r - 1), e_tail(m, 1)
        er, e1 = e_sym(m, r), e_sym(m, 1)
        b1 = p_is_zero(p_add(p_mul(X1, PI(p_mul(er, e1))), p_mul(PI(er), PI(e1)), -1))
        b2 = p_is_zero(p_add(PI(er), p_add(p_mul(X1, f), p_scale(p_mul(p_mul(X1, X1), g), c_Q(1))), -1))
        X1sq, X1cu = p_mul(X1, X1), p_mul(p_mul(X1, X1), X1)
        rhs = p_add(p_add(p_mul(X1, p_mul(f, h)),
                          p_scale(p_mul(X1sq, p_add(f, p_mul(g, h))), c_Q(1))),
                    p_scale(p_mul(X1cu, g), c_Q(2)))
        b3 = p_is_zero(p_add(PI(p_mul(er, e1)), rhs, -1))
        ok &= b1 and b2 and b3
        print(f"  r={r} m={m}: (B1) {b1}  (B2) {b2}  (B3) {b3}")
print("STEP B OVERALL:", "PASSED" if ok else "FAILED")
