"""inspect_nontrivial.py — Look at the weights where HW count ≥ 2 and
verify the rectangle test logic explicitly. Also test larger content."""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
from bdi_qLR import is_Bn_highest

from collections import defaultdict


def enumerate_b2_catalog(max_content):
    configs = []
    for total in range(max_content + 1):
        for M1 in range(total + 1):
            for B1 in range(total - M1 + 1):
                for T1 in range(total - M1 - B1 + 1):
                    S = total - M1 - B1 - T1
                    if S < 0:
                        continue
                    configs.append(((M1,), (B1,), (T1,), S))
    return configs


def kp_weight_b2(M, B, T, S):
    nu1 = M[0] + B[0] + T[0]
    nu2 = S - B[0] + T[0]
    return (nu1, nu2)


def analyze_factoring(buckets, label):
    print(f"\n=== {label} ===")
    multi_hw_weights = []
    failures = []
    for nu, cfgs in sorted(buckets.items(), key=lambda x: (sum(abs(z) for z in x[0]), x[0])):
        hw = [cfg for cfg in cfgs if is_Bn_highest(*cfg, 2)]
        if len(hw) < 2:
            continue
        multi_hw_weights.append((nu, len(cfgs), len(hw)))
        # Project to (chain, sing) coords
        chi = {}
        for cfg in cfgs:
            c = (cfg[0][0], cfg[1][0], cfg[2][0])
            s = cfg[3]
            chi[(c, s)] = 1 if cfg in hw else 0
        # Find HW pairs and test rectangle
        hw_pairs = [(cfg[0][0], cfg[1][0], cfg[2][0], cfg[3]) for cfg in hw]
        bad = False
        details = ""
        for i, (m1, b1, t1, s1) in enumerate(hw_pairs):
            for j, (m2, b2, t2, s2) in enumerate(hw_pairs):
                if i == j: continue
                c1 = (m1, b1, t1); c2 = (m2, b2, t2)
                # Rectangle partners: (c1, s2) and (c2, s1)
                # Are they in the basis (weight = ν)?
                if (c1, s2) in chi and (c2, s1) in chi:
                    if chi[(c1, s2)] == 0 or chi[(c2, s1)] == 0:
                        bad = True
                        details = (f"HW: (M={m1},B={b1},T={t1},S={s1}) & "
                                   f"(M={m2},B={b2},T={t2},S={s2}); "
                                   f"swap (c={c1},S={s2})HW={bool(chi[(c1,s2)])}, "
                                   f"(c={c2},S={s1})HW={bool(chi[(c2,s1)])}")
                        break
            if bad:
                break
        print(f"  ν={nu}: |basis|={len(cfgs)}, |HW|={len(hw)}, "
              f"factors={'NO' if bad else 'yes'}")
        if bad:
            print(f"    obstruction: {details}")
            failures.append((nu, details))
        else:
            for (m, b, t, s) in hw_pairs:
                print(f"    HW: M={m}, B={b}, T={t}, S={s}")
    return multi_hw_weights, failures


# Run at content ≤ 4
configs4 = enumerate_b2_catalog(4)
buckets4 = defaultdict(list)
for cfg in configs4:
    buckets4[kp_weight_b2(*cfg)].append(cfg)
multi4, fail4 = analyze_factoring(buckets4, "content ≤ 4 (70 configs)")

# Run at content ≤ 6
configs6 = enumerate_b2_catalog(6)
buckets6 = defaultdict(list)
for cfg in configs6:
    buckets6[kp_weight_b2(*cfg)].append(cfg)
multi6, fail6 = analyze_factoring(buckets6, "content ≤ 6 (larger catalog)")

# Run at content ≤ 8
configs8 = enumerate_b2_catalog(8)
buckets8 = defaultdict(list)
for cfg in configs8:
    buckets8[kp_weight_b2(*cfg)].append(cfg)
multi8, fail8 = analyze_factoring(buckets8, "content ≤ 8 (extensive)")

print()
print("="*60)
print(f"content ≤ 4: {len(multi4)} weights with |HW|≥2, {len(fail4)} fail factoring")
print(f"content ≤ 6: {len(multi6)} weights with |HW|≥2, {len(fail6)} fail factoring")
print(f"content ≤ 8: {len(multi8)} weights with |HW|≥2, {len(fail8)} fail factoring")
