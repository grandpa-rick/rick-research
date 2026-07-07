"""Verify γ(c) closed form against brute-force min v₂(H_c(a,b,0)) for c=8,10,12.

This is a sanity check: for even c, β'(c) should be close to γ(c), and γ(c)
is the exact min at j=0.
"""
from hc import H_c_at_j0, v2, gamma


def brute_min_j0(c, box=48):
    """Min v₂(H_c(a,b,0)) over (a,b) in [0, box)² for both parities."""
    best_even = float('inf')
    best_odd = float('inf')
    pt_even = None
    pt_odd = None
    for a in range(box):
        for b in range(box):
            h = H_c_at_j0(a, b, c)
            if h == 0:
                continue
            val = v2(h)
            if (a + b) % 2 == 0:
                if val < best_even:
                    best_even = val
                    pt_even = (a, b)
            else:
                if val < best_odd:
                    best_odd = val
                    pt_odd = (a, b)
    return best_even, pt_even, best_odd, pt_odd


print("=" * 78)
print("Verify γ(c) closed form vs brute-force min v₂(H_c(a,b,0))")
print("=" * 78)
print(f"{'c':>3} {'γ formula':>10} {'brute same':>11} {'brute opp':>11} {'match?':>7}")
for c in range(4, 17):
    g = gamma(c)
    e, ept, o, opt = brute_min_j0(c, box=64)
    brute_min = min(e, o)
    match = "✓" if g == brute_min else "?"
    print(f"{c:>3} {g:>10} {e:>11} {o:>11} {match:>7}")
