"""
Day 61 — Minimal cover recomputation.

What's the true minimal subset of the 26 pieces that covers all BDI
lattice points with |q| <= N, for N = 8, 9, 10?

If 9 essential pieces suffice, the 26-piece number is inflated by
combinatorial overcount.

If the true min cover grows from 9 (N=8) to >=26 (N=10), then the
26-piece structure is N-dependent and the 'reframe' question is whether
the cover stabilizes (number of pieces tends to a limit) or grows.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

from verify_full_v7 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26


def compute_hits(N):
    """For each BDI lattice point with |q|<=N, list pieces that hit it."""
    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    aii_pts = list(enumerate_aii_n3_full(N))
    bdi_hits = {}
    for p in aii_pts:
        for name in pieces:
            spec = ALL_PI[name]
            q = apply_pi(spec, p)
            if q is None or not bdi_feasible_n3(q):
                continue
            q_key = tuple(q[v] for v in ['M_1','M_2','B_1','T_1','B_2','T_2','S'])
            if sum(abs(x) for x in q_key) > N: continue
            bdi_hits.setdefault(q_key, set()).add(name)
    return bdi_hits, pieces


def greedy_cover(bdi_hits, pieces):
    """Greedy set cover."""
    uncovered = set(bdi_hits.keys())
    chosen = []
    piece_covers = {name: {q for q, h in bdi_hits.items() if name in h}
                    for name in pieces}
    while uncovered:
        best = max(piece_covers, key=lambda n: len(piece_covers[n] & uncovered))
        if not (piece_covers[best] & uncovered):
            print(f"  WARNING: uncovered points remain: {len(uncovered)}")
            break
        chosen.append(best)
        uncovered -= piece_covers[best]
    return chosen


def lp_cover(bdi_hits, pieces):
    """LP-relaxation of minimum set cover, then round.

    For exact min set cover use ILP. Use scipy + manual rounding.
    Actually let's just use brute-force lower bound: # essentials.
    """
    essentials = set()
    for q, hitters in bdi_hits.items():
        if len(hitters) == 1:
            essentials.add(next(iter(hitters)))
    return essentials


def main():
    print("=" * 78)
    print("DAY 61 — MIN COVER PROGRESSION")
    print("=" * 78)
    for N in [6, 7, 8, 9, 10]:
        print(f"\n--- N = {N} ---")
        bdi_hits, pieces = compute_hits(N)
        print(f"  # BDI lattice points hit: {len(bdi_hits)}")
        essentials = lp_cover(bdi_hits, pieces)
        print(f"  # essential pieces (sole-hitter of some q): {len(essentials)}")

        # Check: do essentials alone cover all points?
        ess_covers = set()
        for q, hitters in bdi_hits.items():
            if hitters & essentials:
                ess_covers.add(q)
        essential_only_covers = len(ess_covers) == len(bdi_hits)
        print(f"  Essentials alone cover all: {essential_only_covers}")
        if not essential_only_covers:
            uncovered = set(bdi_hits.keys()) - ess_covers
            print(f"    # not covered by essentials: {len(uncovered)}")

        # Greedy min cover
        chosen = greedy_cover(bdi_hits, pieces)
        print(f"  Greedy minimum cover size: {len(chosen)}")
        print(f"  Greedy chosen pieces: {chosen}")


if __name__ == "__main__":
    main()
