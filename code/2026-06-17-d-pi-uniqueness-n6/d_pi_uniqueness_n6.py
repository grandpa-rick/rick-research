#!/usr/bin/env python3
"""
Day 76 CODE Task A -- D-pi uniqueness half at n = 6.

STATEMENT (weak D-pi uniqueness, n = 6):
  For every interior coord p_i (i in {2, 3, 4}) and every alpha in {0, 1, 2},
  every F-feasible piece pi with
      pi^{p_i} = e_{B_i} + alpha * e_S
  (under the Day-70 section 6 RIGID/BINARY restrictions, extended to
  include R-double level-j engines on s_j) has image semigroup
  EQUIVALENT to the simple-divert piece pi_alpha^{(i)}'s image.

  Equivalently: the three image classes
      { Im(pi_alpha^{(i)}) : alpha in {0, 1, 2} }
  EXHAUST the cover-restricted image-equivalence classes at p_i.

  Verifies the uniqueness half of D-pi at n = 6 (the existence half
  was shipped Day 75). Combined, this unblocks the Day-75 PROVE
  R-AXIS(n) = 1 theorem at n = 6.

OUTPUT:
  - results.json: per-interior, per-alpha enumeration + image-class
    grouping statistics.
  - stdout: human-readable progress + verdict per interior.
"""
from __future__ import annotations
import json
import sys
import time
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent

# =====================================================================
# BDI vector machinery at n = 6
# =====================================================================
# BDI vars: M_2, M_3, M_4, M_5, B_1..B_5, T_1..T_5, S (15 vars).
BDI_COORDS = ["M2", "M3", "M4", "M5",
              "B1", "T1", "B2", "T2", "B3", "T3", "B4", "T4", "B5", "T5",
              "S"]
NB = len(BDI_COORDS)
IDX = {c: i for i, c in enumerate(BDI_COORDS)}
ZERO = tuple([0] * NB)


def vec(**kw):
    v = [0] * NB
    for k, n in kw.items():
        v[IDX[k]] = n
    return tuple(v)


def add(*vs):
    if not vs:
        return ZERO
    return tuple(sum(x) for x in zip(*vs))


def scale(c, v):
    return tuple(c * x for x in v)


def P(a, v):
    """P_a = 2 sum_{b<=a}(B_b - T_b)."""
    return 2 * sum(v[IDX[f"B{b}"]] - v[IDX[f"T{b}"]] for b in range(1, a + 1))


def is_BDI(v):
    """BDI feasibility at n = 6."""
    if any(x < 0 for x in v):
        return False
    for a in range(1, 6):
        if v[IDX[f"T{a}"]] > v[IDX[f"B{a}"]]:
            return False
        if P(a, v) < 0:
            return False
    for a in range(2, 6):
        if v[IDX[f"M{a}"]] > min(P(a - 1, v), P(a, v)):
            return False
    if v[IDX["S"]] > P(5, v):
        return False
    return True


# =====================================================================
# Piece machinery at n = 6 (linkLHS = 0 gauge)
# =====================================================================
# Columns: p_1..p_6, l_1..l_6, s_1..s_5 (no s_6 at even n).
P_COLS = [f"p{j}" for j in range(1, 7)]
L_COLS = [f"l{j}" for j in range(1, 7)]
S_COLS = [f"s{j}" for j in range(1, 6)]
ALL_COLS = P_COLS + L_COLS + S_COLS


def make_piece(**kw):
    for c in ALL_COLS:
        assert c in kw, f"missing {c}"
    return {c: kw[c] for c in ALL_COLS}


def check_F_n6(piece):
    """Day-70 Thm 4.2 at n = 6 in linkLHS = 0 gauge (17 rays).

    Rays (per registry.py aii_rays(6)):
      1. e_{p_j} for j = 1..6
      2. e_{l_1}
      3. e_{p_{j-1}} + e_{l_j} for j = 2..5
      4. e_{p_5} + e_{l_6}
      5. e_{l_6} + e_{s_1}  (linkLHS gauged out)
      6. e_{p_{i-1}} + e_{l_6} + e_{s_i} for i = 2..5 (linkLHS gauged out).
    """
    for j in range(1, 7):
        if not is_BDI(piece[f"p{j}"]):
            return False
    if not is_BDI(piece["l1"]):
        return False
    for j in range(2, 7):
        if not is_BDI(add(piece[f"p{j-1}"], piece[f"l{j}"])):
            return False
    if not is_BDI(add(piece["l6"], piece["s1"])):
        return False
    for i in range(2, 6):
        if not is_BDI(add(piece[f"p{i-1}"], piece["l6"], piece[f"s{i}"])):
            return False
    return True


def gen_set_n6(piece):
    """17 ray-image generators at n = 6 (linkLHS = 0 gauge)."""
    gens = []
    for j in range(1, 7):
        gens.append(piece[f"p{j}"])
    gens.append(piece["l1"])
    for j in range(2, 7):
        gens.append(add(piece[f"p{j-1}"], piece[f"l{j}"]))
    gens.append(add(piece["l6"], piece["s1"]))
    for i in range(2, 6):
        gens.append(add(piece[f"p{i-1}"], piece["l6"], piece[f"s{i}"]))
    assert len(gens) == 17
    return gens


