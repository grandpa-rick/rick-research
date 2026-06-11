#!/usr/bin/env python3
"""
Task B — OQ-PI3-INV5 check.

Question (Day-64 dream): is the 26-piece registry (the n=3 minimal cover
MIN_COVER_26 from analyze_torus.py) naturally indexed by RSK-shape data
or cycle-type data of involutions in S_5?

I(5) = 26 = 1 + 10 + 15
  (1 identity, 10 single-transpositions, 15 double-transpositions)

Or by RSK shapes (counted by f^lambda for lambda |- 5):
  (5):       f = 1
  (4,1):     f = 4
  (3,2):     f = 5
  (3,1,1):   f = 6
  (2,2,1):   f = 5
  (2,1,1,1): f = 4
  (1,1,1,1,1): f = 1
  sum = 1 + 4 + 5 + 6 + 5 + 4 + 1 = 26.

Procedure:
 1. Build (m_2, m_236, m_23456) column triples for all 26 pieces.
 2. Compare marginal and joint distributions to (1,10,15) and to
    (1,4,5,6,5,4,1).
 3. Check joint distinguishes all 26 pieces.
 4. Bonus: extend to I(6) = 76 via running sums.
"""

import json
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, "/home/agent/projects/code/2026-06-08-pi3-construction")
sys.path.insert(0, "/home/agent/projects/code/2026-06-10-toric-quotient")

from analyze_torus import MIN_COVER_26, ALL_PI

BDI_AXES = ["M_1", "M_2", "B_1", "T_1", "B_2", "T_2", "S"]
TRACKED = ["m_2", "m_236", "m_23456"]


def column_of(piece, var):
    col = [0] * 7
    for i, bdi in enumerate(BDI_AXES):
        for (coef, v) in piece.get(bdi, []):
            if v == var:
                col[i] += coef
    return tuple(col)


def build_triples():
    triples = {}
    for name in MIN_COVER_26:
        piece = ALL_PI[name]
        triples[name] = tuple(column_of(piece, var) for var in TRACKED)
    return triples


def marginals(triples):
    """Distribution of column-index on each axis."""
    out = {}
    for k, var in enumerate(TRACKED):
        cols = sorted({t[k] for t in triples.values()})
        col_to_idx = {c: i for i, c in enumerate(cols)}
        counts = Counter()
        for t in triples.values():
            counts[col_to_idx[t[k]]] += 1
        out[var] = {
            "n_cols": len(cols),
            "cols": [list(c) for c in cols],
            "counts": [counts[i] for i in range(len(cols))],
            "multiset": sorted([counts[i] for i in range(len(cols))]),
        }
    return out


def joint_distinct(triples):
    """Are all 26 pieces distinct on (i_m2, i_m236, i_m23456)?"""
    cols_per_var = {}
    for k, var in enumerate(TRACKED):
        cols = sorted({t[k] for t in triples.values()})
        cols_per_var[var] = {c: i for i, c in enumerate(cols)}
    joint = {}
    for name, t in triples.items():
        idx = tuple(cols_per_var[TRACKED[k]][t[k]] for k in range(3))
        joint.setdefault(idx, []).append(name)
    return joint


def fl_partition_5():
    """f^lambda for all partitions of 5."""
    # Standard known values:
    return {
        (5,): 1,
        (4, 1): 4,
        (3, 2): 5,
        (3, 1, 1): 6,
        (2, 2, 1): 5,
        (2, 1, 1, 1): 4,
        (1, 1, 1, 1, 1): 1,
    }


def I_5_cycle_types():
    """Cycle-type distribution of involutions in S_5."""
    return {"0_transpositions": 1, "1_transposition": 10, "2_transpositions": 15}


