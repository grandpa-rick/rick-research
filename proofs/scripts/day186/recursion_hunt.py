#!/usr/bin/env python3
"""
Day 186: Look for a recursion X_{P_n}(q) in the h-basis. We have computed
X_{P_n}(q) for n = 1..4 in h-basis. Now:

1. Rewrite X_{P_n} in the "h_1, h_2, ..." polynomial ring, treating h_1, h_2, ...
   as commuting indeterminates (they are algebraically independent).
2. Try ansatz X_{P_n} = A(q) h_1 X_{P_{n-1}} + B(q) h_2 X_{P_{n-2}} + ...
   and see if it fits for n = 3, 4.

For a bonus, compute at t via the Hikita (q,t) interpretation:
X_{P_n}(q,t) = sum_lam c_lam(t) e_lam^{(q,t)} where c_lam(t) are Ellzey-Wachs
coefficients (obtained by q -> t in our X_{P_n}(q)).

But the h-basis expansion depends on the choice of basis. In the ordinary
Λ ring, h and e are related by e_r = det(h_{1-i+j})_{i,j=1..r}. So under
q=1, h-basis conversion is standard. For (q,t) we'd need a "(q,t) h-basis"
which is not standard — Hikita gives e^{(q,t)} but no h^{(q,t)}.

So really the (q,t) redirect via the h-basis boils down to: does X_{P_n}(q)
(one-parameter, Ellzey-Wachs) exhibit a clean h-basis recursion?
"""

from sympy import symbols, expand, simplify, factor, Rational, Integer, Poly, together, cancel, Matrix, zeros
from sympy import solve, Symbol, groebner, S

q = symbols('q')
t = symbols('t')

# From chromatic_qt_path.py output (verified):
# n=1: X_{P_1} = h_1
# n=2: X_{P_2} = -(q+1) h_2 + (q+1) h_11
#      = (q+1)*(h_1^2 - h_2)
# n=3: X_{P_3} = (q^2+q+1) h_3 - (2q^2+3q+2) h_21 + (q+1)^2 h_111
# n=4: X_{P_4} = -(q+1)(q^2+1) h_4 + (q+1)(2q^2+q+2) h_31 + (q+1)(q^2+q+1) h_22
#              - (q+1)(3q^2+4q+3) h_211 + (q+1)^3 h_1111

# Treat h1, h2, h3, h4, h5 as commuting indeterminates.
h1, h2, h3, h4, h5 = symbols('h1 h2 h3 h4 h5', commutative=True)

X = {}
X[1] = h1
X[2] = (q + 1) * h1**2 - (q + 1) * h2
X[3] = (q**2 + q + 1) * h3 - (2*q**2 + 3*q + 2) * h2 * h1 + (q + 1)**2 * h1**3
X[4] = -(q + 1)*(q**2 + 1) * h4 + (q + 1)*(2*q**2 + q + 2) * h3 * h1 \
       + (q + 1)*(q**2 + q + 1) * h2**2 \
       - (q + 1)*(3*q**2 + 4*q + 3) * h2 * h1**2 \
       + (q + 1)**3 * h1**4

print("=== X_{P_n}(q) in h-basis (h_i commuting) ===")
for n in range(1, 5):
    print(f"X_{n} = {expand(X[n])}")

print()
print("=== Try recursion ansatz A ===")
print("Ansatz: X_n = A(q) * h1 * X_{n-1} + B(q) * h2 * X_{n-2}   (naive)")
# n = 3:  X_3 =? A * h1 * X_2 + B * h2 * X_1
#        h1 * X_2 = (q+1)*h_1^3 - (q+1)*h_2 h_1
#        h2 * X_1 = h2 h1
# so     A*(q+1) = (q+1)^2  ==> A = q+1  (from h_1^3 coeff)
# check h2 h1 coeff on RHS: -A*(q+1) + B = -(q+1)^2 + B, and LHS coeff = -(2q^2+3q+2)
#   ==> B = -(2q^2+3q+2) + (q+1)^2 = -(2q^2+3q+2) + q^2 + 2q + 1 = -q^2 - q - 1 = -(q^2+q+1)
# check h_3 coeff on RHS: 0 (RHS has no h_3), LHS = q^2+q+1
# CONTRADICTION unless we add a C(q)*h3 term.

# Extended ansatz:
# X_n = A(q) * h1 * X_{n-1} + B(q) * h2 * X_{n-2} + C(q) * h_n  (n>=1, X_0=1)
# For n=3:
#   RHS = A*h1*X_2 + B*h2*X_1 + C*h3
#       = A*(q+1)*(h1^3 - h2 h1) + B*h2 h1 + C*h3
#   LHS h1^3 coeff: (q+1)^2 => A(q+1) = (q+1)^2 => A = q+1
#   LHS h2 h1 coeff: -(2q^2+3q+2) => -A(q+1) + B = -(q+1)^2 + B; solve: B = -(2q^2+3q+2)+(q+1)^2 = -q^2-q-1
#   LHS h3 coeff: q^2+q+1 => C = q^2+q+1

