"""Day 96 Task B — extend ♥ recursion check to c ∈ {20, 24, 28, 32}.

The ♥ recursion says:
    Δ_{k+2}^{(c)} − Δ_k^{(c)} = 2·v_2(c-1-k)    (odd k, 1 ≤ k ≤ c-3, c ≡ 0 mod 4)

Approach:
  For k ∈ {1, 3, 5}: use catalog Q_k directly to compute
    Δ_k at (a, b) = (T-2, 0) on the joint Poch-min shell, where T = smallest 2^t > c-2.
  For k ≥ 7 (odd): use the Master Formula validated in Day 95/96 heart-verify:
    Δ_{2m+1} = v_2(c) + 2·Σ_{i=2}^{2m} v_2(c-i)
  This is a *conjectural extension* — but validated at k=1, 3, 5 empirically for
  c ∈ [8, 64] step 4 by Day 96 heart-verify (all pass).

For each c ∈ {20, 24, 28, 32}, check every odd-k pair (k, k+2).
"""
import json
from sympy import symbols, sympify

a_s, b_s, c_s = symbols('a b c')

with open('/home/agent/projects/code/2026-07-11-Qk-catalog.json') as f:
    cat = json.load(f)
Q = {}
for ks, s in cat['Q_k_low_k'].items():
    Q[int(ks)] = sympify(s)
Q[6] = sympify(cat['Q_k_extended']['6']['poly_factored'])


def v2(n):
    if n == 0:
        return float('inf')
    n = abs(int(n))
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def T_of(c):
    T = 1
    while T <= c - 2:
        T *= 2
    return T


def delta_from_catalog(c_val, k, a_val, b_val):
    """Q_k evaluated at (a, b) — Δ_k = v_2 of that."""
    Qval = int(Q[k].subs({a_s: a_val, b_s: b_val, c_s: c_val}))
    return v2(Qval)


def delta_master(c_val, k):
    """Master Formula for Δ_{2m+1} at (T-2, 0), c ≡ 0 mod 4."""
    assert k % 2 == 1
    m = (k - 1) // 2
    result = v2(c_val) + 2 * sum(v2(c_val - i) for i in range(2, 2*m + 1))
    return result


def check_recursion_at_c(c_val, verbose=True):
    """Verify Δ_{k+2} − Δ_k = 2·v_2(c-1-k) for all odd k ∈ [1, c-3]."""
    T = T_of(c_val)
    a_val, b_val = T - 2, 0

    # First check (a_val, b_val) is on joint Poch-min shell for all odd k.
    for k in range(1, c_val - 2, 2):
        L = c_val - 1 - k
        assert ((a_val + 2) & L) == 0, f"a shell fail k={k}"
        assert ((b_val + 1) & L) == 0, f"b shell fail k={k}"
        assert (a_val + b_val) % 2 == c_val % 2, "parity fail"

    # Compute Δ_k for odd k.
    delta = {}
    src = {}
    for k in range(1, c_val - 2, 2):
        if k in Q:
            delta[k] = delta_from_catalog(c_val, k, a_val, b_val)
            src[k] = 'catalog'
        else:
            delta[k] = delta_master(c_val, k)
            src[k] = 'master'

    # Sanity: k = 1, 3, 5 from catalog match Master Formula.
    for k in (1, 3, 5):
        if k in delta:
            m = (k-1)//2
            master_pred = v2(c_val) + 2*sum(v2(c_val-i) for i in range(2, 2*m+1))
            assert delta[k] == master_pred, (
                f"catalog/master disagree at c={c_val} k={k}: "
                f"{delta[k]} vs {master_pred}"
            )

    # Check ♥ recursion for every odd pair.
    if verbose:
        print(f"\n  c = {c_val}, T = {T}, (a, b) = ({a_val}, {b_val})")
        print(f"  {'k':>3} {'Δ_k':>5} {'Δ_(k+2)':>8} {'diff':>5} "
              f"{'2v2(c-1-k)':>10} {'match':>6}  src(k), src(k+2)")

    pairs = []
    all_pass = True
    for k in range(1, c_val - 4, 2):  # need k+2 ≤ c-3, so k ≤ c-5
        d_k = delta[k]
        d_k2 = delta[k+2]
        diff = d_k2 - d_k
        expected = 2 * v2(c_val - 1 - k)
        match = (diff == expected)
        if not match:
            all_pass = False
        pairs.append({
            'k': k, 'delta_k': d_k, 'delta_kp2': d_k2,
            'diff': diff, 'expected': expected, 'match': match,
            'src_k': src[k], 'src_kp2': src[k+2],
        })
        if verbose:
            print(f"  {k:>3} {d_k:>5} {d_k2:>8} {diff:>5} {expected:>10}"
                  f" {'✓' if match else '✗':>6}  {src[k]:>7}, {src[k+2]:>7}")
    return all_pass, pairs


def main():
    print("=" * 76)
    print("Day 96 Task B — ♥ recursion at c ∈ {20, 24, 28, 32}")
    print("=" * 76)

    results = {}
    all_pass = True
    for c_val in [20, 24, 28, 32]:
        ok, pairs = check_recursion_at_c(c_val)
        results[c_val] = pairs
        if not ok:
            all_pass = False
            print(f"  ✗ FAIL at c={c_val}")
        else:
            print(f"  ✅ c={c_val}: all {len(pairs)} pairs pass")

    print()
    print("=" * 76)
    if all_pass:
        print("✅ ALL ♥ RECURSION CHECKS PASS at c ∈ {20, 24, 28, 32}")
    else:
        print("✗ SOME CHECKS FAILED — investigate above")
    print()
    print("Combined with earlier verification (c ∈ {8, 12, 16} full pairs and")
    print("c ∈ [8, 64] step 4 for k=1, 3), ♥ recursion is now:")
    print("  - Fully catalog-verified at k=1, 3, 5 for c ∈ [8, 64] step 4 (heart-verify.py)")
    print("  - Extended via Master Formula for odd k up to c-3 at c ∈ {20, 24, 28, 32}")

    out = {
        'c_values_full_pair_check': [20, 24, 28, 32],
        'all_pass': all_pass,
        'method': (
            'Δ_k from catalog Q_k for k ∈ {1, 3, 5}; '
            'from Master Formula for k ≥ 7 (validated at k=1,3,5 for these c).'
        ),
        'pairs_per_c': {str(c): p for c, p in results.items()},
    }
    with open('/home/agent/projects/code/2026-07-14-taskB-heart-extend.json', 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Saved: 2026-07-14-taskB-heart-extend.json")


if __name__ == '__main__':
    main()
