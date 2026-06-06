"""
Section 3 sign-tracking: symbolic BGG sliding computation at C_3 s_1.

Given pi (a Kostant partition) and c (a positive integer), compute the PBW
expansion of f_{alpha_1}^c . pi(f) in the C_3 negative-root PBW algebra.
Each term is a Kostant monomial with a coefficient that is a polynomial in
the SYMBOLIC Chevalley structure constants N_{i, beta}.

We use the identity
    f_alpha . f_beta = f_beta . f_alpha + N_{alpha, beta} . f_{alpha + beta}
whenever alpha + beta is a positive root, and 0 otherwise (in n^-).

Conventions:
  * BGG sliding ABSORBS f_{alpha_i} into a slot, shifting beta -> beta + alpha_i.
  * In Phase A's orbit-swap labelling at s_1 (C_3):
      "+" direction takes Phase-A-donor (high-pairing) -> receiver (low-pairing).
      BGG sliding goes the OTHER way (low-pairing -> high-pairing) = Phase A "-".
    The sign-flip is a relabeling; we work in BGG sliding's natural direction.

The core verification (Lemma BGG-orbit-swap correspondence):

Each same-bidegree, fully-absorbed (alpha_i-free) Kostant target pi' produced
by BGG sliding from pi at simple s_i corresponds to a UNIQUE reduced
orbit-swap multiset M_0, and the BGG matrix entry M_{pi,pi'} factorizes as
  M_{pi,pi'} = K(pi,pi') . prod_{st in supp(M_0)} (chain product of Chevalley constants)
where K(pi,pi') is a POSITIVE INTEGER combinatorial factor (multinomial) and
the chain product depends only on M_0 and the structure constants.

We verify this across many small (pi, c) cases.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fractions import Fraction
from collections import defaultdict, Counter
from itertools import product

import sympy as sp

import aug_tilde_C3_richer as C3
import su1_phase_a_C3 as SU1


N = 3

POS_ROOTS = C3.positive_roots_Cn(N)
POS_ROOTS_SET = set(r for r, _ in POS_ROOTS)
ROOT_KIND = dict(POS_ROOTS)

# Simple roots in our convention (matching the script):
SIMPLES = {
    ('S', 0): (1, -1, 0),   # alpha_0 = e_0 - e_1 (short)
    ('S', 1): (0, 1, -1),   # alpha_1 = e_1 - e_2 (short)
    ('L', 2): (0, 0, 2),    # alpha_2 = 2 e_2 (long)
}


def add(u, v):
    return tuple(u[i] + v[i] for i in range(N))


def bracket_root(alpha, beta):
    """Return alpha + beta if it's a positive root, else None."""
    s = add(alpha, beta)
    if s in POS_ROOTS_SET:
        return s
    return None


def sym_N(alpha, beta):
    """Symbol for the Chevalley structure constant in [f_alpha, f_beta] = N f_{alpha+beta}."""
    return sp.Symbol(f"N({alpha},{beta})", commutative=True)


def kostant_key(pi):
    return tuple(sorted((beta, m) for beta, m in pi.items() if m != 0))


# ============ BGG sliding expansion =================
#
# Apply f_{alpha}^c to a PBW monomial (Kostant partition) using
#   f_alpha . prod_i f_{beta_i}^{n_i} = (sum over absorptions)
# Each step: either let f_alpha stay (joins leftover alpha pile) or absorb
# into a current slot beta with mult n, contributing n . N_{alpha, beta}.

def expand_alpha_c_times_pi(alpha, c, pi):
    """Compute  f_alpha^c . pi(f)  in the Kostant basis.
    Returns dict {kostant_key: sympy_coeff}.
    """
    results = defaultdict(lambda: sp.Integer(0))

    def dfs(current_pi, abs_left, coeff):
        if abs_left == 0:
            results[kostant_key(current_pi)] += coeff
            return
        # Option 1: leftover f_alpha (joins pile)
        np_ = dict(current_pi)
        np_[alpha] = np_.get(alpha, 0) + 1
        dfs(np_, abs_left - 1, coeff)
        # Option 2: absorb into a slot
        for beta in list(current_pi.keys()):
            mult = current_pi[beta]
            new_root = bracket_root(alpha, beta)
            if new_root is None:
                continue
            N_const = sym_N(alpha, beta)
            np_ = dict(current_pi)
            np_[beta] -= 1
            if np_[beta] == 0:
                del np_[beta]
            np_[new_root] = np_.get(new_root, 0) + 1
            dfs(np_, abs_left - 1, coeff * mult * N_const)

    dfs(dict(pi), c, sp.Integer(1))
    return dict(results)


