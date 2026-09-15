"""Systematic pattern hunt for e_3 ⋆ e_r using q-integer identities.

Focus on d_k(r) = c_k(r) * q^3 / (q-1) for k=0,1 (and k=2,3 already established).

r=3: c_1 raw = (t^2+1)(qt^2+qt+q-t)/q^3 · (q-1)
r=4: c_1 raw = (qt^2+q-t)·[5]_t/q^3 · (q-1)
r=5: c_1 raw = (t^4+t^2+1)(qt^4+qt^3+qt^2+qt+q-t^3-t^2-t)/q^3 · (q-1)

Note that for r=3 vs r=4, the "outer" and "inner" factors trade roles:
  r=3: outer = (t^2+1) = [4]_t/[2]_t;  inner = q·(t^2+t+1) - t = q[3]_t - t
  r=4: outer = (qt^2+q-t) = q(1+t^2) - t = q[2]_{t^2} - t;   inner = [5]_t
  r=5: outer = (t^4+t^2+1) = [6]_t/[2]_t;  inner = q[5]_t - t[3]_t = q[5]_t - t(1+t+t^2)

So we have two "features" per c_1: an outer q-independent factor and an inner q-linear factor.

r=3: c_1 = (q-1)·[4]_t/[2]_t · (q[3]_t - t) / q^3
r=4: c_1 = (q-1)·[5]_t · (q[2]_{t^2} - t)/q^3
r=5: c_1 = (q-1)·[6]_t/[2]_t · (q[5]_t - t[3]_t)/q^3

But r=4 has a different "outer" structure. Let me check if there's a uniform form.
Try: c_1(r) = (q-1)/q^3 · [r+1]_t · (q · A_r(t) - t · B_r(t)) / [2]_t
   r=3: (q-1)/q^3 · [4]_t · (q [3]_t - t) / [2]_t = (q-1)/q^3 · (t+1)(1+t^2)/(t+1) · (q[3]_t - t) = (q-1)(1+t^2)(q[3]_t - t)/q^3. YES!
   r=4: (q-1)/q^3 · [5]_t · (q · A - t · B)/[2]_t. Actual: (q-1)/q^3 · (q(t^2+1)-t)·[5]_t
     = (q-1)[5]_t/q^3 · (q(t^2+1) - t) = (q-1)[5]_t·(q[2]_{t^2} - t)/q^3
     Compare with template: need (q·A - t·B)/[2]_t = q[2]_{t^2} - t → A/[2]_t · q term = q(t^2+1), so A = (t^2+1)(t+1) = [4]_{t}(?)? Actually (t^2+1)(t+1) = 1+t+t^2+t^3 = [4]_t. And B/[2]_t · t term = t, so B = [2]_t = t+1.
     So r=4: c_1 = (q-1)/q^3 · [5]_t · (q [4]_t - t [2]_t) / [2]_t. YES.
   r=5: (q-1)/q^3 · [6]_t · (q · A - t · B)/[2]_t = raw
     raw: (q-1)/q^3 · [6]_t/[2]_t · (q[5]_t - t[3]_t)
        = (q-1)/q^3 · [6]_t · (q[5]_t - t[3]_t)/[2]_t
     So A = [5]_t, B = [3]_t.  Compare with r=4: A = [4]_t, B = [2]_t. Compare with r=3: A = [3]_t, B = [1]_t.
     Pattern: A = [r]_t, B = [r-2]_t!

So unified formula:
   c_1(r) = (q-1) · [r+1]_t · (q [r]_t - t [r-2]_t) / (q^3 · [2]_t)  for r >= 3.

Verify:
   r=3: (q-1)[4]_t · (q[3]_t - t[1]_t) / (q^3 [2]_t) = (q-1)(t+1)(t^2+1)/(t+1) · (q(1+t+t^2) - t) / q^3
      = (q-1)(t^2+1)(qt^2+qt+q-t)/q^3 = actual r=3 ✓
   r=4: (q-1)[5]_t · (q[4]_t - t[2]_t)/(q^3 [2]_t) = (q-1)[5]_t · (q(t+1)(1+t^2) - t(t+1))/((t+1)q^3)
      = (q-1)[5]_t · ((t+1)(q(1+t^2) - t)) / (q^3(t+1)) = (q-1)[5]_t(q(1+t^2) - t)/q^3 = actual ✓
   r=5: (q-1)[6]_t · (q[5]_t - t[3]_t)/(q^3 [2]_t). Actual: (q-1)[6]_t/[2]_t · (q[5]_t - t[3]_t)/q^3 = SAME ✓

Extrapolation to r=1, r=2:
   r=2: c_1 = (q-1)[3]_t · (q[2]_t - t[0]_t) / (q^3 [2]_t)?  [0]_t := 0.
      = (q-1)[3]_t · q[2]_t / (q^3 [2]_t) = (q-1)[3]_t/q^2. Actual r=2: (q-1)(t^2+t+1)/q^2 = (q-1)[3]_t/q^2. YES!
   r=1: (q-1)[2]_t · (q[1]_t - t[-1]_t)/(q^3 [2]_t) = (q-1)(q - 0)/q^3 = (q-1)/q^2. Actual r=1 c_1: 1/q. Hmm doesn't match.
      Actual r=1 shows only 2 terms and c_1 = 1/q [that's e_(3,1)]. Let me re-read: r=1 data has k=0 → e_4 = (q-1)(t+1)(t^2+1)/q, k=1 → e_{3,1} = 1/q. But wait, r=1 means the *_r side, and a=3, so partitions of 4. So (a+b-k, k) for k=0,1 gives (4), (3,1). k=1 is c_1(1) = 1/q, NOT (q-1)/q^2.

Hmm, r=1 doesn't fit the general formula. But r=1 has min(3,1)+1 = 2 terms, and by commutativity e_3⋆e_1 = e_1⋆e_3 = (Thm 3.12). At r=1, the k=1 slot is at the boundary (it IS the "bottom" slot), so the formula changes.

At r=2 (also boundary since k=2 is bottom): the c_2 formula changes from (q-1)[r-1]_t/q^3 to just 1/q^2. And c_1 formula (from my check) still works.

So the general formula c_1(r) works for r >= 2.
"""

