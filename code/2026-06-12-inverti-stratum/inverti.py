#!/usr/bin/env python3
"""
INVERTi transform on Day-62 (MODE) and Day-63 (MAX) stratum vectors.

Per Robin's Day-64 reply: Andrews et al. (arXiv:2505.06941) characterize
sequences realizable as graded dimensions of free noncommutative
cocommutative connected Hopf algebras (i.e. universal enveloping algebras
of free Lie algebras / Lyndon-word algebras) by the condition that the
INVERTi transform is termwise nonneg. If yes, b_n = primitive count
in degree n.

INVERTi:
    1 + sum_{n>=1} a(n) t^n  =  1 / (1 - sum_{n>=1} b(n) t^n)
i.e.  (1 + A(t)) (1 - B(t)) = 1
     where A(t) = sum_{n>=1} a(n) t^n,  B(t) = sum_{n>=1} b(n) t^n
Equivalently with the convention a(0)=1, b(0)=0:
    a(n) = sum_{k=1}^{n} b(k) a(n-k)   for n >= 1.
Solve for b(n) recursively:
    b(n) = a(n) - sum_{k=1}^{n-1} b(k) a(n-k).
"""

import json
from pathlib import Path


def inverti(a):
    """
    a is the list [a(1), a(2), ...]; we implicitly set a(0) = 1.
    Returns b = [b(1), b(2), ...] same length.
    """
    n_terms = len(a)
    # full list with a[0] = 1
    A = [1] + list(a)
    B = [0]  # B[0] = 0
    for n in range(1, n_terms + 1):
        s = sum(B[k] * A[n - k] for k in range(1, n))
        b_n = A[n] - s
        B.append(b_n)
    return B[1:]  # drop B[0]


def report(name, a, b):
    print(f"--- {name} ---")
    print(f"  a (input, indices 1..{len(a)}): {a}")
    print(f"  b (INVERTi):                    {b}")
    nonneg = all(x >= 0 for x in b)
    first_neg = next((i + 1 for i, x in enumerate(b) if x < 0), None)
    print(f"  termwise nonneg? {nonneg}")
    if not nonneg:
        print(f"  first negative at index n = {first_neg}: b({first_neg}) = {b[first_neg-1]}")
    print()
    return {"name": name, "a": a, "b": b, "nonneg": nonneg, "first_neg_index": first_neg}


def main():
    # Day-62 MODE stratum vector  (modal dim per degree)
    a_mode = [1, 5, 9, 9, 13, 17, 22, 26]
    # Day-63 MAX (structural)
    a_max = [3, 8, 11, 10, 19, 14, 23, 26]

    results = []
    print("=" * 60)
    print("INVERTi transform on Day-62/63 stratum vectors")
    print("=" * 60)
    print()

    b_mode = inverti(a_mode)
    results.append(report("MODE  (Day-62)", a_mode, b_mode))

    b_max = inverti(a_max)
    results.append(report("MAX   (Day-63)", a_max, b_max))

    # Sanity check: forward-transform b back through INVERT and compare to a.
    # INVERT (forward):  a(n) = sum_{k=1}^n b(k) a(n-k), a(0)=1.
    def forward(b):
        A = [1]
        for n in range(1, len(b) + 1):
            s = sum(b[k - 1] * A[n - k] for k in range(1, n + 1))
            A.append(s)
        return A[1:]

    print("Sanity check (forward INVERT of b should reproduce a):")
    print(f"  forward(b_mode) = {forward(b_mode)}")
    print(f"  expected a_mode = {a_mode}")
    print(f"  match: {forward(b_mode) == a_mode}")
    print(f"  forward(b_max) = {forward(b_max)}")
    print(f"  expected a_max = {a_max}")
    print(f"  match: {forward(b_max) == a_max}")
    print()

    # Also try the alternate convention: maybe the vectors include a(0).
    # MODE has [1, 5, ...] which would mean a(0)=1, a(1)=5, ... a(7)=26.
    print("--- alternate convention: vector entries are a(0), a(1), ... ---")
    print("(only valid for MODE; MAX[0]=3 would mean non-connected)")
    a_mode_alt = a_mode[1:]  # drop a(0)=1
    b_mode_alt = inverti(a_mode_alt)
    results.append(report("MODE alt (a(0)=1 implicit, vec is a(1..7))",
                          a_mode_alt, b_mode_alt))

    out_path = Path(__file__).parent / "inverti_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"saved: {out_path}")


if __name__ == "__main__":
    main()
