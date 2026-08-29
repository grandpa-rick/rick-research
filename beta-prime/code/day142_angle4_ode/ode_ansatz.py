"""
Day 142 Attack B — ODE ansatz.

f(T; U, V) = Σ_b (U)_b (V)_b T^b / b! = 2F0(U, V;; T) (formally).

Recurrence for coefs f_b = (U)_b (V)_b / b!:
    f_{b+1} = (U+b)(V+b)/(b+1) · f_b.

In terms of θ = T d/dT acting on T^b: θ T^b = b T^b.

Try derivation. If  g_b = (U)_b (V)_b, then g_{b+1} = (U+b)(V+b) g_b.
So a formal ODE for the "reduced" series F = Σ g_b T^b (not divided by b!) is:
    Σ_b g_{b+1} T^{b+1} = T · Σ_b (U+b)(V+b) g_b T^b
    F - g_0 = T · (U + θ)(V + θ) F  →  (I - T (U+θ)(V+θ)) F = 1.
For f = Σ g_b T^b / b! things are different because of the 1/b!.

Let f = Σ (U)_b (V)_b T^b / b!.  Then θ f = Σ (U)_b (V)_b · b · T^b / b!
= Σ (U)_b (V)_b T^b / (b-1)!  (b ≥ 1).
θ (θ+1) f =  Σ (U)_b (V)_b · b(b-1+... hmm let's redo).

The recurrence gives:
  (U)_b (V)_b / b! => f coefficient of T^b.
  (U+b)(V+b) f_b = (b+1) f_{b+1}, so
    Σ_b (U+b)(V+b) f_b T^b = Σ_b (b+1) f_{b+1} T^b = d/dT f = f'.
So  (U + θ)(V + θ) · f = θ · (f/T) ??? Wait:
  Σ_b (U+b)(V+b) f_b T^b = f' = df/dT
So we get  (U + θ)(V + θ) f = f'.  Note f' = θf / T.  So equivalently
  T (U + θ)(V + θ) f = θ f
  or  [T (U + θ)(V + θ) - θ] f = 0.
  i.e.  L f = 0  with  L = T (U + θ)(V + θ) - θ.

Check: [T (U + θ)(V + θ) f]_{T^n} = [(U + θ)(V + θ) f]_{T^{n-1}} = (U + n - 1)(V + n - 1) f_{n-1}.
And [θ f]_{T^n} = n f_n = (U + n - 1)(V + n - 1) f_{n-1}  ← from recurrence.
So LHS = RHS.  Verified.

So L = T(U + θ)(V + θ) - θ,  L f = 0.

Now apply L to F_P = Σ P_b(U, V, E_3) T^b / b!  and see what comes out.

If F_P satisfies L F_P = R(T, U, V, E_3) for some "simple" R (like R = c·E_3·F_P or R = f · Q, etc.), we might have a Frobenius-type ODE that captures U_b.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from compute_P_UV import compute_P_UV, U, V
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day140_interior')
from verify_gf_form import E3
from sympy import (symbols, expand, Integer, Rational, Poly, factorial,
                   rf, factor, together, simplify, diff)

T = symbols('T')

def theta(P):
    """θ = T d/dT."""
    return expand(T * diff(P, T))

def apply_L(P):
    """L = T(U+θ)(V+θ) - θ."""
    # First (V + θ) P
    P1 = expand(V*P + theta(P))
    # Then (U + θ) P1
    P2 = expand(U*P1 + theta(P1))
    # T * P2
    P3 = expand(T * P2)
    # subtract θ P
    return expand(P3 - theta(P))

def truncate_T(P, N):
    Pp = Poly(expand(P), T)
    out = Integer(0)
    for d in range(N + 1):
        c = Pp.coeff_monomial(T**d)
        out += c * T**d
    return out

def build_FP(P_UV_dict, B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += P_UV_dict[b] * T**b / factorial(b)
    return F

def build_f(B_max):
    F = Integer(0)
    for b in range(B_max + 1):
        F += rf(U, b) * rf(V, b) * T**b / factorial(b)
    return F

def one_over_series(f, N):
    fp = Poly(expand(f), T)
    a = {d: fp.coeff_monomial(T**d) for d in range(N + 1)}
    if a[0] != 1:
        raise ValueError(f"Series does not start with 1: {a[0]}")
    b = {0: Integer(1)}
    for n in range(1, N + 1):
        s = Integer(0)
        for k in range(1, n + 1):
            s += a[k] * b[n - k]
        b[n] = expand(-s)
    out = Integer(0)
    for d in range(N + 1):
        out += b[d] * T**d
    return out

def main():
    B_MAX = 12
    N_TRUNC = B_MAX

    print(f"Building P_b for b = 0..{B_MAX} ...")
    P_UV = compute_P_UV(B_MAX)

    print("Building F_P and f...")
    FP = build_FP(P_UV, B_MAX)
    f_s  = build_f(B_MAX)

    # First verify L f = 0
    print("\nVerifying L·f = 0 (up to truncation) ...")
    Lf = truncate_T(apply_L(f_s), B_MAX - 1)
    # The T = truncation issue: applying (U+θ)(V+θ) preserves degrees; T shifts up.
    # So L f up to T^{B_MAX - 1} should be exactly 0 in our truncation (since we have f up to T^{B_MAX}).
    print(f"  L·f (up to T^{B_MAX - 1}) = {Lf}")
    # Also verify a few coefficients
    Lfp = Poly(expand(apply_L(f_s)), T)
    for d in range(B_MAX):
        c = Lfp.coeff_monomial(T**d)
        if c != 0:
            print(f"    [T^{d}]  {c}")

    print("\nApplying L to F_P ...")
    LFP = apply_L(FP)
    LFP_trunc = truncate_T(LFP, B_MAX - 1)

    print(f"\nL·F_P (up to T^{B_MAX - 1}):")
    Lp = Poly(expand(LFP_trunc), T)
    for d in range(B_MAX):
        c = expand(Lp.coeff_monomial(T**d))
        if c != 0:
            # factor out E_3 if possible
            print(f"\n  [T^{d}]  {c}")

    # Now try: LFP = E_3 · Q(T, U, V, E_3) · F_P ?  Or LFP = R · f ?
    # First: LFP / F_P.
    print("\n" + "=" * 70)
    print("Trying LFP = X · F_P (rational X in T with coefs in U, V, E_3)")
    print("=" * 70)
    invFP = one_over_series(FP, N_TRUNC - 1)
    ratio = truncate_T(expand(LFP_trunc * invFP), N_TRUNC - 1)
    print(f"\nLFP / F_P (series in T):")
    rp = Poly(expand(ratio), T)
    for d in range(N_TRUNC):
        c = expand(rp.coeff_monomial(T**d))
        if c != 0:
            print(f"  [T^{d}]  {c}")
            if d > 8: break

    # Also try LFP / f
    print("\n" + "=" * 70)
    print("Trying LFP = Y · f (rational Y in T with coefs in U, V, E_3)")
    print("=" * 70)
    invf = one_over_series(f_s, N_TRUNC - 1)
    ratio2 = truncate_T(expand(LFP_trunc * invf), N_TRUNC - 1)
    print(f"\nLFP / f (series in T):")
    rp2 = Poly(expand(ratio2), T)
    for d in range(N_TRUNC):
        c = expand(rp2.coeff_monomial(T**d))
        if c != 0:
            print(f"  [T^{d}]  {c}")
            if d > 8: break

    return LFP_trunc, FP, f_s

if __name__ == '__main__':
    main()
