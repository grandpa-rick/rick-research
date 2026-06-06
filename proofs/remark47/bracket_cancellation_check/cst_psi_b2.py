"""
Compute Psi^{-1} from a B_2 Kostant partition to a marginally-large tableau,
and compute Kashiwara crystal operators e_i, f_i on the tableau side
(via bracket cancellation on the i-signature).

Reference: Criswell-Salisbury-Tingley arXiv:1708.04311 Theorem 3.1 and Def 2.6/2.7.

B_2 setup:
  Alphabet J(B_2) = {1 < 2 < 0 < 2bar < 1bar}.  Internal codes:
    1 -> 1, 2 -> 2, 0 -> 3, 2bar -> 4, 1bar -> 5  (so order matches).
  In each row j of a marginally-large tableau:
    - Row 1 starts with at least one '1' (length of row 2 + 1 copies of '1').
    - Row 2 starts with at least one '2' (length of row 3 + 1 = 1 copy of '2').

  Positive roots:
    beta_{1,1} = e_1 - e_2  (long-diff)
    gamma_{1,2} = e_1 + e_2 (long-sum)
    beta_{1,2} = e_1        (short, B-only: row 1 contributes via "0" or "(2, 2bar)")
    beta_{2,2} = e_2        (short, B-only: row 2 "2bar" gives 2*beta_{2,2})

  Psi (T -> alpha):
    Row 1 (j=1) contents (beyond shaded '1's):
      Each '(2, 2bar)' pair -> 2*beta_{1,2} = 2*e_1  (rule 1 with n=2)
      Each '0'             -> beta_{1,2} = e_1       (rule 2)
      Each unpaired '2'    -> beta_{1, 2-1} = beta_{1,1} = e_1 - e_2  (rule 8 with k=2)
      Each unpaired '2bar' -> gamma_{1,2} = e_1 + e_2 (rule 9 with k=2)
      [No k<n=2 contributions in B_2 since j=1, k must satisfy j<k<n=2 — empty.]
    Row 2 (j=2=n):
      Each '2bar' in row 2 -> 2*beta_{2,2} = 2*e_2   (rule 3 with j=n=2)
      [No '0' contribution rule for row n explicitly stated, but a '0' is allowed.]
      Each '(2, 2bar)' pair -> not applicable; row 2 entries are all >= 2.

  We need to INVERT this map.

  Note Aug~ in Rick's setup involves multiplicities at the four roots
    (e_1 - e_2): beta_{1,1}
    (e_1 + e_2): gamma_{1,2}
    e_1:          beta_{1,2}  (short)
    e_2:          beta_{2,2}  (short)

CST's Definition 2.14 of f_i, e_i on Kp(infty) uses bracketing sequences
S_i^B over a SPECIFIC sequence Phi_i^B of roots.  But for the verification
we can equivalently:
  1. Compute T = Psi^{-1}(pi) (marginally-large tableau).
  2. Read off the i-signature string br_i(T) using CST Def 2.6/2.7 boxes-that-act
     rules:
        For each box in T (read in a specific order — column-by-column, top-to-bottom,
        right-to-left, which is the standard B(infty) reading):
          '(' if f_i would act on that box (box becomes a higher letter)
          ')' if e_i would act on that box (box becomes a lower letter)
          '.' otherwise.
     Then cancel adjacent ')(' pairs to get br_i^c(T).
  3. f_i acts on the leftmost UNCANCELED '(' box; e_i on the rightmost UNCANCELED ')'.

To avoid implementing the full Kashiwara reading order from scratch, we use the
"single-box action" rule: in a marginally-large B(infty) tableau, f_i changes one
box ENTRY by a single +1 step in the alphabet (with column-insertion at the
shaded boundary).  For type B with i=2 (alpha_2 = e_2, the short root), f_2
turns 2 -> 0, 0 -> 2bar, etc. — see Kashiwara-Nakashima for the precise table.

We'll just hand-compute for the specific example.
"""

# Alphabet positions for B_2
ALPH = ['1', '2', '0', '2bar', '1bar']
POS = {a: i for i, a in enumerate(ALPH)}


