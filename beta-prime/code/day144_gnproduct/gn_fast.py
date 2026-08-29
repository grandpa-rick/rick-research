"""Fast GN-product-at-N=1 test.

At N=1 in Das-Pattanayak Prop 2.3 (as read):
  1 - G(z, lam) = (1 - z lam(lam+1)) / (1 - z lam(lam-1))
so
  G(z, lam) = 2 z lam / (1 - z lam(lam-1)).

Question: can we substitute z, lam as functions of tau so G(z, lam) = F(tau)?

Approach A: z = tau, lam = constant.
Approach B: z = tau, lam = lam(tau) power series.

The kernel expansion is
  G(z, lam) = 2 z lam * sum_{k>=0} (z lam(lam-1))^k = 2 z lam sum_k (z mu)^k, mu := lam(lam-1).

So [z^k] G = 2 [lam mu^{k-1}] (constant lam) = 2 lam^k (lam-1)^{k-1}.

For Approach B we solve sequentially:
  b_1 = 2 lam_0 => lam_0 = 3/2
  b_2 = ? -> yields lam_1
  ...
"""

from sympy import Rational, symbols, expand, Poly

tau = symbols('tau')
LamMax = 8

# Rick's F(tau) coefficients b_k = [tau^k] F
b = [Rational(0), Rational(3), Rational(27), Rational(417), Rational(7851),
     Rational(164124), Rational(3661389), Rational(85384566), Rational(2056373739)]

# ---------- Approach A: constant lambda ----------
print("=== Approach A: z=tau, lam=constant ===")
print("[z^k] G = 2 lam^k (lam-1)^{k-1}")
print("Match b_1: 2 lam = 3 -> lam = 3/2")
print("Then b_2 should be 2 lam^2 (lam-1) = 2 (9/4)(1/2) = 9/4. Actual b_2 = 27. MISMATCH.")

# ---------- Approach B: lam = 3/2 + lam_1 tau + lam_2 tau^2 + ... ----------
print("\n=== Approach B: z=tau, lam(tau) power series ===")

# Represent lam(tau) as a Poly in tau; we build it coefficient by coefficient.
lam_syms = symbols(f'l0:{LamMax}')
# Actually since we know l0 = 3/2 fixed, treat sequentially.

# Convert lam and mu = lam*(lam-1) to polynomial truncations up to degree N-1.
# For each k=1..N, compute [tau^{k-1}] (lam * mu^{k-1}) and set to b_k / 2.
# This determines lam_{k-1} because lam_{k-1} first appears at [tau^{k-1}] lam.

N = LamMax
# Build lam as list of coefficients [l0, l1, ..., l_{N-1}], each rational (l0=3/2 fixed).
lam_coeffs = [Rational(3, 2)]  # l0

def series_mul(a, b, N):
    """Multiply two length-N truncated series."""
    c = [Rational(0)] * N
    for i in range(N):
        if a[i] == 0:
            continue
        for j in range(N - i):
            c[i + j] += a[i] * b[j]
    return c

def series_pow(a, k, N):
    """Raise truncated series a to integer power k."""
    result = [Rational(0)] * N
    result[0] = Rational(1)
    for _ in range(k):
        result = series_mul(result, a, N)
    return result

# We solve for l1, l2, ..., l_{N-1} sequentially.
for k in range(2, N + 1):
    # Need to determine lam_{k-1} from b_k.
    # Formula: b_k = 2 [tau^{k-1}] (lam * mu^{k-1}), mu = lam*(lam-1).
    # Add a symbol for the next lambda coefficient and solve linearly.
    l_next = symbols(f'l{k-1}')
    lam_trial = lam_coeffs + [l_next] + [Rational(0)] * (N - k)
    # Compute mu = lam*(lam-1) mod tau^{k}, then mu^{k-1} mod tau^{k}, then lam*mu^{k-1} mod tau^{k}
    # Truncate to degree k-1.
    T = k  # length
    # subtract 1 in constant term for (lam - 1)
    lam_minus_1 = lam_trial[:T].copy()
    lam_minus_1[0] = lam_minus_1[0] - 1
    mu = series_mul(lam_trial[:T], lam_minus_1, T)
    mu_pow = series_pow(mu, k - 1, T)
    lam_mu_pow = series_mul(lam_trial[:T], mu_pow, T)
    coeff = lam_mu_pow[k - 1]  # [tau^{k-1}]
    coeff = expand(coeff)
    target = b[k] / 2
    from sympy import solve
    sol = solve(coeff - target, l_next)
    if not sol:
        print(f"  k={k}: NO SOLUTION for l_{k-1} — degenerate.")
        break
    lam_coeffs.append(sol[0])
    print(f"  k={k}: lam_{k-1} = {sol[0]}")

print("\nFinal lam(tau) coefficients:")
for i, lc in enumerate(lam_coeffs):
    from sympy import fraction, together, factorint
    num, den = fraction(together(lc))
    print(f"  lam_{i} = {lc}   (num factors: {factorint(abs(int(num))) if num != 0 else '0'}, den factors: {factorint(int(den))})")
