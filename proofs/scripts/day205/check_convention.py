"""Cross-check common.sigma against the Day 204 sigma_m_apply (build_action convention)."""
import sys, random
import sympy as sp
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day204')
sys.path.insert(0, '/home/agent/projects/proofs/scripts/day198')
from sigma_m_partial_symmetrizer import sigma_m_apply
from common import sigma, Xs
random.seed(1)
ok = True
for m in [2, 3, 4]:
    X = Xs(m)
    for trial in range(3):
        F = sp.Add(*[random.randint(-3, 3) * sp.Mul(*[x**random.randint(0, 2) for x in X]) for _ in range(4)])
        d = sp.expand(sigma(F, m) - sigma_m_apply(F, m))
        ok &= (d == 0)
        print(m, trial, d == 0)
print("convention cross-check:", "PASS" if ok else "FAIL")
