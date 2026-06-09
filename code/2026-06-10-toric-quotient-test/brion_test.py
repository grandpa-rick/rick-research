"""
Day 60 Task 3 (b): Brion's lemma test.

For a torus quotient X → Y of rank k, Brion's lemma + symplectic
reduction predicts:

  Ehrhart(X) at level N  ~  Ehrhart(Y) at level N  *  ('orbit volume')

with the "orbit volume" being a polynomial of degree k = torus rank
in the moment-map coords.

For us, IF AII → BDI were a clean torus quotient of rank 3 (= f(3)),
then |AII_N| / |BDI_N| should grow like N^3.

We test:
  - Count |AII ∩ Z^9|_{sum <= N} and |BDI ∩ Z^6|_{sum <= N} at
    N = 4, 6, 8, 10.
  - Fit |AII_N| ~ c_AII * N^{dim AII} = c_AII * N^9, and similarly
    BDI ~ c_BDI * N^6.
  - Predicted from Brion: c_AII / c_BDI should equal a 3-dim "torus
    polytope" leading coefficient.

If the ratio is well-defined and matches the prediction, that's
evidence FOR a torus-quotient structure (at least in the leading
Ehrhart). If it's wonky, that's against.

This is a NECESSARY but not sufficient condition: the leading Ehrhart
matches for "any" surjective polynomial map.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')

import numpy as np
from verify_full import enumerate_aii_n3_full, enumerate_bdi_n3


def main():
    print("=" * 72)
    print("Day 60 Task 3(b): Brion's lemma / Ehrhart growth test")
    print("=" * 72)
    print()

    Ns = [4, 6, 8, 10]
    print(f"{'N':>3} | {'|AII_N|':>10} | {'|BDI_N|':>10} | {'ratio':>10} | "
          f"{'N^3':>6} | {'ratio/N^3':>12}")
    print("-" * 72)
    rows = []
    for N in Ns:
        aii_pts = enumerate_aii_n3_full(N)
        bdi_pts = enumerate_bdi_n3(N)
        aii_count = len(aii_pts)
        bdi_count = len(bdi_pts)
        ratio = aii_count / bdi_count if bdi_count else None
        ratio_per_n3 = ratio / N**3 if ratio is not None else None
        print(f"{N:>3} | {aii_count:>10} | {bdi_count:>10} | {ratio:>10.4f} | "
              f"{N**3:>6} | {ratio_per_n3:>12.6f}")
        rows.append((N, aii_count, bdi_count, ratio, ratio_per_n3))

    # Leading-order Ehrhart fit: log(count) vs log(N)
    print()
    print("--- Leading-order Ehrhart fit ---")
    log_Ns = np.log([row[0] for row in rows])
    log_aii = np.log([row[1] for row in rows])
    log_bdi = np.log([row[2] for row in rows])

    slope_aii = np.polyfit(log_Ns, log_aii, 1)[0]
    slope_bdi = np.polyfit(log_Ns, log_bdi, 1)[0]
    print(f"  AII: log|AII_N| ~ {slope_aii:.3f} * log(N) + const  "
          f"(expected slope = dim AII = 9, but lattice growth incl. N^9 only as N→∞)")
    print(f"  BDI: log|BDI_N| ~ {slope_bdi:.3f} * log(N) + const  "
          f"(expected slope = dim BDI = 6)")
    print(f"  Ratio slope: {slope_aii - slope_bdi:.3f}  (expected = f(n) = 3 if torus)")

    # Brion: if torus quotient of rank k, the fiber at every BDI point
    # is a polytope of dim k. So |AII_N| / |BDI_N| should grow like
    # N^k * c where c is the typical fiber size leading coeff.
    # We test: does ratio / N^k stabilize?
    print()
    print("--- Ratio / N^k test ---")
    for k in [2, 3, 4]:
        print(f"  k = {k}: |AII_N| / (|BDI_N| * N^k) =", end=" ")
        for row in rows:
            N, aii_c, bdi_c, ratio, _ = row
            val = ratio / (N ** k) if N else None
            print(f"N={N}:{val:.5f}", end="  ")
        print()

    # The "right" k is the one where the ratio stabilizes.
    print()
    print("--- Diagnostic: how does the ratio scale? ---")
    # If it's polynomial in N of degree d, log(ratio) ~ d * log(N).
    log_ratio = np.log([row[3] for row in rows])
    d = np.polyfit(log_Ns, log_ratio, 1)[0]
    print(f"  log(ratio) ~ {d:.3f} * log(N) + const")
    print(f"  → ratio grows like N^{d:.2f}")
    print(f"  Predicted (torus rank) = f(n) = 3 (matches if d ≈ 3).")

    # Brion at vertex: at each vertex of BDI, generating function
    # factor is 1 / prod(1 - t^a_i). If torus quotient, the vertices
    # of AII map to vertices of BDI in a known way. Hard to test
    # without explicit vertex enumeration; deferred.

    print()
    print("--- Verdict ---")
    if abs(d - 3) < 0.5:
        print(f"  Leading-order Ehrhart growth (ratio ~ N^{d:.2f}) is "
              f"COMPATIBLE with a rank-3 torus quotient.")
        print(f"  But this is necessary, not sufficient (any surjection of "
              f"the right dim would give this).")
    else:
        print(f"  Leading-order Ehrhart growth (ratio ~ N^{d:.2f}) is NOT 3.")
        print(f"  → Inconsistent with a simple rank-3 torus quotient.")

    print()
    print("  Together with Step 2 of moment_map_check.py (common kernel = 0),")
    print("  this rules out a universal torus quotient. The Ehrhart leading")
    print("  term can still match (any rank-3 'projection' would give it)")
    print("  but the structure is NOT a clean toric GIT picture.")


if __name__ == "__main__":
    main()
