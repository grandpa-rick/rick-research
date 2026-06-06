"""
verify_witnesses.py — verify the type-uniform witnesses I cite in the proof.

For each B_n, n in {2..7}, construct the explicit witnesses for non-redundancy
of L_a (2 <= a <= n-1), U_a (2 <= a <= n-1), E, and check each violates ONLY
the claimed fence.

Witnesses:
  L_a:  M_a = 1, B_a = 1, all else 0.   (P_{a-1} = 0 forced, M_a = 1 > 0 violates L_a;
                                          P_a = 2 OK; P_b = 2 for b > a OK)
  U_a:  M_a = 1, B_{a-1} = 1, T_a = 1, all else 0.
                                        (P_{a-1} = 2 OK; P_a = 0 < 1 = M_a violates U_a;
                                         P_b = 0 for b > a OK)
  E:    S = 1, all else 0.              (P_{n-1} = 0 < 1 = S violates E)

Rick.
"""

from classify_fences import fences_Bn


def check_violates_only(M, B, T, S, n, target_name):
    """Return True iff the config violates exactly the fence with the given name."""
    fences = fences_Bn(n)
    violated = []
    for nm, fn in fences:
        slack = fn(M, B, T, S)
        if slack < 0:
            violated.append(nm)
    return violated == [target_name]


def make_zero(n):
    return ([0]*(n-1), [0]*(n-1), [0]*(n-1), 0)


def witness_L_a(n, a):
    """L_a witness: M_a = 1, B_a = 1, all else 0."""
    M = [0]*(n-1); B = [0]*(n-1); T = [0]*(n-1); S = 0
    M[a-1] = 1; B[a-1] = 1
    return tuple(M), tuple(B), tuple(T), S


def witness_U_a(n, a):
    """U_a witness: M_a = 1, B_{a-1} = 1, T_a = 1, all else 0."""
    assert a >= 2, "U_a witness needs a >= 2"
    M = [0]*(n-1); B = [0]*(n-1); T = [0]*(n-1); S = 0
    M[a-1] = 1; B[a-2] = 1; T[a-1] = 1
    return tuple(M), tuple(B), tuple(T), S


def witness_E(n):
    M = [0]*(n-1); B = [0]*(n-1); T = [0]*(n-1); S = 1
    return tuple(M), tuple(B), tuple(T), S


def witness_L_1(n):
    """L_1 violation witness (just to confirm L_1 IS non-redundant — even though
    L_1 is 'degenerate', it's still a non-redundant constraint: M_1 = 1 is not
    forced to 0 without it. We just observe that on the HW polytope, L_1 forces
    M_1 = 0, collapsing a dimension; but L_1 itself is a needed inequality."""
    M = [0]*(n-1); B = [0]*(n-1); T = [0]*(n-1); S = 0
    M[0] = 1; B[0] = 1  # M_1 = 1, B_1 = 1, all else 0
    return tuple(M), tuple(B), tuple(T), S


def main():
    print(f"{'n':>2}  {'fence':>5}   {'violates-only?':<14}   config")
    print("-" * 90)
    failures = 0
    for n in range(2, 8):
        # L_1
        wit = witness_L_1(n)
        ok = check_violates_only(*wit, n, "L_1")
        mark = "OK" if ok else "FAIL"
        failures += (0 if ok else 1)
        print(f"{n:>2}  {'L_1':>5}   {mark:<14}   {wit}")

        for a in range(2, n):
            # L_a
            wit = witness_L_a(n, a)
            ok = check_violates_only(*wit, n, f"L_{a}")
            mark = "OK" if ok else "FAIL"
            failures += (0 if ok else 1)
            print(f"{n:>2}  {f'L_{a}':>5}   {mark:<14}   {wit}")
            # U_a
            wit = witness_U_a(n, a)
            ok = check_violates_only(*wit, n, f"U_{a}")
            mark = "OK" if ok else "FAIL"
            failures += (0 if ok else 1)
            print(f"{n:>2}  {f'U_{a}':>5}   {mark:<14}   {wit}")
        # E
        wit = witness_E(n)
        ok = check_violates_only(*wit, n, "E")
        mark = "OK" if ok else "FAIL"
        failures += (0 if ok else 1)
        print(f"{n:>2}  {'E':>5}   {mark:<14}   {wit}")
        print()

    print(f"\nTotal failures: {failures}")
    return failures == 0


if __name__ == '__main__':
    main()
