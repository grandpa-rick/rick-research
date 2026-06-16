#!/usr/bin/env python3
"""
Day-74 CODE Task A — finite verification of Conjecture 6.2 at n = 5.

CLAIM (Day-73 Conjecture 6.2, strong form):
  Let pi be a BDI-feasible piece at n = 5 with
      pi^{p_1} = b_2 = e_{B_1} + 2 e_S
      pi^{l_2} = e_{M_2}.
  Then pi's non-{p_1, l_2} columns are uniquely determined
  (up to BDI-equivalence) as the Day-69 R-double-rest profile.

VERIFICATION strategy (Day-70 §6 RIGID/BINARY restrictions):
  Restrict each non-{p_1, l_2} column to its Day-70 §6 image-class
  representative + extended candidates for AXIS columns (p_5, l_1,
  s_1) and for the s_4 R-double engine. Enumerate F1-F4 feasibility.
  Group by image semigroup equivalence (relative to a reference cover
  containing base, R-double family, Lemma B/C, divert variants).

OUTCOME (Day-74):
  Conjecture 6.2 strong form is PRODUCTIVELY FALSIFIED:
    - 4320 F-feasible pieces satisfy pi^{p_1} = b_2, pi^{l_2} = e_{M_2}.
    - Only pi^{s_2} is uniquely F-forced (= e_{B_2} + e_{T_2}).
    - 3456 / 4320 pieces have image-semigroup contained in the
      reference cover's joint image.
    - 18 pieces are image-EQUIVALENT to R-double-alpha=2 in the
      strong sense (their image semigroups CONTAIN R-double-alpha=2's
      image). These 18 are explained by a 3-parameter image-class
      freedom on {l_1, s_1, s_5}: 3 * 2 * 3 = 18.

The corrected statement (Day-74 Theorem 6.2; see
proofs/2026-06-19-r-axis-uniform-1-n5.md) replaces "rest uniquely
forced" with "rest image-equivalent up to (l_1, s_1, s_5) freedom".
"""
from itertools import product
import json
import sys
from pathlib import Path

# === n=5 BDI coords ===
BDI_COORDS = ["M2", "M3", "M4", "B1", "T1", "B2", "T2", "B3", "T3", "B4", "T4", "S"]
NB = len(BDI_COORDS)
IDX = {c: i for i, c in enumerate(BDI_COORDS)}


def vec(**kw):
    v = [0] * NB
    for k, n in kw.items():
        v[IDX[k]] = n
    return tuple(v)


def add(*vs):
    if not vs:
        return tuple([0] * NB)
    return tuple(sum(x) for x in zip(*vs))


def scale(c, v):
    return tuple(c * x for x in v)


def P(a, v):
    """P_a = 2 sum_{b<=a} (B_b - T_b)."""
    return 2 * sum(v[IDX[f"B{b}"]] - v[IDX[f"T{b}"]] for b in range(1, a + 1))


def is_BDI(v):
    """Day-70 BDI feasibility at n = 5: T_a <= B_a, P_a >= 0,
    M_a <= min(P_{a-1}, P_a), S <= P_4, all >= 0."""
    if any(x < 0 for x in v):
        return False
    for a in range(1, 5):
        if v[IDX[f"T{a}"]] > v[IDX[f"B{a}"]]:
            return False
        if P(a, v) < 0:
            return False
    for a in range(2, 5):
        if v[IDX[f"M{a}"]] > min(P(a - 1, v), P(a, v)):
            return False
    if v[IDX["S"]] > P(4, v):
        return False
    return True


# === Piece machinery ===
COLS = ["p1", "p2", "p3", "p4", "p5",
        "l1", "l2", "l3", "l4", "l5",
        "s1", "s2", "s3", "s4", "s5"]


def make_piece(**kw):
    for c in COLS:
        assert c in kw, f"missing column {c}"
    return {c: kw[c] for c in COLS}