# ============ Reduced multiset to expected coefficient ============

def chain_factor_for_subtype(kind, i, st, sign, N=3):
    """The chain product of Chevalley constants for ONE swap of subtype st
    at simple (kind, i) in BGG sliding direction.

    For 1-unit subtypes: one absorption, factor = N_{alpha_i, beta_low-pairing-end}.
    For 2-unit subtypes (LL at C_n short simples): two chained absorptions,
        factor = N_{alpha_i, low-pairing-end} . N_{alpha_i, intermediate}.

    The "low-pairing end" in Phase A convention: this is the donor of the
    "+" direction's RECEIVER (since +/- is reversed between Phase A and BGG).

    Specifically: in Phase A "(b+, p=0) +" at s_1: donor = e_0+e_1 (high pairing),
    receiver = e_0+e_2 (low pairing).  In BGG sliding, "−" direction absorbs
    f_{alpha_1} into f_{e_0+e_2} (low pairing) to get f_{e_0+e_1}.  So BGG-direction
    chain factor for "(b+, p=0) BGG-direction" = N_{alpha_1, e_0+e_2}.
    """
    alpha = SIMPLES[(kind, i)]
    # Get the BGG-direction donor (= Phase A receiver in '+' direction).
    # We'll compute via Phase A's subtype_donor_receiver with c < 0 (which gives
    # donor = Phase A receiver of '+').
    bgg_donor, bgg_recv = C3.subtype_donor_receiver(kind, i, st, -1, N)
    u = C3.subtype_units_per_swap(kind, i, st, N)
    if u == 1:
        return sym_N(alpha, bgg_donor)
    elif u == 2:
        # Chain: bgg_donor -> intermediate -> bgg_recv via two absorptions.
        intermediate = add(alpha, bgg_donor)
        if intermediate not in POS_ROOTS_SET:
            raise ValueError(f"Chain intermediate {intermediate} not a positive root")
        return sym_N(alpha, bgg_donor) * sym_N(alpha, intermediate)
    else:
        raise ValueError(f"Unsupported units {u}")


def apply_reduced_multiset_bgg(pi, M0, kind, i, N=3):
    """Apply a REDUCED multiset M0 to pi in the BGG-direction.

    Phase A's reduced multiset has at most one of '+' or '-' per subtype.
    For a sign 's' entry (st, s) with count m: applies m swaps in 's' direction.
    But BGG sliding only naturally implements ONE direction.  We translate:
    if M0 has only '+' entries, that's Phase A "+" = high-pairing-to-low (Phase A).
    If M0 has only '-' entries, that's Phase A "−" = low-to-high = BGG direction.

    For c > 0 in Phase A, the natural reduced multisets have net "+" → these are
    NON-BGG-direction.  For c < 0 in Phase A, reduced multisets are net "−" →
    BGG direction.

    To match BGG sliding (which corresponds to Phase A c < 0), we pass c = -BGG_c
    to Phase A and expect "−" entries.
    """
    new_pi = dict(pi)
    for (st, sign), m in M0.items():
        # In BGG-sliding direction: donor is the BGG-donor (= Phase A's receiver of '+')
        bgg_donor, bgg_recv = C3.subtype_donor_receiver(kind, i, st, -1, N)
        # If sign is '-' in Phase A: that's BGG direction.  Apply normally.
        # If sign is '+' in Phase A: that's reverse-BGG direction.  Skip / error.
        if sign != '-':
            # Phase A "+" multiset = REVERSE-BGG; doesn't appear in BGG sliding f_alpha^c with c > 0.
            return None
        new_pi[bgg_donor] = new_pi.get(bgg_donor, 0) - m
        if new_pi[bgg_donor] == 0:
            del new_pi[bgg_donor]
        new_pi[bgg_recv] = new_pi.get(bgg_recv, 0) + m
    return {r: v for r, v in new_pi.items() if v > 0}


