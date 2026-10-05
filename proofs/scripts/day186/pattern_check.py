#!/usr/bin/env python3
"""
Day 186: check the pattern
  X_n = sum_{k=1}^n A_k^{(n)}(q) h_k X_{n-k}
where empirically:
  n=2: (q+1, -(q+1))            = ([2], -[2])
  n=3: (q+1, -[3], [3])         = ([2], -[3], [3])
  n=4: (q+1, -[3], [4], -[4])   = ([2], -[3], [4], -[4])

Guess: A_k^{(n)} = (-1)^{k-1} * (something).
Or: A_k^{(n)} for k=1: [2]_q. For k>=2: (-1)^{k-1} * [max(k, n-k+1)]_q?

n=2, k=2: A=-[2] = -[max(2,1)]_q = -[2]. ✓
n=3, k=2: A=-[3] = -[max(2,2)]_q = -[2]?  NO — we have -[3]_q. So [max(k, n-k+1)]... hmm.
n=3, k=3: A=[3] = [max(3, 1)]_q = [3]. ✓
n=4, k=2: A=-[3]_q = -[max(2, 3)]_q = -[3]. ✓
n=4, k=3: A=[4]_q = [max(3, 2)]_q = [3]? NO — [4]_q, not [3]_q. Hmm.

Try: A_k^{(n)} for k = 1: [2]_q; for k = 2..n-1: (-1)^{k-1} [n]_q or [k+1]_q?
n=2, k=2: -[2]. [n]=[2] ✓
n=3, k=2: -[3]. [n]=[3] ✓
n=3, k=3: [3]. [n]=[3] ✓
n=4, k=2: -[3]. [n]=[4] ✗ but [n-1]=[3] ✓
n=4, k=3: [4]. [n]=[4] ✓
n=4, k=4: -[4]. [n]=[4] ✓

Try: A_k^{(n)} = (-1)^{k-1} [something depending on k, n].
n=2: k=1: [2] = [k+1] = [2].  k=2: -[2] = -[k] = -[2].
n=3: k=1: [2] = [k+1] = [2].  k=2: -[3] = -[k+1] = -[3].  k=3: [3] = [k] = [3].
n=4: k=1: [2] = [k+1].          k=2: -[3] = -[k+1].          k=3: [4] = [k+1] = [4].       k=4: -[4] = -[k] = -[4].

Hypothesis: A_k^{(n)} = (-1)^{k-1} [k+1]_q  for k < n,  and A_n^{(n)} = (-1)^{n-1} [n]_q.
Equivalently:  A_k^{(n)} = (-1)^{k-1} [k+1]_q     if k < n
              A_n^{(n)} = (-1)^{n-1} [n]_q       (drops by 1)

Check:
n=2: A_1 = [2], A_2 = -[2].  ✓ (matches k=1: (+)[2]; k=n=2: (-)[2])
n=3: A_1 = [2], A_2 = -[3], A_3 = [3]. ✓
n=4: A_1 = [2], A_2 = -[3], A_3 = [4], A_4 = -[4]. ✓

YES! Clean pattern.

Rewrite:
  X_n = [2] h_1 X_{n-1} + sum_{k=2}^{n-1} (-1)^{k-1} [k+1]_q h_k X_{n-k}
        + (-1)^{n-1} [n]_q h_n

If we naively used A_n = (-1)^{n-1} [n+1]_q, we'd add:
  extra = (-1)^{n-1} ([n+1]_q - [n]_q) h_n = (-1)^{n-1} q^n h_n
So the recursion could be written as:
  X_n = sum_{k=1}^n (-1)^{k-1} [k+1]_q h_k X_{n-k}  -  (-1)^{n-1} q^n h_n

i.e. clean "shift by q^n h_n":
  X_n = sum_{k=1}^n (-1)^{k-1} [k+1]_q h_k X_{n-k}  +  (-1)^n q^n h_n

Let me test this.
"""

from sympy import symbols, expand, simplify, factor, Rational, Integer, Poly

q = symbols('q')
h1, h2, h3, h4, h5, h6 = symbols('h1 h2 h3 h4 h5 h6', commutative=True)

X = {
    0: Integer(1),
    1: h1,
    2: (q + 1) * h1**2 - (q + 1) * h2,
    3: (q**2 + q + 1) * h3 - (2*q**2 + 3*q + 2) * h2 * h1 + (q + 1)**2 * h1**3,
    4: -(q + 1)*(q**2 + 1) * h4 + (q + 1)*(2*q**2 + q + 2) * h3 * h1
       + (q + 1)*(q**2 + q + 1) * h2**2
       - (q + 1)*(3*q**2 + 4*q + 3) * h2 * h1**2
       + (q + 1)**3 * h1**4,
}
h_map = {1: h1, 2: h2, 3: h3, 4: h4, 5: h5}

