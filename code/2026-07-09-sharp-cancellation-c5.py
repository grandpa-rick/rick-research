"""Day 85 — Sharp-Cancellation Lemma at c = 5 (Task 4 fallback).

The quantity Q(a, b) = (a + 2)(b + 1) − 24 = ab + a + 2b − 22 arises inside
Clio's H_5 polynomial as the "innermost non-factorable" piece of the j = 2
coefficient. Understanding min v_2(Q) under the PROVE-Step-P1 constraints
gives an alternative handle on β'(5).

Test the claim min v_2(Q(a, b)) = 3 under several natural constraints.

Parity of (a + b + 5) even ⇒ a + b odd. So exactly one of a, b is even.

- Case A (a even, b odd): (a + 2) even, (b + 1) even ⇒ (a + 2)(b + 1) ≡ 0
  mod 4. Then Q ≡ -24 mod 4 → Q ≡ 0 mod 4 (since 24 ≡ 0 mod 4). Actually
  24 = 8·3, so mod 8 we get more info.
- Case B (a odd, b even): (a + 2) odd, (b + 1) odd ⇒ (a + 2)(b + 1) odd,
  so Q = odd − 24 = odd. v_2(Q) = 0. This case has no cancellation —
  it's the trivial case.

So the sharp-cancellation lemma only makes sense under Case A. Verify:
    min_{a even, b odd, a ≥ b ≥ 5} v_2(Q(a, b)) = 3   ← does this hold?
"""


def s2(n): return bin(n).count('1')


def v2(n):
    if n == 0:
        return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def Q(a, b):
    return (a + 2) * (b + 1) - 24


def sweep(a_range, b_range, filt):
    """Return (min_v, achievers) under filter."""
    min_v = None
    achievers = []
    all_vs = []
    for a in a_range:
        for b in b_range:
            if not filt(a, b):
                continue
            q = Q(a, b)
            if q == 0:
                continue
            vq = v2(q)
            all_vs.append(((a, b), q, vq))
            if min_v is None or vq < min_v:
                min_v = vq
                achievers = [(a, b, q)]
            elif vq == min_v:
                achievers.append((a, b, q))
    return min_v, achievers, all_vs


def main():
    print("=" * 70)
    print("Sharp-Cancellation Lemma at c = 5")
    print("=" * 70)

    print("\n[Case A] a even, b odd, a ≥ b ≥ 5, a ≤ 40")
    print("  (this is the case where Q has any cancellation at all)")
    A_min, A_ach, A_all = sweep(
        range(0, 41), range(0, 41),
        filt=lambda a, b: a % 2 == 0 and b % 2 == 1 and a >= b >= 5,
    )
    print(f"  min v_2(Q) = {A_min}")
    print(f"  # achievers: {len(A_ach)}")
    for a, b, q in A_ach[:20]:
        print(f"    (a, b) = ({a}, {b}), Q = {q} = 2^{v2(q)} · {q >> v2(q)}")

    # Distribution of v_2 in Case A
    from collections import Counter
    ctr = Counter(v for _, _, v in A_all)
    print(f"\n  v_2 distribution across Case A sweep:")
    for v, cnt in sorted(ctr.items()):
        print(f"    v_2 = {v}: {cnt} pairs")

    print("\n[Case B] a odd, b even, a ≥ b ≥ 5, a ≤ 40")
    print("  (Q is odd here → v_2 = 0 trivially)")
    B_min, B_ach, B_all = sweep(
        range(0, 41), range(0, 41),
        filt=lambda a, b: a % 2 == 1 and b % 2 == 0 and a >= b >= 5,
    )
    print(f"  min v_2(Q) = {B_min}")

    print("\n[Combined] a + b odd (parity for c = 5), a ≥ b ≥ 5, a ≤ 40")
    C_min, C_ach, C_all = sweep(
        range(0, 41), range(0, 41),
        filt=lambda a, b: (a + b) % 2 == 1 and a >= b >= 5,
    )
    print(f"  min v_2(Q) = {C_min}  (dominated by Case B)")

    # Fine structure of Case A: which (a mod 8, b mod 8) give v_2 ≥ 3?
    print("\n[Case A fine structure] (a mod 8, b mod 8) vs min v_2 achieved")
    fine = {}
    for (a, b), q, vq in A_all:
        key = (a % 8, b % 8)
        if key not in fine or vq < fine[key][0]:
            fine[key] = (vq, (a, b, q))
    print("  a mod 8 | b mod 8 | min v_2 | example (a, b, Q)")
    for key in sorted(fine.keys()):
        vq, ex = fine[key]
        print(f"     {key[0]:>2d}   |   {key[1]:>2d}   |   {vq:>2d}    | {ex}")

    # Where v_2 ≥ 3 in Case A — the "sharp cancellation" achievers.
    ge3 = [(ab, q, vq) for (ab, q, vq) in A_all if vq >= 3]
    print(f"\n[v_2 ≥ 3 in Case A] {len(ge3)} pairs")
    print("  First 15 achievers with v_2 exactly 3:")
    exactly3 = [x for x in ge3 if x[2] == 3][:15]
    for (a, b), q, vq in exactly3:
        print(f"    (a, b) = ({a}, {b}), Q = {q} = 2^3 · {q >> 3}")

    # Verify lemma variant: min over a ≡ 2 (mod 4) AND b ≡ 1 (mod 2)
    print("\n[Refined] a ≡ 2 mod 4 AND b odd, a ≥ b ≥ 5:")
    R_min, R_ach, R_all = sweep(
        range(0, 41), range(0, 41),
        filt=lambda a, b: a % 4 == 2 and b % 2 == 1 and a >= b >= 5,
    )
    print(f"  min v_2(Q) = {R_min}")
    print(f"  # achievers: {len(R_ach)}")
    for a, b, q in R_ach[:15]:
        print(f"    (a, b) = ({a}, {b}), Q = {q}")

    # Verdict
    print("\n" + "=" * 70)
    print("Verdict")
    print("=" * 70)
    if A_min == 3:
        print(f"  Case A (a even, b odd, a ≥ b ≥ 5) gives min v_2 = 3.")
        print(f"  Lemma HOLDS in Case A.")
    elif A_min < 3:
        print(f"  Case A min v_2 = {A_min} < 3. Lemma as stated FAILS in Case A.")
        # List the (a, b) where cancellation is worse than v_2 = 3
        worse = [(ab, q, vq) for (ab, q, vq) in A_all if vq < 3]
        print(f"  Case A has {len(worse)} pairs with v_2 < 3.")
        print(f"  First 10 such:")
        for (a, b), q, vq in worse[:10]:
            print(f"    (a, b) = ({a}, {b}), Q = {q}, v_2 = {vq}")


if __name__ == '__main__':
    main()
