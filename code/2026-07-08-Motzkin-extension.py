"""Day 86 CODE Task 3 — Motzkin coefficient extension to j = 7..10.

Sum of K_{μ^T, (2^j)} over μ ⊢ 2j with <= 3 rows.

Day 85 observed the sequence 1, 1, 2, 4, 9, 21, 51 for j = 0..6. These are
the first Motzkin numbers (OEIS A001006).

This extends to j = 7..10 and confirms:
 (a) The sequence matches Motzkin (OEIS A001006): 1, 1, 2, 4, 9, 21, 51,
     127, 323, 835, 2188.
 (b) The Motzkin recurrence a_{j+1} = ((2j+3) a_j + 3j a_{j-1}) / (j+3).

The Motzkin identity comes from the FACT that summing K_{μ^T, (2^j)} over
μ ⊢ 2j with EXACTLY 3 rows in ν = μ^T (i.e., μ has parts <= 3, equivalently
ν has <= 3 columns... no, μ having ≤ 3 rows means μ^T has ≤ 3 columns).

Actually: μ has ≤ 3 rows iff μ^T has ≤ 3 columns. K_{μ^T, (2^j)} is the
number of SSYT of shape μ^T with content (2^j). Summing over all μ ⊢ 2j
with μ^T having ≤ 3 columns is the number of SSYT with content (2^j) and
shape a partition with ≤ 3 columns — equivalently, sequences 1,...,j of
values in {1, 2, 3} forming a lattice path... which is Motzkin.

Explanation:  ⟨e_2^j · 1, s_λ⟩ for λ with ≤ 3 rows tracks the number of
length-j Motzkin paths (up-step / horizontal-step / down-step).
"""
from collections import defaultdict


# ---------------------------------------------------------------------------
# Pieri: add vertical 2-strip.
# ---------------------------------------------------------------------------

def add_v2_strip(mu, max_rows=6):
    mu = list(mu) + [0] * max_rows
    out = []
    for i1 in range(max_rows):
        v1 = mu[:]
        v1[i1] += 1
        if i1 > 0 and v1[i1] > v1[i1 - 1]:
            continue
        for i2 in range(i1 + 1, max_rows):
            v2 = v1[:]
            v2[i2] += 1
            if v2[i2] > v2[i2 - 1]:
                continue
            out.append(tuple(x for x in v2 if x > 0))
    return out


def e2_power_kostka(j, max_rows_filter=None):
    """Full {mu: K_{mu^T, (2^j)}} table for mu ⊢ 2j (no row restriction
    unless max_rows_filter is set)."""
    current = defaultdict(int)
    current[tuple()] = 1
    for _ in range(j):
        nxt = defaultdict(int)
        for mu, k in current.items():
            for nu in add_v2_strip(mu, max_rows=j * 2 + 2):
                nxt[nu] += k
        current = nxt
    if max_rows_filter is not None:
        return {mu: k for mu, k in current.items() if len(mu) <= max_rows_filter}
    return dict(current)


# ---------------------------------------------------------------------------
# Compute the "3-row sum": total over mu ⊢ 2j with ≤ 3 parts.
# ---------------------------------------------------------------------------

def three_row_sum(j):
    table = e2_power_kostka(j, max_rows_filter=3)
    return sum(table.values())


# ---------------------------------------------------------------------------
# OEIS A001006 (Motzkin numbers).
# ---------------------------------------------------------------------------

MOTZKIN_OEIS = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188, 5798, 15511,
                41835, 113634, 310572, 853467, 2356779, 6536382, 18199284]


def motzkin_recurrence(seq):
    """Verify a_{j+1} = ((2j+3) a_j + 3j a_{j-1}) / (j+3)."""
    ok = True
    for j in range(1, len(seq) - 1):
        lhs = seq[j + 1]
        rhs_num = (2 * j + 3) * seq[j] + 3 * j * seq[j - 1]
        if rhs_num % (j + 3) != 0:
            return False, j, f"non-integer at j={j}"
        rhs = rhs_num // (j + 3)
        if lhs != rhs:
            ok = False
            return False, j, f"seq[{j+1}]={lhs} != {rhs}"
    return ok, None, "OK"


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    lines = []
    lines.append("=" * 72)
    lines.append("Day 86 CODE Task 3 — Motzkin extension to j = 7..10")
    lines.append("=" * 72)
    lines.append("")
    lines.append("For each j, sum_μ K_{μ^T, (2^j)} where μ ⊢ 2j, ≤ 3 rows.")
    lines.append("Prediction: Motzkin numbers (OEIS A001006).")
    lines.append("")
    lines.append(f"{'j':>3s} | {'3-row sum':>12s} | {'A001006':>10s} | match")
    lines.append("-" * 45)

    seq = []
    for j in range(0, 12):
        s = three_row_sum(j)
        seq.append(s)
        expected = MOTZKIN_OEIS[j]
        match = (s == expected)
        lines.append(f"{j:>3d} | {s:>12d} | {expected:>10d} | {match}")

    all_match = all(seq[j] == MOTZKIN_OEIS[j] for j in range(len(seq)))
    lines.append("")
    lines.append(f"Match against OEIS A001006 for j = 0..{len(seq)-1}: "
                 f"{'ALL MATCH' if all_match else 'MISMATCH'}")
    lines.append("")

    # Verify Motzkin recurrence.
    ok, jbad, msg = motzkin_recurrence(seq)
    lines.append("Motzkin recurrence a_{j+1} = ((2j+3) a_j + 3j a_{j-1}) / (j+3):")
    lines.append(f"  {'HOLDS' if ok else f'FAILS at j={jbad}: {msg}'}")
    lines.append("")

    # Extended μ decomposition table for j = 7..10 (nice for the paper).
    lines.append("=" * 72)
    lines.append("Detailed μ-Kostka table (μ ⊢ 2j, ≤ 3 rows) for j = 7..10")
    lines.append("=" * 72)
    for j in range(7, 11):
        table = e2_power_kostka(j, max_rows_filter=3)
        lines.append(f"\nj = {j}: total = {sum(table.values())}")
        for mu, k in sorted(table.items()):
            lines.append(f"    μ = {mu}, K_{{μ^T, (2^{j})}} = {k}")

    lines.append("")
    lines.append("Motzkin ✓" if all_match and ok else "Motzkin FAILED")
    out = "\n".join(lines)
    print(out)

    with open("/home/agent/projects/code/2026-07-08-Motzkin-extension.txt", "w") as f:
        f.write(out)
    print("\nWritten: /home/agent/projects/code/2026-07-08-Motzkin-extension.txt")


if __name__ == "__main__":
    main()
