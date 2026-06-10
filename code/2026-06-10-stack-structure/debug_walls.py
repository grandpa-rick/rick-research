"""Print every rank-1 difference matrix and its row form."""
import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import sympy as sp
from verify_full_v9 import ALL_PI
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS


def main():
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    Ms = [piece_matrix(ALL_PI[name]) for name in pieces]
    count = 0
    for i in range(len(Ms)):
        for j in range(i+1, len(Ms)):
            D = Ms[i] - Ms[j]
            if D.rank() != 1:
                continue
            count += 1
            # find first non-zero row
            row = None
            for k in range(6):
                if any(D[k, l] != 0 for l in range(9)):
                    row = [int(D[k, l]) for l in range(9)]
                    break
            form_str = " + ".join(
                f"{row[k]}*{AII_VARS[k]}" for k in range(9) if row[k] != 0
            )
            print(f"  {pieces[i]:<35s} - {pieces[j]:<35s}  ->  {form_str}")
    print(f"Total rank-1 pairs: {count}")


if __name__ == "__main__":
    main()
