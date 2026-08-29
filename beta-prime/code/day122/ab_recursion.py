"""Experiment 1: (A, B) recursion in sympy.

Build A_a(j, t), B_a(j, t) via the recursion:
  A_{a+1} = (j - a) A_a + B_a
  B_{a+1} = -t A_a - a B_a
  A_0 = 0, B_0 = 1

Verify:
  deg_t A_a = floor((a-1)/2)
  deg_t B_a = floor(a/2)
  A_{2m+2}(2m+1, t) = 0 for m = 0..4

Compute W_{a,b}(j, t) = A_a B_b - A_b B_a table, check W_{a,b} = -W_{b,a},
W_{a,a} = 0. Pickle for later use.
"""

import pickle
import sympy as sp
from sympy import symbols, expand, Poly, Integer, degree, simplify

j, t = symbols('j t')

MAX_A = 20


def build_AB(N=MAX_A):
    """Return lists A[0..N], B[0..N] as sympy expressions in j, t."""
    A = [Integer(0)]
    B = [Integer(1)]
    for a in range(N):
        A_next = expand((j - a) * A[a] + B[a])
        B_next = expand(-t * A[a] - a * B[a])
        A.append(A_next)
        B.append(B_next)
    return A, B


def deg_t(expr):
    if expr == 0:
        return -1
    return Poly(expr, t).degree()


def deg_j(expr):
    if expr == 0:
        return -1
    return Poly(expr, j).degree()


def main():
    A, B = build_AB(MAX_A)

    print("=" * 70)
    print("A_a and B_a for a = 0..10:")
    print("=" * 70)
    for a in range(11):
        print(f"  A_{a} = {A[a]}")
        print(f"  B_{a} = {B[a]}")
        print()

    print("=" * 70)
    print("Degree check: deg_t A_a = floor((a-1)/2), deg_t B_a = floor(a/2)")
    print("=" * 70)
    ok = True
    for a in range(1, MAX_A + 1):
        expected_A = (a - 1) // 2
        expected_B = a // 2
        got_A = deg_t(A[a])
        got_B = deg_t(B[a])
        okA = got_A == expected_A
        okB = got_B == expected_B
        if not (okA and okB):
            ok = False
        marker = "OK" if okA and okB else "!!! MISMATCH"
        print(f"  a={a:2d}: deg_t A_a = {got_A} (exp {expected_A}), "
              f"deg_t B_a = {got_B} (exp {expected_B})  {marker}")
    print(f"\nDegree check: {'PASSED' if ok else 'FAILED'}")

    print()
    print("=" * 70)
    print("Sub-lemma: A_{2m+2}(2m+1, t) = 0 for m = 0..4")
    print("=" * 70)
    all_zero = True
    for m in range(5):
        a = 2 * m + 2
        j_val = 2 * m + 1
        val = expand(A[a].subs(j, j_val))
        is_zero = (val == 0)
        marker = "OK" if is_zero else f"!!! NONZERO = {val}"
        print(f"  m={m}: A_{a}(j={j_val}, t) = {val}  {marker}")
        if not is_zero:
            all_zero = False
    print(f"\nSub-lemma check: {'PASSED' if all_zero else 'FAILED'}")

    print()
    print("=" * 70)
    print("W_{a,b}(j, t) = A_a B_b - A_b B_a for a,b <= 6")
    print("=" * 70)
    W = {}
    for a in range(11):
        for b in range(11):
            W[(a, b)] = expand(A[a] * B[b] - A[b] * B[a])
    # symmetry and diagonal
    sym_ok = True
    diag_ok = True
    for a in range(11):
        if W[(a, a)] != 0:
            diag_ok = False
        for b in range(11):
            if expand(W[(a, b)] + W[(b, a)]) != 0:
                sym_ok = False
    print(f"  W_{{a,a}} = 0 for a in [0,10]: {'OK' if diag_ok else 'FAIL'}")
    print(f"  W_{{a,b}} = -W_{{b,a}} for a,b in [0,10]: {'OK' if sym_ok else 'FAIL'}")

    # print a few sample W's
    print("\nSample W_{a,b} for small (a,b):")
    for a in range(1, 7):
        for b in range(a):
            wab = W[(a, b)]
            print(f"  W_{{{a},{b}}} = {wab}")

    # deg_t W_{a,b} for a>b — Day 121 conjecture: deg = b + floor((a-b-1)/2)
    print("\nDegree check: deg_t W_{a,b} = b + floor((a-b-1)/2) for a > b, a<=8")
    ok_wdeg = True
    for a in range(1, 9):
        for b in range(a):
            expected = b + (a - b - 1) // 2
            got = deg_t(W[(a, b)])
            marker = "OK" if got == expected else "!!! MISMATCH"
            if got != expected:
                ok_wdeg = False
            print(f"  (a,b)=({a},{b}): deg_t W = {got} (exp {expected})  {marker}")
    print(f"\nW degree check: {'PASSED' if ok_wdeg else 'FAILED'}")

    # Pickle everything for downstream use
    out_path = "/home/agent/projects/beta-prime/code/day122/ab_table.pkl"
    with open(out_path, "wb") as f:
        pickle.dump({
            "A": [str(a) for a in A],
            "B": [str(b) for b in B],
            # store raw exprs by srepr for portability
            "A_expr": A,
            "B_expr": B,
            "W_expr": W,
            "j_sym": j,
            "t_sym": t,
        }, f)
    print(f"\nPickled to {out_path}")


if __name__ == "__main__":
    main()