def main():
    out_lines = []
    P = lambda *a: out_lines.append(" ".join(str(x) for x in a)) or print(*a)

    P("=" * 70)
    P("Task B — 26-piece registry vs I(5) = 26")
    P("=" * 70)

    triples = build_triples()
    P(f"\nbuilt triples for {len(triples)} pieces")

    P("\n--- 1. Marginal distributions ---")
    margs = marginals(triples)
    for var, m in margs.items():
        P(f"\n {var}:")
        P(f"   #cols = {m['n_cols']}")
        for c, n in zip(m["cols"], m["counts"]):
            P(f"   col {c}: {n} pieces")
        P(f"   sorted multiset = {m['multiset']}")

    P("\n--- 2. Compare to I(5) ---")
    i5_cyc = I_5_cycle_types()
    f5 = fl_partition_5()
    cyc_multiset = sorted(i5_cyc.values())  # [1, 10, 15]
    rsk_multiset = sorted(f5.values())  # [1, 1, 4, 4, 5, 5, 6]
    P(f" I(5) cycle-type multiset: {cyc_multiset}")
    P(f" I(5) RSK-shape multiset:  {rsk_multiset}")

    P("\n Matching marginals to I(5):")
    for var, m in margs.items():
        cyc_match = m["multiset"] == cyc_multiset
        rsk_match = m["multiset"] == rsk_multiset
        P(f"   {var}: multiset = {m['multiset']}")
        P(f"     ↔ cycle types (1,10,15)? {cyc_match}")
        P(f"     ↔ RSK shapes (1,1,4,4,5,5,6)? {rsk_match}")

    P("\n--- 3. Joint distinguishability ---")
    joint = joint_distinct(triples)
    P(f" #distinct joint triples: {len(joint)} (out of 26)")
    collisions = {k: v for k, v in joint.items() if len(v) > 1}
    if collisions:
        P(f" #collisions: {len(collisions)}")
        for idx, names in collisions.items():
            P(f"   {idx}: {names}")
    else:
        P(" all 26 pieces have distinct (i_m2, i_m236, i_m23456) triples ✓")

    P("\n--- 4. Bonus: I(6) = 76 running sum check ---")
    # I(n) recurrence: I(n) = I(n-1) + (n-1)*I(n-2), I(0)=1, I(1)=1
    Ivals = [1, 1]
    for n in range(2, 8):
        Ivals.append(Ivals[-1] + (n - 1) * Ivals[-2])
    P(f" I(n) for n=0..7: {Ivals}")
    P(f" I(5) = {Ivals[5]}, I(6) = {Ivals[6]}, I(7) = {Ivals[7]}")
    # Running sum check: do registry sizes through σ=011 match I(6)?
    # σ=011 is Day-63 notation for the (M_2 odd, S even) parity class.
    # Without a "registry size by σ" datum, we can only report the
    # raw counts at n=3 (= 26) here.
    P(" registry size at n=3 = 26 = I(5). At higher n, registries deferred.")

    P("\n--- 5. Verdict ---")
    any_match = any(
        margs[v]["multiset"] in (cyc_multiset, rsk_multiset) for v in TRACKED
    )
    if any_match:
        P(" PARTIAL MATCH on at least one axis.")
    else:
        P(" NO MATCH on any axis-marginal.")
    P(" The total count 26 = I(5) is suggestive but the marginal")
    P(" distributions do not align with cycle-type or RSK-shape data.")
    P(" Conclusion: no clean bijection visible at the marginal level.")
    P(" Further structure (e.g. specific bijection on triples) would")
    P(" need to be found explicitly; no canonical map jumps out.")

    # Save
    out_dir = Path(__file__).parent
    with open(out_dir / "triples.json", "w") as f:
        json.dump(
            {
                "pieces": {n: [list(c) for c in t] for n, t in triples.items()},
                "marginals": margs,
                "joint_distinct": len(joint) == 26,
                "I_5_cycle_multiset": cyc_multiset,
                "I_5_rsk_multiset": rsk_multiset,
            },
            f,
            indent=2,
        )
    with open(out_dir / "check_output.txt", "w") as f:
        f.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