def reduced_multiset_for_target(pi, pi_prime, c_bgg, kind, i, N=3):
    """Find the unique REDUCED multiset (in Phase A '-' direction) taking pi to pi_prime
    via c_bgg BGG-direction absorptions.  Returns (M0, expected_chain_factor) or None.
    """
    # Phase A's c = -c_bgg (sign flip).
    c_phaseA = -c_bgg
    multisets_phase_a = SU1.enumerate_orbit_swap_multisets(pi, c_phaseA, kind, i, N)
    # Filter to reduced multisets in '-' direction (= BGG direction).  Multiple
    # RAW multisets may collapse to the same REDUCED multiset; dedupe by reduced key.
    candidates = {}
    for M in multisets_phase_a:
        red = SU1.reduce_multiset(M)
        if not all(sg == '-' for (st, sg) in red.keys()):
            continue
        end_pi = apply_reduced_multiset_bgg(pi, red, kind, i, N)
        if end_pi is None:
            continue
        if kostant_key(end_pi) == kostant_key(pi_prime):
            candidates[SU1.freeze_multiset(red)] = red
    if len(candidates) != 1:
        return None, None
    M0 = next(iter(candidates.values()))
    # Compute expected chain factor.
    chain = sp.Integer(1)
    for (st, sg), m in M0.items():
        chain *= chain_factor_for_subtype(kind, i, st, sg, N)**m
    return M0, chain


def bidegree_of_kostant_key(key, N=3):
    """(long_count, short_count) of a Kostant partition."""
    long_cnt = 0
    short_cnt = 0
    for beta, m in key:
        if ROOT_KIND[beta] == 'L':
            long_cnt += m
        else:
            short_cnt += m
    return (long_cnt, short_cnt)


# ============ Comprehensive verification ============

def verify_case(pi, c, kind='S', i=1, N=3, verbose=False):
    """Verify Lemma BGG-orbit-swap correspondence at a single (pi, c) case.

    For each same-bidegree FULL-ABSORPTION target pi' in BGG expansion:
      - Find the unique reduced multiset M_0 mapping pi -> pi' (BGG direction).
      - Verify coefficient factors as K(pi, pi') * chain_factor(M_0) where K is a positive integer.

    Returns (ok, n_targets_checked, n_mismatches, details).
    """
    alpha = SIMPLES[(kind, i)]
    result = expand_alpha_c_times_pi(alpha, c, pi)
    src_bd = bidegree_of_kostant_key(kostant_key(pi))
    src_bd_total = (src_bd[0], src_bd[1])  # (long, short) of pi (without alpha pile)

    n_targets = 0
    n_mismatches = 0
    details = []

    for key, coeff in result.items():
        # Only consider targets with FULL absorption: alpha multiplicity in pi' = 0.
        alpha_mult = dict(key).get(alpha, 0)
        if alpha_mult != 0:
            continue
        # Target bidegree
        tgt_bd = bidegree_of_kostant_key(key)
        if tgt_bd != src_bd:
            continue  # Cross-bidegree — not in Aug~ framework.
        n_targets += 1
        pi_prime = dict(key)
        # Find reduced multiset
        M0, chain_factor = reduced_multiset_for_target(pi, pi_prime, c, kind, i, N)
        if M0 is None:
            n_mismatches += 1
            details.append((pi_prime, sp.expand(coeff), "NO unique reduced multiset"))
            continue
        # Check factorization: coeff / chain_factor should be a positive integer
        simplified = sp.expand(coeff)
        ratio = sp.simplify(simplified / chain_factor)
        if not (ratio.is_integer and ratio.is_positive):
            # Try assuming integer
            if not (ratio.is_constant() and ratio == sp.simplify(ratio).as_real_imag()[0]):
                pass
            try:
                ratio_int = int(ratio)
                ok = (ratio_int > 0 and sp.simplify(simplified - ratio_int * chain_factor) == 0)
            except (TypeError, ValueError):
                ok = False
        else:
            ok = True
        if not ok:
            n_mismatches += 1
            details.append((pi_prime, simplified, f"factor MISMATCH; ratio = {ratio}"))
        else:
            details.append((pi_prime, simplified, f"OK: K = {ratio} * {chain_factor}"))

    return n_mismatches == 0, n_targets, n_mismatches, details