def psi_row(j, row, n=2):
    """Given row contents (excluding the shaded leftmost (row-length-of-(j+1)+1) copies of 'j'),
    return the contribution to the Kostant partition.

    Wait — the shaded boxes ALSO can carry weight if they're "unshaded shifted",
    but per CST Def 2.4 weight is supported on UNSHADED part.  We pass only the
    unshaded part of row j.

    Returns a dict (root_tuple) -> coefficient.
    """
    if n != 2:
        raise NotImplementedError("only n=2 implemented")

    result = {}

    def add(root, k=1):
        result[root] = result.get(root, 0) + k

    # Tally entries
    from collections import Counter
    cnt = Counter(row)

    if j == 1:
        # Row 1: entries can be in {1, 2, 0, 2bar, 1bar}.  Unshaded means entries beyond
        # the shaded '1's.  We assume row passed in is already unshaded; allowed entries:
        #   2, 0, 2bar, 1bar (and maybe extra 1's only in shaded but we pass unshaded part).
        # Pair (2, 2bar): rule 1, contributes 2*beta_{1,2} = 2*e_1.
        n_pair_22bar = min(cnt['2'], cnt['2bar'])
        for _ in range(n_pair_22bar):
            add((1, 0), 2)
        cnt['2'] -= n_pair_22bar
        cnt['2bar'] -= n_pair_22bar

        # Single 0: rule 2, beta_{1,2} = e_1.
        for _ in range(cnt.get('0', 0)):
            add((1, 0), 1)

        # Unpaired 2: rule 8 with k=2 -> beta_{1, 2-1} = beta_{1,1} = e_1 - e_2.
        for _ in range(cnt['2']):
            add((1, -1), 1)

        # Unpaired 2bar: rule 9 with k=2 -> gamma_{1,2} = e_1 + e_2.
        for _ in range(cnt['2bar']):
            add((1, 1), 1)

        # Unpaired 1bar: rule 6, single jbar in own row: (beta_{1,1}) + (gamma_{1,2}).
        # For j=1, single 1bar: contributes beta_{1,1} + gamma_{1,2}.
        for _ in range(cnt.get('1bar', 0)):
            add((1, -1), 1)
            add((1, 1), 1)

    elif j == 2:
        # Row 2: entries can be in {2, 0, 2bar} (since must be >= 2 and <= 2bar).
        # Each 2bar in row 2: rule 3, 2*beta_{2,2} = 2*e_2.
        for _ in range(cnt.get('2bar', 0)):
            add((0, 1), 2)
        # Each 0 in row 2: not explicit in CST B_n rules quoted in the extraction note,
        # but by symmetry with rule 2, a single 0 in row j contributes beta_{j,n}.
        # For j=2=n, that's beta_{2,2} = e_2.
        for _ in range(cnt.get('0', 0)):
            add((0, 1), 1)
    else:
        raise ValueError(f"j={j} out of range for B_2")

    return result


def psi_tableau(rows, n=2):
    """rows: dict {j: list of entries in row j (excluding shaded)}.
       Or: full rows including shaded; we pass the FULL row content."""
    # The "unshaded" part of row j is everything after the shaded leftmost j's,
    # where the shaded count is (length of row j+1) + 1, or 1 if j=n.
    result = {}
    row_lengths = {j: len(r) for j, r in rows.items()}

    for j in sorted(rows.keys()):
        full_row = rows[j]
        # Compute shaded count: row j must start with at least
        #   (len(row j+1) if j+1 in rows else 0) + 1
        # copies of 'j' (entry indexed at row j).  Entries in J: 1,2,0,2bar,1bar; here
        # 'j'-letter is str(j).
        next_len = row_lengths.get(j + 1, 0)
        shaded_count = next_len + 1
        # Check
        for k in range(shaded_count):
            if k >= len(full_row) or full_row[k] != str(j):
                raise ValueError(f"Row {j} not marginally large: needs {shaded_count} shaded '{j}'s, got {full_row[:shaded_count]}")
        unshaded = full_row[shaded_count:]
        contrib = psi_row(j, unshaded, n=n)
        for root, c in contrib.items():
            result[root] = result.get(root, 0) + c
    return result


# ====== INVERSE Psi (by direct case analysis for small B_2 partitions) ======

