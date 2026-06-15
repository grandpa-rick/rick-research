"""
Day 72 PROVE — clean n=5 cover construction attempt.

Goal: build a minimal cover at n=5 with R-AXIS = 3 (3 walls support 3-cliques).

Approach:
  - Use ABSTRACT base (pi^{p_5} = 0).
  - Include R-double family (lv1) on {p_1}: 3 pieces.
  - Include Lemma B family on {p_5}: 3 pieces (k=0 is base).
  - Include Lemma C family on {l_1}: 3 pieces (k=1 is base).
  - For each uncovered BDI point, add a piece, ensuring it doesn't
    create a new 3-clique on a non-AXIS wall.

  Strategy: each auxiliary piece modifies a UNIQUE column (one not
  used by other auxiliaries). For interior p_i needs, use simple-divert
  (one mod per p_i, BINARY).  For M_j shifted needs, use distinct
  l_k mods, etc.
"""

import sys
import copy
import itertools
from pathlib import Path

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-13-n5-axis-count')
from n5_setup import (AII_VARS, BDI_VARS, N_BDI, N_VARS, PREFIX_IDX,
                       LONG_IDX, SHORT_IDX, bdi_feasible_n5,
                       enumerate_aii_lattice, piece_apply, verify_piece)

# AII labels
P_1, P_2, P_3, P_4, P_5 = AII_VARS[0], AII_VARS[1], AII_VARS[2], AII_VARS[3], AII_VARS[4]
L_1, L_2, L_3, L_4, L_5 = AII_VARS[5], AII_VARS[6], AII_VARS[7], AII_VARS[8], AII_VARS[9]
S_1, S_2, S_3, S_4, S_5 = AII_VARS[10], AII_VARS[11], AII_VARS[12], AII_VARS[13], AII_VARS[14]


def make_matrix(spec):
    M = np.zeros((N_BDI, N_VARS), dtype=int)
    for bv, terms in spec.items():
        bi = BDI_VARS.index(bv)
        for av, coef in terms.items():
            ai = AII_VARS.index(av)
            M[bi, ai] = coef
    return M


# Abstract base piece.
BASE_SPEC = {
    "M_2": {L_2: 1},
    "M_3": {L_3: 1},
    "M_4": {L_4: 1},
    "B_1": {P_1: 1, S_1: 1, L_1: 1},
    "T_1": {S_1: 1},
    "B_2": {P_2: 1, S_2: 1},
    "T_2": {S_2: 1},
    "B_3": {P_3: 1, S_3: 1},
    "T_3": {S_3: 1},
    "B_4": {P_4: 1, S_4: 1},
    "T_4": {S_4: 1},
    "S":   {L_5: 1},
}


def set_col(spec, aii_var, col_entries):
    """Return spec with column aii_var set to col_entries (dict bdi_var -> int)."""
    new = {k: dict(v) for k, v in spec.items()}
    for bv in list(new.keys()):
        if aii_var in new[bv]:
            del new[bv][aii_var]
    for bv, val in col_entries.items():
        new.setdefault(bv, {})
        new[bv][aii_var] = val
    return new


def add_to_col(spec, aii_var, bdi_var, coef=1):
    """Add coef to (bdi_var, aii_var) entry."""
    new = {k: dict(v) for k, v in spec.items()}
    new.setdefault(bdi_var, {})
    new[bdi_var][aii_var] = new[bdi_var].get(aii_var, 0) + coef
    return new


