"""Verify the closed form c_0^(3)(r) against the freshly-computed r=6 data.

Load the pickled expansion from compute_e3_e6.py and check that the coefficient
of e_(9,) equals my closed-form prediction.
"""

import pickle
import sympy as sp

q, t = sp.symbols('q t')

def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))

# Load compute output
with open('/home/agent/projects/proofs/scripts/day193/e3_e6_m9.pkl', 'rb') as f:
    exp_r6 = pickle.load(f)

print("Nonzero coefficients from e_3 ⋆ e_6 compute (r=6, m=9):")
for lam, c in exp_r6.items():
    cs = sp.simplify(c)
    if cs != 0:
        print(f"  e_{lam} = {sp.factor(cs)}")

# Closed-form predictions
def closed_form_ck(k, r):
    if k == 3:
        return sp.Rational(1)/q**3
    elif k == 2:
        return (q-1) * qint(r-1) / q**3
    elif k == 1:
        return (q-1) * qint(r+1) * (q*qint(r) - t*qint(r-2)) / (q**3 * qint(2))
    elif k == 0:
        return (q-1)/q**3 * qint(r+3)/(qint(2)*qint(3)) * (
            qint(r+1)*qint(r+2)*q**2
            - t*qint(2)*qint(r-1)*qint(r+1)*q
            + t**3*qint(r-2)*qint(r-1)
        )
    else:
        raise ValueError

r = 6
print(f"\n\n=== Verifying closed forms at r={r} ===")
for k in [0, 1, 2, 3]:
    lam = (r+3-k, k) if k > 0 else (r+3,)
    actual = exp_r6.get(lam, sp.Integer(0))
    predicted = closed_form_ck(k, r)
    diff = sp.simplify(actual - predicted)
    status = "PASS" if diff == 0 else "FAIL"
    print(f"\nk = {k}, shape = {lam}: diff = {diff}  [{status}]")
    if diff != 0:
        print(f"  Actual:    {sp.factor(sp.simplify(actual))}")
        print(f"  Predicted: {sp.factor(sp.simplify(predicted))}")

# Also verify at (r=1, 2) via commutativity with Day 191
print(f"\n\n=== Verifying c_0^(3)(r) at r=1, 2 as boundary ===")
# r=1: e_3 ⋆ e_1 = e_1 ⋆ e_3 (Thm 3.12), so c_1(1) = q^{-1}, c_0(1) = (q-1)[4]_t/q^{-1}...
# actually Thm 3.12: e_1 ⋆ e_3 = q^{-1} e_{3,1} + (1-q^{-1})[4]_t e_4
# So c_0(1) = e_4 coeff = (1-1/q)[4] = (q-1)[4]/q. And 1/q term is c_1(1) = q^{-1}.

# For r=1 the closed form doesn't apply since it's a "top" boundary; conventional Thm 3.12 gives:
# c_0 coeff of e_4 = (q-1)[4]/q (single q^{-1} pole, not q^{-3})
# c_1 coeff of e_{3,1} = q^{-1}

# r=2: e_3 ⋆ e_2 = q^{-2} e_{3,2} + (q-1)/q^2·[3]_t·e_{4,1} + (q-1)(qt^2+q-t)[5]/q^2·e_5
# So this differs from the r>=3 formulas.

# Sanity at q=1
print("\n=== Sanity: e_3 ⋆ e_6 at q=1 ===")
for lam, c in exp_r6.items():
    cs = sp.simplify(c.subs(q, 1))
    if cs != 0:
        print(f"  e_{lam} at q=1 = {cs}  (should be 1 for lam=(6,3), 0 else)")

# Sanity at q -> ∞
print("\n=== Sanity: e_3 ⋆ e_6 at q → ∞ (leading term) ===")
for lam, c in exp_r6.items():
    cs = sp.simplify(c)
    if cs != 0:
        # Compute leading coefficient in q
        num = sp.numer(cs)
        den = sp.denom(cs)
        pn = sp.Poly(num, q)
        pd = sp.Poly(den, q)
        deg_num = pn.degree() if pn.degree() > 0 else 0
        deg_den = pd.degree() if pd.degree() > 0 else 0
        # (q-1)[stuff]/(q^k) as q -> infinity: expand
        lim = sp.limit(cs, q, sp.oo)
        print(f"  e_{lam} as q → ∞: {sp.factor(sp.simplify(lim))}")

# The predicted q -> ∞ limit is [r+3 choose 3]_t · e_{r+3}
r = 6
G = qint(r+1)*qint(r+2)*qint(r+3)/(qint(2)*qint(3))
print(f"\n  Predicted at q→∞: [{r+3} choose 3]_t = {sp.factor(sp.simplify(G))}")
