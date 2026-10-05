"""
Day 189 secondary — probe Hikita's Thm 3.12 star-Pieri rule at small n.

Hikita 2503.23597 Thm 3.12:
    e_1 ⋆ e_r = (1 - q^{-1})[r+1]_t e_{r+1} + q^{-1} e_1 e_r

Compute e_1^{⋆ 2}, e_1^{⋆ 3}, and check specialization q=1 (should reduce
to (ordinary) e_1^n = X_{disconnected n vertices} up to N-twist).

The star-product is not distributive over ordinary product without a
Leibniz rule, so we can only iterate ⋆ against e-basis atoms directly
from Thm 3.12. This script computes only iterated e_1 ⋆ e_1 ⋆ ... ⋆ e_1,
tracking the e-expansion via successive applications of Thm 3.12 combined
with bilinearity of ⋆.

Bilinearity assumption: (a·F + b·G) ⋆ H = a·(F ⋆ H) + b·(G ⋆ H).

For F ⋆ (a·G + b·H) similarly (⋆ is commutative and associative per
sub-agent report from Hikita §3).

Problem: Thm 3.12 gives e_1 ⋆ e_r, i.e. one factor is e_1 and the other
is e_r (a single e-monomial atom). For terms like e_1 ⋆ (e_1 e_r) we
have NO given rule — we'd need a Leibniz-like rule, which is not stated.

However, since ⋆ is associative:
    e_1 ⋆ e_1 ⋆ e_r = e_1 ⋆ (e_1 ⋆ e_r) = (e_1 ⋆ e_1) ⋆ e_r
so we can build up by iterated left-application of e_1 ⋆ ·, provided
we always have a single-e-atom right operand. Since our starting element
is e_r (single atom) and each e_1 ⋆ e_r step produces e_{r+1} (single
atom) + e_1 e_r (product atom).

The e_1 e_r term ambiguity: does it mean e_1 ⋆ e_r or e_1 · e_r? From
Thm 3.12: "e_1 e_r" is the ORDINARY product. And in the next step
(e_1 ⋆ (e_1 · e_r)) we need a Leibniz rule.

So Thm 3.12 alone is INSUFFICIENT to compute e_1^{⋆ 3} without more
of Hikita's machinery.

WHAT WE CAN DO: compute e_1 ⋆ e_1 (unambiguously), and confirm the
answer specializes correctly.
"""

from sympy import Symbol, symbols, expand, simplify, sympify, Poly


def q_int_t(k, t):
    """[k]_t = 1 + t + t^2 + ... + t^{k-1}."""
    return sum(t**i for i in range(k))


def main():
    q, t = symbols('q t')

    # e-basis atoms; represent as formal symbols and track by name
    # We'll work in a symbolic ring with atoms e_1, e_2, e_3, and their
    # ordinary products.
    e = symbols('e_1 e_2 e_3 e_4 e_5')
    e1, e2, e3, e4, e5 = e

    print("=" * 78)
    print("Day 189 secondary — Hikita Thm 3.12 star-Pieri rule at n=2, 3")
    print("=" * 78)

    # e_1 ⋆ e_1 by Thm 3.12 with r=1
    e1_star_e1 = (1 - q**-1) * q_int_t(2, t) * e2 + q**-1 * e1**2
    print("\ne_1 ⋆ e_1 = (1 - q^{-1})[2]_t e_2 + q^{-1} e_1^2")
    print(f"         = {expand(e1_star_e1)}")

    print("\nSpecialization q=t=1:")
    print(f"  e_1 ⋆ e_1 |_{{q=1, t=1}} = {expand(e1_star_e1.subs([(q,1), (t,1)]))}")
    print(f"  Expected: e_1^2 (totally disconnected 2 vertices, ordinary product)")

    print("\nSpecialization q=1 (t free):")
    print(f"  e_1 ⋆ e_1 |_{{q=1}} = {expand(e1_star_e1.subs(q, 1))}")
    print(f"  Expected: e_1^2 (since (1-q^{{-1}}) = 0 kills first term)")

    # e_1 ⋆ e_r for r=2
    e1_star_e2 = (1 - q**-1) * q_int_t(3, t) * e3 + q**-1 * e1 * e2
    print("\ne_1 ⋆ e_2 = (1 - q^{-1})[3]_t e_3 + q^{-1} e_1 e_2")
    print(f"         = {expand(e1_star_e2)}")

    # Attempt to compute e_1 ⋆ (e_1 ⋆ e_1) via associativity
    # e_1 ⋆ (e_1 ⋆ e_1) = (e_1 ⋆ e_1) ⋆ e_1 — right side is
    # (1-q^{-1})[2]_t (e_2 ⋆ e_1) + q^{-1} (e_1^2 ⋆ e_1)
    #
    # e_2 ⋆ e_1 = e_1 ⋆ e_2 (commutativity) = above formula.
    # e_1^2 ⋆ e_1 = ??? Needs Leibniz rule for ⋆ against ordinary product.
    #   NOT IN THM 3.12.

    print("\n" + "-" * 78)
    print("BLOCKER — cannot compute e_1^{⋆ 3} from Thm 3.12 alone:")
    print("  e_1 ⋆ (e_1 ⋆ e_1) = (1-q^{-1})[2]_t (e_2 ⋆ e_1) + q^{-1} (e_1^2 ⋆ e_1)")
    print("  e_2 ⋆ e_1 = commutativity + Thm 3.12: available (= e_1 ⋆ e_2)")
    print("  e_1^2 ⋆ e_1 = REQUIRES Leibniz-type rule for ⋆ against ordinary product.")
    print("  Hikita's Thm 3.12 gives only e_1 ⋆ e_r (one atom on right).")
    print("  A full recursion for X_{P_n}(q,t) requires the Hecke-operator")
    print("  machinery from Hikita §2, not just Thm 3.12.")
    print("-" * 78)

    print("\nAt q=t=1 sanity check:")
    print(f"  e_1 ⋆ e_2 |_{{q=t=1}} = {expand(e1_star_e2.subs([(q,1),(t,1)]))}")
    print(f"  Expected: e_1 e_2 (since ⋆ reduces to ordinary product at q=1)")

    print("\nAt q=1 (t free):")
    print(f"  e_1 ⋆ e_2 |_{{q=1}} = {expand(e1_star_e2.subs(q,1))}")

    print("\n" + "=" * 78)
    print("Conclusion: Thm 3.12 is a Pieri rule with e_1 on the left AND")
    print("a single e_r atom on the right. To iterate and derive a full")
    print("recursion for X_{P_n}(q,t), one needs Hikita's Hecke operators")
    print("(Theorem A, §2) and/or a Leibniz-like formula for ⋆ against ·.")
    print("This is out-of-scope for the current PROVE session.")
    print("=" * 78)


if __name__ == '__main__':
    main()