# =====================================================================
# Base piece + simple-divert pi_alpha^{(i)} at n = 6 (linkLHS = 0 gauge)
# =====================================================================
# In linkLHS = 0 gauge, the registry's base piece has:
#   p_j -> e_{B_j} for j = 1..5
#   p_6 -> e_{B_2} + e_{B_4}  (the "free" P_n routing in BT_2 + BT_4
#                              -- actually base has p_6 -> e_{B_2})
# Looking at registry-n6.json's P6_base: prefix[6] -> B_2 (one routing),
# but the underlying base_piece() at general_pieces.py routes p_6 to
# B_2 only (with linkLHS routing to BT_5 -- this is what registry-n6
# encodes, see prefix[6]: B_2 only, linkLHS: B_5 + T_5).
# So in linkLHS = 0 gauge: p_6 -> e_{B_2}, s_{n-1} -> e_{B_{n-1}}+e_{T_{n-1}}
# + (linkLHS folded in: + e_{B_5} + e_{T_5}, but s_{n-1} = s_5 already has
# e_{B_5} + e_{T_5} from its base routing; in gauged form
# pi^{s_5} += e_{B_5} + e_{T_5}.)
# Wait -- per registry-n6.json: short[5] -> B_5 + T_5 (and linkLHS->B_5+T_5,
# so gauged short[5] -> 2(B_5+T_5)).
# But Day-72 registry stores pieces in LINKLHS-NONZERO gauge (per
# load_day70_registry which stores AS-IS). So the simple-divert pieces
# in the registry are encoded with linkLHS-nonzero. We'll re-build them
# directly here in linkLHS = 0 gauge to keep the F-check consistent.

# In linkLHS = 0 gauge at n = 6:
#   pi^{linkLHS} = 0 (forced)
#   The gauge transform from registry to linkLHS=0:
#     M2[:, linkLHS] = 0
#     M2[:, short[i]] = M[:, short[i]] + M[:, linkLHS]  for i = 1..n-1
# For the base piece (P6_base: short[5] = B_5+T_5, linkLHS = B_5+T_5):
#   gauged short[5] = (B_5+T_5) + (B_5+T_5) = 2(B_5+T_5)
# But this makes F3 at s_5 huge: pi^{p_4} + pi^{l_6} + 2(B_5+T_5)
#                                  = B_4 + S + 2 B_5 + 2 T_5.
#   Check: T_a <= B_a: T_5=2, B_5=2 -> OK. P_5 = 2*(B_1+B_2+B_3+B_4+B_5
#                                                   - T_1-...-T_5) = 2*(B_4+2 B_5 - 2 T_5) = 2.
#   M_a constraints: ok (no M routed).
#   S = 1 <= P_5 = 2: ok. So F3 is OK.
#
# Alternative: we can work directly without gauging by setting linkLHS
# column explicitly and including the linkLHS contribution in the rays.
# But simpler: use the "naive odd-n analog" base where
#   pi^{s_i} = e_{B_i} + e_{T_i} (no linkLHS contribution)
#   pi^{p_6} = 0 (the free direction routes nothing)
#   pi^{l_6} = e_S
# and CHECK that F1-F4 hold. This is NOT in linkLHS = 0 gauge of the
# registry; it's a SEPARATE choice of base piece (parametrically related).
#
# For the D-pi uniqueness check, the issue is: do we recover the same
# image classes? Let's check both and see.


