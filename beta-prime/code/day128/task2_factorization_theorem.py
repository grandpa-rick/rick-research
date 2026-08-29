"""Day 128 — Task 2: Re-verify Day 125 factorization theorem
using CORRECTED reduce_y library at day127/lib.py.

Theorem:
    Ψ(e_1^{a1} e_2^{a2} e_3^{a3}) = [e_1 − 2a2 − 3a3 − 3]_{a1}
                                    · Ψ(e_2^{a2})(u − a3)
                                    · Ψ(e_3^{a3})

Corollary:
    Ψ(e_3^c) = ∏_{i=1..3} [u_i]_c   (falling factorials in each u_i)

Lemma A (e_3-shift):
    Ψ(f · e_3^c) = Ψ(f)(u − c) · Ψ(e_3^c)

Lemma B (e_1-shift):
    Ψ(e_1^a · g) = [e_1 − deg_u(g) − 3]_a · Ψ(g)

Meaning of "Ψ(f)(u − c)" — shift every u_i to (u_i − c) in Ψ(f).
Since Ψ(f) is symmetric in u_1,u_2,u_3 (equivalently, in E1,E2,E3
after conversion), this shift is well-defined.

deg_u(g) — total degree of g in u_1,u_2,u_3 (uniform degree since g
is a product of elementary symmetric polynomials).
"""
import sys
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
from lib import (reduce_y, falling, apply_S, apply_T_then_S,
                 antisym_orbit, tau_deg, top_tau,
                 s, y, t, u1, u2, u3)

from sympy import symbols, expand, Poly, Integer, S, prod, factor, sympify, together
import random

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


def Psi(f):
    num = expand(T_u(expand(f * V)))
    q, r = Poly(num, u1, u2, u3).div(Poly(V, u1, u2, u3))
    if r.as_expr() != 0:
        raise RuntimeError(f"Nonzero remainder in Ψ: {r.as_expr()}")
    return expand(q.as_expr())


def shift_u(P, c):
    """Apply u_i -> u_i - c to a polynomial in u_i's."""
    return expand(P.subs({u1: u1 - c, u2: u2 - c, u3: u3 - c},
                         simultaneous=True))


def falling_expr(x, n):
    return expand(prod([x - i for i in range(n)])) if n > 0 else Integer(1)


def sym_deg(a1, a2, a3):
    """Total u-degree of e_1^a1 e_2^a2 e_3^a3."""
    return a1 + 2*a2 + 3*a3


# ------------------------- Sub-task (c) corollary -----------------------------
def verify_corollary(c):
    """Ψ(e_3^c) ?= [u1]_c [u2]_c [u3]_c"""
    lhs = Psi(e3_u**c)
    rhs = expand(falling(u1, c) * falling(u2, c) * falling(u3, c))
    diff = expand(lhs - rhs)
    return diff == 0, lhs, rhs, diff


# ------------------------- Sub-task (a) Lemma A -------------------------------
def verify_lemmaA(f, c):
    """Ψ(f · e_3^c) ?= Ψ(f)(u − c) · Ψ(e_3^c)"""
    lhs = Psi(expand(f * e3_u**c))
    Psi_f = Psi(f)
    Psi_e3c = Psi(e3_u**c)
    rhs = expand(shift_u(Psi_f, c) * Psi_e3c)
    diff = expand(lhs - rhs)
    return diff == 0, diff


# ------------------------- Sub-task (b) Lemma B -------------------------------
def verify_lemmaB(a, g, deg_g):
    """Ψ(e_1^a · g) ?= [e_1 − deg_u(g) − 3]_a · Ψ(g)
    where e_1 here means the symmetric function e_1 = u1+u2+u3."""
    lhs = Psi(expand(e1_u**a * g))
    Psi_g = Psi(g)
    factor_a = falling_expr(e1_u - deg_g - 3, a)
    rhs = expand(factor_a * Psi_g)
    diff = expand(lhs - rhs)
    return diff == 0, diff


