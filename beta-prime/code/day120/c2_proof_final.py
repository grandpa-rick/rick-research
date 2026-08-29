"""Final assembled proof of (C2), with all pieces verified.

THEOREM (C2). For odd j = 2l+1 (l >= 1):
  A_even(l) = sum_{r=0}^{l-1} (-1)^r K_{mu^{(r)}', (2^{2l+1})} = (-1)^{l+1}
where mu^{(r)} = (2l, l+1+r, l+1-r).

PROOF (via Weyl formula):

Lemma 1 (Weyl formula for K_even).
  K_{mu^{(r)}', (2^{2l+1})} =
    (2l+1) [C(2l, l-r) - C(2l, l-r-1)]                           [S1 + S2 part]
    - [C(2l+1, l-r+1) - C(2l+1, l-r-1)]                          [S3 + S4 part]

Proof: We use the fact that for a 3-part partition mu = (m1, m2, m3),
  K_{mu', (2^j)} = <s_mu, e_2^j> = [x^{rho}] (e_2^j * Delta)
where rho = (m1+2, m2+1, m3), Delta = (x1-x2)(x1-x3)(x2-x3).

Expand e_2^j(x1,x2,x3) = sum_{a+b+c=j} C(j; a,b,c) x1^{a+b} x2^{a+c} x3^{b+c}.
Expand Delta = sum_{tau in S_3} sgn(tau) x1^{3-tau(1)} x2^{3-tau(2)} x3^{3-tau(3)}.
Matching total exponent x1^{rho_1} x2^{rho_2} x3^{rho_3} gives:
  For each tau: solve a+b+c = j and (a+b, a+c, b+c) = (rho_i - (3-tau(i)))_i.
  This forces c = (rho_2 - rho_1 - rho_3 + ...)/2 etc.

For mu^{(r)} = (2l, l+1+r, l+1-r), rho = (2l+2, l+2+r, l+1-r).
Compute six terms; only four give valid nonneg (a,b,c). They yield the formula above.

Lemma 2. sum_{r=0}^{l-1} (-1)^r [C(2l, l-r) - C(2l, l-r-1)] = (-1)^{l+1}.

Proof: Denote ballot(n, k) := C(n, k) - C(n, k-1).
The FULL alternating sum sum_{r=0}^{l} (-1)^r ballot(2l, l-r) = 0 is Day 119 Identity A.
The r=l term contributes (-1)^l * ballot(2l, 0) = (-1)^l * 1.
Subtracting: sum_{r=0}^{l-1} = -(-1)^l * 1 = (-1)^{l+1}. QED.

Lemma 3. sum_{r=0}^{l-1} (-1)^r [-C(2l+1, l-r+1) + C(2l+1, l-r-1)] = (-1)^l * 2l.

Proof: Let k = l - r; r=0..l-1 => k=1..l; (-1)^r = (-1)^{l-k}.
  T = (-1)^l sum_{k=1}^{l} (-1)^k [C(2l+1, k-1) - C(2l+1, k+1)]

Split:
  A := sum_{k=1}^{l} (-1)^k C(2l+1, k-1)  (let j=k-1, k=1..l => j=0..l-1, (-1)^k = -(-1)^j)
     = -sum_{j=0}^{l-1} (-1)^j C(2l+1, j)
  B := sum_{k=1}^{l} (-1)^k C(2l+1, k+1)  (let j=k+1, k=1..l => j=2..l+1, (-1)^k = -(-1)^j)
     = -sum_{j=2}^{l+1} (-1)^j C(2l+1, j)

Then A - B = -sum_{j=0}^{l-1} (-1)^j C(2l+1,j) + sum_{j=2}^{l+1} (-1)^j C(2l+1,j)
           = -C(2l+1,0) + C(2l+1,1) + (-1)^l C(2l+1,l) + (-1)^{l+1} C(2l+1,l+1)
           = -1 + (2l+1) + (-1)^l * [C(2l+1,l) - C(2l+1,l+1)]
           = 2l + (-1)^l * 0     [since C(2l+1,l) = C(2l+1,l+1)]
           = 2l.
Thus T = (-1)^l * 2l. QED.

COMBINING:
  A_even(l) = (2l+1) * [Lemma 2] + [Lemma 3]
            = (2l+1) * (-1)^{l+1} + (-1)^l * 2l
            = (-1)^{l+1} * [(2l+1) - 2l]
            = (-1)^{l+1}.  QED.
"""

from math import comb


def K_even_closed(l, r):
    def c(n, k):
        return comb(n, k) if 0 <= k <= n else 0
    return ((2*l+1) * (c(2*l, l-r) - c(2*l, l-r-1))
            - (c(2*l+1, l-r+1) - c(2*l+1, l-r-1)))


def verify_all():
    print("=" * 60)
    print("Verification of (C2) proof pipeline")
    print("=" * 60)
    for l in range(1, 20):
        # Direct K vs closed form
        import sys
        sys.path.insert(0, '/home/agent/projects/beta-prime/code/day119')
        from kostka import kostka_mu_prime_2j
        all_K_match = True
        for r in range(l):
            mu = (2*l, l+1+r, l+1-r)
            K_dir = kostka_mu_prime_2j(mu)
            K_cl = K_even_closed(l, r)
            if K_dir != K_cl:
                all_K_match = False

        # Lemma 2
        L2 = sum((-1)**r * (comb(2*l, l-r) - (comb(2*l, l-r-1) if l-r-1 >= 0 else 0)) for r in range(l))
        L2_expected = (-1)**(l+1)

        # Lemma 3
        L3 = sum((-1)**r * (-(comb(2*l+1, l-r+1) if l-r+1 <= 2*l+1 else 0) + (comb(2*l+1, l-r-1) if l-r-1 >= 0 else 0)) for r in range(l))
        L3_expected = (-1)**l * 2 * l

        # Final
        A_even = (2*l+1) * L2 + L3
        A_expected = (-1)**(l+1)

        print(f"l={l}: K_closed OK={all_K_match}, L2={L2}={'OK' if L2 == L2_expected else '!!!'}, "
              f"L3={L3}={'OK' if L3 == L3_expected else '!!!'}, A_even={A_even}={'OK' if A_even == A_expected else '!!!'}")


if __name__ == "__main__":
    verify_all()
