"""
GSSOT enumeration for B_2 dominant spin pairs.

For λ^♯, μ^♯ both dominant spin in B_2 with integer parts λ, μ:
  enumerate GSSOT_{g+1/2}(oc(λ, g), oc-bar(μ, g)) for g = max(λ_1, μ_1).

A GSSOT of shape α (a partition / non-neg int vector of length n=2)
weight β (length n) bound g+1/2 is a sequence T = (T_1, ..., T_n) where
each T_i = (μ_{i-1}, ν_i, μ_i) is a "generalized oscillating horizontal
strip" (gohs) with:
  - I(T_1) = ∅, F(T_n) = α (the shape)
  - F(T_i) = I(T_{i+1})
  - ν_i / μ_{i-1} and ν_i / μ_i are horizontal strips
  - |ν_i / μ_{i-1}| + |ν_i / μ_i| = β_i  OR  β_i - 1 (the "ghost" cell allowed)
  - ν_1 ≤ g, ν_1 + 1/2 ≤ g (ghost case): in either case ν_1 ≤ g.

For B_2 (n=2), this is two oscillating steps.

References: CKL Defs 3.1, 3.2 (p. 9-10).
"""

from itertools import product


def is_partition(p):
    """Check that p is weakly decreasing nonneg-int tuple."""
    return all(p[i] >= p[i+1] for i in range(len(p)-1)) and all(x >= 0 for x in p)


def horizontal_strip(small, big):
    """Check big ⊃ small and big/small is a horizontal strip (each col diff ≤ 1)."""
    if len(small) != len(big):
        return False
    if any(s > b for s, b in zip(small, big)):
        return False
    # convert to col-shape (transpose) and check columns differ by ≤ 1
    from itertools import zip_longest
    big_cols = []  # column heights of big
    if big:
        max_part = big[0]
        for c in range(max_part):
            big_cols.append(sum(1 for r in big if r > c))
        small_cols = []
        max_s = small[0] if small else 0
        for c in range(max(max_part, max_s)):
            small_cols.append(sum(1 for r in small if r > c))
        # pad
        while len(big_cols) < len(small_cols):
            big_cols.append(0)
        while len(small_cols) < len(big_cols):
            small_cols.append(0)
        if any(b - s not in (0, 1) for b, s in zip(big_cols, small_cols)):
            return False
    return True


def all_partitions_bounded(n, max_part):
    """All partitions of length ≤ n with each part ≤ max_part."""
    out = set()
    def rec(remaining_parts, prev):
        if remaining_parts == 0:
            yield ()
            return
        for v in range(prev + 1):
            for tail in rec(remaining_parts - 1, v):
                yield (v,) + tail
    for p in rec(n, max_part):
        # canonical: weakly decreasing
        out.add(p)
    return list(out)


def all_gohs(prev_shape, target_size, max_size, n_parts, max_part):
    """Enumerate gohs (μ, ν, λ): given previous final shape μ = prev_shape,
    target net size (|ν/μ| + |ν/λ|) = target_size or target_size - 1,
    and constraints from CKL Def 3.2:
      - ν/μ and ν/λ are horizontal strips
      - n_parts: max length of partitions in this rank
      - max_part: max part size
    Yields (ν, λ).
    """
    # ν must contain μ as a horizontal strip; |ν/μ| ≥ 0.
    for nu in all_partitions_bounded(n_parts, max_part):
        if not horizontal_strip(prev_shape, nu):
            continue
        size_nu_mu = sum(nu) - sum(prev_shape)
        if size_nu_mu < 0:
            continue
        if size_nu_mu > target_size:
            continue
        # λ must be inside ν, ν/λ horizontal strip, total size = target or target-1
        for size_nu_lam in [target_size - size_nu_mu, target_size - 1 - size_nu_mu]:
            if size_nu_lam < 0:
                continue
            for lam in all_partitions_bounded(n_parts, max_part):
                if sum(nu) - sum(lam) != size_nu_lam:
                    continue
                if not horizontal_strip(lam, nu):
                    continue
                yield (nu, lam, target_size - size_nu_mu - size_nu_lam)  # (nu, lam, ghost_flag: 0 or 1)


