"""Day 85 — cross-join M_j table against Kostka bank.

For each (a, b, c, j), find all mu partitions in our small class with
K_{(a,b,c), mu} = M_j(a, b, c). Report:
- Number of matching mu per (a, b, j).
- Consistent mu patterns across (a, b) sweep.
- If NO Kostka match exists, print M_j / f^{(a,b,c)} — that's the multiplier
  feeding PROVE Step P4.
"""
import csv
import ast
import os
from collections import defaultdict
from math import factorial, gcd


MJ_CSV = '/home/agent/projects/code/2026-07-09-Mj-harvest/Mj_c5.csv'
KOSTKA_CSV = '/home/agent/projects/code/2026-07-09-Mj-harvest/Kostka_bank_c5.csv'
REPORT_MD = '/home/agent/projects/code/2026-07-09-Mj-Kostka-match.md'


def load_mj():
    """Return {(a, b, c) -> {j -> M_j}}."""
    table = {}
    with open(MJ_CSV) as fh:
        r = csv.DictReader(fh)
        for row in r:
            key = (int(row['a']), int(row['b']), int(row['c']))
            j_map = {}
            for j in range(9):
                v = row[f'M_{j}']
                j_map[j] = int(v) if v not in ('', 'None') else None
            j_map['f_lambda'] = int(row['f_lambda'])
            table[key] = j_map
    return table


def load_kostka():
    """Return {(a, b, c) -> [(class, mu, K)]}."""
    table = defaultdict(list)
    with open(KOSTKA_CSV) as fh:
        r = csv.DictReader(fh)
        for row in r:
            key = (int(row['a']), int(row['b']), int(row['c']))
            mu = ast.literal_eval(row['mu'])
            table[key].append((row['class'], mu, int(row['K_lam_mu'])))
    return dict(table)


def find_matches(mj, kostka):
    """For each (a, b, c) and each j, list all mu with K = M_j."""
    matches = defaultdict(list)  # (a, b, c, j) -> [(class, mu, K)]
    for key, j_map in mj.items():
        if key not in kostka:
            continue
        kentries = kostka[key]
        for j in range(9):
            m = j_map.get(j)
            if m is None:
                continue
            for cls, mu, kval in kentries:
                if kval == m:
                    matches[(*key, j)].append((cls, mu, kval))
    return matches


def summarize_by_j(matches, mj, kostka):
    """Print, per j, how many (a, b) had at least one Kostka match and which mu patterns."""
    by_j = defaultdict(list)  # j -> [(a, b, matches_list)]
    for (a, b, c, j), lst in matches.items():
        by_j[j].append(((a, b), lst))
    return dict(by_j)


