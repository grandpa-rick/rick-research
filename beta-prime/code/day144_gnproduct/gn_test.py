"""
Test whether Das-Pattanayak GN product at N=1 matches Rick's F(tau).

GN product (Prop 2.3, eq 2.17):
  1 - sum_{r>=1} HC(c_{2r-1}) z^r  =  prod_{i=1}^N (1 - z*lam_i*(lam_i+1)) / (1 - z*lam_i*(lam_i-1))

At N=1:
  1 - G(z, lam)  =  (1 - z*lam*(lam+1)) / (1 - z*lam*(lam-1))
where G(z,lam) = sum_{r>=1} HC(c_{2r-1}) z^r.

So G(z, lam) = 1 - (1 - z*lam*(lam+1))/(1 - z*lam*(lam-1))
             = [ (1 - z*lam*(lam-1)) - (1 - z*lam*(lam+1)) ] / (1 - z*lam*(lam-1))
             = [ z*lam*(lam+1) - z*lam*(lam-1) ] / (1 - z*lam*(lam-1))
             = 2*z*lam / (1 - z*lam*(lam-1))

Rick's F(tau) = 3*tau + 27*tau^2 + 417*tau^3 + 7851*tau^4 + 164124*tau^5 + 3661389*tau^6 + 85384566*tau^7 + ...

Try to find (z, lam) as function of tau so G(z, lam) = F(tau).

Options:
(A) z = tau, lam = constant. Then G = 2*lam*tau/(1 - lam*(lam-1)*tau) is a rational function
    with coefficients [2*lam, 2*lam*lam*(lam-1), 2*lam*(lam*(lam-1))^2, ...]
    -> geometric progression. F is not.
(B) z = tau, lam = f(tau) power series.
    Match coefficients.
(C) z, lam both functions of tau.
"""

from sympy import symbols, series, Rational, sqrt, simplify, expand, Poly, solve, Symbol, S, Function, Matrix
from sympy import Poly, groebner
import sympy as sp

tau = symbols('tau')

# Rick's F(tau)
F_coeffs = [0, 3, 27, 417, 7851, 164124, 3661389, 85384566]
# Rick's A(tau)
A_coeffs = [0, -3, -18, -255, -4620, -94500, -2078802, -48005802]

N_terms = 8

F = sum(F_coeffs[k]*tau**k for k in range(N_terms))
A = sum(A_coeffs[k]*tau**k for k in range(N_terms))

# Sanity: verify (1-2F)^2 = 1+4A mod tau^N
lhs = expand((1 - 2*F)**2)
rhs = expand(1 + 4*A)
diff = expand(lhs - rhs)
# truncate to N-1 terms
diff_trunc = sum(diff.coeff(tau, k)*tau**k for k in range(N_terms))
print("Sanity (1-2F)^2 - (1+4A) mod tau^8 =", diff_trunc)

# ---------- (A) z=tau, lam=constant ----------
print("\n=== Option A: z=tau, lam=constant ===")
lam = symbols('lam')
# G = 2*z*lam / (1 - z*lam*(lam-1))
# expand in tau
G_A = 2*tau*lam / (1 - tau*lam*(lam-1))
G_A_series = sp.series(G_A, tau, 0, N_terms).removeO()
G_A_series = expand(G_A_series)
print("G(tau, lam) =", G_A_series)
# coefficient of tau^1 should equal 3 --> 2*lam = 3 --> lam = 3/2
# coefficient of tau^2 should equal 27 --> 2*lam*lam*(lam-1) = 27
# With lam = 3/2: 2*(3/2)*(3/2)*(1/2) = 9/4  != 27. So no constant lam works.
sol = solve(G_A_series.coeff(tau, 1) - 3, lam)
print("From coeff tau^1: lam =", sol)
for s in sol:
    print(f"  With lam={s}: coeff tau^2 = {G_A_series.coeff(tau,2).subs(lam, s)} (want 27)")

# ---------- (B) z=tau, lam = lam0 + lam1*tau + lam2*tau^2 + ... ----------
print("\n=== Option B: z=tau, lam = power series ===")
lam_syms = symbols('l0 l1 l2 l3 l4 l5 l6 l7')
lam_ser = sum(lam_syms[k]*tau**k for k in range(N_terms))

# G = 2*tau*lam / (1 - tau*lam*(lam-1))
# Compute as series in tau
denom = 1 - tau*lam_ser*(lam_ser - 1)
numer = 2*tau*lam_ser
# Series expansion
G_B = numer * sum((tau*lam_ser*(lam_ser-1))**k for k in range(N_terms + 2))
G_B = expand(G_B)
# Get coefficients
eqs = []
for k in range(1, N_terms):
    c = G_B.coeff(tau, k)
    c = expand(c)
    eqs.append(c - F_coeffs[k])
    print(f"tau^{k}: {c} = {F_coeffs[k]}")

# solve sequentially
solved = {}
for k in range(1, N_terms):
    eq_k = eqs[k-1].subs(solved)
    eq_k = expand(eq_k)
    # this involves lam_{k-1} at highest new
    sol_k = solve(eq_k, lam_syms[k-1])
    print(f"  Solve for l{k-1}: {sol_k}")
    if sol_k:
        solved[lam_syms[k-1]] = sol_k[0]

print("\nlam(tau) coefficients solved:")
for i, s in enumerate(lam_syms):
    if s in solved:
        print(f"  l{i} = {solved[s]}")
