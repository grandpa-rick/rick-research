#!/usr/bin/env python3
"""
Day-74 CODE v2: extended finite check of Conjecture 6.2 at n = 5.

This adds the standard DIVERT VARIANT pieces of base to the reference cover,
and re-checks image-redundancy.

Hypothesis: with divert variants included, the unique image-irredundant piece
with pi^{p_1} = b_2, pi^{l_2} = e_{M_2} is the R-double piece (alpha = 2).
"""
from itertools import product

# BDI coord indexing at n = 5
BDI_COORDS = ["M2", "M3", "M4", "B1", "T1", "B2", "T2", "B3", "T3", "B4", "T4", "S"]
NB = len(BDI_COORDS)
IDX = {c: i for i, c in enumerate(BDI_COORDS)}

def vec(**kw):
    v = [0] * NB
    for k, n in kw.items():
        v[IDX[k]] = n
    return tuple(v)

def add(*vs):
    if not vs: return tuple([0] * NB)
    return tuple(sum(x) for x in zip(*vs))

def scale(c, v):
    return tuple(c * x for x in v)

def P(a, v):
    return 2 * sum(v[IDX[f"B{b}"]] - v[IDX[f"T{b}"]] for b in range(1, a + 1))

def is_BDI(v):
    if any(x < 0 for x in v): return False
    for a in range(1, 5):
        if v[IDX[f"T{a}"]] > v[IDX[f"B{a}"]]: return False
        if P(a, v) < 0: return False
    for a in range(2, 5):
        if v[IDX[f"M{a}"]] > min(P(a-1, v), P(a, v)): return False
    if v[IDX["S"]] > P(4, v): return False
    return True

def make_piece(p1v, p2v, p3v, p4v, p5v, l1v, l2v, l3v, l4v, l5v, s1v, s2v, s3v, s4v, s5v):
    return {"p1": p1v, "p2": p2v, "p3": p3v, "p4": p4v, "p5": p5v,
            "l1": l1v, "l2": l2v, "l3": l3v, "l4": l4v, "l5": l5v,
            "s1": s1v, "s2": s2v, "s3": s3v, "s4": s4v, "s5": s5v}

def check_F(piece):
    for j in range(1, 6):
        if not is_BDI(piece[f"p{j}"]): return False
    for j in range(2, 6):
        if not is_BDI(add(piece[f"p{j-1}"], piece[f"l{j}"])): return False
        if not is_BDI(add(piece[f"p{j-1}"], piece[f"s{j}"])): return False
    if not is_BDI(piece["l1"]): return False
    if not is_BDI(piece["s1"]): return False
    return True

def gen_set(piece):
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

# === Standard cover pieces ===

base_piece = make_piece(
    p1v=vec(B1=1), p2v=vec(B2=1), p3v=vec(B3=1), p4v=vec(B4=1), p5v=vec(),
    l1v=vec(B1=1), l2v=vec(M2=1), l3v=vec(M3=1), l4v=vec(M4=1), l5v=vec(S=1),
    s1v=vec(B1=1, T1=1), s2v=vec(B2=1, T2=1), s3v=vec(B3=1, T3=1), s4v=vec(B4=1, T4=1), s5v=vec(),
)

# R-double family
def rdouble(alpha):
    return make_piece(
        p1v=vec(B1=1, S=alpha), p2v=vec(B2=1), p3v=vec(B3=1), p4v=vec(B4=1), p5v=vec(B2=1, T2=1),
        l1v=vec(B1=1, T1=1), l2v=vec(M2=1), l3v=vec(M3=1), l4v=vec(M4=1), l5v=vec(S=1),
        s1v=vec(B1=2, T1=1, S=2), s2v=vec(B2=1, T2=1), s3v=vec(B3=1, T3=1),
        s4v=vec(B4=1, T4=1, S=2), s5v=vec(),
    )

# Lemma B family: pi^{p_5} multiplicity
def lemmaB(k):
    return make_piece(
        p1v=vec(B1=1), p2v=vec(B2=1), p3v=vec(B3=1), p4v=vec(B4=1),
        p5v=scale(k, vec(B4=1, T4=1)),
        l1v=vec(B1=1), l2v=vec(M2=1), l3v=vec(M3=1), l4v=vec(M4=1), l5v=vec(S=1),
        s1v=vec(B1=1, T1=1), s2v=vec(B2=1, T2=1), s3v=vec(B3=1, T3=1), s4v=vec(B4=1, T4=1), s5v=vec(),
    )

# Lemma C family: pi^{l_1} multiplicity
def lemmaC(k):
    return make_piece(
        p1v=vec(B1=1), p2v=vec(B2=1), p3v=vec(B3=1), p4v=vec(B4=1), p5v=vec(),
        l1v=vec(B1=k), l2v=vec(M2=1), l3v=vec(M3=1), l4v=vec(M4=1), l5v=vec(S=1),
        s1v=vec(B1=1, T1=1), s2v=vec(B2=1, T2=1), s3v=vec(B3=1, T3=1), s4v=vec(B4=1, T4=1), s5v=vec(),
    )

# Divert variant pieces of base — base with one column changed to divert.
divert_variants = []
for c in ["l3", "l4", "s2", "s3", "s4"]:
    p = dict(base_piece)
    p[c] = vec(S=1)
    divert_variants.append(p)