def find_ratio_when_no_match(mj):
    """For (a, b, j) with M_j non-zero and no Kostka match, print M_j / f^lambda."""
    ratios = defaultdict(list)  # j -> [((a, b), ratio_num, ratio_den)]
    for key, j_map in mj.items():
        a, b, c = key
        f_lam = j_map['f_lambda']
        if f_lam == 0:
            continue
        for j in range(9):
            m = j_map.get(j)
            if m is None:
                continue
            g = gcd(abs(m), f_lam)
            ratios[j].append(((a, b), m // g if g else m, f_lam // g if g else f_lam))
    return dict(ratios)


def mu_pattern(a, b, c, mu):
    """Try to describe mu in terms of (a, b, c). Returns a short label if it matches
    a recognised template, else None."""
    N = a + b + c
    if not mu:
        return None
    mu_t = tuple(mu)
    # (N,) — trivial
    if mu_t == (N,):
        return "(N)"
    # (1^N)
    if all(x == 1 for x in mu_t):
        return "(1^N)"
    # (a, b, c) = lambda itself
    if mu_t == (a, b, c):
        return "lambda"
    # Column-strict (N - k, 1^k)
    if len(mu_t) >= 2 and all(x == 1 for x in mu_t[1:]):
        k = len(mu_t) - 1
        return f"(N-{k}, 1^{k})"
    # Two-part (N - k, k)
    if len(mu_t) == 2:
        return f"(N-{mu_t[1]}, {mu_t[1]})"
    # Hook A (N - 2j, 2^j)
    if len(mu_t) >= 2 and all(x == 2 for x in mu_t[1:]):
        j = len(mu_t) - 1
        return f"(N-2*{j}, 2^{j})"
    # Hook B (N - 2j, 1^{2j})
    if all(x == 1 for x in mu_t[1:]):
        twoj = len(mu_t) - 1
        return f"(N-{twoj}, 1^{twoj})"
    return f"custom {mu_t}"


def main():
    mj = load_mj()
    kostka = load_kostka()
    matches = find_matches(mj, kostka)
    by_j = summarize_by_j(matches, mj, kostka)
    ratios = find_ratio_when_no_match(mj)

    lines = []
    lines.append("# Day 85 — M_j ↔ Kostka match report (c = 5)\n")
    lines.append("Cross-join of `Mj_c5.csv` and `Kostka_bank_c5.csv`.")
    lines.append("For each (a, b, j), lists all μ in our small class with K_{(a,b,5),μ} = M_j(a,b,5).\n")

    for j in range(9):
        lines.append(f"\n## j = {j}\n")

        # Count how many (a, b) had a match at this j.
        entries = by_j.get(j, [])
        entries.sort()
        n_ab_total = sum(1 for k, v in mj.items() if v.get(j) is not None)
        n_ab_matched = len(entries)
        lines.append(f"Match count: **{n_ab_matched} / {n_ab_total}** (a, b) shapes had ≥1 μ match.\n")

        # Find the most common μ pattern.
        pattern_counts = defaultdict(int)
        for (a, b), lst in entries:
            for cls, mu, kval in lst:
                pat = mu_pattern(a, b, 5, mu)
                pattern_counts[pat] += 1
        if pattern_counts:
            lines.append("### μ patterns (occurrences across (a, b)):\n")
            for pat, cnt in sorted(pattern_counts.items(), key=lambda kv: -kv[1])[:20]:
                lines.append(f"- `{pat}` — {cnt} matches")

        # Show a few (a, b) examples with their matches.
        lines.append("\n### Sample matches (first 8 (a, b) with matches):\n")
        for (a, b), lst in entries[:8]:
            m_val = mj[(a, b, 5)][j]
            lines.append(f"- (a,b) = ({a},{b}), M_{j} = {m_val}:")
            for cls, mu, kval in lst[:4]:
                lines.append(f"    - K_{{(a,b,5), {mu}}} = {kval} [{cls}]")
            if len(lst) > 4:
                lines.append(f"    - ... and {len(lst) - 4} more")

        # Where NO match: print M_j / f^lambda ratio, look for constancy.
        no_match_ratios = []
        for key, j_map in mj.items():
            a, b, c = key
            if (a, b, 5, j) in matches:
                continue
            m = j_map.get(j)
            if m is None or m == 0:
                continue
            f_lam = j_map['f_lambda']
            if f_lam == 0:
                continue
            g = gcd(abs(m), f_lam)
            no_match_ratios.append(((a, b), m // g, f_lam // g, m, f_lam))
        if no_match_ratios:
            lines.append(f"\n### No-match (a, b): M_{j} / f^λ ratios ({len(no_match_ratios)} shapes)\n")
            # Group by (num, den) ratio.
            ratio_groups = defaultdict(list)
            for (a, b), num, den, m_raw, f_raw in no_match_ratios:
                ratio_groups[(num, den)].append((a, b))
            for (num, den), abs_list in sorted(ratio_groups.items(), key=lambda kv: -len(kv[1]))[:8]:
                lines.append(f"- ratio = {num}/{den} at {len(abs_list)} shapes: {abs_list[:6]}{'...' if len(abs_list) > 6 else ''}")

    report = "\n".join(lines)
    with open(REPORT_MD, 'w') as fh:
        fh.write(report)
    print(f"Wrote report to {REPORT_MD}")
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    for j in range(9):
        n_ab_total = sum(1 for k, v in mj.items() if v.get(j) is not None)
        n_ab_matched = len(by_j.get(j, []))
        print(f"  j = {j}: {n_ab_matched}/{n_ab_total} (a, b) had ≥1 match")


if __name__ == '__main__':
    main()
