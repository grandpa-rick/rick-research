"""Erratum check for Lemma ER step (4) (Clio review UID 321, 2026-10-04).
b_lam(box;q,t) = (1 - q^a t^(l+1)) / (1 - q^(a+1) t^l)   [Macdonald VI (6.14)]
Checks, for every box of every partition with n <= 8:
  (old)  Rick's step-4 claim at t=0: b = 1 - q^(a+1) if l=0 else 1      -> expected to FAIL
  (new)  corrected claim at t=0:     b = 1/(1 - q^(a+1)) if l=0 else 1  -> expected to PASS
  (q0)   q=0 claim: b = 1 - t^(l+1) if a=0 else 1                       -> expected to PASS
  (unit) numerator and denominator of b are each nonzero at q=0 (in Q(t)) and at t=0 (in Q(q)),
         so b is a unit in R_0 = Q(t)[q]_(q) and in R_inf = Q(q)[t]_(t).
"""
import sympy as sp
from sympy.utilities.iterables import partitions
q, t = sp.symbols('q t')

def boxes(lam):
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    for i, r in enumerate(lam):
        for j in range(r):
            yield (i, j, r - j - 1, conj[j] - i - 1)   # (row, col, arm, leg)

cnt = dict(old_fail=0, new_fail=0, q0_fail=0, unit_fail=0, boxes=0)
witness = None
for n in range(1, 9):
    for p in partitions(n):
        lam = sorted([k for k, m in p.items() for _ in range(m)], reverse=True)
        for (i, j, a, l) in boxes(lam):
            cnt['boxes'] += 1
            num = 1 - q**a * t**(l + 1); den = 1 - q**(a + 1) * t**l
            b = num / den
            bt0 = sp.simplify(b.subs(t, 0)); bq0 = sp.simplify(b.subs(q, 0))
            old = (1 - q**(a + 1)) if l == 0 else 1
            new = 1 / (1 - q**(a + 1)) if l == 0 else 1
            q0c = (1 - t**(l + 1)) if a == 0 else 1
            if sp.simplify(bt0 - old) != 0:
                cnt['old_fail'] += 1
                if witness is None: witness = (lam, (i + 1, j + 1), a, l, bt0, old)
            if sp.simplify(bt0 - new) != 0: cnt['new_fail'] += 1
            if sp.simplify(bq0 - q0c) != 0: cnt['q0_fail'] += 1
            if any(sp.expand(e) == 0 for e in (num.subs(q, 0), num.subs(t, 0), den.subs(q, 0), den.subs(t, 0))):
                cnt['unit_fail'] += 1
print(cnt)
print('first witness against old step 4 (lam, box(row,col), arm, leg, true b|t=0, claimed):', witness)
