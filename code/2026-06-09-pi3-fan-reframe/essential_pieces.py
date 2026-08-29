"""
Day 61 — Essential piece count and tropical-max test.

Q1: Which pieces are ESSENTIAL? A piece i is essential if there exists a
BDI lattice point q (|q|<=N) such that pi^(i) is the UNIQUE piece in the
26-cover that hits q (via some lattice AII preimage).

If most pieces are non-essential, the 26-piece count is inflated by
combinatorial redundancy and the actual "structural" complexity is
smaller.

Q2: Tropical-max unification.
The 4 distinct T_1 expressions:
  T_1^(a) = m_2345
  T_1^(b) = m_2345 + m_23456
  T_1^(c) = m_2345 + m_236
  T_1^(d) = m_2345 + 2 m_236

The TROPICAL MAX T_1^{trop} = m_2345 + max(0, m_23456, m_236, 2 m_236)
  = m_2345 + max(m_23456, 2 m_236, 0)
  = m_2345 + max(m_23456, 2 m_236)  (since both >= 0)

Chambers:
  C_1: m_23456 >= 2 m_236 => T_1^{trop} = m_2345 + m_23456
  C_2: m_23456 < 2 m_236 => T_1^{trop} = m_2345 + 2 m_236

So T_1^{trop} is a tropical max with 2 chambers. The piece T_1^(c) (with
m_236 coeff 1) is NOT a chamber of this max.

Q: Could this be a CHOICE problem (the piece chooses based on q, not p)?
Then the relevant tropical structure is in BDI-space, viewed as a
multivalued tropical inverse.
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')
sys.path.insert(0, '/home/agent/projects/code/2026-06-10-toric-quotient')

import sympy as sp
from itertools import product
from verify_full_v7 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi
from analyze_torus import MIN_COVER_26, piece_matrix, AII_VARS, BDI_VARS


def main():
    print("=" * 78)
    print("DAY 61 — ESSENTIAL PIECE COUNT")
    print("=" * 78)

    pieces = [name for name in MIN_COVER_26 if name in ALL_PI]
    N = 8  # speed

    # Enumerate all AII lattice points up to |p|<=N, compute BDI image per piece
    print(f"\nEnumerating AII lattice points with |p| <= {N}...")
    aii_pts = list(enumerate_aii_n3_full(N))
    print(f"  # AII lattice points: {len(aii_pts)}")

    # For each BDI lattice point, list which pieces hit it (from any AII preimage)
    bdi_hits = {}  # q_tuple -> set of piece names
    for p in aii_pts:
        for name in pieces:
            spec = ALL_PI[name]
            q = apply_pi(spec, p)
            if q is None:
                continue
            # q is a tuple/dict; check feasibility
            if not bdi_feasible_n3(q):
                continue
            q_key = tuple(q[v] for v in ['M_1', 'M_2', 'B_1', 'T_1', 'B_2', 'T_2', 'S'])
            if sum(abs(x) for x in q_key) > N:
                continue
            bdi_hits.setdefault(q_key, set()).add(name)

    print(f"  # BDI lattice points hit (|q|<={N}): {len(bdi_hits)}")

    # Essential pieces: those that are sole hitters of some q
    essential = set()
    unique_q = {}
    for q, hitters in bdi_hits.items():
        if len(hitters) == 1:
            piece = next(iter(hitters))
            essential.add(piece)
            unique_q.setdefault(piece, []).append(q)

    print(f"\n  Essential pieces (sole hitter of some q with |q|<={N}): {len(essential)}")
    for p in sorted(essential):
        examples = unique_q[p][:3]
        print(f"    {p}: {len(unique_q[p])} unique-hit lattice points; e.g., {examples}")

    nonessential = set(pieces) - essential
    print(f"\n  NON-essential pieces (every q they hit is also hit by another piece): {len(nonessential)}")
    for p in sorted(nonessential):
        print(f"    {p}")

    # Histogram of multiplicity (how many pieces hit each q)
    print(f"\nMultiplicity histogram (how many pieces hit a given BDI point):")
    hist = {}
    for q, hitters in bdi_hits.items():
        hist[len(hitters)] = hist.get(len(hitters), 0) + 1
    for k in sorted(hist.keys()):
        print(f"  {k} pieces hit: {hist[k]} BDI points")

    # Average multiplicity
    if bdi_hits:
        avg = sum(len(h) for h in bdi_hits.values()) / len(bdi_hits)
        print(f"\n  Average multiplicity: {avg:.2f}")


if __name__ == "__main__":
    main()
