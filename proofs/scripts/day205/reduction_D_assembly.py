"""
Day 205, Step D: assembly.
 (D1) SYMBOLIC IN r: with A := [r+2]_t, B := [r]_t, D := [2]_t treated as
      independent indeterminates (so no substitution t^r is needed, and the
      identity holds for EVERY integer r >= 1), the weighted sum
      1*(L1) + q^{-1}(L2) + q^{-1}(L3) + q^{-2}(L4) equals the Sub-Lemma Z table.
      Also the same check with [n]_t = (1 - t^n)/(1 - t), u = t^r symbolic.
 (D2) END-TO-END: e_1(Y) . (e_r e_1) computed directly from the Y_i (no
      sigma_m, no pi-split) equals sum_mu c_mu(Z_r) e_mu AS POLYNOMIALS,
      r = 1..7, m = 2..r+4 (m<=10); for m >= r+2 the e-expansion is unique and
      has exactly the 4 predicted nonzero terms when r >= 2 (3 when r = 1).
 (D3) NEGATIVE CONTROLS: wrong weights (1, q^{-1}, q^{-1}, q^{-1}) or a
      perturbed (L2) do not reproduce Z_r.
"""
import sys, time
import sympy as sp
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day205')
from reduction_engine import *

ok = True
# ---------- (D1) ----------
q, t, A, B, D, u = sp.symbols('q t A B D u')
E = {'(r+2)': 0, '(r+1,1)': 0, '(r,2)': 0, '(r,1,1)': 0}
L = {1: {'(r+2)': A, '(r+1,1)': t * B},
     2: {'(r+2)': -A, '(r+1,1)': 1},
     3: {'(r+2)': -A, '(r+1,1)': -t * B, '(r,2)': D},
     4: {'(r+2)': A, '(r+1,1)': -1, '(r,2)': -D, '(r,1,1)': 1}}
W = {1: 1, 2: 1 / q, 3: 1 / q, 4: 1 / q**2}
for k in L:
    for mu, c in L[k].items():
        E[mu] += W[k] * c
Z = {'(r+2)': (q - 1)**2 * A / q**2,
     '(r+1,1)': (q - 1) * (q * t * B + 1) / q**2,
     '(r,2)': (q - 1) * D / q**2,
     '(r,1,1)': 1 / q**2}
d1 = True
for mu in E:
    diff = sp.simplify(E[mu] - Z[mu])
    d1 &= diff == 0
    print(f"  (D1) {mu:8s}: assembled = {sp.factor(E[mu])}   target = {sp.factor(Z[mu])}   diff = {diff}")
subs = {A: (1 - u * t**2) / (1 - t), B: (1 - u) / (1 - t), D: 1 + t}
d1b = all(sp.simplify((E[mu] - Z[mu]).subs(subs)) == 0 for mu in E)
print("  (D1) with [n]_t=(1-t^n)/(1-t), u=t^r:", d1b)
ok &= d1 and d1b

# ---------- (D2) ----------
for r in range(1, 8):
    for m in range(2, r + 5):
        if m > 10: continue
        t0 = time.time()
        F = p_mul(e_sym(m, r), e_sym(m, 1))
        Zdir = e1Y(F, m)
        poly_ok = p_is_zero(p_add(Zdir, from_e_expansion(m, claimed_Z(r)), -1))
        msg = ""
        if m >= r + 2:
            ex = e_decompose(Zdir, m)
            uniq_ok = exp_equal(ex, claimed_Z(r))
            nsupp = len(ex)
            want = 4 if r >= 2 else 3
            poly_ok &= uniq_ok and nsupp == want
            msg = f", e-expansion unique & matches, support size {nsupp} (expect {want})"
        ok &= poly_ok
        print(f"  (D2) r={r} m={m}: e_1(Y)(e_r e_1) == sum c_mu e_mu: {poly_ok}{msg}  ({time.time()-t0:.1f}s)")

# ---------- (D3) ----------
r, m = 3, 5
X1 = var(m, 1); X1sq = p_mul(X1, X1); X1cu = p_mul(X1sq, X1)
f, g, h = e_tail(m, r), e_tail(m, r - 1), e_tail(m, 1)
Zdir = e_decompose(e1Y(p_mul(e_sym(m, r), e_sym(m, 1)), m), m)
badW = {1: c_Q(0), 2: c_Q(1), 3: c_Q(1), 4: c_Q(1)}
asm = {}
for k in range(1, 5): asm = exp_add(asm, claimed_L(r, k), badW[k])
neg1 = not exp_equal(asm, Zdir)
L2bad = dict(claimed_L(r, 2)); L2bad[(r + 1, 1)] = c_int(2)
asm = {}
for k in range(1, 5): asm = exp_add(asm, L2bad if k == 2 else claimed_L(r, k), WEIGHTS[k])
neg2 = not exp_equal(asm, Zdir)
print(f"  (D3) wrong weights rejected: {neg1};  perturbed (L2) rejected: {neg2}")
ok &= neg1 and neg2
print("STEP D OVERALL:", "PASSED" if ok else "FAILED")
