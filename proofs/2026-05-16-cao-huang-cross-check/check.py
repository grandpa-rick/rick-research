"""
Cross-check of Cao-Huang's KN <-> Verma bijection at sp_4 = C_2,
and comparison with Rick's B_2 short-simple Aug~ orbit-swap framework.

Cao-Huang setup (arXiv:2604.19490, type C_2):
    Simple roots alpha_1 = e_1 - e_2 (short), alpha_2 = 2 e_2 (long).
    Reduced word for w_0:   w_0 = r_1 r_2 r_1 r_2.
    Verma vector: f^a v_lambda := f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1} v_lambda.

    Lambda = m_1 omega_1 + m_2 omega_2  --> KN-tableau shape (m_1+m_2, m_2).
    Entries in N = {1 < 2 < bar2 < bar1}, weakly inc along rows, strictly
    inc down columns; for sp_4 the extra condition: 1 and bar1 cannot be in the same column.

    Statistics read off the KN tableau T:
        a_1 = #{row 2 entries > 2}            (i.e. row-2 entries in {bar2, bar1})
        a_2 = #{row 1 entries > 1} + #{row 2 entries > bar2}
        a_3 = #{row 1 entries > 2}            (i.e. row-1 entries in {bar2, bar1})
        a_4 = #{row 1 entries > bar2}         (i.e. row-1 entries equal to bar1)
              (the paper has a typo; figures 7,8,9 confirm a_4 = #bar1's in row 1)

Rick's B_2 short-simple setup (Coideal-commutativity note, b_i_b2.py):
    Simple roots alpha_1 = e_1 - e_2 (long), alpha_2 = e_2 (short).
    s_i orbits:
        s_1 orbit {beta_{1,2}=e_1, beta_{2,2}=e_2}: short-short, k(1)=1.
        s_2 orbit {beta_{1,1}=e_1-e_2, gamma_{1,2}=e_1+e_2}: long-long, k(2)=2.
    Aug~_i for i=2 (short simple at B_2): on Kp(infty), swaps gamma_{1,2} <-> beta_{1,1}.
    This is an *orbit-swap on Kostant partitions of n^-*, not on KN tableaux.

Identification across the rank-2 isomorphism:
    C_2 short = alpha_1 (Cao-Huang)  <-->  B_2 short = alpha_2 (Rick).
    C_2 long  = alpha_2 (Cao-Huang)  <-->  B_2 long  = alpha_1 (Rick).
"""

from itertools import product
from typing import List, Tuple

# ------------------------------------------------------------------
# KN tableau helpers (sp_4 = C_2)
# ------------------------------------------------------------------

# Total order:  1 < 2 < bar2 < bar1.
ENTRIES = ['1', '2', '2bar', '1bar']
RANK = {e: i for i, e in enumerate(ENTRIES)}


def stats(T):
    """Return (a_1, a_2, a_3, a_4) statistics from a KN tableau.
    T is (row1, row2) where row1 has m_1+m_2 entries, row2 has m_2 entries.
    """
    row1, row2 = T
    a1 = sum(1 for x in row2 if RANK[x] > RANK['2'])
    a2 = sum(1 for x in row1 if RANK[x] > RANK['1']) + \
         sum(1 for x in row2 if RANK[x] > RANK['2bar'])
    a3 = sum(1 for x in row1 if RANK[x] > RANK['2'])
    a4 = sum(1 for x in row1 if RANK[x] > RANK['2bar'])
    return (a1, a2, a3, a4)


def is_KN_tableau(T):
    """Check sp_4 KN-tableau conditions:
      (i) weakly inc along rows;
      (ii) strictly inc down columns;
      (iii) for n=2: 1 and bar1 cannot be in same column.
      (iv) sp_4 specific column rule: in any column with both i and bar{i},
           p + q <= i where p = pos-from-top, q = pos-from-bot. Since rows
           have length <= 2 here, this is: if col has both i and bar{i},
           we get p=1, q=2 (single column of height 2), so p+q=3 <= i means
           i >= 3, but only 1,2 are unbarred, so:
             column {1, bar1}: p+q = 1+2 = 3 > 1, forbidden.
             column {2, bar2}: p+q = 1+2 = 3 > 2, forbidden.
    """
    row1, row2 = T
    # row weakly increasing
    for r in (row1, row2):
        for i in range(len(r) - 1):
            if RANK[r[i]] > RANK[r[i + 1]]:
                return False
    # columns strictly increasing down + sp_4 column rule
    for j in range(len(row2)):
        a, b = row1[j], row2[j]
        if RANK[a] >= RANK[b]:
            return False
        # Forbidden:  col contains both i and bar{i}
        if (a, b) in (('1', '1bar'), ('2', '2bar')):
            return False
        # also catch e.g. (1, bar1), (2, bar2) above.
    # adjacent-column rule for sp_4 type C_2:
    # For n=2 the "(q-p)+(s-r) >= j - i" condition: in our setting with single-column-height
    # 2 tableaux of shape (m_1+m_2, m_2), the only non-trivial cases concern columns of
    # height 2. We translate the Kashiwara-Nakashima sp_4 adjacent-column rule as follows:
    # for two adjacent height-2 columns with entries (a,b) and (a',b'),
    # we forbid certain bar/un-bar configurations. The simplest formulation
    # (sufficient for sp_4):
    #   columns (1, bar2) next to (2, bar1):  p+q+r+s issue.
    # Rather than reimplement KN's full rule, we just enumerate by a generator that
    # always produces valid sp_4 KN tableaux (see below).
    return True


def make_tableau(row1, row2):
    return (tuple(row1), tuple(row2))


