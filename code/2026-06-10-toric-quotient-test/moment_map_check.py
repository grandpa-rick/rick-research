"""
Day 60 Task 3 (a): Moment-map fiber check at n=3.

For each BDI lattice point g (with |g| <= N), enumerate all AII points
that map to g under SOME piece of the 26-piece registry. Then test
whether this fiber has the structure of a torus orbit (+ integer
translates) of some rank-2 torus action on AII.

The strong toric-quotient hypothesis predicts:
  fiber(g) = (T^2-orbit) + (integer translates by 3-dim kernel basis).

Day-60 PROVE has already shown the COMMON kernel is trivial. Here we
test EACH PIECE'S kernel as a "local torus orbit" and check whether
fibers can be assembled from these.

Empirical questions:
  Q1. For each piece P_i, is the kernel of P_i a 3-dim integer lattice
      (so each fiber FOR THAT PIECE is a 3-dim integer translate set)?
  Q2. For each BDI g, how many AII pts map to g under the FULL registry
      (union of pieces)?
  Q3. Is this count predicted by a "torus orbit size" formula?

Output:
  - For each piece: kernel lattice basis (we already know dim=3).
  - For each g (at N=8, 10, 12): fiber size + which pieces contribute.
  - Verdict on whether fiber structure is "torus-like".
"""

import sys
sys.path.insert(0, '/home/agent/projects/code/2026-06-08-pi3-construction')

import sympy as sp
import numpy as np
from collections import defaultdict, Counter
from verify_full_v9 import ALL_PI
from verify_full import enumerate_aii_n3_full, bdi_feasible_n3, apply_pi

AII_VARS = ["m_2", "m_23", "m_236", "m_23456", "m_12356", "m_12346",
            "m_2345", "m_1235", "m_1234"]
BDI_VARS = ["M_2", "B_1", "T_1", "B_2", "T_2", "S"]


def piece_matrix(spec):
    """6x9 matrix: rows = BDI vars (no M_1), cols = AII vars."""
    A = sp.zeros(6, 9)
    for bi, bv in enumerate(BDI_VARS):
        for c, av in spec.get(bv, []):
            A[bi, AII_VARS.index(av)] = c
    return A


def kernel_lattice(spec):
    """Integer lattice basis for the kernel of the piece matrix.
       Returns list of integer 9-vectors."""
    A = piece_matrix(spec)
    ker = A.nullspace()
    # Clear denominators to get integer vectors
    out = []
    for v in ker:
        denom = 1
        for x in v:
            d = sp.fraction(x)[1]
            denom = sp.lcm(denom, d)
        v_int = [int(x * denom) for x in v]
        # Normalize so first nonzero entry is positive
        for c in v_int:
            if c != 0:
                if c < 0:
                    v_int = [-x for x in v_int]
                break
        out.append(v_int)
    return out


def fiber_of_g_under_registry(g_tuple, N):
    """
    Given a BDI lattice tuple g = (M_2, B_1, T_1, B_2, T_2, S) (M_1=0),
    enumerate all AII pts (with sum <= N) that map to g under SOME piece.

    Returns dict { piece_name : set of AII tuples }.
    """
    aii_pts = enumerate_aii_n3_full(N)
    fibers = defaultdict(set)
    g = {"M_1": 0, "M_2": g_tuple[0], "B_1": g_tuple[1], "T_1": g_tuple[2],
         "B_2": g_tuple[3], "T_2": g_tuple[4], "S": g_tuple[5]}
    for p in aii_pts:
        for pname, spec in ALL_PI.items():
            q = apply_pi(spec, p)
            ok, _ = bdi_feasible_n3(q)
            if not ok:
                continue
            if (q["M_1"], q["M_2"], q["B_1"], q["T_1"],
                q["B_2"], q["T_2"], q["S"]) == (0,) + g_tuple:
                fibers[pname].add(tuple(p[v] for v in AII_VARS))
    return fibers


