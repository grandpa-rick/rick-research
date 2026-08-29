"""Day 130 — More factorization attempts on the EGF."""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, e1_u, e2_u, e3_u, E1, E2, E3)
from sympy import (symbols, expand, Poly, Integer, S, Rational, binomial,
                    factorial, series, log, exp, cancel, together, simplify,
                    factor, Symbol, sqrt, collect, apart, Function, oo, O)

T_ = Symbol('T_')


def Pb(b):
    if b == 0:
        return Integer(1)
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    return top_weight_part(psi_e, b)


def main():
    N = 6
    Ps = [Pb(b) for b in range(N+1)]

    # Pure E3 slice at E1=E2=0.
    print("Pure E3 slice at E1=E2=0 of P_b:")
    for b, p in enumerate(Ps):
        val = expand(p.subs({E1: 0, E2: 0}))
        print(f"  b={b}: {val}")

    # Values: 1, 0, -3E3, 0, 27 E3^2, 0, -405 E3^3
    # EGF: sum val_b T^b / b! = 1 + 0 + -3E3 T^2/2 + 0 + 27 E3^2 T^4/24 + 0 + -405 E3^3 T^6/720
    # = 1 - 3E3/2 T^2 + 9E3^2/8 T^4 - 9E3^3/16 T^6
    # This looks like Bessel or hypergeometric.
    # Actually (1 - c T^2)^{-alpha} etc. Let's compare with (1+x)^{1/2}: 1 + x/2 - x^2/8 + x^3/16 - 5x^4/128
    # With x = -3 E3 T^2: 1 - 3E3T^2/2 - 9E3^2 T^4/8 - 27 E3^3 T^6/16. Signs of T^4 and T^6 wrong.
    # (1+x)^{-1/2}: 1 - x/2 + 3x^2/8 - 5x^3/16.  With x = -3E3T^2: 1 + 3E3T^2/2 + ... wrong sign.

    # Try functional relation. Let f(T) = 1 - 3E3/2 T^2 + 9E3^2/8 T^4 - 9E3^3/16 T^6.
    # Ratios of consecutive nonzero coeffs:
    # (9/8) / (-3/2) = -3/4
    # (-9/16) / (9/8) = -1/2
    # So ratio changes: -3/4, -1/2 — not exponential.
    # Bessel-like? J_0(z) = sum (-1)^k (z/2)^{2k} / (k!)^2.
    # (z/2)^2 = 3 E3 T^2 / ??? Hmm. Try z^2/4 = 3E3T^2/2 → z^2 = 6 E3 T^2 → z = sqrt(6 E3) T.
    # J_0 coeffs at T^{2k}: (-1)^k * (6 E3 T^2 / 4)^k / (k!)^2 = (-1)^k (3E3T^2/2)^k / (k!)^2.
    # k=0: 1. k=1: -3E3/2 T^2 ok. k=2: 9E3^2/4 / 4 = 9E3^2/16 T^4 → we have 9/8 T^4. Off by 2.
    # k=3: -27 E3^3 / 8 / 36 = -3E3^3/32. We have -9/16. Off.
    # Not exactly Bessel.

    # Try: sum_k (-3 E3 T^2)^k / (2k choose k) or (2k+1)?
    # We have coeffs 1, -3E3/2, 9E3^2/8, -9E3^3/16.
    # Simplify: 1 = 1/1, -3/2 = -3/2, 9/8 = 9/8, -9/16 = -9/16.
    # Compare to (1/2)_k / k! * (-3E3T^2)^k where (1/2)_k = (2k)!/(4^k k!) is Pochhammer.
    # (1/2)_0 = 1, (1/2)_1 = 1/2, (1/2)_2 = 3/4, (1/2)_3 = 15/8.
    # (1/2)_k / k! * (-3E3T^2)^k:
    # k=1: 1/2 * (-3E3) = -3E3/2 ok
    # k=2: 3/4 / 2 * 9E3^2 = 27E3^2/8 — we have 9/8. Off.

    # Look at another interpretation. Let a_k = coefficient of E3^k T^{2k} in EGF|_{E1=E2=0}.
    # a_0 = 1, a_1 = -3/2, a_2 = 9/8, a_3 = -9/16.
    # a_1 / a_0 = -3/2, a_2 / a_1 = -3/4, a_3 / a_2 = -1/2.
    # Differences of ratios: -3/2 → -3/4 → -1/2.
    # -3/(2k) for k=1: -3/2. k=2: -3/4. k=3: -1/2. YES!
    # So a_k / a_{k-1} = -3/(2k), meaning a_k = (-3/2)^k / k!.
    # Check: a_1 = -3/2/1 = -3/2 ✓. a_2 = 9/4/2 = 9/8 ✓. a_3 = -27/8/6 = -9/16 ✓.
    # So a_k = (-3/2)^k / k!, i.e. sum_k a_k E3^k T^{2k} = sum_k (-3 E3 T^2 / 2)^k / k!
    #   = exp(-3 E3 T^2 / 2).
    # So EGF|_{E1=E2=0} = exp(-3 E3 T^2 / 2).
    print("\nEGF pure-E3 slice = exp(-3 E3 T^2 / 2). Check:")
    from sympy import exp as sym_exp
    predicted = sym_exp(-3 * E3 * T_**2 / 2)
    predicted_series = predicted.series(T_, 0, N+1).removeO()
    print(f"  predicted series: {predicted_series}")
    # Compare with actual
    actual_series = sum(Ps[b].subs({E1: 0, E2: 0}) * T_**b / factorial(b) for b in range(N+1))
    print(f"  actual series:    {expand(actual_series)}")
    diff = expand(predicted_series - actual_series)
    print(f"  diff = {diff}  {'MATCH' if diff == 0 else 'MISMATCH'}")

    # Now full EGF: F(T) = ?
    # We have F|_{E3=0} = (1 + T E1)^{E2/E1 - 1}
    # F|_{E1=E2=0} = exp(-3 E3 T^2 / 2)
    # Conjecture: F(T) = (1 + T E1)^{E2/E1 - 1} * exp(-3 E3 T^2 / 2 * H(T, E1, E2))?
    # Or maybe F(T) = (1 + T E1)^{alpha} * exp(-3 E3 T^2 / 2 / (1+TE1)^k)?
    # Let's compute F * (1+TE1)^{1 - E2/E1} = G(T) and see if G = exp(-3 E3 T^2 / (2 * something))
    # We computed g_coef: 1, 0, -3E3/2, 8 E1 E3/3, -15 E1^2 E3/4 + 9 E3^2/8, 24 E1^3 E3/5 - 4 E1 E3^2, ...
    # Take log(G):
    F = sum(Ps[b] * T_**b / factorial(b) for b in range(N+1))
    F = expand(F)

    alpha_series = Integer(0)
    for n in range(N+1):
        cn = Integer(1)
        for r in range(1, n+1):
            cn *= (E2 - r*E1)
        alpha_series += cn * T_**n / factorial(n)

    a_coef = [alpha_series.coeff(T_, n) for n in range(N+1)]
    F_coef = [F.coeff(T_, n) for n in range(N+1)]
    g_coef = []
    for n in range(N+1):
        g = F_coef[n]
        for k in range(1, n+1):
            g -= a_coef[k] * g_coef[n-k]
        g = expand(g / a_coef[0])
        g_coef.append(g)

    G = sum(g_coef[n] * T_**n for n in range(N+1))
    print(f"\nG(T) = F(T) * (1+T*E1)^(1-E2/E1)  [truncated to T^{N}]:")
    print(f"  {expand(G)}")

    # Take log(G) up to O(T^7)
    # log(1 + h) = h - h^2/2 + h^3/3 - ...
    # where h = G - 1
    h = expand(G - 1)
    logG = Integer(0)
    hpow = Integer(1)
    for k in range(1, N+2):
        hpow = expand(hpow * h)
        # Truncate to O(T^(N+1))
        hpow_trunc = Integer(0)
        p = Poly(hpow, T_)
        for m in range(N+1):
            hpow_trunc += p.coeff_monomial(T_**m) * T_**m
        hpow = hpow_trunc
        logG += ((-1)**(k+1) / Integer(k)) * hpow
    logG = expand(logG)
    print(f"\nlog G(T) [truncated to T^{N}]:")
    for n in range(N+1):
        c = logG.coeff(T_, n)
        c = expand(c)
        print(f"  T^{n}: {c}")
        try:
            print(f"         factored: {factor(c)}")
        except Exception:
            pass

    # Save
    with open('/home/agent/projects/beta-prime/code/day130/log_G_expansion.txt', 'w') as fp:
        fp.write("log G(T) where G(T) = F(T) * (1 + T E1)^{1 - E2/E1}\n")
        fp.write(f"F(T) = sum_b Psi(e_2^b)|_top * T^b / b!\n\n")
        for n in range(N+1):
            c = expand(logG.coeff(T_, n))
            fp.write(f"T^{n}: {c}\n")
            try:
                fp.write(f"       factored: {factor(c)}\n")
            except Exception:
                pass


if __name__ == '__main__':
    main()
