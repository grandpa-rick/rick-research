"""
TEST 2: Lagrange inversion ansatz b_k = (1/k) [τ^{k-1}] h(τ)^k.
Fit c_0, ..., c_6.

Also: compute compositional inverse G of F to order 7.
"""
from sympy import Rational, Symbol, symbols, Poly, expand, series, solve, Matrix, factor

tau = Symbol('tau')

b = [0, 3, 27, 417, 7851, 164124, 3661389, 85384566]

# Fit c_0..c_6 iteratively.
# h(τ) = c_0 + c_1 τ + ... + c_6 τ^6
c = [Symbol(f'c{i}') for i in range(7)]
h = sum(c[i] * tau**i for i in range(7))

# Compute h^k and read coefficient [τ^{k-1}] / k, set equal to b_k.
# Solve incrementally.
values = {}

# k=1: b_1 = c_0
values[c[0]] = Rational(b[1])
print(f"c_0 = {values[c[0]]}")

for k in range(2, 8):
    # h with previously found c substituted, plus c_{k-1} unknown
    h_sub = h.subs(values)
    hk = expand(h_sub**k)
    hk_poly = Poly(hk, tau)
    coef = hk_poly.nth(k-1)
    # equation: coef / k = b_k
    eq = coef - k * b[k]
    # solve for c_{k-1}
    sol = solve(eq, c[k-1])
    if len(sol) != 1:
        print(f"Warning: solving for c_{k-1} gave {len(sol)} solutions: {sol}")
    values[c[k-1]] = sol[0]
    print(f"c_{k-1} = {values[c[k-1]]}  = {float(values[c[k-1]]):.6f}")

print("\nFinal c values (rational):")
for i in range(7):
    v = values[c[i]]
    print(f"  c_{i} = {v}")

print("\nAs decimals:")
for i in range(7):
    v = values[c[i]]
    print(f"  c_{i} ≈ {float(v):.10f}")

# Also compute compositional inverse of F(τ) to see if there's a nice form.
# F(τ) = sum b_k τ^k. Its compositional inverse G(x) satisfies F(G(x)) = x.
# Write G(x) = g_1 x + g_2 x^2 + ... solve iteratively.
print("\n--- Compositional inverse G of F ---")
x = Symbol('x')
N = 7
F_poly_expr = sum(Rational(b[k]) * tau**k for k in range(1, N+1))

# G(x) = sum g_k x^k with g_0 = 0
g = [Rational(0)] + [Symbol(f'g{i}') for i in range(1, N+1)]

# F(G(x)) = x means sum_k b_k G(x)^k = x
# Solve iteratively.
g_vals = {}
# g_1: F(G(x))|_{x^1} = b_1 · g_1 = 1 → g_1 = 1/b_1 = 1/3
g_vals[g[1]] = Rational(1, 3)
print(f"g_1 = {g_vals[g[1]]}")

for order in range(2, N+1):
    # Substitute known g values into G
    G_sub = sum((g_vals.get(g[i], g[i]) if isinstance(g[i], Symbol) else g[i]) * x**i for i in range(1, N+1))
    # Compute F(G(x)) up to order `order`
    FG = sum(Rational(b[k]) * G_sub**k for k in range(1, N+1))
    FG_expanded = expand(FG)
    FG_poly = Poly(FG_expanded, x)
    coef = FG_poly.nth(order)
    # Equation: coef = 0 (for order > 1) or 1 (for order 1)
    rhs = 1 if order == 1 else 0
    eq = coef - rhs
    sol = solve(eq, g[order])
    if len(sol) != 1:
        print(f"Warning at order {order}: {sol}")
    g_vals[g[order]] = sol[0]
    print(f"g_{order} = {g_vals[g[order]]}")

print("\nCompositional inverse G(x) coefficients:")
for i in range(1, N+1):
    v = g_vals[g[i]]
    print(f"  g_{i} = {v}")
