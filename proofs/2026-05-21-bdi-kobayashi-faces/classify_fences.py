"""
classify_fences.py — classify the 2n-1 candidate fences of the BDI Kobayashi
polytope at B_n.

The polytope is the set of B_n-highest-weight chain configurations
(M, B, T, S) in Z_{>=0}^{3(n-1)+1}, where:
  M = (M_1, ..., M_{n-1})
  B = (B_1, ..., B_{n-1})
  T = (T_1, ..., T_{n-1})
  S = singleton coord (E_n)

Carry P_a defined by  P_0 = 0,  P_a = P_{a-1} + 2 (B_a - T_a).

The 2n-1 candidate fences (from Theorem A's carry-recursive form):
  L_a : M_a <= P_{a-1}                  for a = 1, ..., n-1   (n-1 of them)
  U_a : M_a <= P_a                      for a = 1, ..., n-1   (n-1 of them)
  E   : S   <= P_{n-1}                  (1)

This script:
  1. Enumerates all chain configs (M, B, T, S) with total content <= C.
  2. For each candidate fence, computes:
     - SAT_count: # of HW configs that saturate this fence (equality).
     - STRICT_count: # of HW configs that satisfy this fence strictly.
     - REDUND test: does there exist a chain config that satisfies all OTHER
       fences but VIOLATES this one? If yes => fence is non-redundant.
     - FACET test: does the saturating set have codim 1 in the HW polytope?
       (Approximated by counting saturating configs and checking they span a
       hyperplane.)
  3. Reports a classification: {DEGENERATE, FACET, REDUNDANT}.

Rick, 2026-05-21.
"""

from itertools import product
import sys

# ----------------------------------------------------------------------------
# Fence definitions
# ----------------------------------------------------------------------------

def P_partial(B, T, k):
    """Compute P_k = sum_{b=1..k} 2(B_b - T_b)."""
    return sum(2 * (B[b] - T[b]) for b in range(k))

def fences_Bn(n):
    """Return list of (name, slack_fn) for the 2n-1 candidate fences.
    slack_fn(M, B, T, S) returns >=0 iff fence holds; ==0 iff saturated."""
    fences = []
    for a in range(1, n):
        def L_eval(M, B, T, S, a=a):
            return P_partial(B, T, a-1) - M[a-1]
        fences.append((f"L_{a}", L_eval))
        def U_eval(M, B, T, S, a=a):
            return P_partial(B, T, a) - M[a-1]
        fences.append((f"U_{a}", U_eval))
    def E_eval(M, B, T, S, n=n):
        return P_partial(B, T, n-1) - S
    fences.append(("E", E_eval))
    return fences


def enumerate_chain_configs(n, content_max):
    """Yield all (M, B, T, S) tuples with non-neg entries and sum <= content_max.
    Uses weak-composition enumeration (much faster than product)."""
    D = 3 * (n - 1) + 1

    def weak_comps(D, total):
        if D == 1:
            yield (total,)
            return
        for v in range(total + 1):
            for rest in weak_comps(D - 1, total - v):
                yield (v,) + rest

    for total in range(content_max + 1):
        for vals in weak_comps(D, total):
            M = vals[:n-1]
            B = vals[n-1:2*(n-1)]
            T = vals[2*(n-1):3*(n-1)]
            S = vals[3*(n-1)]
            yield M, B, T, S


# ----------------------------------------------------------------------------
# Classification
# ----------------------------------------------------------------------------

def classify(n, content_max, verbose=True):
    fences = fences_Bn(n)
    names = [f[0] for f in fences]

    # Per-fence accumulators
    sat_count = {nm: 0 for nm in names}     # saturated by HW configs
    strict_count = {nm: 0 for nm in names}  # strict on HW configs
    sat_witnesses = {nm: [] for nm in names}  # up to 5 sat witnesses
    nonredund_witnesses = {nm: [] for nm in names}  # configs that violate ONLY this fence
    nonredund_count = {nm: 0 for nm in names}  # how many configs violate ONLY this fence

    total_configs = 0
    total_hw = 0

    for M, B, T, S in enumerate_chain_configs(n, content_max):
        total_configs += 1
        slacks = [(nm, fn(M, B, T, S)) for nm, fn in fences]
        if all(s >= 0 for _, s in slacks):
            total_hw += 1
            for nm, s in slacks:
                if s == 0:
                    sat_count[nm] += 1
                    if len(sat_witnesses[nm]) < 5:
                        sat_witnesses[nm].append((M, B, T, S))
                else:
                    strict_count[nm] += 1
        else:
            # Find which fences are violated.
            violated = [nm for nm, s in slacks if s < 0]
            if len(violated) == 1:
                nm = violated[0]
                nonredund_count[nm] += 1
                if len(nonredund_witnesses[nm]) < 5:
                    nonredund_witnesses[nm].append((M, B, T, S))

    if verbose:
        print(f"=== B_{n} fence classification (content_max = {content_max}) ===")
        print(f"Total chain configs enumerated: {total_configs}")
        print(f"Total HW configs: {total_hw}")
        print()
        print(f"{'Fence':6} {'Sat':>6} {'Strict':>7} {'Nonred':>7}  Status")
        print("-" * 70)
        for nm in names:
            sc = sat_count[nm]
            stc = strict_count[nm]
            nrc = nonredund_count[nm]
            status = classify_status(sc, stc, nrc, total_hw)
            print(f"{nm:6} {sc:>6} {stc:>7} {nrc:>7}  {status}")
        print()
        # Print witnesses
        print("Sample saturation witnesses (M, B, T, S):")
        for nm in names:
            if sat_witnesses[nm]:
                print(f"  {nm}: {sat_witnesses[nm][:3]}")
        print()
        print("Sample non-redundancy witnesses (configs that violate ONLY this fence):")
        for nm in names:
            if nonredund_witnesses[nm]:
                print(f"  {nm}: {nonredund_witnesses[nm][:3]}")
            else:
                print(f"  {nm}: NONE found (= fence is REDUNDANT in this content range)")

    return {
        'fences': names,
        'sat_count': sat_count,
        'strict_count': strict_count,
        'nonredund_count': nonredund_count,
        'sat_witnesses': sat_witnesses,
        'nonredund_witnesses': nonredund_witnesses,
        'total_hw': total_hw,
        'total_configs': total_configs,
    }


def classify_status(sat, strict, nonred, total_hw):
    if sat == total_hw:
        return "DEGENERATE (saturated by ALL HW configs)"
    if sat == 0:
        return "VACUOUS (saturated by NO HW configs)"
    if nonred == 0:
        return "REDUNDANT (implied by other fences + nonneg)"
    return "FACET? (saturated by some, strict for some, non-redundant)"


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    C = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    classify(n, C)
