"""Route 1: Search for a recursion Psi(e_2^{b+1}) = R(Psi(e_2^b)).

Because T is falling-factorial substitution, T(fg) != T(f)T(g). So
Psi is very much not multiplicative. But maybe there's a top-weight
identity, or a low-order-perturbed one.

Strategy:
 (a) Compute Psi(e_2^b) fully (all weights, not just top) for b=0..5.
     Ask: is there an operator R (a differential/multiplication operator
     in E1,E2,E3, allowed to lower weight) with
        Psi(e_2^{b+1}) = R(Psi(e_2^b)).
 (b) If R is not obvious, restrict to top weight. Look for a linear operator
     L on the (1,1,2)-weight-b subspace whose matrix in the E-basis matches
     the b -> b+1 transition.
 (c) Cross-check: an operator with (i) weight +1, and (ii) diagonalizable
     with eigenvalues matching top row entries, would be strong evidence.
"""
import sys, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import (reduce_y, falling, apply_S, apply_T_then_S,
                 antisym_orbit, tau_deg, top_tau,
                 s, y, t, u1, u2, u3)
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, list_top_weight_coeffs,
                                 e1_u, e2_u, e3_u, E1, E2, E3,
                                 weight_of_e_monom, max_weight)

from sympy import (symbols, expand, Poly, Integer, S, factor, simplify,
                    Rational, factorial, Symbol, diff)


def compute_full_psi_e(b, cache={}):
    if b in cache:
        return cache[b]
    psi_u = Psi_direct(e2_u**b)
    cache[b] = sym_to_ebasis_direct(psi_u)
    return cache[b]


def poly_dict_E(expr):
    expr = expand(expr)
    if expr == 0:
        return {}
    p = Poly(expr, E1, E2, E3)
    return {m: c for m, c in p.as_dict().items() if c != 0}


def print_by_weight(expr, title=""):
    if title:
        print(f"--- {title} ---")
    d = poly_dict_E(expr)
    by_w = {}
    for m, c in d.items():
        w = weight_of_e_monom(*m)
        by_w.setdefault(w, []).append((m, c))
    for w in sorted(by_w.keys(), reverse=True):
        print(f"  weight {w}:")
        for m, c in sorted(by_w[w]):
            print(f"    E1^{m[0]} E2^{m[1]} E3^{m[2]}: {c}")


def top_weight(expr, w):
    return top_weight_part(expr, w)


