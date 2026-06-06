"""
Analyze the support of M: F -> F' and classify by net-move type.

Two main classifications to try:
  (1) Net difference d = (a'_1 - a_1, a'_2 - a_2, a'_3 - a_3, a'_4 - a_4).
      How many distinct d-vectors arise in the support?
  (2) Pattern (a) <-> (a') with leading bijection sigma stripped out.
      For each F'-vector, identify the "leading" F-vector (largest coef in some
      ordering) and consider the "corrections" as moves.

  (3) For each F'-vector a', the support entries form a "move profile":
      one main (leading) plus corrections.
"""

import json
from collections import defaultdict, Counter
from fractions import Fraction
import os

HERE = os.path.dirname(__file__)
with open(os.path.join(HERE, 'M_matrix.json')) as f:
    data = json.load(f)

F = [tuple(a) for a in data['F_admissible']]
Fp = [tuple(a) for a in data['Fp_admissible']]
M = {}
for entry in data['M_entries']:
    M[(tuple(entry['a_prime']), tuple(entry['a']))] = Fraction(entry['coef'])

print(f"|F| = {len(F)}, |F'| = {len(Fp)}, |support of M| = {len(M)}")

# ---------------------------------------------------------------------
# Classification (1): difference d = a' - a
# ---------------------------------------------------------------------

deltas = []
for (ap, a), coef in M.items():
    d = tuple(ap[i] - a[i] for i in range(4))
    deltas.append((d, ap, a, coef))

delta_counter = Counter(d for d, _, _, _ in deltas)
print(f"\nClassification 1: distinct delta = a' - a")
print(f"Number of distinct delta vectors: {len(delta_counter)}")
for d, count in sorted(delta_counter.items(), key=lambda x: (-x[1], x[0])):
    print(f"  {d}: {count} entries")

# ---------------------------------------------------------------------
# Classification (2): partition by F'-row -> identify leading & corrections
# ---------------------------------------------------------------------

# Group entries by a'
by_ap = defaultdict(list)
for (ap, a), coef in M.items():
    by_ap[ap].append((a, coef))

print(f"\n=== F'-row breakdown ===")
print(f"F'-vectors total: {len(by_ap)}")

n_single = 0
n_multi = 0
for ap, entries in by_ap.items():
    if len(entries) == 1:
        n_single += 1
    else:
        n_multi += 1
print(f"Single-entry F' rows: {n_single}")
print(f"Multi-entry F' rows: {n_multi}")

print(f"\nMulti-entry F' rows in detail:")
for ap in sorted(by_ap):
    entries = by_ap[ap]
    if len(entries) > 1:
        print(f"  a' = {ap}  weight (n1, n2) = ({ap[0] + ap[2]}, {ap[1] + ap[3]}):")
        for a, c in sorted(entries):
            d = tuple(ap[i] - a[i] for i in range(4))
            print(f"    <- a = {a}  delta = {d}  coef = {c}")


# ---------------------------------------------------------------------
# Classification (3): try defining a "leading" F-vector for each a'
# ---------------------------------------------------------------------
# Possible rule: maximize a_4 (i.e., longest f_1^{a_4} prefix) among support
# entries, since the F'-word "starts" with f_2^{a'_4}.

print(f"\n=== Per-row analysis: choose 'leading' a via various rules ===")
def pick_leading(entries, rule='max_a4'):
    """Pick the leading F-vector among (a, coef) entries."""
    if rule == 'max_a4':
        return max(entries, key=lambda x: (x[0][3], x[0][2], x[0][1], x[0][0]))
    if rule == 'min_a1':
        return min(entries, key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3]))
    if rule == 'coef_1':
        ones = [x for x in entries if x[1] == 1]
        if len(ones) == 1:
            return ones[0]
        return None  # ambiguous

# Try 'coef_1' rule: pick the unique entry with coef 1, if it exists
print("\nRule: pick the unique entry with coef 1")
sigma_coef1 = {}
n_resolved = 0
for ap, entries in by_ap.items():
    ones = [x for x in entries if x[1] == 1]
    if len(ones) == 1:
        sigma_coef1[ap] = ones[0][0]
        n_resolved += 1
    elif len(ones) == 0:
        sigma_coef1[ap] = None
    else:
        sigma_coef1[ap] = 'multiple'
print(f"  Resolved (unique coef-1): {n_resolved}/{len(by_ap)} = {n_resolved}/40")
ambig = [ap for ap, s in sigma_coef1.items() if s == 'multiple']
none = [ap for ap, s in sigma_coef1.items() if s is None]
print(f"  Ambiguous (>1 entry with coef 1): {ambig}")
print(f"  No coef-1 entry: {none}")


# ---------------------------------------------------------------------
# Classification (4): look at delta = a' - a but group entries together
# in the leading + corrections structure
# ---------------------------------------------------------------------

print(f"\n=== Per-row delta profiles ===")
profile_counter = Counter()
for ap in sorted(by_ap):
    entries = by_ap[ap]
    deltas_row = sorted([(tuple(ap[i] - a[i] for i in range(4)), c) for a, c in entries])
    # The "delta profile" is the multiset of deltas (ignoring coefs for now)
    profile = tuple(d for d, _ in deltas_row)
    profile_counter[profile] += 1

print(f"Distinct delta-profiles: {len(profile_counter)}")
for profile, count in sorted(profile_counter.items(), key=lambda x: (len(x[0]), x[0])):
    print(f"  {profile}: {count} F'-rows")


# ---------------------------------------------------------------------
# Classification (5): try classifying just OFF-LEADING deltas
# (where leading = the entry with coef 1, or min a_1, etc.)
# ---------------------------------------------------------------------

print(f"\n=== Off-leading delta analysis (rule: largest a_1 = leading) ===")
# Conjecture: the "leading" entry is the one with the LARGEST a_1 (i.e.,
# the F-vector with the most f_2's applied first), since the F'-vector
# starts with f_2's.

# Actually let me try: pick the F-vector whose F-word, after canonical
# straightening, gives the largest leading PBW term. This might be the
# one with smallest a_4 (since a_4 is the outermost f_1, and we want to
# minimize the "f_1 first" which is canonical for F'-form).

# Try: pick leading by "min a_4", since F' starts with f_2.
print("\nRule: leading = entry with min a_4 (then min a_2, etc.)")
leading_assignment = {}
for ap, entries in by_ap.items():
    sorted_entries = sorted(entries, key=lambda x: (x[0][3], x[0][2], x[0][1], x[0][0]))
    leading_assignment[ap] = sorted_entries[0][0]

# Check: how many leading deltas (ap - leading_a) are zero?
n_zero_delta_lead = 0
for ap, a in leading_assignment.items():
    if all(ap[i] - a[i] == 0 for i in range(4)):
        n_zero_delta_lead += 1
print(f"  Leading entries with delta = 0: {n_zero_delta_lead}/40")

# What ARE the leading deltas?
lead_delta_counter = Counter()
for ap, a in leading_assignment.items():
    lead_delta_counter[tuple(ap[i] - a[i] for i in range(4))] += 1
print(f"  Distinct leading deltas: {len(lead_delta_counter)}")
for d, count in sorted(lead_delta_counter.items(), key=lambda x: -x[1]):
    print(f"    {d}: {count}")
