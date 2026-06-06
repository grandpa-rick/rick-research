"""
Check the case pi = 2*b11 + 2*g12 on Rick's side and Kashiwara's side.

Kashiwara: br_2(pi) = '(((())))' cancels fully, so e_2 pi = 0 (no raising step).
Rick's REDUCED orbit-swap: {(LL, +): 1} is valid, takes pi -> 3*b11 + 1*g12.

This shows a STRUCTURAL DIVERGENCE: Rick's orbit-swap is broader than crystal e_2/f_2.

Question: what is the "crystal" of (2*b11 + 2*g12) under e_2/f_2?
  - br_2^c is empty, so neither e_2 nor f_2 can act (well: f_2 has no leftmost
    '(', so f_2 pi = pi + alpha_2 = pi + b22.  But e_2 pi = 0.)
  - This means pi is a highest-weight element with respect to the i=2 direction.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main_check import (build_S_2_B2, cancel_brackets, s_to_str, e_2_action_B2,
                        f_2_action_B2, beta11, gamma12, beta12, beta22, alpha2,
                        ROOT_NAMES, pp)

pi = {beta11: 2, gamma12: 2}

s = build_S_2_B2(pi)
sc = cancel_brackets(s)
print(f"pi = {pp(pi)}")
print(f"S_2(pi)  = {s_to_str(s)}")
print(f"S_2^c(pi) = {s_to_str(sc)}")

e_res = e_2_action_B2(pi)
print(f"e_2 pi = {e_res}")

f_res = f_2_action_B2(pi)
print(f"f_2 pi = {pp(f_res[0]) if f_res[0] else '0'}")

# This shows: e_2 pi = None (= 0 in B(infty)).  Kashiwara declares no raising step.
# But Rick's orbit-swap (LL, +) at c=2 still applies (donor g12 capacity 2 -> we use 1).

# So Rick's REDUCED orbit-swap multiset is BROADER than the crystal raising operator
# e_2: it allows transitions that the crystal does not.

# Hmm. Let me reconsider.
# The CST crystal isomorphism Psi : T(infty) -> Kp(infty) is a crystal iso. So
# for every pi in Kp(infty), e_i pi is well-defined (possibly = 0). When = 0, there is
# NO i-arrow up from pi.
#
# Rick's orbit-swap multiset (LL, +): 1 sends 2*b11 + 2*g12 -> 3*b11 + 1*g12. Both
# of these are valid Kostant partitions. But the crystal i-arrow from 3*b11+1*g12 to
# 2*b11+2*g12 (i.e., f_2 from upper to lower) probably also exists or doesn't.
#
# Actually wait — let me think about direction. Rick's orbit-swap '+' goes
# gamma_{1,2} -> beta_{1,1} via shifting weight by -2*alpha_2.  In terms of weight
# wt(alpha) = -sum c_beta beta:
#   wt(2*b11 + 2*g12) = -(2(1,-1) + 2(1,1)) = -(4, 0) = (-4, 0).
#   wt(3*b11 + 1*g12) = -(3(1,-1) + 1(1,1)) = -(4, -2) = (-4, 2).
#   Weight change: (0, 2) = +2*alpha_2. So this is two RAISING steps in Kashiwara
#   (e_2 e_2).
#
# So orbit-swap (LL,+) is the RAISING direction (e_2 type), but it's REJECTED by the
# crystal (e_2 of pi = 0).

# Let's compute e_2 on pi' = 3*b11 + 1*g12 to see:
pip = {beta11: 3, gamma12: 1}
s2 = build_S_2_B2(pip)
sc2 = cancel_brackets(s2)
print(f"\npi' = {pp(pip)}")
print(f"S_2(pi')  = {s_to_str(s2)}")
print(f"S_2^c(pi') = {s_to_str(sc2)}")
e_res2 = e_2_action_B2(pip)
if e_res2 is None:
    print(f"e_2 pi' = 0")
else:
    print(f"e_2 pi' = {pp(e_res2[0])}, applying via root {ROOT_NAMES[e_res2[1]]}")

# Also f_2 of pi':
f_res2 = f_2_action_B2(pip)
print(f"f_2 pi' = {pp(f_res2[0]) if f_res2[0] else '0'}")

# Conclusion: if e_2 acts via the crystal, we trace what happens.
# The question is: does crystal e_2 (or two of them) bring pi back from pi' to pi?
