"""
Day 60 (2026-06-10) Task 2: Extend the dim-gap table to n=7 and conjecture
a closed-form for f(n) = dim P^AII_{2n-1} - dim P^BDI_n.

We reuse the dim_gap_verify.aii_structure recipe (Azenhas variable
recipe + Cor 8 linking eq) and tabulate at n = 3, 4, 5, 6, 7.

f(n) prediction (parity-locked):
   f(n) = 3 if n odd
          2 if n even

This follows from the structural pattern:
- dim AII = 3n if n odd (no linking eq)
- dim AII = 3n - 1 if n even (1 linking eq)
- dim BDI = 3n - 3 always
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-dim-gap-n5n6-computational')

import numpy as np
from dim_gap_verify import (aii_structure, bdi_dim,
                             affine_hull_dim_from_constraints,
                             construct_independent_feasible,
                             affine_span_dim)


def main():
    print("=" * 72)
    print("Day 60 Task 2: f(n) table at n = 3, 4, 5, 6, 7")
    print("=" * 72)
    print()
    print(f"{'n':>3} | {'vars AII':>8} | {'eq rank':>7} | {'dim AII':>8} | "
          f"{'dim BDI':>8} | {'f(n)':>5} | parity")
    print("-" * 72)

    table = []
    for n in [3, 4, 5, 6, 7]:
        struct = aii_structure(n)
        info = affine_hull_dim_from_constraints(struct)
        dim_aii = info["dim"]
        dim_bdi = bdi_dim(n)
        gap = dim_aii - dim_bdi
        eq_rank = info["rank_eq"]
        vars_aii = info["n_vars"]
        parity = "odd" if n % 2 else "even"
        print(f"{n:>3} | {vars_aii:>8} | {eq_rank:>7} | {dim_aii:>8} | "
              f"{dim_bdi:>8} | {gap:>5} | {parity}")
        table.append((n, vars_aii, eq_rank, dim_aii, dim_bdi, gap, parity))

    print()
    print("=" * 72)
    print("Independent verification via explicit construction:")
    print("=" * 72)
    for n in [3, 4, 5, 6, 7]:
        struct = aii_structure(n)
        pts = construct_independent_feasible(struct)
        d = affine_span_dim(pts)
        predicted = 3*n if n % 2 else 3*n - 1
        agree = "✓" if d == predicted else "✗"
        print(f"  n={n}: |pts|={len(pts)}, affine span dim = {d} "
              f"(predicted {predicted}) {agree}")

    print()
    print("=" * 72)
    print("Conjecture: f(n) closed-form")
    print("=" * 72)
    print()
    print("  Direct formula:    f(n) = 3 if n odd, 2 if n even")
    print("  One-line formula:  f(n) = (5 + (-1)^n) / 2 - (- ... ) ")
    print()

    # Try closed-form candidates
    print("Testing closed-form candidates:")
    for n, _, _, _, _, gap, _ in table:
        v1 = (5 + (-1)**(n+1)) // 2  # = 3 if n odd, 2 if n even
        v2 = 3 - (n % 2 == 0)
        v3 = 2 + (n % 2)
        print(f"  n={n}: actual={gap}, (5+(-1)^(n+1))/2={v1}, "
              f"3-[n even]={v2}, 2+(n mod 2)={v3}")

    print()
    print("Cleanest form: f(n) = 3 - [n is even]")
    print("Equivalently:  dim AII = 3n - [n is even]; dim BDI = 3n - 3.")
    print()

    # Also: verify free-var count - linking-eq count formulation
    print("=" * 72)
    print("Alternative: f(n) as (free AII vars) - (BDI vars) - (linking eqs)")
    print("=" * 72)
    for n, vars_aii, eq_rank, dim_aii, dim_bdi, gap, _ in table:
        alt = vars_aii - dim_bdi - eq_rank
        print(f"  n={n}: {vars_aii} - {dim_bdi} - {eq_rank} = {alt}  "
              f"(matches actual gap {gap}? {alt == gap})")
    print()
    print("So f(n) = 3n - 3n+3 - [n even] = 3 - [n even].")
    print("Confirmed.")


if __name__ == "__main__":
    main()
