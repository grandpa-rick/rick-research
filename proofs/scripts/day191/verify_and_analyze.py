"""Day 191 PROVE: verify e_2 * e_2 formula and analyze structure.

From m=4 direct computation:
  e_2 * e_2 = (q-1)(1+t^2)(q*t^2 + q*t + q - t)/q^2 * e_4
            + (q-1)(1+t)/q^2 * e_{3,1}
            + 1/q^2 * e_{2,2}

Simplify:
  coeff(e_{2,2}) = 1/q^2 = (q^{-1})^2
  coeff(e_{3,1}) = (q-1)(1+t)/q^2 = q^{-1} (1 - q^{-1}) [2]_t
  coeff(e_4)    = (q-1)(1+t^2)(q(1+t+t^2) - t)/q^2

Rewrite:
  coeff(e_4) = q^{-1} (1 - q^{-1}) (1+t^2) [q [3]_t - t]
             = (1 - q^{-1})(1+t^2)([3]_t - t/q)
             ... but note: q [3]_t - t = q(1+t+t^2) - t = q + t(q-1) + qt^2
                                       = q(1+t^2) + t(q-1)

Also, (1+t^2)*[3]_t = (1+t^2)(1+t+t^2) = 1 + t + t^2 + t^2 + t^3 + t^4
                    = 1 + t + 2t^2 + t^3 + t^4
Hmm not obviously a symmetric-function pattern.

Also: is there a nicer form?
  (q-1)*(qt^2 + qt + q - t)
  Let me expand:  q^2 t^2 + q^2 t + q^2 - qt - qt^2 - qt - q + t
                = q^2(1+t+t^2) - q(2t + t^2 + 1) + t
                = q^2 [3]_t - q(1 + 2t + t^2) + t
                = q^2 [3]_t - q(1+t)^2 + t
  Or: q^2 [3]_t - q [2]_t^2 + t
So coeff(e_4) = (1+t^2) * (q^2 [3]_t - q [2]_t^2 + t) / q^2
              = (1+t^2) * ([3]_t - [2]_t^2/q + t/q^2)
Hmm let's check by expansion: q^2[3]_t = q^2 + q^2 t + q^2 t^2. Divided by q^2: [3]_t. Yes.
And -q[2]_t^2/q^2 = -[2]_t^2/q = -(1+2t+t^2)/q. And t/q^2.
So (1+t^2)([3]_t - [2]_t^2/q + t/q^2). Let me verify numerically at q=1,t=1:
  [3]_t=3, [2]_t^2=4, so [3]_t - [2]_t^2/q + t/q^2 = 3 - 4 + 1 = 0.
And (1+t^2)|_{t=1} = 2, so total = 0.  Good, at q=1 the whole thing vanishes.

Also, let me check: at q=1, we expect e_2 * e_2 = e_2 * e_2 (ordinary) = e_{2,2}.
So coeffs at q=1: e_4 -> 0, e_{3,1} -> 0, e_{2,2} -> 1.
  coeff(e_4)|_{q=1} = 0 * (...) / 1 = 0. Check.
  coeff(e_{3,1})|_{q=1} = 0 * 2 / 1 = 0. Check.
  coeff(e_{2,2})|_{q=1} = 1. Check!
"""

import sympy as sp

q, t = sp.symbols('q t')