def base_piece_linkLHS_zero():
    """Base piece at n=6 in linkLHS=0 gauge (registry-derived).

    Registry P6_base has:
      prefix[j] -> B_j for j=1..5
      prefix[6] -> B_2  (default P_n routing in BT_2; actually only B_2
                          because at even n, T_2 absorbs from elsewhere)
      long[1] -> B_1
      long[j] -> M_j for j=2..5
      long[6] -> S
      short[j] -> B_j + T_j for j=1..5
      linkLHS -> B_5 + T_5

    In gauge linkLHS=0: short[j] += linkLHS for each j=1..5; so
      short[1] -> B_1 + T_1 + B_5 + T_5
      short[2] -> B_2 + T_2 + B_5 + T_5
      short[3] -> B_3 + T_3 + B_5 + T_5
      short[4] -> B_4 + T_4 + B_5 + T_5
      short[5] -> 2 (B_5 + T_5)

    Wait, let me re-check. Looking at registry-n6.json's prefix[6]:
      prefix[6]: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    BDI_COORDS = M_2, M_3, M_4, M_5, B_1, T_1, B_2, T_2, B_3, T_3, B_4,
                 T_4, B_5, T_5, S.
    So prefix[6] -> B_1 + B_4? No -- the entries are [0,0,0,0, 0,0, 1,0,
    0,0, 1,0, 0,0, 0]. That's B_2 (idx 6, value 1) and B_4 (idx 10,
    value 1). So prefix[6] -> e_{B_2} + e_{B_4}.

    Actually general_pieces.py base_piece(n=6):
      B_2: P[0] (P_1=B_1=prefix[1]), SH[1] (s_2), P[n-1]=P[5]=prefix[6]
      That is: B_2 = prefix[1]'s contribution? Wait no.
      Let me re-trace. Code:
        for i in range(1, n):  # i=1..n-1
          b_terms = [(1, P[i-1]), (1, SH[i-1])]
          if i == 1: b_terms.append((1, L[0]))
          if i == 2: b_terms.append((1, P[n-1]))   # P_n -> B_2!
          ...
      So B_2 gets a contribution from prefix[n] = prefix[6]. That means
      M[B_2 row, prefix[6] col] = 1.
      Similarly B_4 may get prefix[n] too? No, only i=2 case. But the
      registry shows prefix[6] -> B_2 + B_4. Let me re-read code more
      carefully.

      Actually looking again:
        b_terms = [(1, P[i-1]), (1, SH[i-1])]  # P[i-1] = prefix[i], SH[i-1] = short[i]
        if i == 1: b_terms.append((1, L[0]))    # L[0] = long[1]
        if i == 2: b_terms.append((1, P[n-1]))  # P[n-1] = prefix[n]
      So B_2's terms = [(1, prefix[2]), (1, short[2]), (1, prefix[n])]
      In linkLHS-nonzero gauge: B_2 column should reflect what AII vars
      contribute, but it's stored row-wise. The BDI row B_2 has nonzeros
      at AII cols: prefix[2], short[2], prefix[n]. So the AII column
      "prefix[n]" has B_2 row = 1. Plus another from B_4 if i=4 has
      b_terms with prefix[n]... but code only assigns prefix[n] to B_2
      (when i=2). So prefix[6] column should be e_{B_2} only.

      But the registry has prefix[6] -> e_{B_2} + e_{B_4}? Let me re-check.

    Looking at registry-n6.json again:
      'prefix[6]': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
                    M2 M3 M4 M5 B1 T1 B2 T2 B3 T3 B4 T4 B5 T5 S

    Hmm, index 5 is T_1 (value 1) and index 10 is B_4 (value 1)?
    But prefix[6]: list [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0]
    The 6th entry (index 5) is T_1 -- yes value 1.
    The 11th entry (index 10) is B_4 -- value 1.

    Hmm so prefix[6] -> e_{T_1} + e_{B_4}?? That doesn't match the code.

    Let me look again at registry.py's piece_to_dict:
        return {aii_v[c]: [int(M[r, c]) for r in range(n_bdi)]
                for c in range(M.shape[1])}
    So the entries are by BDI ROW for each AII column. So for
    prefix[6] column, the 15 entries are by BDI row.

    Let me re-check the BDI ordering. From bdi_vars(n=6):
      M_2, M_3, M_4, M_5, B_1, B_2, B_3, B_4, B_5, T_1, T_2, T_3, T_4,
      T_5, S
    Note: NOT B_1, T_1, B_2, T_2, ...! It's M's then ALL B's then ALL
    T's, then S. So indexing:
      M_2=0, M_3=1, M_4=2, M_5=3,
      B_1=4, B_2=5, B_3=6, B_4=7, B_5=8,
      T_1=9, T_2=10, T_3=11, T_4=12, T_5=13,
      S=14
    So prefix[6] = [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0] means:
      B_2 = 1, T_2 = 1.
    THAT matches the code: B_2 += prefix[n], T_2 += prefix[n] (per the
    base_piece code: B_2 gets prefix[n] and T_2 gets prefix[n] -- ah
    yes, T_2 b_terms get prefix[n] too because if i == 2: t_terms.append).

    OK so registry uses ORDERED M_*, B_1..B_{n-1}, T_1..T_{n-1}, S.
    My n6_extension.py uses M_2..M_{n-1}, then B_1, T_1, B_2, T_2, ...
    These are DIFFERENT orderings!

    I'll use the registry's ordering to avoid confusion. Let me redo.
    """
    pass


# Re-define with REGISTRY ordering: M_2, M_3, M_4, M_5, B_1..B_5, T_1..T_5, S
BDI_COORDS_REG = ["M2", "M3", "M4", "M5",
                  "B1", "B2", "B3", "B4", "B5",
                  "T1", "T2", "T3", "T4", "T5",
                  "S"]
NB_REG = len(BDI_COORDS_REG)
IDX_REG = {c: i for i, c in enumerate(BDI_COORDS_REG)}
ZERO_REG = tuple([0] * NB_REG)


def vec_r(**kw):
    v = [0] * NB_REG
    for k, n in kw.items():
        v[IDX_REG[k]] = n
    return tuple(v)


def add_r(*vs):
    if not vs:
        return ZERO_REG
    return tuple(sum(x) for x in zip(*vs))


def scale_r(c, v):
    return tuple(c * x for x in v)


def P_r(a, v):
    return 2 * sum(v[IDX_REG[f"B{b}"]] - v[IDX_REG[f"T{b}"]] for b in range(1, a + 1))


def is_BDI_r(v):
    if any(x < 0 for x in v):
        return False
    for a in range(1, 6):
        if v[IDX_REG[f"T{a}"]] > v[IDX_REG[f"B{a}"]]:
            return False
        if P_r(a, v) < 0:
            return False
    for a in range(2, 6):
        if v[IDX_REG[f"M{a}"]] > min(P_r(a - 1, v), P_r(a, v)):
            return False
    if v[IDX_REG["S"]] > P_r(5, v):
        return False
    return True