def check_F(piece):
    """Day-70 Thm 4.2 ray-image-feasibility:
       F1: pi^{p_j} in BDI                          for j = 1..5
       F2: pi^{p_{j-1}} + pi^{l_j} in BDI           for j = 2..5
       F3: pi^{p_{j-1}} + pi^{s_j} in BDI           for j = 2..5
       F4: pi^{l_1}, pi^{s_1} in BDI."""
    for j in range(1, 6):
        if not is_BDI(piece[f"p{j}"]):
            return False
    for j in range(2, 6):
        if not is_BDI(add(piece[f"p{j-1}"], piece[f"l{j}"])):
            return False
        if not is_BDI(add(piece[f"p{j-1}"], piece[f"s{j}"])):
            return False
    if not is_BDI(piece["l1"]):
        return False
    if not is_BDI(piece["s1"]):
        return False
    return True


def gen_set(piece):
    """The 15 ray-images of a piece (Day-70 Lemma 4.1)."""
    gens = []
    for j in range(1, 6):
        gens.append(piece[f"p{j}"])
    gens.append(piece["l1"])
    gens.append(piece["s1"])
    for j in range(2, 6):
        gens.append(add(piece[f"p{j-1}"], piece[f"l{j}"]))
    for j in range(2, 6):
        gens.append(add(piece[f"p{j-1}"], piece[f"s{j}"]))
    return gens


# === Reference cover pieces (Day-72 / Day-73) ===
base_piece = make_piece(
    p1=vec(B1=1), p2=vec(B2=1), p3=vec(B3=1), p4=vec(B4=1), p5=vec(),
    l1=vec(B1=1), l2=vec(M2=1), l3=vec(M3=1), l4=vec(M4=1), l5=vec(S=1),
    s1=vec(B1=1, T1=1), s2=vec(B2=1, T2=1), s3=vec(B3=1, T3=1),
    s4=vec(B4=1, T4=1), s5=vec(),
)


def rdouble(alpha):
    """Day-69 R-double piece with pi^{p_1} = b_alpha."""
    return make_piece(
        p1=vec(B1=1, S=alpha), p2=vec(B2=1), p3=vec(B3=1), p4=vec(B4=1),
        p5=vec(B2=1, T2=1),
        l1=vec(B1=1, T1=1), l2=vec(M2=1), l3=vec(M3=1), l4=vec(M4=1),
        l5=vec(S=1),
        s1=vec(B1=2, T1=1, S=2), s2=vec(B2=1, T2=1), s3=vec(B3=1, T3=1),
        s4=vec(B4=1, T4=1, S=2), s5=vec(),
    )


def lemmaB(k):
    """Day-69 Lemma B piece: pi^{p_5} = k(e_{B_4} + e_{T_4})."""
    p = dict(base_piece)
    p["p5"] = scale(k, vec(B4=1, T4=1))
    return p


def lemmaC(k):
    """Day-69 Lemma C piece: pi^{l_1} = k e_{B_1}."""
    p = dict(base_piece)
    p["l1"] = vec(B1=k)
    return p


def divert_variant(col, value):
    """Day-70 §6 divert variant: base with one column replaced."""
    p = dict(base_piece)
    p[col] = value
    return p


# Build reference cover = {base, RD(0,1,2), B(0,1,2), C(0,1,2), divert variants}.
cover_pieces = [base_piece]
for a in range(3):
    cover_pieces.append(rdouble(a))
for k in range(3):
    cover_pieces.append(lemmaB(k))
for k in range(3):
    cover_pieces.append(lemmaC(k))
# Standard divert variants of base:
for c in ["l3", "l4", "s2", "s3", "s4"]:
    cover_pieces.append(divert_variant(c, vec(S=1)))

# Sanity-check feasibility of cover pieces.
for i, p in enumerate(cover_pieces):
    assert check_F(p), f"cover piece {i} infeasible — review setup"

cover_gens = set()
for p in cover_pieces:
    cover_gens.update(gen_set(p))

print("=" * 70)
print("Day-74 CODE Task A — Conjecture 6.2 finite check at n = 5")
print("=" * 70)
print(f"\nReference cover: {len(cover_pieces)} pieces, "
      f"{len(cover_gens)} distinct ray-image generators")