def main():
    print("=" * 70)
    print("Route 1: Look for a recursion Psi(e_2^{b+1}) = R(Psi(e_2^b))")
    print("=" * 70)

    # Compute Psi(e_2^b) for b=0..5.
    Psi_e = {}
    for b in range(0, 6):
        t0 = time.time()
        psi_u = Psi_direct(e2_u**b) if b > 0 else Psi_direct(Integer(1))
        Psi_e[b] = sym_to_ebasis_direct(psi_u)
        print(f"b={b}: max weight = {max_weight(Psi_e[b])}, "
              f"time {time.time()-t0:.1f}s")

    # First: display FULL Psi(e_2^b) for b=0..3 by weight-graded pieces.
    for b in range(0, 4):
        print(f"\n\n===== Psi(e_2^{b}) full =====")
        print_by_weight(Psi_e[b])

    # Now test candidate operators R on TOP-WEIGHT parts.
    # Idea: try R = a*E2 + b*E1^2 + c*E1*derivations + ... etc.
    # Guess motivated by: Psi(e_2)^top = E2 - E1  (let's check).
    print("\n\n===== Guess: R takes top(Psi(e_2^b)) to top(Psi(e_2^{b+1})) =====")
    tops = {b: top_weight(Psi_e[b], b) for b in range(0, 6)}
    for b in range(6):
        print(f"  top(Psi(e_2^{b})) = {tops[b]}")

    # Now test various candidate operators R (weight +1).
    # Note: multiplication by E1, E2 raises weight by 1; E3 raises by 2.
    # Differentiation d/dEi lowers weight by w(Ei).
    # A weight-preserving operator times a weight-1 multiplier can also work.
    #
    # First, easy check: R = c * E1  (mult by E1).
    # tops[b+1] / tops[b] should be c * E1 if this holds.
    print("\n\n===== Test: does tops[b+1] / tops[b] equal a fixed operator? =====")
    for b in range(1, 5):
        num = expand(tops[b+1])
        den = expand(tops[b])
        # Try polynomial division
        q, r = Poly(num, E1, E2, E3).div(Poly(den, E1, E2, E3))
        print(f"  b={b}: q = {q.as_expr()}, remainder = {r.as_expr()}")

    # Very unlikely to divide cleanly. But let's try to fit a LINEAR operator
    # on the (1,1,2)-weight-b + weight-(b+1) spaces.
    # Basis for weight-b monomials in E1,E2,E3: mono_basis(b).
    # Operator with weight +1 mapping weight-b -> weight-(b+1) has matrix.
    # Number of degrees of freedom: dim(w=b) * dim(w=b+1) ??? too much.
    # Instead, constrain the operator to be a FIRST-ORDER differential operator
    #    R = sum_{i,j} c_{ij} * E_i * (d/dE_j)  (multiplicative-derivative)
    # plus multiplication operators.
    # This is 3 mult ops + 9 E_i d/dE_j = 12 parameters, with weight +1 constraint:
    # E1*I:  weight +1 OK
    # E2*I:  weight +1 OK
    # E3*(d/dE_i)*(1/E_i?)... hmm
    # let's simplify: weight-1 first-order diff op:
    #   c1 * E1
    #   c2 * E2
    #   c3 * E1 * E1 * d/dE1  (weight = 2+1-1 = 2  NO)
    # We need weight of monomial R to be +1.
    # Weight(E_a * (d/dE_b)) = w(E_a) - w(E_b).
    # For +1: (a,b) in {(1,*): a-b=? for a=1: w(E1)=1, need w(E_b)=0 — none}.
    #   (2,1): 1-1=0. no.
    #   (2,2): 0. no.  Hmm no first-order op raises weight by exactly 1
    #   unless we allow degree>1 monomial times d/dE.
    # Try monomials of degree 2 times d/dE: e.g. E1^2 d/dE1 has weight 2-1=1. YES.
    # Also E1 E2 d/dE1 (w=2-1=1), E1 E2 d/dE2 (w=2-1=1),
    # E1 E3 d/dE3 (w=1+2-2=1), E2^2 d/dE1 (w=2-1=1),
    # E2^2 d/dE2 (w=2-1=1), E2 E3 d/dE3 (w=1+2-2=1),
    # E3 d/dE1 (w=2-1=1), E3 d/dE2 (w=2-1=1),
    # E1 * (identity)  -- mult by E1
    # E2 * (identity)  -- mult by E2
    #
    # Second-order diff ops of weight +1:
    #   E3 d^2/dE1 dE2 has weight 2 - 1 - 1 = 0. no.
    #   E1 E3 d^2/... — too many. Start with first-order first.
    #
    # Build candidate ansatz: sum_j c_j * B_j where B_j = weight-1 mono-deriv ops.
    # Then require R(tops[b]) = tops[b+1] for b = 0..4, giving overdetermined linear system.

    # Basis of weight-1 first-order operators (mult and mult+deriv):
    op_basis = []
    op_names = []
    E_vars = (E1, E2, E3)
    E_weights = (1, 1, 2)
    # multiplication ops with weight 1: E1, E2
    op_basis.append(('mult', E1))
    op_names.append('*E1')
    op_basis.append(('mult', E2))
    op_names.append('*E2')
    # E_a * (d/dE_b) with weight w(E_a)-w(E_b)=1: need w_a - w_b = 1
    # (1,0) impossible; (E_a of weight w_a > 1, deriv of weight 0)? no.
    # Basic first-order diff: E_a d/dE_b:
    #   E2 d/dE1: w = 1-1 = 0. NO.
    # We need degree(E)_a - w(E_b) = 1 in the multiplier * deriv.
    # Actually "E_a * d/dE_b" has weight w(E_a) - w(E_b) as an operator on E-monomials.
    # For weight +1: possibilities (a,b): w_a - w_b = 1
    #   (E1, none since no weight 0)
    #   (E3, E1): w = 2 - 1 = 1  YES
    #   (E3, E2): w = 2 - 1 = 1  YES
    # OK, so first-order "linear multiplier" deriv ops:
    op_basis.append(('deriv', (E3, E1)))
    op_names.append('E3*d/dE1')
    op_basis.append(('deriv', (E3, E2)))
    op_names.append('E3*d/dE2')
    # Degree-2 multiplier * derivative:
    # E_a E_b * d/dE_c with weight = w_a + w_b - w_c = 1
    # (a,b,c) with w_a+w_b-w_c=1:
    #   (1,1,1): 1+1-1=1 YES  E1^2 d/dE1, E1 E2 d/dE1, E2^2 d/dE1, ...
    #     -- but wait E1 E1 = E1^2 etc. Let's enumerate:
    for a in range(3):
        for b in range(a, 3):
            for c in range(3):
                w_op = E_weights[a] + E_weights[b] - E_weights[c]
                if w_op == 1:
                    op_basis.append(('deriv2', (E_vars[a], E_vars[b], E_vars[c])))
                    op_names.append(f"{E_vars[a]}*{E_vars[b]}*d/d{E_vars[c]}")

    print(f"\n\nBasis of weight-1 op candidates: {len(op_basis)}")
    for n in op_names:
        print(f"  {n}")

    def apply_op(op, expr):
        kind = op[0]
        if kind == 'mult':
            return expand(op[1] * expr)
        elif kind == 'deriv':
            mult, wrt = op[1]
            return expand(mult * diff(expr, wrt))
        elif kind == 'deriv2':
            m1, m2, wrt = op[1]
            return expand(m1 * m2 * diff(expr, wrt))

    # Set up linear system: sum c_j * B_j(tops[b]) = tops[b+1] for b=0..4
    # Unknowns: c_j (one per op).  We equate coefficients of each E-monomial.
    from sympy import zeros, Matrix, linsolve, symbols as sym_symbols
    coeffs_syms = sym_symbols('c0:%d' % len(op_basis))

    equations = []
    for b in range(0, 5):
        lhs = Integer(0)
        for cj, oj in zip(coeffs_syms, op_basis):
            lhs += cj * apply_op(oj, tops[b])
        rhs = tops[b+1]
        eq = expand(lhs - rhs)
        d = poly_dict_E(eq)
        for m, c in d.items():
            equations.append(c)

    print(f"\n# equations: {len(equations)}, # unknowns: {len(coeffs_syms)}")
    sol = linsolve(equations, coeffs_syms)
    print(f"Solution set: {sol}")


if __name__ == '__main__':
    main()
