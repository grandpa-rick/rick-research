"""Continue pattern hunt for c_0(r) in e_3 ⋆ e_r.

We have:
   c_0(r) = (q-1)/q^3 · d_0(r), where d_0(r) is a quadratic in q.
   d_0(r) = A_2(r,t) · q^2 - A_1(r,t) · q · t + A_0(r,t) · t^3
   with A_2(r,t) = [r+1]_t · [r+2]_t · [r+3]_t / ([2]_t · [3]_t).

Let me compute the q^0 and q^1 coefficients divided by t^? factors.

q^0 coefficients:
   r=3: t^3(t^3+1)
   r=4: t^3 · [7]_t
   r=5: t^3(t+1)(t^2+1)^2(t^4+1)

Divide by t^3:
   r=3: t^3+1 = 1 + t^3
   r=4: [7]_t = 1+t+t^2+t^3+t^4+t^5+t^6
   r=5: (t+1)(t^2+1)^2(t^4+1) = 1+t+2t^2+2t^3+2t^4+2t^5+2t^6+2t^7+t^8+t^9  (as expanded)

Hmm r=5 has all coefficients ≤ 2 with palindromic pattern. Not immediately recognizable.

Let me try: does q^0/t^3 = [r-2]_t · [r+3]_t · [r+2]_t / ([2]_t [3]_t)? — analogue of q^2 coeff.
   r=3: [1]_t · [6]_t · [5]_t / ([2]_t · [3]_t) = 1 · [6]_t · [5]_t / ((1+t)(1+t+t^2))
       [6]_t = (1+t+..+t^5); (1+t)(1+t+t^2) = (1+2t+2t^2+t^3). Hmm.
       Actually [6]_t / [2]_t = 1+t^2+t^4. [5]_t · (1+t^2+t^4) / [3]_t.
       [5]_t (1+t^2+t^4) = (1+t+t^2+t^3+t^4)(1+t^2+t^4) = expand...
       No, simpler: [6]_t · [5]_t = [6·5]... not helpful.
       Try: [6]_t · [5]_t / ([2]_t · [3]_t) = q-binomial coefficient C(5,2)_t · [5]_t / [3]_t? Not clean.
       Actually, [n+r choose r]_t = [n+r]_t! / ([n]_t! [r]_t!). So [5]_t · [6]_t / ([2]_t · [3]_t)? Hmm no.

Try a different form:  q^0/t^3 = something · [3]_t?
   r=3: 1+t^3 = 1+t^3. Doesn't factor by [3]_t = 1+t+t^2.
   r=4: [7]_t. Doesn't factor by [3]_t.

Try: q^0/t^3 - constant?
   r=3: 1+t^3
   r=4: 1+t+t^2+t^3+t^4+t^5+t^6
   r=5: 1+t+2t^2+2t^3+2t^4+2t^5+2t^6+2t^7+t^8+t^9

Difference r=4 - r=3: t+t^2+t^4+t^5+t^6 = t([1+t+t^3+t^4+t^5]). Ugly.

Let's try yet another form: maybe q^0 = t^3 · [r]_t · [r+3]_t / [2]_t?
   r=3: t^3 · [3]_t · [6]_t / [2]_t = t^3 (1+t+t^2)(1+t+...+t^5)/(1+t)
        = t^3 (1+t+t^2) · (1+t)(1+t^2)(1-t+t^2)?... this is getting messy.
        Numerically: [3]_t[6]_t/[2]_t: [3]_t=1+t+t^2; [6]_t=1+t+t^2+t^3+t^4+t^5; product=1+2t+3t^2+3t^3+3t^4+3t^5+2t^6+t^7. Divide by 1+t:
        (1+2t+3t^2+3t^3+3t^4+3t^5+2t^6+t^7)/(1+t) = 1+t+2t^2+t^3+2t^4+t^5+t^6+t^7? Let me do division.
        Actually not clean. So this guess is wrong.

I'll try a numerical approach: fit q^0 as polynomial combination of q-numbers.
"""

import sympy as sp

q, t = sp.symbols('q t')


def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


