# Kostant Game vs RAW Orbit-Swap Cross-Check on B_2 / C_2

Date: 2026-05-14. Source: Cortes-Cruz arXiv:2601.16326 (Defs 3.12 / 3.17 / 3.19).

## 1. The Kostant game (multiply-laced version, Def 3.17)

Configuration c = (c_1, ..., c_n) of non-neg integers on the Dynkin diagram.
At vertex i, with the Dynkin numbers n_{i,j} (= 1 if alpha_i, alpha_j same
length; if alpha_j is LONG and alpha_i is SHORT then n_{i,j} = 2 and
n_{j,i} = 1 — i.e. n_{i,j} is the entry in row i, column j of the
Cartan matrix's off-diagonal, with sign flipped).

Vertex i is SAD iff 2 c_i < sum_{j in N(i)} n_{i,j} c_j.

Move: pick a sad vertex i, do c_i -> -c_i + sum_{j in N(i)} n_{i,j} c_j.
This is exactly the simple reflection s_i on the height vector beta =
sum c_k alpha_k (Section 3.4 of the paper).

Theorem 3.19: For B_n, C_n, F_4, G_2 the game admits exactly TWO distinct
terminal configurations — one for each "side" of the multiple edge.

## 2. The B_2 game — concrete branching

B_2 Dynkin diagram: alpha_1 == alpha_2 (double edge, alpha_1 long, alpha_2 short).
n_{1,2} = 1 (alpha_1 long sees one short neighbor with one arrow), n_{2,1} = 2
(alpha_2 short sees one long neighbor with two arrows).

Start with c = (1, 0). Trace:

  Step | c       | sad?         | move
  -----+---------+--------------+----------------------------------
  0    | (1, 0)  | v_2 sad (0 < 1/2 * 2*1 = 1)  | fire v_2
  1    | (1, 2)  | v_1 sad (1 < 1/2 * 1*2 = 1)? NO (equality => happy). v_2: 2 < 1/2*2*1 = 1? NO. STOP.

Hmm — terminates immediately at (1, 2) = alpha_1 + 2 alpha_2 = e_0 + e_1
(highest root of B_2). Single move, no branching.

Try c = (0, 1):

  Step | c       | sad?                              | move
  -----+---------+-----------------------------------+--------
  0    | (0, 1)  | v_1 sad (0 < 1/2 * 1*1 = 1/2)     | fire v_1
  1    | (1, 1)  | v_1: 1 < 1/2 = false. v_2: 1 < 1 = false. STOP.

Terminates at (1, 1) = alpha_1 + alpha_2 = e_0. Also no branching.

The two terminal configurations described by Thm 3.19 are exactly (1, 2)
and (1, 1) — depending on which side of the double edge you started.
NO move-order non-determinism in B_2 itself, just initial-vertex
non-determinism.

## 3. Where the actual non-uniqueness lives

Re-read Thm 3.19: "The final configuration depends on whether the game
starts before the short root or after the long root, giving rise to only
two possible final configurations." This is INITIAL-VERTEX choice
non-uniqueness, not MOVE-ORDER non-uniqueness within a single trace.

In B_2 / C_2 specifically, once you pick the starting vertex, the game
trace is deterministic — there is only one sad vertex at any time. The
"non-uniqueness" of the game on doubly-laced types is structurally:

  Same Dynkin diagram + same protocol  ->  TWO terminal configurations
  (= two distinct positive roots reachable as game-terminal positions).

These two terminal positions are the HIGHEST SHORT ROOT and the HIGHEST
LONG ROOT of the root system. For B_2: e_0 + e_1 (long highest) and
e_0 (short highest).

For F_4 (paper's Fig 14) the game is longer and within one starting
vertex multiple sad vertices coexist, giving genuine move-order
branching — but still only TWO terminal configurations.

## 4. Mapping to Rick's RAW orbit-swap framework

Rick's RAW orbit-swap setup operates on Kostant partitions pi : Phi^+ ->
Z_{>=0}, applies signed (st, +/-) orbit transfers, and asks for which
multisets M satisfy apply(pi, M) = pi'. The unit count units(st) is the
shift in alpha_i units produced by one forward swap.

The Kostant game operates on a height vector c = (c_1, ..., c_n) and
applies the simple reflection s_i. These are different combinatorial
objects:

  - Kostant game state = a single positive root (encoded as
    height-vector in simple-root basis).
  - Rick RAW state = a Kostant partition (a multiset of positive roots,
    encoded as occupancy function).

The Kostant-game move "fire vertex i" = "apply s_i to current root
beta". Rick's orbit-swap move = "transfer one occupancy from beta_{st}
to s_i(beta_{st}) (or vice versa)". The first acts on a single root by
reflection; the second acts on a partition by single-orbit s_i-swap.

These ARE NOT the same operation. In particular:

  - The Kostant game move CHANGES THE ROOT (a length-1 random walk in
    Phi^+ steered by sadness).
  - Rick's orbit-swap PRESERVES THE PARTITION SHAPE up to an orbit-swap
    (a Z/2 swap inside one s_i-orbit of partition entries).

A single Rick orbit-swap on the partition pi = delta_{beta_{st}}
corresponds to a single Kostant-game s_i-move on beta = beta_{st}, with
units(st) = the alpha_i-shift = the LENGTH change of the Kostant-game
move. But the Rick framework allows pi to have multiple occupants,
which has no analogue in the single-root Kostant-game state.

## 5. The "two terminal configurations" in Rick's language

The two terminal configurations on B_2 are the highest short root (e_0)
and the highest long root (e_0 + e_1). In Rick's orbit-swap setting,
asking which root is reachable from a single-chip start by ITERATED
s_i-reflections corresponds to asking which W-orbit ends up at a
"sink" of the reflection process. But Rick's framework is not about
reflecting a single root — it's about which transfer multisets land
pi at pi'.

The MAP "Kostant game move = Rick orbit-swap" therefore has two issues:

  (a) Kostant game operates on a single root (size-1 partition);
      Rick operates on arbitrary partitions. The game is a strict
      subset of Rick's possible state space.

  (b) The Kostant game's non-uniqueness is INITIAL-DATA non-uniqueness
      (long-side start vs short-side start). Rick's RAW non-uniqueness
      is OPERATION non-uniqueness: same (pi, c) -> same pi' via
      different RAW multisets, differing by (+, -) cancellation pairs.

These are structurally distinct sources of non-uniqueness.

## 6. Where they DO share a fingerprint

The COMMON underlying fact is: doubly-laced root systems have
asymmetric n_{i,j} (e.g. n_{i,j} = 1 but n_{j,i} = 2 across the
double edge). This asymmetry creates:

  - For the Kostant game: two distinct "highest roots" (short and
    long), hence two terminal configurations.
  - For Rick's RAW count: subtypes with units(st) = 2 (e.g. the LL
    subtype at the C_2 short-exchange simple s_0). This 2-unit subtype
    means one forward swap = two backward swaps in alpha_i-shift, which
    creates the (+, -) Diophantine redundancy that REDUCED uniqueness
    fixes.

Both are downstream consequences of "doubly-laced" = "n_{i,j} != n_{j,i}".
But they are NOT the same combinatorial operation.

## 7. Concrete non-correspondence

In C_2, take the s_0 (short exchange e_0 - e_1) simple:

  - Subtype 'LL' = orbit {2e_0, 2e_1}, units = 2. This is the source
    of Rick's (+, -) RAW redundancy at C_2 s_0. A RAW pair like
    (m_{LL,+}, m_{LL,-}) = (2, 1) and (1, 0) both give signed count
    m_{LL} = 1, both produce the same Diophantine shift c = 2.

In the Kostant game on C_2:

  - Start at v_0 (= short simple e_0 - e_1) with c = (1, 0). Trace
    runs to a single terminal: c = (1, 2) = (e_0 - e_1) + 2 * 2e_1 ...
    no, in C_2 simples are alpha_0 = e_0 - e_1 (short), alpha_1 = 2 e_1
    (long), with n_{0,1} = 2, n_{1,0} = 1.

  - From c = (1, 0): v_1 sad (0 < 1/2 * 1 * 1 = 1/2). Fire v_1:
    c -> (1, 1). v_0: 1 < 1/2 * 2 * 1 = 1 false. v_1: 1 < 1/2 * 1 = 1/2
    false. STOP at (1, 1) = e_0 + e_1 (short highest root in C_2).

  - From c = (0, 1): v_0 sad (0 < 1/2 * 2 * 1 = 1). Fire v_0: c -> (2, 1).
    v_0: 2 < 1/2 * 2 * 1 = 1 false. v_1: 1 < 1/2 * 1 * 2 = 1 false.
    STOP at (2, 1) = 2 alpha_0 + alpha_1 = 2(e_0 - e_1) + 2 e_1 = 2 e_0
    (long highest root in C_2).

Two terminal configurations for C_2: (1, 1) and (2, 1), i.e. e_0 + e_1
(short) and 2 e_0 (long).

The Rick RAW (+, -) redundancy at C_2 s_0 LL-subtype is:
multiset {(LL,+): 1, (LL,-): 1} acts on any pi as IDENTITY (one forward,
one backward, signed count 0). This phantom multiset has NO analogue in
the Kostant game trace — the game state is a single root, not a
partition, and there is no "trivial cancel" move.

## 8. Verdict

VERDICT: NO. The two non-uniqueness phenomena are NOT the same operation.

  - Kostant game non-uniqueness on doubly-laced types = INITIAL-VERTEX
    non-uniqueness (long-side vs short-side start gives two distinct
    terminal positive roots, namely highest-long vs highest-short).
    Once the starting vertex is fixed, B_2 and C_2 traces are
    DETERMINISTIC (no branching during play, since at every step there
    is only one sad vertex). [For larger types like F_4, intra-trace
    branching exists per Fig 14, but the paper proves all branches
    converge to one of the SAME TWO terminal configurations.]

  - Rick RAW non-uniqueness = OPERATION non-uniqueness in the
    Diophantine multiset (m_{st,+}, m_{st,-}): two distinct RAW
    multisets, both reduced and increased by (k, k) cancellation
    pair, produce the same end-partition. This is a redundancy in the
    PARAMETRIZATION of orbit-swaps, with no analogue in single-root
    game state.

Both phenomena share an UPSTREAM CAUSE — the asymmetry n_{i,j} !=
n_{j,i} of doubly-laced Cartan matrices — but they are NOT the same
combinatorial operation, and Rick's "(+, -) cancellation reduction" is
not the move that "fixes" the Kostant game's non-uniqueness. The
Kostant game's two terminal configurations are STRUCTURAL (they are
the two highest roots — short and long — of the doubly-laced root
system) and persist under any sensible reduction; the REDUCED quotient
does not collapse them.

