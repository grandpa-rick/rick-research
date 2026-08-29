"""Day 135 — verify uniform sign conjecture for sub_2[b].

Conjecture (crown insight #1, Day 134 dream):
    Every nonzero coefficient in sub_k[b] has sign (-1)^{x_1 + x_3}
    for all k. Days 133/134 established k = 0 and k = 1.
    Here we test k = 2 empirically for b = 2, 3, ..., up to b = 10
    (or as far as time permits).

For each b:
    * Compute Ψ_b = Ψ(e_2^b) via the direct route (day128/task1).
    * Convert to E-basis.
    * Extract sub_2[b] = weight-(b-2) component with weight(E_i)=(1,1,2).
    * Enumerate every allowed monomial with x_1+x_2+2 x_3 = b-2.
    * Report coefficient, expected sign (-1)^{x_1+x_3}, match/no-match.
    * Flag any zero coefficients (support holes).
"""

import sys
import time

sys.path.insert(0, '/home/agent/projects/beta-prime/code/day127')
sys.path.insert(0, '/home/agent/projects/beta-prime/code/day128')

from task1_psi_e2_b5_b6 import (
    Psi_direct,
    sym_to_ebasis_direct,
    e2_u,
    E1, E2, E3,
    weight_of_e_monom,
    count_p112,
    list_top_weight_coeffs,   # works for any target weight (i+j+2k = target)
)

from sympy import Poly, Integer, expand


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

B_MAX = 10          # ambitious ceiling
B_MIN = 2           # sub_2 requires b >= 2 (weight b-2 >= 0)
TIME_BUDGET = 900   # abort further b's if cumulative time exceeds this


def sub_k_part(psi_e, target_weight):
    """Return the weight = target_weight component (weight = i+j+2k)."""
    psi_e = expand(psi_e)
    if psi_e == 0:
        return Integer(0)
    p = Poly(psi_e, E1, E2, E3)
    out = Integer(0)
    for monom, coeff in p.as_dict().items():
        i, j, k = monom
        if weight_of_e_monom(i, j, k) == target_weight:
            out += coeff * E1**i * E2**j * E3**k
    return out


def main():
    log_lines = []

    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 78)
    log("Day 135: sub_2[b] := Ψ(e_2^b)|_{weight = b-2}, uniform-sign test")
    log("Conjecture:  sign(coeff at E_1^x1 E_2^x2 E_3^x3) == (-1)^{x1 + x3}")
    log("=" * 78)

    grand_summary = []  # (b, n_allowed, n_nonzero, n_zero, n_mismatch, exceptions)
    all_exceptions = []
    t_start = time.time()

    for b in range(B_MIN, B_MAX + 1):
        if time.time() - t_start > TIME_BUDGET:
            log(f"\n[time budget exhausted after b={b-1}; stopping]")
            break

        t0 = time.time()
        psi_u = Psi_direct(e2_u**b)
        t1 = time.time()
        psi_e = sym_to_ebasis_direct(psi_u)
        t2 = time.time()

        target_w = b - 2
        rows = list_top_weight_coeffs(psi_e, target_w)  # includes zero entries
        n_allowed = len(rows)  # equals count_p112(b-2)
        expected_count = count_p112(target_w)
        assert n_allowed == expected_count, (n_allowed, expected_count)

        nonzero = [(k, c) for k, c in rows if c != 0]
        zero_rows = [(k, c) for k, c in rows if c == 0]

        mismatches = []
        for (x1, x2, x3), c in nonzero:
            expected_sign = 1 if (x1 + x3) % 2 == 0 else -1
            actual_sign = 1 if c > 0 else -1
            if expected_sign != actual_sign:
                mismatches.append(((x1, x2, x3), c, expected_sign))

        log(f"\n--- b = {b} (target weight = {b - 2}) ---")
        log(f"  timing:  Psi = {t1-t0:.2f}s, sym→E = {t2-t1:.2f}s")
        log(f"  |allowed triples (x1+x2+2 x3 = {b-2})| = {n_allowed}"
            f"  (A002620({b}) = floor({b}^2/4) = {(b*b)//4})")
        log(f"  |nonzero coefficients|                 = {len(nonzero)}")
        log(f"  |zero coefficients (support holes)|    = {len(zero_rows)}")
        log(f"  |sign mismatches|                      = {len(mismatches)}")

        log(f"  full sub_2[{b}] coefficient table:")
        log(f"    {'x1':>3} {'x2':>3} {'x3':>3}   {'coefficient':>18}"
            f"   {'expected':>8}   {'match?':>7}")
        for (x1, x2, x3), c in rows:
            if c == 0:
                exp_sign_str = f"{'(±1)':>8}"
                match_str = "ZERO"
            else:
                exp_sign = 1 if (x1 + x3) % 2 == 0 else -1
                act_sign = 1 if c > 0 else -1
                exp_sign_str = f"{exp_sign:+d}".rjust(8)
                match_str = "OK" if exp_sign == act_sign else "*** MISMATCH ***"
            log(f"    {x1:>3} {x2:>3} {x3:>3}   {str(c):>18}   "
                f"{exp_sign_str}   {match_str:>7}")

        if mismatches:
            log("  !!! MISMATCHES FOR b = {} !!!".format(b))
            for (x1, x2, x3), c, exp_sign in mismatches:
                log(f"    E1^{x1} E2^{x2} E3^{x3}: coeff={c}, expected sign={exp_sign:+d}")
                all_exceptions.append((b, (x1, x2, x3), c, exp_sign))

        grand_summary.append(
            (b, n_allowed, len(nonzero), len(zero_rows), len(mismatches))
        )

    log("\n" + "=" * 78)
    log("SUMMARY")
    log("=" * 78)
    log(f"  {'b':>3}  {'#allowed':>9}  {'#nonzero':>9}  {'#zero':>6}  "
        f"{'#mismatch':>10}  {'A002620(b)':>10}")
    for (b, n_allowed, n_nz, n_zero, n_mis) in grand_summary:
        log(f"  {b:>3}  {n_allowed:>9}  {n_nz:>9}  {n_zero:>6}  "
            f"{n_mis:>10}  {(b*b)//4:>10}")

    total_mismatch = sum(row[4] for row in grand_summary)
    log("")
    if total_mismatch == 0:
        log("VERDICT: YES — uniform sign (-1)^{x1+x3} confirmed for sub_2[b]")
        log(f"         across every nonzero coefficient for b = {B_MIN}..{grand_summary[-1][0]}.")
    else:
        log(f"VERDICT: FAILURE — {total_mismatch} sign mismatch(es) found.")
        for row in all_exceptions:
            b, xs, c, exp = row
            log(f"    b={b}  E1^{xs[0]} E2^{xs[1]} E3^{xs[2]}: coeff={c}, "
                f"expected sign={exp:+d}")

    out_path = '/home/agent/projects/beta-prime/code/day135_sub2_sign/verify_sub2_sign.txt'
    with open(out_path, 'w') as fp:
        fp.write('\n'.join(log_lines))
    log(f"\nSaved log to {out_path}")

    return grand_summary, all_exceptions


if __name__ == '__main__':
    main()
