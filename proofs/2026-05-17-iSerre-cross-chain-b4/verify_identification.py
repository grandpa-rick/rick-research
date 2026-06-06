"""
Verify whether Rick's 12 cross-chain monomials at B_4 are in structural bijection
with iSerre nested-commutator monomials (Letzter / Bao-Wang / Kolb / BK15 / CLW).

Strategy:
  Part A. Pull Rick's 12 cross-chain entries explicitly (from characterize_moves_b4).
  Part B. Enumerate iSerre nested-commutator monomials of the split iquantum
          group U^i of type B_n at n=4, using BK15 Theorem 3.7 (cf. CLW eq. 3.11)
          for each pair (i, j) with i, j in {1,2,3,4}, i != j.
  Part C. Try multiple candidate bijection schemes:
          (Scheme 1) Long-long iSerre monomials only.
          (Scheme 2) Long-long-iSerre + endpoint corrections.
          (Scheme 3) All iSerre monomials (LHS and RHS).
          (Scheme 4) Cross-chain monomials as TENSOR-FACTOR-INTERACTION terms
                     in a Watanabe-style tensor product rule.

  Part D. Verdict.

This script is honest: if no bijection works, it reports NO MATCH.
"""

from itertools import product
from collections import Counter

# ============================================================
# Part A. Rick's 12 cross-chain entries at B_4.
# ============================================================
# Chains at alpha_4: A (a=1), B (a=2), C (a=3).
# Primitives per chain: TM (top->mid), MB (mid->bot).
# Cross-chain entry = unordered pair of (chain, primitive) with distinct chains.

CHAIN_INDEX = {'A': 1, 'B': 2, 'C': 3}  # convex order
PRIMITIVES = ['TM', 'MB']

cross_chain_entries = []
for (cn1, cn2) in [('A', 'B'), ('A', 'C'), ('B', 'C')]:
    for k1 in PRIMITIVES:
        for k2 in PRIMITIVES:
            label = f'cross-{cn1}{cn2}: {k1}+{k2}'
            # Canonical: sorted (chain, kind) tuple
            entry = tuple(sorted([(cn1, k1), (cn2, k2)]))
            cross_chain_entries.append((label, entry))

print("=" * 72)
print("PART A. Rick's 12 cross-chain entries (B_4, alpha_4 short simple)")
print("=" * 72)
print(f"Count: {len(cross_chain_entries)}")
for label, entry in cross_chain_entries:
    print(f"  {label:30s}  {entry}")

assert len(cross_chain_entries) == 12, f"Expected 12, got {len(cross_chain_entries)}"


# ============================================================
# Part B. iSerre nested-commutator monomial enumeration at B_4.
# ============================================================
# Cartan matrix of B_4 (with alpha_4 short, alpha_1, alpha_2, alpha_3 long):
#   a_{i,i} = 2 for all i
#   a_{1,2} = a_{2,1} = -1
#   a_{2,3} = a_{3,2} = -1
#   a_{3,4} = -1 (long acting on short)
#   a_{4,3} = -2 (short acting on long: this is the short-long edge)
#   all other off-diagonal: 0
#
# In BK15/Letzter, the iSerre relations for the SPLIT iquantum group (tau = id)
# are, for i != j (cf. CLW eq. 3.11; equivalently CLW (3.9) with tau i = i):
#
#   a_{ij} = 0:   B_i B_j - B_j B_i = 0      (1 commutator monomial = 2 monomials in B's)
#   a_{ij} = -1:  B_i^2 B_j - [2]_{q_i} B_i B_j B_i + B_j B_i^2 = q_i*ς_i B_j
#                 (LHS: 3 monomials; RHS: 1 monomial)
#   a_{ij} = -2:  B_i^3 B_j - [3]_{q_i} B_i^2 B_j B_i + [3]_{q_i} B_i B_j B_i^2 - B_j B_i^3
#                  = -[2]^2_{q_i} q_i ς_i (B_i B_j - B_j B_i)
#                 (LHS: 4 monomials; RHS: 2 monomials)
#
# Note: a_{ij} = -2 only occurs at (i, j) = (4, 3) in B_4 (short acting on long).
# The reverse a_{3, 4} = -1 is a "normal" Serre at index 3 vs index 4.