# Data
data_c0 = {
    3: (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    4: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    5: (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
}


def dq(c0, k):
    """Extract q^k coefficient from d_0(r) = c_0(r) * q^3 / (q-1)."""
    d = sp.expand(c0 * q**3 / (q - 1))
    return sp.Poly(d, q).nth(k)


# For each r=3,4,5, show q^0, q^1, q^2 factored
for r in [3, 4, 5]:
    c0 = data_c0[r]
    for k in [0, 1, 2]:
        coef = dq(c0, k)
        print(f"r={r}, q^{k} coef = {sp.factor(coef)}")
    print()

# Try: q^2 = [r+1]_t[r+2]_t[r+3]_t / ([2]_t[3]_t)   (confirmed)
# Conjecture q^0 = t^3 · [r]_t · [r+3]_t / ??? and q^1 = combination.
#
# Alternative: maybe there's a factored form
#   d_0(r) = f_2(r,t) q^2 - t f_1(r,t) q + t^3 f_0(r,t)
# where f_i(r,t) are all q-hooked polynomials.
#
# Note: from d_1(r) = [r+1]_t (q[r]_t - t[r-2]_t)/[2]_t we can factor as
#   d_1(r) = [r+1]_t / [2]_t · (q [r]_t - t [r-2]_t).
# The polynomial (q [r]_t - t [r-2]_t) has a lovely structure.

# For c_0(r), maybe similarly:
#   d_0(r) = X(r,t) · (q^2 A - q t B + t^3 C) / Y(r,t)
# where A, B, C are simple polynomials in t depending on r.

# Compute q^2/q^1 and q^1/q^0 ratios:
print("Ratios:")
for r in [3, 4, 5]:
    c0 = data_c0[r]
    a2 = dq(c0, 2)
    a1 = dq(c0, 1)
    a0 = dq(c0, 0)
    r21 = sp.simplify(a2 / a1)
    r10 = sp.simplify(a1 / a0)
    print(f"  r={r}: q^2/q^1 = {sp.factor(r21)}")
    print(f"          q^1/q^0 = {sp.factor(r10)}")
    print()

# Also: divide d_0(r) by the q^2 coefficient (which is [r+1][r+2][r+3]/([2][3]))
print("d_0(r) / (q^2 coefficient):")
for r in [3, 4, 5]:
    c0 = data_c0[r]
    a2 = dq(c0, 2)
    d = sp.expand(c0 * q**3 / (q - 1))
    ratio = sp.simplify(d / a2)
    print(f"  r={r}: d_0/A_2 = {sp.factor(ratio)}")

# Alternative approach: write in "shape" q^2 A - q·(sum) + t^3·B form.

# For e_2⋆e_r we had per Day 191:
#   c_0 = (q-1)([r+2]_t/[2]_t) · ([r+1]_t - t[r-1]_t/q)
#       = (q-1)([r+2]_t/[2]_t) · (q[r+1]_t - t[r-1]_t) / q
#   So d_0^{a=2}(r) = c_0 · q^2/(q-1) = [r+2]_t/[2]_t · (q[r+1]_t - t[r-1]_t) · q^1 / q
#      Wait, c_0 for a=2 = (q-1)/q^2 · (…) since c_2 = q^{-2}, that's the a=2 case.
#   Anyway the "linear-in-q" factor (q[r+1]_t - t[r-1]_t) is key.

# Guess for a=3: maybe d_0(r) = ([r+2]_t · [r+3]_t / ([2]_t · [3]_t)) · (q^2 [r+1]_t - q · t · (2 [r-1]_t) + t^3 [r-3]_t) or similar.
# But wait, q^2 coefficient is [r+1]·[r+2]·[r+3]/([2][3]). So if I factor out [r+2][r+3]/([2][3]), the q^2 coeff becomes [r+1]_t.
# Then q^1 coeff of remainder = ? , q^0 coeff = ?
print()
print("d_0(r) / ([r+2]_t[r+3]_t/([2]_t[3]_t)):")
for r in [3, 4, 5]:
    c0 = data_c0[r]
    a2 = dq(c0, 2)
    # Factor out [r+2][r+3]/([2][3])
    factor_out = qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    d = sp.expand(c0 * q**3 / (q - 1))
    reduced = sp.simplify(d / factor_out)
    print(f"  r={r}: reduced d_0 = {sp.factor(reduced)}")
    reduced_expand = sp.expand(reduced)
    print(f"          as poly in q: coeffs {sp.Poly(reduced_expand, q).all_coeffs()}")