import sympy as sp

q, t = sp.symbols('q t')


def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


data = {
    (1, 0): (q - 1)*(t + 1)*(t**2 + 1)/q,
    (1, 1): sp.Rational(1)/q,
    (2, 0): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**2,
    (2, 1): (q - 1)*(t**2 + t + 1)/q**2,
    (2, 2): sp.Rational(1)/q**2,
    (3, 1): (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**3,
    (3, 2): (q - 1)*(t + 1)/q**3,
    (3, 3): sp.Rational(1)/q**3,
    (4, 1): (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**3,
    (4, 2): (q - 1)*(t**2 + t + 1)/q**3,
    (4, 3): sp.Rational(1)/q**3,
    (5, 1): (q - 1)*(t**2 - t + 1)*(t**2 + t + 1)*(q*t**4 + q*t**3 + q*t**2 + q*t + q - t**3 - t**2 - t)/q**3,
    (5, 2): (q - 1)*(t + 1)*(t**2 + 1)/q**3,
    (5, 3): sp.Rational(1)/q**3,
}


def check(name, r, k, guess):
    if (r, k) not in data:
        print(f"  {name} r={r} k={k}: no data")
        return None
    diff = sp.simplify(data[(r, k)] - guess)
    status = "PASS" if diff == 0 else "FAIL"
    print(f"  {name} r={r} k={k}: diff = {sp.factor(diff)}   [{status}]")
    return diff == 0


print("=" * 72)
print("Conjectured formulas (v4) for e_3 ⋆ e_r ")
print("=" * 72)

print("\nc_1(r) = (q-1) · [r+1]_t · (q [r]_t - t [r-2]_t) / (q^3 · [2]_t)   [r >= 2]:")
all_ok = True
for r in [2, 3, 4, 5]:
    guess = (q - 1) * qint(r + 1) * (q * qint(r) - t * qint(r - 2)) / (q**3 * qint(2))
    ok = check("c_1", r, 1, guess)
    all_ok = all_ok and (ok or ok is None)
print(f"  Overall c_1 for r >= 2: {'PASS' if all_ok else 'FAIL'}")

# At r=1: expected c_1 = 1/q from Thm 3.12 (e_3⋆e_1 = e_1⋆e_3, coeff of e_{3,1} = q^{-1}).
# Does the general formula collapse to 1/q at r=1?
# guess r=1: (q-1)·[2]_t·(q·[1]_t - t·0)/(q^3·[2]_t) = (q-1)·q/q^3 = (q-1)/q^2. NOT 1/q.
# So formula fails at r=1 (boundary case where k=1 is min(3,1)=1).
# At the "bottom" slot, coefficient is always q^{-a} (from AHA scaling).

# For c_0(r): let me try more aggressive template.

# From d_0(r) analysis:
#   r=3: q^0: t^3 (t+1)(t^2-t+1) = t^3 [4]_t/[2]_t · ??? hmm t^3(t+1)(t^2-t+1) = t^3(t^3+1)
#        Note t^3(t+1)(t^2-t+1) = t^3 · (t+1)(t^2-t+1) = t^3 · (t^3+1). So q^0 = t^3(t^3+1).
#   r=4: q^0: t^3 [7]_t
#   r=5: q^0: t^3 (t+1)(1+t^2)^2(1+t^4) = t^3 · [something]
#
# Try to compute in terms of [k]_t:
#   r=3: t^3(t^3+1) = t^3 · [6]_t/[2]_t · [1]_t?? [6]_t=1+t+..+t^5. Not obvious.
#   Note (t^3+1) = (t+1)(t^2-t+1). And [6]_t = (t+1)(1+t+t^2)(1+t^3)/... hmm.
# Alternative: for r=3: t^3·(t^3+1) = t^3+t^6. For r=4: t^3·[7]_t = t^3(1+t+...+t^6).
# For r=5: t^3(t+1)(t^2+1)^2(t^4+1).

# For c_2(r>=3): already have (q-1)[r-1]_t/q^3. Compare with c_2(r=2) = 1/q^2.
# At r=2, the k=2 slot is the "bottom": min(3,2)=2. Coefficient is 1/q^2 = 1/q^{min(a,r)}?
# At r>=3, k=2 is "middle": (q-1)[r-1]_t/q^3.

# For c_0(r), let me try: d_0(r) has degree 2 in q. Coefficient of q^2:
#   r=3: (t+1)(t^2+1)(t^2-t+1)(t^4+t^3+t^2+t+1) = (t^3+1)(t^2+1)·[5]_t
#        Note (t^3+1)(t^2+1) = ... nah try [6]_t/[2]_t · [5]_t: [6]_t/[2]_t = t^4+t^2+1. Not same.
#        Actually (t+1)(t^2-t+1) = t^3+1 = [6]_t/[3]_t. And (t^2+1) = [4]_t/[2]_t.
#        So q^2 coefficient = (t^3+1)(t^2+1)[5]_t = [6]_t/[3]_t · [4]_t/[2]_t · [5]_t.
#   r=4: (t^2-t+1)·[5]_t·[7]_t. Note (t^2-t+1) = [6]_{t}/[2]_t/[3]_t · (t+1)(t^2+t+1) hmm.
#        Or: (t^2-t+1) = (t^3+1)/(t+1) = [6]_t/([2]_t·[3]_t). So q^2 coef = [6]_t/([2]_t·[3]_t) · [5]_t · [7]_t.
#   r=5: (t+1)(t^2+1)(t^4+1)(t^2-t+1)·[7]_t
#        (t+1)(t^2+1)(t^4+1) = 1+t+t^2+...+t^7 = [8]_t.
#        (t^2-t+1) = [6]_t/([2]_t[3]_t).
#        So q^2 coef = [8]_t · [6]_t/([2]_t[3]_t) · [7]_t = [6]_t · [7]_t · [8]_t / ([2]_t · [3]_t).
#
# So q^2 coefficient at r>=3:
#   r=3: [4]_t · [5]_t · [6]_t / ([2]_t · [3]_t)   [checking: [4]/[2]·[5]·[6]/[3] = same, yes]
#   r=4: [5]_t · [6]_t · [7]_t / ([2]_t · [3]_t)
#   r=5: [6]_t · [7]_t · [8]_t / ([2]_t · [3]_t)
# Pattern: q^2 coefficient = [r+1]_t · [r+2]_t · [r+3]_t / ([2]_t · [3]_t)   — the q-Gaussian coefficient (r+3 choose 3)_t? Yes!

print()
print("Testing c_0(r): q^2 coefficient = [r+1]_t·[r+2]_t·[r+3]_t / ([2]_t·[3]_t) = q-Gaussian coeff.")
data_c0 = {
    3: (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    4: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    5: (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
}

for r in [3, 4, 5]:
    d = sp.expand(data_c0[r] * q**3 / (q - 1))
    dp = sp.Poly(d, q)
    q2_coef = dp.nth(2)
    guess_q2 = qint(r + 1) * qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    diff = sp.simplify(q2_coef - guess_q2)
    print(f"  r={r}: q^2 diff = {diff}   [{'PASS' if diff == 0 else 'FAIL'}]")

# Now the q^0 and q^1 coefficients of d_0(r):
print()
print("q^0 coefficients of d_0(r) = c_0(r) · q^3/(q-1):")
guesses_q0 = {}
for r in [3, 4, 5]:
    d = sp.expand(data_c0[r] * q**3 / (q - 1))
    dp = sp.Poly(d, q)
    q0 = dp.nth(0)
    print(f"  r={r}: q^0 = {sp.factor(q0)}")
    guesses_q0[r] = q0

# r=3: t^3 (t+1)(t^2-t+1) = t^3(t^3+1)
# r=4: t^3 · [7]_t
# r=5: t^3 (t+1)(1+t^2)^2(1+t^4). (1+t^2)(1+t^4) = 1+t^2+t^4+t^6 = ?
#      Note (t+1)(1+t^2)^2(1+t^4)... Let's think.
#      1+t^2 = [4]_t/[2]_t.  1+t^4 = [8]_t/[4]_t.  (t+1) = [2]_t.
#      Product: [2]_t · ([4]_t/[2]_t)^2 · [8]_t/[4]_t = [4]_t · [8]_t / [2]_t.
#      Verify: (t+1)(t^2+1)^2(t^4+1) = [2]_t · [4]_t^2/[2]_t^2 · [8]_t/[4]_t = [4]_t · [8]_t / [2]_t.
#      Substituting: [4]_t · [8]_t / [2]_t.

# So q^0 factors:
#   r=3: t^3 · [6]_t/[3]_t   [since t^3+1 = [6]_t/[3]_t but wait [6]_t/[3]_t = (1+t^3)... yes since [6]_t = (1+t+..+t^5) = (1+t^3)(1+t+t^2) = [6]_t = (1+t^3)·[3]_t. So [6]_t/[3]_t = 1+t^3 = t^3+1 ✓]
#   r=4: t^3 · [7]_t
#   r=5: t^3 · [4]_t · [8]_t / [2]_t

# Hmm not obvious. Let me try:
#   r=3: t^3 (t^3+1). Coefficient at r+3=6.
#   r=4: t^3 [7]_t. Coefficient at r+3=7.
#   r=5: t^3 · (t+1)(t^2+1)^2(t^4+1). Coefficient at r+3=8. In q-form...

# Alternate: maybe q^0 = t^3 · [something depending on r].
# r=3: (t^3+1) has degree 3.
# r=4: [7]_t has degree 6.
# r=5: (t+1)(t^2+1)^2(t^4+1) has degree 1+2+2+4 = 9.
# Deg 3, 6, 9: arithmetic progression! Difference 3.

# In terms of q-integers:
# r=3: (t^3+1) = (t^6-1)/(t^3-1) not q-integer. But it IS (t^3+1) = 1+t^3.
# r=4: [7]_t = (t^7-1)/(t-1). Coefficient degree 6.
# r=5: (t+1)(t^2+1)^2(t^4+1). Hmm.

# Try: q^0 = t^3 · [3(?)] Note [3]_t^0 has degree 0. Not matching.

# One more try: r=3: t^3(t^3+1) = t^3 + t^6.
# r=4: t^3[7]_t = t^3(1+t+t^2+t^3+t^4+t^5+t^6) = t^3+t^4+...+t^9. Deg 3..9.
# r=5: t^3 · (t+1)(1+t^2)^2(1+t^4) = t^3·(1+t)(1+2t^2+t^4)(1+t^4). Hmm this has multiplicities.
#      Actually (1+t^2)^2 = 1 + 2t^2 + t^4.
#      Let me just expand r=5 q^0 numerically.

r5q0 = sp.expand(t**3 * (t + 1) * (t**2 + 1)**2 * (t**4 + 1))
print(f"\n  r=5 q^0 expanded: {r5q0}")
