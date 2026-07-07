"""Test hypothesis: H_c(a,b,j) = (shortened run product) × G_j^(c)(a,b),
where G_j^(c) is a "small" polynomial in (a,b) of bounded degree.

Rick's review file mentions:
    G_4^(c) = H_c(a,b,4) / [ ∏_{s=3}^{c−3}(a+s) · ∏_{s=2}^{c−4}(b+s) ]

So the shortened run at j=4 is [3..c-3] in a (c-5 factors) and [2..c-4] in b (c-5 factors).
That's (c-1) - 4 = c-5 factors. So pattern: at level j, drop j top factors from each run.

Full: at level j, a-run is [3..c+1-j] and b-run is [2..c-j]. Both have (c-1-j) factors.

Test this with H_5.
"""
import sympy as sp

a, b, j = sp.symbols('a b j', integer=True)


def C_sym(n, k):
    """Binomial coefficient as a symbolic polynomial in n."""
    if k < 0:
        return sp.Integer(0)
    if k == 0:
        return sp.Integer(1)
    p = sp.Integer(1)
    for i in range(k):
        p *= (n - i)
    return p / sp.factorial(k)


def H5_sym(a, b, j):
    h0 = (a+3)*(a+4)*(a+5)*(a+6)*(b+2)*(b+3)*(b+4)*(b+5)
    h1 = -20*(a+3)*(a+4)*(a+5)*(b+2)*(b+3)*(b+4)
    h2 = -10*(a+3)*(a+4)*(b+2)*(b+3)*(a*b + a + 2*b - 22)
    h3 = 360*(a+3)*(b+2)*(a*b + a + 2*b - 2)
    h4 = 240*(a*a*b*b + a*a*b + 3*a*b*b - 15*a*b - 18*a + 2*b*b - 34*b - 24)
    h5 = -7200*(a*b + b - 2)
    h6 = -7200*(a*b - a - 6)
    h7 = 100800
    h8 = 201600
    hs = [h0, h1, h2, h3, h4, h5, h6, h7, h8]
    return sum(hs[k] * C_sym(j, k) for k in range(9))


# For each j, compute H_5(a,b,j), factor out the shortened run product, get G_j
print("=" * 70)
print("Test: H_5(a,b,j) = [∏_{t=3..6-j}(a+t) · ∏_{s=2..5-j}(b+s)] · G_j^(5)")
print("=" * 70)

for j_val in range(0, 5):  # j <= c-1 = 4
    # Shortened run product
    run_a = sp.Integer(1)
    for t in range(3, 7 - j_val):
        run_a *= (a + t)
    run_b = sp.Integer(1)
    for s in range(2, 6 - j_val):
        run_b *= (b + s)
    shortened = run_a * run_b

    Hj = sp.expand(H5_sym(a, b, j_val))

    if shortened == 1:
        Gj_ratio = Hj
    else:
        Gj_ratio = sp.simplify(Hj / shortened)

    print(f"\nj={j_val}:")
    print(f"  shortened runs = {shortened}")
    print(f"  H_5(a,b,{j_val}) / shortened = {sp.expand(Gj_ratio)}")
    # Check if it's a polynomial
    Gj_poly, r = sp.div(Hj, shortened, a, b)
    print(f"  div check: quotient = {sp.expand(Gj_poly)}")
    print(f"             remainder = {sp.expand(r)}")


# Also test at j = c-1 = 4 (both runs empty), G_4 = H_5(a,b,4)
print("\n=== At j=c-1 (empty runs): G_{c-1} = H_c(a,b,c-1) ===")
print(f"H_5(a,b,4) = {sp.expand(H5_sym(a, b, 4))}")


# At j = 5, 6, ..., 8 — runs would have negative length; G_j should carry all
print("\n=== j > c-1 (would-be-empty runs): H_5 fully in G_j ===")
for j_val in range(5, 9):
    Hj = sp.expand(H5_sym(a, b, j_val))
    print(f"H_5(a,b,{j_val}) = {Hj}")