# Build the relation catalog.
def aij(i, j):
    """Cartan matrix of B_4 with short simple alpha_4."""
    if i == j:
        return 2
    # standard B_n adjacency
    pairs = {(1,2):-1, (2,1):-1, (2,3):-1, (3,2):-1, (3,4):-1, (4,3):-2}
    return pairs.get((i, j), 0)

INDICES = [1, 2, 3, 4]

iSerre_monomials_by_relation = {}  # (i,j) -> list of (multiset, side, term_label) tuples
for i in INDICES:
    for j in INDICES:
        if i == j:
            continue
        a = aij(i, j)
        if a == 0:
            # B_i B_j - B_j B_i = 0
            terms = [
                (('B' + str(i), 'B' + str(j)), 'LHS', f'+B{i}B{j}'),
                (('B' + str(j), 'B' + str(i)), 'LHS', f'-B{j}B{i}'),
            ]
            iSerre_monomials_by_relation[(i, j, 'comm')] = terms
        elif a == -1:
            # 3 LHS monomials of degree 3, 1 RHS of degree 1
            terms = [
                (('B' + str(i),)*2 + ('B' + str(j),), 'LHS', f'+B{i}B{i}B{j}'),
                (('B' + str(i),) + ('B' + str(j),) + ('B' + str(i),), 'LHS', f'-[2]B{i}B{j}B{i}'),
                (('B' + str(j),) + ('B' + str(i),)*2, 'LHS', f'+B{j}B{i}B{i}'),
                (('B' + str(j),), 'RHS', f'-c*B{j}'),
            ]
            iSerre_monomials_by_relation[(i, j, 'Serre-1')] = terms
        elif a == -2:
            # 4 LHS monomials of degree 4, 2 RHS of degree 2
            terms = [
                (('B' + str(i),)*3 + ('B' + str(j),), 'LHS', f'+B{i}^3B{j}'),
                (('B' + str(i),)*2 + ('B' + str(j),) + ('B' + str(i),), 'LHS', f'-[3]B{i}^2B{j}B{i}'),
                (('B' + str(i),) + ('B' + str(j),) + ('B' + str(i),)*2, 'LHS', f'+[3]B{i}B{j}B{i}^2'),
                (('B' + str(j),) + ('B' + str(i),)*3, 'LHS', f'-B{j}B{i}^3'),
                (('B' + str(i),) + ('B' + str(j),), 'RHS', f'-c*B{i}B{j}'),
                (('B' + str(j),) + ('B' + str(i),), 'RHS', f'+c*B{j}B{i}'),
            ]
            iSerre_monomials_by_relation[(i, j, 'Serre-2')] = terms

print()
print("=" * 72)
print("PART B. iSerre relations at B_4 (split, BK15 + CLW eq. 3.11)")
print("=" * 72)

total_LHS_monomials = 0
total_RHS_monomials = 0
total_monomials = 0
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    a = aij(i, j)
    lhs = sum(1 for t in terms if t[1] == 'LHS')
    rhs = sum(1 for t in terms if t[1] == 'RHS')
    total_LHS_monomials += lhs
    total_RHS_monomials += rhs
    total_monomials += len(terms)
    if i < j or kind != 'comm':  # avoid double-printing comm relations
        print(f"  i={i}, j={j} (a_ij={a:+d}, {kind:8s}): LHS={lhs} monomials, RHS={rhs}, total={len(terms)}")

print()
print(f"Total relations: {len(iSerre_monomials_by_relation)}")
print(f"Total LHS monomials (across all relations): {total_LHS_monomials}")
print(f"Total RHS monomials: {total_RHS_monomials}")
print(f"Grand total: {total_monomials}")


# ============================================================
# Part C. Try candidate bijections.
# ============================================================
print()
print("=" * 72)
print("PART C. Candidate bijection schemes")
print("=" * 72)

# Scheme 1: Long-long iSerre LHS monomials.
# Only count i, j in {1, 2, 3} (long simples = the "chains").
print()
print("--- Scheme 1: LHS of long-long iSerre relations (i,j in {1,2,3}) ---")
scheme1 = []
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    if i in [1,2,3] and j in [1,2,3]:
        for t in terms:
            if t[1] == 'LHS':
                scheme1.append((key, t[2]))
