"""
bdi_qLR.py — explicit BDI quantum Littlewood-Richardson algorithm via
factor-by-factor descent through v2's chain-factor decomposition.

Author: Rick, 2026-05-18, deep work session.

This module implements:
  1. Chain-factor coordinates of a Kostant partition pi at type B_n.
  2. A LOCAL characterization of "B_n-highest" (eps_n(pi) = 0) in terms of
     a left-to-right carry P_a through the chain factors.
  3. A counting algorithm: given a Kostant weight nu, count B_n-highest pi
     of weight nu by enumerating valid (M, B, T, S) configurations.
  4. A "descent recording" map: for any pi, produce its B_n-highest reduction
     pi^hw plus the sequence of (step_type, factor) descent steps.
  5. Cross-checks against the existing CST bracket-based crystal scripts
     (b_i_b{2,3,4,5}.py at /home/agent/projects/proofs/remark47/coideal_check/).

DESIGN NOTES.

Roots of B_n (n >= 2):
  - Chain roots: E_a, E_a - E_n, E_a + E_n for a = 1, ..., n-1.
  - Singleton: E_n.
  - Non-touching: E_a - E_b, E_a + E_b for 1 <= a < b < n.
    (Notation here: 1-indexed root labels match v2 paper.)

Chain factor C_a (a in 1..n-1) coords: (M_a, B_a, T_a):
  M_a = multiplicity of E_a (mid)
  B_a = multiplicity of E_a - E_n (bot)
  T_a = multiplicity of E_a + E_n (top)

Singleton C_sing coords: S = multiplicity of E_n.

Non-touching coords: pi^NT (multiplicity vector on the (n-1)(n-2) non-touching
roots). The B_n-action ignores pi^NT, so counts factor.

Bracket string for B_n-action (CST Def 2.14 / v2 §1):
  S_n(pi) = prod_{a=1..n-1} [ )^{M_a}_{E_a} (^{2B_a}_{E_a-E_n} )^{2T_a}_{E_a+E_n} (^{M_a}_{E_a} ]
          . )^S_{E_n}.

Cancellation: repeatedly delete '(' immediately followed by ')'. After cancel,
all surviving ')' are left of all surviving '('.
  eps_n(pi) = # surviving ')'.
  phi_n(pi) = # surviving '('.

KEY THEOREM (proved in main proof file): pi is B_n-highest (eps_n(pi) = 0) iff
the chain coordinates satisfy:

  (HW_a) for each a = 1..n-1:  M_a <= P_{a-1} AND M_a + 2*T_a <= P_{a-1} + 2*B_a
  (HW_sing):                    S <= P_{n-1}

  where  P_0 = 0  and  P_a = P_{a-1} + 2*(B_a - T_a).

This is a LOCAL (chain-by-chain) test, with a single forward-carry variable P_a.

The "descent recording" R(pi) records which chain factor's bracket was hit at
each e_n step in the chain pi -> e_n pi -> e_n^2 pi -> ... -> pi^hw. This is
the BDI analog of Azenhas's recording tableau (arXiv:2603.16698).
"""

from itertools import product
from collections import defaultdict


# ============================================================================
# Chain-factor highest-weight test
# ============================================================================

def is_Bn_highest(M, B, T, S, n):
    """Test whether the Kostant partition with chain+sing coords (M, B, T, S)
    at type B_n is B_n-highest, i.e., eps_n(pi) = 0.

    M, B, T are tuples of length n-1 (indices 0..n-2 ↔ chains a=1..n-1).
    S is a non-negative integer.

    By the local characterization (proof in main file), this is equivalent to
    (HW_a) for all a and (HW_sing) holding."""
    assert len(M) == len(B) == len(T) == n - 1
    P = 0  # P_0 = 0
    for a in range(n - 1):
        if M[a] > P:                              # (HW_a) part 1: leading-) test
            return False
        if M[a] + 2 * T[a] > P + 2 * B[a]:        # (HW_a) part 2: top-) test
            return False
        P = P + 2 * (B[a] - T[a])                 # P_a
    if S > P:                                     # (HW_sing)
        return False
    return True


def carry_profile(M, B, T, n):
    """Return the carry profile (P_0, P_1, ..., P_{n-1})."""
    P = [0]
    for a in range(n - 1):
        P.append(P[-1] + 2 * (B[a] - T[a]))
    return tuple(P)


