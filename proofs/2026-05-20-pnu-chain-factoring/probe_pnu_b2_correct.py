"""
probe_pnu_b2_correct.py — CORRECTED probe. The chain-factor tensor
decomposition is Kp(∞)|_{B_2} ≅ C_1 ⊗ C_sing, which is a decomposition
OF THE WHOLE Kp(∞), not within a fixed weight ν. The projection
p : Kp(∞) → ⊕_ν V^ı_BDI(ν) factors as p_1 ⊗ p_sing iff the indicator
[π is B_2-HW] factors as f(M_1, B_1, T_1) · g(S) over the WHOLE
catalog.

This script does the corrected factoring test.

Setup:
  C_1 has basis indexed by (M_1, B_1, T_1) ∈ Z_{≥0}^3.
  C_sing has basis indexed by S ∈ Z_{≥0}.
  Kp(∞)|_{B_2} basis: pairs ((M_1, B_1, T_1), S).

Projection p : Kp(∞) → "B_2-HW subspace" is the basis-truncation
projector with indicator χ((M, B, T), S) = [B_2-HW(M, B, T, S)].

p factors as p_1 ⊗ p_sing iff p_1 is a projector on C_1 and p_sing
is a projector on C_sing such that
  χ((M, B, T), S) = χ_1(M, B, T) · χ_sing(S)
for some indicators χ_1, χ_sing.

Equivalently: the set of B_2-HW configs is a Cartesian product
A × B with A ⊂ C_1-coords, B ⊂ C_sing-coords.

We test this directly.
"""

import sys
sys.path.insert(0, '/home/agent/projects/proofs/2026-05-18-bdi-qLR')
from bdi_qLR import is_Bn_highest


def enumerate_b2_pairs(max_content):
    """All ((M, B, T), S) with M+B+T+S ≤ max_content."""
    pairs = []
    for total in range(max_content + 1):
        for M in range(total + 1):
            for B in range(total - M + 1):
                for T in range(total - M - B + 1):
                    S = total - M - B - T
                    pairs.append(((M, B, T), S))
    return pairs


def test_global_factoring(max_content):
    """Test whether the B_2-HW indicator factors as f(M, B, T) · g(S)
    across the WHOLE catalog of content ≤ max_content."""
    print(f"\n=== Global factoring test, content ≤ {max_content} ===")
    pairs = enumerate_b2_pairs(max_content)
    is_hw = {p: is_Bn_highest((p[0][0],), (p[0][1],), (p[0][2],), p[1], 2)
             for p in pairs}

    # Collect HW pairs
    hw_set = {p for p in pairs if is_hw[p]}
    print(f"  Total pairs (catalog size): {len(pairs)}")
    print(f"  B_2-HW pairs: {len(hw_set)}")

    # Project to each factor
    A_chain = sorted({c for (c, s) in hw_set})       # chain coords that appear in any HW
    B_sing = sorted({s for (c, s) in hw_set})        # sing coords that appear in any HW
    print(f"  Chain coords appearing in HW: {len(A_chain)}")
    print(f"  Sing coords appearing in HW: {sorted(B_sing)}")

    # If HW = A × B, then for every (c ∈ A_chain, s ∈ B_sing) WITHIN the
    # catalog (M+B+T+S ≤ max_content), (c, s) must be B_2-HW.
    failures = []
    for c in A_chain:
        for s in B_sing:
            M, B, T = c
            total = M + B + T + s
            if total > max_content:
                # Not in the catalog at this content cap — skip
                continue
            if (c, s) not in hw_set:
                # (c, s) is in the catalog but NOT B_2-HW — failure!
                failures.append((c, s))

    if not failures:
        print(f"  → A_chain × B_sing ⊂ HW : check on catalog passes ({len(A_chain)*len(B_sing)} pairs).")
        # Now also need that HW ⊂ A_chain × B_sing — this is by construction.
        # Check that the chain×sing product really IS the HW set:
        # In the catalog, for every (c ∈ A_chain, s ∈ B_sing) with total ≤ max_content, (c,s) is HW.
        # Conversely every HW pair lies in A_chain × B_sing trivially.
        print(f"  ⇒ B_2-HW factors as a Cartesian product on the catalog!")
        return True, [], A_chain, B_sing
    else:
        print(f"  → FACTORING FAILS: {len(failures)} (c, s) ∈ A_chain × B_sing but NOT B_2-HW")
        for c, s in failures[:5]:
            M, B, T = c
            P1 = 2 * (B - T)
            print(f"    c=(M={M},B={B},T={T}), s={s}: "
                  f"NOT HW. (HW_sing demands S ≤ {P1}; here S={s})")
        return False, failures, A_chain, B_sing