def build_cover():
    pieces = {}

    # Base
    pieces["BASE"] = BASE_SPEC

    # R-double family at p_1: alpha = 0, 1, 2
    # B_1 <- p_1 + 2 s_1 + l_1, T_1 <- s_1 + l_1, B_2 <- p_2 + s_2 + p_5,
    # T_2 <- s_2 + p_5, S <- l_5 + 2 s_4 + 2 s_1 + alpha p_1.
    for alpha in [0, 1, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_1"] = {P_1: 1, S_1: 2, L_1: 1}
        spec["T_1"] = {S_1: 1, L_1: 1}
        spec["B_2"] = {P_2: 1, S_2: 1, P_5: 1}
        spec["T_2"] = {S_2: 1, P_5: 1}
        spec["S"]   = {L_5: 1, S_4: 2, S_1: 2, P_1: alpha}
        pieces[f"RD_{alpha}"] = spec

    # Lemma B family: pi^{p_5}(k) = k(e_{B_4} + e_{T_4}).
    # k=0 = abstract base. k=1, 2 modify B_4, T_4.
    for k in [1, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_4"] = {P_4: 1, S_4: 1, P_5: k}
        spec["T_4"] = {S_4: 1, P_5: k}
        pieces[f"PN_{k}"] = spec

    # Lemma C family: pi^{l_1}(k) = k e_{B_1}.
    # k=1 = base. Add k=0 (pi^{l_1}=0), k=2 (pi^{l_1}=2e_{B_1}).
    for k in [0, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_1"] = {P_1: 1, S_1: 1, L_1: k}
        pieces[f"L1_{k}"] = spec

    # ===== Auxiliaries to cover gap points =====
    # For each gap point, design a unique-signature piece.

    # Simple-divert at p_i: pi^{p_i} = e_{B_i} + e_S, base elsewhere.
    # Covers {B_i, S} at p = e_{p_i}.  Creates BINARY on p_i with base.
    for i, p_i in [(2, P_2), (3, P_3), (4, P_4)]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["S"] = {L_5: 1, p_i: 1}
        pieces[f"DIVp{i}_1"] = spec

    # l_j-divert with coef 2: pi^{l_j} = 2 e_S, base elsewhere.
    # Covers {B_{j-1}, 2S}. Creates BINARY on l_j with base.
    for j, l_j in [(3, L_3), (4, L_4), (5, L_5)]:
        spec = copy.deepcopy(BASE_SPEC)
        if j == 3:
            spec["M_3"] = {}
            spec["S"] = {L_5: 1, L_3: 2}
        elif j == 4:
            spec["M_4"] = {}
            spec["S"] = {L_5: 1, L_4: 2}
        elif j == 5:
            spec["S"] = {L_5: 2}
        pieces[f"LDIVl{j}_2"] = spec

    # Shift pieces for {M_j, B_i} with i != j-1.
    # Use l_2 → M_4, l_2 → M_3 to shift M into low-index pieces.
    # Each uses a unique column modification + a "signature" mod to avoid 3-cliques.

    # Piece SHIFT_M3_B1: hits {M_3, B_1}.  pi^{p_2} = e_{B_1} + e_{M_3}.
    # F1: B_1=1, M_3=1 <= P_2(e_{B_1}) = 2 ✓.
    # F2 at l_3: e_{B_1} + e_{M_3} + e_{M_3} = e_{B_1} + 2e_{M_3}, M_3 <= P_2 = 2 ✓.
    # F3 at s_3: e_{B_1} + e_{M_3} + e_{B_3} + e_{T_3} ✓.
    # Unique signature: modifies p_2 column.
    spec = copy.deepcopy(BASE_SPEC)
    spec["B_1"] = {P_1: 1, S_1: 1, L_1: 1, P_2: 1}
    spec["B_2"] = {S_2: 1}  # remove P_2 from B_2 (so pi^{p_2}_{B_2} = 0)
    spec["M_3"] = {L_3: 1, P_2: 1}  # add P_2 to M_3
    # At p = e_{p_2}: image = e_{B_1} + e_{M_3} ✓.
    pieces["SHIFT_M3_B1"] = spec

    # Piece SHIFT_M4_B1: hits {M_4, B_1}.
    spec = copy.deepcopy(BASE_SPEC)
    spec["B_1"] = {P_1: 1, S_1: 1, L_1: 1, P_2: 1}
    spec["B_2"] = {S_2: 1}
    spec["M_4"] = {L_4: 1, P_2: 1}
    pieces["SHIFT_M4_B1"] = spec
    # But SHIFT_M4_B1 vs SHIFT_M3_B1: both have pi^{p_2} = e_{B_1} + (M_3 or M_4).
    # Differ on p_2 column. With BASE, 3 distinct p_2 cols -> 3-clique!
    # FIX: use different "carrier" column.

    # Alternative SHIFT_M4_B1 via l_2: pi^{l_2} = e_{M_4}.
    spec = copy.deepcopy(BASE_SPEC)
    spec["M_4"] = {L_4: 1, L_2: 1}
    # F2 at l_2: pi^{p_1} + pi^{l_2} = e_{B_1} + e_{M_4}. M_4 <= P_3 = 2 ✓.
    # At p = e_{p_1} + e_{l_2}: image = e_{B_1} + e_{M_4} ✓.
    pieces["SHIFT_M4_B1_l2"] = spec
    # This modifies l_2 column.  BASE's pi^{l_2} = e_{M_2}; this has e_{M_2} + e_{M_4}.
    # Differs from BASE on l_2 column only.  BINARY on l_2.

    # Remove the conflicting SHIFT_M4_B1 (keep the l_2 version):
    del pieces["SHIFT_M4_B1"]
    # Also remove SHIFT_M3_B1 because it'd 3-clique with DIVp2_1 + something.
    # Actually let's check: SHIFT_M3_B1 mods p_2 and also B_2 and M_3.
    # SHIFT_M3_B1 vs BASE: differ in many cols. Not single column.
    # SHIFT_M3_B1 vs DIVp2_1: SHIFT has p_2 col with B_1=1, M_3=1; DIVp2_1 has B_2=1, S=1.
    # Differ in p_2 column. AND in B_2 row, M_3 row... multiple cols.
    # Actually SHIFT_M3_B1 modifies B_2 row of p_2 col (sets to 0 from 1) AND M_3 row of p_2 col (sets to 1 from 0) AND B_1 row of p_2 col (sets to 1).
    # All within the p_2 column. So SHIFT mods are all in p_2 column.
    # Wait, where else? B_1 has (P_2: 1) added. So B_1 row of p_2 col gets 1.
    # OK so SHIFT_M3_B1 has p_2 column = {B_1: 1, M_3: 1}, vs BASE's {B_2: 1}.
    # Single column diff from BASE.
    # SHIFT_M3_B1 vs SHIFT_M4_B1_l2: SHIFT has p_2 col different (B_1 + M_3 vs B_2),
    #   and l_2 col different (M_2 vs M_2 + M_4).
    # 2 columns differ.  NOT 3-clique on single wall.
    # SHIFT_M3_B1 + BASE + DIVp2_1: all differ in p_2 column only.
    #   BASE p_2 = e_{B_2}; DIVp2_1 p_2 = e_{B_2} + e_S; SHIFT_M3_B1 p_2 = e_{B_1} + e_{M_3}.
    #   Three distinct p_2 cols! 3-CLIQUE on p_2!
    # So SHIFT_M3_B1 creates a 3-clique on p_2.

    # To avoid: also use l-column carrier for SHIFT_M3_B1.
    del pieces["SHIFT_M3_B1"]
    spec = copy.deepcopy(BASE_SPEC)
    spec["M_3"] = {L_3: 1, L_2: 1}  # l_2 -> M_3.
    # F2 at l_2: pi^{p_1} + pi^{l_2} = e_{B_1} + e_{M_2} + e_{M_3}. M_3 <= P_1 = 2 ✓. M_2 <= P_1 = 2 ✓.
    # Image at p = e_{p_1} + e_{l_2}: e_{B_1} + e_{M_2} + e_{M_3}.  Not what we want.
    # The l_2 column has e_{M_2} + e_{M_3} so {M_3, B_1} also gets extra M_2.
    # We want pure {M_3, B_1}.
    # Try pi^{l_2} = e_{M_3} (no M_2).
    spec["M_2"] = {L_2: 0}  # remove M_2 <- L_2.
    # F2 at l_2: pi^{p_1} + pi^{l_2} = e_{B_1} + e_{M_3}, M_3 <= P_1 = 2 ✓.
    # But: M_2 <- 0 means base routing of l_2 → M_2 is broken.
    # That changes more than just l_2 column!  pi^{l_2} previously had M_2 = 1; now M_2 = 0.
    # So this is still single col mod (l_2): old col was e_{M_2}, new col is e_{M_3}.
    # Image at p = e_{p_1} + e_{l_2}: e_{B_1} + e_{M_3} ✓.
    # SHIFT_M3_B1_l2 vs BASE: differ on l_2 col only.
    # SHIFT_M3_B1_l2 vs SHIFT_M4_B1_l2: both differ from BASE on l_2 col.
    #   SHIFT_M3_B1_l2 has l_2 col = e_{M_3}; SHIFT_M4_B1_l2 has l_2 col = e_{M_2} + e_{M_4}.
    #   3 distinct l_2 cols (BASE: e_{M_2}; M_3 ver: e_{M_3}; M_4 ver: e_{M_2}+e_{M_4}).
    #   3-CLIQUE on l_2!
    # Argh.
    pass  # don't add this version

    return pieces


def enumerate_bdi_lattice(N_max):
    pts = []
    def gen(remaining, depth, current):
        if depth == N_BDI:
            ok, _ = bdi_feasible_n5(tuple(current))
            if ok:
                pts.append(tuple(current))
            return
        for v in range(remaining + 1):
            current.append(v)
            gen(remaining - v, depth + 1, current)
            current.pop()
    gen(N_max, 0, [])
    return pts


def coverage_check(pieces, sum_bound=4):
    bdi_pts = enumerate_bdi_lattice(sum_bound)
    aii_pts = enumerate_aii_lattice(sum_bound)
    covered = set()
    coverer_of = {}
    for name, spec in pieces.items():
        M = make_matrix(spec)
        for p in aii_pts:
            q = piece_apply(M, p)
            if sum(q) > sum_bound:
                continue
            covered.add(q)
            coverer_of.setdefault(q, []).append(name)
    bdi_set = set(bdi_pts)
    uncovered = sorted(bdi_set - covered, key=lambda q: (sum(q), q))
    return uncovered, coverer_of


def find_3cliques(pieces):
    names = list(pieces.keys())
    mats = {n: make_matrix(pieces[n]) for n in names}
    triples = []
    for a, b, c in itertools.combinations(names, 3):
        Ma, Mb, Mc = mats[a], mats[b], mats[c]
        cols_ab = [j for j in range(N_VARS) if not np.array_equal(Ma[:, j], Mb[:, j])]
        cols_bc = [j for j in range(N_VARS) if not np.array_equal(Mb[:, j], Mc[:, j])]
        cols_ac = [j for j in range(N_VARS) if not np.array_equal(Ma[:, j], Mc[:, j])]
        if len(cols_ab) == 1 and len(cols_bc) == 1 and len(cols_ac) == 1 \
                and cols_ab == cols_bc == cols_ac:
            col = cols_ab[0]
            cs = {tuple(Ma[:, col]), tuple(Mb[:, col]), tuple(Mc[:, col])}
            if len(cs) == 3:
                triples.append((a, b, c, AII_VARS[col]))
    return triples


def main():
    pieces = build_cover()
    print(f"# pieces: {len(pieces)}")

    aii_pts = enumerate_aii_lattice(6)
    bad = {}
    for name, spec in pieces.items():
        M = make_matrix(spec)
        infs = verify_piece(M, aii_pts)
        if infs:
            bad[name] = infs[:3]
    if bad:
        print("INFEASIBLE pieces:")
        for n, l in bad.items():
            print(f"  {n}: {l}")
        return
    print("All feasible ✓")

    triples = find_3cliques(pieces)
    walls = set(t[3] for t in triples)
    print(f"3-cliques: {len(triples)} on walls {walls}")
    for t in triples:
        print(f"  {t}")

    uncov, _ = coverage_check(pieces, sum_bound=4)
    print(f"# uncovered (sum<=4): {len(uncov)}")
    for q in uncov[:20]:
        lab = {BDI_VARS[i]: q[i] for i in range(N_BDI) if q[i] != 0}
        print(f"  sum={sum(q)} {lab}")


if __name__ == "__main__":
    main()