# ------------------------- Sub-task (d) full factorization ---------------------
def verify_full_factorization(a1, a2, a3):
    """Ψ(e_1^a1 e_2^a2 e_3^a3)
        ?= [e_1 - 2a2 - 3a3 - 3]_{a1} · Ψ(e_2^{a2})(u − a3) · Ψ(e_3^{a3})"""
    f = expand(e1_u**a1 * e2_u**a2 * e3_u**a3)
    lhs = Psi(f)
    factor_a1 = falling_expr(e1_u - 2*a2 - 3*a3 - 3, a1)
    Psi_e2a2 = Psi(e2_u**a2)
    Psi_e2a2_shift = shift_u(Psi_e2a2, a3)
    Psi_e3a3 = Psi(e3_u**a3)
    rhs = expand(factor_a1 * Psi_e2a2_shift * Psi_e3a3)
    diff = expand(lhs - rhs)
    return diff == 0, diff


def main():
    log_lines = []
    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 70)
    log("Task 2: Re-verify Day 125 factorization theorem")
    log("=" * 70)

    total_pass = 0
    total_fail = 0

    # ------------------- (c) Corollary -----------------------------
    log("\n----- (c) Corollary: Ψ(e_3^c) = ∏ [u_i]_c  for c = 1..4 -----")
    for c in range(1, 5):
        ok, lhs, rhs, diff = verify_corollary(c)
        status = "PASS" if ok else "FAIL"
        log(f"  c = {c}: {status}")
        if not ok:
            log(f"    diff = {diff}")
            total_fail += 1
        else:
            total_pass += 1

    # ------------------- (a) Lemma A -------------------------------
    log("\n----- (a) Lemma A: Ψ(f · e_3^c) = Ψ(f)(u−c) · Ψ(e_3^c) -----")
    f_list = [
        ("e_1", e1_u),
        ("e_2", e2_u),
        ("e_1·e_2", e1_u * e2_u),
        ("e_2^2", e2_u**2),
    ]
    for name, f in f_list:
        for c in (1, 2, 3):
            ok, diff = verify_lemmaA(f, c)
            status = "PASS" if ok else "FAIL"
            log(f"  f = {name:<8}  c = {c}: {status}")
            if not ok:
                log(f"    diff = {diff}")
                total_fail += 1
            else:
                total_pass += 1

    # ------------------- (b) Lemma B -------------------------------
    log("\n----- (b) Lemma B: Ψ(e_1^a · g) = [e_1 − deg_u(g) − 3]_a · Ψ(g) -----")
    g_list = [
        ("e_2",       e2_u,       2),   # deg_u(e_2) = 2
        ("e_3",       e3_u,       3),
        ("e_2·e_3",   e2_u*e3_u,  5),
    ]
    for name, g, deg_g in g_list:
        for a in (1, 2, 3):
            ok, diff = verify_lemmaB(a, g, deg_g)
            status = "PASS" if ok else "FAIL"
            log(f"  a = {a}  g = {name:<8} (deg_u = {deg_g}): {status}")
            if not ok:
                log(f"    diff = {diff}")
                total_fail += 1
            else:
                total_pass += 1

    # ------------------- (d) Full factorization on random monomials --------
    log("\n----- (d) Full factorization on 5+ random (a1,a2,a3) with a1+a2+a3 ≤ 4 -----")
    random.seed(42)
    triples = []
    for a1 in range(5):
        for a2 in range(5):
            for a3 in range(5):
                if a1 + a2 + a3 <= 4 and a1 + a2 + a3 >= 1:
                    triples.append((a1, a2, a3))
    random.shuffle(triples)
    # take a diverse set: 5 randomly chosen, ensure coverage of edge cases
    tested = set()
    chosen = []
    # First force some interesting ones
    for req in [(1,1,1),(2,1,0),(1,0,2),(0,2,1),(1,2,1)]:
        if req in triples:
            chosen.append(req)
            tested.add(req)
    for tr in triples:
        if len(chosen) >= 8:
            break
        if tr not in tested:
            chosen.append(tr)
            tested.add(tr)

    for (a1, a2, a3) in chosen:
        ok, diff = verify_full_factorization(a1, a2, a3)
        status = "PASS" if ok else "FAIL"
        log(f"  (a1,a2,a3) = ({a1},{a2},{a3})  [sum = {a1+a2+a3}]: {status}")
        if not ok:
            log(f"    diff = {diff}")
            total_fail += 1
        else:
            total_pass += 1

    log("\n" + "=" * 70)
    log(f"TOTAL: {total_pass} PASS, {total_fail} FAIL")
    log("=" * 70)

    with open('/home/agent/projects/beta-prime/code/day128/task2_output.txt', 'w') as fp:
        fp.write('\n'.join(log_lines))
    log("\nSaved to task2_output.txt")


if __name__ == '__main__':
    main()