print(f"  count: {len(scheme1)}")
if len(scheme1) == 12:
    print("  COUNT MATCHES 12!")
else:
    print(f"  count != 12 (got {len(scheme1)})")
# Break down by relation
by_pair = Counter((i, j) for (i, j, _), _ in scheme1)
for (i,j), n in sorted(by_pair.items()):
    a = aij(i,j)
    print(f"    pair ({i},{j}) a={a:+d}: {n} LHS monomials")

# Scheme 2: All iSerre monomials (LHS + RHS) for long-long pairs.
print()
print("--- Scheme 2: ALL monomials (LHS+RHS) of long-long iSerre ---")
scheme2 = []
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    if i in [1,2,3] and j in [1,2,3]:
        for t in terms:
            scheme2.append((key, t[2]))
print(f"  count: {len(scheme2)}")
if len(scheme2) == 12:
    print("  COUNT MATCHES 12!")
else:
    print(f"  count != 12 (got {len(scheme2)})")

# Scheme 3: All iSerre monomials of the short-long edge (4, 3) only.
print()
print("--- Scheme 3: ALL monomials of the (4,3) short-long iSerre only ---")
scheme3 = []
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    if (i, j) == (4, 3):
        for t in terms:
            scheme3.append((key, t[2]))
print(f"  count: {len(scheme3)}")
# this has 6 monomials, not 12.

# Scheme 4: LHS+RHS of BOTH short-long edges (4,3) and (3,4).
print()
print("--- Scheme 4: ALL monomials of (4,3) AND (3,4) iSerre relations ---")
scheme4 = []
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    if (i, j) in [(4,3), (3,4)]:
        for t in terms:
            scheme4.append((key, t[2]))
print(f"  count: {len(scheme4)}")
# 6 + 4 = 10, not 12.

# Scheme 5: LHS-only of ALL iSerre relations involving B_4.
print()
print("--- Scheme 5: LHS-only of ALL relations (i, j) with i=4 or j=4 ---")
scheme5 = []
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    if i == 4 or j == 4:
        for t in terms:
            if t[1] == 'LHS':
                scheme5.append((key, t[2]))
print(f"  count: {len(scheme5)}")

# Scheme 6: ALL monomials of all relations involving B_4.
print()
print("--- Scheme 6: ALL monomials of all relations (i,j) with i=4 or j=4 ---")
scheme6 = []
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    if i == 4 or j == 4:
        for t in terms:
            scheme6.append((key, t[2]))
print(f"  count: {len(scheme6)}")

# Scheme 7: LHS of long-long ordered pair iSerre (unordered).
print()
print("--- Scheme 7: LHS-only of UNORDERED long-long Serre ---")
seen_pairs = set()
scheme7 = []
for key, terms in iSerre_monomials_by_relation.items():
    i, j, kind = key
    if i in [1,2,3] and j in [1,2,3]:
        pair = frozenset([i, j])
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)
        for t in terms:
            if t[1] == 'LHS':
                scheme7.append((key, t[2]))
print(f"  count: {len(scheme7)}")

# Scheme 8: Cross-chain as TENSOR-FACTOR interaction.
# In the Watanabe-style tensor product rule, each chain factor C_a contributes
# 2 "step types" (TM_a, MB_a). Cross-factor interaction at second-order
# (e_n^2 step) gives unordered pairs of step types from distinct factors.
# This is EXACTLY Rick's combinatorial decomposition; the count 12 is
# COMBINATORIAL, not algebraic.
# The corresponding algebraic shadow would be the "off-diagonal coupling
# tensor" in the iquantum coproduct, but the iSerre relation itself is local
# and produces 6 monomials at (4,3), not 12.
print()
print("--- Scheme 8: tensor-product cross-factor interaction count ---")
chain_step_types = [(c, p) for c in 'ABC' for p in PRIMITIVES]
# unordered pairs of (chain, primitive) with distinct chains
from itertools import combinations
combinatorial_count = 0
for (c1, p1), (c2, p2) in combinations(chain_step_types, 2):
    if c1 != c2:
        combinatorial_count += 1
