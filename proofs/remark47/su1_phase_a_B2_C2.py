"""
SU1 Phase A — IH base case verification at B_2 and C_2 in REDUCED form.

For the inductive proof (Phase C of the v0 draft), the IH at n=2 must hold
at both B_2 and C_2 in the *current* REDUCED-multiset / Kostant-basis
formulation.  This script confirms it.

B_2 and C_2 root systems (Bourbaki conventions):
  B_2: simple roots alpha_0 = e_0 - e_1 (long), alpha_1 = e_1 (short).
       Positive roots: e_0 - e_1, e_0 + e_1 (long), e_0, e_1 (short).
  C_2: simple roots alpha_0 = e_0 - e_1 (short), alpha_1 = 2 e_1 (long).
       Positive roots: e_0 - e_1, e_0 + e_1 (short), 2 e_0, 2 e_1 (long).

B_2 and C_2 are abstractly isomorphic as root systems (long/short swap), but
we treat them separately to match the SU1 framework's type-uniformity check.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from collections import defaultdict, Counter
from fractions import Fraction
from itertools import product

N = 2

# ============ C_2 root system ============

def c2_positive_roots():
    """Return list of (root, kind) for C_2 positive roots."""
    return [
        ((1, -1), 'S'),   # e_0 - e_1
        ((1,  1), 'S'),   # e_0 + e_1
        ((2,  0), 'L'),   # 2 e_0
        ((0,  2), 'L'),   # 2 e_1
    ]


def c2_subtypes_for_simple(kind, i):
    """Subtypes for simple (kind, i) at C_2."""
    if kind == 'S':
        # short exchange alpha_0 = e_0 - e_1: subtype LL only (since p < i = 0 empty, q > i+1 = 1 empty in N=2)
        return [('LL',)]
    elif kind == 'L':
        # long flip alpha_1 = 2 e_1: subtype (S, p) for p < N-1 = 0... wait p < 1 means p = 0.
        return [('S', 0)]


def c2_subtype_units(kind, i, st):
    if kind == 'S' and st[0] == 'LL':
        return 2
    if kind == 'L' and st[0] == 'S':
        return 1
    raise ValueError


def c2_subtype_donor_receiver(kind, i, st, c):
    """Per C_n convention.  c sign determines direction."""
    if kind == 'S':  # alpha_0 = e_0 - e_1
        # ('LL',): orbit {2 e_0, 2 e_1}, 2-unit
        if c > 0:
            return (2, 0), (0, 2)  # donor 2 e_0, receiver 2 e_1
        else:
            return (0, 2), (2, 0)
    elif kind == 'L':  # alpha_1 = 2 e_1
        p = st[1]
        # (S, p): orbit {e_p + e_1, e_p - e_1}, 1-unit
        # For c > 0: donor = e_p + e_1, receiver = e_p - e_1
        donor = (1, 1) if p == 0 else None  # only p=0 in N=2
        recv = (1, -1)
        if c > 0:
            return donor, recv
        else:
            return recv, donor


# ============ B_2 root system ============

def b2_positive_roots():
    """Return list of (root, kind) for B_2 positive roots."""
    return [
        ((1, -1), 'L'),   # e_0 - e_1 (long in B_2)
        ((1,  1), 'L'),   # e_0 + e_1 (long)
        ((1,  0), 'S'),   # e_0 (short)
        ((0,  1), 'S'),   # e_1 (short)
    ]


def b2_subtypes_for_simple(kind, i):
    """Subtypes for simple (kind, i) at B_2.

    B_2 simples: alpha_0 = e_0 - e_1 (LONG exchange), alpha_1 = e_1 (SHORT flip).

    In Bourbaki convention for B_n:
      ('L', i) for i = 0, ..., N-2: long EXCHANGE simples (swap e_i, e_{i+1}).
      ('S', N-1): short FLIP simple (negate e_{N-1}).

    For B_2:
      alpha_0 is long exchange: subtypes are analogous to C_n short exchange but with
        kind/sign roles reversed.  The orbit of 2 e_i goes to 2 e_{i+1} (but in B_n,
        2 e_i is NOT a root).  Hmm — B_n doesn't have 2 e_i roots.
      Let me redo.

    B_2 positive roots: {e_0 - e_1, e_0 + e_1, e_0, e_1}.

    Action of s_{alpha_0} = s_{e_0 - e_1} (swap coords 0, 1):
      e_0 - e_1 -> -(e_0 - e_1) (not in Phi^+ \ {alpha_0}; this is alpha_0 itself).
      e_0 + e_1 -> e_1 + e_0 = e_0 + e_1 (fixed).
      e_0 -> e_1.
      e_1 -> e_0.
      So orbits on Phi^+ \ {alpha_0} = {e_0 + e_1, e_0, e_1}:
        Singleton: {e_0 + e_1}.
        2-orbit: {e_0, e_1}.

    Action of s_{alpha_1} = s_{e_1} (negate coord 1):
      e_0 - e_1 -> e_0 + e_1, e_0 + e_1 -> e_0 - e_1.  2-orbit: {e_0 - e_1, e_0 + e_1}.
      e_0 -> e_0 (fixed).
      e_1 -> -e_1 (not in Phi^+ \ {alpha_1}; this is alpha_1 itself).
      So orbits on Phi^+ \ {alpha_1} = {e_0 - e_1, e_0 + e_1, e_0}:
        2-orbit: {e_0 - e_1, e_0 + e_1}.
        Singleton: {e_0}.

    Subtypes per simple:
      s_{alpha_0}: ONE 2-orbit subtype (call it 'b'): {e_0, e_1}, 1-unit (since pairing
                   <e_0, alpha_0^v> = 1 with alpha_0 long).
      s_{alpha_1}: ONE 2-orbit subtype: {e_0 - e_1, e_0 + e_1}, 2-unit (since alpha_1 is short and
                   pairing <e_0+e_1, alpha_1^v> = 2).

    Wait — pairings:
      <e_0, alpha_0^v>?  alpha_0 = e_0 - e_1 (long, alpha_0^v = alpha_0 since long), so
        <e_0, e_0 - e_1> = 1.  Units = 1.
      <e_1, alpha_0^v> = -1.  s_0(e_1) = e_1 + alpha_0 = e_0.  OK.
      <e_0 + e_1, alpha_1^v>?  alpha_1 = e_1 (short, alpha_1^v = 2 alpha_1 / |alpha_1|^2 = 2 e_1 / 1 = 2 e_1).
        <e_0+e_1, 2 e_1> = 2.  Units = 2.
      <e_0 - e_1, alpha_1^v> = -2.  s_1(e_0 - e_1) = (e_0 - e_1) + 2 e_1 = e_0 + e_1.  OK.

    So B_2 subtype structure:
      s_0 (long exchange):
        ONE 2-orbit subtype, 1-unit shift each: orbit {e_0, e_1}.  Call this ('B', 0) for "B-type, p=0".
        Actually there's NO matching analogue to C_n's LL since B_2 has no roots 2 e_i.  Different structure.

      s_1 (short flip):
        ONE 2-orbit subtype, 2-unit shift each: orbit {e_0 - e_1, e_0 + e_1}.  Call this ('LL',).

    Each simple has EXACTLY ONE non-trivial subtype.  REDUCED uniqueness is therefore TRIVIAL —
    each pi -> pi' transition uses a multiset with at most one (st, sign) key, fully determined
    by the Diophantine.
    """
    if kind == 'L':  # long exchange s_0
        return [('B', 0)]
    elif kind == 'S':  # short flip s_1
        return [('LL',)]


def b2_subtype_units(kind, i, st):
    if kind == 'L':  # long exchange has 1-unit orbit
        return 1
    elif kind == 'S':  # short flip has 2-unit orbit
        return 2


def b2_subtype_donor_receiver(kind, i, st, c):
    if kind == 'L':  # s_0 long exchange: orbit {e_0, e_1}, donor + = e_0 (high-pairing)
        # Pairing <e_0, alpha_0^v> = 1, so e_0 is high.  '+': donor e_0, receiver e_1.
        if c > 0:
            return (1, 0), (0, 1)
        else:
            return (0, 1), (1, 0)
    elif kind == 'S':  # s_1 short flip: orbit {e_0 - e_1, e_0 + e_1}, 2-unit
        # Pairing <e_0+e_1, alpha_1^v> = 2 > 0, so e_0+e_1 is high.  '+': donor e_0+e_1, receiver e_0-e_1.
        if c > 0:
            return (1, 1), (1, -1)
        else:
            return (1, -1), (1, 1)


# ============ Generic Phase A reduce/enumerate (copied/adapted from su1_phase_a_C3) ============

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


def freeze_pi(pi):
    return tuple(sorted(pi.items()))


def enumerate_orbit_swap_multisets(pi, c, subtype_units, subtype_donor_receiver_fn, subtypes):
    """Generic enumerator: returns list of multisets {(st, sign): count} with given Diophantine."""
    actions = []
    for st in subtypes:
        u = subtype_units(st)
        d_p, r_p = subtype_donor_receiver_fn(st, +1)
        d_m, r_m = subtype_donor_receiver_fn(st, -1)
        actions.append(((st, '+'), d_p, r_p, u))
        actions.append(((st, '-'), d_m, r_m, u))
    caps = [pi.get(d, 0) for _, d, _, _ in actions]
    results = []
    n_a = len(actions)

    def recurse(idx, remaining, partial):
        if idx == n_a:
            if remaining == 0:
                results.append(dict(partial))
            return
        lbl, _, _, u = actions[idx]
        sign = lbl[1]
        signed = u if sign == '+' else -u
        for n in range(caps[idx] + 1):
            if n > 0:
                partial[lbl] = n
            recurse(idx + 1, remaining - n * signed, partial)
            if n > 0:
                del partial[lbl]

    recurse(0, c, {})
    return results


def apply_multiset(pi, M, subtype_donor_receiver_fn):
    """Apply multiset, looking up donor/receiver per (st, sign)."""
    new_pi = dict(pi)
    for (st, sg), n in M.items():
        c = +1 if sg == '+' else -1
        donor, recv = subtype_donor_receiver_fn(st, c)
        new_pi[donor] = new_pi.get(donor, 0) - n
        if new_pi[donor] == 0:
            del new_pi[donor]
        new_pi[recv] = new_pi.get(recv, 0) + n
    return {r: m for r, m in new_pi.items() if m > 0}


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


def phase_a_check(name, simples, subtype_units_fn, subtype_dr_fn, subtypes_fn,
                  donor_roots, c_values, max_pi_total):
    """Run Phase A at a single rank-2 root system."""
    print(f"\n{'='*70}")
    print(f"Phase A: {name}")
    print(f"{'='*70}")
    print(f"  c in {c_values}, |pi| <= {max_pi_total}")
    print()

    grand_raw_total = 0
    grand_raw_unique = 0
    grand_raw_multi = 0
    grand_red_total = 0
    grand_red_unique = 0
    grand_red_multi = 0

    for kind, i in simples:
        subtypes = subtypes_fn(kind, i)
        roots_for_simple = donor_roots(kind, i)
        pis = enumerate_pis(roots_for_simple, max_pi_total)

        def sr_units(st): return subtype_units_fn(kind, i, st)
        def sr_dr(st, c): return subtype_dr_fn(kind, i, st, c)

        per_raw_total = 0
        per_raw_unique = 0
        per_raw_multi = 0
        per_red_total = 0
        per_red_unique = 0
        per_red_multi = 0

        for pi in pis:
            if sum(pi.values()) == 0:
                continue
            for c in c_values:
                multisets = enumerate_orbit_swap_multisets(pi, c, sr_units, sr_dr, subtypes)
                if not multisets:
                    continue
                end_states = defaultdict(list)
                for M in multisets:
                    epi = apply_multiset(pi, M, sr_dr)
                    end_states[freeze_pi(epi)].append(M)
                for k, ms_list in end_states.items():
                    per_raw_total += 1
                    if len(ms_list) == 1:
                        per_raw_unique += 1
                    else:
                        per_raw_multi += 1
                    reduced_set = set(freeze_multiset(reduce_multiset(M)) for M in ms_list)
                    per_red_total += 1
                    if len(reduced_set) == 1:
                        per_red_unique += 1
                    else:
                        per_red_multi += 1

        print(f"  simple ({kind}, {i}): RAW total={per_raw_total} unique={per_raw_unique} multi={per_raw_multi} || "
              f"REDUCED total={per_red_total} unique={per_red_unique} multi={per_red_multi}")
        grand_raw_total += per_raw_total
        grand_raw_unique += per_raw_unique
        grand_raw_multi += per_raw_multi
        grand_red_total += per_red_total
        grand_red_unique += per_red_unique
        grand_red_multi += per_red_multi

    print()
    print(f"  GRAND ({name}): RAW total={grand_raw_total} unique={grand_raw_unique} multi={grand_raw_multi} || "
          f"REDUCED total={grand_red_total} unique={grand_red_unique} multi={grand_red_multi}")
    return grand_red_multi == 0


def c2_donor_roots(kind, i):
    """Roots appearing as donor/receiver under simple (kind, i) at C_2."""
    subs = c2_subtypes_for_simple(kind, i)
    roots = set()
    for st in subs:
        for c in [+1, -1]:
            d, r = c2_subtype_donor_receiver(kind, i, st, c)
            roots.add(d); roots.add(r)
    return sorted(roots)


def b2_donor_roots(kind, i):
    subs = b2_subtypes_for_simple(kind, i)
    roots = set()
    for st in subs:
        for c in [+1, -1]:
            d, r = b2_subtype_donor_receiver(kind, i, st, c)
            roots.add(d); roots.add(r)
    return sorted(roots)


if __name__ == "__main__":
    # C_2 check
    c2_ok = phase_a_check(
        "C_2",
        simples=[('S', 0), ('L', 1)],
        subtype_units_fn=c2_subtype_units,
        subtype_dr_fn=c2_subtype_donor_receiver,
        subtypes_fn=c2_subtypes_for_simple,
        donor_roots=c2_donor_roots,
        c_values=[1, 2, 3, 4, -1, -2, -3, -4],
        max_pi_total=4,
    )

    # B_2 check
    b2_ok = phase_a_check(
        "B_2",
        simples=[('L', 0), ('S', 1)],
        subtype_units_fn=b2_subtype_units,
        subtype_dr_fn=b2_subtype_donor_receiver,
        subtypes_fn=b2_subtypes_for_simple,
        donor_roots=b2_donor_roots,
        c_values=[1, 2, 3, 4, -1, -2, -3, -4],
        max_pi_total=4,
    )

    print()
    print("="*70)
    print(f"IH base case verification:")
    print(f"  C_2 REDUCED uniqueness: {'OK' if c2_ok else 'FAILED'}")
    print(f"  B_2 REDUCED uniqueness: {'OK' if b2_ok else 'FAILED'}")
    print("="*70)
