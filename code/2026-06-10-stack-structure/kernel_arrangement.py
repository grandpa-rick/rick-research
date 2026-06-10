"""
Day 62 — Kernel arrangement of piece differences.

Two pieces i, j give the same BDI image at p iff D(i,j) p = 0, where
D(i,j) = pi^(i) - pi^(j) as 6x9 matrices.  The collection
  A := { ker D(i,j) : 1 <= i < j <= 26 }
is a (rational) linear-subspace arrangement in AII (Q^9).

Compute it:
- For each pair (i, j), compute rank(D(i, j)) and ker D(i, j) as
  a subspace of Q^9.
- Group the kernels by dimension and report.
- Identify the codim-1 (hyperplane) kernels and their defining linear
  forms.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import sympy as sp
from itertools import combinations
from collections import Counter, defaultdict

from verify_full_v9 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    Ms = [piece_matrix(ALL_PI[name]) for name in pieces]

    print(f"# pieces = {len(pieces)}")
    print(f"All 6x9 matrices. AII vars (cols): {AII_VARS}")

    # Pairwise differences.
    diff_rank = Counter()
    kernels_by_dim = defaultdict(list)
    ker_basis_strings = defaultdict(set)

    for (i, A_i), (j, A_j) in combinations(enumerate(Ms), 2):
        D = A_i - A_j
        r = D.rank()
        diff_rank[r] += 1
        ker = D.nullspace()
        d_ker = len(ker)
        # Each null-space basis vector is a 9-vec.  Reduce it canonically.
        basis = tuple(tuple(v[k, 0] for k in range(9)) for v in ker)
        kernels_by_dim[d_ker].append((pieces[i], pieces[j], r, basis))

    print("\n--- Distribution of rank(D(i,j)) ---")
    for r, c in sorted(diff_rank.items()):
        print(f"  rank {r}: {c} pairs   (ker dim = {9-r})")

    print("\n--- Kernel dimensions ---")
    for d in sorted(kernels_by_dim):
        print(f"  ker dim {d}: {len(kernels_by_dim[d])} pairs")

    # For codim 1 (rank 8), the kernel is a hyperplane.  Find the defining
    # row vector (the unique-up-to-scale linear form vanishing on it).
    # For higher codim, list a basis.
    print("\n--- Codimension 1 walls (ker dim = 8): rank(D) = 1 ---")
    # Re-iterate with diff matrices directly (rank 1 case).
    wall_forms = Counter()
    wall_examples = defaultdict(list)
    for i, A_i in enumerate(Ms):
        for j in range(i+1, len(Ms)):
            A_j = Ms[j]
            D = A_i - A_j
            if D.rank() != 1:
                continue
            # Take the first non-zero row of D as the linear form.
            form_row = None
            for k in range(6):
                if any(D[k, l] != 0 for l in range(9)):
                    form_row = [D[k, l] for l in range(9)]
                    break
            if form_row is None:
                continue
            coords = list(form_row)
            # Normalise: divide by gcd of integer entries; make leading sign positive
            from sympy import gcd as sgcd
            ints = [int(c) for c in coords if c != 0]
            if ints:
                g = ints[0]
                for x in ints[1:]:
                    g = sgcd(g, x)
                g = abs(g) or 1
                coords = [int(c) // g if c % g == 0 else c / g for c in coords]
                for c in coords:
                    if c != 0:
                        if c < 0:
                            coords = [-x for x in coords]
                        break
        # Find gcd of integer coeffs
        from sympy import gcd, sign
        ints = [int(c) for c in coords if c != 0]
        if ints:
            g = ints[0]
            for x in ints[1:]:
                g = gcd(g, x)
            g = abs(g)
            if g == 0:
                g = 1
            coords = [c / g for c in coords]
            # Sign: leading non-zero positive
            for c in coords:
                if c != 0:
                    if c < 0:
                        coords = [-x for x in coords]
                    break
            form_str = " + ".join(
                f"{coords[k]}*{AII_VARS[k]}" for k in range(9) if coords[k] != 0
            )
            wall_forms[form_str] += 1
            wall_examples[form_str].append((pieces[i], pieces[j]))

    print(f"  Distinct wall forms: {len(wall_forms)}")
    for f, c in sorted(wall_forms.items(), key=lambda x: -x[1]):
        print(f"    {c:3d} pairs: {f} = 0")
        ex = wall_examples[f][:2]
        for a, b in ex:
            print(f"          e.g. {a}  ~  {b}")


if __name__ == "__main__":
    main()
