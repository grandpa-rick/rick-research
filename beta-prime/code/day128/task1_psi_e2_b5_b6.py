"""Day 128 — Task 1: Extend Ψ(e_2^b) verification to b=5, b=6
using the CORRECTED reduce_y library at day127/lib.py.

Two independent computations to cross-verify:
  A) Direct: Ψ(f) = T(f·V)/V in u_1,u_2,u_3 (division must be exact).
     Then convert result to e-basis by the standard leading-term algorithm.
  B) Via (s,y,τ) coordinates: S(Ψ(f)) = S(T(f·V))/S(V), computed by
     reducing S(T(f·V)) and S(V) mod y²-sy+τ. Then match against
     an e-basis expansion by using the fact that in these coordinates
     e_1 = τ+s, e_2 = τ(s+1), e_3 = τ² (all free of y after reduce_y).

We will do (A) as the primary calculation and use (B) only if (A) is
too slow. For b=5, b=6 the direct route should still be feasible.
"""

import sys, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
from lib import (reduce_y, falling, apply_S, apply_T_then_S,
                 antisym_orbit, tau_deg, top_tau,
                 s, y, t, u1, u2, u3)

from sympy import symbols, expand, Poly, Integer, S, prod, factor
from itertools import permutations

E1, E2, E3 = symbols('E1 E2 E3')

V = (u1 - u2) * (u1 - u3) * (u2 - u3)
e1_u = u1 + u2 + u3
e2_u = u1*u2 + u1*u3 + u2*u3
e3_u = u1*u2*u3