# ============================================================================
# Enumeration: count B_n-highest chain configurations of given weight
# ============================================================================

def enumerate_chain_configs(c, weight_n):
    """Yield (M, B, T, S) configurations where:
      - c[a-1] = M_a + B_a + T_a (chain-a content), for a = 1..n-1.
      - weight_n = S + sum_a (T_a - B_a) (total E_n-component).

    Here n = len(c) + 1. No B_n-highest filter applied."""
    n = len(c) + 1
    # Per-chain choices: (M_a, B_a, T_a) with M_a + B_a + T_a = c[a-1].
    chain_choices = []
    for a in range(n - 1):
        choices = []
        for M_a in range(c[a] + 1):
            for B_a in range(c[a] - M_a + 1):
                T_a = c[a] - M_a - B_a
                choices.append((M_a, B_a, T_a))
        chain_choices.append(choices)
    for combo in product(*chain_choices):
        M = tuple(x[0] for x in combo)
        B = tuple(x[1] for x in combo)
        T = tuple(x[2] for x in combo)
        S = weight_n - sum(T[a] - B[a] for a in range(n - 1))
        if S < 0:
            continue
        yield (M, B, T, S)


def count_Bn_highest(c, weight_n):
    """Count B_n-highest Kostant partitions with chain+sing content (c, weight_n).

    Returns (count, witnesses) where witnesses is a list of (M, B, T, S) tuples."""
    n = len(c) + 1
    count = 0
    witnesses = []
    for (M, B, T, S) in enumerate_chain_configs(c, weight_n):
        if is_Bn_highest(M, B, T, S, n):
            count += 1
            witnesses.append((M, B, T, S))
    return count, witnesses


# ============================================================================
# Non-touching root multiplicities (NT factor — free w.r.t. B_n action)
# ============================================================================

def nt_root_dims(n):
    """Return the list of non-touching positive roots at B_n: {E_a +/- E_b : 1 <= a < b < n}.
    Each contributes a free non-negative-integer multiplicity, with weight in
    E_a +/- E_b only — they have no E_n component.

    Returns list of (a, b, sign) tuples representing E_a + sign * E_b for 1 <= a < b < n."""
    out = []
    for b in range(2, n):  # b >= 2, b < n
        for a in range(1, b):
            out.append((a, b, +1))   # E_a + E_b
            out.append((a, b, -1))   # E_a - E_b
    return out


def count_nt_configs(weight_chains_NT, n):
    """Count non-negative integer multiplicities on non-touching roots
    realizing the chain-portion weight weight_chains_NT.

    weight_chains_NT is a vector indexed 1..n-1: the E_a-component contributed
    by NT roots only (NT roots have no E_n component).

    Each NT root E_a +/- E_b contributes to E_a and E_b coordinates.
    This is a parking-function-like counting; can be done by recursion."""
    nt_roots = nt_root_dims(n)
    # Decision-tree enumeration. For each NT root, choose multiplicity 0, 1, ...
    # subject to weight_chains_NT[a] >= sum of contributions to a.

    # Recursive memoized
    max_per_nt = [min(weight_chains_NT[a-1], weight_chains_NT[b-1])
                  for (a, b, sign) in nt_roots]

    def recurse(idx, remaining):
        """Count completions starting from nt root #idx with remaining weight."""
        if idx == len(nt_roots):
            return 1 if all(r == 0 for r in remaining) else 0
        a, b, sign = nt_roots[idx]
        total = 0
        # Multiplicity m for this NT root: needs remaining[a-1] >= m and remaining[b-1] >= m.
        max_m = min(remaining[a-1], remaining[b-1])
        for m in range(max_m + 1):
            new_rem = list(remaining)
            new_rem[a-1] -= m
            new_rem[b-1] -= m
            total += recurse(idx + 1, tuple(new_rem))
        return total

    return recurse(0, tuple(weight_chains_NT))


# ============================================================================
# Total B_n-highest count for a given Kp weight nu (full count over Kp(infty))
# ============================================================================