# So for n = 3: A = q+1, B = -(q^2+q+1), C = q^2+q+1.
# Now test n = 4 with same A, B, C(q) parameters (C now applies to h4).

# n=4: RHS_4 = A*h1*X_3 + B*h2*X_2 + C4*h4  (allow C_n to depend on n)

def coeff_of(f, mon_tuple):
    """Get coefficient of monomial h1^a1 h2^a2 h3^a3 h4^a4 (h5^a5) in f."""
    a1, a2, a3, a4 = mon_tuple[:4]
    a5 = mon_tuple[4] if len(mon_tuple) > 4 else 0
    p = Poly(expand(f), h1, h2, h3, h4, h5)
    return p.coeff_monomial((a1, a2, a3, a4, a5))

# Solve for A_n, B_n, C_n at each n:
def solve_recursion_naive(n_max=4):
    """
    X_n = A_n * h1 * X_{n-1} + B_n * h2 * X_{n-2} + C_n * h_n + ... (leftover)
    For each n, fit A_n, B_n, C_n and compute residual.
    """
    X0 = Integer(1)
    X_full = {0: X0, 1: X[1], 2: X[2], 3: X[3], 4: X[4]}
    results = []
    for n in range(2, n_max + 1):
        A, B, C = symbols(f'A_{n} B_{n} C_{n}')
        h_n = {1: h1, 2: h2, 3: h3, 4: h4, 5: h5}[n]
        rhs = A * h1 * X_full[n-1] + (B * h2 * X_full[n-2] if n >= 2 else 0) + C * h_n
        diff = expand(X_full[n] - rhs)
        # Extract all coefficients of monomials in h1,...,h5:
        p_diff = Poly(diff, h1, h2, h3, h4, h5)
        eqs = list(p_diff.as_dict().values())
        # These must all vanish. Solve for A, B, C:
        sol = solve(eqs, [A, B, C], dict=True)
        if sol:
            s = sol[0]
            print(f"n={n}: A={factor(s.get(A, 'free'))}, B={factor(s.get(B, 'free'))}, C={factor(s.get(C, 'free'))}")
            # substitute back and check residual
            res = expand(diff.subs(s))
            print(f"      residual = {expand(res)}")
        else:
            print(f"n={n}: no solution to naive 3-term recursion")
            # find best-fit by solving linear system over the coefficient monomials
            # Try leaving out constraints on higher monomials
            print(f"      diff (unsolved) = {expand(diff)}")
        results.append(sol)
    return results

print("=== Fitting naive 3-term recursion X_n = A h1 X_{n-1} + B h2 X_{n-2} + C h_n ===")
solve_recursion_naive(4)


print()
print("=== Alternative ansatz: X_n = alpha h1 X_{n-1} + beta h_1^2 X_{n-2} + ... ===")
# Try: X_n = alpha(q) * h1 * X_{n-1} + beta(q) * (h_2 - h_1^2/2 or something) * X_{n-2}
# Look at the pattern of e-basis coefficients (which is what Hikita's theory
# actually gives natively):
print("e-basis coefficients c_lambda(q) for X_{P_n}(q):")
e_coefs = {
    1: {(1,): 1},
    2: {(2,): q + 1},
    3: {(2, 1): q, (3,): q**2 + q + 1},
    4: {(2, 2): q * (q + 1), (3, 1): q * (q + 1), (4,): (q + 1) * (q**2 + 1)},
}
for n, d in e_coefs.items():
    print(f"  n={n}: {d}")

# Look at natural pattern for c_{(n)}(q):
print()
print("c_{(n)}(q) = leading e-basis coefficient (of e_n):")
for n in range(1, 5):
    key = (n,)
    if key in e_coefs[n]:
        print(f"  n={n}: c_(n) = {factor(e_coefs[n][key])}")
# n=1: 1
# n=2: q+1 = [2]_q
# n=3: q^2+q+1 = [3]_q
# n=4: (q+1)(q^2+1) = ... = 1+q+q^2+q^3 = [4]_q
# So c_{(n)}(q) = [n]_q for path graph! (Ellzey-Wachs classical result.)

print()
print("=== Note: c_{(n)}(q) = [n]_q for path graph. ===")

# Now check h-basis GF ansatz:
# Define Z(z) = sum_{n>=1} X_{P_n}(q) z^n  (formal, ignoring convergence)
# Look for algebraic equation.
# At q=1: X_{P_n}(1) is the usual chromatic symmetric function, and there
# should be Rick's Theorem B (Day 170) giving an algebraic GF.

print()
print("=== Test q=1 case (classical chromatic sym fn) ===")
for n in range(1, 5):
    print(f"  n={n}: X_{{P_{n}}}(1) in h-basis:")
    Xn_at_1 = X[n].subs(q, 1)
    print(f"    {expand(Xn_at_1)}")

# Standard Stanley-Stembridge: X_{P_n}(1) = h_n + ... nice h-positive?
# Actually X_{P_n} at q=1 is the classical CSF. Its h-basis expansion has
# NEGATIVE coefficients (it's e-positive, not h-positive in general).
