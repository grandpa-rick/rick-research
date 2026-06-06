"""
probe_pnu_b2.py — Probe whether the abstract orthogonal projection
p_ν : V(ν) → V^ı_BDI(ν) factors over Rick's chain-factor decomposition
Kp(∞)|_{B_2} ≅ C_1 ⊗ C_sing.

Author: prove/compute agent, Day 25 (2026-05-20).

Setup (per 2026-05-19-bdi-watanabe-template-W.md, Verdict W):

  * The chain-factor PBW basis E_π is orthogonal under the Kashiwara/Lusztig
    form (Lusztig [Lus93] §38.2 — Lusztig PBW orthogonality), with diagonal
    entries D_π in 1 + q^{-1/2} Z[[q^{-1/2}]] (almost-orthonormal).

  * The U^ı_BDI-submodule V^ı_BDI(ν) ⊂ V(ν) is spanned (per the chain-factor
    framework and Watanabe 2407 §5) by the PBW vectors E_π for π that are
    B_n-highest (eps_n(π) = 0).

  * The orthogonal projection p_ν : V(ν) → V^ı_BDI(ν) is then, on the PBW
    basis,
        p_ν(E_π) = [π is B_n-HW and wt(π) = ν] · E_π.
    (The form is diagonal ⇒ orthogonal projection onto a basis-spanned
    subspace is the basis-truncation projection.)

For the factoring question: under Kp(∞)|_{B_2} ≅ C_1 ⊗ C_sing, the PBW
basis factors as E_π = E_{(M_1, B_1, T_1)} ⊗ E_S (call these
e_a ⊗ e_s). We test whether p_ν acts as p_1 ⊗ p_sing for some operators
p_1 on C_1, p_sing on C_sing.

The B_2-highest condition at weight ν is:
  (HW_1):   M_1 ≤ 0  AND  M_1 + 2 T_1 ≤ 2 B_1.    [pure-C_1]
  (HW_sing): S ≤ 2(B_1 - T_1) = P_1.              [CROSS-FACTOR]

The cross-factor (HW_sing) is the structural obstruction to factoring: the
allowed set of (M_1, B_1, T_1, S) is not a product set — the bound on S
depends on (B_1, T_1).

This script:

  1. Enumerates the catalog at B_2 (content ≤ 4, 70 configs total).
  2. For each Kp weight ν, computes V(ν) as the span of PBW vectors of
     that weight, identifies V^ı_BDI(ν) by the B_2-highest test, and
     computes the projection p_ν as the basis-truncation projector.
  3. Tests whether p_ν = p_1 ⊗ p_sing for ANY choice of p_1 on C_1, p_sing
     on C_sing.  This is checked by extracting the "characteristic function"
     of the allowed set in (M_1, B_1, T_1, S) and asking whether it
     factors as (chain-indicator)(sing-indicator).

  4. If it doesn't factor as a tensor product of indicators (which is the
     direct consequence of the form being diagonal), record the obstruction.

This probe answers the LITERAL question P1/¬P1 from the connection note.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
from bdi_qLR import is_Bn_highest

from collections import defaultdict
from itertools import product


N = 2  # B_2 throughout

# ----------------------------------------------------------------------
# Step 1: enumerate the catalog (content ≤ 4 ⇒ 70 configs, per Day-19 prior)
# ----------------------------------------------------------------------

def enumerate_b2_catalog(max_content=4):
    """Enumerate all chain+sing configurations (M_1, B_1, T_1, S) with
    M_1 + B_1 + T_1 + S ≤ max_content. Returns a list of (M, B, T, S)
    tuples (with M, B, T being length-1 tuples for B_2)."""
    configs = []
    for total in range(max_content + 1):
        for M1 in range(total + 1):
            for B1 in range(total - M1 + 1):
                for T1 in range(total - M1 - B1 + 1):
                    S = total - M1 - B1 - T1
                    if S < 0:
                        continue
                    M, B, T = (M1,), (B1,), (T1,)
                    configs.append((M, B, T, S))
    return configs


# ----------------------------------------------------------------------
# Step 2: bucket by Kp weight ν.
# ----------------------------------------------------------------------

def kp_weight_b2(M, B, T, S):
    """Compute the Kp weight ν = ν_1 E_1 + ν_2 E_2 of (M, B, T, S) at B_2.
    Recall: chain root multiplicities contribute:
        E_1 (mid)     : (+E_1)
        E_1 - E_2 (bot): (+E_1, -E_2)
        E_1 + E_2 (top): (+E_1, +E_2)
        E_2 (sing)    : (+E_2)
    So:
        ν_1 = M_1 + B_1 + T_1
        ν_2 = S - B_1 + T_1
    """
    nu1 = M[0] + B[0] + T[0]
    nu2 = S - B[0] + T[0]
    return (nu1, nu2)


def bucket_by_weight(configs):
    """Bucket configs by their Kp weight."""
    buckets = defaultdict(list)
    for cfg in configs:
        nu = kp_weight_b2(*cfg)
        buckets[nu].append(cfg)
    return buckets


# ----------------------------------------------------------------------
# Step 3: for each ν, identify V^ı_BDI(ν) = span of B_2-HW vectors and
# compute the projection p_ν as the basis-truncation projector.
#
# Since the Gram matrix is diagonal (Lusztig PBW orthogonality, Verdict W),
# the orthogonal projection of E_π is:
#   p_ν(E_π) = [π in V^ı_BDI(ν)] · E_π = [π is B_2-HW] · E_π    (for wt = ν)
#
# Test factoring: does there exist a function f on C_1-coords and g on
# S such that the B_2-HW indicator equals f(M_1, B_1, T_1) · g(S)?
# Equivalently: does the allowed set
#   A(ν) = {(M_1, B_1, T_1, S) : weight = ν, B_2-HW}
# factor as A_chain(ν) × A_sing(ν)?
# ----------------------------------------------------------------------

def analyze_weight(nu, configs_at_nu):
    """For a given weight ν and the list of all configs of that weight,
    determine V(ν)'s basis, identify V^ı_BDI(ν), and test factoring."""
    # All basis vectors of V(ν):
    basis = configs_at_nu
    # Identify which are in V^ı_BDI(ν) (B_2-HW):
    is_hw = {cfg: is_Bn_highest(*cfg, N) for cfg in basis}
    hw_set = {cfg for cfg, h in is_hw.items() if h}

    # Project to chain-coords and sing-coord:
    chain_coords = sorted({(cfg[0][0], cfg[1][0], cfg[2][0]) for cfg in basis})
    sing_coords = sorted({cfg[3] for cfg in basis})

    # Build characteristic function χ: (chain, sing) -> {0, 1} on the
    # ν-weight slice.
    chi = {}
    for cfg in basis:
        c = (cfg[0][0], cfg[1][0], cfg[2][0])
        s = cfg[3]
        chi[(c, s)] = 1 if cfg in hw_set else 0

    # Test whether χ factors as f(c) · g(s).
    #
    # If χ factors, then for every two (c, s) and (c', s') in the support
    # of basis, χ(c, s) · χ(c', s') = χ(c, s') · χ(c', s). This is the
    # "rectangle test" — the indicator of a Cartesian product set is
    # exactly the set of functions for which the rectangle test holds.

    # Equivalent for indicators: the support of χ is the Cartesian
    # product of its projections to (c, ·) and (·, s) intersected with
    # the available (c, s) pairs of weight ν.

    factor_ok = True
    rectangle_fail = None
    basis_pairs = [(c, s) for c, s in chi.keys()]
    for i, (c1, s1) in enumerate(basis_pairs):
        for (c2, s2) in basis_pairs[i+1:]:
            # Check whether (c1, s2) and (c2, s1) are in the basis (else
            # the rectangle test is vacuous).
            if (c1, s2) in chi and (c2, s1) in chi:
                lhs = chi[(c1, s1)] * chi[(c2, s2)]
                rhs = chi[(c1, s2)] * chi[(c2, s1)]
                # For an indicator product χ(c, s) = f(c) g(s), we need
                # χ(c1, s1) χ(c2, s2) = χ(c1, s2) χ(c2, s1) as integers.
                # But for indicators of products, both sides are 0 or 1.
                # The rectangle test for set-indicators is exactly:
                #   if χ(c1, s1) = 1 and χ(c2, s2) = 1, then both
                #   χ(c1, s2) and χ(c2, s1) must be 1.
                if chi[(c1, s1)] == 1 and chi[(c2, s2)] == 1:
                    if chi[(c1, s2)] == 0 or chi[(c2, s1)] == 0:
                        factor_ok = False
                        rectangle_fail = ((c1, s1), (c2, s2), (c1, s2), (c2, s1),
                                          chi[(c1, s2)], chi[(c2, s1)])
                        break
        if not factor_ok:
            break

    return {
        'nu': nu,
        'basis_size': len(basis),
        'hw_count': len(hw_set),
        'factor_ok': factor_ok,
        'rectangle_fail': rectangle_fail,
        'hw_set': hw_set,
        'chi': chi,
    }


