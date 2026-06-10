"""
Day 62 — Which AII variables are 'rigid' (same coeff column in every piece)
vs 'flexible' (vary across pieces)?
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import sympy as sp
from verify_full_v9 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS, BDI_VARS


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    Ms = [piece_matrix(ALL_PI[name]) for name in pieces]

    print(f"BDI rows: {BDI_VARS}")
    print(f"AII cols: {AII_VARS}\n")

    print(f"{'AII var':<10} | column across 26 pieces (sets of 6-tuples)")
    print("-" * 80)
    for col_idx, av in enumerate(AII_VARS):
        cols = set()
        for M in Ms:
            cols.add(tuple(int(M[r, col_idx]) for r in range(6)))
        if len(cols) == 1:
            col = next(iter(cols))
            nonzero = [(BDI_VARS[r], col[r]) for r in range(6) if col[r] != 0]
            tag = "RIGID"
            desc = ", ".join(f"{v}+={c}" for v, c in nonzero)
            print(f"{av:<10} | {tag:<8} {desc}")
        else:
            print(f"{av:<10} | FLEXIBLE ({len(cols)} distinct columns)")
            for col in sorted(cols):
                nonzero = [(BDI_VARS[r], col[r]) for r in range(6) if col[r] != 0]
                desc = ", ".join(f"{v}+={c}" for v, c in nonzero)
                print(f"            -> {desc if desc else '(zero)'}")


if __name__ == "__main__":
    main()
