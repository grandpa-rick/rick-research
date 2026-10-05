"""
Day 205, Step A:  for symmetric F in Lambda_m and each 1 <= i <= m,
      Y_i . F = rho_i pi F,   rho_i := T_{i-1} ... T_1,
hence e_1(Y) . F = sigma_m pi F.
Proof: T_j F = tF for symmetric F => T_j^{-1} F = t^{-1} F, and each
intermediate t^{-k} F is still symmetric; the t^{m-i} prefactor cancels.
Checked here on F = e_r e_1 (the Sub-Lemma Z input) and on a few more
symmetric F, r = 2..6, m = r+2, r+3; per-i (stronger than the sum).
Negative control: the per-i identity FAILS for a non-symmetric F.
"""
import sys, time
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day205')
from reduction_engine import *

ok = True
for r in range(2, 8):
    for m in (r + 2, r + 3, r + 4):
        if m > 10: continue
        t0 = time.time()
        inputs = {f"e_{r} e_1": p_mul(e_sym(m, r), e_sym(m, 1)),
                  f"e_{r}": e_sym(m, r)}
        for name, F in inputs.items():
            piF = PI(F)
            tot = {}
            for i in range(1, m + 1):
                lhs = Y(F, i, m)
                rhs = rho(piF, i)
                good = p_is_zero(p_add(lhs, rhs, -1))
                ok &= good
                if not good:
                    print(f"  FAIL r={r} m={m} F={name} i={i}")
                tot = p_add(tot, lhs)
            good = p_is_zero(p_add(tot, sigma(piF, m), -1))
            ok &= good
            print(f"  r={r} m={m} F={name}: Y_i F = rho_i pi F for all i, and e_1(Y)F = sigma_m pi F: {good}  ({time.time()-t0:.1f}s)")
# negative control
m = 3
F = monomial(m, (2, 0, 1))
bad = any(not p_is_zero(p_add(Y(F, i, m), rho(PI(F), i), -1)) for i in range(1, m + 1))
print("  negative control (non-symmetric F = X1^2 X3): identity fails as expected:", bad)
ok &= bad
print("STEP A OVERALL:", "PASSED" if ok else "FAILED")