def total_Bn_highest_count(nu_chains, nu_n, n, m_bound=None):
    """Total count of B_n-highest pi in Kp(infty) with weight:
      sum_a nu_chains[a-1] * E_a + nu_n * E_n.

    nu_chains[a-1] is the TOTAL E_a coord (chain + NT contributions, signed).
    Decompose by enumerating NT configurations and summing chain counts.

    NT root (a, b, sign) at multiplicity m contributes +m to coord a, sign*m to coord b.
    Chain content[a-1] = nu_chains[a-1] - (NT contribution to coord a). Must be >= 0.

    m_bound: per-root multiplicity bound (defaults to a conservative cap based on |nu_chains|)."""
    if m_bound is None:
        m_bound = max(2 * sum(abs(x) for x in nu_chains) + abs(nu_n) + 4, 6)

    nt_roots = nt_root_dims(n)

    def recurse_nt(idx, residual):
        """residual[a-1] = remaining nu_chains[a-1] budget for chain part + later NT.
        At idx == len(nt_roots), residual IS the chain content; must be >= 0."""
        if idx == len(nt_roots):
            chain_content = tuple(residual)
            if any(c < 0 for c in chain_content):
                return 0
            cnt, _ = count_Bn_highest(chain_content, nu_n)
            return cnt
        a, b, sign = nt_roots[idx]
        # NT mult m: -m to residual[a-1], -sign*m to residual[b-1].
        # Need residual[a-1] - m to be achievable (>= 0 ultimately, but other NTs only add — actually no other NTs only subtract from residual[a-1] further if they involve a).
        # Conservative bound: m <= m_bound.
        total = 0
        for m in range(m_bound + 1):
            new_a = residual[a-1] - m
            new_b = residual[b-1] - sign * m
            # Early pruning: if residual[a-1] - m < 0 and no later NT involves (a, ?) adds to it, we're dead.
            # NT root (a', b') with a' == a or b' == a: only with sign affects.
            # NT roots later than idx involving a may further reduce residual[a-1] (if they contribute +1 to coord a).
            # Actually ALL NT roots have +1 contribution to their first coord and ±1 to their second.
            # So if a appears as first index of a later NT, that NT can only further DECREASE residual[a-1].
            # If a appears as second index with sign=-1, that NT can INCREASE residual[a-1].
            #
            # Simplest pruning: check if new_a or new_b are too negative to recover.
            # Skip the pruning for clarity, but cap m at a level where it can't possibly work.
            if new_a < -m_bound or new_b < -m_bound:
                break
            new_residual = list(residual)
            new_residual[a-1] = new_a
            new_residual[b-1] = new_b
            total += recurse_nt(idx + 1, new_residual)
        return total

    return recurse_nt(0, list(nu_chains))


# ============================================================================
# Descent recording: factor-by-factor reduction to B_n-highest
# ============================================================================

def chain_factor_for(beta, n):
    """Return which factor the root beta belongs to: ('C', a), ('SING',), or ('NT', a, b, sign)."""
    # Parse root label tuple: (a, sign_n) for chain root E_a + sign_n * E_n where sign_n in {-1, 0, +1};
    # ('sing',) for E_n; ('nt', a, b, sign) for E_a + sign * E_b with 1 <= a < b < n.
    raise NotImplementedError  # we'll use chain_factor_step instead


