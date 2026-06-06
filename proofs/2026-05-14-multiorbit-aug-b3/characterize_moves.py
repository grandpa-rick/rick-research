"""
For each of the 15 e_3^2 move types at B_3 (short simple, k=2), determine
the sub-slice (set of pi in S_3) on which e_3^2 acts as that specific move.

Aim: a clean characterization in terms of multiplicities (c_EP13, c_E1, c_EM13,
c_EP23, c_E2, c_EM23, c_E3) and the bracketing structure.
"""
import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47/coideal_check')

from b_i_b3 import (
    enumerate_partitions, eps_i, e_i_k, kp_repr,
    EM12, EM13, EM23, EP12, EP13, EP23, E1, E2, E3, ROOTS,
)
from collections import Counter, defaultdict


CHAIN_A_TOP = EP13
CHAIN_A_MID = E1
CHAIN_A_BOT = EM13
CHAIN_B_TOP = EP23
CHAIN_B_MID = E2
CHAIN_B_BOT = EM23
SINGLE_E3 = E3


def diff(pi_new, pi_old):
    d = {}
    for r in ROOTS:
        d[r] = pi_new.get(r, 0) - pi_old.get(r, 0)
    return tuple(sorted((r, c) for r, c in d.items() if c != 0))


# Name the 15 moves:
MOVE_NAMES = {
    # Pure chain A
    ((EP13, -1), (EM13, +1)): "A_TB",        # top-to-bottom (one swap)
    ((EP13, -2), (E1, +2)): "A_TM2",         # top-to-mid (twice)
    ((E1, -2), (EM13, +2)): "A_MB2",         # mid-to-bot (twice)
    # Pure chain B
    ((EP23, -1), (EM23, +1)): "B_TB",
    ((EP23, -2), (E2, +2)): "B_TM2",
    ((E2, -2), (EM23, +2)): "B_MB2",
    # Cross A+B (each: one chain primitive each)
    ((EP13, -1), (E1, +1), (EP23, -1), (E2, +1)): "AB_TT",   # A top-mid + B top-mid
    ((EP13, -1), (E1, +1), (E2, -1), (EM23, +1)): "AB_TM",   # A top-mid + B mid-bot
    ((E1, -1), (EM13, +1), (EP23, -1), (E2, +1)): "AB_MT",   # A mid-bot + B top-mid
    ((E1, -1), (EM13, +1), (E2, -1), (EM23, +1)): "AB_MM",   # A mid-bot + B mid-bot
    # Pure singleton
    ((E3, -2),): "E3_2",
    # Chain A + singleton
    ((EP13, -1), (E1, +1), (E3, -1)): "AE_T",
    ((E1, -1), (EM13, +1), (E3, -1)): "AE_M",
    # Chain B + singleton
    ((EP23, -1), (E2, +1), (E3, -1)): "BE_T",
    ((E2, -1), (EM23, +1), (E3, -1)): "BE_M",
}


def move_name(d):
    """Reorder tuple d to canonical form matching MOVE_NAMES keys, then look up."""
    # The keys in MOVE_NAMES are tuples of (root, delta) with the order I listed.
    # But `diff` returns sorted by root name. Let me build a lookup robustly.
    d_set = frozenset(d)
    for key, name in MOVE_NAMES.items():
        if frozenset(key) == d_set:
            return name
    return "UNKNOWN"


def main():
    MAX = 5
    print(f"Characterizing e_3^2 net moves on S_3 at B_3 (max_total={MAX})")
    print(f"Slice S_3 = {{pi : eps_3(pi) >= 2}}\n")
    move_to_pis = defaultdict(list)
    for pi in enumerate_partitions(MAX):
        if eps_i(pi, 3) < 2:
            continue
        e2 = e_i_k(pi, 3, 2)
        if e2 is None:
            continue
        d = diff(e2, pi)
        nm = move_name(d)
        move_to_pis[nm].append(pi)

    for nm in ['A_TB', 'A_TM2', 'A_MB2',
               'B_TB', 'B_TM2', 'B_MB2',
               'AB_TT', 'AB_TM', 'AB_MT', 'AB_MM',
               'E3_2', 'AE_T', 'AE_M', 'BE_T', 'BE_M']:
        pis = move_to_pis[nm]
        print(f"  Move {nm}: {len(pis)} partitions")
        # Find the structural characterization by examining the multiplicities
        chars = []
        for pi in pis[:5]:
            c = {r: pi.get(r, 0) for r in ROOTS}
            chars.append((c[EP13], c[E1], c[EM13],
                          c[EP23], c[E2], c[EM23],
                          c[E3], c[EM12], c[EP12]))
        for c in chars[:3]:
            print(f"    (cEP13,cE1,cEM13)=({c[0]},{c[1]},{c[2]}) "
                  f"(cEP23,cE2,cEM23)=({c[3]},{c[4]},{c[5]}) "
                  f"cE3={c[6]} (cEM12,cEP12)=({c[7]},{c[8]})")
        print()


if __name__ == "__main__":
    main()