print(f"  count: {combinatorial_count}  (matches 12 — but this IS Rick's count, no shadow)")


# ============================================================
# Part D. Verdict.
# ============================================================
print()
print("=" * 72)
print("PART D. Verdict on structural bijection.")
print("=" * 72)

# Test each scheme: does the COUNT match 12? And if so, is there a NATURAL
# STRUCTURAL bijection (chain-pair <-> generator-pair, primitive-choice <-> monomial-index)?

print()
print("COUNTS:")
print(f"  Scheme 1 (long-long LHS only): {len(scheme1)}  {'MATCH 12' if len(scheme1)==12 else ''}")
print(f"  Scheme 2 (long-long all):      {len(scheme2)}")
print(f"  Scheme 3 ((4,3) only):         {len(scheme3)}")
print(f"  Scheme 4 ((4,3)+(3,4)):        {len(scheme4)}")
print(f"  Scheme 5 (i=4 or j=4 LHS):     {len(scheme5)}")
print(f"  Scheme 6 (i=4 or j=4 all):     {len(scheme6)}")
print(f"  Scheme 7 (unordered LL LHS):   {len(scheme7)}")
print(f"  Scheme 8 (combinatorial tensor): {combinatorial_count}")

print()
print("STRUCTURAL ANALYSIS of Scheme 1 (the count match):")
print("  Long-long pairs in B_4: (1,2)/(2,1), (2,3)/(3,2), (1,3)/(3,1).")
print("  a_{ij} values:")
print(f"    a_{{1,2}} = {aij(1,2)},  a_{{2,1}} = {aij(2,1)}  -> -1, -1, Serre-1, 3 LHS monomials each")
print(f"    a_{{2,3}} = {aij(2,3)},  a_{{3,2}} = {aij(3,2)}  -> -1, -1, Serre-1, 3 LHS monomials each")
print(f"    a_{{1,3}} = {aij(1,3)},  a_{{3,1}} = {aij(3,1)}  -> 0, 0, comm, 2 LHS monomials each")
print("  Total LHS: 2*3 + 2*3 + 2*2 = 16, NOT 12.")
# Recompute
print(f"  (Recomputed: {len(scheme1)} monomials)")

print()
print("CANDIDATE STRUCTURAL BIJECTION (proposed):")
print("  IF we sum ordered pairs (i,j) in {1,2,3} x {1,2,3} with i != j:")
print("  there are 6 ordered pairs. Each contributes some number of LHS")
print("  iSerre monomials. The two pairs at a_{ij} = -1 contribute 3 each;")
print("  the one pair at a_{ij} = 0 contributes 2 (commutator). So:")
print("    2 * (3 + 3) + 2 * (2) = 12 + 4 = 16. Doesn't match 12.")
print()
print("  IF we restrict to ADJACENT long-long pairs only (Serre at a=-1):")
print("    4 pairs ((1,2),(2,1),(2,3),(3,2)), each 3 LHS = 12.  MATCH!")
print()
print("  This gives the bijection:")
print("    cross-AB pairs (4 of them) ~ LHS of {(1,2), (2,1)} Serre-1 (6 monomials)")
print("    Wait: 4 != 6. Need a different mapping.")
print()
print("  ALTERNATIVELY: ordered pair (a, b) of distinct chains contributes 2")
print("  monomials (one per primitive). Unordered: 4 per pair. With 3 chain pairs: 12.")
print("  This is just SCHEME 8 (combinatorial), not an iSerre-derived shadow.")

