"""
SU1 Phase A — F_4 at ALL four simples.

The original Phase A only tested s_3 in F_4 (mixed-unit short).  For the
type-uniform SU1 theorem, the v1 paper claims F_4 is empirically verified
at every simple via Phase A's REDUCED-multiset framework.

This script extends to s_1, s_2, s_3, s_4 in F_4.  Conventions follow
Bourbaki: simple roots
  alpha_1 = e_2 - e_3 (long)
  alpha_2 = e_3 - e_4 (long)
  alpha_3 = e_4       (short)
  alpha_4 = 1/2 (e_1 - e_2 - e_3 - e_4) (short)

Each simple s_i partitions Phi^+ \\ {alpha_i} into s_i-orbits.  Each non-fixed
orbit has cardinality 2.  Units(st) = |<beta, alpha_i^v>| in {1, 2}.

REDUCED uniqueness check at each simple.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fractions import Fraction
from collections import defaultdict, Counter
from itertools import product
import su1_phase_a_C3 as SU1


def f4_positive_roots():
    """24 positive roots."""
    roots = []
    F = Fraction
    # Long: e_i - e_j (i < j) and e_i + e_j (i < j)
    for i in range(4):
        for j in range(i + 1, 4):
            v = [F(0)] * 4; v[i] = F(1); v[j] = F(-1)
            roots.append((tuple(v), 'L'))
            v = [F(0)] * 4; v[i] = F(1); v[j] = F(1)
            roots.append((tuple(v), 'L'))
    # Short: e_i
    for i in range(4):
        v = [F(0)] * 4; v[i] = F(1)
        roots.append((tuple(v), 'S'))
    # Short: 1/2 (s1 e_1 + s2 e_2 + s3 e_3 + s4 e_4) with s1 = +1
    half = F(1, 2)
    for s2, s3, s4 in product([1, -1], repeat=3):
        v = (half, half * s2, half * s3, half * s4)
        roots.append((v, 'S'))
    return roots


def f4_simples():
    """Bourbaki simples for F_4."""
    F = Fraction
    return [
        ('L1', (F(0), F(1), F(-1), F(0))),   # alpha_1 = e_2 - e_3 (long)
        ('L2', (F(0), F(0), F(1), F(-1))),   # alpha_2 = e_3 - e_4 (long)
        ('S3', (F(0), F(0), F(0), F(1))),    # alpha_3 = e_4 (short)
        ('S4', (F(1, 2), F(-1, 2), F(-1, 2), F(-1, 2))),  # alpha_4 (short)
    ]


def inner(u, v):
    return sum(u[i] * v[i] for i in range(4))


def pairing(beta, alpha):
    n2 = inner(alpha, alpha)
    return 2 * inner(beta, alpha) / n2


def reflect(beta, alpha):
    p = pairing(beta, alpha)
    return tuple(beta[i] - p * alpha[i] for i in range(4))


def orbit_actions_at_simple(alpha):
    """For F_4 simple alpha, return list of (label, donor, receiver, units) for each
    orbit-swap (subtype, direction).
    """
    pos = [r for r, _ in f4_positive_roots()]
    pos_set = set(pos)
    actions = []
    seen = set()
    for beta in pos:
        if beta == alpha:
            continue
        p = pairing(beta, alpha)
        if p == 0:
            continue
        partner = reflect(beta, alpha)
        if partner not in pos_set:
            continue
        if p > 0:
            donor, recv = beta, partner
        else:
            donor, recv = partner, beta
        orbit_key = frozenset({beta, partner})
        if orbit_key in seen:
            continue
        seen.add(orbit_key)
        units = abs(p)
        st = ('orbit', tuple(sorted([beta, partner])))
        actions.append(((st, '+'), donor, recv, units))
        actions.append(((st, '-'), recv, donor, units))
    return actions


def freeze_pi(pi):
    return tuple(sorted(pi.items()))


def reduce_multiset(M):
    by_st = defaultdict(lambda: {'+': 0, '-': 0})
    for (st, sg), n in M.items():
        by_st[st][sg] += n
    out = {}
    for st, d in by_st.items():
        a, b = d['+'], d['-']
        if a > b:
            out[(st, '+')] = a - b
        elif b > a:
            out[(st, '-')] = b - a
    return out


def freeze_multiset(M):
    return tuple(sorted(M.items()))


def enumerate_orbit_swap_multisets(pi, c, actions):
    caps = [pi.get(d, 0) for _, d, _, _ in actions]
    results = []
    n_a = len(actions)

    def recurse(idx, remaining, partial):
        if idx == n_a:
            if remaining == 0:
                results.append(dict(partial))
            return
        lbl, _, _, u = actions[idx]
        signed = u if lbl[1] == '+' else -u
        for n in range(caps[idx] + 1):
            if n > 0:
                partial[lbl] = n
            recurse(idx + 1, remaining - n * signed, partial)
            if n > 0:
                del partial[lbl]

    recurse(0, c, {})
    return results


def apply_multiset(pi, M, actions):
    lookup = {lbl: (d, r) for lbl, d, r, _ in actions}
    new_pi = dict(pi)
    for lbl, n in M.items():
        d, r = lookup[lbl]
        new_pi[d] = new_pi.get(d, 0) - n
        if new_pi[d] == 0:
            del new_pi[d]
        new_pi[r] = new_pi.get(r, 0) + n
    return {x: v for x, v in new_pi.items() if v > 0}


def enumerate_pis(roots, max_total):
    out = []
    def recurse(idx, remaining, partial):
        if idx == len(roots):
            out.append(dict(partial))
            return
        for n in range(remaining + 1):
            if n > 0:
                partial[roots[idx]] = n
            recurse(idx + 1, remaining - n, partial)
            if n > 0:
                del partial[roots[idx]]
    recurse(0, max_total, {})
    return out


def phase_a_at_simple(simple_label, alpha, c_values, max_pi_total):
    actions = orbit_actions_at_simple(alpha)
    donor_roots = sorted(set(d for _, d, _, _ in actions), key=lambda v: tuple(float(x) for x in v))
    pis = enumerate_pis(donor_roots, max_pi_total)

    units_dist = Counter(u for _, _, _, u in actions)
    print(f"\n[{simple_label}] alpha = {alpha}")
    print(f"  # orbit actions: {len(actions)}, units distribution: {dict(units_dist)}")
    print(f"  # donor profiles enumerated: {len(pis)}")

    raw_total = raw_unique = raw_multi = 0
    red_total = red_unique = red_multi = 0

    for pi in pis:
        if sum(pi.values()) == 0:
            continue
        for c in c_values:
            ms = enumerate_orbit_swap_multisets(pi, c, actions)
            if not ms:
                continue
            end_states = defaultdict(list)
            for M in ms:
                epi = apply_multiset(pi, M, actions)
                end_states[freeze_pi(epi)].append(M)
            for k, lst in end_states.items():
                raw_total += 1
                if len(lst) == 1:
                    raw_unique += 1
                else:
                    raw_multi += 1
                red_set = set(freeze_multiset(reduce_multiset(M)) for M in lst)
                red_total += 1
                if len(red_set) == 1:
                    red_unique += 1
                else:
                    red_multi += 1

    print(f"  RAW: total={raw_total} unique={raw_unique} multi={raw_multi}")
    print(f"  REDUCED: total={red_total} unique={red_unique} multi={red_multi}")
    return red_multi == 0, raw_total, raw_unique, raw_multi, red_total, red_unique, red_multi


if __name__ == "__main__":
    print("="*70)
    print("F_4 Phase A at ALL four simples (REDUCED uniqueness check)")
    print("="*70)
    grand_raw = 0
    grand_red = 0
    grand_red_multi = 0
    for lbl, alpha in f4_simples():
        ok, _, _, _, rt, ru, rm = phase_a_at_simple(lbl, alpha, c_values=[1, 2, 3, -1, -2, -3], max_pi_total=3)
        grand_red += rt
        grand_red_multi += rm
    print()
    print("="*70)
    print(f"GRAND F_4 (s_1, s_2, s_3, s_4): REDUCED total={grand_red} multi={grand_red_multi}")
    print(f"  IH base case for F_4: {'OK' if grand_red_multi == 0 else 'FAILED'}")
    print("="*70)