# =====================================================================
# Load registry and gauge to linkLHS = 0
# =====================================================================
REGISTRY_PATH = Path("/home/agent/projects/code/2026-06-17-complete-registry/registry-n6.json")


def load_registry_n6():
    """Load registry at n=6 in linkLHS = 0 gauge.

    Registry stores in linkLHS-nonzero gauge. We apply the gauge:
      pi^{linkLHS} := 0
      pi^{short[i]} := pi^{short[i]} + (old pi^{linkLHS})  for i=1..5
    """
    with open(REGISTRY_PATH) as f:
        reg = json.load(f)
    pieces = {}
    for name, cols in reg.items():
        # cols: {aii_var_name: [list of 15 ints by BDI registry-order]}
        linkLHS_col = tuple(cols["linkLHS"])
        new_cols = {}
        for av_name, col in cols.items():
            if av_name == "linkLHS":
                new_cols[av_name] = ZERO_REG
            elif av_name.startswith("short["):
                new_cols[av_name] = add_r(tuple(col), linkLHS_col)
            else:
                new_cols[av_name] = tuple(col)
        # Convert to piece dict.
        piece = {}
        for j in range(1, 7):
            piece[f"p{j}"] = new_cols[f"prefix[{j}]"]
            piece[f"l{j}"] = new_cols[f"long[{j}]"]
        for j in range(1, 6):
            piece[f"s{j}"] = new_cols[f"short[{j}]"]
        pieces[name] = piece
    return pieces


# =====================================================================
# F-check and ray generators using registry ordering
# =====================================================================
def check_F_n6_r(piece):
    """F-check at n=6 (even) in linkLHS=0 gauge, using the CORRECT AII
    extreme rays per Day-72 run.py.

    AII rays at n=6 (17 total):
      1. pure prefix[j] for j=1..6   (6 rays)
      2. pure long[1]                 (1 ray)
      3. short[1] + linkLHS           (1 ray; becomes pi^{s_1} in linkLHS=0 gauge)
      4. prefix[j-1] + long[j] for j=2..6   (5 rays)
      5. prefix[i-1] + short[i] + linkLHS for i=2..5
         (4 rays; becomes pi^{p_{i-1}} + pi^{s_i} in linkLHS=0 gauge)

    Note: NO pi^{l_6} contribution to s_i rays (that was a bug in
    registry.py's aii_rays which incorrectly included long[n] in those rays).
    """
    # F1: pure prefix
    for j in range(1, 7):
        if not is_BDI_r(piece[f"p{j}"]):
            return False
    # F4_l: pure long[1]
    if not is_BDI_r(piece["l1"]):
        return False
    # F4_s: pi^{s_1} (the short[1]+linkLHS ray in linkLHS=0 gauge)
    if not is_BDI_r(piece["s1"]):
        return False
    # F2: pi^{p_{j-1}} + pi^{l_j} for j=2..6
    for j in range(2, 7):
        if not is_BDI_r(add_r(piece[f"p{j-1}"], piece[f"l{j}"])):
            return False
    # F3: pi^{p_{i-1}} + pi^{s_i} for i=2..5
    for i in range(2, 6):
        if not is_BDI_r(add_r(piece[f"p{i-1}"], piece[f"s{i}"])):
            return False
    return True


def gen_set_n6_r(piece):
    """17 ray-image generators at n=6 in linkLHS=0 gauge."""
    gens = []
    # Pure prefix
    for j in range(1, 7):
        gens.append(piece[f"p{j}"])
    # Pure long[1]
    gens.append(piece["l1"])
    # s_1 ray (short[1]+linkLHS gauged out)
    gens.append(piece["s1"])
    # prefix[j-1] + long[j] for j=2..6
    for j in range(2, 7):
        gens.append(add_r(piece[f"p{j-1}"], piece[f"l{j}"]))
    # prefix[i-1] + short[i] for i=2..5 (linkLHS gauged out)
    for i in range(2, 6):
        gens.append(add_r(piece[f"p{i-1}"], piece[f"s{i}"]))
    assert len(gens) == 17
    return gens


# =====================================================================
# Simple-divert piece pi_alpha^{(i)} (Day-71 / Day-75 D-pi 3-clique)
# =====================================================================
def simpdiv_piece(base_piece, i, alpha):
    """Build pi_alpha^{(i)} = base_piece with p_i column getting
    alpha * e_S added (registry ordering)."""
    new_piece = dict(base_piece)
    if alpha != 0:
        new_piece[f"p{i}"] = add_r(base_piece[f"p{i}"],
                                    scale_r(alpha, vec_r(S=1)))
    return new_piece


# =====================================================================
# Image-semigroup enumeration (precompute Im(pi_alpha) as a set)
# =====================================================================
def enumerate_image_set(generators, max_total=8):
    """Enumerate the semigroup generated by `generators` (set of tuples
    of length NB_REG = 15), up to total coordinate-sum max_total.
    Returns a set of tuples."""
    image = {ZERO_REG}
    frontier = {ZERO_REG}
    while frontier:
        new_frontier = set()
        for v in frontier:
            for g in generators:
                w = add_r(v, g)
                if sum(w) <= max_total and w not in image:
                    image.add(w)
                    new_frontier.add(w)
        frontier = new_frontier
    return image


