"""
Day-58 Task 3 (CODE.md): Computational verification of the piecewise
pi_3' candidate produced by Day-58 PROVE.

PROVE deliverable: `proofs/2026-06-08-pi3-construction.md` claims a
26-piece (here 55-piece in v7's registry) piecewise-linear
$\\tilde\\pi_3'$ surjective up to N=10. The proof note tabled coverage
through N=10.

This script extends to N=12 and N=15 to test predictiveness:
- 100% coverage at higher N supports the conjecture (PL+integer
  registry is enough at all N).
- Anything <100% at N=15 surfaces a NEW family that needs a 56-th piece.

Output: PIECEWISE-RESULTS.md (committed to projects/code/).
"""
import sys
import time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from verify_full_v7 import (
    ALL_PI, get_image,
    enumerate_aii_n3_full, enumerate_bdi_n3,
)


def union_coverage(piece_names, N):
    """Return (coverage_count, total_BDI, union_image, BDI_set, bad_total)."""
    bdi_pts = enumerate_bdi_n3(N)
    union = set()
    bad_tot = 0
    bad_by_piece = {}
    for name in piece_names:
        img, bad, n_aii = get_image(name, N)
        union |= img
        bad_tot += bad
        bad_by_piece[name] = bad
    covered = union & bdi_pts
    return len(covered), len(bdi_pts), union, bdi_pts, bad_tot, bad_by_piece


def main():
    pieces = list(ALL_PI.keys())
    print(f"# Piecewise pi_3' verification — Day 58 Task 3")
    print(f"# {len(pieces)} pieces in the v7 registry (PROVE-produced)")
    print()
    Ns = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    rows = []
    print(f"{'N':>3} | {'|AII|':>7} | {'|BDI|':>7} | {'covered':>8} | {'coverage':>10} | {'land-in-cone violations':>26} | {'time (s)':>9}")
    print("-" * 100)
    for N in Ns:
        t0 = time.time()
        cov, total, union, bdi_set, bad_tot, _ = union_coverage(pieces, N)
        dt = time.time() - t0
        pct = 100.0 * cov / total if total else 0
        rows.append((N, total, cov, bad_tot, dt, pct))
        # AII count for context
        aii_pts = enumerate_aii_n3_full(N)
        print(f"{N:>3} | {len(aii_pts):>7} | {total:>7} | {cov:>8} | {pct:>9.2f}% | "
              f"{bad_tot:>26} | {dt:>9.2f}")
        if cov < total:
            # Find missing
            missing = bdi_set - union
            print(f"     MISSING at N={N}: {len(missing)} points")
            for q in sorted(missing)[:30]:
                _, M_2, B_1, T_1, B_2, T_2, S = q
                P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
                print(f"       M2={M_2} B1={B_1} T1={T_1} B2={B_2} T2={T_2} S={S}  "
                      f"P_1={P_1} P_2={P_2}")
    return rows


if __name__ == "__main__":
    main()
