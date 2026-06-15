"""
Day 72 PROVE — extended n=5 cover construction.

Strategy: each gap-cover piece modifies TWO columns from base, with a unique
modification signature, so no triple of cover pieces can pairwise differ on a
single column.
"""

import sys
import copy
import itertools

import numpy as np

sys.path.insert(0, '/home/agent/projects/code/2026-06-13-n5-axis-count')
from n5_setup import (AII_VARS, BDI_VARS, N_BDI, N_VARS,
                       bdi_feasible_n5, enumerate_aii_lattice,
                       piece_apply, verify_piece)

P_1, P_2, P_3, P_4, P_5 = AII_VARS[0:5]
L_1, L_2, L_3, L_4, L_5 = AII_VARS[5:10]
S_1, S_2, S_3, S_4, S_5 = AII_VARS[10:15]


def make_matrix(spec):
    M = np.zeros((N_BDI, N_VARS), dtype=int)
    for bv, terms in spec.items():
        bi = BDI_VARS.index(bv)
        for av, coef in terms.items():
            ai = AII_VARS.index(av)
            M[bi, ai] = coef
    return M


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


def zero_col(spec, aii_var):
    new = {k: dict(v) for k, v in spec.items()}
    for bv in list(new.keys()):
        if aii_var in new[bv]:
            del new[bv][aii_var]
    return new


def set_col(spec, aii_var, bdi_dict):
    new = zero_col(spec, aii_var)
    for bv, val in bdi_dict.items():
        new.setdefault(bv, {})
        new[bv][aii_var] = val
    return new


