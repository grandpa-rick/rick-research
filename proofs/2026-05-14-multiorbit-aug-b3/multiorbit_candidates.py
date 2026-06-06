"""
Test candidate multi-orbit Aug~_3 definitions for commutativity with B_3 on the slice.

Candidates:
  C1: Aug~^sum := Aug~_{3,1} + Aug~_{3,2} (linear combination).
  C2: Aug~^sum + E3-decrement when c_E3 > 0 sub-orbit.
  C3: Aug~^sum + correction by "second-chain term" when both orbits available.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from b_i_b3 import (
    enumerate_partitions, eps_i, e_i_k, e_i, f_i, kp_clean, kp_repr, kp_add, kp_key,
    EM12, EM13, EM23, EP12, EP13, EP23, E1, E2, E3, ROOTS,
    LinComb, apply_e, apply_f, apply_B, aug_e_chain,
)
from collections import Counter, defaultdict


# -----------------------------------------------------------------
# Candidate 1: simple sum
# -----------------------------------------------------------------
def aug_sum(pi):
    """Aug~^sum(pi) := Aug~_{3,1}(pi) + Aug~_{3,2}(pi).
    Returns a LinComb."""
    result = LinComb.zero()
    a1 = aug_e_chain(pi, 3, '1')
    a2 = aug_e_chain(pi, 3, '2')
    if a1 is not None:
        result = result + LinComb.from_kp(a1)
    if a2 is not None:
        result = result + LinComb.from_kp(a2)
    return result


def apply_aug_sum(lc):
    """Apply Aug~^sum to a LinComb termwise."""
    out = LinComb.zero()
    for k, (pi, coeff) in lc.terms.items():
        out = out + coeff * aug_sum(pi)
    return out


def commutator_aug_sum(pi):
    """[Aug~^sum, B_3] pi = Aug~^sum(B_3 pi) - B_3(Aug~^sum pi)."""
    pi_lc = LinComb.from_kp(pi)
    B_pi = apply_B(pi_lc, 3)
    Aug_B_pi = apply_aug_sum(B_pi)
    Aug_pi = aug_sum(pi)
    B_Aug_pi = apply_B(Aug_pi, 3)
    return Aug_B_pi - B_Aug_pi


# -----------------------------------------------------------------
# Test framework
# -----------------------------------------------------------------
def test_candidate_on_slice(commutator_fn, max_total=4, name='?'):
    print(f"\n=== Candidate '{name}' on slice S_3 (eps_3 >= 2) ===")
    n_total = 0
    n_zero = 0
    failures = defaultdict(int)
    failure_examples = defaultdict(list)
    for pi in enumerate_partitions(max_total):
        if eps_i(pi, 3) < 2:
            continue
        n_total += 1
        comm = commutator_fn(pi)
        if comm.is_zero():
            n_zero += 1
        else:
            # Tag by which terms remain
            tag = frozenset((r, c) for r, c in
                            [(kp_repr(p), cf) for k, (p, cf) in comm.terms.items()])
            failures[len(comm.terms)] += 1
            if len(failure_examples[len(comm.terms)]) < 3:
                failure_examples[len(comm.terms)].append((pi, comm))
    print(f"  on-slice tested: {n_total}, commutator=0: {n_zero}, failed: {n_total - n_zero}")
    for k in sorted(failures.keys()):
        print(f"    failures with {k} terms in comm: {failures[k]}")
        for pi, comm in failure_examples[k][:1]:
            print(f"      e.g. pi = {kp_repr(pi)}")
            print(f"           [Aug,B]pi = {comm}")
    return n_total, n_zero


def main():
    MAX = 4
    test_candidate_on_slice(commutator_aug_sum, MAX, name='C1 sum')


if __name__ == "__main__":
    main()