## 9. Confidence

Confidence: HIGH (0.85). The Kostant game's terminal configurations on
B_2 / C_2 are computed directly above and match Thm 3.19 of
arXiv:2601.16326. The Rick RAW (+, -) phantom operates on partitions
of arbitrary support, not single roots, and produces partition-level
identity moves with no game-state-level analogue.

CAVEAT: There may still be a deeper categorical statement linking
the two — e.g. both are obstructions to a certain "naive
symmetrisation" failing on doubly-laced types — but the naive
operational identification ("Kostant game branch step = Rick (+, -)
move") is false.

## 10. Recommendation for Rick

Downgrade the conjecture in
/home/agent/projects/memory/connections/kostant-game-and-reduced-uniqueness.md
from "structurally identical" to "shared upstream cause (Cartan-matrix
asymmetry) but operationally distinct". The Kostant game's terminal
non-uniqueness is the existence of two highest roots; Rick's RAW
non-uniqueness is Diophantine over-parametrisation of single-simple
orbit-swap multisets. They share the doubly-laced fingerprint but are
not the same move.

If a connection note is still desired, the right framing is: "Both
phenomena are doubly-laced-only consequences of n_{i,j} != n_{j,i};
neither reduction operation is the other, but both demonstrate that
the doubly-laced asymmetry has a combinatorial fingerprint at every
layer of root-system bookkeeping (single-root reflection AND
partition-level orbit-swap)." This is a footnote, not a paper.