# Cover includes: base, R-double 0/1/2, Lemma B 0/1/2, Lemma C 0/1/2, divert variants
cover_pieces = [base_piece]
for a in range(3):
    cover_pieces.append(rdouble(a))
for k in range(3):
    cover_pieces.append(lemmaB(k))
for k in range(3):
    cover_pieces.append(lemmaC(k))
cover_pieces.extend(divert_variants)

# Sanity: all feasible?
for i, p in enumerate(cover_pieces):
    if not check_F(p):
        print(f"WARNING: cover piece {i} not feasible")

# Collect all generators
cover_gens = set()
for p in cover_pieces:
    cover_gens.update(gen_set(p))

print(f"Reference cover: {len(cover_pieces)} pieces, {len(cover_gens)} distinct generators")

# === Enumerate feasible pieces with pi^{p_1}=b_2, pi^{l_2}=eM_2 ===

p1_b2 = vec(B1=1, S=2)
p2 = vec(B2=1)
p3 = vec(B3=1)
p4 = vec(B4=1)
l2 = vec(M2=1)
l5 = vec(S=1)

p5_cands = [vec(), vec(B4=1, T4=1), scale(2, vec(B4=1, T4=1)), vec(B2=1, T2=1), vec(B3=1, T3=1), vec(S=1)]
l1_cands = [vec(), vec(B1=1), vec(B1=2), vec(B1=1, T1=1)]
l3_cands = [vec(M3=1), vec(S=1)]
l4_cands = [vec(M4=1), vec(S=1)]
s1_cands = [vec(B1=1, T1=1), vec(B1=2, T1=1, S=2), vec(B1=1, S=1)]
s2_cands = [vec(B2=1, T2=1), vec(S=1)]
s3_cands = [vec(B3=1, T3=1), vec(S=1)]
s4_cands = [vec(B4=1, T4=1), vec(B4=1, T4=1, S=2), vec(S=1)]
s5_cands = [vec(), vec(B4=1), vec(S=1)]

# Filter s1_cands by BDI feasibility
s1_cands = [v for v in s1_cands if is_BDI(v)]

# Enumerate feasible pieces
feasible_pieces = []
for p5v in p5_cands:
    for l1v in l1_cands:
        for l3v in l3_cands:
            for l4v in l4_cands:
                for s1v in s1_cands:
                    for s2v in s2_cands:
                        for s3v in s3_cands:
                            for s4v in s4_cands:
                                for s5v in s5_cands:
                                    piece = make_piece(
                                        p1v=p1_b2, p2v=p2, p3v=p3, p4v=p4, p5v=p5v,
                                        l1v=l1v, l2v=l2, l3v=l3v, l4v=l4v, l5v=l5,
                                        s1v=s1v, s2v=s2v, s3v=s3v, s4v=s4v, s5v=s5v,
                                    )
                                    if check_F(piece):
                                        feasible_pieces.append(piece)

print(f"\nFeasible pieces with pi^p1=b2, pi^l2=eM2: {len(feasible_pieces)}")

# === Image semigroup membership ===

def semigroup_membership(point, generators, max_coef=3):
    N = len(generators)
    gens_tuple = tuple(generators)
    cache = {}
    def rec(i, remaining):
        if remaining == tuple([0]*NB):
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

# For each feasible piece, identify which generators are NEW (not in cover_gens semigroup).
print("\nChecking image-containment against the reference cover...")
contained_pieces = []
not_contained = []
ref_gens_list = sorted(cover_gens)
for i, piece in enumerate(feasible_pieces):
    all_in = True
    new_gens = []
    for g in gen_set(piece):
        if not semigroup_membership(g, ref_gens_list, max_coef=4):
            all_in = False
            new_gens.append(g)
    if all_in:
        contained_pieces.append(piece)
    else:
        not_contained.append((piece, new_gens))
    if (i+1) % 500 == 0:
        print(f"  Processed {i+1}/{len(feasible_pieces)}")

print(f"\nResults:")
print(f"  Pieces image-contained in reference cover: {len(contained_pieces)}")
print(f"  Pieces with at least one new generator: {len(not_contained)}")

# Among the contained pieces, is R-double-α=2 present?
def is_rdouble2(piece):
    return piece == rdouble(2)
rd2_in_contained = any(is_rdouble2(p) for p in contained_pieces)
print(f"  R-double-α=2 in contained pieces: {rd2_in_contained}")

# Identify the unique "R-double-equivalent" pieces.
# A piece is R-double-equivalent if its image semigroup CONTAINS R-double's image semigroup.
rd2_gens = list(set(gen_set(rdouble(2))))

print(f"\nChecking which contained pieces contribute ALL R-double-α=2 generators...")
rd_equivalents = []
for piece in contained_pieces:
    piece_gens = list(set(gen_set(piece)))
    contains_rd = all(semigroup_membership(g, piece_gens, max_coef=4) for g in rd2_gens)
    if contains_rd:
        rd_equivalents.append(piece)

print(f"  Pieces that image-CONTAIN R-double-α=2's image: {len(rd_equivalents)}")
for p in rd_equivalents[:10]:
    print()
    for c in ["p5", "l1", "l3", "l4", "s1", "s2", "s3", "s4", "s5"]:
        if p[c] != vec():
            print(f"    pi^{c} = {dict((k,vv) for k,vv in zip(BDI_COORDS, p[c]) if vv)}")
