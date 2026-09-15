"""More careful pattern-hunting for c_1(r) and c_0(r) in e_3 ⋆ e_r.

r=3: c_1 = (q-1)(t^2+1)(qt^2+qt+q-t)/q^3
       = (q-1)(t^2+1) · (q(1+t+t^2) - t)/q^3
       = (q-1)(t^2+1) · (q[3]_t - t)/q^3

r=4: c_1 = (q-1)(qt^2+q-t)(t^4+t^3+t^2+t+1)/q^3
       = (q-1) · (q(1+t^2) - t) · [5]_t / q^3
       = (q-1) · [5]_t · (q(1+t^2) - t) / q^3

r=5: c_1 = (q-1)(t^2-t+1)(t^2+t+1)(qt^4+qt^3+qt^2+qt+q-t^3-t^2-t)/q^3
       = (q-1)(t^4+t^2+1) · (q[5]_t - t·t(1+t+t^2))/q^3
       = (q-1) · [6]_t/[2]_t · (q[5]_t - t^2·[3]_t) / q^3
   Note: t^4+t^2+1 = (t^2-t+1)(t^2+t+1) = [6]_t/[2]_t   (also = [3]_{t^2})

Look, let me redo:
r=3: (t^2+1) = [4]_t/[2]_t. So factor = [4]_t/[2]_t. Linear-in-q part: q[3]_t - t.
r=4: [5]_t. Linear-in-q part: q(1+t^2) - t = q[2]_{t^2} - t.
r=5: [6]_t/[2]_t. Linear-in-q part: q[5]_t - (t^3+t^2+t) = q[5]_t - t[3]_t.

Hmm, the "leading in q" factor is:
   r=3: q[3]_t - t
   r=4: q(1+t^2) - t = q[2]_{t^2} - t
   r=5: q[5]_t - t[3]_t = q[5]_t - t(1+t+t^2)

Let me try re-expressing. Maybe: q[r+1]_t - t[r-1]_t?
   r=3: q[4]_t - t[2]_t = q(1+t+t^2+t^3) - t(1+t) = q+qt+qt^2+qt^3-t-t^2. NOPE, we want q+qt+qt^2-t.
   r=3: qt^2+qt+q-t = q(1+t+t^2) - t = q[3]_t - t. So actual formula uses [3]_t not [4]_t.

Try: q[r]_t - t[r-2]_t?
   r=3: q[3]_t - t[1]_t = q(1+t+t^2) - t. YES matches r=3.
   r=4: q[4]_t - t[2]_t = q(1+t+t^2+t^3) - t(1+t) = q+qt+qt^2+qt^3-t-t^2.
        But r=4 has q+qt^2-t = q(1+t^2) - t. NO.

So r=3 and r=4 don't have the same formula pattern.

Let me try to write these in a different way:
r=3: (t^2+1)(qt^2+qt+q-t)
   Expand: qt^2·(t^2+1) + qt·(t^2+1) + q·(t^2+1) - t·(t^2+1)
         = qt^4+qt^2 + qt^3+qt + qt^2+q - t^3-t
         = q + qt + 2qt^2 + qt^3 + qt^4 - t - t^3
Combine: (q-1) · above / q^3.

r=4: (qt^2+q-t)(t^4+t^3+t^2+t+1)
   = q(t^2+1)(1+t+t^2+t^3+t^4) - t(1+t+t^2+t^3+t^4)
   = q(1+t+t^2+t^3+t^4+t^2+t^3+t^4+t^5+t^6) - t - t^2 - t^3 - t^4 - t^5
   = q(1+t+2t^2+2t^3+2t^4+t^5+t^6) - (t+t^2+t^3+t^4+t^5)

r=5: (t^2-t+1)(t^2+t+1)(qt^4+qt^3+qt^2+qt+q-t^3-t^2-t)
   (t^2-t+1)(t^2+t+1) = t^4+t^2+1
   inner: q[5]_t - t(1+t+t^2) = q[5]_t - t[3]_t
   = (t^4+t^2+1)(q[5]_t - t[3]_t)

Actually r=3 form: (t^2+1)(q[3]_t - t). Note t^2+1 = [4]_t/[2]_t = 1 + t^2 (the "even" q-integer at t^2).
Or: (t^2+1) = t^{r-1}·[2]_{t^-1} for r=3? Let's see: t^2 + 1... hmm.

Try: maybe factor as (t^{r-1} + something · t^{r-3} + ...).
r=3: t^2+1
r=4: t^4+t^3+t^2+t+1 = [5]_t
r=5: t^4+t^2+1 = (t^6-1)/(t^2-1)

Pattern check: what happens with e_{r+2, 1}? Note c_1(r) = (q-1)/q^3 * (something in q, t) always.
Let me define d_1(r) = c_1(r) * q^3 / (q-1).
   d_1(3) = (t^2+1)(qt^2+qt+q-t)
   d_1(4) = (qt^2+q-t)(t^4+t^3+t^2+t+1)
   d_1(5) = (t^2-t+1)(t^2+t+1)(qt^4+qt^3+qt^2+qt+q-t^3-t^2-t)

Ratio d_1(4) / d_1(3) as polynomial in q,t...
"""

import sympy as sp

q, t = sp.symbols('q t')

def qint(n):
    return sum(t**i for i in range(n))

data_c1 = {
    2: (q - 1)*(t**2 + t + 1)/q**2,
    3: (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**3,
    4: (q - 1)*(q*t**2 + q - t)*(t**4 + t**3 + t**2 + t + 1)/q**3,
    5: (q - 1)*(t**2 - t + 1)*(t**2 + t + 1)*(q*t**4 + q*t**3 + q*t**2 + q*t + q - t**3 - t**2 - t)/q**3,
}

# Factor out (q-1)/q^3 from r=3,4,5
for r in [3, 4, 5]:
    d = sp.simplify(data_c1[r] * q**3 / (q - 1))
    print(f"d_1({r}) = c_1(r) * q^3 / (q-1) = {sp.expand(d)}")
    print(f"       factored = {sp.factor(d)}")
    # As poly in q:
    dp = sp.Poly(sp.expand(d), q)
    print(f"       degree in q = {dp.degree()}")
    for k in range(dp.degree() + 1):
        c = dp.nth(k)
        print(f"          q^{k}: {sp.factor(c)}")
    print()

# Now the "linear in q" pattern: d_1(r) as function of q has degree 1 in q.
# d_1(r) = q * A(r,t) - B(r,t)
# r=3: q · (t^2+1)(t^2+t+1) - t·(t^2+1) = q(t^2+1)[3]_t - t(t^2+1)
# r=4: q · (t^2+1)[5]_t - t·[5]_t
# r=5: q · (t^4+t^2+1)[5]_t - (t^3+t^2+t)(t^4+t^2+1) = q·[6]_t/[2]_t · [5]_t - t[3]_t · [6]_t/[2]_t

# So d_1(r) = q · A(r) · B(r) - t^? · C(r) · D(r)... but let's just look at leading and constant coefficients
