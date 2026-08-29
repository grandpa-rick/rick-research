"""STEP 0: Empirical baseline for sub_1[b] := Ψ(e_2^b)|_{weight = b-1}.

For b = 2..8:
  - Compute Ψ_b directly.
  - Extract sub_1[b] = weight-(b-1) component.
  - List support: which (x_1, x_2, x_3) with x_1 + x_2 + 2 x_3 = b - 1
    have nonzero coefficient.
  - Signs and coefficient values.
  - Compare to A002620(b+1) = floor((b+1)^2 / 4) full-density prediction.
"""
import sys, time
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from lib import s, y, t, u1, u2, u3
from task1_psi_e2_b5_b6 import (Psi_direct, sym_to_ebasis_direct,
                                 top_weight_part, e1_u, e2_u, e3_u,
                                 E1, E2, E3, weight_of_e_monom, count_p112,
                                 list_top_weight_coeffs)

from sympy import Poly, Integer, expand


def sub_k_part(expr_E, target_weight):
    """Return the (1,1,2)-weight = target_weight component."""
    expr_E = expand(expr_E)
    if expr_E == 0:
        return Integer(0)
    p = Poly(expr_E, E1, E2, E3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if weight_of_e_monom(i, j, k) == target_weight:
            out += coeff * E1**i * E2**j * E3**k
    return out


def list_weight_coeffs(expr_E, target_weight):
    expr_E = expand(expr_E)
    p = Poly(expr_E, E1, E2, E3)
    d = p.as_dict()
    out = []
    # iterate all triples (x1, x2, x3) with x1 + x2 + 2*x3 = target_weight
    for x3 in range(target_weight // 2 + 1):
        for x2 in range(target_weight - 2*x3 + 1):
            x1 = target_weight - 2*x3 - x2
            if x1 < 0:
                continue
            key = (x1, x2, x3)
            c = d.get(key, Integer(0))
            out.append((key, c))
    return out


def main():
    log_lines = []
    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 70)
    log("STEP 0: sub_1[b] := Ψ(e_2^b)|_{weight = b-1}, for b = 2..8")
    log("=" * 70)

    for b in range(2, 9):
        t0 = time.time()
        psi_u = Psi_direct(e2_u**b)
        t1 = time.time()
        psi_e = sym_to_ebasis_direct(psi_u)
        t2 = time.time()
        log(f"\n--- b = {b} (Psi t={t1-t0:.2f}s, sym→E t={t2-t1:.2f}s) ---")

        sub1 = sub_k_part(psi_e, b - 1)
        expected_count = count_p112(b - 1)
        rows = list_weight_coeffs(psi_e, b - 1)
        nonzero = [(k, c) for k, c in rows if c != 0]
        log(f"  |allowed triples (x1+x2+2*x3 = {b-1})| = {expected_count}")
        log(f"  |nonzero coefficients|               = {len(nonzero)}")

        # Sign pattern analysis
        signs = set()
        for (x1, x2, x3), c in nonzero:
            signs.add(1 if c > 0 else -1)
        log(f"  distinct signs = {signs}")

        # Also check candidate sign formula (-1)^{b - x2 - x3} (extrapolating from tops[b])
        mismatches_A = []
        # and (-1)^{b - 1 - x2 - x3} (top-weight formula at b-1 instead of b)
        mismatches_B = []
        for (x1, x2, x3), c in nonzero:
            s_pred_A = 1 if ((b - x2 - x3) % 2 == 0) else -1
            s_pred_B = 1 if ((b - 1 - x2 - x3) % 2 == 0) else -1
            s_act = 1 if c > 0 else -1
            if s_pred_A != s_act:
                mismatches_A.append(((x1, x2, x3), c, s_pred_A))
            if s_pred_B != s_act:
                mismatches_B.append(((x1, x2, x3), c, s_pred_B))
        log(f"  sign fit (-1)^{{b-x2-x3}}   mismatches: {len(mismatches_A)}")
        log(f"  sign fit (-1)^{{b-1-x2-x3}} mismatches: {len(mismatches_B)}")

        # Print the actual coefficient table
        log(f"  Weight-{b-1} coefficient table:")
        for (x1, x2, x3), c in rows:
            marker = "  <-- ZERO" if c == 0 else ""
            log(f"    E1^{x1} E2^{x2} E3^{x3}: {c}{marker}")

    with open('/home/agent/projects/beta-prime/code/day134_subtop/step0_output.txt', 'w') as fp:
        fp.write('\n'.join(log_lines))
    log("\nSaved to step0_output.txt")


if __name__ == '__main__':
    main()
