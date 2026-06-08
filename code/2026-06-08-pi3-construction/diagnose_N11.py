"""Diagnose: list ALL missing BDI points at N=11, 12, 13 under the full
55-piece v7 registry. Group by structural features."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from verify_full_v7 import ALL_PI, get_image, enumerate_bdi_n3
from collections import Counter


def all_missing(N):
    bdi_pts = enumerate_bdi_n3(N)
    union = set()
    for name in ALL_PI:
        img, _, _ = get_image(name, N)
        union |= img
    missing = bdi_pts - union
    return sorted(missing), len(bdi_pts)


def classify(q):
    _, M_2, B_1, T_1, B_2, T_2, S = q
    flags = []
    if B_2 == T_2:
        flags.append("B2=T2")
    if T_1 == 0 and T_2 == 0:
        flags.append("T=0")
    # ratio
    g = 0
    if T_1 > 0 and T_2 > 0:
        # primitive ratio
        from math import gcd
        g = gcd(T_1, T_2)
        flags.append(f"T1:T2={T_1//g}:{T_2//g}")
    P_1 = 2 * (B_1 - T_1)
    P_2 = P_1 + 2 * (B_2 - T_2)
    if M_2 == P_1:
        flags.append("M2=P1")
    if S == P_2:
        flags.append("S=P2")
    if S > P_1 and B_2 - T_2 > 0:
        flags.append("S-uses-L2")
    return " ".join(flags)


def main():
    for N in [11, 12, 13]:
        miss, total = all_missing(N)
        print(f"\n=== N={N}: {len(miss)}/{total} missing ===")
        feats = Counter()
        for q in miss:
            feats[classify(q)] += 1
        print("Feature counts:")
        for f, k in feats.most_common():
            print(f"  {k:4d}  [{f}]")
        print(f"\nFirst 25 missing:")
        for q in miss[:25]:
            _, M_2, B_1, T_1, B_2, T_2, S = q
            P_1 = 2*(B_1-T_1); P_2 = P_1 + 2*(B_2-T_2)
            print(f"  M2={M_2} B1={B_1} T1={T_1} B2={B_2} T2={T_2} S={S}  "
                  f"P_1={P_1} P_2={P_2}  [{classify(q)}]")


if __name__ == "__main__":
    main()