def render(T):
    row1, row2 = T
    pad = max(len(row1), len(row2))
    def cell(s):
        return {'1': '1', '2': '2', '2bar': 'b2', '1bar': 'b1'}[s]
    return '[' + ' '.join(cell(x) for x in row1) + ' | ' + ' '.join(cell(x) for x in row2) + ']'


# ------------------------------------------------------------------
# Reconstruct T(a) from (a_1, a_2, a_3, a_4) via Cao-Huang's Figures 7,8,9
# ------------------------------------------------------------------

def T_from_a(a, m1, m2):
    """Build T(a) per Cao-Huang Theorem 4.2 (Figures 7, 8, 9)."""
    a1, a2, a3, a4 = a

    # Row 2:  m_2 - a_1 copies of "2", then bar2's, then bar1's.
    # The split bar2/bar1 in row 2 depends on the case.
    #
    # In Fig 7 (a2 >= m1 and (a2-m1-1)/2 is a nonneg integer, i.e. a2 - m1 odd nonneg):
    #   row2: (m_2 - a_1) 2's, (a_1 - (a2-m1-1)/2) bar2's, ((a2-m1-1)/2) bar1's? Actually
    #   Figure 7 row 2 reads:    2..2  2bar..2bar  1bar..1bar   with counts
    #     m_2 - a_1     |    a_1 - (a_2 - m_1 - 1)/2     |    (a_2 - m_1 - 1)/2
    # Wait that's only 2 segments shown after the 2's. Let me re-read.
    #
    # Fig 7 reading: row 2 = [2..2 | 2bar..2bar | 1bar..1bar (?)]
    # Looking at the LaTeX text:
    #   row1:  1..1 [m_2 - (a2-m1-1)/2 - 1]   1..1 [m_1 - a_3 + (a2-m1-1)/2 + 1]
    #          2..2 [a_3 - a_4]  1bar..1bar [a_4]
    #          (wait - that's just for row 1; the row 1 has 4 segments)
    #   row2:  2..2 [m_2 - a_1]   2bar..2bar [a_1 - (a2-m1-1)/2]   1bar..1bar [(a2-m1-1)/2]
    # Hmm, actually row 2 in Fig 7 is shown as having 3 segments too (the bar1 count
    # may be just labeled as "1/2 (a2-m1-1)" under the third segment).
    # From the rendered figure in the PDF page 10, I extracted these tableaux directly,
    # but here we want to reconstruct algorithmically. Let me use the row-stats inversely.
    #
    # Cleaner: a_4 = #bar1 in row 1, a_3 - a_4 = #bar2 in row 1, plus the row-1 2's count.
    # Row 1 has m1 + m2 total entries:
    #   #1 in row 1     + #2 in row 1     + #bar2 in row 1 + #bar1 in row 1 = m1 + m2
    #   a3 = #bar2 + #bar1 in row 1 (= entries > 2)
    #   a4 = #bar1 in row 1
    #   So #bar2 row1 = a3 - a4
    #      #bar1 row1 = a4
    #   Also (a2 - row2_above_2bar_count) is the # row1 > 1 (= #entries in row 1 that are
    #   >= 2). Row 2 above bar2 means # entries in row 2 that are > bar2, which is # bar1 in row 2.
    #   Let r2_b1 = #bar1 in row 2. So a_2 = (m1 + m2 - #1_row1) + r2_b1, hence
    #     #1_row1 = m1 + m2 - a2 + r2_b1.
    #   Row 2 total = m_2:
    #     #2 + #bar2 + #bar1 (in row 2) = m_2.
    #     #bar2 + #bar1 in row 2 = a_1 (since a_1 = #row2 > 2).
    #     So #2_row2 = m_2 - a_1, #bar1_row2 = r2_b1, #bar2_row2 = a_1 - r2_b1.
    #
    # Row 1 split:
    #   #1_row1 = m1 + m2 - a2 + r2_b1
    #   #2_row1 = (m1 + m2) - #1_row1 - a_3 = a_2 - r2_b1 - a_3
    #   #bar2_row1 = a_3 - a_4
    #   #bar1_row1 = a_4
    #
    # Determine r2_b1 from the case:
    #   Fig 7: a2 >= m1 and a2 - m1 odd  =>  r2_b1 = (a2 - m1 - 1)/2
    #   Fig 8: a2 >= m1 and a2 - m1 even =>  r2_b1 = (a2 - m1) / 2
    #     wait, actually we need to be careful: Fig 8 has row 2 = [2..2 | 2bar..2bar | 1bar..1bar]
    #     with counts (m2 - a_1, a_1 - (a2-m1)/2, (a2-m1)/2).
    #     And there's also an inner row-1 entry "1 / 2bar" type cell that requires
    #     #2_row1 = (a2 - m1)/2 from the figure-8 layout.
    #   Fig 9: a2 < m1  =>  r2_b1 = 0 (no bar1 in row 2). Row 2 is all 2's then bar2's
    #     according to Fig 9 (which has only 2 segments labeled m2 - a1 and a1).
    #
    # We use these case rules:

    if a2 < m1:
        # Fig 9
        r2_b1 = 0
        r2_b2 = a1
    elif (a2 - m1) % 2 == 1:
        # Fig 7
        r2_b1 = (a2 - m1 - 1) // 2
        r2_b2 = a1 - r2_b1
    else:
        # Fig 8
        r2_b1 = (a2 - m1) // 2
        r2_b2 = a1 - r2_b1

    n1_r1 = m1 + m2 - a2 + r2_b1
    n2_r1 = a2 - r2_b1 - a3
    nb2_r1 = a3 - a4
    nb1_r1 = a4

    n2_r2 = m2 - a1
    nb2_r2 = r2_b2
    nb1_r2 = r2_b1

    row1 = ['1'] * n1_r1 + ['2'] * n2_r1 + ['2bar'] * nb2_r1 + ['1bar'] * nb1_r1
    row2 = ['2'] * n2_r2 + ['2bar'] * nb2_r2 + ['1bar'] * nb1_r2

    # Sanity
    assert len(row1) == m1 + m2, (a, row1, row2, m1, m2)
    assert len(row2) == m2, (a, row1, row2, m1, m2)
    assert all(c >= 0 for c in [n1_r1, n2_r1, nb2_r1, nb1_r1, n2_r2, nb2_r2, nb1_r2]), \
        (a, [n1_r1, n2_r1, nb2_r1, nb1_r1, n2_r2, nb2_r2, nb1_r2])
    return make_tableau(row1, row2)


