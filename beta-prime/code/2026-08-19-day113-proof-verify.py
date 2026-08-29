"""Verify all algebraic identities in the Lemma 1 proof.

Proof structure:
  1. A_1 = alpha * A_0 - s*_{(j+1,0)} + B_j (decomposition, structurally derived)
  2. A_0 = (b+c)^{↓j} (Slice-0)
  3. Central Lemma: s*_{(j+1,0)} - B_j = (sigma-1)^{↓(j+1)} - j*pi*(sigma-3)^{↓(j-1)}
  4. Slice-0 & Central Lemma via interpolation on shifted-Schur basis.
     Key identity 1 (Slice-0 coefficient match):
       binom(j, m3)*(j - 2*m3 + 1)/(j - m3 + 1) = j!*(j - 2*m3 + 1)/((j+1-m3)!*m3!)
     Key identity 2 (Central Lemma coefficient match):
       c_{m3,j} = j*(j-1)!*(j+2-2*m3)/((j+1-m3)!*(m3-1)!)
       where c_{m3,j} is the combinatorial sum.
  5. Final algebraic identity:
       (3-j)(b+c)(b+c-1) + 2*(b+1)*c*(b+c-j)
         = (b+c)(2bc+3b+5c-3) - j*(b^2 + 4bc + c^2 - b + c)
"""

import sympy as sp
from sympy import symbols, expand, simplify, factorial, binomial, Integer, Rational, Symbol

b, c, j = symbols('b c j', integer=True)
m3 = symbols('m3', integer=True)


def check(desc, lhs, rhs):
    diff = expand(lhs - rhs)
    status = "OK" if diff == 0 else f"FAIL: diff = {diff}"
    print(f"  {desc}: {status}")
    return diff == 0


def main():
    print("=" * 72)
    print("KEY ALGEBRAIC IDENTITIES IN LEMMA 1 PROOF")
    print("=" * 72)

    print("\n[1] Slice-0 coefficient identity:")
    print("     binom(j, m3)*(j-2*m3+1)/(j-m3+1) = j!*(j-2*m3+1)/[(j+1-m3)! * m3!]")
    # LHS
    lhs1 = binomial(j, m3) * (j - 2*m3 + 1) / (j - m3 + 1)
    rhs1 = factorial(j) * (j - 2*m3 + 1) / (factorial(j + 1 - m3) * factorial(m3))
    diff = sp.simplify(lhs1 - rhs1)
    print(f"    diff = {diff}  {'OK' if diff == 0 else 'FAIL'}")

    print("\n[2] Central Lemma coefficient identity (for m3 >= 2):")
    print("     binom(j+1, m3)*(j+2-2*m3)/(j+2-m3) + (m3-1)*(j+1-2*m3)/(j+1-m3)*binom(j, m3) + binom(j, m3-2)")
    print("     = j*(j-1)!*(j+2-2*m3)/[(j+1-m3)! * (m3-1)!]")
    lhs2 = (binomial(j + 1, m3) * (j + 2 - 2*m3) / (j + 2 - m3)
            + (m3 - 1) * (j + 1 - 2*m3) / (j + 1 - m3) * binomial(j, m3)
            + binomial(j, m3 - 2))
    rhs2 = j * factorial(j - 1) * (j + 2 - 2*m3) / (factorial(j + 1 - m3) * factorial(m3 - 1))
    diff = sp.simplify(lhs2 - rhs2)
    print(f"    diff = {diff}  {'OK' if diff == 0 else 'FAIL'}")

    print("\n[2b] Central Lemma coefficient identity (for m3 = 1):")
    print("     j (only term from second sum, no B_j contribution)")
    print("     = j*(j-1)!*(j+2-2)/[(j+1-1)! * (1-1)!]  (with m3=1)")
    lhs2b = Integer(1) * j  # coefficient c_{1, j} = j
    rhs2b = j * factorial(j - 1) * (j + 2 - 2) / (factorial(j) * factorial(0))
    diff = sp.simplify(lhs2b - rhs2b)
    print(f"    diff = {diff}  {'OK' if diff == 0 else 'FAIL'}")

    print("\n[3] Final algebraic identity:")
    print("     (3-j)(b+c)(b+c-1) + 2*(b+1)*c*(b+c-j) = (b+c)*(2bc+3b+5c-3) - j*(b^2+4bc+c^2-b+c)")
    lhs3 = (3 - j) * (b + c) * (b + c - 1) + 2 * (b + 1) * c * (b + c - j)
    rhs3 = (b + c) * (2*b*c + 3*b + 5*c - 3) - j * (b**2 + 4*b*c + c**2 - b + c)
    diff = expand(lhs3 - rhs3)
    print(f"    diff = {diff}  {'OK' if diff == 0 else 'FAIL'}")

    print("\n[4] Sub-leading formula: 2*j - binom(j+2, 2) + (y_2+y_3) = b+c - binom(j, 2)")
    print("     with y_2 = b+1, y_3 = c")
    lhs4 = 2*j - (j + 2) * (j + 1) / 2 + (b + 1) + c
    rhs4 = b + c - j * (j - 1) / 2
    diff = sp.simplify(lhs4 - rhs4)
    print(f"    diff = {diff}  {'OK' if diff == 0 else 'FAIL'}")

    print("\n[5] Reformulated central identity (with substitutions):")
    print("     alpha*(b+c)^↓j - (b+c)^↓(j+1) = j*(3-j)/2 * (b+c)^↓j")
    print("     (i.e., alpha - (b+c-j) = j*(3-j)/2)")
    alpha = b + c - j * (j - 1) / 2
    lhs5 = alpha - (b + c - j)
    rhs5 = j * (3 - j) / 2
    diff = sp.simplify(lhs5 - rhs5)
    print(f"    diff = {diff}  {'OK' if diff == 0 else 'FAIL'}")


if __name__ == "__main__":
    main()