# ----------------------------------------------------------------------
# Step 4: stronger test — for the diagonal-form projection p_ν, also test
# whether the projection is a TENSOR PRODUCT OF LINEAR MAPS, not just of
# indicators. p_ν = p_1 ⊗ p_sing means for ALL (c, s), (c', s'):
#   <p_ν(e_c ⊗ e_s), e_{c'} ⊗ e_{s'}> = <p_1(e_c), e_{c'}> · <p_sing(e_s), e_{s'}>
# When p_ν is the basis-truncation operator (orthogonal projector with
# diagonal Gram), the LHS is D_{(c,s)} · χ(c, s) · δ_{(c,s), (c',s')}
# (where χ is the B_2-HW indicator and D is the diagonal Gram entry).
#
# For this to factor as a tensor product of linear maps on the chain and
# sing pieces, we need the matrix χ to factor as an outer product up to
# a per-basis-vector scaling D — and the scaling D itself must factor
# across chain and sing (which Lusztig diagonal does, since it's a
# product over chain factors and the singleton).
#
# So the WHOLE question reduces to whether χ factors. We do that test
# above. If it doesn't factor → ¬P1.
# ----------------------------------------------------------------------

def report_factoring(max_content=4):
    print("=" * 76)
    print(f"PROBE: does p_ν factor as p_1 ⊗ p_sing at B_2?")
    print(f"Catalog: content ≤ {max_content}")
    print("=" * 76)
    print()

    configs = enumerate_b2_catalog(max_content)
    print(f"Total catalog entries (chain+sing configs): {len(configs)}")
    buckets = bucket_by_weight(configs)
    print(f"Total Kp weights: {len(buckets)}")
    print()

    all_factor = True
    obstructions = []
    weights_with_hw = 0
    weights_factor = 0
    weights_no_hw = 0

    # Sort weights for stable output
    sorted_weights = sorted(buckets.keys(),
                            key=lambda nu: (sum(abs(x) for x in nu), nu))

    print(f"{'ν':>10} {'|basis|':>7} {'|HW|':>5} {'factors?':>9}  details")
    print("-" * 76)
    for nu in sorted_weights:
        configs_at_nu = buckets[nu]
        result = analyze_weight(nu, configs_at_nu)
        bs = result['basis_size']
        hw = result['hw_count']
        ok = result['factor_ok']
        nu_str = f"({nu[0]},{nu[1]})"
        if hw == 0:
            tag = " --"
            weights_no_hw += 1
        elif ok:
            tag = "yes"
            weights_factor += 1
            weights_with_hw += 1
        else:
            tag = "NO"
            all_factor = False
            weights_with_hw += 1
            obstructions.append(result)
        details = ""
        if not ok and result['rectangle_fail']:
            (c1, s1), (c2, s2), (c1s2), (c2s1), v12, v21 = result['rectangle_fail']
            details = (f" rect fail: ({c1},{s1})∧({c2},{s2})=1 but "
                       f"({c1},{s2})={v12}, ({c2},{s1})={v21}")
        print(f"{nu_str:>10} {bs:>7d} {hw:>5d} {tag:>9}{details}")

    print()
    print("=" * 76)
    print(f"Summary: {weights_factor}/{weights_with_hw} weights with HW factor; "
          f"{weights_no_hw} weights have empty HW (vacuous).")
    if all_factor:
        print("(P1) VERDICT: all V^ı_BDI(ν) factor as products at B_2.")
    else:
        print(f"(¬P1) VERDICT: factoring FAILS at {len(obstructions)} weights.")
        print()
        print("Sample obstruction(s):")
        for ob in obstructions[:5]:
            nu = ob['nu']
            (c1, s1), (c2, s2), (c1_s2), (c2_s1), v12, v21 = ob['rectangle_fail']
            print(f"  ν = {nu}:")
            print(f"    Rectangle: ((M,B,T)={c1}, S={s1}) and ((M,B,T)={c2}, S={s2}) BOTH B_2-HW (= 1)")
            print(f"    But ((M,B,T)={c1}, S={s2}) HW={v12}  &  ((M,B,T)={c2}, S={s1}) HW={v21}")
            print(f"    ⇒ indicator does not factor → p_ν has cross-chain entry.")
    print("=" * 76)
    return all_factor, obstructions