def build_cover_v2():
    pieces = {}
    pieces["BASE"] = BASE_SPEC

    # --- AXIS families ---
    # R-double at p_1
    for alpha in [0, 1, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_1"] = {P_1: 1, S_1: 2, L_1: 1}
        spec["T_1"] = {S_1: 1, L_1: 1}
        spec["B_2"] = {P_2: 1, S_2: 1, P_5: 1}
        spec["T_2"] = {S_2: 1, P_5: 1}
        spec["S"]   = {L_5: 1, S_4: 2, S_1: 2, P_1: alpha}
        pieces[f"RD_{alpha}"] = spec

    # Lemma B at p_5
    for k in [1, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_4"] = {P_4: 1, S_4: 1, P_5: k}
        spec["T_4"] = {S_4: 1, P_5: k}
        pieces[f"PN_{k}"] = spec

    # Lemma C at l_1
    for k in [0, 2]:
        spec = copy.deepcopy(BASE_SPEC)
        spec["B_1"] = {P_1: 1, S_1: 1, L_1: k}
        pieces[f"L1_{k}"] = spec

    # --- Auxiliaries with UNIQUE multi-column signatures ---
    # Each auxiliary modifies a UNIQUE pair of columns from base.
    # Pair (a, b): tracks (column1, column2).

    # AUX_1: pi^{p_2} = e_{B_2} + e_S, pi^{s_3} = e_{B_3} + e_{T_3} + e_{T_4}
    # Covers {B_2, S} = (1, 1) at p = e_{p_2}.
    # Signature: (p_2, s_3).
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, P_2, {"B_2": 1, "S": 1})  # pi^{p_2} = e_{B_2} + e_S
    spec = set_col(spec, S_3, {"B_3": 1, "T_3": 1, "T_4": 1})  # signature mod
    # Check feasibility of s_3 col: T_4 <= B_4 = 0 -- not in col alone, but F3 at s_3:
    # pi^{p_2} + pi^{s_3} = e_{B_2} + e_S + e_{B_3} + e_{T_3} + e_{T_4}.
    # T_4 <= B_4 in sum: B_4 from sum = 0, T_4 = 1.  FAILS.
    # Revert sig:
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, P_2, {"B_2": 1, "S": 1})
    spec = set_col(spec, S_3, {"B_3": 1, "T_3": 1, "B_4": 1, "T_4": 1})  # add (B_4, T_4) balanced
    # F3 at s_3: pi^{p_2} + pi^{s_3} = e_{B_2} + e_S + e_{B_3} + e_{T_3} + e_{B_4} + e_{T_4}.
    # B_4 = 1, T_4 = 1: T_4 <= B_4 ✓.
    # P_4 = 2(B_2-0) + 2(B_3-T_3) + 2(B_4-T_4) = 2 + 0 + 0 = 2.  S = 1 <= 2 ✓.
    # M's = 0 <= P's ✓.  ✓.
    # Hmm but s_3 = 1 in AII requires p_2 >= 1, so we get extra image from p_2.
    # At p = e_{p_2}: image = pi^{p_2} = e_{B_2} + e_S. (s_3 = 0).
    # So this hits {B_2, S} ✓.  Signature: (p_2, s_3).
    pieces["AUX_B2_S"] = spec

    # AUX_2: pi^{p_3} = e_{B_3} + e_S, pi^{s_4} signature.
    # Covers {B_3, S}.
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, P_3, {"B_3": 1, "S": 1})
    spec = set_col(spec, S_4, {"B_4": 1, "T_4": 1, "B_3": 1, "T_3": 1})
    # F3 at s_4: pi^{p_3} + pi^{s_4} = e_{B_3} + e_S + e_{B_4} + e_{T_4} + e_{B_3} + e_{T_3}
    #                                = 2e_{B_3} + e_{T_3} + e_{B_4} + e_{T_4} + e_S.
    # T_3 <= 2 ✓, T_4 <= 1 ✓.
    # P_4 = 2(2-1) + 2(1-1) + ... = 2.  S = 1 <= 2 ✓.
    # Hmm wait does the s_4 col have B_3 = 1?  Then AII point with s_4 > 0 has p_3 >= s_4 (Main_4)
    #  giving extra B_3 etc. Anyway, at p = e_{p_3}: image = pi^{p_3} = e_{B_3} + e_S. ✓
    pieces["AUX_B3_S"] = spec

    # AUX_3: pi^{p_4} = e_{B_4} + e_S, pi^{s_5} signature.
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, P_4, {"B_4": 1, "S": 1})
    spec = set_col(spec, S_5, {"S": 1})  # add signature: s_5 -> S
    # F3 at s_5: pi^{p_4} + pi^{s_5} = e_{B_4} + e_S + e_S = e_{B_4} + 2 e_S.
    # S = 2 <= P_4(e_{B_4}) = 2 ✓.
    # At p = e_{p_4}: image = e_{B_4} + e_S ✓.
    pieces["AUX_B4_S"] = spec

    # AUX_4: pi^{l_3} = 2 e_S, pi^{p_2} unchanged.  Covers {B_2, 2 S}.
    # Modify l_3 only. Signature: (l_3, l_4) — need second column mod.
    # Use l_4 with M_4 added redundantly: M_4 + L_4 (already in base; canonical).
    # Hmm need genuine signature.  Try: l_3 -> 2 e_S AND s_2 -> e_{B_2} + e_{T_2} + e_{T_3} (signature).
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, L_3, {"S": 2})
    spec = set_col(spec, S_2, {"B_2": 1, "T_2": 1, "T_3": 1})  # signature
    # F3 at s_2: pi^{p_1} + pi^{s_2} = e_{B_1} + e_{B_2} + e_{T_2} + e_{T_3}.
    # T_3 <= B_3 in sum: B_3 = 0, T_3 = 1.  FAILS.
    # Fix: add B_3.
    spec = set_col(spec, S_2, {"B_2": 1, "T_2": 1, "B_3": 1, "T_3": 1})
    # F3 at s_2: e_{B_1} + e_{B_2} + e_{T_2} + e_{B_3} + e_{T_3}.  T_3 = 1 <= B_3 = 1 ✓.
    # P_4 = 2(1) + 2(1-1) + 2(1-1) + 0 = 2.  All ok.
    # F2 at l_3: pi^{p_2} + pi^{l_3} = e_{B_2} + 2e_S.  S = 2 <= P_4 = 2 ✓.
    # At p = e_{p_2} + e_{l_3}: image = e_{B_2} + 2e_S ✓.  Covers {B_2, 2S}.
    pieces["AUX_B2_2S"] = spec

    # AUX_5: pi^{l_4} = 2 e_S, signature s_3.
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, L_4, {"S": 2})
    spec = set_col(spec, S_3, {"B_3": 1, "T_3": 1, "B_4": 1, "T_4": 1})  # NOTE shared with AUX_B3_S
    # WAIT this has same s_3 signature as AUX_B3_S.  So AUX_B2_2S' s_3 (base) vs
    # AUX_B3_S's s_3 vs AUX_5's s_3 — both AUX_B3_S and AUX_5 have non-base s_3.
    # If they share same s_3 column, AUX_B3_S and AUX_5 differ only on
    # (p_3, l_4) — multiple columns.  Not 3-clique.
    # Anyway, let me just pick a different signature for AUX_5.
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, L_4, {"S": 2})
    spec = set_col(spec, S_2, {"B_2": 1, "T_2": 1, "B_4": 1, "T_4": 1})  # different signature
    # F3 at s_2: pi^{p_1} + pi^{s_2} = e_{B_1} + e_{B_2} + e_{T_2} + e_{B_4} + e_{T_4}.
    # T_4 <= B_4 ✓.  P_4 = 2(1) + 0 + 0 + 0 = 2. ✓.
    # F2 at l_4: pi^{p_3} + 2e_S = e_{B_3} + 2e_S.  S = 2 <= P_4 = 2 ✓.
    # At p = e_{p_3} + e_{l_4}: image = e_{B_3} + 2 e_S ✓.
    pieces["AUX_B3_2S"] = spec

    # AUX_6: pi^{l_5} = 2 e_S, signature s_4.
    spec = copy.deepcopy(BASE_SPEC)
    spec = set_col(spec, L_5, {"S": 2})
    spec = set_col(spec, S_4, {"B_4": 1, "T_4": 1, "B_3": 1, "T_3": 1})  # signature
    # F3 at s_4: pi^{p_3} + e_{B_4} + e_{T_4} + e_{B_3} + e_{T_3} = e_{B_3} + e_{B_4} + e_{T_4} + e_{B_3} + e_{T_3}
    #          = 2e_{B_3} + e_{T_3} + e_{B_4} + e_{T_4}.  T_3 <= B_3, T_4 <= B_4 ✓.
    # F2 at l_5: pi^{p_4} + 2 e_S = e_{B_4} + 2 e_S.  S = 2 <= P_4(e_{B_4}) = 2 ✓.
    # At p = e_{p_4} + e_{l_5}: image = e_{B_4} + 2 e_S ✓.
    pieces["AUX_B4_2S"] = spec

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


