#!/usr/bin/env python3
"""
Day-74 CODE: finite check of Conjecture 6.2 at n = 5.

Enumerate all BDI-feasible pieces pi at n=5 with:
  pi^{p_1} = b_2 = e_{B_1} + 2 e_S
  pi^{l_2} = e_{M_2}

We restrict each column to candidates from the Day-70 §6 RIGID/BINARY classes,
PLUS extended candidates for the AXIS columns p_5, l_1, s_1 (and for s_4, which
the R-double piece "engines" via 2 e_S).
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

# Forced columns from Day-70 §6 + D-pi at n=5.
p1 = vec(B1=1, S=2)        # b_2 (given)
p2 = vec(B2=1)             # RIGID by D-pi
p3 = vec(B3=1)             # RIGID by D-pi
p4 = vec(B4=1)             # RIGID by §6.4
l2 = vec(M2=1)             # given
l5 = vec(S=1)              # RIGID by §6.1

# Candidate values for the BINARY / AXIS columns.
# Restrict each BINARY column to its TWO image-classes (canonical, divert).
# For AXIS columns, allow {0, canonical, 2×canonical} (Lemma B / Lemma C / R-double).
# For s_1, s_4: R-double has engine. Allow both base and R-double engines.

p5_cands = [
    vec(),                              # base / Lemma B k=0
    vec(B4=1, T4=1),                    # Lemma B k=1
    scale(2, vec(B4=1, T4=1)),          # Lemma B k=2
    vec(B2=1, T2=1),                    # R-double pi^{p_5}
    vec(B3=1, T3=1),                    # other possibility?
    vec(S=1),                           # p_5 -> S divert
]
l1_cands = [
    vec(),                              # Lemma C k=0
    vec(B1=1),                          # Lemma C k=1 / base
    vec(B1=2),                          # Lemma C k=2
    vec(B1=1, T1=1),                    # R-double pi^{l_1}
]
l3_cands = [
    vec(M3=1),                          # canonical
    vec(S=1),                           # divert
]
l4_cands = [
    vec(M4=1),                          # canonical
    vec(S=1),                           # divert
]
s1_cands = [
    vec(B1=1, T1=1),                    # base canonical balanced
    vec(B1=2, T1=1, S=2),               # R-double engine
    vec(B1=1, S=1),                     # weird variant (B-T = 0, S = 1, not BDI alone since S > P_1=0 unless...)
]
# Filter s1: must be in BDI
s1_cands = [v for v in s1_cands if is_BDI(v)]

s2_cands = [
    vec(B2=1, T2=1),                    # canonical balanced
    vec(S=1),                           # divert
]
s3_cands = [
    vec(B3=1, T3=1),                    # canonical balanced
    vec(S=1),                           # divert
]
s4_cands = [
    vec(B4=1, T4=1),                    # canonical balanced
    vec(B4=1, T4=1, S=2),               # R-double engine
    vec(S=1),                           # divert
]
s5_cands = [
    vec(),                              # RIGID 0 (base)
    vec(B4=1),                          # alternative?
    vec(S=1),                           # divert?
]
# Filter by basic BDI feasibility of the column itself for j=1 cases
# (Note: for j >= 2 columns of l, s, the column itself need NOT be in BDI;
# only the sum with the preceding p column needs to be in BDI.)

# F-constraints filter.
def check_F(piece):
    """Return True iff F1-F4 hold."""
    # F1: pi^{p_j} in BDI for j=1..5
    for j in range(1, 6):
        if not is_BDI(piece[f"p{j}"]): return False
    # F2: pi^{p_{j-1}} + pi^{l_j} in BDI for j=2..5
    for j in range(2, 6):
        if not is_BDI(add(piece[f"p{j-1}"], piece[f"l{j}"])): return False
    # F3: pi^{p_{j-1}} + pi^{s_j} in BDI for j=2..5
    for j in range(2, 6):
        if not is_BDI(add(piece[f"p{j-1}"], piece[f"s{j}"])): return False
    # F4: pi^{l_1}, pi^{s_1} in BDI
    if not is_BDI(piece["l1"]): return False
    if not is_BDI(piece["s1"]): return False
    return True

def make_piece(p1v, p2v, p3v, p4v, p5v, l1v, l2v, l3v, l4v, l5v, s1v, s2v, s3v, s4v, s5v):
    return {"p1": p1v, "p2": p2v, "p3": p3v, "p4": p4v, "p5": p5v,
            "l1": l1v, "l2": l2v, "l3": l3v, "l4": l4v, "l5": l5v,
            "s1": s1v, "s2": s2v, "s3": s3v, "s4": s4v, "s5": s5v}

print("Candidate counts (restricted to Day-70 §6 classes):")
for name, cands in [("p_5", p5_cands), ("l_1", l1_cands),
                     ("l_3", l3_cands), ("l_4", l4_cands),
                     ("s_1", s1_cands), ("s_2", s2_cands), ("s_3", s3_cands),
                     ("s_4", s4_cands), ("s_5", s5_cands)]:
    print(f"  {name}: {len(cands)}")

total = (len(p5_cands) * len(l1_cands) * len(l3_cands) * len(l4_cands) *
         len(s1_cands) * len(s2_cands) * len(s3_cands) * len(s4_cands) * len(s5_cands))
print(f"\nTotal enumeration size: {total}")

# Enumerate
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
                                        p1v=p1, p2v=p2, p3v=p3, p4v=p4, p5v=p5v,
                                        l1v=l1v, l2v=l2, l3v=l3v, l4v=l4v, l5v=l5,
                                        s1v=s1v, s2v=s2v, s3v=s3v, s4v=s4v, s5v=s5v,
                                    )
                                    if check_F(piece):
                                        feasible_pieces.append(piece)

print(f"\nFeasible pieces with pi^p1=b2, pi^l2=e_M2: {len(feasible_pieces)}")

# Identify F-forced columns: which columns have the SAME value across all feasible pieces?
print("\nF-forced columns (same value across all feasible pieces):")
all_cols = ["p5", "l1", "l3", "l4", "s1", "s2", "s3", "s4", "s5"]
for c in all_cols:
    vals = set(p[c] for p in feasible_pieces)
    if len(vals) == 1:
        v = list(vals)[0]
        print(f"  pi^{c} = {dict((k,vv) for k,vv in zip(BDI_COORDS, v) if vv)} (FORCED)")
    else:
        print(f"  pi^{c}: {len(vals)} distinct values across feasible pieces")
        for v in sorted(vals):
            print(f"    {dict((k,vv) for k,vv in zip(BDI_COORDS, v) if vv)}")

# === Image-redundancy analysis ===
# For each feasible piece, compute its image generators (the 15 ray-images).
# Then check which pieces are image-contained in the union { Im(base), Im(R-double-alpha-2 canonical) }.

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

base_piece = make_piece(
    p1v=vec(B1=1), p2v=vec(B2=1), p3v=vec(B3=1), p4v=vec(B4=1), p5v=vec(),
    l1v=vec(B1=1), l2v=vec(M2=1), l3v=vec(M3=1), l4v=vec(M4=1), l5v=vec(S=1),
    s1v=vec(B1=1, T1=1), s2v=vec(B2=1, T2=1), s3v=vec(B3=1, T3=1), s4v=vec(B4=1, T4=1), s5v=vec(),
)
rdouble_alpha = lambda a: make_piece(
    p1v=vec(B1=1, S=a), p2v=vec(B2=1), p3v=vec(B3=1), p4v=vec(B4=1), p5v=vec(B2=1, T2=1),
    l1v=vec(B1=1, T1=1), l2v=vec(M2=1), l3v=vec(M3=1), l4v=vec(M4=1), l5v=vec(S=1),
    s1v=vec(B1=2, T1=1, S=2), s2v=vec(B2=1, T2=1), s3v=vec(B3=1, T3=1),
    s4v=vec(B4=1, T4=1, S=2), s5v=vec(),
)

assert check_F(base_piece), "base not feasible"
for a in range(3):
    assert check_F(rdouble_alpha(a)), f"R-double alpha={a} not feasible"

print("\n[Image-semigroup membership]")

def semigroup_membership(point, generators, max_coef=3):
    """Return True iff `point` is a non-negative integer combination of generators.
    Bounded search: each coefficient <= max_coef. Sufficient for small targets."""
    N = len(generators)
    def rec(i, remaining):
        if remaining == tuple([0]*NB):
            return True
        if i == N:
            return False
        # Bound coef by max in any component of remaining / corresponding generator.
        g = generators[i]
        # max possible coef without overshooting any component
        max_c = max_coef
        for k in range(NB):
            if g[k] > 0:
                max_c = min(max_c, remaining[k] // g[k])
            elif g[k] < 0:
                pass  # shouldn't happen with non-neg generators
        for c in range(max_c + 1):
            new_rem = tuple(remaining[k] - c * g[k] for k in range(NB))
            if any(x < 0 for x in new_rem):
                continue
            if rec(i + 1, new_rem):
                return True
        return False
    return rec(0, point)

def is_image_contained(piece, ref_gens, max_coef=3):
    """Check if all of piece's generators lie in the semigroup generated by ref_gens."""
    for g in gen_set(piece):
        if not semigroup_membership(g, ref_gens, max_coef):
            return False
    return True

