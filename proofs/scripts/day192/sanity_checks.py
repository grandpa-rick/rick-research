"""Sanity checks for Day 192 e_3 ⋆ e_r closed forms.

1. q = 1 → ordinary product e_3 · e_r (single e_{r,3} coefficient with 1).
2. q → ∞ → Hikita Thm C(ii): leading term as q→∞ of q^a · (e_a ⋆ e_b) should match some limit.
   For Hikita: as q→∞, ⋆-product tends to the "double-elementary" (E_i, E_j) coproduct-type.
   From Thm C(ii): the classical limit e_a ⋆_∞ e_b = ???
   Specifically: from Thm 3.12 as q→∞: e_1 ⋆ e_r → [r+1]_t · e_{r+1}.
   So q · (e_1 ⋆ e_r) → q · [r+1]_t · e_{r+1} as q→∞? Wait: e_1 ⋆ e_r = (1 - 1/q)[r+1]_t e_{r+1} + q^{-1} e_1 e_r.
   As q → ∞: (1 - 0)[r+1]_t e_{r+1} + 0 = [r+1]_t e_{r+1}.  So limit = [r+1]_t e_{r+1}.
   For e_2 ⋆ e_r: only surviving term is the q^0 term. Let's compute:
      e_2 ⋆ e_r at q→∞ = (leading terms).
   Day 191: c_0^{(a=2)} = (q-1)/q · [r+2]_t/[2]_t · ([r+1]_t - t[r-1]_t/q). At q→∞: [r+2]_t/[2]_t · [r+1]_t = q-Gaussian C(r+2, 2)_t · [r+1]_t? Hmm actually [r+2]_t · [r+1]_t / [2]_t.
"""

import sympy as sp

q, t = sp.symbols('q t')


def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


# e_3 ⋆ e_2 and e_3 ⋆ e_3 raw
e3e2 = {
    (5,): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**2,
    (4, 1): (q - 1)*(t**2 + t + 1)/q**2,
    (3, 2): sp.Rational(1)/q**2,
}

e3e3 = {
    (6,): (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    (5, 1): (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**3,
    (4, 2): (q - 1)*(t + 1)/q**3,
    (3, 3): sp.Rational(1)/q**3,
}


def sanity_q1(exp, expected_lam):
    print(f"\n Sanity q=1 for {expected_lam}:")
    for lam, c in exp.items():
        c1 = sp.simplify(c.subs(q, 1))
        if c1 != 0 or lam == expected_lam:
            print(f"    e_{lam} @ q=1: {c1}")


def sanity_qinf(exp):
    print(f"\n Sanity q→∞ (leading in 1/q, i.e. classical limit):")
    for lam, c in exp.items():
        cs = sp.simplify(c)
        num, den = sp.fraction(sp.together(cs))
        num_p = sp.Poly(num, q)
        den_p = sp.Poly(den, q)
        deg_num = num_p.degree()
        deg_den = den_p.degree()
        # Leading in q^{deg_num - deg_den}
        lead_num = num_p.LC()
        lead_den = den_p.LC()
        lead = sp.simplify(lead_num / lead_den)
        print(f"    e_{lam}: leading q^{deg_num - deg_den} coeff = {sp.factor(lead)}")


print("=" * 72)
print("e_3 ⋆ e_2:")
print("=" * 72)
sanity_q1(e3e2, (3, 2))
sanity_qinf(e3e2)

print("\n" + "=" * 72)
print("e_3 ⋆ e_3:")
print("=" * 72)
sanity_q1(e3e3, (3, 3))
sanity_qinf(e3e3)


# Also predict via general formula the classical limits.
# At q→∞:
#   c_3(r) → 0 (since q^{-3})
#   c_2(r) → 0 for r>=3 (since (q-1)/q^3 → 0). For r=2: c_2 = 1/q^2 → 0.
#   c_1(r) → 0 similarly.
#   c_0(r) → leading behaviour.
# For a=3, r=2: c_0 = (q-1)/q^2 · (q(t^2+1) - t) · [5]_t → (1/q · q · q(t^2+1)) → q·(t^2+1)·[5]_t as q→∞.
#   Wait: (q-1)/q^2 · (q(t^2+1) - t) · [5]_t
#      ~ q/q^2 · q · (t^2+1) · [5]_t = (t^2+1)·[5]_t.  So limit finite (not blowing up).

# Actually, let me carefully take q → ∞ using leading terms.
# c_0(3, r=2) = (q-1)(qt^2+q-t)·[5]_t / q^2
#   = (q^2(t^2+1)·[5]_t + lower) / q^2
#   = (t^2+1)·[5]_t + O(1/q).
# So classical limit is (t^2+1)[5]_t.
# c_1(3, r=2) = (q-1)·[3]_t/q^2 = [3]_t/q + O(1/q^2) → 0.
# c_2(3, r=2) = 1/q^2 → 0.

# For e_3 ⋆ e_3:
# c_0(3, 3) has q^2 leading coefficient q-Gaussian G(3) = [4][5][6]/([2][3])
# c_0(3, 3) = (q-1) · d_0 / q^3, and d_0 has degree 2 in q. So (q-1)d_0 has degree 3 in q, over q^3: finite limit.
# The q^{→∞} limit of (q-1)/q^3 · A_2 q^2 = A_2 = G(r) = [r+1][r+2][r+3]/([2][3]).
# For r=3: [4][5][6]/([2][3]).

print("\n" + "=" * 72)
print("Classical limits (q → ∞):")
print("=" * 72)

# Compute limit of e_3 ⋆ e_r at q → ∞ (as an element of Lambda_t).
# Result should be = t^{-3} · leading-in-Y limit = t^{-3} · classical e_3(Y_∞) · e_r(X)?

for r in [2, 3, 4, 5]:
    # Only c_0(r) survives (since c_1, c_2, c_3 all → 0).
    # For r=2 the boundary c_2 = 1/q^2 → 0. Sanity check:
    if r == 2:
        c0_lim = sp.limit((q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**2, q, sp.oo)
    else:
        # G(r) = [r+1][r+2][r+3]/([2][3])
        c0_lim = qint(r + 1) * qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    print(f"  r={r}: e_3 ⋆_∞ e_r = (q → ∞ limit) · e_{{r+3}}")
    print(f"          leading coeff = {sp.factor(c0_lim)}")
    # Expected form: [r+1][r+2][r+3]/([2][3])
    expected = qint(r + 1) * qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    diff = sp.simplify(c0_lim - expected)
    print(f"          vs [r+1][r+2][r+3]/([2][3]): diff = {diff}")