def coverage_check(pieces, sum_bound=4):
    bdi_pts = enumerate_bdi_lattice(sum_bound)
    aii_pts = enumerate_aii_lattice(sum_bound)
    covered = set()
    for name, spec in pieces.items():
        M = make_matrix(spec)
        for p in aii_pts:
            q = piece_apply(M, p)
            if sum(q) <= sum_bound:
                covered.add(q)
    return sorted(set(bdi_pts) - covered, key=lambda q: (sum(q), q))


def main():
    pieces = build_cover_v2()
    print(f"# pieces: {len(pieces)}")
    aii_pts = enumerate_aii_lattice(6)

    # Feasibility
    bad = {}
    for name, spec in pieces.items():
        M = make_matrix(spec)
        infs = verify_piece(M, aii_pts)
        if infs:
            bad[name] = infs[:2]
    if bad:
        print("INFEASIBLE:")
        for n, l in bad.items():
            print(f"  {n}: {len(l)} samples; first: {l[0]}")
        return
    print("Feasible ✓")

    triples = find_3cliques(pieces)
    walls = set(t[3] for t in triples)
    print(f"3-cliques: {len(triples)} on walls {walls}")
    for t in triples:
        print(f"  {t}")

    uncov = coverage_check(pieces, sum_bound=4)
    print(f"Uncovered (sum<=4): {len(uncov)}")
    for q in uncov[:30]:
        lab = {BDI_VARS[i]: q[i] for i in range(N_BDI) if q[i] != 0}
        print(f"  sum={sum(q)} {lab}")


if __name__ == "__main__":
    main()
