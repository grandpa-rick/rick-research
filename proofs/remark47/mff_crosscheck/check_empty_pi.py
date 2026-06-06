"""Check what Rick's Section 3 expansion gives for pi=empty, the MFF/highest-weight case."""
import sys, os
sys.path.insert(0, '/home/agent/projects/proofs/remark47')
import section3_sign_tracking_C3 as S3

# pi = empty Kostant partition (just the highest weight vector)
pi_empty = {}
for (kind, i) in [('S', 0), ('S', 1), ('L', 2)]:
    for c in [1, 2]:
        alpha = S3.SIMPLES[(kind, i)]
        try:
            result = S3.expand_alpha_c_times_pi(alpha, c, pi_empty)
        except Exception as e:
            print(f"  ERROR: {e}")
            continue
        print(f"({kind},{i}) alpha={alpha} c={c}:")
        for key, coeff in result.items():
            print(f"  pi' = {dict(key)}  coeff = {S3.sp.expand(coeff)}")
        print()
