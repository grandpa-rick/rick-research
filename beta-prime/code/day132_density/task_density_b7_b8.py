"""Day 132 — Density conjecture at b=7 (and b=8 if time permits).

Rick's crown jewel (Day 131) predicts F(T) = A(T)·B(T) EGF and, in
particular, that the top-(1,1,2)-weight part of Ψ(e_2^b) has ALL possible
monomials nonzero for every b. Day 128 verified this for b = 2..6.

Here we push to b = 7 (20 top monomials expected) and b = 8 (25 expected),
time-capping b=8 at ~10 minutes.

The direct route from day128 template:
    Ψ(f) = T(f·V)/V in u1,u2,u3 (exact division)
    Then convert to E-basis by leading-term stripping.
"""

import sys, time, signal
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
from lib import (reduce_y, falling, apply_S,
                 s, y, t, u1, u2, u3)

from sympy import symbols, expand, Poly, Integer, S

E1, E2, E3 = symbols('E1 E2 E3')

V = (u1 - u2) * (u1 - u3) * (u2 - u3)
e1_u = u1 + u2 + u3
e2_u = u1*u2 + u1*u3 + u2*u3
e3_u = u1*u2*u3


def T_u(poly_u):
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
    num = expand(T_u(expand(f * V)))
    q, r = Poly(num, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise RuntimeError(f"Nonzero remainder in Psi direct: {r.as_expr()}")
    return q.as_expr()


def sym_to_ebasis_direct(f):
    f = expand(f)
    result = Integer(0)
    while f != 0:
        p = Poly(f, u1, u2, u3)
        d = p.as_dict()
        if not d:
            break
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
    lhs = reduce_y(apply_S(psi_u))
    rhs = expand(psi_e.subs({E1: t + s, E2: t*(s + 1), E3: t**2}))
    diff = expand(lhs - rhs)
    return diff == 0


def timeout_handler(signum, frame):
    raise TimeoutError("Time cap reached")


def run_b(b, log, time_cap_s=None):
    if time_cap_s is not None:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(time_cap_s)
    try:
        t0 = time.time()
        psi_u = Psi_direct(e2_u**b)
        t1 = time.time()
        log(f"  Psi(e_2^{b}) time = {t1-t0:.2f}s")

        psi_e = sym_to_ebasis_direct(psi_u)
        t2 = time.time()
        log(f"  sym->E time = {t2-t1:.2f}s")

        w = max_weight(psi_e)
        log(f"  max (1,1,2)-weight = {w}  (bound: b = {b})  "
            + ("OK" if w <= b else "VIOLATION"))

        # Cross-check via (s,y,tau) coords
        ok = sy_tau_check(psi_u, psi_e)
        t3 = time.time()
        log(f"  cross-check S(Psi) via reduce_y <-> e-basis: "
            + ("MATCH" if ok else "MISMATCH") + f"  ({t3-t2:.2f}s)")

        p112 = count_p112(b)
        tw_list = list_top_weight_coeffs(psi_e, b)
        nonzero = [(k, c) for k, c in tw_list if c != 0]
        zeros = [k for k, c in tw_list if c == 0]
        log(f"  # weight-{b} e-monomials p_{{1,1,2}}({b}) = {p112}")
        log(f"  # top-weight monomials NONZERO = {len(nonzero)}")
        log(f"  # top-weight monomials ZERO   = {len(zeros)}")
        if zeros:
            log(f"  ZERO ones: {zeros}")
        log(f"  top-weight polynomial (weight = {b}):")
        tw_poly = top_weight_part(psi_e, b)
        log(f"    {tw_poly}")

        # Pattern coefficients requested
        d = Poly(psi_e, E1, E2, E3).as_dict()
        def get_c(i, j, k):
            return d.get((i, j, k), Integer(0))
        log(f"  Pattern coefficients (top weight):")
        log(f"    [E_1^{b}]           = {get_c(b, 0, 0)}")
        log(f"    [E_2^{b}]           = {get_c(0, b, 0)}")
        log(f"    [E_1^{b-1} E_2]     = {get_c(b-1, 1, 0)}")
        if b % 2 == 0:
            log(f"    [E_3^{b//2}]         = {get_c(0, 0, b//2)}")

        log(f"  full top-weight coefficient table:")
        for (i, j, k), c in tw_list:
            marker = "  <-- ZERO" if c == 0 else ""
            log(f"    E1^{i} E2^{j} E3^{k}  (weight {weight_of_e_monom(i,j,k)}): {c}{marker}")

        return {'b': b, 'p112': p112, 'nonzero': len(nonzero),
                'zeros': zeros, 'tw_poly': tw_poly, 'psi_e': psi_e}
    finally:
        if time_cap_s is not None:
            signal.alarm(0)


def check_from_closed_form(b, zeros, log):
    """If any monomial is zero, extract that coefficient from A(T)*B(T) EGF."""
    if not zeros:
        return
    from sympy import symbols as syms, series, Symbol, log as sym_log, factorial
    T = Symbol('T')
    A = (1 + E1*T)**(E2/E1 - 1)
    # B = exp(E3 * [T/(E1*(1+E1 T)^2) - log(1+E1 T)/E1^2])
    # For a series in T we expand about T=0. But (E2/E1 - 1) and 1/E1
    # make this tricky. Use series in T with E's as symbols.
    from sympy import series as sym_series
    # Simpler: expand A and B separately as series in T up to O(T^{b+1}).
    # A(T): (1+E1 T)^{alpha}, alpha = E2/E1 - 1
    # Use sympy's series
    A_ser = sym_series(A, T, 0, b+1).removeO()
    inner = T/(E1*(1+E1*T)**2) - sym_log(1+E1*T)/E1**2
    inner_ser = sym_series(inner, T, 0, b+1).removeO()
    # exp( E3 * inner_ser ) truncated
    from sympy import exp as sym_exp
    B_ser = sym_series(sym_exp(E3 * inner_ser), T, 0, b+1).removeO()
    F_ser = expand(A_ser * B_ser)
    # coefficient of T^b, times b!
    coef_Tb = Poly(F_ser, T).as_dict().get((b,), Integer(0))
    top = expand(coef_Tb * factorial(b))
    log(f"  From closed form A(T)*B(T), Ψ(e_2^{b})|_top predicted =")
    log(f"    {top}")
    # Compare the specific zero monomials
    d = Poly(top, E1, E2, E3).as_dict()
    for (i, j, k) in zeros:
        c = d.get((i, j, k), Integer(0))
        log(f"    Closed-form coeff of E1^{i} E2^{j} E3^{k} = {c}")


def main():
    log_lines = []
    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 70)
    log("Day 132: Density conjecture at b=7 (and b=8 if time permits)")
    log("=" * 70)

    results = {}

    log("\n--- b = 7 ---")
    try:
        r7 = run_b(7, log)
        results[7] = r7
        if r7['zeros']:
            log("\n  ANOMALY: zeros found at b=7. Checking closed form...")
            check_from_closed_form(7, r7['zeros'], log)
    except Exception as e:
        log(f"  b=7 FAILED: {e!r}")

    log("\n--- b = 8 (time-capped ~10 min) ---")
    try:
        r8 = run_b(8, log, time_cap_s=600)
        results[8] = r8
        if r8['zeros']:
            log("\n  ANOMALY: zeros found at b=8. Checking closed form...")
            check_from_closed_form(8, r8['zeros'], log)
    except TimeoutError:
        log("  b=8 TIMEOUT (>10 min)")
    except Exception as e:
        log(f"  b=8 FAILED: {e!r}")

    # Summary
    log("\n" + "=" * 70)
    log("Summary (b, #possible, #nonzero)")
    log("=" * 70)
    for b in sorted(results):
        r = results[b]
        log(f"  b={b}: possible = {r['p112']}, nonzero = {r['nonzero']}"
            + (f", ZEROS: {r['zeros']}" if r['zeros'] else "  (FULLY DENSE)"))

    with open('/home/agent/projects/beta-prime/code/day132_density/output.txt', 'w') as fp:
        fp.write('\n'.join(log_lines))
    log("\nSaved to /home/agent/projects/beta-prime/code/day132_density/output.txt")


if __name__ == '__main__':
    main()
