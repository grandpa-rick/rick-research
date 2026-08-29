"""Day 130 extended verification.

Purpose:
  (a) Reproduce prior agent's b=2..6 match for the candidate EGF.
  (b) Extend to b=7 and b=8 — compute Ψ(e_2^b)|_top with the CORRECTED
      day127/lib.py and compare monomial-by-monomial against the T^b/b!
      coefficient of the candidate EGF.
  (c) Check whether the FULL Ψ(e_2^b) equals its top-weight part
      (for b=3,4,5), so we know if the EGF captures the full crown-jewel
      claim or only the top slice.
  (d) Structural weight check on the candidate EGF.
"""

import sys, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, max_weight,
                                 list_top_weight_coeffs, count_p112,
                                 weight_of_e_monom,
                                 e1_u, e2_u, e3_u, E1, E2, E3)

from sympy import (symbols, expand, Poly, Integer, S, Rational, binomial,
                    factorial, log, exp, cancel, together, simplify,
                    factor, Symbol, series as sser, oo)

T_ = Symbol('T_')

# ---------------------------------------------------------------------
# Compute P_b = Ψ(e_2^b)|_top and also keep the full Ψ(e_2^b) around
# ---------------------------------------------------------------------
def compute_psi_full_and_top(b):
    if b == 0:
        return Integer(1), Integer(1)
    psi_u = Psi_direct(e2_u**b)
    psi_e = sym_to_ebasis_direct(psi_u)
    return psi_e, top_weight_part(psi_e, b)


# ---------------------------------------------------------------------
# Expand the candidate EGF to order T^N, coefficient by coefficient.
# We handle the E2/E1 - 1 exponent by expanding (1+E1 T)^{E2/E1 - 1}
# via the generalized binomial series:
#   (1+y)^alpha = sum_{n>=0} binomial(alpha, n) y^n
# where binomial(alpha, n) = alpha(alpha-1)...(alpha-n+1)/n!.
# With alpha = E2/E1 - 1, each falling-factorial
#   alpha(alpha-1)...(alpha-n+1)
# is a polynomial in E2/E1, then multiplied by y^n = (E1 T)^n gives
# a polynomial in E1 and E2 times T^n.  The E1's clear the denominators
# in a way we verify by construction.
# ---------------------------------------------------------------------

def expand_A(N):
    """A(T) = (1+E1 T)^{E2/E1 - 1}, return dict {n: coeff_of_T^n}."""
    # alpha = E2/E1 - 1
    # binomial(alpha, n) * (E1 T)^n
    # Using falling factorial:
    #   alpha_falling_n = prod_{k=0..n-1} (alpha - k)
    #                    = prod_{k=0..n-1} (E2/E1 - 1 - k)
    #                    = prod_{k=0..n-1} (E2 - (k+1) E1) / E1^n
    # So binomial(alpha, n) * (E1 T)^n
    #   = [ prod_{k=0..n-1} (E2 - (k+1) E1) / E1^n ] * E1^n * T^n / n!
    #   = [ prod_{r=1..n} (E2 - r E1) ] / n!  * T^n
    coeffs = {0: Integer(1)}
    for n in range(1, N+1):
        prod = Integer(1)
        for r in range(1, n+1):
            prod = expand(prod * (E2 - r * E1))
        coeffs[n] = expand(prod / factorial(n))
    return coeffs


# ---------------------------------------------------------------------
# L(T) = E3 * [ T/(E1 (1+E1 T)^2) - log(1+E1 T)/E1^2 ]
# Expand as a power series in T.  We expand each piece separately,
# multiply by E3, then exponentiate.
# ---------------------------------------------------------------------

def expand_L(N):
    """L(T) as dict {n: coeff of T^n}, coefficients are polynomials in E1,E3.
    (No E2 dependence.)
    """
    # 1/(1 + E1 T)^2 = sum_{k>=0} (-1)^k (k+1) (E1 T)^k
    # So T / (E1 (1+E1 T)^2) = sum_{k>=0} (-1)^k (k+1) E1^(k-1) T^(k+1)
    # Let n = k+1, k = n-1:
    #   [T^n] = (-1)^(n-1) * n * E1^(n-2),  for n >= 1
    # (For n=1 this is 1 · E1^{-1} — a Laurent pole in E1.  It gets
    # cancelled by the log piece.)
    # log(1+E1 T)/E1^2 = sum_{n>=1} (-1)^(n-1) (E1 T)^n / n  · 1/E1^2
    #                  = sum_{n>=1} (-1)^(n-1) E1^(n-2) T^n / n
    # So [T^n] of bracket:
    #   (-1)^(n-1) * n * E1^(n-2) - (-1)^(n-1) * E1^(n-2) / n
    #   = (-1)^(n-1) * E1^(n-2) * (n - 1/n)
    #   = (-1)^(n-1) * E1^(n-2) * (n^2 - 1) / n
    # For n=1 this is 0, so no E1^{-1} pole (as expected).
    coeffs = {0: Integer(0)}
    for n in range(1, N+1):
        if n == 1:
            coeffs[n] = Integer(0)
        else:
            coeffs[n] = expand( Rational((-1)**(n-1)) * E1**(n-2)
                                * (n**2 - 1) * Rational(1, n) * E3 )
    return coeffs