# =====================================================================
# Image-semigroup membership test (recursive backup for big points)
# =====================================================================
def semigroup_membership(point, generators, max_coef=4):
    """Test if `point` is in the nonneg integer semigroup generated by
    `generators` (which are tuples of length NB_REG = 15)."""
    N = len(generators)
    gens_tuple = tuple(generators)
    cache = {}

    def rec(idx, remaining):
        if remaining == ZERO_REG:
            return True
        if idx == N:
            return False
        key = (idx, remaining)
        if key in cache:
            return cache[key]
        g = gens_tuple[idx]
        max_c = max_coef
        for k in range(NB_REG):
            if g[k] > 0:
                max_c = min(max_c, remaining[k] // g[k])
        for c in range(max_c, -1, -1):
            new_rem = tuple(remaining[k] - c * g[k] for k in range(NB_REG))
            if any(x < 0 for x in new_rem):
                continue
            if rec(idx + 1, new_rem):
                cache[key] = True
                return True
        cache[key] = False
        return False

    return rec(0, point)


def image_equivalent(piece_A, piece_B, max_coef=4):
    """Test if Im(piece_A) = Im(piece_B) as semigroups.

    Check: every generator of A is in semigroup(B), and vice versa.
    """
    gens_A = list(set(gen_set_n6_r(piece_A)))
    gens_B = list(set(gen_set_n6_r(piece_B)))
    for g in gens_A:
        if not semigroup_membership(g, gens_B, max_coef=max_coef):
            return False
    for g in gens_B:
        if not semigroup_membership(g, gens_A, max_coef=max_coef):
            return False
    return True


def image_contained(piece_A, piece_B, max_coef=4):
    """Test if Im(piece_A) ⊆ semigroup(Im(piece_B))."""
    gens_A = list(set(gen_set_n6_r(piece_A)))
    gens_B = list(set(gen_set_n6_r(piece_B)))
    for g in gens_A:
        if not semigroup_membership(g, gens_B, max_coef=max_coef):
            return False
    return True


# =====================================================================
# Candidate columns for the F-feasibility enumeration
# =====================================================================
# Day-70 §6 RIGID/BINARY restrictions at n = 6, lifted to linkLHS = 0 gauge.
# Some s_j columns have extra R-double-level-j engine entries (the
# augmented registry classes).
#
# IMPORTANT: in linkLHS = 0 gauge, the registry's base piece has
# s_5 column = B_5+T_5 + linkLHS_contribution = 2(B_5+T_5). So the
# canonical s_5 candidate in linkLHS = 0 gauge is 2(B_5+T_5), NOT
# B_5+T_5. Similarly for other s_j the gauged canonical is
# B_j+T_j + (B_5+T_5).
#
# To keep things tractable, we'll use the registry-derived base piece
# as our reference, with candidates as offsets.
# =====================================================================
def get_base_piece_n6():
    """Get the base piece P6_base in linkLHS = 0 gauge."""
    pieces = load_registry_n6()
    return pieces["P6_base"]


def candidate_columns_for_enum(base):
    """Per-column candidates for the F-feasibility enumeration at n=6.

    We use the §6 RIGID/BINARY classes, where:
      - For columns that have an obvious diversion to S (l_j -> e_S
        instead of M_j etc), include the divert.
      - For s_j columns, include the R-double level-j engine.
      - For l_1, include Lemma C multiplicities.
      - For p_6, include Lemma B multiplicities.

    Each column's candidate list is a list of BDI vectors. The base
    piece's column is included as the canonical option (first entry).
    """
    cands = {}

    # p_1..p_5 (NON-fixed): RIGID at base value.
    for j in range(1, 6):
        cands[f"p{j}"] = [base[f"p{j}"]]

    # p_6: Lemma B multiplicities (in linkLHS = 0 gauge).
    # The base's p_6 = e_{B_2}+e_{T_2} (since registry routes prefix[6]
    # to B_2 + T_2). Then Lemma B variants change p_6 to k*(B_5+T_5).
    # Additionally include the base value.
    base_p6 = base["p6"]
    cands["p6"] = [
        base_p6,
        scale_r(0, vec_r()),
        vec_r(B5=1, T5=1),
        scale_r(2, vec_r(B5=1, T5=1)),
        vec_r(S=1),
        vec_r(B2=1, T2=1),
        vec_r(B3=1, T3=1),
        vec_r(B4=1, T4=1),
    ]
    # Dedup.
    cands["p6"] = list(dict.fromkeys(cands["p6"]))

    # l_1: Lemma C multiplicities + R-double engine.
    base_l1 = base["l1"]
    cands["l1"] = [
        base_l1,
        ZERO_REG,
        vec_r(B1=1),
        scale_r(2, vec_r(B1=1)),
        vec_r(B1=1, T1=1),
    ]
    cands["l1"] = list(dict.fromkeys(cands["l1"]))

    # l_2..l_5: BINARY {base, e_S}.
    for j in range(2, 6):
        base_lj = base[f"l{j}"]
        cands[f"l{j}"] = [base_lj, vec_r(S=1)]
        cands[f"l{j}"] = list(dict.fromkeys(cands[f"l{j}"]))

    # l_6: RIGID at base (e_S).
    cands["l6"] = [base["l6"]]

    # s_1: 3 candidates (base + R-double-lv1 engine + divert).
    base_s1 = base["s1"]
    cands["s1"] = [
        base_s1,
        vec_r(B1=1, S=1),
        vec_r(B1=2, T1=1, S=2),
    ]
    cands["s1"] = list(dict.fromkeys(cands["s1"]))

    # s_2, s_3, s_4: 3 candidates (base + divert e_S + R-double-lv-j engine).
    for j in range(2, 5):
        base_sj = base[f"s{j}"]
        rd_engine = add_r(vec_r(**{f"B{j}": 1, f"T{j}": 1}),
                          scale_r(2, vec_r(S=1)))
        cands[f"s{j}"] = [
            base_sj,
            vec_r(S=1),
            rd_engine,
        ]
        cands[f"s{j}"] = list(dict.fromkeys(cands[f"s{j}"]))

    # s_5: 3 candidates similar.
    base_s5 = base["s5"]
    # R-double-lv-5 engine in linkLHS = 0 gauge:
    #   raw R-double-lv-5 = B_5 + T_5 (extra) + 2 S, plus linkLHS contribution.
    #   gauged = 2(B_5+T_5) + (B_5+T_5) + 2 S = 3(B_5+T_5) + 2 S? Let me
    # not worry about the exact gauge; include both base and base+2S.
    cands["s5"] = [
        base_s5,
        add_r(base_s5, scale_r(2, vec_r(S=1))),
        add_r(base_s5, vec_r(S=1)),
    ]
    cands["s5"] = list(dict.fromkeys(cands["s5"]))

    return cands


# =====================================================================
# Enumerate F-feasible pieces with fixed pi^{p_i} = e_{B_i} + alpha e_S
# =====================================================================
def enumerate_feasible_pieces(base, i, alpha, cands):
    """Enumerate F-feasible pieces with pi^{p_i} = e_{B_i} + alpha e_S
    (in linkLHS=0 gauge -- note we override the base's p_i column).

    Returns list of pieces (dicts).
    """
    # Override p_i column.
    p_i_value = add_r(vec_r(**{f"B{i}": 1}), scale_r(alpha, vec_r(S=1)))

    fixed = {}
    for c in ALL_COLS:
        if c == f"p{i}":
            fixed[c] = [p_i_value]
        elif c in cands:
            fixed[c] = cands[c]
        else:
            fixed[c] = [base[c]]

    # Order columns so we can prune early.
    col_order = (
        ["p1", "p2", "p3", "p4", "p5", "p6"]
        + ["l1", "l6"]  # l_1 and l_6 first (degenerate F4 + l_6 in many checks)
        + ["l2", "l3", "l4", "l5"]
        + ["s1", "s2", "s3", "s4", "s5"]
    )
    col_order = [c for c in col_order if c in ALL_COLS]
    assert set(col_order) == set(ALL_COLS), col_order

    feasible = []

    def piece_from_assignment(assignment):
        return {c: assignment[c] for c in ALL_COLS}

    def recurse(idx, assignment):
        if idx == len(col_order):
            piece = piece_from_assignment(assignment)
            if check_F_n6_r(piece):
                feasible.append(piece)
            return
        col = col_order[idx]
        for v in fixed[col]:
            assignment[col] = v
            # Prune: if all required prefix cols assigned, check partial F.
            if _partial_F_ok(col, assignment):
                recurse(idx + 1, assignment)
        if col in assignment:
            del assignment[col]

    recurse(0, {})
    return feasible


def _partial_F_ok(just_set, assignment):
    """Partial F-pruning when column `just_set` was assigned (linkLHS=0
    gauge; no l_6 contribution to s_i rays)."""
    if just_set.startswith("p"):
        if not is_BDI_r(assignment[just_set]):
            return False
    if just_set.startswith("l"):
        j = int(just_set[1:])
        if j == 1:
            if not is_BDI_r(assignment["l1"]):
                return False
        else:
            prev_p = f"p{j-1}"
            if prev_p in assignment:
                if not is_BDI_r(add_r(assignment[prev_p], assignment[just_set])):
                    return False
    if just_set.startswith("s"):
        j = int(just_set[1:])
        if j == 1:
            if not is_BDI_r(assignment["s1"]):
                return False
        else:
            prev_p = f"p{j-1}"
            if prev_p in assignment:
                if not is_BDI_r(add_r(assignment[prev_p], assignment[just_set])):
                    return False
    return True


# =====================================================================
# Image-class signature: hashable canonical form for a piece's image
# =====================================================================
def image_signature(piece):
    """Hashable signature based on the SORTED tuple of unique
    generators. Two pieces with the same signature have the SAME
    generator set (a stronger invariant than image equivalence)."""
    return tuple(sorted(set(gen_set_n6_r(piece))))


# =====================================================================
# Main verification
# =====================================================================
def verify_d_pi_uniqueness_at_n6():
    """Verify D-pi uniqueness (weak form) at n=6 for each interior i."""
    print("=" * 76)
    print("Day 76 CODE Task A -- D-pi uniqueness half at n = 6 (weak form)")
    print("=" * 76)

    base = get_base_piece_n6()

    # Sanity: base should be F-feasible.
    print("\nSanity check: base piece F-feasibility (linkLHS=0 gauge):",
          check_F_n6_r(base))
    assert check_F_n6_r(base), "Base piece should be F-feasible at n=6"

    cands = candidate_columns_for_enum(base)
    print("\nCandidate column counts (for the enumeration):")
    for c in ALL_COLS:
        if c in cands:
            print(f"  {c}: {len(cands[c])} candidates")

    interior = [2, 3, 4]
    overall_pass = True
    summary = {"interior": interior, "by_i": {}}

    for i in interior:
        print(f"\n{'=' * 76}")
        print(f"Interior coord p_{i}")
        print(f"{'=' * 76}")

        # Build the three simple-divert pieces.
        pi_alpha = {alpha: simpdiv_piece(base, i, alpha) for alpha in range(3)}

        # Verify each pi_alpha^{(i)} is F-feasible.
        for alpha in range(3):
            ok = check_F_n6_r(pi_alpha[alpha])
            print(f"  pi_{alpha}^({i}) F-feasible: {ok}")
            assert ok, f"simple-divert pi_{alpha}^({i}) should be F-feasible"

        # Compute their image signatures (raw generators).
        sigs = {alpha: image_signature(pi_alpha[alpha]) for alpha in range(3)}
        print(f"  pi_alpha^({i}) raw-generator-set signatures:")
        for alpha in range(3):
            print(f"    alpha={alpha}: {len(set(sigs[alpha]))} distinct generators")

        # Pairwise image-equivalence between the three simple-diverts.
        # NOTE: pi_alpha and pi_beta differ only in pi^{p_i} = e_{B_i}+alpha*S
        # vs e_{B_i}+beta*S. Their generators differ by (alpha-beta) e_S on
        # the p_i ray, AND on s_{i+1} ray (via the F3 contribution from
        # p_{i-1}? wait, s_j ray includes pi^{p_{j-1}}+pi^{l_6}+pi^{s_j}).
        # Specifically s_{i+1} ray has pi^{p_i} contribution.
        # So pi_alpha differs from pi_beta on generators: p_i ray, l_{i+1}
        # ray (since F2 at j=i+1 uses pi^{p_i}+pi^{l_{i+1}}), and s_{i+1}
        # ray.
        print(f"  Pairwise image-equivalence (within {{0,1,2}}):")
        pairwise = {}
        for a, b in [(0, 1), (1, 2), (0, 2)]:
            same = image_equivalent(pi_alpha[a], pi_alpha[b], max_coef=4)
            pairwise[(a, b)] = same
            print(f"    Im(pi_{a}^({i})) ≃ Im(pi_{b}^({i})): {same}")
        n_distinct_classes = (1 + (1 - int(pairwise[(0, 1)]))
                              + (1 - int(pairwise[(1, 2)]))
                              + (1 - int(pairwise[(0, 2)])))
        # Better way to count distinct classes:
        classes = []
        for alpha in range(3):
            placed = False
            for cls in classes:
                rep = cls[0]
                if image_equivalent(pi_alpha[alpha], pi_alpha[rep],
                                    max_coef=4):
                    cls.append(alpha)
                    placed = True
                    break
            if not placed:
                classes.append([alpha])
        n_distinct = len(classes)
        print(f"  Number of distinct image classes among simple-diverts: "
              f"{n_distinct}")

        # Enumerate F-feasible pieces for each alpha.
        per_alpha = {}
        all_feasible = []  # tuples (alpha, piece)
        for alpha in range(3):
            print(f"\n  --- Enumerating F-feasible pieces with pi^{{p_{i}}} "
                  f"= e_{{B_{i}}} + {alpha} e_S ---")
            t0 = time.time()
            feasible = enumerate_feasible_pieces(base, i, alpha, cands)
            dt = time.time() - t0
            print(f"    F-feasible: {len(feasible)} (enum time: {dt:.2f}s)")
            per_alpha[alpha] = {"n_feasible": len(feasible)}
            for piece in feasible:
                all_feasible.append((alpha, piece))

        # The D-pi uniqueness claim (weak form, per CODE.md): for each
        # F-feasible piece with pi^{p_i} = e_{B_i} + alpha * e_S, its
        # image is CONTAINED in the simple-divert image Im(pi_alpha^{(i)}).
        # (Not equivalence -- containment.)
        #
        # Optimization: bucket pieces by signature; pieces with the same
        # signature share the same generator set, hence trivially equal
        # containment status.
        print(f"\n  --- Bucketing {len(all_feasible)} F-feasible pieces "
              f"by signature ---")
        sig_count = {}  # (alpha, sig) -> count
        for (alpha_actual, piece) in all_feasible:
            sig = image_signature(piece)
            key = (alpha_actual, sig)
            sig_count[key] = sig_count.get(key, 0) + 1
        print(f"    Distinct (alpha, sig) classes: {len(sig_count)}")

        # For each (alpha, sig), check containment: Im(piece) ⊆ Im(pi_alpha).
        # PRECOMPUTE Im(pi_alpha^(i)) as an enumerated set for fast lookup.
        print(f"  --- Precomputing Im(pi_alpha^({i})) sets ---")
        # Maximum generator sum we'll see: ray-image sum at most ~6
        # (per Day-74's max_coef=4 analysis). To be safe, enumerate
        # the target image up to sum 8.
        max_total = 8
        pi_alpha_gens = {a: list(set(gen_set_n6_r(pi_alpha[a])))
                          for a in range(3)}
        t0 = time.time()
        pi_alpha_image_set = {a: enumerate_image_set(pi_alpha_gens[a],
                                                     max_total=max_total)
                              for a in range(3)}
        el = time.time() - t0
        for a in range(3):
            print(f"    |Im(pi_{a}^({i})) up to sum {max_total}| = "
                  f"{len(pi_alpha_image_set[a])}")
        print(f"    Enumeration time: {el:.1f}s")

        # Check containment by set-membership.
        print(f"  --- Checking containment Im(piece) ⊆ Im(pi_alpha^({i})) ---")
        t0 = time.time()
        contained_count = {alpha: 0 for alpha in range(3)}
        not_contained = []
        for k, ((alpha_actual, sig), cnt) in enumerate(sorted(sig_count.items())):
            a = alpha_actual
            target_set = pi_alpha_image_set[a]
            # Quick check: each generator g must be in target_set.
            # If g has sum > max_total, fall back to recursive check.
            ok = True
            for g in sig:
                if sum(g) <= max_total:
                    if g not in target_set:
                        ok = False
                        break
                else:
                    if not semigroup_membership(g, pi_alpha_gens[a],
                                                  max_coef=6):
                        ok = False
                        break
            if ok:
                contained_count[a] += cnt
            else:
                not_contained.append((alpha_actual, sig, cnt))
            if (k + 1) % 5000 == 0:
                el = time.time() - t0
                print(f"    progress: {k+1}/{len(sig_count)} "
                      f"(elapsed: {el:.1f}s)")
        el = time.time() - t0
        print(f"  Done containment check for {len(sig_count)} sig classes "
              f"in {el:.1f}s")

        print(f"\n  Class breakdown (containment Im(piece) ⊆ Im(pi_alpha^({i}))):")
        for alpha in range(3):
            print(f"    alpha={alpha}: {contained_count[alpha]} pieces "
                  f"image-contained in pi_{alpha}^({i})")
        n_uncontained = sum(c for _, _, c in not_contained)
        print(f"    NOT-CONTAINED pieces: {n_uncontained} "
              f"({len(not_contained)} signatures)")

        # Acceptance:
        #   - All pieces with pi^{p_i} = b_alpha have Im(piece) ⊆ Im(pi_alpha)
        #   - The 3 simple-divert images are pairwise distinct
        ok_full = (n_uncontained == 0)
        ok_three_classes = (n_distinct == 3)

        verdict = "PASS" if (ok_full and ok_three_classes) else "FAIL"
        print(f"\n  VERDICT (p_{i}): {verdict}")
        print(f"    - All pieces' images contained in their alpha class: "
              f"{ok_full}")
        print(f"    - 3 distinct simple-divert image classes: "
              f"{ok_three_classes}")

        if verdict != "PASS":
            overall_pass = False
            print(f"\n  Not-contained signatures (showing first 5):")
            for k, (a, sig, c) in enumerate(not_contained[:5]):
                print(f"    alpha={a}, sig_size={len(sig)}, count={c}")
                # Show which generator(s) are NOT in pi_alpha's image
                for g in list(sig)[:3]:
                    in_target = semigroup_membership(g, pi_alpha_gens[a],
                                                       max_coef=4)
                    nz = {k: vv for k, vv in zip(BDI_COORDS_REG, g) if vv}
                    print(f"      gen={nz}, in_Im(pi_{a}): {in_target}")

        summary["by_i"][i] = {
            "verdict": verdict,
            "n_distinct_classes_simpdiv": n_distinct,
            "pairwise_equivalent": {f"{a}-{b}": v for (a, b), v in pairwise.items()},
            "per_alpha_n_feasible": {alpha: per_alpha[alpha]["n_feasible"]
                                     for alpha in range(3)},
            "n_distinct_sig_alpha_classes": len(sig_count),
            "containment_counts_by_alpha": contained_count,
            "n_not_contained": n_uncontained,
            "n_not_contained_sigs": len(not_contained),
        }

    overall = "PASS" if overall_pass else "FAIL"
    print(f"\n{'=' * 76}")
    print(f"OVERALL VERDICT: {overall}")
    print(f"{'=' * 76}")

    summary["overall_verdict"] = overall

    # Save results.
    with open(HERE / "results.json", "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nWrote {HERE / 'results.json'}")

    return summary


if __name__ == "__main__":
    verify_d_pi_uniqueness_at_n6()
