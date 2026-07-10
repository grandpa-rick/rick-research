"""Day 87 evening stretch — Extract h_k^{(9)} for the v_2(c-1) >= 3 regime.

D1 at c=9 predicts Δβ'(9) = 1 − max(2, v_2(8)) = 1 − 3 = -2.
Empirical: β'(8) = 11, β'(9) = 9, so Δβ' = -2. ✓

At c=9 the polynomial fits are larger (h_0 total degree 16). Need many samples.
"""
import sys
sys.path.insert(0, '/home/agent/projects/code')

exec(open('/home/agent/projects/code/2026-07-09-hk-c67-fit.py').read().split('if __name__')[0])


if __name__ == "__main__":
    print("### c = 9 ###\n")
    res9 = fit_all_h_k(c_val=9, jmax=18, max_deg=16, sample_range=(9, 40))
