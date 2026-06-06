"""
Type C_n: verify the chain factor structure transfers from B_n with E_n <-> F_n relabeling.

C_n positive roots: {E_i - E_j, E_i + E_j (i < j), 2 E_i}. The short-long edge is at
a_{n-1,n} = -1, a_{n,n-1} = -2 — but now alpha_n = 2 E_n is LONG, and alpha_{n-1} = E_{n-1} - E_n
is SHORT.  (Magnitudes swapped from B_n: in B_n, alpha_n short, alpha_{n-1} long.)

For the C_n short-long-edge tensor rule, we act with B_{n-1} (the short coideal generator
of the type-AI/AII coideal subalgebra of U_q(C_n) at type C_n short root alpha_{n-1}).

For the alpha_{n-1}-action on C_n:
  alpha_{n-1}-string structure on Phi^+(C_n):
  - Take chain through alpha_a = E_a - E_{a+1} ... actually no, let's pick chain through what?

Actually for type C_n with edge a_{n,n-1} = -2 (long-side coefficient), the short simple is
alpha_{n-1}, and the magnitude |a_{n,n-1}| = 2 still produces the length-3 chain through some
fixed-by-alpha_{n-1} long root.

Let me work this out concretely for C_2 = B_2 as a sanity check (Lie algebras isomorphic but
different conventions).

For C_3 specifically:
  Phi^+(C_3) = {E_1-E_2, E_1-E_3, E_2-E_3 (short long-like differences),
                E_1+E_2, E_1+E_3, E_2+E_3 (short sums),
                2 E_1, 2 E_2, 2 E_3 (long doubles)}.
  alpha_1 = E_1 - E_2, alpha_2 = E_2 - E_3 (short), alpha_3 = 2 E_3 (long).

The short-long edge is between alpha_2 and alpha_3:
  a_{23} = <alpha_2, alpha_3^v> = <E_2 - E_3, E_3> = -1.
  a_{32} = <alpha_3, alpha_2^v> = <2 E_3, E_2 - E_3> = -2.

So the short simple is alpha_2 (with pairing -2 with alpha_3 — i.e., 'j' contributing m=2 to short
i=2). The chain factor would be through chain roots fixed by alpha_2.

alpha_2-action on Phi^+(C_3): pairings <beta, alpha_2^v>:
  E_1-E_2: <E_1-E_2, E_2-E_3> = -1
  E_1-E_3: <E_1-E_3, E_2-E_3> = 0
  E_2-E_3: pairing 2 (self)
  E_1+E_2: <E_1+E_2, E_2-E_3> = 1
  E_1+E_3: <E_1+E_3, E_2-E_3> = -1
  E_2+E_3: <E_2+E_3, E_2-E_3> = 0
  2 E_1:   <2 E_1, E_2-E_3> = 0
  2 E_2:   <2 E_2, E_2-E_3> = 2
  2 E_3:   <2 E_3, E_2-E_3> = -2

Sorting into alpha_2-strings (each beta has chain {beta-k alpha_2, ..., beta+l alpha_2}):
  alpha_2 = E_2 - E_3 (pairing +2, top of its chain since alpha_2 + alpha_2 = 2E_2 - 2 E_3 not in Phi+)
    Chain: from alpha_2 + alpha_2 = 2(E_2 - E_3) — not a root. Chain goes from alpha_2 down by alpha_2.
    Wait, alpha_2 has pairing +2, so it's at TOP of a length-3 string in Phi unrestricted.
    In Phi+: alpha_2 - alpha_2 = 0 (remove), alpha_2 (self), alpha_2 + alpha_2 = 2 E_2 - 2 E_3 (not a root).
    So alpha_2 is a SINGLETON (pairing 2 self-loop) like alpha_n in B_n.

  Better partitioning:
    - Singleton at alpha_2 = E_2 - E_3 (pairing +2 like B_n singleton).
    - Chain through 2 E_3 (pairing -2): {2 E_3, 2 E_3 + alpha_2 = ?}
      2 E_3 + (E_2 - E_3) = E_2 + E_3 (pairing 0 with alpha_2 — wait <E_2+E_3, E_2-E_3> = 1-1 = 0 ✓).
      E_2 + E_3 + (E_2 - E_3) = 2 E_2. <2E_2, E_2-E_3> = 2 ✓ (top).
      So chain: {2 E_3, E_2 + E_3, 2 E_2}, pairings {-2, 0, +2}. Length 3 (m=2). ✓

    - Chain through E_1 - E_2 (pairing -1):
      E_1 - E_2 + alpha_2 = E_1 - E_3 (pairing 0).
      E_1 - E_3 + alpha_2 = E_1 - E_3 + E_2 - E_3 — not a root.  Wait E_1 - E_3 + E_2 - E_3 = E_1 + E_2 - 2 E_3 not a root.
      Hmm so chain is {E_1 - E_2, E_1 - E_3}, length 2 (m=1, simply-laced).

    - Chain through E_1 + E_3 (pairing -1):
      E_1 + E_3 + alpha_2 = E_1 + E_2 (pairing 1). Top.
      So chain: {E_1 + E_3, E_1 + E_2}, length 2 (m=1, simply-laced).

    - 2 E_1 (pairing 0, not adjacent to anything via alpha_2 — fixed singleton, no contribution).

So in C_3 at alpha_2-action:
  - 1 length-3 chain: {2 E_3, E_2 + E_3, 2 E_2}, with m=2 (DOUBLY-LACED chain).
  - 2 length-2 chains: {E_1-E_2, E_1-E_3} and {E_1+E_3, E_1+E_2}, m=1 (simply-laced chains).
  - Singleton alpha_2 (pairing +2): contributes )^c.
  - Fixed roots (pairing 0): 2 E_1 — no contribution.

This is exactly the structure of B_2 chain plus extra simply-laced chains. The chain factor for
the doubly-laced edge has the SAME bracket structure as B_n's chain factor (m=2):
    )^M (^{2B} )^{2T} (^M

with M = mult of E_2+E_3 (mid), B = mult of 2 E_3 (bot), T = mult of 2 E_2 (top). The roles
of long/short within the chain are E_n <-> F_n swapped (which is the C_n vs B_n distinction)
but the BRACKET STRUCTURE is identical.

CONCLUSION: C_n at the short-long edge (alpha_{n-1} short, alpha_n long, a_{n,n-1} = -2) has a
chain factor at the doubly-laced edge with the SAME bracket structure )^M (^{2B} )^{2T} (^M as B_n.

The number of chain factors and their roots differ from B_n (C_n has roots 2 E_i instead of E_i),
but the CHAIN FACTOR FORMULA IS UNIFORM IN |a| = 2.

For C_n at alpha_{n-1}-action: there is exactly ONE 'doubly-laced chain factor' through the
fixed long root chain, plus several simply-laced chains and singletons. The catalog count
should match the pattern n(2n-1) = sum of class sizes per v2 structure (or differ slightly due
to having more simply-laced chains).
"""
print(__doc__)