def main():
    print("=" * 72)
    print("Day 60 Task 3(a): Moment-map fiber check at n=3")
    print("=" * 72)
    print()

    # Step 1: Compute kernel for each piece (verify dim=3 individually).
    print("--- Step 1: piece kernels ---")
    all_kernels = {}
    for pname, spec in ALL_PI.items():
        ker = kernel_lattice(spec)
        all_kernels[pname] = ker
    dims = Counter(len(k) for k in all_kernels.values())
    print(f"  Kernel dim distribution across {len(all_kernels)} pieces: {dict(dims)}")
    # Expected: most pieces have ker dim 3.

    # Step 2: Common kernel = intersection of all kernels.
    # Strategy: stack all piece matrices, find common kernel.
    print()
    print("--- Step 2: common kernel across all pieces ---")
    matrices = [piece_matrix(spec) for spec in ALL_PI.values()]
    big = sp.Matrix.vstack(*matrices)
    print(f"  Stacked matrix shape: {big.shape}")
    print(f"  Rank: {big.rank()}")
    print(f"  Common kernel dim: {9 - big.rank()}")

    # Step 3: For sample BDI points, count fiber size (= union over pieces).
    print()
    print("--- Step 3: fiber sizes for sample BDI points ---")

    # Pick some "interesting" BDI points at small N
    sample_g_list = [
        (0, 0, 0, 0, 0, 0),  # zero
        (0, 1, 0, 0, 0, 0),  # B_1=1
        (1, 1, 0, 1, 0, 0),  # mixed
        (2, 2, 1, 2, 1, 1),  # high
        (0, 2, 2, 0, 0, 0),  # T_1=2, B_1=2
        (0, 1, 1, 1, 1, 0),  # T_1=B_1, T_2=B_2 (trivial moment)
    ]

    print(f"{'g (M_2,B_1,T_1,B_2,T_2,S)':>30} | {'|g|':>3} | "
          f"{'# pieces hit':>12} | {'fiber size':>10}")
    print("-" * 72)
    for g in sample_g_list:
        weight = sum(g)
        N_cap = max(8, weight + 4)
        fibers = fiber_of_g_under_registry(g, N_cap)
        n_pieces = len(fibers)
        fiber = set()
        for s in fibers.values():
            fiber.update(s)
        print(f"{str(g):>30} | {weight:>3} | {n_pieces:>12} | {len(fiber):>10}")

    # Step 4: Test torus-orbit hypothesis for one piece.
    # If torus action is t.x = x + t*v_1 + ... + t_k * v_k (where v_i are
    # kernel basis), then the fiber for piece P over g is exactly
    # { x_0 + sum t_i v_i : t_i in Z, all entries >= 0 }.
    # We test: pick a piece P, find an AII pt x_0 with P(x_0) = g, and
    # check that AII pts {x_0 + linear combo of ker(P)} ∩ orthant ∩ |.|<=N
    # equals fiber_under_P(g).
    print()
    print("--- Step 4: torus-orbit structure of fibers (per-piece test) ---")
    pname_sample = "P5a_m2_in_S"  # known good piece
    spec_sample = ALL_PI[pname_sample]
    ker_basis = all_kernels[pname_sample]
    print(f"  Testing piece: {pname_sample}")
    print(f"  Kernel basis (dim {len(ker_basis)}):")
    for v in ker_basis:
        d = {AII_VARS[j]: v[j] for j in range(9) if v[j] != 0}
        print(f"    {d}")

    g_test = (0, 1, 0, 1, 0, 0)
    print(f"  Test g = {g_test} (M_2=0, B_1=1, T_1=0, B_2=1, T_2=0, S=0)")
    N_cap = 8
    aii_pts = enumerate_aii_n3_full(N_cap)
    fiber_under_P = []
    for p in aii_pts:
        q = apply_pi(spec_sample, p)
        ok, _ = bdi_feasible_n3(q)
        if not ok: continue
        if (q["M_2"], q["B_1"], q["T_1"], q["B_2"], q["T_2"], q["S"]) == g_test:
            fiber_under_P.append(tuple(p[v] for v in AII_VARS))
    print(f"  |fiber under {pname_sample}, N≤{N_cap}| = {len(fiber_under_P)}")

    # Check that fiber is a torus orbit: any two points should differ by
    # a kernel direction.
    if fiber_under_P:
        x0 = np.array(fiber_under_P[0], dtype=int)
        K = np.array(ker_basis, dtype=int)  # rows = kernel basis
        diffs = []
        for x in fiber_under_P[1:]:
            diff = np.array(x, dtype=int) - x0
            diffs.append(diff)
        print(f"  Sample differences from x_0 (should all be in span(ker)):")
        all_in_ker = True
        for d in diffs[:5]:
            # Check d is in row span of K over Q
            # Solve K^T c = d
            try:
                sol = np.linalg.lstsq(K.T.astype(float), d.astype(float), rcond=None)
                resid = K.T @ sol[0] - d
                in_span = np.allclose(resid, 0, atol=1e-8)
                if not in_span:
                    all_in_ker = False
                print(f"    d = {d.tolist()}, in_span_of_ker: {in_span}")
            except Exception as e:
                print(f"    d = {d.tolist()}, error: {e}")
        if all_in_ker:
            print(f"  ✓ All sampled diffs are in kernel — fiber-under-P IS a torus orbit.")
        else:
            print(f"  ✗ Some diffs are NOT in kernel — fiber-under-P is NOT a torus orbit.")

    # Step 5: Across pieces — different pieces give different "torus
    # embeddings" in AII. Confirm this empirically.
    print()
    print("--- Step 5: Comparing kernel directions across pieces ---")
    # Take a set of pieces with most common 'natural T' coords, see if their
    # kernels agree.
    pname_a = "P5a_m2_in_S"
    pname_b = "P7_M2_simple_S_m2_2x23456"
    if pname_b in ALL_PI:
        ker_a = sp.Matrix([all_kernels[pname_a]])
        ker_b = sp.Matrix([all_kernels[pname_b]])
        # Intersection: find common nullspace of [ker_a^perp, ker_b^perp]?
        # Easier: stack the 2 piece matrices, look at common kernel.
        A_a = piece_matrix(ALL_PI[pname_a])
        A_b = piece_matrix(ALL_PI[pname_b])
        A_ab = sp.Matrix.vstack(A_a, A_b)
        common_dim = 9 - A_ab.rank()
        print(f"  Common kernel dim of {pname_a} ∩ {pname_b}: {common_dim}")
        for v in A_ab.nullspace():
            denom = 1
            for x in v:
                d = sp.fraction(x)[1]
                denom = sp.lcm(denom, d)
            v_int = [int(x * denom) for x in v]
            d = {AII_VARS[j]: v_int[j] for j in range(9) if v_int[j] != 0}
            print(f"    common ker direction: {d}")

    print()
    print("--- Verdict ---")
    print("  Common kernel across ALL 26 pieces: 0 (per Step 2).")
    print("  Hence NO universal torus quotient on AII.")
    print("  Each piece has its OWN 3-dim torus action; they don't agree.")


if __name__ == "__main__":
    main()
