"""Look for a P-recurrence or algebraic equation for b_k with extended data (up to b_9)."""
import sys
from sympy import symbols, Integer, Rational, Poly, solve, expand

# b_seq needs to be filled in after running extend_k8, extend_k9
b_seq = [3, 27, 417, 7851, 164124, 3661389, 85384566]

# Try to load b_8, b_9 from files
try:
    with open('/home/agent/projects/beta-prime/code/day144_bk_extension/a8_b8.txt') as f:
        for line in f:
            if line.startswith('b_8'):
                b_seq.append(int(line.split('=')[1].strip()))
except FileNotFoundError:
    pass
try:
    with open('/home/agent/projects/beta-prime/code/day144_bk_extension/a9_b9.txt') as f:
        for line in f:
            if line.startswith('b_9'):
                b_seq.append(int(line.split('=')[1].strip()))
except FileNotFoundError:
    pass

print(f"b sequence ({len(b_seq)} terms): {b_seq}")


def try_precursive(order, deg):
    n = len(b_seq)
    n_vars = (order + 1) * (deg + 1)
    cs = symbols(f'c0:{n_vars}')
    eqs = []
    for idx in range(order, n):
        true_k = idx + 1
        eq = 0
        for j in range(order + 1):
            poly_val = sum(cs[j*(deg+1) + d] * true_k**d for d in range(deg + 1))
            eq += poly_val * b_seq[idx - j]
        eqs.append(eq)
    sol = solve(eqs, cs, dict=True)
    return sol, n_vars, len(eqs)


print("\n=== Search for P-recurrence of b_k ===")
for order in range(1, 6):
    for deg in range(0, 6):
        try:
            sol, nv, ne = try_precursive(order, deg)
        except Exception as e:
            print(f"  order={order} deg={deg}: FAILED — {e}")
            continue
        if not sol:
            continue
        first_sol = sol[0]
        free_syms = set()
        for v in first_sol.values():
            free_syms |= v.free_symbols
        free_syms &= set(symbols(f'c0:{nv}'))
        n_free = len(free_syms)
        excess = nv - ne
        # Check if the "solution" is the trivial all-zero one
        nonzero_count = sum(1 for kk, vv in first_sol.items() if vv != 0)
        # A "unique up to scale" nontrivial solution: n_free == 1, and non-trivial
        marker = ""
        if excess <= 0 and n_free <= 1:
            # meaningful only if nontrivial
            marker = "  **UNIQUE up to scale**"
        print(f"  order={order} deg={deg}: nvars={nv} neqs={ne} free={n_free} excess={excess} nonzero_in_soln={nonzero_count}{marker}")
        if excess <= 0 and n_free <= 1:
            print("    Recurrence coefficients:")
            for kk, vv in first_sol.items():
                if vv != 0:
                    print(f"      {kk} = {vv}")


# Also test algebraic equations for F(τ) = Σ b_k τ^k
tau = symbols('tau')
F_series = sum(b_seq[i] * tau**(i+1) for i in range(len(b_seq)))
N_terms = len(b_seq)


def try_algebraic(deg_F, deg_tau):
    n_coefs = (deg_F + 1) * (deg_tau + 1)
    cs = symbols(f'a0:{n_coefs}')
    def P_at(j, tval):
        return sum(cs[j*(deg_tau+1) + d] * tval**d for d in range(deg_tau + 1))
    F_powers = [Integer(1)]
    for j in range(1, deg_F + 1):
        Fp = expand(F_powers[-1] * F_series)
        Fp = sum([Rational(int(c)) * tau**e for e, c in enumerate(Poly(Fp, tau).all_coeffs()[::-1])])
        F_powers.append(Fp)
    total = Integer(0)
    for j in range(deg_F + 1):
        total = expand(total + P_at(j, tau) * F_powers[j])
    Poly_total = Poly(total, tau)
    eqs = []
    for d in range(N_terms + 1):
        eqs.append(Poly_total.coeff_monomial(tau**d))
    sol = solve(eqs, cs, dict=True)
    return sol, n_coefs, len(eqs)


print("\n=== Search for algebraic equation for F(τ) = Σ b_k τ^k ===")
for deg_F in [2, 3, 4]:
    for deg_tau in range(0, 5):
        try:
            sol, nv, ne = try_algebraic(deg_F, deg_tau)
        except Exception as e:
            print(f"  deg_F={deg_F} deg_tau={deg_tau}: FAILED — {e}")
            continue
        if not sol:
            continue
        s = sol[0]
        free_syms = set()
        for v in s.values():
            free_syms |= v.free_symbols
        free_syms &= set(symbols(f'a0:{nv}'))
        n_free = len(free_syms)
        nonzero_count = sum(1 for k, v in s.items() if v != 0)
        marker = ""
        if n_free <= 1 and nv - ne <= 0:
            marker = "  **possibly UNIQUE**"
        print(f"  deg_F={deg_F} deg_tau={deg_tau}: nvars={nv} neqs={ne} free={n_free} nonzero_in_soln={nonzero_count}{marker}")