def check_q_equals_1():
    """At q=1, e_2 * e_2 should equal e_2 * e_2 (ordinary) = e_{2,2}."""
    coeff_e4 = (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**2
    coeff_e31 = (q - 1)*(t + 1)/q**2
    coeff_e22 = 1/q**2
    print("At q=1:")
    print(f"  e_4 coeff: {sp.simplify(coeff_e4.subs(q, 1))}")
    print(f"  e_{{3,1}} coeff: {sp.simplify(coeff_e31.subs(q, 1))}")
    print(f"  e_{{2,2}} coeff: {sp.simplify(coeff_e22.subs(q, 1))}")
    print("Expected: 0, 0, 1  (since e_2 * e_2 = e_{2,2} at q=1)")


def check_q_infinity():
    """As q -> infty, in Hikita Thm C, X_Gamma(q,t) -> t^{...} [n]_t! e_n(X).

       For e_a * e_b: as q -> infty (holding e_a, e_b fixed as elements of Lambda_{q,t}),
       what should happen?  The Y_i's essentially become... hmm, this is more subtle.
       Skip for now.
    """
    coeff_e4 = (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**2
    coeff_e31 = (q - 1)*(t + 1)/q**2
    coeff_e22 = 1/q**2
    # Take q -> infty means q^{-1} -> 0. Leading behavior:
    # coeff(e_4) = q^{-1} (1 - q^{-1})(1+t^2)(q [3]_t - t)
    #            ~ (1)(1+t^2) [3]_t  as q -> infty
    lim_e4 = sp.limit(coeff_e4, q, sp.oo)
    lim_e31 = sp.limit(coeff_e31, q, sp.oo)
    lim_e22 = sp.limit(coeff_e22, q, sp.oo)
    print("\nAs q -> infinity:")
    print(f"  e_4 coeff: {lim_e4}   -- should be (1+t^2)[3]_t = 1+t+2t^2+t^3+t^4")
    print(f"  e_{{3,1}} coeff: {lim_e31}")
    print(f"  e_{{2,2}} coeff: {lim_e22}")


def check_t_zero():
    """At t=0, [n]_t = 1, so if the formula has a nice t=0 specialization, we get..."""
    coeff_e4 = (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**2
    coeff_e31 = (q - 1)*(t + 1)/q**2
    coeff_e22 = 1/q**2
    print("\nAt t=0:")
    print(f"  e_4 coeff: {sp.simplify(coeff_e4.subs(t, 0))}")
    print(f"  e_{{3,1}} coeff: {sp.simplify(coeff_e31.subs(t, 0))}")
    print(f"  e_{{2,2}} coeff: {sp.simplify(coeff_e22.subs(t, 0))}")


def analyze_structure():
    """Try to write the coefficients in a Pieri-like closed form.

       Guess: e_a * e_b = q^{-b(a-b+???)/...} ??? -- probably not that simple.

       Think about it as:  each of e_a, e_b costs a q^{-1} factor via q^{-1}_m.
       The "diagonal" term e_{a,b} = e_a e_b has coefficient q^{-2} (product of q^{-1}).

       Then Pieri-type expansions push weight up.
    """
    print("\n=== Structure Analysis ===")
    print("Coefficient of e_{2,2}: 1/q^2 = q^{-2}")
    print("  (matches product of q^{-1} factors: (q^{-1} in e_2) * (q^{-1} in e_2))")

    print("\nCoefficient of e_{3,1}: (q-1)(1+t)/q^2 = (1-q^{-1})[2]_t / q")
    print("  Compare Thm 3.12 for e_1*e_r: (1-q^{-1})[r+1]_t e_{r+1} + q^{-1} e_1 e_r")
    print("  Idea: e_{3,1} arises from 'moving' one box from e_2 to make e_3, times the other e_1")
    print("  Coefficient shape: (1-q^{-1}) * [2]_t (like Thm 3.12 with r=1) times 1/q")
    print("  So: coeff = (1-q^{-1})[2]_t * q^{-1}  <- the second q^{-1} is from the remaining e_1")

    print("\nCoefficient of e_4:")
    c = (q - 1)*(t**2 + 1)*(q*t**2 + q*t + q - t)/q**2
    print(f"  As-is: {c}")
    # Try to factor:
    print(f"  Numerator: {sp.expand((q-1)*(t**2+1)*(q*t**2 + q*t + q - t))}")
    # Consider: (q-1)(qt^2+qt+q-t) = q^2[3]_t - q(1+t)^2 + t
    e = sp.expand((q-1)*(q*t**2 + q*t + q - t))
    print(f"  (q-1)(qt^2+qt+q-t) = {e}")
    # This looks like q^2 [3]_t - q(1+t)^2 + t
    expected1 = q**2 * (1 + t + t**2) - q*(1+t)**2 + t
    print(f"  q^2[3]_t - q[2]_t^2 + t = {sp.expand(expected1)}, diff: {sp.simplify(e - expected1)}")
    # so numerator = (1+t^2)(q^2 [3]_t - q [2]_t^2 + t)
    # We can write:
    # coeff(e_4) = (1+t^2) * (q^2[3]_t - q[2]_t^2 + t) / q^2
    #            = (1+t^2) * ([3]_t - [2]_t^2/q + t/q^2)
    print()
    print("Candidate closed forms for coeff(e_4):")
    print("  (1+t^2) * ([3]_t - [2]_t^2/q + t/q^2)")
    print("  = (1+t^2) * ([3]_t - (1+t)^2/q + t/q^2)")

    # Alternative:  (1-q^{-1})^2 * something + linear in (1-q^{-1}) * something
    # We know at q=1, coeff(e_4) = 0.
    # Expand around q=1:
    print("\n  Coefficient of (q-1) around q=1:")
    dc = sp.diff(c, q).subs(q, 1)
    print(f"    d/dq at q=1: {sp.simplify(dc)}")
    # this is the coefficient of (q-1) in the Taylor expansion of c(q,t) around q=1
    # so at leading order, coeff(e_4) ~ (q-1) * dc/dq|_{q=1}
    #                                = (q-1) * (?)

    # More useful: rewrite in terms of q^{-1}. Let u = q^{-1}. Then q = 1/u.
    u = sp.Symbol('u')
    c_u = c.subs(q, 1/u)
    c_u_s = sp.simplify(sp.expand(c_u))
    print(f"\n  In terms of u = q^{{-1}}: {sp.expand(c_u_s)}")
    print(f"  Factored: {sp.factor(c_u_s)}")

    # Let me try yet another form:
    # coeff(e_4) = (q-1)(1+t^2)(q(1+t+t^2) - t)/q^2
    # Note q(1+t+t^2) - t = q + q*t + q*t^2 - t = q + t(q-1) + q*t^2
    # Or:  q*[3]_t - t.  With q -> 1: [3]_t - t = 1 + t^2.
    # So (q-1)(1+t^2)(q[3]_t - t)/q^2, and at q=1 this becomes 0*(1+t^2)*(1+t^2)/1 = 0.
    # As q -> infty: ~ (q)(1+t^2)(q[3]_t)/q^2 = (1+t^2)[3]_t.

    # Try yet another rewrite:
    # (q-1)(q[3]_t - t)/q^2
    # = (q-1)[3]_t/q - (q-1)*t/q^2
    # = (1 - q^{-1})[3]_t - (1 - q^{-1})*t/q
    # = (1 - q^{-1})([3]_t - t/q)
    # = (1 - q^{-1})*[3]_t - (1 - q^{-1})*t*q^{-1}
    a = sp.expand((1 - 1/q)*(1+t+t**2) - (1 - 1/q)*t/q)
    b = sp.expand((q-1)*(q*t**2 + q*t + q - t)/q**2)
    print(f"\n  Verify (1-q^-1)*[3]_t - (1-q^-1)*t/q = (q-1)(qt^2+qt+q-t)/q^2:  {sp.simplify(a-b)}")

    # So the whole coefficient of e_4 is:
    # (1+t^2) * (1 - q^{-1}) * ([3]_t - t/q)
    a2 = sp.expand((1+t**2) * (1 - 1/q) * ((1+t+t**2) - t/q))
    print(f"  Verify (1+t^2)(1-q^-1)([3]_t - t/q) = c(e_4):  {sp.simplify(a2 - c)}")

    # Can we combine (1+t^2)([3]_t) - (1+t^2)*t/q  into something recognizable?
    # (1+t^2)*[3]_t = (1+t^2)(1+t+t^2) = 1+t+2t^2+t^3+t^4
    # Alternative: [3]_t * [3]_{-t} = (1+t+t^2)(1-t+t^2) = 1+t^2+t^4
    # So (1+t^2)[3]_t != any obvious [n]_t style.
    # BUT: (1+t)*(1+t^2)*... = t-integers for various things.
    # (1+t^2)(1+t+t^2) = 1+t+2t^2+t^3+t^4 -- not obviously symmetric in t/1.
    # Try [4]_t * [2]_t?  [4]_t = 1+t+t^2+t^3, [2]_t = 1+t.
    #  = (1+t)(1+t+t^2+t^3) = 1+t+t^2+t^3+t+t^2+t^3+t^4 = 1+2t+2t^2+2t^3+t^4  -- no.
    # Try [5]_t*[3]_t/[some] ?  Hmm.

    # I'll leave this in the form (1+t^2)(1-q^{-1})([3]_t - t/q)


def main():
    check_q_equals_1()
    check_q_infinity()
    check_t_zero()
    analyze_structure()


if __name__ == "__main__":
    main()
