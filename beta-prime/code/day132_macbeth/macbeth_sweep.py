"""Day 132 — MacBeth support-variety sweep.

Rick knows Ψ(e_2^b) has zero top-weight cancellations for b ≤ 6.
MacBeth's question: does zero-cancellation extend to
   Ψ(e_2^a · e_1^c)   and   Ψ(e_2^a · e_3^c) ?

We compute both DIRECTLY (via Ψ = T(f·V)/V) and via the Day 125
factorization theorem, verifying agreement, then report:
   - #possible top-weight e-monomials (p_{1,1,2}(w))
   - #nonzero top-weight monomials in the E-basis expansion
   - #cancellations = possible − nonzero
   - Schur rank of the top-weight polynomial (as a symmetric function
     obtained by substituting E_i → e_i(x_1,x_2,x_3), then expanding in
     Schurs). Rank = number of distinct Schur functions with nonzero coeff.

By the (1,1,2)-weighting on the E-basis (deg E_1 = 1, deg E_2 = 1, deg E_3 = 2),
the top weight of Ψ(e_2^a · e_1^c) is a + c (weight of e_1 is 1),
and the top weight of Ψ(e_2^a · e_3^c) is a + 2c (weight of e_3 is 2).

The factorization theorem:
  Ψ(e_2^a · e_1^c) = [e_1 − 2a − 3]_c · Ψ(e_2^a)   (multiplicative in E-basis)
  Ψ(e_2^a · e_3^c) = Ψ(e_2^a)(u − c) · Ψ(e_3^c)    (u-shift then multiply)
"""
import sys, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
from lib import (reduce_y, falling, apply_S, apply_T_then_S,
                 antisym_orbit, tau_deg, top_tau,
                 s, y, t, u1, u2, u3)

from sympy import symbols, expand, Poly, Integer, S, prod, factor, Rational
from itertools import permutations

E1, E2, E3 = symbols('E1 E2 E3')

# 3 x-variables for Schur expansions
x1, x2, x3 = symbols('x1 x2 x3')
X = (x1, x2, x3)

V = (u1 - u2) * (u1 - u3) * (u2 - u3)
e1_u = u1 + u2 + u3
e2_u = u1*u2 + u1*u3 + u2*u3
e3_u = u1*u2*u3

Vx = (x1 - x2) * (x1 - x3) * (x2 - x3)
e1_x = x1 + x2 + x3
e2_x = x1*x2 + x1*x3 + x2*x3
e3_x = x1*x2*x3


# ------------------------- Ψ core --------------------------------------------

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