def psi_inverse_b2(pi):
    """Given a B_2 Kostant partition pi (dict root -> count),
    construct the marginally-large tableau as rows dict.

    Strategy: greedy decomposition using Psi rules.  This is essentially
    Theorem 3.1 read backwards.  For each root contribution we assign
    boxes to the appropriate row.

    Roots in B_2:
      (1, -1) = e_1 - e_2 = beta_{1,1}: row 1 unpaired '2' (rule 8) OR row 1 has
                lone '1bar' contributing (beta_{1,1}, gamma_{1,2}) together.
      (1, 1)  = e_1 + e_2 = gamma_{1,2}: row 1 unpaired '2bar' (rule 9) OR pairs
                in a lone 1bar (with beta_{1,1}).
      (1, 0)  = e_1 = beta_{1,2}:
                - Row 1 pair (2, 2bar): contributes 2*e_1 (rule 1).
                - Row 1 single '0' (rule 2): contributes e_1.
      (0, 1)  = e_2 = beta_{2,2}:
                - Row 2 entry '2bar' contributes 2*e_2 (rule 3).
                - Row 2 entry '0' contributes e_2 (by symmetry/general rule).

    Choices: there's ambiguity in which "rule" produced each contribution.
    For MARGINALLY LARGE tableaux Psi is a BIJECTION (Theorem 3.1).  So
    given pi, there's a UNIQUE tableau.

    The unique decomposition for small cases is dictated by marginal largeness:
    we need to add a 'shaded' leftmost block to each row.  Specifically the
    SHORTEST consistent tableau is what marginally-large enforces.

    Decomposition algorithm:
      Step 1: Determine the row 2 content from (e_2)-multiplicity.
        Let m_short_2 = pi.get((0, 1), 0).
        We split m_short_2 as 2*n_2bar + n_0 with n_2bar, n_0 >= 0.
        Marginally-large for row 2: row 2 = ['2'] * (1) + [2bar's] * n_2bar + ['0'] * n_0
        — actually, all '2's first, then '0's, then '2bar's by semistandard order.
        But to make pi(e_2) match exactly, we need a CANONICAL choice.
        Convention: prefer '2bar' over '0' for compactness (and since '0' uses up
        e_1 quota too if in row 1...). Actually in row 2, '0' contributes only e_2
        not e_1, so it's just a different way to spend e_2 quota.

        Actually the issue: marginally large tableaux have a UNIQUE form for each pi.
        The bijection Psi is well-defined.  But the INVERSE requires breaking the
        choice between (n_2bar copies of '2bar') vs (n_0 copies of '0') at row 2.

        Hmm — let's go to CST stack notation (§4 of extraction note).  Each positive
        root corresponds to a "stack" (column).  Marginal largeness just says you
        also fill in shaded boxes (the boundary "frame").  The fiber of Psi over pi
        IS a single tableau because the stacking RULES determine the shape uniquely.

      For our specific test case, we just need ONE example.  Let me hand-compute.

    For the specific test:
        pi = {(1, -1): 1, (1, 1): 2}  =  1*beta_{1,1} + 2*gamma_{1,2}
        pi(e_2) = 0, so row 2 has only the shaded boxes (length 1: just one '2').
        Wait — but row 2 length = pi(e_2)/2 contributions + ... let me re-derive.

        Row 2 length = 1 (shaded) + 0 (unshaded — no contribution to pi(e_2)).
        Hmm but we have contributions from gamma_{1,2}: rule 9 says unpaired '2bar' in
        row 1 (with k=2) -> gamma_{1,2}.

        Row 1 content:
          shaded: len(row 2) + 1 = 1 + 1 = 2 copies of '1'.
          unshaded: contributions for pi(beta_{1,1})=1, pi(gamma_{1,2})=2, pi(beta_{1,2})=0.
            - beta_{1,1}=1: rule 8 unpaired '2' -> 1 unpaired '2'.
            - gamma_{1,2}=2: rule 9 unpaired '2bar' -> 2 unpaired '2bar'.
            - beta_{1,2}=0: no '0', no (2,2bar) pair, no extra '2' or '2bar' for pairing.
          So unshaded part = ['2', '2bar', '2bar'].

        Full T:
          Row 1: 1 1 2 2bar 2bar
          Row 2: 2
        Verify semistandard: rows weakly increasing (1<=1<=2<=2bar<=2bar OK; row 2: 2 alone OK).
        Verify marginal largeness: row 1 has (1+1=2) leading '1's, row 2 has (0+1=1) leading '2'. OK.

    So T = Psi^{-1}(pi) is straightforward in this case.
    """
    pi = dict(pi)
    n_beta_11 = pi.get((1, -1), 0)  # e_1 - e_2
    n_gamma_12 = pi.get((1, 1), 0)   # e_1 + e_2
    n_beta_12 = pi.get((1, 0), 0)    # e_1 (short)
    n_beta_22 = pi.get((0, 1), 0)    # e_2 (short)

    # ===== Row 2 =====
    # pi(e_2) = 2*n_2bar_row2 + n_0_row2 (from rule 3 + rule for '0' in row 2).
    # CANONICAL CHOICE: use as many '2bar's as possible (= 2-pair count).
    # If pi(e_2) is even: all '2bar's, no '0'.
    # If pi(e_2) is odd: one '0', rest split into '2bar's. BUT! Row 2 can only have
    # at most ONE '0' (B_n rule: 0 appears at most once per row).
    # If pi(e_2) is odd and > 1: one '0' + (pi(e_2)-1)/2 '2bar's.

    # For our test case pi(e_2)=0, so no extra entries in row 2.

    if n_beta_22 % 2 == 0:
        row2_n0 = 0
        row2_n2bar = n_beta_22 // 2
    else:
        row2_n0 = 1
        row2_n2bar = (n_beta_22 - 1) // 2

    # ===== Row 1 =====
    # pi(beta_{1,2}) = pi(e_1) = 2*n_pair_22bar + n_0 (from rules 1 + 2).
    # Canonical: max pairs first, leftover -> single '0'.
    # Rule: 0 at most once per row.
    if n_beta_12 % 2 == 0:
        row1_n0 = 0
        row1_npair_22bar = n_beta_12 // 2
    else:
        row1_n0 = 1
        row1_npair_22bar = (n_beta_12 - 1) // 2

    # pi(beta_{1,1}) = pi(e_1 - e_2) = #(unpaired '2' in row 1) + #(unpaired '1bar' in row 1)
    # pi(gamma_{1,2}) = pi(e_1 + e_2) = #(unpaired '2bar' in row 1) + #(unpaired '1bar' in row 1)
    # Rule 6: lone '1bar' contributes (beta_{1,1}) + (gamma_{1,2}) together.
    # Canonical: prefer rule 8/9 (separate '2' and '2bar') over rule 6 ('1bar's).
    # I.e., use NO '1bar's in row 1 if possible.

    # CRITICAL: the pair-matching rule pairs each '2' with the EARLIEST '2bar' in the
    # row. So if we have both unpaired '2's AND '2bar's in the same row, they will
    # get matched and produce 2*beta_{1,2} contributions, not separate ones.
    #
    # In semistandard order [2,2,...,0?,2bar,2bar,...,1bar,...], a '2' followed by a
    # '2bar' is matched. So you CANNOT have both unpaired '2' and unpaired '2bar' in
    # the same row.
    #
    # Resolution: when both beta_{1,1} and gamma_{1,2} are positive, you MUST use '1bar's
    # to encode the combined contribution (beta_{1,1} + gamma_{1,2}) per rule 6.
    # The minimum number of '1bar's is min(beta_{1,1}, gamma_{1,2}).

    n_1bar = min(n_beta_11, n_gamma_12)
    row1_n1bar = n_1bar
    row1_n2_unpaired = n_beta_11 - n_1bar  # only if gamma_{1,2} = 0
    row1_n2bar_unpaired = n_gamma_12 - n_1bar  # only if beta_{1,1} = 0

    # Total row 1 boxes
    row1_n2 = row1_n2_unpaired + row1_npair_22bar
    row1_n2bar = row1_n2bar_unpaired + row1_npair_22bar
    row1_total_unshaded = row1_n2 + row1_n0 + row1_n2bar + row1_n1bar

    # ===== Row 2 shaded =====
    # Row 2 shaded count = 1 (since no row 3).
    row2_total = 1 + row2_n2bar + row2_n0
    # Row 1 shaded count = len(row 2) + 1.
    row1_shaded = row2_total + 1

    # Build rows in semistandard order: 1's, then 2's, then 0, then 2bar's, then 1bar's.
    row1 = ['1'] * row1_shaded + ['2'] * row1_n2
    if row1_n0:
        row1.append('0')
    row1 += ['2bar'] * row1_n2bar
    row1 += ['1bar'] * row1_n1bar

    row2 = ['2'] * 1 + (['0'] if row2_n0 else [])
    row2 += ['2bar'] * row2_n2bar

    return {1: row1, 2: row2}


def print_tableau(rows):
    for j in sorted(rows):
        print(f"  Row {j}: {' '.join(rows[j])}")


# ====== Test ======

if __name__ == "__main__":
    print("=== Test 1: pi = {beta_{1,1}: 1, gamma_{1,2}: 2} ===")
    pi = {(1, -1): 1, (1, 1): 2}
    T = psi_inverse_b2(pi)
    print(f"pi = {pi}")
    print("T = Psi^{-1}(pi):")
    print_tableau(T)

    # Round-trip verify
    pi_back = psi_tableau(T)
    print(f"Psi(T) = {pi_back}")
    assert pi_back == pi, f"Round-trip failed: {pi} vs {pi_back}"
    print("  -> Round-trip OK")

    print("\n=== Test 2: pi = {beta_{1,1}: 2, gamma_{1,2}: 1} ===")
    pi2 = {(1, -1): 2, (1, 1): 1}
    T2 = psi_inverse_b2(pi2)
    print(f"pi' = {pi2}")
    print("T' = Psi^{-1}(pi'):")
    print_tableau(T2)
    pi2_back = psi_tableau(T2)
    print(f"Psi(T') = {pi2_back}")
    assert pi2_back == pi2
    print("  -> Round-trip OK")