# Image of {base, R-double alpha=0,1,2}: union of generators.
ref_pieces = [base_piece, rdouble_alpha(0), rdouble_alpha(1), rdouble_alpha(2)]
ref_gens = []
for p in ref_pieces:
    ref_gens.extend(gen_set(p))
# Dedupe
ref_gens = list(set(ref_gens))
print(f"  Reference {len(ref_pieces)} pieces, {len(ref_gens)} distinct generators")

# Check how many feasible pieces are image-contained in this reference set.
print("\nChecking image-containment of feasible pieces in {base, R-double_alpha=0,1,2}:")
contained_count = 0
not_contained = []
for i, piece in enumerate(feasible_pieces):
    if is_image_contained(piece, ref_gens, max_coef=4):
        contained_count += 1
    else:
        not_contained.append(piece)
    if (i+1) % 50 == 0:
        print(f"  Processed {i+1}/{len(feasible_pieces)}")
print(f"\n  Contained: {contained_count}/{len(feasible_pieces)}")
print(f"  NOT contained: {len(not_contained)}")

if not_contained:
    print("\nNot-contained pieces (potential cover-distinct rests):")
    for piece in not_contained[:5]:
        print()
        for c in ["p5", "l1", "s1", "s2", "s3", "s4", "s5", "l3", "l4"]:
            print(f"    pi^{c} = {dict((k,vv) for k,vv in zip(BDI_COORDS, piece[c]) if vv)}")
        # Identify which generator(s) are NOT in ref.
        for g in gen_set(piece):
            if not semigroup_membership(g, ref_gens, max_coef=4):
                print(f"    NEW gen: {dict((k,vv) for k,vv in zip(BDI_COORDS, g) if vv)}")
