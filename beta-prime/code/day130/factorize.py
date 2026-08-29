"""Day 130 — Try to factorize the full EGF.
We know EGF|_{E3=0} = (1 + t E1)^{E2/E1 - 1}.
Hypothesis: EGF = (1 + t E1)^{E2/E1 - 1} * exp(some E3 tail) or similar.

We compute H(t, E1, E2, E3) = EGF / (1 + t E1)^{E2/E1 - 1}, expanded to O(t^7),
and see what pattern emerges.
"""
import sys, math
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, list_top_weight_coeffs,
                                 e1_u, e2_u, e3_u, E1, E2, E3)
from sympy import (symbols, expand, Poly, Integer, S, Rational, binomial,
                    factorial, series, log, exp, cancel, together, simplify,
                    factor, Symbol, sqrt, collect, apart)

T_ = Symbol('T_')

def Pb(b):
    if b == 0:
        return Integer(1)
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    return top_weight_part(psi_e, b)


def main():
    N = 6
    print("Computing P_b for b=0..6 ...", flush=True)
    Ps = [Pb(b) for b in range(N+1)]
    for b, p in enumerate(Ps):
        print(f"  P_{b} = {p}")

    # EGF: F = sum P_b T^b / b!
    F = sum(Ps[b] * T_**b / factorial(b) for b in range(N+1))
    F = expand(F)

    # We want to work with G(T) = (1 + T E1)^{1 - E2/E1} * F(T)
    # (multiplying by INVERSE of (1+TE1)^{E2/E1 - 1}, i.e. (1+TE1)^{1 - E2/E1})
    # This should equal 1 + T^2 * (E3 stuff) + ...
    # But we can only extract as a formal power series in T.
    #
    # (1+TE1)^{alpha} = sum_n C(alpha, n) (TE1)^n  where alpha = 1 - E2/E1 or E2/E1 - 1.
    # Let alpha = E2/E1 - 1. C(alpha, n) = alpha(alpha-1)...(alpha - n+1)/n!
    # = (E2/E1 - 1)(E2/E1 - 2)...(E2/E1 - n) / n!
    # = prod_{r=1}^n (E2 - r E1) / (E1^n n!)
    # So (1+TE1)^{alpha} = sum_n prod_{r=1}^n (E2 - r E1) * T^n / n!
    # Now compute the INVERSE as a power series in T:
    # (1+TE1)^{-alpha} = sum_n prod_{r=1}^n (-alpha - r + 1) (TE1)^n / n!   [rising factorial]
    # We just want to compute F * (1+TE1)^{-alpha} as formal series in T to order N.
    #
    # Easier: precompute (1+TE1)^{alpha} series in T, then divide F by it as a
    # polynomial in T with sympy series operations.

    alpha_series = Integer(0)
    for n in range(N+1):
        cn = Integer(1)
        for r in range(1, n+1):
            cn *= (E2 - r*E1)
        alpha_series += cn * T_**n / factorial(n)

    print(f"\n(1+TE1)^alpha (truncated to T^{N}):\n  {expand(alpha_series)}")

    # Compute F / alpha_series as a truncated power series in T.
    # Use polynomial long division in T variable.
    from sympy import Poly as SP
    # Multiply out: F(T) = alpha_series(T) * G(T)  where G is unknown.
    # Coefficient extraction:
    # Let a_n = coeff of T^n in alpha_series, g_n = coeff of T^n in G.
    # F_n = sum_{k=0}^n a_k g_{n-k}.
    # So g_n = (F_n - sum_{k=1}^n a_k g_{n-k}) / a_0. a_0 = 1.
    a_coef = [alpha_series.coeff(T_, n) for n in range(N+1)]
    F_coef = [F.coeff(T_, n) for n in range(N+1)]
    g_coef = []
    for n in range(N+1):
        g = F_coef[n]
        for k in range(1, n+1):
            g -= a_coef[k] * g_coef[n-k]
        g = expand(g / a_coef[0])  # a_coef[0] = 1
        g_coef.append(g)

    print("\nG(T) = F(T) / (1+T*E1)^{E2/E1 - 1}, coefficients:")
    for n, gn in enumerate(g_coef):
        gn_factored = factor(gn)
        print(f"  T^{n}: {expand(gn)}")
        print(f"         factored: {gn_factored}")

    # Now try dividing by the "even" E3 series prod: does G(T) = exp(-3 E3 T^2 / 2) * ...?
    # From g_2 = -3 E3.
    # exp(-3 E3 T^2 / 2) = 1 - (3/2) E3 T^2 + (9/8) E3^2 T^4 - (9/16) E3^3 T^6 + ...
    # Multiply by 1: coeff of T^2 = -3E3/2? No, we wanted -3 E3. So maybe exp(-3 E3 T^2)?
    # exp(-3 E3 T^2) = 1 - 3 E3 T^2 + (9/2) E3^2 T^4 - (9/2) E3^3 T^6 + ...
    # Wait, but g_2 as coefficient in FT means EGF: g_2 * T^2 term / ... hmm.
    # Actually G is not EGF; it's OGF now. Because I did NOT rescale.
    # Actually g_coef[n] IS the coefficient of T^n in G (ordinary power series).
    # So if G = exp(-3 E3 T^2/2) then g_2 = -3E3/2 but we got g_2 = -3E3.
    # Hmm. Let me look at what g_coef gives and see if it's another nice form.

    # Try: g_n /= factorial(n)... no.
    # Or: G(T) as EGF: sum g_n T^n / n!, then reinterpret.
    # Let's look at the pattern in g_coef more carefully.

    # Print numerical evaluations
    print("\nEvaluating g_coef at (E1=1, E2=1) to see E3-only structure:")
    for n, gn in enumerate(g_coef):
        val = expand(gn.subs({E1: 1, E2: 1}))
        print(f"  T^{n}: {val}")

    # Also try (E1=0, E2=0) to isolate E3^k terms only:
    print("\nEvaluating g_coef at (E1=0, E2=0) (isolates E3^k parts):")
    for n, gn in enumerate(g_coef):
        val = expand(gn.subs({E1: 0, E2: 0}))
        print(f"  T^{n}: {val}")

    # Try dividing by something involving E3.
    # g_0 = 1, g_1 = 0, g_2 = -3 E3, g_3 = ?, g_4 = ?, g_5 = ?, g_6 = ?
    # At E1 = E2 = 0:
    # g_0 = 1, g_1 = 0, g_2 = -3 E3, g_3 = 0, g_4 = 9 E3^2 / ?, g_5 = 0, g_6 = ?
    # If G(T)|_{E1=E2=0} = h(T) satisfies h(T) = exp(-3 E3 T^2 / 2)?
    # exp(-3 E3 T^2/2) = 1 - (3E3/2) T^2 + (9E3^2/8) T^4 - (9E3^3/16) T^6 + ...
    # But we have coefficient at T^2 as -3 E3 (no factor of 1/2).
    # So maybe (1 - 3 E3 T^2)^{1/2}? Let's expand:
    # (1 + x)^{1/2} = 1 + x/2 - x^2/8 + x^3/16 - 5x^4/128 + ...
    # With x = -3 E3 T^2: 1 + (-3E3/2) T^2 - (9E3^2/8) T^4 + (-27 E3^3/16) T^6...
    # Nope, sign disagrees.

    # Actually looking at coefficient of E3^k in g at (E1=0, E2=0):
    # We have coeff of T^{2k} being... let me compute a bit more carefully.

    # Save results
    out = ['Full G(T) = F(T) / (1+T*E1)^{E2/E1 - 1} coefficients:']
    for n, gn in enumerate(g_coef):
        out.append(f"g_{n}(E1,E2,E3) = {expand(gn)}")
        out.append(f"    factored: {factor(gn)}")
    with open('/home/agent/projects/beta-prime/code/day130/G_expansion.txt', 'w') as fp:
        fp.write('\n'.join(out))


if __name__ == '__main__':
    main()
