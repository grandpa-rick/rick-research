"""
verify_facet_interiors.py — for each candidate facet, exhibit a HW config that
saturates only that fence (and L_1, which is always saturated), confirming the
facet has a relative interior in P_n.

For L_a (a >= 2): need M_a = P_{a-1} > 0 and all other slacks > 0.
   Witness: B_1 = 1, M_a = 2, B_a = 1, all else 0.
   P_0 = 0, P_1 = 2, P_b = 2 for 1 <= b < a, P_a = 4, P_b = 4 for b > a, P_{n-1} = 4.
   L_1: 0=0 sat. L_b (b<a, b>1): 0<2. U_b (b<a): 0<2. L_a: 2=2 sat. U_a: 2<4. L_b (b>a): 0<4.
   U_b (b>a): 0<4. E: 0<4.

For U_a (a >= 2): need M_a = P_a > 0 strict on others.
   Witness: M_a = 1, B_{a-1} = 1, T_a = 1, B_a = 1, all else 0.
   ... actually need M_a + 2T_a = P_{a-1} + 2B_a and other slacks > 0.
   Let me try: B_{a-1} = 1, M_a = 1, B_a = 1, T_a = 2, B_{a+1...} = 0
   P_{a-1} = 2, P_a = 2 + 2 - 4 = 0. U_a: M_a = 1 <= 0. Violated.
   Try: B_{a-1} = 1, M_a = 1, B_a = 0, T_a = 1
   P_{a-1} = 2, P_a = 0. U_a: 1 <= 0 violated.
   Hmm we need P_a >= M_a strict NO wait equal.
   M_a = P_a: M_a + 2T_a = P_{a-1} + 2B_a.
   Try: M_a = 1, T_a = 1, B_{a-1} = 1, B_a = 1. So M_a + 2T_a = 3, P_{a-1} + 2B_a = 2 + 2 = 4. NO.
   Try: M_a = 2, T_a = 0, B_{a-1} = 1, B_a = 0. P_{a-1} = 2, M_a = 2 = P_a (since P_a = P_{a-1} = 2).
   Check L_a: M_a = 2 = P_{a-1} = 2, also saturated! So L_a is sat too.
   Want strict on L_a: M_a < P_{a-1}. So P_{a-1} > M_a = P_a.
   M_a + 2T_a = P_{a-1} + 2B_a => P_{a-1} = M_a + 2T_a - 2B_a.
   Want P_{a-1} > M_a: T_a > B_a.
   Try: M_a = 0, T_a = 1, B_a = 0, B_{a-1} = 1: P_{a-1} = 2, M_a + 2T_a = 2, P_{a-1} + 2B_a = 2. U_a saturated.
   M_a = 0 < P_{a-1} = 2: L_a strict. ✓
   But what about L_{a+1}? P_a = P_{a-1} + 2(B_a - T_a) = 2 + 2(0-1) = 0. L_{a+1}: M_{a+1} <= 0.
   So M_{a+1} = 0. And U_{a+1}: 0 <= P_{a+1}. If we set B_{a+1} = ..., free.
   Set all chains after a to 0. Then P_b = 0 for b >= a, hence E: S <= 0, so S = 0.
   L_{a+1}: 0 = 0 sat — extra saturation! Bad.

Hmm. To avoid saturating L_{a+1}: need M_{a+1} < P_a = 0, impossible since M_{a+1} >= 0.
So at boundary a = n-1 it's fine (no L_{n}). For a < n-1, this is hard.

Actually I realize: when U_a is saturated with P_a = 0, then P_a = 0 forces L_{a+1}: M_{a+1} = 0, which is the lower-bound case (saturated). So U_a saturation at low P implies L_{a+1} saturation.

To get U_a saturated WITHOUT L_{a+1} saturated: need M_{a+1} < P_a, hence P_a > 0.
Then M_a + 2T_a = P_{a-1} + 2B_a > 0 - 2(P_a - P_{a-1})... hmm getting tangled.

Let me try: M_a = 1, P_{a-1} = 3, P_a = 1, so 2(B_a - T_a) = -2, e.g., T_a = 1, B_a = 0.
M_a + 2T_a = 3 = P_{a-1} + 2B_a = 3. U_a sat. L_a: M_a = 1 < P_{a-1} = 3. ✓
P_{a-1} = 3: need to construct. E.g., B_1 = 1, B_2 = 1 (if a >= 3), so P_1 = 2, P_2 = 4. Want P_{a-1} = 3? 3 is odd, but each step of P changes by 2(B - T), an even number. So all P's are even! P_{a-1} = 3 is impossible.

OK P is always even. So if M_a is even, we can have M_a = P_a > 0 with L_a strict. If M_a is odd, then M_a = P_a is impossible.

Let me try M_a = 2, T_a = 1, B_a = 1, P_{a-1} = 2 (= 2(B_{a-1} - T_{a-1}) summed up to a-1).
Easy: B_{a-1} = 1, T_{a-1} = 0. Then P_{a-1} = 2.
P_a = P_{a-1} + 2(B_a - T_a) = 2 + 0 = 2.
U_a: M_a + 2T_a = 4 = P_{a-1} + 2B_a = 4. SAT ✓
L_a: 2 = 2. SAT. Hmm L_a is also saturated.

Try M_a = 1: M_a = P_a needs P_a = 1, impossible.

Try M_a = 2, T_a = 0, B_a = 1, P_{a-1} = 4:
P_a = 4 + 2 = 6. U_a: M_a = 2 < P_a = 6. NOT saturated.

I want U_a saturated AND L_a strict. U_a saturated: M_a = P_a. L_a strict: M_a < P_{a-1}.
So P_a < P_{a-1}, i.e., B_a < T_a. Also M_a = P_a needs P_a = M_a, even (since all P even).

Smallest: M_a = 2, P_a = 2. P_{a-1} > 2, so P_{a-1} >= 4. Let's say P_{a-1} = 4.
B_a < T_a: B_a = 0, T_a = 1. Then P_a = 4 - 2 = 2 = M_a ✓.
L_a strict: 2 < 4 ✓.

For L_{a+1} strict (if a+1 <= n-1): M_{a+1} < P_a = 2. Set M_{a+1} = 0. ✓
For U_{a+1} strict: M_{a+1} + 2T_{a+1} < P_a + 2B_{a+1}, i.e., 0 < 2 + 2 B_{a+1}. Always (if B_{a+1} = 0, RHS = 2 > 0 ✓).
For chains b > a+1: M_b = 0, B_b = T_b = 0. ✓
E: S < P_{n-1}. With chains after a all zero: P_{n-1} = P_a = 2. Set S = 0 or 1.

Configuration: P_{a-1} = 4 needs sum_{b<a} 2(B_b - T_b) = 4. E.g., B_{a-1} = 2 (a-1 in 1..n-2 OK), T_{a-1} = 0.

So config: M_{a-1} = 0, B_{a-1} = 2, T_{a-1} = 0, M_a = 2, B_a = 0, T_a = 1, all others 0, S = 0 (or 1).

Let me verify for B_4, a = 2: M = (0, 2, 0), B = (2, 0, 0), T = (0, 1, 0), S = 0.
P_0 = 0, P_1 = 4, P_2 = 4 + 2(0-1) = 2, P_3 = 2.
- L_1: 0 = 0 sat
- U_1: 0 <= 4 strict
- L_2: 2 < 4 strict
- U_2: 2 = 2 sat (TARGET)
- L_3: 0 < 2 strict
- U_3: 0 < 2 strict
- E: 0 < 2 strict

✓ Only U_2 (and degenerate L_1) saturated.

Witness for U_a interior:
  B_{a-1} = 2, M_a = 2, T_a = 1, all others 0.

Rick.
"""

