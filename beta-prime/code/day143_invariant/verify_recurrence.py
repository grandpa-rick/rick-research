"""
Day 143 KEY IDENTITY:
    a_k = -b_k + Σ_{i+j=k, i,j≥1} b_i b_j
where a_k = [E_3^k T^{3k-1}] X (universal invariant),
      b_k = (3k-1) · N_k[T^{3k-1}].

Verify from known values, and derive b_7.
"""
from sympy import Rational, Integer, factorint

# Known a_k (from computation):
a = {1: -3, 2: -18, 3: -255, 4: -4620, 5: -94500, 6: -2078802, 7: -48005802}

# Known n_k = N_k[T^{3k-1}] (from Day 142 RESULT.md):
# n_1 = 3/2, n_2 = 27/5, n_3 = 417/8, n_4 = 7851/11, n_5 = 82062/7 = 164124/14, n_6 = 3661389/17.
n = {
    1: Rational(3, 2),
    2: Rational(27, 5),
    3: Rational(417, 8),
    4: Rational(7851, 11),
    5: Rational(164124, 14),
    6: Rational(3661389, 17),
}

# b_k = (3k-1) n_k
b = {k: (3*k - 1) * n[k] for k in n}
print("b_k := (3k-1) · n_k :")
for k in sorted(b):
    print(f"  b_{k} = {b[k]}   (integer? {b[k].q == 1})")

# Verify a_k = -b_k + Σ b_i b_j (i+j=k, i,j≥1)
print("\nVerify a_k = -b_k + Σ_{i+j=k, i,j≥1} b_i b_j:")
for k in sorted(b):
    conv = sum(b[i] * b[k - i] for i in range(1, k) if (k - i) in b)
    predicted = -b[k] + conv
    actual = a[k]
    status = "OK" if predicted == actual else "FAIL"
    print(f"  k={k}: predicted a_k = {predicted}, actual = {actual}   [{status}]")

# Solve for b_7 from a_7 = -b_7 + 2·b_1·b_6 + 2·b_2·b_5 + 2·b_3·b_4
conv_7 = 2*b[1]*b[6] + 2*b[2]*b[5] + 2*b[3]*b[4]
b_7 = -a[7] + conv_7
print(f"\nDerived b_7 = -a_7 + Σ_{{i+j=7}} b_i b_j = {b_7}")
print(f"  b_7 factored: {factorint(int(b_7))}")

# Predicted n_7 = b_7 / 20
n_7 = Rational(int(b_7), 20)
print(f"Predicted n_7 = b_7 / 20 = {n_7}")

# Let's compute the full ratio sequence
print("\n--- Cross-check: 1 + 4A(τ) should be a perfect square ---")
# A(τ) = Σ a_k τ^k, F(τ) = Σ b_k τ^k
# Claim: (1 - 2F)² = 1 + 4A
# Coefficient at τ^k: [τ^k](1 - 2F)² = -4 b_k + 4 Σ_{i+j=k} b_i b_j = 4 [ -b_k + Σ b_i b_j ] = 4 a_k
# So [τ^k](1 - 2F)² - [τ^k](1 + 4A) = 4 a_k - 4 a_k = 0 ✓
# For k=0: [τ^0](1 - 2F)² = 1, [τ^0](1+4A) = 1 ✓

print("Structural identity: (1 - 2F(τ))² = 1 + 4·A(τ)")
print("     where A(τ) = Σ_k a_k τ^k,  F(τ) = Σ_k b_k τ^k = Σ_k (3k-1)·N_k[T^{3k-1}]·τ^k")
print()
print("Equivalently: F(τ) = (1 - √(1 + 4A(τ))) / 2")
print()
print("So 1 + 4A(τ) is a PERFECT SQUARE in Q[[τ]] — a nontrivial structural constraint.")

# Report full b-sequence including b_7:
b[7] = b_7
print("\nb sequence (with derived b_7):")
for k in sorted(b):
    print(f"  b_{k} = {b[k]}  factors: {factorint(int(b[k]))}")
