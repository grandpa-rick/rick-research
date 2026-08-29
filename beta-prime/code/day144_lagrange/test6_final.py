"""
Final checks:
1. Explore h(τ) more — perhaps h(τ) has a simple algebraic closed form.
2. Test whether h(τ) = 3 · (some Catalan-like series).
3. Check ratio behavior and 3-adic valuation.
"""
from sympy import Rational, Symbol, Poly, expand, series, sqrt, factor, together
from sympy import symbols, Function, dsolve, integrate

tau = Symbol('tau')
c = [Rational(3), Rational(9), Rational(58,3), Rational(322,9), Rational(1639,27),
     Rational(7879,81), Rational(36376,243)]
h_poly = sum(c[i]*tau**i for i in range(len(c)))
print("h(τ) =", h_poly)

# Test 1: is h(τ) = 3 · f(τ) for some f with integer coefficients?
# f = h/3 = 1 + 3τ + (58/9)τ² + (322/27)τ³ + ...
# Not integer.

# Test 2: is h(τ) algebraic — say h satisfies P(τ, h) = 0 for low-degree polynomial P?
# We have 7 coefficients. Fit polynomial relation.
# Try h² = polynomial(τ)·h + polynomial(τ)?
h2 = expand(h_poly**2)
h2poly = Poly(h2, tau)
print("\nh(τ)² coefficients:")
for k in range(13):
    v = h2poly.nth(k)
    print(f"  [τ^{k}] h² = {v}")

# Try to find (α(τ), β(τ)) with α, β polynomials of low degree such that
# h² = α(τ) h + β(τ)
# Compare coefficients.
# Say α = a0 + a1 τ, β = b0 + b1 τ + b2 τ² + b3 τ³.
# Then coeff [τ^k] h² = sum α_j · c_{k-j} + β_k (if k<= deg β) ...
# We have 7 known c_k. So [τ^k] h² for k=0..12 needs c up to k=6. Actually [τ^k] h² only needs c_0..c_k so k up to 6 is well-defined.
# Set up linear system.

# α: coefficients of degrees 0..d_α, β: 0..d_β
# equations: [τ^k] h² = sum_j a_j c_{k-j} + b_k for k in valid range
# Unknowns: (d_α+1) + (d_β+1)

from sympy import Matrix
def try_algebraic(d_alpha, d_beta):
    """Try h² = α h + β with deg α = d_alpha, deg β = d_beta."""
    N_unk = (d_alpha+1) + (d_beta+1)
    # We have known h² coefficients [τ^0]..[τ^6] (7 equations)
    eqs = []
    N_eq = 7
    if N_eq < N_unk:
        return None, "underdetermined"
    for k in range(N_eq):
        row = []
        # α coefficients: a_j contributes to [τ^k] as a_j · c_{k-j} for j<=k, j<=d_alpha
        for j in range(d_alpha+1):
            if j <= k:
                row.append(c[k-j])
            else:
                row.append(Rational(0))
        # β coefficients: b_k contributes only to [τ^k]
        for j in range(d_beta+1):
            if j == k:
                row.append(Rational(1))
            else:
                row.append(Rational(0))
        eqs.append(row + [h2poly.nth(k)])
    M = Matrix(eqs)
    # Solve
    n_cols = N_unk
    aug = M
    # Row reduce or use solve_linear_system
    from sympy import solve_linear_system, symbols as sym_sym
    xs = sym_sym(f'x0:{N_unk}')
    sol = solve_linear_system(aug, *xs)
    if sol is None:
        return None, "inconsistent"
    return sol, None

print("\n=== Try h² = α(τ)·h + β(τ) for various degrees ===")
for da in range(0, 4):
    for db in range(0, 5):
        sol, err = try_algebraic(da, db)
        if sol is None:
            print(f"  deg α={da}, deg β={db}: {err}")
            continue
        # If exact solution (no free params), check consistency
        if all(v.free_symbols == set() for v in sol.values()):
            print(f"  deg α={da}, deg β={db}: SOLUTION FOUND")
            for k, v in sol.items():
                print(f"    {k} = {v}")

# Also try: h(τ) = polynomial / polynomial
# Let's compute Padé approximants
print("\n=== Padé approximants of h(τ) ===")
from sympy import Poly

def pade(series_coefs, m, n):
    """Compute [m/n] Padé approximant of the series."""
    N = m + n
    if len(series_coefs) < N + 1:
        return None
    # a(τ) numerator degree m, b(τ) denominator degree n, b_0 = 1
    # a(τ) = f(τ) · b(τ) mod τ^{m+n+1}
    # coefficients: a_i = sum_j f_{i-j} b_j
    # unknowns: a_0..a_m, b_1..b_n (b_0 = 1)
    # equations for i = 0..m+n
    from sympy import Matrix, symbols, solve_linear_system
    a_syms = symbols(f'a0:{m+1}')
    b_syms = symbols(f'b1:{n+1}')
    eqs = []
    for i in range(N+1):
        row = [Rational(0)] * (m+1+n)
        # a_i term
        if i <= m:
            row[i] = Rational(1)
        # -sum_j f_{i-j} b_j for j=1..n and i-j >= 0
        for j in range(1, n+1):
            if i-j >= 0:
                row[m+1+j-1] = -series_coefs[i-j]
        # RHS: f_i · b_0 = f_i
        rhs = series_coefs[i] if i < len(series_coefs) else 0
        eqs.append(row + [rhs])
    M = Matrix(eqs)
    sol = solve_linear_system(M, *(a_syms + b_syms))
    return sol

for m in range(0, 4):
    for n in range(0, 4):
        if m+n > 6:
            continue
        sol = pade(c, m, n)
        if sol is None:
            continue
        print(f"[{m}/{n}] Padé:")
        for k, v in sol.items():
            print(f"    {k} = {v}")