def descent_step(M, B, T, S, n):
    """Perform one e_n step on the chain+sing coords (B_n action) and return
    the new (M', B', T', S') plus the recording (step_type, factor_index).

    factor_index is in {1, ..., n-1, 'sing'} indicating which factor was hit.
    step_type is in {'MB', 'TM', 'Sing'}.

    Returns None if eps_n = 0 (no e_n possible)."""
    # Build the bracket string and find rightmost surviving ')'.
    # We use the optimized chain-by-chain stack:
    P = 0           # paren count after consuming earlier chains
    # We need to find rightmost surviving ')' -- so walk through chains and track.
    # Easier: build the labeled bracket string and use cancel + scan.
    bracket = []    # list of (token, beta_label, factor_index)
    for a_idx in range(n - 1):
        a = a_idx + 1
        for _ in range(M[a_idx]):
            bracket.append((')', ('E', a), a))                # mid )_{E_a}
        for _ in range(2 * B[a_idx]):
            bracket.append(('(', ('E-En', a), a))             # bot ( on E_a - E_n
        for _ in range(2 * T[a_idx]):
            bracket.append((')', ('E+En', a), a))             # top ) on E_a + E_n
        for _ in range(M[a_idx]):
            bracket.append(('(', ('E', a), a))                # mid ( on E_a (trailing)
    for _ in range(S):
        bracket.append((')', ('En',), 'sing'))                # singleton )

    # Cancel.
    while True:
        for k in range(len(bracket) - 1):
            if bracket[k][0] == '(' and bracket[k+1][0] == ')':
                del bracket[k:k+2]
                break
        else:
            break

    # Find rightmost surviving ')'.
    rightmost = None
    for k in range(len(bracket) - 1, -1, -1):
        if bracket[k][0] == ')':
            rightmost = bracket[k]
            break
    if rightmost is None:
        return None  # eps_n = 0

    _, beta_label, factor = rightmost
    M_new = list(M); B_new = list(B); T_new = list(T); S_new = S
    if beta_label[0] == 'En':
        # Singleton root E_n: decrement S.
        S_new -= 1
        return (tuple(M_new), tuple(B_new), tuple(T_new), S_new, 'Sing', 'sing')
    elif beta_label[0] == 'E':
        # Mid root E_a: MB step. (M, B, T) -> (M-1, B+1, T).
        a_idx = beta_label[1] - 1
        M_new[a_idx] -= 1
        B_new[a_idx] += 1
        return (tuple(M_new), tuple(B_new), tuple(T_new), S_new, 'MB', factor)
    elif beta_label[0] == 'E+En':
        # Top root E_a + E_n: TM step. (M, B, T) -> (M+1, B, T-1).
        a_idx = beta_label[1] - 1
        M_new[a_idx] += 1
        T_new[a_idx] -= 1
        return (tuple(M_new), tuple(B_new), tuple(T_new), S_new, 'TM', factor)
    else:
        raise ValueError(f"unexpected beta_label {beta_label}")


def descent_recording(M, B, T, S, n):
    """Repeatedly apply descent_step until B_n-highest, recording each step.

    Returns (M_hw, B_hw, T_hw, S_hw, recording) where recording is a list of
    (step_type, factor_index) pairs."""
    M, B, T, S = tuple(M), tuple(B), tuple(T), S
    recording = []
    while True:
        step = descent_step(M, B, T, S, n)
        if step is None:
            break
        M, B, T, S, step_type, factor = step
        recording.append((step_type, factor))
    return M, B, T, S, recording


def reconstruct(M_hw, B_hw, T_hw, S_hw, recording):
    """Inverse of descent_recording: replay the recording in reverse to recover
    the original (M, B, T, S) from the B_n-highest reduction."""
    M = list(M_hw); B = list(B_hw); T = list(T_hw); S = S_hw
    for step_type, factor in reversed(recording):
        if step_type == 'Sing':
            S += 1
        elif step_type == 'MB':
            a_idx = factor - 1
            M[a_idx] += 1
            B[a_idx] -= 1
        elif step_type == 'TM':
            a_idx = factor - 1
            T[a_idx] += 1
            M[a_idx] -= 1
    return tuple(M), tuple(B), tuple(T), S


# ============================================================================
# Cross-checks against b_i_bN.py
# ============================================================================

def to_kp_b3(M, B, T, S):
    """Convert chain+sing coords at B_3 to a Kp dict matching b_i_b3.py keys."""
    # Chain a=1: E_1 (mid), E_1-E_3 (bot), E_1+E_3 (top)
    # Chain a=2: E_2 (mid), E_2-E_3 (bot), E_2+E_3 (top)
    # Sing: E_3
    pi = {}
    if M[0]: pi['e1'] = M[0]
    if B[0]: pi['e1-e3'] = B[0]
    if T[0]: pi['e1+e3'] = T[0]
    if M[1]: pi['e2'] = M[1]
    if B[1]: pi['e2-e3'] = B[1]
    if T[1]: pi['e2+e3'] = T[1]
    if S: pi['e3'] = S
    return pi