# === Enumerate F-feasible pieces with pi^{p_1} = b_2, pi^{l_2} = e_{M_2} ===
# Restrict candidate columns to Day-70 §6 RIGID/BINARY + extended AXIS classes.

p1_b2 = vec(B1=1, S=2)
p2_can = vec(B2=1)
p3_can = vec(B3=1)
p4_can = vec(B4=1)
l2_M2 = vec(M2=1)
l5_S = vec(S=1)

p5_cands = [vec(),
            vec(B4=1, T4=1), scale(2, vec(B4=1, T4=1)),
            vec(B2=1, T2=1), vec(B3=1, T3=1), vec(S=1)]
l1_cands = [vec(), vec(B1=1), vec(B1=2), vec(B1=1, T1=1)]
l3_cands = [vec(M3=1), vec(S=1)]
l4_cands = [vec(M4=1), vec(S=1)]
s1_cands = [vec(B1=1, T1=1), vec(B1=2, T1=1, S=2), vec(B1=1, S=1)]
s2_cands = [vec(B2=1, T2=1), vec(S=1)]
s3_cands = [vec(B3=1, T3=1), vec(S=1)]
s4_cands = [vec(B4=1, T4=1), vec(B4=1, T4=1, S=2), vec(S=1)]
s5_cands = [vec(), vec(B4=1), vec(S=1)]

s1_cands = [v for v in s1_cands if is_BDI(v)]

print("\nCandidate counts (Day-70 §6 + extended AXIS):")
for nm, cs in [("p_5", p5_cands), ("l_1", l1_cands),
               ("l_3", l3_cands), ("l_4", l4_cands),
               ("s_1", s1_cands), ("s_2", s2_cands),
               ("s_3", s3_cands), ("s_4", s4_cands), ("s_5", s5_cands)]:
    print(f"  pi^{nm}: {len(cs)} candidates")

total = 1
for cs in [p5_cands, l1_cands, l3_cands, l4_cands,
           s1_cands, s2_cands, s3_cands, s4_cands, s5_cands]:
    total *= len(cs)
print(f"  Total enumeration size (before F1-F4 filter): {total}")

feasible_pieces = []
for p5v, l1v, l3v, l4v, s1v, s2v, s3v, s4v, s5v in product(
        p5_cands, l1_cands, l3_cands, l4_cands,
        s1_cands, s2_cands, s3_cands, s4_cands, s5_cands):
    piece = make_piece(
        p1=p1_b2, p2=p2_can, p3=p3_can, p4=p4_can, p5=p5v,
        l1=l1v, l2=l2_M2, l3=l3v, l4=l4v, l5=l5_S,
        s1=s1v, s2=s2v, s3=s3v, s4=s4v, s5=s5v,
    )
    if check_F(piece):
        feasible_pieces.append(piece)

print(f"\nF-feasible pieces: {len(feasible_pieces)} "
      f"(of {total} candidates)")


# === Per-column F-forcing analysis ===
print("\n[F-forcing] columns that are F-uniquely-forced across all "
      f"{len(feasible_pieces)} feasible pieces:")
free_cols = []
for c in ["p5", "l1", "l3", "l4", "s1", "s2", "s3", "s4", "s5"]:
    vals = set(piece[c] for piece in feasible_pieces)
    if len(vals) == 1:
        v = list(vals)[0]
        nz = {k: vv for k, vv in zip(BDI_COORDS, v) if vv}
        print(f"  pi^{c} FORCED = {nz}")
    else:
        free_cols.append((c, len(vals), vals))
        print(f"  pi^{c}: {len(vals)} F-allowed values (NOT F-forced)")