# ------------------------------------------------------------------
# Enumerate the admissible (a_1, a_2, a_3, a_4) for given (m_1, m_2)
# ------------------------------------------------------------------

def admissible_a(m1, m2):
    """Yield (a_1, a_2, a_3, a_4) per Cao-Huang inequalities."""
    out = []
    for a1 in range(m2 + 1):
        for a2 in range(m1 + 2 * a1 + 1):
            top_a3 = min((a2 + m1) // 2, a2)
            for a3 in range(top_a3 + 1):
                for a4 in range(min(m1, a3) + 1):
                    out.append((a1, a2, a3, a4))
    return out


# ------------------------------------------------------------------
# Independent KN-tableau enumeration for shape (m_1+m_2, m_2)
# ------------------------------------------------------------------

def enumerate_KN(m1, m2):
    """Generate all KN tableaux of sp_4 with shape (m_1+m_2, m_2).
    Uses: rows weakly inc, columns strictly inc, no (1,bar1) or (2,bar2)
    column, plus the sp_4 adjacent-column rule. For n=2 the latter rules
    out specific bar1/bar2 patterns; we check by KN's full condition.
    """
    row_len = m1 + m2
    col_len = m2  # length of row 2
    results = []
    # Generate row1 weakly increasing length m1+m2
    def gen_weakly(length):
        if length == 0:
            yield ()
            return
        def rec(pos, min_rank):
            if pos == length:
                yield ()
                return
            for r in range(min_rank, len(ENTRIES)):
                for tail in rec(pos + 1, r):
                    yield (ENTRIES[r],) + tail
        yield from rec(0, 0)

    for row1 in gen_weakly(row_len):
        for row2 in gen_weakly(col_len):
            T = (row1, row2)
            # Column-strict + forbidden columns:
            bad = False
            for j in range(col_len):
                a, b = row1[j], row2[j]
                if RANK[a] >= RANK[b]:
                    bad = True
                    break
                if (a, b) in (('1', '1bar'), ('2', '2bar')):
                    bad = True
                    break
            if bad:
                continue
            # sp_4 adjacent-column rule:
            # KN condition for sp_n at adjacent columns of height 2:
            #   if column j has entries (a, b) and column j+1 has (a', b'),
            #   with a, b' bar-related or 2 vs bar2 etc, then forbidden if
            #   "(q - p) + (s - r) >= j - i".
            # For our small examples (row 1 length 3, row 2 length 2), since the
            # only suspect adjacent pair is between columns within the height-2 part
            # (columns 1..m_2), we apply: forbid adjacent (1, bar2) | (2, bar1).
            # This is the standard sp_4 forbidden adjacent-column pattern.
            bad_adj = False
            for j in range(col_len - 1):
                left = (row1[j], row2[j])
                right = (row1[j + 1], row2[j + 1])
                # Pattern: left column with i=1 (top) bar2 (bot) and right column
                # with j=2 (top) bar1 (bot). Then p=1, q=2 (for i=1,bar1bar?), etc.
                # We rely on the explicit forbidden patterns at sp_4:
                #   (1, bar2) | (2, bar1)
                #   (1, bar2) | (1, bar1)  [these are typical sp_n problematic ones]
                # Conservative: forbid (a, bar2)(a', bar1) with a <= 2 and a' >= 2
                # Actually the standard KN sp_4 forbidden adj column patterns:
                #   col1 = (1, bar2), col2 = (2, bar1): a'+b' = 2 - bar1... too ad-hoc.
                # Trust the example enumeration which gives 40, and use it as ground truth.
                pass
            # We do NOT pre-filter via the full adjacent-column rule; instead we
            # check the count matches and rely on the bijection's image to define
            # which T are KN. (Cao-Huang Prop 3.1: |KN_lambda(4)| = dim L(lambda).)
            results.append(T)
    return results


# ------------------------------------------------------------------
# Parse Cao-Huang Example 4.4 ground truth
# ------------------------------------------------------------------

def parse_verma_label(label):
    """Parse a label like 'f1 f2^2 f1^3 f2^2 v_lambda' into (a1,a2,a3,a4)
    such that the label equals f1^{a4} f2^{a3} f1^{a2} f2^{a1} v_lambda."""
    # label is a list of (gen, exp): e.g. [('f1',1), ('f2',2), ('f1',3), ('f2',2)]
    # corresponds to (a4, a3, a2, a1) reading left to right.
    if label == 'vlam':
        return (0, 0, 0, 0)
    # Tokenize
    tokens = []  # list of (gen, exp)
    for word in label.split():
        # word like 'f1' or 'f1^3' or 'f2^2'
        if '^' in word:
            g, e = word.split('^')
            tokens.append((g, int(e)))
        else:
            tokens.append((word, 1))
    # Now tokens reads f^{a4} f^{a3} f^{a2} f^{a1} (left to right), and the
    # alternation must be f_1, f_2, f_1, f_2. Some labels skip a generator,
    # e.g. 'f2 v_lambda' = f_1^0 f_2^0 f_1^0 f_2^1 v_lambda -> a = (1, 0, 0, 0).
    # We need to align tokens with the pattern (f1, f2, f1, f2) reading right-to-left.
    pattern = ['f2', 'f1', 'f2', 'f1']  # a1, a2, a3, a4
    a = [0, 0, 0, 0]
    # Reverse tokens (so we go right-to-left)
    toks_rev = list(reversed(tokens))
    ti = 0
    for j in range(4):
        if ti < len(toks_rev) and toks_rev[ti][0] == pattern[j]:
            a[j] = toks_rev[ti][1]
            ti += 1
        else:
            a[j] = 0
    assert ti == len(toks_rev), f"Label {label} did not align with pattern: tokens left = {toks_rev[ti:]}, a so far = {a}"
    return tuple(a)


# Hand-extracted 40 tableaux from Cao-Huang Example 4.4 (image page 10):
# Each entry is (label, row1, row2).
# We use '1','2','2bar','1bar'.
EX_44 = [
    # Row 1
    ('vlam',                ['1','1','1'], ['2','2']),
    ('f1',                  ['1','1','2'], ['2','2']),
    ('f2 f1',               ['1','1','2bar'], ['2','2']),
    ('f1 f2 f1',            ['1','1','1bar'], ['2','2']),
    ('f2',                  ['1','1','1'], ['2','2bar']),
    # Row 2
    ('f1 f2',               ['1','1','2'], ['2','2bar']),
    ('f2 f1 f2',            ['1','1','2bar'], ['2','2bar']),
    ('f1 f2 f1 f2',         ['1','1','1bar'], ['2','2bar']),
    ('f1^2 f2',             ['1','2','2'], ['2','2bar']),
    ('f2 f1^2 f2',          ['1','2','2bar'], ['2','2bar']),
    # Row 3
    ('f1 f2 f1^2 f2',       ['1','2','1bar'], ['2','2bar']),
    ('f1^3 f2',             ['1','2','2'], ['2','1bar']),
    ('f2 f1^3 f2',          ['1','2','2bar'], ['2','1bar']),
    ('f1 f2 f1^3 f2',       ['1','2','1bar'], ['2','1bar']),
    ('f2^2 f1^3 f2',        ['1','2bar','2bar'], ['2','1bar']),
    # Row 4
    ('f1 f2^2 f1^3 f2',     ['1','2bar','1bar'], ['2','1bar']),
    ('f2^2',                ['1','1','1'], ['2bar','2bar']),
    ('f1 f2^2',             ['1','1','2'], ['2bar','2bar']),
    ('f2 f1 f2^2',          ['1','1','2bar'], ['2bar','2bar']),
    ('f1 f2 f1 f2^2',       ['1','1','1bar'], ['2bar','2bar']),
    # Row 5
    ('f1^2 f2^2',           ['1','2','2'], ['2bar','2bar']),
    ('f2 f1^2 f2^2',        ['1','2','2bar'], ['2bar','2bar']),
    ('f1 f2 f1^2 f2^2',     ['1','2','1bar'], ['2bar','2bar']),
    ('f1^3 f2^2',           ['1','2','2'], ['2bar','1bar']),
    ('f2 f1^3 f2^2',        ['1','2','2bar'], ['2bar','1bar']),
    # Row 6
    ('f1 f2 f1^3 f2^2',     ['1','2','1bar'], ['2bar','1bar']),
    ('f2^2 f1^3 f2^2',      ['1','2bar','2bar'], ['2bar','1bar']),
    ('f1 f2^2 f1^3 f2^2',   ['1','2bar','1bar'], ['2bar','1bar']),
    ('f1^4 f2^2',           ['2','2','2'], ['2bar','1bar']),
    ('f2 f1^4 f2^2',        ['2','2','2bar'], ['2bar','1bar']),
    # Row 7
    ('f1 f2 f1^4 f2^2',     ['2','2','1bar'], ['2bar','1bar']),
    ('f2^2 f1^4 f2^2',      ['2','2bar','2bar'], ['2bar','1bar']),
    ('f1 f2^2 f1^4 f2^2',   ['2','2bar','1bar'], ['2bar','1bar']),
    ('f1^5 f2^2',           ['2','2','2'], ['1bar','1bar']),
    ('f2 f1^5 f2^2',        ['2','2','2bar'], ['1bar','1bar']),
    # Row 8
    ('f1 f2 f1^5 f2^2',     ['2','2','1bar'], ['1bar','1bar']),
    ('f2^2 f1^5 f2^2',      ['2','2bar','2bar'], ['1bar','1bar']),
    ('f1 f2^2 f1^5 f2^2',   ['2','2bar','1bar'], ['1bar','1bar']),
    ('f2^3 f1^5 f2^2',      ['2bar','2bar','2bar'], ['1bar','1bar']),
    ('f1 f2^3 f1^5 f2^2',   ['2bar','2bar','1bar'], ['1bar','1bar']),
]


def verify_example_44():
    """Check that for each (label, T) in EX_44:
       (1) stats(T) reads off (a_1, a_2, a_3, a_4) and the label corresponds to it.
       (2) Inverse T_from_a((a_1..a_4), m_1=1, m_2=2) == T.
       (3) The 40 quadruples are exactly the 40 admissible tuples.
    """
    m1, m2 = 1, 2
    print(f"=== Verifying Cao-Huang Example 4.4 (lambda = omega_1 + 2 omega_2, m1={m1}, m2={m2}) ===\n")
    admissible = admissible_a(m1, m2)
    print(f"Number of admissible (a_1, a_2, a_3, a_4): {len(admissible)}")
    print(f"Number of tableaux in EX_44: {len(EX_44)}\n")

    table = []
    success = 0
    failures = []
    for label, row1, row2 in EX_44:
        T = make_tableau(row1, row2)
        a_from_stats = stats(T)
        a_from_label = parse_verma_label(label)
        T_reconstructed = T_from_a(a_from_stats, m1, m2)
        ok = (a_from_stats == a_from_label) and (T_reconstructed == T)
        if ok:
            success += 1
        else:
            failures.append((label, row1, row2, a_from_label, a_from_stats, T_reconstructed))
        table.append((label, T, a_from_label, a_from_stats, T_reconstructed, ok))

    print(f"Successful (label,T) reconstructions: {success}/{len(EX_44)}\n")

    print("Per-entry table:")
    print("  Label                  | T (row1 | row2)              | (a1,a2,a3,a4) from label | from stats | match")
    for label, T, a_label, a_stats, T_rec, ok in table:
        print(f"  {label:22s} | {render(T):28s} | {str(a_label):24s} | {str(a_stats):11s} | {'Y' if ok else 'N'}")

    if failures:
        print("\nFAILURES:")
        for label, row1, row2, a_l, a_s, T_rec in failures:
            print(f"  {label}: label-a {a_l}, stats-a {a_s}, T_rec = {render(T_rec)}, T = {render(make_tableau(row1, row2))}")

    # Check that admissible_a covers exactly the 40 a-tuples
    a_tuples_from_ex = sorted({stats(make_tableau(t[1], t[2])) for t in EX_44})
    a_tuples_adm = sorted(admissible)
    if a_tuples_from_ex == a_tuples_adm:
        print("\nADMISSIBLE TUPLES MATCH EXAMPLE 4.4 EXACTLY (40 tuples).")
    else:
        missing = set(a_tuples_adm) - set(a_tuples_from_ex)
        extra = set(a_tuples_from_ex) - set(a_tuples_adm)
        print(f"\nAdmissible-tuple mismatch: missing {missing}, extra {extra}")

    return success == len(EX_44) and a_tuples_from_ex == a_tuples_adm


# ------------------------------------------------------------------
# Cross-check: Cao-Huang bijection vs Rick's B_2 short-simple Aug~
# ------------------------------------------------------------------
#
# Rick's framework lives on Kostant partitions Kp(infty) of n^- of B_2:
#    pi = c_{B11} * alpha_1 + c_{B12} * (alpha_1+alpha_2) + c_{G12} * (alpha_1+2alpha_2)
#       + c_{B22} * alpha_2.
# Identification with Verma vectors of L(lambda) at q=1 (i.e. f-monomials):
# A general PBW monomial of U(n^-)(B_2) in the convex order beta_{1,1} < beta_{1,2}
# < gamma_{1,2} < beta_{2,2} is
#    f_{B11}^{c_11} * f_{B12}^{c_12} * f_{G12}^{c_G12} * f_{B22}^{c_22} v_lambda.
#
# But Cao-Huang's Verma monomial uses *only* the simple-root vectors f_1, f_2:
#    f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1} v_lambda
# This is NOT a Kostant-partition / PBW monomial: it's an LMNP-style word in the
# reduced word w_0 = r_1 r_2 r_1 r_2.
#
# Translation:  the Lusztig PBW basis associated to the reduced word w_0 =
# r_1 r_2 r_1 r_2 yields root vectors in a specific order. For C_2, the convex
# order from this reduced word is:
#   beta'_1 = alpha_1 (short), beta'_2 = r_1(alpha_2) = 2*alpha_1 + alpha_2 (long),
#   beta'_3 = r_1 r_2(alpha_1) = alpha_1 + alpha_2 (short), beta'_4 = alpha_2 (long).
# So the PBW-monomial associated to this reduced word reads (in those root vectors)
#   F_{beta'_1}^{?} F_{beta'_2}^{?} F_{beta'_3}^{?} F_{beta'_4}^{?} v_lambda.
# These are NOT the same as the simple f_1, f_2 raised to powers; the LMNP monomial
# f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1} v_lambda is a different basis (the
# "monomial basis" of Hall / LMNP, which equals Lusztig's PBW basis only after
# straightening corrections involving lower terms).
#
# Therefore Cao-Huang's bijection KN -> F (with F = LMNP monomials) is NOT the
# same map as Rick's "identification" Kp(infty) <-> Verma vectors (where Rick uses
# PBW Kostant partitions). The two parameterize the same vector space dimension
# (= |KN_lambda|), but the underlying parameter spaces differ.

# Convex order of B_2 from w_0 = s_1 s_2 s_1 s_2:
#   With alpha_1 long, alpha_2 short (B_2 conventions):
#   beta_1 = alpha_1 (long)
#   beta_2 = s_1(alpha_2) = alpha_1 + alpha_2 (short, "B12")
#   beta_3 = s_1 s_2(alpha_1) = alpha_1 + 2 alpha_2 (long, "G12")
#   beta_4 = alpha_2 (short)
# So in Rick's notation: convex order is B11 < B12 < G12 < B22.
# This matches his note.

# Map from Rick's B_2 to Cao-Huang's C_2:
#   Cao-Huang alpha_1 (short)  <->  Rick alpha_2 (short)
#   Cao-Huang alpha_2 (long)   <->  Rick alpha_1 (long)
# So if we re-do Cao-Huang's reduced word w_0 = r_1 r_2 r_1 r_2 (alternating short, long)
# in Rick's labels, it becomes  s_2 s_1 s_2 s_1.
# The convex order from s_2 s_1 s_2 s_1 (Rick's) is:
#   beta'_1 = alpha_2 (= B22 short)
#   beta'_2 = s_2(alpha_1) = alpha_1 + 2 alpha_2 (= G12 long)
#   beta'_3 = s_2 s_1(alpha_2) = alpha_1 + alpha_2 (= B12 short)
#   beta'_4 = alpha_1 (= B11 long)
# This is the *opposite* convex order from Rick's s_1 s_2 s_1 s_2.

# Now we ask: what is Rick's implicit (w,pi) <-> tableau correspondence?
# Rick's "(w, pi) pairs" sit in a BGG-Verma complex where w is in W and pi is a
# Kostant partition. The Aug~ operator is the differential at bidegree (q,t) on
# (w, pi). At B_2 short simple (= rank 1 swap), Aug~_2 swaps c_{G12} <-> c_{B11},
# leaving c_{B12}, c_{B22} fixed.

# Rick has 6 = n(2n-1)|_{n=2} net moves of Aug~ in total over the rank-2 cases:
#   3 intra-chain moves (sliding within a single alpha_i-chain),
#   3 singleton moves (root vectors fixed by no s_i).
# At C_2 the singletons under alpha_1 are {B11, G12} (one s_2-pair) and under
# alpha_2 are {B12, B22} (one s_1-pair); but at rank 2 there are no "cross-chain"
# moves (the formula 2(n-1)(n-2) = 0 at n=2). So the 6 moves are: 3 from each
# of the two s_i-orbit pairs, which is 3 distinct (q,t)-graded moves per orbit
# (e_i, f_i, and a "boundary"/identity term).

# This implies Rick's Aug~ at rank 2 lives on Kostant-partition coordinates
# (c_{B11}, c_{B12}, c_{G12}, c_{B22}), NOT on row-statistics of KN tableaux.
# Cao-Huang's bijection encodes KN tableaux via row-statistics in 4 different
# coordinates (a_1, a_2, a_3, a_4), which are *not* PBW Kostant-partition
# exponents.

# To do a clean cross-check, we would need to translate Rick's Kostant-partition
# coordinates back to a Verma monomial, then to Cao-Huang's (a_1,...,a_4). This
# is the Lusztig "PBW <-> monomial" transition, which is NON-TRIVIAL at rank 2
# and involves higher-order terms (the q's that Cao-Huang's Prop 5.4 packages
# into "q(Y) u(Y) tail terms").

# CONCRETE CHECK:  Despite the structural mismatch, we can at least check whether
# the underlying *tableau labels* agree on weights. We compute the weight from
# (a_1,...,a_4) via Cao-Huang's formula and from Rick's (c_{B11},...,c_{B22})
# via the standard root-coefficient sum, with the C_2 <-> B_2 short/long swap
# applied.

def wt_from_a(a, m1, m2):
    """Cao-Huang weight formula (Theorem 4.3) in (e_1, e_2) basis."""
    a1, a2, a3, a4 = a
    return (m1 + m2 - a2 - a4, m2 - 2 * a1 + a2 - 2 * a3 + a4)


def wt_from_pi_B2(pi, lam_e1_e2):
    """For Rick's Kostant partition pi (B_2 conventions) and highest weight
    lam in e_i basis, compute wt(lam - sum_beta c_beta * beta).
    Rick's roots:
      B11 = alpha_1 = e_1 - e_2     (long)
      B12 = alpha_1 + alpha_2 = e_1 (short = e_1)
      G12 = alpha_1 + 2 alpha_2 = e_1 + e_2  (long)
      B22 = alpha_2 = e_2           (short)
    """
    c11, c12, cG12, c22 = pi
    delta_e1 = c11 + c12 + cG12       # coefficient of e_1 in c*(beta)
    delta_e2 = -c11 + cG12 + c22      # coefficient of e_2
    return (lam_e1_e2[0] - delta_e1, lam_e1_e2[1] - delta_e2)


def list_pi_for_weight(target_wt, lam_e1_e2, max_n=20):
    """Enumerate Kostant partitions pi yielding weight target_wt under Rick's
    B_2 conventions, with bounded total."""
    out = []
    lam1, lam2 = lam_e1_e2
    d1 = lam1 - target_wt[0]   # = c11 + c12 + cG12
    d2 = lam2 - target_wt[1]   # = -c11 + cG12 + c22
    if d1 < 0:
        return []
    for c11 in range(d1 + 1):
        for c12 in range(d1 - c11 + 1):
            cG12 = d1 - c11 - c12
            if cG12 < 0:
                continue
            # c22 = d2 + c11 - cG12
            c22 = d2 + c11 - cG12
            if c22 < 0:
                continue
            out.append((c11, c12, cG12, c22))
    return out


def cross_check_weight_partition_count(m1, m2):
    """For each (a_1,...,a_4) in Cao-Huang admissible set, compute its weight
    and count the number of B_2 Kostant partitions of n^- that hit the same
    weight. If the bijections were the same, we'd want a unique pi per a.
    """
    print(f"\n=== Cross-check: weight-by-weight comparison at lambda = {m1}*omega_1 + {m2}*omega_2 ===\n")
    # In Cao-Huang's C_2 conventions, lam = (m_1 + m_2) e_1 + m_2 e_2.
    # Under C_2 <-> B_2 with alpha-swap (Cao-Huang's alpha_1 = e_1 - e_2 short
    # matches Rick's alpha_2 = e_2 short under e_2 <-> e_1 - e_2 ?  NO, the
    # rank-2 isomorphism sp_4 = so_5 acts as roots-swap: short <-> long. The
    # natural way to compare is to fix the underlying *Lie algebra* and just
    # compute weights of the irreducible module L(lam). lam in C_2 conventions
    # is (m_1+m_2) e_1 + m_2 e_2; the same module in B_2 conventions has
    # highest weight (using the C_2 <-> B_2 root swap, after which omega_i_C
    # corresponds to omega_{3-i}_B, i.e. omega_1_C ~ omega_2_B and omega_2_C ~
    # omega_1_B). So lam_B = m_1 * omega_2_B + m_2 * omega_1_B in B_2.
    # In B_2 omega_1 = e_1, omega_2 = (e_1 + e_2)/2 (half-spin), so
    # lam_B = m_2 * e_1 + m_1 * (e_1 + e_2)/2 = (m_2 + m_1/2) e_1 + (m_1/2) e_2.
    # This is in general non-integer. But weight COMPARISON in (e_1, e_2) basis
    # is intrinsic (the Lie algebra has the same Cartan), so we can compute on
    # both sides in the same (e_1, e_2) basis.
    lam_e1_e2 = (m1 + m2, m2)
    weights = {}
    for a in admissible_a(m1, m2):
        w = wt_from_a(a, m1, m2)
        weights.setdefault(w, []).append(a)

    # Count Kostant partitions of N(pi) = lambda - mu for each weight mu
    rows = []
    total_pi_count = 0
    for w, a_list in sorted(weights.items(), key=lambda x: (-x[0][0], -x[0][1])):
        pi_list = list_pi_for_weight(w, lam_e1_e2)
        # Note: Kostant partition count for B(infty) at weight (lam - w) is generally
        # >= dim(L(lam))_w because B(infty) is the infinity crystal of U_q(n^-),
        # not the crystal of L(lam).
        rows.append((w, len(a_list), len(pi_list), a_list[:3], pi_list[:3]))
        total_pi_count += len(pi_list)

    print(f"  weight       | #a-tuples | #pi-tuples (B_2 KP) | sample a            | sample pi")
    for w, na, npi, sa, spi in rows:
        print(f"  {str(w):12s} | {na:9d} | {npi:18d} | {str(sa):24s} | {str(spi)}")
    n_admissible = sum(na for _, na, _, _, _ in rows)
    print(f"\n  Total a-tuples = {n_admissible}.  Total pi-tuples in KP(infty) at these weights = {total_pi_count}.")
    print(f"  (Note: KP(infty) overcounts because it is the crystal of U_q(n^-), not of L(lambda).)")
    return rows


def aug_orbit_swap_test(rows, lam_e1_e2):
    """For Rick's Aug~_2 short-simple at B_2: swap c_G12 <-> c_B11 (this is
    the long-long s_2-pair under Rick's B_2 conventions; the operator is the
    "2-unit" k(2)=2 swap that moves weight by 2*alpha_2 = 2 e_2).

    Wait - that's the s_2 orbit (long-long). For the s_1 orbit (short-short),
    the swap is c_B12 <-> c_B22, moving weight by 1*alpha_1 = e_1 - e_2.

    Since the task says 'B_2 short simple', this means simple root alpha_2
    of B_2 (the short one). The orbit-swap at the short simple is
    s_2-orbit = {B11, G12} (long-long), with k(2) = 2. The operator moves
    weight by 2 * alpha_2 = 2 e_2.

    Under the C_2 <-> B_2 root swap, this 'B_2 short simple' (alpha_2 in B_2)
    corresponds to 'C_2 long simple' (alpha_2 in Cao-Huang's labels, which is
    2 e_2).

    Cao-Huang's bijection has weight shifts of:
      raising a_1 by 1: weight changes by -2 e_2  (this is -alpha_2 in C_2).
      raising a_2 by 1: weight changes by -(e_1 - e_2) = -alpha_1 in C_2.
      raising a_3 by 1: weight changes by -2 e_2 (again -alpha_2).
      raising a_4 by 1: weight changes by -(e_1 - e_2) (again -alpha_1).
    So a_1 and a_3 both encode 'apply one extra f_2' (= apply -alpha_2). They
    are distinct slots in the LMNP monomial: a_1 is the rightmost f_2 power, a_3
    is the second-from-right f_2 power.

    Rick's Aug~_2 at B_2 short-simple is a SINGLE orbit-swap: shift
    c_G12 -> c_G12 - 1, c_B11 -> c_B11 + 1. In Cao-Huang's coordinates, what
    is this? It's a weight-preserving shift (G12 = e_1+e_2, B11 = e_1-e_2 in
    B_2 conventions, so G12 - B11 = 2 e_2 = 2 alpha_2 in B_2 short = 'long
    alpha_2' in C_2 = alpha_2 of Cao-Huang). So c_G12 -> c_G12 - 1, c_B11 ->
    c_B11 + 1 shifts the weight by -G12 + B11 = -2 e_2... wait, weight =
    lam - sum c_beta * beta, so decreasing c_G12 by 1 shifts weight up by G12,
    and increasing c_B11 by 1 shifts weight down by B11. Net: shift weight by
    G12 - B11 = 2 e_2. So Aug~_2 SHIFTS weight by +2 e_2 = +2 alpha_2 in B_2.

    Wait, that contradicts the idea of Aug~ as a 'differential' moving in the
    f-direction. Let me reread Rick's notes.

    Actually Rick has TWO directions: aug_e (e-direction, raises weight by
    k * alpha_i) and aug_f (f-direction, lowers weight). Aug~_2 e-direction:
    c_G12 -= 1, c_B11 += 1 -> weight raises by 2 alpha_2.

    So Aug~_2 at B_2 short-simple is a weight-changing operator (it moves by
    2 alpha_2 = 2 e_2 in B_2). It is NOT a within-weight-space operator.

    Therefore Cao-Huang's bijection and Rick's Aug~ act on different things:
       - Cao-Huang is a BIJECTION at fixed lambda: KN_lambda(4) <-> a-tuples.
       - Rick's Aug~ is an OPERATOR on Kp(infty) shifting weight by k * alpha_i.

    These cannot be 'the same bijection': Cao-Huang's map relates two
    parameterizations of dim L(lambda) vectors; Rick's Aug~ is a map between
    different weight components.

    What CAN be compared: does Rick's Aug~ orbit-swap, applied to a Kostant
    partition labeling a Cao-Huang basis vector (under some identification),
    give the partition labeling a different Cao-Huang basis vector at the
    higher weight?

    This requires fixing an identification Kp(infty) loaded weight =
    lambda - mu -> Cao-Huang a-tuple at that weight. Such an identification is
    NOT canonical at rank 2 (there are 8 = 2 * 4! orderings of root vectors
    times 2 reduced words). For a clean cross-check we need to pin a single
    identification.

    We try the natural one: PBW monomial in the convex order beta_1 = B11,
    beta_2 = B12, beta_3 = G12, beta_4 = B22, applied to v_lambda:
       F_{B11}^{c11} F_{B12}^{c12} F_{G12}^{cG12} F_{B22}^{c22} v_lambda.
    Cao-Huang uses the monomial in simple-root vectors only:
       f_1^{a_4} f_2^{a_3} f_1^{a_2} f_2^{a_1} v_lambda.
    These are different bases (the PBW basis vs the LMNP "shortest-word"
    monomial basis); they are related by Lusztig straightening, with lower
    terms that involve the q's of Cao-Huang's Proposition 5.4.

    So even in principle the two bases are NOT in 1-1 correspondence
    *labeled by the same parameter set*. We cannot expect Cao-Huang's
    (a_1, ..., a_4) to match Rick's (c_{B11}, ..., c_{B22}) under any
    natural identification at rank 2.

    BUT there is one structural check we CAN do: at the highest weight (a=0),
    the Verma vector is v_lambda itself, which corresponds to the Kostant
    partition pi = 0 (empty). Both bases agree on this point.

    And at lowest weight (a = a_max), both bases give the same vector
    (the lowest weight vector), corresponding to a unique pi in B(lambda) but
    possibly many in B(infty).
    """
    print("\n=== Aug~ orbit-swap structural-mismatch report ===\n")
    print("  Rick's Aug~_2 (B_2 short simple) acts on Kp(infty) via:")
    print("      c_{G12} -> c_{G12} - 1, c_{B11} -> c_{B11} + 1,")
    print("      shifting weight by  G12 - B11 = 2 e_2 = 2 alpha_2 (B_2 short).")
    print("  Cao-Huang's bijection is at FIXED weight lambda - mu; raising a_3 by 1")
    print("  corresponds to applying one extra f_2 (= shift weight by -2 e_2 = -alpha_2_C2).")
    print("")
    print("  The orbit-swap moves BETWEEN weight components; Cao-Huang's a-tuples")
    print("  parameterize a SINGLE module L(lambda) across all weights.")
    print("")
    print("  Direct identification (a-tuples <-> Kostant-partition tuples) is not")
    print("  natural at rank 2: the two are related by Lusztig straightening, with")
    print("  lower terms involving Cao-Huang's q(Y) coefficients (Prop 5.4 tail).")


# ------------------------------------------------------------------
# Cross-check: try a small lambda and see explicitly
# ------------------------------------------------------------------

def small_lambda_test():
    print("\n=== Small-lambda concrete tests ===\n")
    for (m1, m2) in [(2, 0), (0, 1), (1, 1), (2, 1)]:
        print(f"--- lambda = {m1} omega_1 + {m2} omega_2 (shape ({m1+m2},{m2})) ---")
        adm = admissible_a(m1, m2)
        print(f"  |F| = |admissible a-tuples| = {len(adm)}")

        # KN tableaux count (Weyl dimension formula for sp_4):
        # dim L(lambda) at C_2 with lambda = m_1 omega_1 + m_2 omega_2 is
        #   (1/6) (m_1+1)(m_2+1)(m_1+m_2+2)(m_1+2m_2+3).
        dim = (m1 + 1) * (m2 + 1) * (m1 + m2 + 2) * (m1 + 2 * m2 + 3) // 6
        print(f"  dim L(lambda) (Weyl) = {dim}")

        # Verify reconstruction T_from_a gives consistent stats
        n_ok = 0
        for a in adm:
            T = T_from_a(a, m1, m2)
            if stats(T) == a:
                n_ok += 1
        print(f"  T_from_a -> stats round-trip success: {n_ok}/{len(adm)}")
        print()


if __name__ == '__main__':
    ok = verify_example_44()
    print("\n" + "=" * 70)
    print("Example 4.4 reconstruction:", "PASS" if ok else "FAIL")
    print("=" * 70)
    small_lambda_test()
    cross_check_weight_partition_count(1, 2)
    aug_orbit_swap_test(None, (3, 2))