def cross_check_B3(max_total=4):
    """Compare is_Bn_highest with the direct CST computation in b_i_b3.py."""
    import sys
    sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')
    import b_i_b3 as B3

    n = 3
    n_total = 0
    n_agree = 0
    n_disagree = 0
    disagreements = []

    # Enumerate (M_1, B_1, T_1, M_2, B_2, T_2, S) with sum <= max_total.
    for M1 in range(max_total + 1):
      for B1 in range(max_total + 1):
        for T1 in range(max_total + 1):
          for M2 in range(max_total + 1):
            for B2 in range(max_total + 1):
              for T2 in range(max_total + 1):
                for S in range(max_total + 1):
                    total = M1+B1+T1+M2+B2+T2+S
                    if total > max_total:
                        continue
                    M = (M1, M2); B = (B1, B2); T = (T1, T2)
                    pi = to_kp_b3(M, B, T, S)

                    # B_n-highest via my chain test
                    mine = is_Bn_highest(M, B, T, S, n)

                    # B_n-highest via direct CST: eps_3(pi) == 0
                    direct = (B3.eps_i(pi, 3) == 0)

                    n_total += 1
                    if mine == direct:
                        n_agree += 1
                    else:
                        n_disagree += 1
                        if len(disagreements) < 5:
                            disagreements.append((M, B, T, S, mine, direct))

    print(f"B_3 cross-check (max_total={max_total}): {n_agree}/{n_total} agree, {n_disagree} disagree")
    if disagreements:
        print("  Disagreements:")
        for M, B, T, S, mine, direct in disagreements:
            print(f"    M={M} B={B} T={T} S={S}: chain-test={mine}, direct={direct}")
    return n_disagree == 0


def cross_check_B4(max_total=4):
    """Compare is_Bn_highest with the direct CST computation in b_i_b4.py."""
    import sys
    sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')
    import b_i_b4 as B4

    n = 4
    n_total = 0
    n_agree = 0
    n_disagree = 0
    disagreements = []

    # Helper: chain coords (M, B, T) for a in 1..3, plus S, with total content <= max_total.
    # M, B, T are tuples of length 3.
    def kp_from_coords(M, B, T, S, NT):
        """Build the b_i_b4 Kp dict."""
        # b_i_b4 uses keys like 'e1', 'e2', 'e3', 'e1-e4', 'e1+e4', etc.
        pi = {}
        # Chain roots:
        for a_idx in range(3):
            a = a_idx + 1
            if M[a_idx]: pi[f'e{a}'] = M[a_idx]
            if B[a_idx]: pi[f'e{a}-e4'] = B[a_idx]
            if T[a_idx]: pi[f'e{a}+e4'] = T[a_idx]
        if S: pi['e4'] = S
        # NT roots: NT is dict from (a, b, sign) to multiplicity.
        for (a, b, sign), m in NT.items():
            if m:
                op = '+' if sign == +1 else '-'
                pi[f'e{a}{op}e{b}'] = m
        return pi

    # Just enumerate the chain+sing part; ignore NT for this test.
    # (NT doesn't affect B_n-highest since NT roots don't contribute to the
    # S_n bracket — verified separately in b_i_b4.py.)
    for M1 in range(max_total + 1):
      for M2 in range(max_total + 1):
        for M3 in range(max_total + 1):
          for B1 in range(max_total + 1):
            for B2 in range(max_total + 1):
              for B3 in range(max_total + 1):
                if M1+M2+M3+B1+B2+B3 > max_total:
                    continue
                for T1 in range(max_total + 1):
                  for T2 in range(max_total + 1):
                    for T3 in range(max_total + 1):
                      for S in range(max_total + 1):
                        total = M1+M2+M3+B1+B2+B3+T1+T2+T3+S
                        if total > max_total:
                            continue
                        M = (M1, M2, M3); B = (B1, B2, B3); T = (T1, T2, T3)
                        pi = kp_from_coords(M, B, T, S, {})
                        mine = is_Bn_highest(M, B, T, S, n)
                        direct = (B4.eps_i(pi, 4) == 0)
                        n_total += 1
                        if mine == direct:
                            n_agree += 1
                        else:
                            n_disagree += 1
                            if len(disagreements) < 5:
                                disagreements.append((M, B, T, S, mine, direct))

    print(f"B_4 cross-check (max_total={max_total}, chain+sing only): {n_agree}/{n_total} agree, {n_disagree} disagree")
    if disagreements:
        for M, B, T, S, mine, direct in disagreements:
            print(f"    M={M} B={B} T={T} S={S}: chain-test={mine}, direct={direct}")
    return n_disagree == 0


# ============================================================================
# Main: run cross-checks
# ============================================================================

if __name__ == '__main__':
    print("=" * 72)
    print("BDI quantum LR algorithm: cross-checks")
    print("=" * 72)
    print()

    ok3 = cross_check_B3(max_total=5)
    print()
    ok4 = cross_check_B4(max_total=4)
    print()

    if ok3 and ok4:
        print("ALL CROSS-CHECKS PASSED.")
    else:
        print("SOME CROSS-CHECKS FAILED.")