# === Image-semigroup membership ===
def semigroup_membership(point, generators, max_coef=4):
    """Test point in nonneg integer cone(generators)."""
    N = len(generators)
    gens_tuple = tuple(generators)
    cache = {}

    def rec(i, remaining):
        if remaining == tuple([0] * NB):
            return True
        if i == N:
            return False
        key = (i, remaining)
        if key in cache:
            return cache[key]
        g = gens_tuple[i]
        max_c = max_coef
        for k in range(NB):
            if g[k] > 0:
                max_c = min(max_c, remaining[k] // g[k])
        for c in range(max_c + 1):
            new_rem = tuple(remaining[k] - c * g[k] for k in range(NB))
            if any(x < 0 for x in new_rem):
                continue
            if rec(i + 1, new_rem):
                cache[key] = True
                return True
        cache[key] = False
        return False
    return rec(0, point)


# === Image-containment check vs. reference cover ===
print("\n[Image-redundancy] checking each F-feasible piece's generators "
      "vs. reference cover...")
ref_gens_list = sorted(cover_gens)
contained_pieces = []
not_contained = 0
for i, piece in enumerate(feasible_pieces):
    all_in = True
    for g in gen_set(piece):
        if not semigroup_membership(g, ref_gens_list, max_coef=4):
            all_in = False
            break
    if all_in:
        contained_pieces.append(piece)
    else:
        not_contained += 1
    if (i + 1) % 1000 == 0:
        print(f"    progress: {i+1}/{len(feasible_pieces)}")

print(f"\n  Pieces image-contained in reference cover:   {len(contained_pieces)}")
print(f"  Pieces with at least one NEW generator:      {not_contained}")


# === Image-equivalence to R-double-alpha=2 ===
rd2 = rdouble(2)
rd2_gens = sorted(set(gen_set(rd2)))

print("\n[Image-equivalence to R-double-α=2] "
      "find F-feasible pieces whose image contains Im(R-double-α=2)...")
rd_equiv = []
for piece in feasible_pieces:
    piece_gens = list(set(gen_set(piece)))
    if all(semigroup_membership(g, piece_gens, max_coef=4) for g in rd2_gens):
        rd_equiv.append(piece)

print(f"\n  Pieces image-CONTAINING Im(R-double-α=2): {len(rd_equiv)}")

if rd_equiv:
    # Tabulate free-column distribution among the 18 (expected) image-eqv pieces.
    print("\n  Distribution of free columns among image-equivalent pieces:")
    for c in ["p5", "l1", "l3", "l4", "s1", "s2", "s3", "s4", "s5"]:
        vals = sorted(set(piece[c] for piece in rd_equiv))
        if len(vals) > 1:
            print(f"    pi^{c}: {len(vals)} distinct value(s)")
            for v in vals:
                nz = {k: vv for k, vv in zip(BDI_COORDS, v) if vv}
                print(f"      {nz}")


# === REPORT line ===
print("\n" + "=" * 70)
report_status = "FALSIFIED" if len(rd_equiv) > 1 else "CONFIRMED"
print(f"REPORT: Conjecture 6.2 (strong form) is {report_status} at n = 5.")
print(f"        F-feasible: {len(feasible_pieces)}; "
      f"image-contained: {len(contained_pieces)}; "
      f"image-eqv to R-double-α=2: {len(rd_equiv)}.")
print("        Corrected (Day-74) Theorem 6.2 carries the "
      "image-equivalence class statement.")
print("=" * 70)

# === Save results to JSON ===
out = {
    "n_feasible": len(feasible_pieces),
    "n_image_contained_in_cover": len(contained_pieces),
    "n_image_equivalent_to_rdouble_alpha2": len(rd_equiv),
    "F_forced_columns": [
        c for c in ["p5", "l1", "l3", "l4", "s1", "s2", "s3", "s4", "s5"]
        if len(set(piece[c] for piece in feasible_pieces)) == 1
    ],
    "F_free_columns": [
        {"col": c, "n_values": n,
         "values": [{"".join(k for k, vv in zip(BDI_COORDS, v) if vv) or "0":
                     [vv for vv in v if vv]}
                    for v in vals]}
        for c, n, vals in free_cols
    ],
    "conjecture_6_2_strong_form": report_status,
}
out_path = Path(__file__).parent / "results.json"
with open(out_path, "w") as f:
    json.dump(out, f, indent=2, default=str)
print(f"\nWrote results to {out_path}")