def series_from_dict(coeff_dict, N):
    """Convert {n: c_n} back to a truncated sympy expression sum c_n T^n."""
    return sum(coeff_dict.get(n, Integer(0)) * T_**n for n in range(N+1))


def truncated_mul(A, B, N):
    """Multiply two series-coefficient-dicts truncated at T^N."""
    out = {n: Integer(0) for n in range(N+1)}
    for i in range(N+1):
        ai = A.get(i, Integer(0))
        if ai == 0:
            continue
        for j in range(N+1 - i):
            bj = B.get(j, Integer(0))
            if bj == 0:
                continue
            out[i+j] = expand(out[i+j] + ai * bj)
    return out


def exp_series(L_coeffs, N):
    """exp(L) as dict, where L_coeffs is dict with L[0]=0."""
    if L_coeffs.get(0, Integer(0)) != 0:
        raise ValueError("exp requires L(0)=0 for polynomial expansion")
    # exp(L) = sum_k L^k / k!.  Since L starts at T (or T^2 here), only
    # need k up to N.
    result = {n: Integer(0) for n in range(N+1)}
    result[0] = Integer(1)
    L_power = {n: Integer(0) for n in range(N+1)}
    L_power[0] = Integer(1)  # L^0
    for k in range(1, N+1):
        L_power = truncated_mul(L_power, L_coeffs, N)
        # add L^k / k!
        fk = factorial(k)
        for n in range(N+1):
            if L_power[n] != 0:
                result[n] = expand(result[n] + L_power[n] / fk)
        # if L_power is all zero for n<=N we could stop, but N small
    return result


def egf_coeffs(N):
    """Compute [T^n] F(T) for n=0..N as sympy polynomials in E1,E2,E3."""
    A = expand_A(N)
    L = expand_L(N)
    expL = exp_series(L, N)
    F = truncated_mul(A, expL, N)
    return F


# ---------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------

def compare_top(b, P_top, F_coeff_Tb):
    """Compare P_top (weight-b polynomial in E1,E2,E3) with b! * F_coeff_Tb.
    Return (bool_ok, diff_expr)."""
    predicted_Pb = expand(factorial(b) * F_coeff_Tb)
    diff = expand(P_top - predicted_Pb)
    return diff == 0, diff


# ---------------------------------------------------------------------
# Weight check on candidate EGF
# ---------------------------------------------------------------------