def explain_HW_set():
    """Look at the structure of HW configs at B_2.

    Theorem A reduces (HW_1) at B_2 to: M_1 = 0 AND T_1 ≤ B_1.
    (HW_sing) at B_2: S ≤ 2(B_1 - T_1).

    Let's see: the chain HW condition is M_1 = 0, T_1 ≤ B_1 — pure chain.
    For factoring to hold over ALL of Kp(∞), we'd need a sing-only condition
    too (not depending on B_1, T_1).

    But (HW_sing) has S ≤ 2(B_1 - T_1) which DOES depend on chain coords.

    So unless we're constrained to specific values of (B_1, T_1), the factoring
    cannot hold globally. The minimal failure: any HW config with B_1 - T_1 > 0
    allows some S > 0, but pairing that S with a HW chain having B_1 = T_1
    forces S ≤ 0, breaking factoring.
    """
    print()
    print("=== Structural analysis ===")
    print("Theorem A (B_2):")
    print("  (HW_1):    M_1 = 0  AND  T_1 ≤ B_1.   [pure C_1 condition]")
    print("  (HW_sing): S ≤ 2(B_1 - T_1) = P_1.    [DEPENDS ON B_1, T_1]")
    print()
    print("If HW = A_chain × A_sing for some A_chain ⊂ C_1, A_sing ⊂ N, then")
    print("the upper bound on S must be uniform across A_chain.")
    print("But P_1 = 2(B_1 - T_1) varies: e.g., B_1=T_1=1 gives P_1=0 (only S=0),")
    print("while B_1=2, T_1=0 gives P_1=4 (S ∈ {0,1,2,3,4}).")
    print()
    print("Concrete cross-chain obstruction:")
    print("  chain c_a := (M=0, B=1, T=1):  ALLOWED S values: {0} (P_1=0).")
    print("  chain c_b := (M=0, B=2, T=0):  ALLOWED S values: {0,1,2,3,4} (P_1=4).")
    print()
    print("Both c_a and c_b are B_2-HW for S=0.")
    print("(c_a, S=2): is it B_2-HW? M=0,B=1,T=1,S=2.  P_1 = 2(1-1) = 0, S=2 > 0 → NOT HW.")
    print("(c_b, S=2): is it B_2-HW? M=0,B=2,T=0,S=2.  P_1 = 2(2-0) = 4, S=2 ≤ 4 → HW.")
    print()
    print("If HW factored as A_chain × A_sing, then S=2 ∈ A_sing (witnessed by c_b)")
    print("AND c_a ∈ A_chain (witnessed by S=0), so (c_a, S=2) ∈ A_chain × A_sing.")
    print("But (c_a, S=2) is NOT B_2-HW. → CONTRADICTION.")
    print()
    print("⇒ HW does NOT factor as a Cartesian product across Kp(∞).")
    print("⇒ p_ν does NOT factor as p_1 ⊗ p_sing globally.")


def per_weight_analysis():
    """For each weight ν at B_2, check ALSO whether p_ν restricted to V(ν)
    factors as a tensor product across the splitting of V(ν) under chain
    coords. (This is a weaker question: per-weight factoring.)"""
    from collections import defaultdict
    print()
    print("=== Per-weight analysis (weaker question) ===")
    pairs = enumerate_b2_pairs(4)
    is_hw = {p: is_Bn_highest((p[0][0],), (p[0][1],), (p[0][2],), p[1], 2)
             for p in pairs}
    buckets = defaultdict(list)
    for p in pairs:
        M, B, T = p[0]; S = p[1]
        nu = (M+B+T, S-B+T)
        buckets[nu].append(p)
    print(f"  {len(buckets)} weights in catalog (content ≤ 4)")
    print()
    print(f"  Crucial observation: at fixed ν = (ν_1, ν_2), the basis is")
    print(f"  parametrized by (M, B, T) — given the chain coord, S is")
    print(f"  determined by S = ν_2 - T + B. So V(ν) doesn't have an")
    print(f"  independent chain × sing tensor decomposition; the factoring")
    print(f"  question reduces to the global Kp(∞) one.")
    print()
    print(f"  Therefore the per-weight rectangle tests are vacuous (no two")
    print(f"  basis pairs share a chain or sing coord within a single weight).")


if __name__ == '__main__':
    print("=" * 76)
    print("PROBE (corrected): does p factor as p_1 ⊗ p_sing globally?")
    print("=" * 76)
    explain_HW_set()
    print()
    for M in [4, 5, 6, 8]:
        ok, failures, A, B = test_global_factoring(M)
    per_weight_analysis()
    print()
    print("=" * 76)
    print("FINAL VERDICT")
    print("=" * 76)
    print()
    if not ok:
        print("¬P1 — p does NOT factor as p_1 ⊗ p_sing at B_2.")
        print()
        print("Root cause: the B_2-highest condition (HW_sing): S ≤ 2(B_1 - T_1)")
        print("            couples the singleton bound to the chain coords.")
        print("            The B_2-HW set is NOT a Cartesian product A × B")
        print("            in C_1-coords × C_sing-coords.")
        print()
        print("Implication: p_ν has a cross-chain term tracking the carry P_1.")
        print("             This fires Instance 7 of asymmetric-mirror (global")
        print("             recording level).")
    else:
        print("P1 — p factors at B_2.")
