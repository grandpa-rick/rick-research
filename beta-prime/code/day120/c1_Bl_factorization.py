"""Check the claim A_l(t) := [y]_{2l+2}|_{y+c=j, yc=t} = prod_{k=0}^l (t - k(j-k))."""
import sympy as sp
from sympy import symbols, expand, Poly, Integer, Rational

y, t = symbols('y t')

def check(l_val):
    j = 2*l_val + 1
    # A(y) = [y]_{2l+2} as polynomial in y
    A_of_y = Integer(1)
    for i in range(2*l_val + 2):
        A_of_y *= (y - i)
    A_of_y = expand(A_of_y)
    # Reduce mod y^2 - j*y + t (i.e., substitute y^2 -> j*y - t)
    # This is equivalent to polynomial division
    Ay_poly = Poly(A_of_y, y)
    divisor = Poly(y**2 - j*y + t, y)
    q, r = sp.div(Ay_poly, divisor)
    # r has degree < 2 in y, so r = alpha(t) + beta(t) * y
    r_expr = r.as_expr()
    # Since A(y) = A(c) (proved), r should have y-degree 0
    r_poly_y = Poly(r_expr, y)
    print(f"l={l_val}: A_l(t) reduced to: {r_expr}")
    # Check: is r independent of y?
    coeffs = r_poly_y.all_coeffs()
    print(f"  y-degree of r: {r_poly_y.degree()}")
    # Claim: r = prod_{k=0}^l (t - k(j-k))
    prod = Integer(1)
    for k in range(l_val + 1):
        prod *= (t - k*(j - k))
    prod = expand(prod)
    print(f"  Predicted: {prod}")
    print(f"  Match: {expand(r_expr - prod) == 0}")

for l_val in range(1, 5):
    check(l_val)
    print()