import sys
sys.path.insert(0, '.')
from classify_fences import fences_Bn


def witnesses():
    """For each fence (other than L_1, U_1), return a HW config in relative interior of that facet."""
    return None  # placeholder


def check_only_saturates(M, B, T, S, n, target_fence):
    """Check the config is in HW (all slacks >= 0), saturates target_fence and L_1, and is strict on all others."""
    fences = fences_Bn(n)
    sat = []
    for nm, fn in fences:
        slack = fn(M, B, T, S)
        if slack < 0:
            return False, f"violates {nm}"
        if slack == 0:
            sat.append(nm)
    # L_1 always saturated (degenerate). target_fence should also be saturated.
    # No other should be.
    expected = {"L_1", target_fence}
    if set(sat) == expected:
        return True, "OK"
    return False, f"saturated: {sat}, expected: {expected}"


def relative_interior_witness_L_a(n, a):
    """L_a relative-interior witness: B_a = 1, M_a = 2, B_a' = 1 from chain a (already there),
    actually: want M_a = P_{a-1} > 0 with strict on others.
    Construction: chain b = a-1 has B_{a-1} = 1, T_{a-1} = 0 (gives P_{a-1} = 2), chain a has
    M_a = 2, B_a = 1, T_a = 0, all else 0. P_b for b < a-1 is 0; we need L_b strict for b in
    {2, ..., a-1}: M_b = 0 < 0, NO, those are also saturated unless b=a-1... let me reconsider.
    """
    # Need P_{a-1} > 0 AND L_b strict for all b != a (b >= 2).
    # L_b: M_b <= P_{b-1}. M_b = 0 < P_{b-1} iff P_{b-1} > 0. P_{b-1} = 0 for b = 2 ⟹ b = 2 saturated.
    # Hmm. So L_2 always saturated unless we change things.

    # Wait — actually it's fine for L_b to be saturated too if we're checking the FACET-interior
    # of L_a specifically. The relative interior of the L_a facet is where ONLY L_a is at its
    # boundary among the facets (not counting L_1 which is always saturated).

    # But L_b can be saturated when P_{b-1} = M_b = 0. Both are simultaneously at lower bound.
    # That doesn't put us in the L_a facet's relative interior — it puts us at a higher-codim
    # intersection.

    # I'll keep the witness simple: use a configuration where ALL P_b > 0 for b >= 1, by giving
    # B_1 > 0.
    # Try: B_1 = 1, B_2 = 1, ..., B_{a-1} = 1, M_a = P_{a-1} = 2(a-1), B_a = 1, T_a = 0.
    # Then P_{a-1} = 2(a-1), M_a = 2(a-1), so L_a saturated.
    # P_a = 2(a-1) + 2 = 2a. M_a = 2(a-1) < P_a = 2a ✓ U_a strict.
    # P_b for b < a: P_b = 2b > 0. L_b: M_b = 0 < 2(b-1). Strict if b >= 2.
    # Wait, L_b: M_b <= P_{b-1}. For b=2: 0 <= 2 ✓ strict. For b in [2, a-1]: 0 <= 2(b-1), strict if b >= 2. ✓
    # U_b for b < a: M_b = 0 <= P_b = 2b, strict.
    # For b > a: M_b = 0, B_b = T_b = 0 (default), so P_b = P_a = 2a. L_b: 0 <= 2a ✓ strict. U_b: 0 <= 2a strict.
    # E: S = 0 <= P_{n-1} = 2a. Strict.
    M = [0]*(n-1); B = [0]*(n-1); T = [0]*(n-1); S = 0
    for b in range(1, a):
        B[b-1] = 1
    M[a-1] = 2*(a-1)
    B[a-1] = 1
    return tuple(M), tuple(B), tuple(T), S