def q_int(k):
    """[k]_q = 1 + q + ... + q^{k-1}."""
    return sum(q**j for j in range(k))

print("=== TEST: X_n =? sum_{k=1}^n (-1)^{k-1} [k+1]_q h_k X_{n-k} + (-1)^n q^n h_n ===")
for n in range(1, 5):
    predicted = sum((-1)**(k-1) * q_int(k+1) * h_map[k] * X[n-k] for k in range(1, n+1))
    predicted += (-1)**n * q**n * h_map[n]
    diff = expand(X[n] - predicted)
    print(f"n={n}: diff = {diff}  {'PASS' if diff == 0 else 'FAIL'}")

print()
print("=== ALTERNATE FORM: X_n = sum_{k=1}^{n-1} (-1)^{k-1} [k+1]_q h_k X_{n-k} + (-1)^{n-1} [n]_q h_n ===")
for n in range(1, 5):
    predicted = sum((-1)**(k-1) * q_int(k+1) * h_map[k] * X[n-k] for k in range(1, n))
    predicted += (-1)**(n-1) * q_int(n) * h_map[n]
    diff = expand(X[n] - predicted)
    print(f"n={n}: diff = {diff}  {'PASS' if diff == 0 else 'FAIL'}")

print()
print("=== Generating function form ===")
print("If X_n = sum_{k=1}^n A_k h_k X_{n-k} + delta_k = ..., and if we can find a")
print("CLEAN identity, we'd get a functional equation for Z(z) = sum X_n z^n.")
print()
print("Reformulation attempt: write the CORRECTION as boundary term.")
print("Predicted recursion (form 1):")
print("  X_n = sum_{k=1}^n (-1)^{k-1} [k+1]_q h_k X_{n-k} + (-1)^n q^n h_n")
print()
print("Multiply by z^n and sum over n >= 1:")
print("  Z(z) = sum_{n>=1} X_n z^n")
print("  sum_{n>=1} sum_{k=1}^n (-1)^{k-1} [k+1]_q h_k X_{n-k} z^n")
print("     = sum_{k>=1} (-1)^{k-1} [k+1]_q h_k z^k * (1 + Z(z))")
print("       [since X_0=1 so the inner sum is (1+Z(z))]")
print("  sum_{n>=1} (-1)^n q^n h_n z^n = sum_{n>=1} (-qz)^n h_n / ? ")
print("  Not immediate to close because h_n's are algebraically independent.")
print()
print("Formal GF (in the polynomial ring Q(q)[h_1, h_2, ...][[z]]):")
print("  Z(z) = K(z) * (1 + Z(z)) + R(z)")
print("  where K(z) = sum_{k>=1} (-1)^{k-1} [k+1]_q h_k z^k")
print("        R(z) = sum_{n>=1} (-1)^n q^n h_n z^n")
print()
print("So: Z(z) = (K(z) + R(z)) / (1 - K(z))")
print()
print("Let's verify by expanding:")

# Compute K and R as formal series to order 5:
from sympy import series, Symbol
z = symbols('z')
K = sum((-1)**(k-1) * q_int(k+1) * h_map[k] * z**k for k in range(1, 5))
R = sum((-1)**n * q**n * h_map[n] * z**n for n in range(1, 5))
print(f"K(z) = {K}")
print(f"R(z) = {R}")

# Z(z) = (K + R) / (1 - K), expand to order 4:
# Compute (K+R) * (1 + K + K^2 + K^3 + K^4) truncated
Kpow = [Integer(1), K, expand(K*K), expand(K*K*K), expand(K*K*K*K)]
inv = sum(Kpow)  # 1/(1-K) up to order 4
Z_computed = expand((K + R) * inv)

# Truncate at z^4:
Zp = Poly(Z_computed, z, *[h_map[i] for i in range(1, 5)])
Z_z_terms = {}
for (mon, coef) in Zp.as_dict().items():
    zpow = mon[0]  # z is first
    if zpow > 4:
        continue
    hmon = mon[1:]
    Z_z_terms.setdefault(zpow, Integer(0))
    # rebuild h monomial
    hterm = Integer(1)
    for i, e in enumerate(hmon):
        hterm *= [h1, h2, h3, h4][i]**e
    Z_z_terms[zpow] += coef * hterm

for zp in sorted(Z_z_terms.keys()):
    print(f"\n[z^{zp}] of GF: {expand(Z_z_terms[zp])}")
    if zp in X:
        diff = expand(Z_z_terms[zp] - X[zp])
        print(f"    Expected X_{zp} = {X[zp]}")
        print(f"    diff = {diff}  {'MATCH' if diff == 0 else 'MISMATCH'}")