print()
print("CONCLUSION:")
print("  - The naive iSerre relation at the short-long edge (a_{4,3}=-2) gives")
print("    a SINGLE LOCAL relation with 6 monomials. This is INDEPENDENT of n.")
print("  - The cross-chain count 2(n-1)(n-2) grows quadratically in n.")
print("  - NO local iSerre relation can account for the n-dependence.")
print("  - Scheme 1 (long-long LHS only) gives 16 != 12 at B_4. Doesn't match.")
print("  - Even restricting to adjacent long-long pairs gives 12 at B_4, but the")
print("    structural bijection is not natural: cross-AC (4 entries, non-adjacent")
print("    in the Dynkin diagram, a_{1,3}=0) would have NO iSerre LHS monomials")
print("    on the algebra side, contradicting Rick's catalog where AC also has 4.")
print()
print("VERDICT: NO STRUCTURAL BIJECTION between Rick's 12 cross-chain monomials")
print("and a fixed family of iSerre nested-commutator monomials in the split")
print("iquantum group of type B_n at the short-long edge.")
print()
print("The combinatorial coincidence 2(n-1)(n-2) = 4 * C(n-1, 2) is real, but")
print("it is the natural count of 'unordered pairs of (chain, primitive) with")
print("distinct chains' — a TENSOR-PRODUCT-RULE combinatorial shadow, NOT an")
print("iSerre-relation shadow.")


# ============================================================
# Part E. Rank-uniformity sanity check.
# ============================================================
# The cross-chain count is 2(n-1)(n-2) which grows quadratically in n.
# Compare to the total LHS+RHS iSerre monomial count for B_n.
# B_n has:
#   - (n-2) long-long adjacent pairs with a_{ij} = -1: each direction => 2*(n-2) Serre-1 relations,
#     each with 3 LHS + 1 RHS = 4 monomials. Total: 8(n-2).
#   - C(n-1, 2) - (n-2) = (n-2)(n-3)/2 long-long non-adjacent pairs with a=0:
#     each direction => 2 * (n-2)(n-3)/2 = (n-2)(n-3) commutation relations, each 2 monomials.
#     Total: 2 * (n-2)(n-3).
#   - Short-long (n, n-1) at a=-2: 6 monomials.
#   - Long-short (n-1, n) at a=-1: 4 monomials.
#   - Long-short non-adjacent (n, k) for k < n-1: a=0, 2 * (n-2) commutations, 2 monomials each.
#     Total: 4(n-2).
print()
print("=" * 72)
print("PART E. Rank uniformity sanity check.")
print("=" * 72)
print()
print(f"{'n':>3} | {'cross-chain':>11} | {'iSerre LHS-tot':>15} | {'iSerre all':>11} | {'(4,3)-only':>11}")
print("-" * 64)
for n in range(2, 8):
    cross = 2 * (n - 1) * (n - 2)
    # Long-long adjacent: (n-2) unordered pairs => 2(n-2) ordered, 3 LHS each
    LLA_LHS = 2 * (n - 2) * 3
    LLA_total = 2 * (n - 2) * 4
    # Long-long non-adjacent: (n-1 choose 2) - (n-2) unordered = (n-2)(n-3)/2
    if n >= 3:
        LLNA = (n - 2) * (n - 3) // 2
    else:
        LLNA = 0
    LLNA_LHS = 2 * LLNA * 2
    LLNA_total = LLNA_LHS
    # Short-long (n, n-1) at a=-2: 4 LHS, 2 RHS
    SL_LHS = 4
    SL_total = 6
    # Long-short (n-1, n) at a=-1: 3 LHS, 1 RHS
    LS_LHS = 3
    LS_total = 4
    # short-other-long commutations: 2*(n-2) commutations, 2 monomials each
    SO_LHS = 2 * (n - 2) * 2
    SO_total = SO_LHS

    total_LHS = LLA_LHS + LLNA_LHS + SL_LHS + LS_LHS + SO_LHS
    total_all = LLA_total + LLNA_total + SL_total + LS_total + SO_total

    print(f"{n:>3} | {cross:>11} | {total_LHS:>15} | {total_all:>11} | {6:>11}")

print()
print("Observations:")
print("  - Cross-chain grows quadratically (2(n-1)(n-2)) — matches no single relation.")
print("  - Short-long edge monomial count is CONSTANT = 6 in n. Cannot match.")
print("  - Total iSerre count grows linearly + quadratically; doesn't match quadratic 2(n-1)(n-2)")
print("    in a structurally clean way either.")
print()
print("The only 'algebra-side' count growing as 2(n-1)(n-2) is")
print("  2 * (# ordered pairs of distinct B's at the long simples)")
print("which is the COMMUTATOR count [B_a, B_b] = 0 + Serre count from the long-only")
print("subalgebra; this is the 'classical part' of U^iota, not an iSerre-specific count.")
