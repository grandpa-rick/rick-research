"""Look for a P-recurrence or algebraic equation for b_k = 3, 27, 417, 7851, 164124, 3661389, 85384566."""
from sympy import symbols, Integer, Rational, Poly, solve, Matrix, sqrt, series, simplify
from sympy.abc import k, x

b_seq = [3, 27, 417, 7851, 164124, 3661389, 85384566]

# --- Test P-recurrences of type: p_0(k) b_k + p_1(k) b_{k-1} + ... = 0 ---
def try_precursive(order, deg):
    n = len(b_seq)
    # variables
    n_vars = (order + 1) * (deg + 1)
    cs = symbols(f'c0:{n_vars}')
    eqs = []
    for idx in range(order, n):  # actual index of the "current" term
        true_k = idx + 1  # 1-indexed
        eq = 0
        for j in range(order + 1):
            poly_val = sum(cs[j*(deg+1) + d] * true_k**d for d in range(deg + 1))
            eq += poly_val * b_seq[idx - j]
        eqs.append(eq)
    sol = solve(eqs, cs, dict=True)
    return sol, n_vars, len(eqs)

print("=== Search for P-recurrence of b_k ===")
for order in range(1, 5):
    for deg in range(0, 5):
        sol, nv, ne = try_precursive(order, deg)
        if not sol:
            continue
        # Filter: is there a non-trivial solution not just parameters?
        # Number of free parameters should be small (ideally 1)
        # Count free parameters
        if sol:
            first_sol = sol[0]
            # Free params = symbols appearing on RHS
            free_syms = set()
            for v in first_sol.values():
                free_syms |= v.free_symbols
            free_syms &= set(symbols(f'c0:{nv}'))
            n_free = len(free_syms)
            excess = nv - ne  # extra freedom without recurrence
            print(f"  order={order} deg={deg}: nvars={nv}, neqs={ne}, free_params={n_free}, deg-of-freedom-excess={excess}")
            if n_free <= 1 and excess <= 0:
                print(f"    UNIQUE recurrence up to scale!")
                for kk, vv in first_sol.items():
                    print(f"      {kk} = {vv}")

# --- Test algebraic equation for F(τ) = Σ b_k τ^k ---
# Try F satisfies: Σ_{i, j} c_{i, j} τ^i F^j = 0, with total degree bounded.
print("\n=== Search for algebraic equation for F(τ) ===")
tau = symbols('tau')
F_series = sum(b_seq[i] * tau**(i+1) for i in range(len(b_seq)))
N_terms = len(b_seq)  # coefficients we know

def try_algebraic(deg_F, deg_tau):
    """Look for Σ_{j=0..deg_F} P_j(tau) F^j = 0, where deg P_j ≤ deg_tau."""
    n_coefs = (deg_F + 1) * (deg_tau + 1)
    cs = symbols(f'a0:{n_coefs}')
    def P_at(j, tval):
        return sum(cs[j*(deg_tau+1) + d] * tval**d for d in range(deg_tau + 1))
    # Compute Σ_j P_j(τ) F^j as a series in τ up to τ^{N_terms}
    from sympy import Poly, expand
    F_powers = [Integer(1)]
    for j in range(1, deg_F + 1):
        Fp = expand(F_powers[-1] * F_series)
        # truncate
        Fp = sum([Rational(int(c)) * tau**e for e, c in enumerate(Poly(Fp, tau).all_coeffs()[::-1])])
        F_powers.append(Fp)
    total = Integer(0)
    for j in range(deg_F + 1):
        total = expand(total + P_at(j, tau) * F_powers[j])
    # Extract coefficients up to τ^N_terms (i.e., check that they're all zero)
    Poly_total = Poly(total, tau)
    eqs = []
    for d in range(N_terms + 1):
        eqs.append(Poly_total.coeff_monomial(tau**d))
    sol = solve(eqs, cs, dict=True)
    return sol, n_coefs, len(eqs)

for deg_F in [2, 3]:
    for deg_tau in range(0, 4):
        sol, nv, ne = try_algebraic(deg_F, deg_tau)
        if sol:
            s = sol[0]
            free_syms = set()
            for v in s.values():
                free_syms |= v.free_symbols
            free_syms &= set(symbols(f'a0:{nv}'))
            n_free = len(free_syms)
            # Check if identically zero:
            nonzero_count = sum(1 for k, v in s.items() if v != 0)
            print(f"  deg_F={deg_F}, deg_tau={deg_tau}: nvars={nv}, neqs={ne}, free={n_free}, nontrivial? {nonzero_count > 0 or n_free < nv}")
            if n_free <= 1 and nv - ne <= 0:
                print(f"    Possibly UNIQUE algebraic equation")
                for kk, vv in s.items():
                    if vv != 0 or 'a' in str(kk):
                        print(f"      {kk} = {vv}")

# The quadratic identity (1 - 2F)² = 1 + 4 A(τ) is essentially saying F satisfies:
# F² - F - A(τ) = 0, with A(τ) known.
# So F is algebraic over ℚ(τ, A(τ)) trivially. The question is whether F is algebraic over ℚ(τ) alone.