def all_gssot(shape, weight, n_parts, max_part):
    """Enumerate GSSOT of shape `shape` with `weight` (length-n_parts integer vector).
    Returns list of [(nu_1, lam_1, ghost_1), ..., (nu_n, lam_n, ghost_n)] where
    lam_n must equal shape, and lam_{i-1} = "previous final" (= I(T_i) = F(T_{i-1})).
    Note: weight[i] = β_i is target size of step i.
    """
    n = len(weight)
    results = []
    def rec(i, prev_shape, accum):
        if i == n:
            if prev_shape == shape:
                results.append(list(accum))
            return
        for (nu, lam, ghost) in all_gohs(prev_shape, weight[i], max_part, n_parts, max_part):
            accum.append((nu, lam, ghost))
            rec(i + 1, lam, accum)
            accum.pop()
    rec(0, tuple([0]*n_parts), [])
    return results


def gssot_to_str(T):
    return " | ".join(f"(ν={nu}, λ={lam}, ghost={ghost})" for nu, lam, ghost in T)


def main():
    # Pair 1: λ^♯ = (3/2, 1/2), μ^♯ = (1/2, 1/2). Integer parts: λ = (1, 0), μ = (0, 0).
    # CKL: GSSOT_{g+1/2}(oc(λ, g), ocBar(μ, g)) where g ≥ λ_1 = 1.
    # Take g = 1: oc(λ, 1) = (1 - λ_2, 1 - λ_1) = (1, 0).
    #             ocBar(μ, 1) = (1 - μ_1, 1 - μ_2) = (1, 1).
    # So we want GSSOT_{3/2}(shape=(1, 0), weight=(1, 1)).

    # First: pad shape to length 2 -> (1, 0).
    print("=== B_2, λ^♯ = (3/2, 1/2), μ^♯ = (1/2, 1/2) ===")
    print("    integer λ = (1, 0), μ = (0, 0), g = 1")
    print("    enumerate GSSOT_{3/2}(shape=(1, 0), weight=(1, 1))")
    print()

    shape = (1, 0)
    weight = (1, 1)
    g = 1
    n_parts = 2
    max_part = g  # ν_1 ≤ g

    Ts = all_gssot(shape, weight, n_parts, max_part)
    print(f"Found {len(Ts)} GSSOT:")
    for idx, T in enumerate(Ts):
        print(f"  [{idx}] {gssot_to_str(T)}")
    print()

    # Pair 2: λ^♯ = (5/2, 1/2), μ^♯ = (1/2, 1/2). Integer: λ = (2, 0), μ = (0, 0).
    print("=== B_2, λ^♯ = (5/2, 1/2), μ^♯ = (1/2, 1/2) ===")
    print("    integer λ = (2, 0), μ = (0, 0), g = 2")
    print("    enumerate GSSOT_{5/2}(shape=(2, 0), weight=(2, 2))")

    shape = (2, 0)
    weight = (2, 2)
    g = 2
    Ts = all_gssot(shape, weight, n_parts=2, max_part=g)
    print(f"Found {len(Ts)} GSSOT:")
    for idx, T in enumerate(Ts):
        print(f"  [{idx}] {gssot_to_str(T)}")
    print()

    # Pair 3
    print("=== B_2, λ^♯ = (5/2, 3/2), μ^♯ = (1/2, 1/2) ===")
    print("    integer λ = (2, 1), μ = (0, 0), g = 2")
    print("    enumerate GSSOT_{5/2}(shape=(1, 0), weight=(2, 2))")
    # oc(λ=(2,1), 2) = (2-1, 2-2) = (1, 0). ocBar(μ, 2) = (2, 2).
    shape = (1, 0)
    weight = (2, 2)
    Ts = all_gssot(shape, weight, n_parts=2, max_part=2)
    print(f"Found {len(Ts)} GSSOT:")
    for idx, T in enumerate(Ts):
        print(f"  [{idx}] {gssot_to_str(T)}")


if __name__ == "__main__":
    main()