def Psi(f):
    """Ψ(f) = T(f·V)/V in u1,u2,u3 (exact division)."""
    num = expand(T_u(expand(f * V)))
    q, r = Poly(num, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise RuntimeError(f"Nonzero remainder in Ψ: {r.as_expr()}")
    return expand(q.as_expr())


def sym_to_ebasis(f):
    """Elementary-symmetric conversion via leading term (u1>u2>u3 lex)."""
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


def shift_u(P, c):
    return expand(P.subs({u1: u1 - c, u2: u2 - c, u3: u3 - c},
                         simultaneous=True))


def falling_expr(x, n):
    return expand(prod([x - i for i in range(n)])) if n > 0 else Integer(1)


# ------------------------- weight / top-weight utils --------------------------

def weight_of_e_monom(i, j, k):
    return i + j + 2*k


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


# ------------------------- Schur rank -----------------------------------------

def schur_mu_x(mu):
    """Ordinary Schur s_mu(x1,x2,x3) via Weyl det formula."""
    mu = list(mu) + [0] * (3 - len(mu))
    mu = mu[:3]
    exps = [mu[0] + 2, mu[1] + 1, mu[2]]
    rows = [[X[i]**exps[l] for l in range(3)] for i in range(3)]
    numer = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
             - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
             + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
    q, r = Poly(expand(numer), *X).div(Poly(expand(Vx), *X))
    if r.as_expr() != 0:
        raise ValueError(f"Schur numerator not divisible by V for mu={mu}")
    return expand(q.as_expr())


def partitions_le3(n):
    """All partitions of n with at most 3 parts, descending tuple."""
    out = []
    for a in range(n + 1):
        for b in range(a + 1):
            c = n - a - b
            if 0 <= c <= b:
                out.append((a, b, c))
    return out


def E_to_x(expr_E):
    """Substitute E_i -> e_i(x1,x2,x3), giving a symmetric polynomial in X."""
    return expand(expr_E.subs({E1: e1_x, E2: e2_x, E3: e3_x}))


def schur_expand(sym_poly_x):
    """Expand a symmetric polynomial in x1,x2,x3 in Schur basis (partitions
    with l <= 3). Returns dict {mu: coeff} for nonzero coeffs."""
    sym_poly_x = expand(sym_poly_x)
    if sym_poly_x == 0:
        return {}
    total = Poly(sym_poly_x, *X).total_degree()
    # Schurs indexed by partitions of degrees 0..total, l <= 3, descending
    schur_basis = {}
    for d in range(total + 1):
        for mu in partitions_le3(d):
            schur_basis[mu] = schur_mu_x(mu)

    # Order partitions by descending total then descending lex
    partitions_sorted = sorted(schur_basis.keys(),
                               key=lambda mu: (-sum(mu),
                                               tuple(-x for x in mu)))

    remainder = sym_poly_x
    coeffs = {}
    for mu in partitions_sorted:
        s_mu = schur_basis[mu]
        if remainder == 0:
            break
        poly_rem = Poly(remainder, *X)
        # leading monomial of s_mu is x1^mu[0] x2^mu[1] x3^mu[2] with coeff 1
        coeff = poly_rem.coeff_monomial(tuple(mu))
        if coeff != 0:
            coeffs[mu] = coeff
            remainder = expand(remainder - coeff * s_mu)
    if expand(remainder) != 0:
        raise RuntimeError(f"Schur expansion residue nonzero: {remainder}")
    return coeffs


def schur_rank(top_weight_poly_E):
    """Rank = # distinct Schur functions in expansion of top-weight polynomial
    as a symmetric polynomial (via E_i -> e_i substitution)."""
    if top_weight_poly_E == 0:
        return 0, {}
    sym = E_to_x(top_weight_poly_E)
    d = schur_expand(sym)
    return len(d), d


# ------------------------- factorized computations ---------------------------

def Psi_e2_a_via_direct(a):
    return Psi(e2_u**a)


def Psi_e3_c_direct(c):
    return Psi(e3_u**c)


def Psi_e2a_e1c_direct(a, c):
    return Psi(expand(e2_u**a * e1_u**c))


def Psi_e2a_e1c_factored(a, c, Psi_e2a):
    """[e_1 − 2a − 3]_c · Ψ(e_2^a)."""
    factor_c = falling_expr(e1_u - 2*a - 3, c)
    return expand(factor_c * Psi_e2a)


def Psi_e2a_e3c_direct(a, c):
    return Psi(expand(e2_u**a * e3_u**c))


def Psi_e2a_e3c_factored(a, c, Psi_e2a, Psi_e3c):
    """Ψ(e_2^a)(u − c) · Ψ(e_3^c)."""
    Psi_e2a_shift = shift_u(Psi_e2a, c)
    return expand(Psi_e2a_shift * Psi_e3c)


# ------------------------- main -----------------------------------------------

def analyze(psi_e, w):
    """Return (n_possible, n_nonzero, n_cancel, top_poly, rank, schur_dict)."""
    n_possible = count_p112(w)
    tw_list = list_top_weight_coeffs(psi_e, w)
    n_nonzero = sum(1 for _, c in tw_list if c != 0)
    n_cancel = n_possible - n_nonzero
    top_poly = top_weight_part(psi_e, w)
    rank, sd = schur_rank(top_poly)
    return n_possible, n_nonzero, n_cancel, top_poly, rank, sd, tw_list


def main():
    log_lines = []

    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 74)
    log("Day 132 — MacBeth sweep: Ψ(e_2^a · e_1^c) and Ψ(e_2^a · e_3^c)")
    log("=" * 74)

    # Cache Ψ(e_2^a) and Ψ(e_3^c) for reuse
    log("\nPrecomputing Ψ(e_2^a) for a = 0..4 ...")
    Psi_e2 = {}
    for a in range(5):
        t0 = time.time()
        Psi_e2[a] = Psi(e2_u**a) if a > 0 else Integer(1)
        log(f"  a={a}: {time.time()-t0:.2f}s")

    log("\nPrecomputing Ψ(e_3^c) for c = 0..2 ...")
    Psi_e3 = {}
    for c in range(3):
        t0 = time.time()
        Psi_e3[c] = Psi(e3_u**c) if c > 0 else Integer(1)
        log(f"  c={c}: {time.time()-t0:.2f}s")

    # =========== e_1 series ===========
    log("\n" + "=" * 74)
    log("SERIES 1: Ψ(e_2^a · e_1^c)   (a + c ≤ 6, a ≤ 4, c ≤ 4)")
    log("=" * 74)
    log("\nFactorization check + top-weight analysis:")

    e1_rows = []  # (a, c, w, npos, nnz, ncancel, rank)
    e1_cancels = []  # cases with cancellations

    for a in range(5):
        for c in range(5):
            if a + c > 6:
                continue
            if a == 0 and c == 0:
                continue
            # DIRECT
            t0 = time.time()
            psi_u_direct = Psi_e2a_e1c_direct(a, c)
            t_direct = time.time() - t0

            # FACTORED
            psi_u_fact = Psi_e2a_e1c_factored(a, c, Psi_e2[a])

            # Cross-check
            diff = expand(psi_u_direct - psi_u_fact)
            if diff != 0:
                log(f"  (a={a}, c={c}) FACTORIZATION MISMATCH! diff = {diff}")
                continue

            # E-basis
            psi_e = sym_to_ebasis(psi_u_direct)
            w = a + c  # top (1,1,2) weight
            w_actual = max_weight(psi_e)
            if w_actual != w:
                log(f"  (a={a}, c={c}) expected w={w}, got {w_actual}")

            npos, nnz, ncancel, top_poly, rank, sd, tw_list = analyze(psi_e, w)
            e1_rows.append((a, c, w, npos, nnz, ncancel, rank))
            log(f"  (a={a}, c={c})  w={w}: direct={t_direct:.2f}s  fact=MATCH  "
                f"|  #possible={npos}  #nonzero={nnz}  #cancel={ncancel}  rank={rank}")

            if ncancel > 0:
                e1_cancels.append((a, c, w, tw_list, top_poly, sd))

    # =========== e_3 series ===========
    log("\n" + "=" * 74)
    log("SERIES 2: Ψ(e_2^a · e_3^c)   (a + 2c ≤ 8, a ≤ 4, c ≤ 2)")
    log("=" * 74)
    log("\nFactorization check + top-weight analysis:")

    e3_rows = []
    e3_cancels = []

    for a in range(5):
        for c in range(3):
            if a + 2*c > 8:
                continue
            if a == 0 and c == 0:
                continue
            t0 = time.time()
            psi_u_direct = Psi_e2a_e3c_direct(a, c)
            t_direct = time.time() - t0

            psi_u_fact = Psi_e2a_e3c_factored(a, c, Psi_e2[a], Psi_e3[c])

            diff = expand(psi_u_direct - psi_u_fact)
            if diff != 0:
                log(f"  (a={a}, c={c}) FACTORIZATION MISMATCH! diff = {diff}")
                continue

            psi_e = sym_to_ebasis(psi_u_direct)
            w = a + 2*c
            w_actual = max_weight(psi_e)
            if w_actual != w:
                log(f"  (a={a}, c={c}) expected w={w}, got {w_actual}")

            npos, nnz, ncancel, top_poly, rank, sd, tw_list = analyze(psi_e, w)
            e3_rows.append((a, c, w, npos, nnz, ncancel, rank))
            log(f"  (a={a}, c={c})  w={w}: direct={t_direct:.2f}s  fact=MATCH  "
                f"|  #possible={npos}  #nonzero={nnz}  #cancel={ncancel}  rank={rank}")

            if ncancel > 0:
                e3_cancels.append((a, c, w, tw_list, top_poly, sd))

    # =========== Cancellation drill-down =========
    log("\n" + "=" * 74)
    log("CANCELLATION DRILL-DOWN")
    log("=" * 74)

    def dump_cancels(name, cases):
        if not cases:
            log(f"\n{name}: NO cancellations detected in the swept range.")
            return
        log(f"\n{name}: {len(cases)} case(s) with cancellations.")
        for (a, c, w, tw_list, top_poly, sd) in cases:
            log(f"\n  --- (a={a}, c={c}, w={w}) ---")
            log(f"  Top-weight polynomial: {top_poly}")
            log(f"  Full top-weight coefficient table (marking ZEROs):")
            for (i, j, k), coef in tw_list:
                mark = "  <-- ZERO" if coef == 0 else ""
                log(f"    E1^{i} E2^{j} E3^{k}: {coef}{mark}")
            zeros = [(k) for k, coef in tw_list if coef == 0]
            log(f"  Zero e-monomials: {zeros}")

    dump_cancels("e_1 series [Ψ(e_2^a · e_1^c)]", e1_cancels)
    dump_cancels("e_3 series [Ψ(e_2^a · e_3^c)]", e3_cancels)

    # =========== Summary tables ==================
    log("\n" + "=" * 74)
    log("MARKDOWN TABLES")
    log("=" * 74)

    log("\n### Series 1: Ψ(e_2^a · e_1^c)\n")
    log("| a | c | weight | #possible | #nonzero | #cancel | Schur rank |")
    log("|---|---|--------|-----------|----------|---------|------------|")
    for (a, c, w, npos, nnz, ncancel, rank) in e1_rows:
        log(f"| {a} | {c} | {w} | {npos} | {nnz} | {ncancel} | {rank} |")

    log("\n### Series 2: Ψ(e_2^a · e_3^c)\n")
    log("| a | c | weight | #possible | #nonzero | #cancel | Schur rank |")
    log("|---|---|--------|-----------|----------|---------|------------|")
    for (a, c, w, npos, nnz, ncancel, rank) in e3_rows:
        log(f"| {a} | {c} | {w} | {npos} | {nnz} | {ncancel} | {rank} |")

    # ---- Overall verdict ----
    log("\n" + "=" * 74)
    log("VERDICT")
    log("=" * 74)
    total_e1_cancel = sum(r[5] for r in e1_rows)
    total_e3_cancel = sum(r[5] for r in e3_rows)
    log(f"  e_1 series: total cancellations across sweep = {total_e1_cancel}")
    log(f"  e_3 series: total cancellations across sweep = {total_e3_cancel}")

    with open('/home/agent/projects/beta-prime/code/day132_macbeth/output.txt', 'w') as fp:
        fp.write('\n'.join(log_lines))
    log("\nSaved to /home/agent/projects/beta-prime/code/day132_macbeth/output.txt")


if __name__ == '__main__':
    main()