def weight_of_poly(expr):
    expr = expand(expr)
    if expr == 0:
        return -1
    p = Poly(expr, E1, E2, E3)
    w = -1
    for monom, coeff in p.as_dict().items():
        if coeff == 0:
            continue
        i, j, k = monom
        w = max(w, i + j + 2*k)
    return w


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():
    log_lines = []
    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    N = 8

    log("=" * 72)
    log("Extended verification of candidate EGF for Ψ(e_2^b)|_top")
    log("  F(T) = (1+E1 T)^{E2/E1 - 1}")
    log("       · exp( E3 * [ T/(E1(1+E1 T)^2) - log(1+E1 T)/E1^2 ] )")
    log("=" * 72)

    # ------------------------------------------------------------------
    # (1) Expand the EGF to order T^8
    # ------------------------------------------------------------------
    log("\nStep 1: Expand candidate EGF via generalized binomial + exp series")
    log("  (No sympy series() — direct polynomial construction.)")
    t0 = time.time()
    F_coeffs = egf_coeffs(N)
    log(f"  Done in {time.time()-t0:.2f}s")
    for n in range(N+1):
        w = weight_of_poly(F_coeffs[n])
        log(f"  [T^{n}] F = polynomial of (1,1,2)-weight {w}"
            f"  (expected ≤ {n})")

    # ------------------------------------------------------------------
    # (2) Compute Ψ(e_2^b) full & top for b=0..N
    # ------------------------------------------------------------------
    log("\nStep 2: Compute Ψ(e_2^b) (full and top) for b=0..%d" % N)
    Ps_full = {0: Integer(1)}
    Ps_top  = {0: Integer(1)}
    for b in range(1, N+1):
        t0 = time.time()
        full, top = compute_psi_full_and_top(b)
        dt = time.time() - t0
        Ps_full[b] = full
        Ps_top[b] = top
        w = max_weight(full)
        log(f"  b={b}: computed in {dt:.2f}s"
            f", max-weight of full Ψ = {w} (expected {b})")

    # ------------------------------------------------------------------
    # (3) Monomial-by-monomial comparison Ψ|_top vs b! * [T^b] F
    # ------------------------------------------------------------------
    log("\nStep 3: Compare Ψ(e_2^b)|_top vs b! · [T^b] F(T), monomial-by-monomial")
    all_ok = True
    per_b_status = {}
    for b in range(N+1):
        ok, diff = compare_top(b, Ps_top[b], F_coeffs[b])
        per_b_status[b] = ok
        if ok:
            log(f"  b={b}: MATCH  (checked {count_p112(b)} monomials of weight {b})")
        else:
            log(f"  b={b}: MISMATCH")
            log(f"       diff = Ψ_top - b!·[T^b]F  =  {diff}")
            # detailed breakdown
            p_diff = Poly(diff, E1, E2, E3)
            for monom, coeff in sorted(p_diff.as_dict().items()):
                i,j,k = monom
                Pcoef = Poly(Ps_top[b], E1, E2, E3).as_dict().get((i,j,k), Integer(0))
                Fcoef = Poly(expand(factorial(b)*F_coeffs[b]), E1, E2, E3).as_dict().get((i,j,k), Integer(0))
                log(f"       E1^{i} E2^{j} E3^{k}: Ψ_top={Pcoef}, b!·[T^b]F={Fcoef}, diff={coeff}")
            all_ok = False

    log("")
    for b in range(N+1):
        marker = "PASS" if per_b_status[b] else "FAIL"
        log(f"  b={b}: {marker}")

    # ------------------------------------------------------------------
    # (4) Full Ψ vs top-only:  does full Ψ have sub-top terms?
    # ------------------------------------------------------------------
    log("\nStep 4: Sub-top terms in the FULL Ψ(e_2^b)")
    log("  If full Ψ = top part, then EGF captures the full crown-jewel.")
    log("  Otherwise, EGF captures ONLY the top slice.")
    for b in range(2, min(N+1, 6)):
        diff_full_minus_top = expand(Ps_full[b] - Ps_top[b])
        if diff_full_minus_top == 0:
            log(f"  b={b}: full Ψ = top part (no sub-top junk)")
        else:
            n_terms = len(Poly(diff_full_minus_top, E1, E2, E3).as_dict())
            w_sub = weight_of_poly(diff_full_minus_top)
            log(f"  b={b}: full Ψ has SUB-TOP TERMS "
                f"({n_terms} nonzero monomials of weight ≤ {w_sub} < {b})")
            log(f"       sub-top part = {diff_full_minus_top}")

    # ------------------------------------------------------------------
    # (5) Structural weight check on candidate EGF (informal)
    # ------------------------------------------------------------------
    log("\nStep 5: Structural weight check on candidate EGF")
    log("  Factor A(T) = (1+E1 T)^{E2/E1 - 1}.")
    log("  Its T^n coefficient equals ∏_{r=1..n}(E2 - r E1) / n!  (from our")
    log("  binomial expansion), which is a polynomial in E1,E2 of degree n")
    log("  and (1,1,·)-weight n.  E1^i E2^j appears only if i+j = n, so")
    log("  (1,1,2)-weight = n ≤ n.  OK.  (In particular NO E1 in denominator.)")
    for n in range(N+1):
        w = weight_of_poly(expand_A(N)[n])
        log(f"    A: [T^{n}] weight = {w}  (bound n = {n})")

    log("\n  Factor exp(E3·M(T,E1)) where")
    log("    [T^n] M = (-1)^(n-1) (n^2-1)/n · E1^(n-2)  for n≥2, zero for n=0,1.")
    log("  Each factor of E3 has (1,1,2)-weight 2; each factor of E1 has")
    log("  weight 1.  [T^n] M has weight (n-2) + 0 = n-2 (in E1) + 0 (no E3")
    log("  yet since we haven't multiplied E3 in — wait, M was defined")
    log("  WITHOUT the E3 prefactor; we absorbed E3 into L earlier).  With E3")
    log("  attached: [T^n] (E3·M) has weight (n-2) + 2 = n.  OK.")
    log("  In exp(L), [T^n] contains (E3·M)^k terms with total T-degree n.")
    log("  Each factor (E3·M) at T^{n_j} contributes weight n_j, and weights")
    log("  add ⇒ (1,1,2)-weight of [T^n] exp(L) ≤ n.  OK.")
    for n in range(N+1):
        w = weight_of_poly(egf_coeffs(N)[n])  # already computed above; recompute for clarity
        log(f"    F: [T^{n}] weight = {w}  (bound n = {n})")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    log("\n" + "=" * 72)
    log("SUMMARY")
    log("=" * 72)
    log(f"  Verification for b=0..{N}: "
        + ("ALL PASS" if all_ok else "SOME FAIL"))
    for b in range(N+1):
        log(f"    b={b}: {'PASS' if per_b_status[b] else 'FAIL'}")

    with open('/home/agent/projects/beta-prime/code/day130/verify_extended_output.txt', 'w') as fp:
        fp.write('\n'.join(log_lines))
    log("\nSaved to verify_extended_output.txt")


if __name__ == '__main__':
    main()