def run_demo():
    print("="*70)
    print("Demo cases (verbose)")
    print("="*70)

    cases = [
        # (pi, c, label)
        ({(1, 0, 1): 1}, 1, "1-unit b+ orbit (e_0+e_2 -> e_0+e_1)"),
        ({(0, 0, 2): 1}, 2, "2-unit LL chain (2 e_2 -> e_1+e_2 -> 2 e_1)"),
        ({(0, 0, 2): 1, (0, 1, 1): 1}, 2, "LL chain with bystander e_1+e_2"),
        ({(0, 0, 2): 2}, 2, "Two copies of 2 e_2"),
        ({(0, 0, 2): 1, (1, 0, 1): 1}, 3, "LL chain + b+ swap (c=3)"),
    ]

    for pi, c, label in cases:
        print(f"\n--- {label}: pi={pi}, c={c} ---")
        result = expand_alpha_c_times_pi(SIMPLES[('S', 1)], c, pi)
        src_bd = bidegree_of_kostant_key(kostant_key(pi))
        for key, coeff in sorted(result.items()):
            pi_prime = dict(key)
            tgt_bd = bidegree_of_kostant_key(key)
            alpha_mult = pi_prime.get(SIMPLES[('S', 1)], 0)
            full_abs = (alpha_mult == 0)
            same_bd = (tgt_bd == src_bd)
            simplified = sp.expand(coeff)
            tag = ""
            if full_abs and same_bd:
                tag = "  [SAME-BD, FULL-ABS]"
            elif full_abs:
                tag = "  [cross-bd]"
            else:
                tag = "  [leftover alpha]"
            print(f"  pi' = {pi_prime}{tag}")
            print(f"    coeff = {simplified}")
        ok, n_tgt, n_mis, details = verify_case(pi, c, verbose=False)
        print(f"  Verification: targets={n_tgt}, mismatches={n_mis}")
        for d in details:
            print(f"    {d[0]}: {d[2]}")


def run_comprehensive(kind='S', i=1, max_pi_total=3, c_values=(1, 2, 3)):
    """Verify BGG-orbit-swap correspondence over a comprehensive set of small cases at C_3 (kind, i)."""
    print("\n" + "="*70)
    print(f"Comprehensive verification at C_3 ({kind}, {i})")
    print("="*70)

    roots = SU1.donor_supports_for_s_i(kind, i, N)
    pis = SU1.enumerate_pis(roots, max_pi_total)

    total_cases = 0
    total_targets = 0
    total_mismatches = 0
    mismatch_examples = []

    for pi in pis:
        if sum(pi.values()) == 0:
            continue
        for c in c_values:
            ok, n_tgt, n_mis, details = verify_case(pi, c, kind, i, N)
            if n_tgt == 0:
                continue
            total_cases += 1
            total_targets += n_tgt
            total_mismatches += n_mis
            if not ok:
                mismatch_examples.append((pi, c, details))

    print(f"\nCases checked: {total_cases}")
    print(f"Same-bidegree full-absorption targets: {total_targets}")
    print(f"Mismatches: {total_mismatches}")

    if mismatch_examples:
        print(f"\nMismatch examples (up to 5):")
        for pi, c, details in mismatch_examples[:5]:
            print(f"  pi={pi}, c={c}:")
            for d in details:
                if "MISMATCH" in d[2] or "NO unique" in d[2]:
                    print(f"    pi' = {d[0]}  coeff = {d[1]}  -- {d[2]}")

    return total_cases, total_targets, total_mismatches


if __name__ == "__main__":
    run_demo()
    grand_cases = 0
    grand_targets = 0
    grand_mismatches = 0
    for (kind, i, c_values) in [('S', 0, (1, 2, 3)),
                                ('S', 1, (1, 2, 3)),
                                ('L', 2, (1, 2, 3, 4))]:
        n_cases, n_targets, n_mismatches = run_comprehensive(kind, i, max_pi_total=3, c_values=c_values)
        grand_cases += n_cases
        grand_targets += n_targets
        grand_mismatches += n_mismatches
    print()
    print("="*70)
    print(f"GRAND SUMMARY (all C_3 simples): {grand_cases} cases, "
          f"{grand_targets} same-bidegree targets, {grand_mismatches} mismatches.")
    if grand_mismatches == 0:
        print("VERIFIED: BGG matrix entries factor as K(pi,pi') * chain(M_0) for unique M_0.")
    else:
        print(f"!!! {grand_mismatches} mismatches need investigation !!!")
    print("="*70)