def relative_interior_witness_U_a(n, a):
    """U_a relative-interior witness: B_{a-1} = 2 (gives P_{a-1} = 4 if no other), M_a = 2, T_a = 1, all else 0.
    Better: B_1 = ... = B_{a-1} = 1, T_b = 0 (b<a). Then P_{a-1} = 2(a-1).
    Want U_a saturated: M_a = P_a. And L_a strict: M_a < P_{a-1}.
    Set M_a < 2(a-1) (so L_a strict) and M_a = P_a = P_{a-1} + 2(B_a - T_a) = 2(a-1) + 2(B_a - T_a).
    Try B_a = 0, T_a = 1, M_a = 2(a-1) - 2 = 2(a-2).
    Then P_a = 2(a-2) = M_a. ✓
    Need M_a >= 0, so a >= 2. ✓
    L_a strict: M_a = 2(a-2) < P_{a-1} = 2(a-1). ✓ if a >= 2.
    For b > a: with B_b = T_b = M_b = 0 default, P_b = P_a = 2(a-2).
    Need this > 0 for L_b, U_b strict (b > a). So a >= 3.
    """
    if a < 3:
        # For a = 2 at any n, need P_a > 0 for strict on later. P_a = 2(a-2) = 0 at a = 2. Bad.
        # Alternative: at a = 2, use different construction.
        # Want U_2 sat, L_2 strict, all else strict (including L_3, U_3, E at n >= 3, or just E at n=2).
        # P_1 > M_2, P_2 = M_2, P_2 > 0 (for L_3, U_3, E strict at n >= 3).
        # P_1 = 2(B_1 - T_1), P_2 = 2(B_1 - T_1) + 2(B_2 - T_2).
        # M_2 = P_2 > 0, M_2 < P_1: so P_1 > P_2 > 0. T_2 > B_2.
        # Set B_1 = 2, T_1 = 0, B_2 = 0, T_2 = 1, M_2 = 2: P_1 = 4, P_2 = 4 - 2 = 2 = M_2 ✓. P_1 = 4 > 2 = M_2 ✓ L_2 strict.
        M = [0]*(n-1); B = [0]*(n-1); T = [0]*(n-1); S = 0
        B[0] = 2
        M[1] = 2
        T[1] = 1
        return tuple(M), tuple(B), tuple(T), S
    # a >= 3
    M = [0]*(n-1); B = [0]*(n-1); T = [0]*(n-1); S = 0
    for b in range(1, a):
        B[b-1] = 1
    M[a-1] = 2*(a-2)
    T[a-1] = 1
    return tuple(M), tuple(B), tuple(T), S


