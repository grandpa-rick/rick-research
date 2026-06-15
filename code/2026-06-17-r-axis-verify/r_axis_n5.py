"""
Day 72 PROVE — R-AXIS(5) = 3: explicit minimal cover construction.

Strategy:
  1. Define "abstract base" piece at n=5 (with pi^{p_5} = 0).
  2. Add R-double family (3 pieces, 3-clique on {p_1 = 0}).
  3. Add Lemma B family (free-top p_5: 3 pieces, 3-clique on {p_5 = 0}).
  4. Add Lemma C family (free-bottom l_1: 3 pieces, 3-clique on {l_1 = 0}).
  5. Add SIMPLE-DIVERT pieces at interior i (i=2,3): pi_1^{(i)}, covering
     e_{B_i} + e_S. Each gives BINARY on {p_i = 0} with base.
  6. Add L-DIVERT pieces pi^{[l_j -> 2 e_S]} for j=3,4,5: covering
     e_{B_{j-1}} + 2 e_S. Each gives BINARY on {l_j = 0} with base.
  7. Add pi_1^{(4)} for e_{B_4} + e_S. BINARY on {p_4 = 0}.
  8. Add auxiliary pieces for remaining uncovered points.

Verify:
  (a) Each piece is BDI-feasible on AII lattice sum <= 6.
  (b) Cover Im (sum <= 4) contains all of T_5 (sum <= 4).
  (c) Identify all 3-cliques (pairs of 3 pieces sharing all-but-one column).
  (d) Check the only 3-cliques are on {p_1, p_5, l_1}.
  (e) Verify minimality: each piece uniquely covers some BDI point.
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

# BDI indices
M_2, M_3, M_4 = 0, 1, 2
B_1, T_1, B_2, T_2, B_3, T_3, B_4, T_4, S = 3, 4, 5, 6, 7, 8, 9, 10, 11


def make_matrix(spec):
    """spec: dict mapping BDI var name -> dict (AII var name -> int coef).

    Construct a 12 x 15 piece matrix.
    """
    M = np.zeros((N_BDI, N_VARS), dtype=int)
    for bv, terms in spec.items():
        bi = BDI_VARS.index(bv)
        for av, coef in terms.items():
            ai = AII_VARS.index(av)
            M[bi, ai] = coef
    return M


# ---------------------------------------------------------------------
# ABSTRACT base piece at n=5: pi^{p_5} = 0
# ---------------------------------------------------------------------
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


def add_col_term(spec, bdi_var, aii_var, coef=1):
    """Return a NEW spec with coef added to (bdi_var, aii_var)."""
    new = {k: dict(v) for k, v in spec.items()}
    new.setdefault(bdi_var, {})
    new[bdi_var][aii_var] = new[bdi_var].get(aii_var, 0) + coef
    return new


def set_col(spec, aii_var, col_entries):
    """Return spec with the (single) column aii_var set to col_entries dict {bdi_var: val}."""
    new = {k: dict(v) for k, v in spec.items()}
    # Remove all current entries with aii_var.
    for bv in list(new.keys()):
        if aii_var in new[bv]:
            del new[bv][aii_var]
    # Set new entries.
    for bv, val in col_entries.items():
        new.setdefault(bv, {})
        new[bv][aii_var] = val
    return new


# ---------------------------------------------------------------------
# Build cover
# ---------------------------------------------------------------------
def build_cover():
    pieces = {}

    # Base
    pieces["BASE"] = BASE_SPEC

    # R-double family at p_1: alpha = 0, 1, 2
    # B_1 <- p_1 + 2 s_1 + l_1, T_1 <- s_1 + l_1, B_2 <- p_2 + s_2 + p_n,
    # T_2 <- s_2 + p_n, S <- l_5 + 2 s_4 + 2 s_1 + alpha p_1.
    # (s_{n-1} = s_4 at n=5)
    for alpha in [0, 1, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_1"] = {P_1: 1, S_1: 2, L_1: 1}
        spec["T_1"] = {S_1: 1, L_1: 1}
        spec["B_2"] = {P_2: 1, S_2: 1, P_5: 1}
        spec["T_2"] = {S_2: 1, P_5: 1}
        spec["S"]   = {L_5: 1, S_4: 2, S_1: 2, P_1: alpha}
        pieces[f"RD_{alpha}"] = spec

    # Lemma B family: pi^{p_5}(k) = k (e_{B_4} + e_{T_4}).
    # B_4 <- p_4 + s_4 + k p_5, T_4 <- s_4 + k p_5.
    # k=0 = base. Add k=1, k=2.
    for k in [1, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_4"] = {P_4: 1, S_4: 1, P_5: k}
        spec["T_4"] = {S_4: 1, P_5: k}
        pieces[f"PN_{k}"] = spec

    # Lemma C family: pi^{l_1}(k) = k e_{B_1}.
    # B_1 <- p_1 + s_1 + k l_1.
    # k=1 = base. Add k=0, k=2.
    for k in [0, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_1"] = {P_1: 1, S_1: 1, L_1: k}
        pieces[f"L1_{k}"] = spec

    # Simple-divert at p_i for i in {2, 3, 4}, alpha = 1.
    # pi^{p_i} = e_{B_i} + e_S, base elsewhere.
    # Modify: add (1, p_i) to S row.
    for i, p_i in [(2, P_2), (3, P_3), (4, P_4)]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["S"] = {L_5: 1, p_i: 1}
        pieces[f"DIVp{i}_1"] = spec

    # L-divert at l_j for j in {3, 4, 5}: pi^{l_j} = 2 e_S, base elsewhere.
    # M_j: remove (1, l_j); S: add (2, l_j).
    for j, l_j in [(3, L_3), (4, L_4), (5, L_5)]:
        spec = copy.deepcopy(BASE_SPEC)
        # Remove M_j entry (if exists) for j=3,4. For j=5, no M_5 anyway, base has S <- L_5.
        if j == 3:
            spec["M_3"] = {}
            spec["S"] = {L_5: 1, L_3: 2}
        elif j == 4:
            spec["M_4"] = {}
            spec["S"] = {L_5: 1, L_4: 2}
        elif j == 5:
            spec["S"] = {L_5: 2}
        pieces[f"LDIVl{j}_2"] = spec

    return pieces


# ---------------------------------------------------------------------
# Verify feasibility
# ---------------------------------------------------------------------
def verify_all_feasible(pieces, sum_bound=6):
    aii_pts = enumerate_aii_lattice(sum_bound)
    print(f"# AII pts sum<={sum_bound}: {len(aii_pts)}")
    bad = {}
    for name, spec in pieces.items():
        M = make_matrix(spec)
        infeasibilities = verify_piece(M, aii_pts)
        if infeasibilities:
            bad[name] = infeasibilities[:5]
    if bad:
        print(f"INFEASIBLE pieces:")
        for name, infeas in bad.items():
            print(f"  {name}: {len(infeas)} sample infeasibilities")
            for p, q, err in infeas[:3]:
                lab_p = {AII_VARS[i]: p[i] for i in range(N_VARS) if p[i] != 0}
                lab_q = {BDI_VARS[i]: q[i] for i in range(N_BDI) if q[i] != 0}
                print(f"    p={lab_p}, q={lab_q}, err={err}")
        return False
    print("All pieces feasible ✓")
    return True


# ---------------------------------------------------------------------
# Coverage check (over BDI lattice up to sum_bound)
# ---------------------------------------------------------------------
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
    print(f"\n=== Coverage check at sum <= {sum_bound} ===")
    bdi_pts = enumerate_bdi_lattice(sum_bound)
    aii_pts = enumerate_aii_lattice(sum_bound)
    print(f"# BDI pts: {len(bdi_pts)}, # AII pts: {len(aii_pts)}")

    covered = set()
    coverer_of = {}
    for name, spec in pieces.items():
        M = make_matrix(spec)
        for p in aii_pts:
            q = piece_apply(M, p)
            if sum(q) > sum_bound:
                continue
            if q not in coverer_of:
                coverer_of[q] = []
            coverer_of[q].append(name)
            covered.add(q)

    bdi_set = set(bdi_pts)
    uncovered = sorted(bdi_set - covered, key=lambda q: (sum(q), q))
    print(f"# covered BDI pts: {len(bdi_set & covered)} / {len(bdi_set)}")
    print(f"# uncovered: {len(uncovered)}")
    if uncovered:
        print("Sample uncovered:")
        for q in uncovered[:30]:
            lab = {BDI_VARS[i]: q[i] for i in range(N_BDI) if q[i] != 0}
            print(f"  sum={sum(q)}  {lab}")
    return uncovered, coverer_of


# ---------------------------------------------------------------------
# 3-clique detection
# ---------------------------------------------------------------------
def find_3cliques(pieces):
    """Find all triples (a, b, c) of piece names such that pieces a, b, c
    pairwise differ ONLY on a single AII column."""
    names = list(pieces.keys())
    mats = {n: make_matrix(pieces[n]) for n in names}

    triples = []  # (a, b, c, AII col index where they differ)
    for a, b, c in itertools.combinations(names, 3):
        Ma, Mb, Mc = mats[a], mats[b], mats[c]
        # Find columns where they differ pairwise
        cols_ab = [j for j in range(N_VARS) if not np.array_equal(Ma[:, j], Mb[:, j])]
        cols_bc = [j for j in range(N_VARS) if not np.array_equal(Mb[:, j], Mc[:, j])]
        cols_ac = [j for j in range(N_VARS) if not np.array_equal(Ma[:, j], Mc[:, j])]
        # Need all pairs to differ in exactly one column, and the same column,
        # and have 3 distinct values there.
        if len(cols_ab) == 1 and len(cols_bc) == 1 and len(cols_ac) == 1:
            if cols_ab == cols_bc == cols_ac:
                col = cols_ab[0]
                # check 3 distinct cols
                col_a = tuple(Ma[:, col])
                col_b = tuple(Mb[:, col])
                col_c = tuple(Mc[:, col])
                if len({col_a, col_b, col_c}) == 3:
                    triples.append((a, b, c, AII_VARS[col]))
    return triples


# ---------------------------------------------------------------------
# Minimality check
# ---------------------------------------------------------------------
def minimality_check(pieces, sum_bound=4):
    """For each piece, check it uniquely covers some BDI point at sum <= sum_bound."""
    print(f"\n=== Minimality check at sum <= {sum_bound} ===")
    aii_pts = enumerate_aii_lattice(sum_bound)

    # Compute image of each piece (restricted to sum <= sum_bound).
    images = {}
    for name, spec in pieces.items():
        M = make_matrix(spec)
        img = set()
        for p in aii_pts:
            q = piece_apply(M, p)
            if sum(q) <= sum_bound:
                img.add(q)
        images[name] = img

    print(f"Piece | unique BDI points covered (at sum <= {sum_bound}):")
    redundant = []
    for name in pieces:
        others_union = set()
        for n2 in pieces:
            if n2 != name:
                others_union |= images[n2]
        unique = images[name] - others_union
        print(f"  {name:>15}: {len(unique)} unique")
        if len(unique) == 0:
            redundant.append(name)
    if redundant:
        print(f"\nREDUNDANT pieces (at sum <= {sum_bound}): {redundant}")
    return redundant


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    pieces = build_cover()
    print(f"# pieces in cover: {len(pieces)}")
    for name in pieces:
        print(f"  {name}")

    print("\n=== Feasibility ===")
    if not verify_all_feasible(pieces, sum_bound=6):
        print("ABORTING due to infeasible pieces.")
        return

    print("\n=== 3-clique detection ===")
    triples = find_3cliques(pieces)
    print(f"# 3-cliques found: {len(triples)}")
    walls = set()
    for a, b, c, col in triples:
        print(f"  ({a}, {b}, {c}) on col {col}")
        walls.add(col)
    print(f"Distinct walls: {walls}")

    uncov, _ = coverage_check(pieces, sum_bound=4)

    redundant = minimality_check(pieces, sum_bound=4)


if __name__ == "__main__":
    main()
