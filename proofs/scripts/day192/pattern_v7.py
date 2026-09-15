"""Continue pattern hunt for c_0.

Divide by different factor. Perhaps the natural leading factor is
   H(r) = [r+1]_t · [r+2]_t / ([2]_t · [3]_t)   [NOT including [r+3]_t].
Then the extra factor [r+3]_t / q^? would appear inside the "linear-in-1/q" combination.

For a=2 case (Day 191):
   c_0(r) = (q-1)/q · ([r+2]_t/[2]_t) · ([r+1]_t - t[r-1]_t/q)
   That is, H^{(a=2)}(r) = [r+2]_t/[2]_t. Then inside is ([r+1]_t - t[r-1]_t/q), a q-Laurent poly of degree 0 to -1.

For a=3:
   Guess c_0(r) = (q-1)/q · H^{(a=3)}(r) · (α(r,t) - β(r,t)/q + γ(r,t)/q^2)
   for some α, β, γ.  Compare to what we have.

   c_0(r) = (q-1)/q^3 · d_0(r) = (q-1)/q · d_0(r)/q^2
   d_0(r)/q^2 = A_2 + A_1/q + A_0/q^2

So the "polynomial" (α - β/q + γ/q^2) = d_0(r)/q^2 = A_2 + A_1/q + A_0/q^2.

Now maybe there's a "double-q-integer" structure. Let's check:
   For a=2 we had: (q-1)/q · ([r+2]_t/[2]_t)·([r+1]_t - t[r-1]_t/q)
   So α = [r+1]_t, β = t[r-1]_t.

Try for a=3:
   (q-1)/q^3 · d_0(r) where d_0 = A_2 q^2 - t A_1' q + t^3 A_0'.
   Equivalently d_0/q^2 = A_2 - t A_1'/q + t^3 A_0'/q^2.
   c_0(r) = (q-1)/q · (A_2 - t A_1'/q + t^3 A_0'/q^2)
   where A_i are the polys we've computed.

We have:
   A_2 = [r+1]·[r+2]·[r+3] / ([2][3])
   -A_1/t = -A_1/t coefficient extracted
   A_0/t^3 = ...

For "cleaner" form, try:
   c_0(r) = (q-1)/q · [r+2]_t · [r+3]_t / ([2]_t · [3]_t) · Big(r, q, t)
where Big(r, q, t) is a polynomial in 1/q.

Compute d_0(r) / ([r+2]_t · [r+3]_t / ([2]_t · [3]_t)):
"""

import sympy as sp

q, t = sp.symbols('q t')


def qint(n):
    if n <= 0:
        return sp.Integer(0)
    return sum(t**i for i in range(n))


data_c0 = {
    3: (q - 1)*(t + 1)*(t**2 - t + 1)*(q**2*t**6 + q**2*t**5 + 2*q**2*t**4 + 2*q**2*t**3 + 2*q**2*t**2 + q**2*t + q**2 - q*t**5 - 2*q*t**4 - 2*q*t**3 - 2*q*t**2 - q*t + t**3)/q**3,
    4: (q - 1)*(t**6 + t**5 + t**4 + t**3 + t**2 + t + 1)*(q**2*t**6 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**5 - q*t**4 - q*t**3 - q*t**2 - q*t + t**3)/q**3,
    5: (q - 1)*(t + 1)*(t**2 + 1)*(t**4 + 1)*(q**2*t**8 + q**2*t**6 + q**2*t**5 + q**2*t**4 + q**2*t**3 + q**2*t**2 + q**2 - q*t**7 - q*t**6 - q*t**5 - 2*q*t**4 - q*t**3 - q*t**2 - q*t + t**5 + t**3)/q**3,
}


print("Dividing d_0(r) by H(r) = [r+2]_t · [r+3]_t / ([2]_t · [3]_t):")
for r in [3, 4, 5]:
    c0 = data_c0[r]
    d = sp.expand(c0 * q**3 / (q - 1))
    H = qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    reduced = sp.simplify(d / H)
    print(f"r={r}: d_0/H = {sp.factor(reduced)}")
    # Show as poly in q
    ratp = sp.Poly(sp.together(reduced), q)
    for k in range(ratp.degree() + 1):
        print(f"    q^{k}: {sp.factor(ratp.nth(k))}")
    print()

print()
print("Dividing d_0(r) by G(r) = [r+1]_t · [r+2]_t · [r+3]_t / ([2]_t · [3]_t):")
for r in [3, 4, 5]:
    c0 = data_c0[r]
    d = sp.expand(c0 * q**3 / (q - 1))
    G = qint(r + 1) * qint(r + 2) * qint(r + 3) / (qint(2) * qint(3))
    reduced = sp.simplify(d / G)
    print(f"r={r}: d_0/G = {sp.factor(reduced)}")
    ratp = sp.Poly(sp.together(reduced), q)
    for k in range(ratp.degree() + 1):
        print(f"    q^{k}: {sp.factor(ratp.nth(k))}")
    print()

# Let me now try yet another form. Perhaps: (q-1)/q^3 · X · (q · P - t · Q · (q · R - t · S))
# I.e., a nested "linear-in-q" structure.
# For a=2: (q[r+1]_t - t[r-1]_t) is linear-in-q.
# For a=3: maybe (q · [r+1]_t · [r+2]_t/[2]_t - t · ??? · (q · ??? - t · ???))
# I.e., d_0(r) = q · [r+2]_t · A - t · B · (q · C - t · D)
# Where [r+2]_t · A = leading factor for c_1 (which is [r+2]_t · [r+1]_t / [2]_t)

# c_1 formula was: c_1(r) = (q-1)/(q^3 [2]_t) · [r+1]_t · (q [r]_t - t [r-2]_t)
# So c_1 has factor [r+1]_t.

# Recursion? Suppose c_0(r) satisfies c_0(r) = something · c_0(r-1) + something · c_1(r).
# Or: c_0(r) = (leading factor) · [linear in q form similar to c_1].

# Try: d_0(r) = f(r,t) · (q · [r+1]_t · [r+2]_t / [2]_t · [something] - t · [something] · (q · [r]_t · [r-2]_t · [??] - t · [??]))

# Actually, the cleanest test: does d_0(r) - (q · [r+3]_t · [something] - t · [some other stuff]) work?
# Let me try: d_0(r) = q · G_upper - t^? · G_lower where G_upper is deg 2 in q.

# Actually the "natural" form based on Day 191 pattern:
#   d_0(r) = (q · A(r) - t · B(r)/q) · C(r) + ...  (multi-linear in 1/q)
#
# Since d_0(r) is degree 2 in q, we can factor over Q(t)[q] as (q-α)(q-β) times constant. Let me check if factors are nice:
print()
print("Roots of d_0(r) as poly in q:")
for r in [3, 4, 5]:
    c0 = data_c0[r]
    d = sp.expand(c0 * q**3 / (q - 1))
    dp = sp.Poly(d, q)
    A2, A1, A0 = dp.nth(2), dp.nth(1), dp.nth(0)
    # roots by quadratic formula: q = (-A1 ± sqrt(A1^2 - 4 A0 A2))/(2 A2)
    disc = sp.expand(A1**2 - 4 * A0 * A2)
    print(f"r={r}: discriminant = {sp.factor(disc)}")
    sq = sp.sqrt(disc)
    print(f"   sqrt(disc) = {sp.simplify(sq)}")