# ----------------------------------------------------------------------
# Inspect: identify the structural cause (the (HW_sing) carry coupling)
# ----------------------------------------------------------------------

def diagnose_carry_coupling():
    print()
    print("=" * 76)
    print("DIAGNOSIS — Source of cross-chain coupling")
    print("=" * 76)
    print()
    print("Theorem A (Day 18, bdi_qLR.md) gives the B_2-highest test:")
    print("  (HW_1):    M_1 = 0  AND  T_1 ≤ B_1.            [pure-C_1]")
    print("  (HW_sing): S ≤ P_1 = 2(B_1 - T_1).             [CROSS-FACTOR]")
    print()
    print("The bound on S depends on (B_1, T_1) — components of C_1 —")
    print("so the B_2-HW condition is NOT a product condition.")
    print()
    print("Concrete witness at the smallest ν where the failure shows up:")
    print()
    # Look for the minimal weight where chi has a rectangle obstruction.
    configs = enumerate_b2_catalog(4)
    buckets = bucket_by_weight(configs)
    for nu in sorted(buckets.keys(), key=lambda x: (sum(abs(z) for z in x), x)):
        cfgs = buckets[nu]
        result = analyze_weight(nu, cfgs)
        if not result['factor_ok']:
            print(f"  ν = {nu}, basis size {result['basis_size']}, "
                  f"HW count {result['hw_count']}:")
            print(f"  Allowed (B_2-HW) (M_1, B_1, T_1, S):")
            for cfg in sorted(result['hw_set']):
                M, B, T, S = cfg
                P1 = 2 * (B[0] - T[0])
                print(f"    M={M[0]}, B={B[0]}, T={T[0]}, S={S} "
                      f"(P_1={P1}; HW_sing requires S ≤ {P1})")
            (c1, s1), (c2, s2), (c1_s2), (c2_s1), v12, v21 = result['rectangle_fail']
            print(f"  Rectangle witnesses BOTH B_2-HW:")
            print(f"    A = ((M,B,T)={c1}, S={s1})")
            print(f"    B = ((M,B,T)={c2}, S={s2})")
            print(f"  Swap-partners (would have to also be B_2-HW for factoring):")
            print(f"    A' = ((M,B,T)={c1}, S={s2}):  B_2-HW? {bool(v12)}")
            print(f"    B' = ((M,B,T)={c2}, S={s1}):  B_2-HW? {bool(v21)}")
            print()
            break


if __name__ == '__main__':
    all_factor, obstructions = report_factoring(max_content=4)
    diagnose_carry_coupling()
    print()
    if all_factor:
        print("FINAL: P1 — p_ν factors at B_2 (catalog content ≤ 4).")
    else:
        print(f"FINAL: ¬P1 — p_ν does NOT factor at B_2.")
        print(f"       {len(obstructions)} weight(s) exhibit cross-chain obstruction.")
        print(f"       Root cause: (HW_sing) carry coupling S ≤ 2(B_1 - T_1).")
