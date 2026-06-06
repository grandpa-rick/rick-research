"""
Compare total counts: |GSSOT| vs |Aug~ fixed points| vs total monomial count of KL(q,t).

CKL Theorem 4.6: KL(q,t) = sum_{T in GSSOT} energy_{q,t}(phi_c(T)).
Each summand is q^a t^b. So if all coefficients of KL are 0 or 1, then
|GSSOT| = total degree count = sum of coefficients.

For our 4 sample pairs we observed:
  Pair 1: KL = t + qt           -> sum of coefficients = 2
  Pair 2: KL = t^2 + qt^2 + q^2t^2  -> sum = 3
  Pair 3: KL = qt + qt^3 + q^2t + q^2t^3  -> sum = 4
  Pair 4: KL = t                -> sum = 1

And |GSSOT| was 2, 3, 4, ?
And |Aug~ fixed points| was 2, 3, 4, 1.

Verify: |GSSOT| = sum of coeffs = |Aug~ fixed points|.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/remark47')
sys.path.insert(0, '/home/agent/projects/proofs/remark47/route_A')

from fractions import Fraction
from gssot_b2 import all_gssot
from verify_kl_polynomial import compute_kl_qt_BGG


def main():
    F = Fraction
    pairs = [
        ((F(3, 2), F(1, 2)), (F(1, 2), F(1, 2)), 1, (1, 0), (1, 1)),
        ((F(5, 2), F(1, 2)), (F(1, 2), F(1, 2)), 2, (2, 0), (2, 2)),
        ((F(5, 2), F(3, 2)), (F(1, 2), F(1, 2)), 2, (1, 0), (2, 2)),
        ((F(3, 2), F(3, 2)), (F(3, 2), F(1, 2)), 2, (0, 0), (1, 1)),
        # Pair (3/2,3/2) μ=(3/2,1/2): integer λ=(1,1), μ=(1,0), g=1.
        # oc(λ, 1)=(0,0). ocBar(μ, 1)=(0, 1). NOT a partition target! oc has descending weight 0.
        # Use g=2: oc(λ, 2)=(1, 1). ocBar(μ, 2)=(1, 2). Hmm.
        # Actually oc = (g - λ_n, ..., g - λ_1). For λ=(1,1), oc = (g-1, g-1).
        # ocBar = (g - μ_1, g - μ_2). For μ=(1,0), ocBar = (g-1, g).
        ((F(7, 2), F(3, 2)), (F(3, 2), F(1, 2)), 3, (2, 0), (3, 3)),
    ]
    for lam, mu, g, shape, weight in pairs:
        # Compute KL
        coeffs = compute_kl_qt_BGG(lam, mu)
        total_coeffs = sum(coeffs.values())

        # Enumerate GSSOT
        Ts = all_gssot(shape, weight, n_parts=2, max_part=g)
        print(f"λ={lam}, μ={mu}: g={g}, shape={shape}, weight={weight}")
        print(f"  KL = {dict(coeffs)}")
        print(f"  sum of coeffs = {total_coeffs}")
        print(f"  |GSSOT| = {len(Ts)}")
        match = "✓" if len(Ts) == total_coeffs else "✗"
        print(f"  {match} match\n")


if __name__ == "__main__":
    main()
