"""Day 135 — verify the Ψ_b-GLOBAL uniform sign conjecture at EVERY weight slice.

Conjecture (crown insight #1, Day 134 dream):
    Every nonzero coefficient in Ψ(e_2^b) has sign (-1)^{x_1 + x_3}.
    (Not just top-weight and sub-top — GLOBAL.)

Days 133 (k=0), 134 (k=1), 135 (k=2) established k = 0, 1, 2.
This script tests EVERY slice k = 0, 1, ..., b for each b, in one pass.

Also records support cardinalities #{allowed} vs #{nonzero} per slice, to
check the conjecture that supports are always full (density at all weights).
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
    list_top_weight_coeffs,
)

from sympy import Poly, Integer, expand


B_MAX = 10
B_MIN = 2
TIME_BUDGET = 1500


def main():
    log_lines = []
    def log(*args):
        line = ' '.join(str(a) for a in args)
        print(line, flush=True)
        log_lines.append(line)

    log("=" * 78)
    log("Day 135: FULL Ψ_b-global uniform-sign test — every slice, every b.")
    log("Conjecture: sign(coeff at E_1^x1 E_2^x2 E_3^x3) == (-1)^{x1+x3}")
    log("            for every nonzero coefficient of Ψ(e_2^b).")
    log("=" * 78)

    t_start = time.time()
    per_b_summary = []  # (b, total_nonzero, total_mismatch, per-slice list)
    grand_mismatches = []

    for b in range(B_MIN, B_MAX + 1):
        if time.time() - t_start > TIME_BUDGET:
            log(f"\n[time budget exhausted, stopping at b={b-1}]")
            break

        t0 = time.time()
        psi_u = Psi_direct(e2_u**b)
        t1 = time.time()
        psi_e = sym_to_ebasis_direct(psi_u)
        t2 = time.time()

        # Bucket by weight
        p = Poly(expand(psi_e), E1, E2, E3)
        by_weight = {}  # weight -> list[(i,j,k, coeff)]
        for monom, coeff in p.as_dict().items():
            i, j, k = monom
            w = weight_of_e_monom(i, j, k)
            by_weight.setdefault(w, []).append((i, j, k, coeff))

        log(f"\n--- b = {b}  (Psi = {t1-t0:.2f}s, sym→E = {t2-t1:.2f}s) ---")
        log(f"  {'slice':>5}  {'weight':>6}  {'#allowed':>8}  "
            f"{'#nonzero':>8}  {'#zero':>5}  {'#mismatch':>9}  A002620")

        total_nonzero = 0
        total_mismatch = 0
        per_slice = []

        max_slice_shown = b  # we look at k = 0..b
        for k in range(0, max_slice_shown + 1):
            w = b - k  # weight of the slice
            if w < 0:
                break
            # allowed triples with weight w, using count_p112(w) helper
            allowed = count_p112(w)
            entries = by_weight.get(w, [])
            nonzero = len(entries)
            mismatches = 0
            for (i, j, kk, c) in entries:
                exp_sign = 1 if (i + kk) % 2 == 0 else -1
                act_sign = 1 if c > 0 else -1
                if exp_sign != act_sign:
                    mismatches += 1
                    grand_mismatches.append((b, k, (i, j, kk), c, exp_sign))
            zero_count = allowed - nonzero
            per_slice.append((k, w, allowed, nonzero, zero_count, mismatches))
            log(f"  sub_{k:<1}  {w:>6}  {allowed:>8}  {nonzero:>8}  "
                f"{zero_count:>5}  {mismatches:>9}  A002620({b+2-k})={count_p112(w) if False else ((w+2)*(w+2))//4}")
            total_nonzero += nonzero
            total_mismatch += mismatches

        per_b_summary.append((b, total_nonzero, total_mismatch, per_slice))

    log("\n" + "=" * 78)
    log("SUMMARY")
    log("=" * 78)
    log(f"  {'b':>3}  {'total nonzero':>13}  {'total mismatch':>14}")
    for b, tnz, tmis, _ in per_b_summary:
        log(f"  {b:>3}  {tnz:>13}  {tmis:>14}")

    total_all_mismatch = sum(x[2] for x in per_b_summary)
    if total_all_mismatch == 0:
        log("")
        log("VERDICT: YES — Ψ_b-global uniform sign (-1)^{x1+x3} holds")
        log(f"         across EVERY slice, EVERY nonzero coefficient,")
        log(f"         for b = {B_MIN}..{per_b_summary[-1][0]}.")
    else:
        log(f"\nVERDICT: FAILURE — {total_all_mismatch} mismatch(es) total.")
        for row in grand_mismatches[:20]:
            b, k, xs, c, exp = row
            log(f"  b={b} k={k}: E1^{xs[0]} E2^{xs[1]} E3^{xs[2]}: coeff={c}, expected sign={exp:+d}")

    # Support density observation
    log("\n" + "-" * 78)
    log("Support cardinality per slice (density check):")
    log("  A002620(m) = floor(m^2/4). If sub_k[b] has full support, #nonzero == A002620(b+2-k).")
    log("")
    log(f"  {'b':>3}  " + "  ".join(f"sub_{k}" for k in range(11)))
    for b, _, _, per_slice in per_b_summary:
        row = [f"{b:>3}  "]
        for k in range(11):
            if k < len(per_slice):
                _, _, allowed, nonzero, _, _ = per_slice[k]
                marker = "="  if nonzero == allowed else "!"
                row.append(f"{nonzero}/{allowed}{marker}")
            else:
                row.append("  ---  ")
        log("  ".join(row))

    out_path = '/home/agent/projects/beta-prime/code/day135_sub2_sign/verify_all_slices.txt'
    with open(out_path, 'w') as fp:
        fp.write('\n'.join(log_lines))
    log(f"\nSaved log to {out_path}")


if __name__ == '__main__':
    main()