def relative_interior_witness_E(n):
    """E relative-interior witness: S = P_{n-1}, all P_b > 0, strict everywhere else.
    Set B_1 = ... = B_{n-1} = 1, T_b = 0, all M_b = 0. P_b = 2b for b < n. S = 2(n-1).
    Check: L_b strict (0 < 2(b-1) for b >= 2). U_b strict (0 < 2b). E sat (S = 2(n-1) = P_{n-1}).
    """
    M = [0]*(n-1); B = [1]*(n-1); T = [0]*(n-1); S = 2*(n-1)
    return tuple(M), tuple(B), tuple(T), S


def main():
    print(f"{'n':>2}  {'fence':>5}  {'status':<60}  config")
    print("-" * 130)
    failures = 0
    for n in range(3, 8):  # interior witnesses work cleanly for n >= 3
        for a in range(2, n):
            # L_a
            wit = relative_interior_witness_L_a(n, a)
            ok, msg = check_only_saturates(*wit, n, f"L_{a}")
            mark = "OK" if ok else f"FAIL: {msg}"
            failures += (0 if ok else 1)
            print(f"{n:>2}  {f'L_{a}':>5}  {mark:<60}  {wit}")
            # U_a
            wit = relative_interior_witness_U_a(n, a)
            ok, msg = check_only_saturates(*wit, n, f"U_{a}")
            mark = "OK" if ok else f"FAIL: {msg}"
            failures += (0 if ok else 1)
            print(f"{n:>2}  {f'U_{a}':>5}  {mark:<60}  {wit}")
        # E
        wit = relative_interior_witness_E(n)
        ok, msg = check_only_saturates(*wit, n, "E")
        mark = "OK" if ok else f"FAIL: {msg}"
        failures += (0 if ok else 1)
        print(f"{n:>2}  {'E':>5}  {mark:<60}  {wit}")
        print()
    print(f"\nTotal failures: {failures}")


if __name__ == '__main__':
    main()
