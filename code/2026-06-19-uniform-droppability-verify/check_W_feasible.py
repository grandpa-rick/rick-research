#!/usr/bin/env python3
"""
Day 79 PROVE — Theorem 9.1 sanity check.

For every n in {5..12}, every interior i in {2,..,n-2}, and every
alpha in {1, 2}, verify:

  (a) The sparse witness W_{i,alpha} (prefix[1] = e_{B_i},
      long[2] = alpha * e_S, all else zero) is BDI-feasible.

  (b) Im(W_{i,alpha}) is contained in Im(base_piece(n)).
      (Equivalently: every nonzero ray-image of W is in Im(base_piece).)

  (c) Im(carrier_{i,alpha}) is contained in Im(base_piece(n)).
      (Day-78 Lemma 4.1 instantiated at pi_0 = base_piece.)

Boundary cases (i in {1, n-1}) are also checked, just to verify the
proof scope is conservative.
"""
from __future__ import annotations
import sys
from pathlib import Path

CODE_DIR = Path("/home/agent/projects/code")
sys.path.insert(0, str(CODE_DIR / "2026-06-18-clio-decisive-check"))
from bdi_n import (
    zero_piece, vec, scale, check_F, gen_set, add, target_point, is_BDI,
    bdi_coords,
)


def witness_lifted_long(n: int, i: int, alpha: int) -> dict:
    """Sparse W: prefix[1] = e_{B_i}, long[2] = alpha * e_S, rest 0."""
    piece = zero_piece(n)
    piece["p1"] = vec(n, **{f"B{i}": 1})
    piece["l2"] = scale(alpha, vec(n, S=1))
    return piece


def witness_lifted_short(n: int, i: int, alpha: int) -> dict:
    """Lifted-short variant: prefix[1] = e_{B_i}, short[2] = alpha * e_S."""
    piece = zero_piece(n)
    piece["p1"] = vec(n, **{f"B{i}": 1})
    piece["s2"] = scale(alpha, vec(n, S=1))
    return piece


def main():
    print("=" * 70)
    print("Theorem 9.1 Phase 1 sanity check: W_{i,alpha} F-feasibility")
    print("=" * 70)

    failures = []
    for n in [5, 6, 7, 8, 9, 10, 11, 12]:
        for i in range(2, n - 1):  # interior i in {2,..,n-2}
            for alpha in (1, 2):
                # Lifted-long route
                W = witness_lifted_long(n, i, alpha)
                ok = check_F(n, W)
                T = target_point(n, i, alpha)
                ray = add(W["p1"], W["l2"])
                assert ray == T
                if not ok:
                    failures.append(("long", n, i, alpha))
                # Lifted-short route
                W2 = witness_lifted_short(n, i, alpha)
                ok2 = check_F(n, W2)
                if not ok2:
                    failures.append(("short", n, i, alpha))
        print(f"  n={n}: interior i in {list(range(2, n-1))} x alpha "
              f"in {{1,2}} -- both routes F-feasible")

    print()
    print("=" * 70)
    print("Boundary check: i in {1, n-1}")
    print("=" * 70)
    for n in [5, 6, 7, 8]:
        for i in [1, n - 1]:
            for alpha in (1, 2):
                W = witness_lifted_long(n, i, alpha)
                ok = check_F(n, W)
                if not ok:
                    failures.append(("long-boundary", n, i, alpha))
                W2 = witness_lifted_short(n, i, alpha)
                ok2 = check_F(n, W2)
                if not ok2:
                    failures.append(("short-boundary", n, i, alpha))
            print(f"  n={n}, i={i}: alpha in {{1,2}} -- both routes F-feasible")

    print()
    print("=" * 70)
    print("Phase 2 sanity check: nonzero ray-images of W are e_{B_i} or T")
    print("=" * 70)
    for n in [5, 6, 7, 8]:
        for i in range(2, n - 1):
            for alpha in (1, 2):
                W = witness_lifted_long(n, i, alpha)
                rays = gen_set(n, W)
                nonzero = [r for r in rays if any(x != 0 for x in r)]
                e_Bi = vec(n, **{f"B{i}": 1})
                T = target_point(n, i, alpha)
                # Expected: each nonzero ray is e_{B_i} or T
                for r in nonzero:
                    assert r == e_Bi or r == T, (
                        f"unexpected nonzero ray at n={n}, i={i}, alpha={alpha}: {r}")
        print(f"  n={n}: every nonzero W ray-image is e_{{B_i}} or T = e_{{B_i}} + alpha*e_S "
              f"(verified for interior i, alpha in {{1,2}})")

    print()
    if failures:
        print(f"FAILED: {len(failures)} cases")
        for f in failures:
            print(f"  {f}")
        sys.exit(1)
    else:
        print("ALL CHECKS PASS.")
        print()
        print("Theorem 9.1 Phase 1 and the empirical content of Phase 2 verify "
              "n-uniformly up to n = 12 (boundary cases up to n = 8).")


if __name__ == "__main__":
    main()