def T_u(poly_u):
    """T on u-monomials: u_1^a u_2^b u_3^c -> [u_1]_a [u_2]_b [u_3]_c."""
    poly_u = expand(poly_u)
    if poly_u == 0:
        return Integer(0)
    p = Poly(poly_u, u1, u2, u3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        a, b, c = monom
        out += coeff * falling(u1, a) * falling(u2, b) * falling(u3, c)
    return expand(out)


def Psi_direct(f):
    """Ψ(f) = T(f·V)/V in u1,u2,u3 (exact division)."""
    num = expand(T_u(expand(f * V)))
    q, r = Poly(num, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise RuntimeError(f"Nonzero remainder in Ψ direct: {r.as_expr()}")
    return q.as_expr()


def sym_to_ebasis_direct(f):
    """Standard elementary-symmetric conversion via leading term (u1>u2>u3, lex)."""
    f = expand(f)
    result = Integer(0)
    while f != 0:
        p = Poly(f, u1, u2, u3)
        d = p.as_dict()
        if not d:
            break
        # leading in lex u1>u2>u3
        lead = max(d.keys())
        coeff = d[lead]
        a, b, c = lead
        if not (a >= b >= c):
            raise ValueError(f"Non-symmetric input; leading exp = {lead}")
        i, j, k = a - b, b - c, c
        e_term_u = e1_u**i * e2_u**j * e3_u**k
        f = expand(f - coeff * e_term_u)
        result += coeff * E1**i * E2**j * E3**k
    return result


def weight_of_e_monom(i, j, k):
    return i + j + 2*k


def max_weight(expr_E):
    expr_E = expand(expr_E)
    if expr_E == 0:
        return -1
    p = Poly(expr_E, E1, E2, E3)
    w = -1
    for monom, coeff in p.as_dict().items():
        if coeff == 0:
            continue
        i, j, k = monom
        w = max(w, weight_of_e_monom(i, j, k))
    return w


def top_weight_part(expr_E, target):
    expr_E = expand(expr_E)
    if expr_E == 0:
        return Integer(0)
    p = Poly(expr_E, E1, E2, E3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if weight_of_e_monom(i, j, k) == target:
            out += coeff * E1**i * E2**j * E3**k
    return out


def count_p112(n):
    """Number of (i,j,k) >= 0 with i+j+2k = n (partitions counted by (1,1,2) weight)."""
    c = 0
    for k in range(n // 2 + 1):
        for j in range(n - 2*k + 1):
            i = n - 2*k - j
            if i >= 0:
                c += 1
    return c


def list_top_weight_coeffs(expr_E, target):
    expr_E = expand(expr_E)
    p = Poly(expr_E, E1, E2, E3)
    d = p.as_dict()
    out = []
    for k in range(target // 2 + 1):
        for j in range(target - 2*k + 1):
            i = target - 2*k - j
            if i < 0:
                continue
            key = (i, j, k)
            c = d.get(key, Integer(0))
            out.append((key, c))
    return out


def sy_tau_check(psi_u, psi_e):
    """Cross-verify: substituting e_1=τ+s, e_2=τ(s+1), e_3=τ² into psi_e
    should equal apply_S(psi_u) reduced mod y²-sy+τ.
    (Both are elements of Q[s,τ] since psi_u is symmetric.)"""
    lhs = reduce_y(apply_S(psi_u))
    rhs = expand(psi_e.subs({E1: t + s, E2: t*(s + 1), E3: t**2}))
    diff = expand(lhs - rhs)
    return diff == 0


def main():
    log_lines = []
    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 70)
    log("Task 1: Ψ(e_2^b) for b = 2..6 using CORRECTED library")
    log("=" * 70)

    results = {}
    for b in range(2, 7):
        t0 = time.time()
        psi_u = Psi_direct(e2_u**b)
        t1 = time.time()
        psi_e = sym_to_ebasis_direct(psi_u)
        t2 = time.time()
        w = max_weight(psi_e)
        results[b] = (psi_u, psi_e, w)
        log(f"\n--- b = {b} ---")
        log(f"  Psi time = {t1-t0:.2f}s ; sym→E time = {t2-t1:.2f}s")
        log(f"  max (1,1,2)-weight = {w}  (bound: b = {b})  "
            + ("OK" if w <= b else "VIOLATION"))

        # Cross-check via (s,y,τ) coordinates
        ok = sy_tau_check(psi_u, psi_e)
        log(f"  cross-check S(Ψ) via reduce_y ↔ e-basis substitution: "
            + ("MATCH" if ok else "MISMATCH"))

        p112 = count_p112(b)
        tw_list = list_top_weight_coeffs(psi_e, b)
        nonzero = [(k, c) for k, c in tw_list if c != 0]
        log(f"  # weight-{b} e-monomials (p_{{1,1,2}}({b})) = {p112}")
        log(f"  # top-weight monomials with NONZERO coefficient = {len(nonzero)}")
        log(f"  top-weight polynomial (weight = {b}):")
        tw_poly = top_weight_part(psi_e, b)
        log(f"    {tw_poly}")
        log(f"  full top-weight coefficient table:")
        for (i, j, k), c in tw_list:
            marker = "  <-- ZERO" if c == 0 else ""
            log(f"    E1^{i} E2^{j} E3^{k}  (weight {weight_of_e_monom(i,j,k)}): {c}{marker}")

        if b <= 4:
            log(f"  full Ψ(e_2^{b}) in E-basis:")
            log(f"    {psi_e}")

    # Summary + surprises
    log("\n" + "=" * 70)
    log("Summary of weights (should equal b in every row if bound tight)")
    log("=" * 70)
    for b in range(2, 7):
        _, _, w = results[b]
        p112 = count_p112(b)
        tw = list_top_weight_coeffs(results[b][1], b)
        nz = sum(1 for _, c in tw if c != 0)
        log(f"  b={b}: max weight = {w}, # top-weight e-monomials = {p112}, "
            f"# nonzero at top = {nz}")

    # Save output
    with open('/home/agent/projects/beta-prime/code/day128/task1_output.txt', 'w') as fp:
        fp.write('\n'.join(log_lines))
    log("\nSaved to task1_output.txt")


if __name__ == '__main__':
    main()
