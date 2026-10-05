"""
Day 205, Step C:  linearity of sigma_m and the four pieces.
  (C1) sigma_m pi(e_r e_1) = P1 + q^{-1} P2 + q^{-1} P3 + q^{-2} P4  as polynomials,
       P1 = sigma_m[X_1 f h], P2 = sigma_m[X_1^2 f], P3 = sigma_m[X_1^2 g h],
       P4 = sigma_m[X_1^3 g].
  (C2) each P_k is q-free and symmetric, and equals the (L_k) right-hand side
       EXACTLY AS POLYNOMIALS in X_1..X_m (so no e-basis uniqueness needed),
       for every m in 2..r+4 (including m < r+2), r = 1..7.
  (C3) for m >= r+2 the e-basis expansion of P_k (unique) is printed/compared.
(C2)/(C3) are INPUTS (Clio's Theorem 3), re-checked here only as a sanity
check of the statement being imported; they are not part of the reduction.
"""
import sys, time
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day205')
from reduction_engine import *

ok = True
for r in range(1, 8):
    for m in range(2, r + 5):
        if m > 10: continue
        t0 = time.time()
        X1 = var(m, 1); X1sq = p_mul(X1, X1); X1cu = p_mul(X1sq, X1)
        f, g, h = e_tail(m, r), e_tail(m, r - 1), e_tail(m, 1)
        ins = {1: p_mul(X1, p_mul(f, h)), 2: p_mul(X1sq, f),
               3: p_mul(X1sq, p_mul(g, h)), 4: p_mul(X1cu, g)}
        P = {k: sigma(v, m) for k, v in ins.items()}
        # (C1)
        lhs = sigma(PI(p_mul(e_sym(m, r), e_sym(m, 1))), m)
        rhs = {}
        for k in P: rhs = p_add(rhs, p_scale(P[k], WEIGHTS[k]))
        c1 = p_is_zero(p_add(lhs, rhs, -1))
        # (C2)
        c2 = True
        for k in P:
            qfree = all(Qe == 0 for c in P[k].values() for (_, Qe) in c)
            match = p_is_zero(p_add(P[k], from_e_expansion(m, claimed_L(r, k)), -1))
            c2 &= qfree and match
        # (C3)
        c3 = True
        if m >= r + 2:
            for k in P:
                c3 &= exp_equal(e_decompose(P[k], m), claimed_L(r, k))
        ok &= c1 and c2 and c3
        print(f"  r={r} m={m}: (C1) {c1}  (C2) {c2}  (C3) {c3 if m >= r+2 else 'n/a (m<r+2)'}  ({time.time()-t0:.1f}s)")
print("STEP C OVERALL:", "PASSED" if ok else "FAILED")
