"""
Attempt to compute β'(c) for c=11, 12 by scanning H_c(0) only.

WARNING: β'(c) = min over (a,b,j) of v2(H_c(a,b,j)). I do NOT have the general
H_c(a,b,j) closed form for c > 5 — only H_c(a,b,0), which is a run product:
    H_c(a,b,0) = prod_{t in Ra} (a+t) * prod_{s in Rb} (b+s)
where R_a and R_b are the "run" ranges.

So the minimum over (a,b) at j=0 gives γ(c) — the "same-parity opposite-parity"
brute-force min. This is an UPPER BOUND on β'(c) (since scanning at j=0 misses
the deeper j's where more cancellation happens).

But actually γ(c) upper-bounds v2(H_c(a,b,0)) as its MINIMUM over (a,b). And Clio's
β' is min over (a,b,j) — so β'(c) <= γ(c). Confirmed by her data:
   γ: 4,6,7,8,11,14,15  ≥  β': 4,3,7,6,11,9,14

So I can compute γ(c) exactly for c=11,12, giving an upper bound on β'.
For a lower bound we'd need her full H_c closed form.
"""
from math import factorial


def s2(n):
    return bin(n).count('1')


def v2(n):
    if n == 0:
        return float('inf')
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def gamma_formula(c):
    if c % 2 == 0:
        k = c // 2
        return 4 * k - 2 - s2(k) - s2(k - 1)
    k = (c - 1) // 2
    return 4 * k - 2 * s2(k)


def H_c_run(a, b, c):
    """H_c(a,b,0) = (a+3)(a+4)...(a+2+c) * (b+2)(b+3)...(b+1+c).
    Read off from spot-check pattern:
      c=4: a-range [3..5]=3 terms, b-range [2..4]=3 terms.  (c-1 each)
      c=5: a-range [3..6]=4 terms, b-range [2..5]=4 terms.  (c-1 each)
      c=6: a-range [3..7]=5 terms, b-range [2..6]=5 terms.  (c-1 each)
    So c=k: a-range [3..1+c] with c-1 terms; b-range [2..c] with c-1 terms.
    """
    r = 1
    for t in range(3, 2 + c):  # 3, 4, ..., c+1  → c-1 terms
        r *= (a + t)
    for t in range(2, 1 + c):  # 2, 3, ..., c    → c-1 terms
        r *= (b + t)
    return r


# Verify formula matches known γ(c)
print("Sanity check: γ(c) formula vs brute-force min at j=0")
print(f"{'c':>3} {'formula':>8} {'brute (a+b even/odd?)':>25}")
for c in range(4, 13):
    # Parity: (a+b) parity matched to c parity typically. Try both.
    m_even = min(v2(H_c_run(a, b, c)) for a in range(48) for b in range(48)
                 if (a + b) % 2 == 0)
    m_odd = min(v2(H_c_run(a, b, c)) for a in range(48) for b in range(48)
                if (a + b) % 2 == 1)
    print(f"{c:>3} {gamma_formula(c):>8}  same-parity={m_even}, opposite-parity={m_odd}")

# For a cleaner extension, sample β'-like quantity at j=0 for c=11, c=12
print()
print("Extended γ(c) for c=1..15 (from formula):")
for c in range(1, 16):
    print(f"  γ({c}) = {gamma_formula(c)}")

# The predicted dimer β'(c) values (as if dimer held):
# From Clio's data: β'(4)=4, β'(6)=7, β'(8)=11.
# For even c, β' seems to be γ(c) — same for c=4,6,8: γ = 4,7,11 = β'. Confirmed.
# For c=10: γ=15, β'=14 → dip 1.
# So even c mostly saturates γ. For c=12, γ = 18: predict β'(12) ∈ {17, 18}.

print()
print("Even-c: does β'(2k) = γ(2k)?")
for k in range(2, 6):
    c = 2 * k
    from_data = {4: 4, 6: 7, 8: 11, 10: 14}.get(c, None)
    if from_data is not None:
        print(f"  c={c}: γ={gamma_formula(c)}, β'={from_data}, "
              f"dip={gamma_formula(c) - from_data}")
print("So even β' hugs γ within 1-2. For odd c we get dips of 3,2,5,1 (c=5,7,9,10).")

# Key computation: what is the parity of s2(k), s2(k-1) at the dimer-fail point?
print()
print("2-adic accounting at each c:")
print(f"{'c':>3} {'β(c)':>5} {'γ(c)':>5} {'β prime':>8} {'β-γ':>5} {'β prime-γ':>10} {'s2(c-1)':>8} {'v2(c-1)':>8}")
bp = {4: 4, 5: 3, 6: 7, 7: 6, 8: 11, 9: 9, 10: 14}
for c in range(4, 11):
    b = 2 * (c - 1) - s2(c - 1)
    g = gamma_formula(c)
    bpv = bp[c]
    print(f"{c:>3} {b:>5} {g:>5} {bpv:>8} {b-g:>5} {bpv-g:>10} "
          f"{s2(c-1):>8} {v2(c-1):>8}")

# Now the actual test: β - γ vs the dimer dip.
print()
print("Rick's β - γ tracks: 0,1,1,2,0,1,1 for c=4..10")
print("Note β-γ jumps by 2 at c=8→9 (from 0 to 1... wait, table says 0,1). Recompute.")
