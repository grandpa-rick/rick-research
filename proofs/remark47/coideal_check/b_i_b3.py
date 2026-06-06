"""
Computational verification of on-slice coideal commutativity at B_3.

Ports b_i_b2.py from B_2 to B_3.

B_3 setup (1-indexed simple roots):
  alpha_1 = e_1 - e_2  (long)
  alpha_2 = e_2 - e_3  (long)
  alpha_3 = e_3        (short, "long simple at the doubly-laced end")

Positive roots (9 total):
  Long minus: e_1 - e_2 (= alpha_1), e_1 - e_3, e_2 - e_3 (= alpha_2)
  Long plus:  e_1 + e_2, e_1 + e_3, e_2 + e_3
  Short:      e_1, e_2, e_3 (= alpha_3)

Unit factors:
  k(1) = 1   (long simple, length-2 chains)
  k(2) = 1   (long simple, length-2 chains)
  k(3) = 2   (short simple at B_n end, length-3 chains)

THEOREM (on-slice commutativity, ported).
For each simple i of B_3, on the depth-k slice
    S_i := { pi in Kp(infty) : eps_i(pi) >= k(i) },
the commutator
    [e_i^{k(i)}, B_i] = 0,  where B_i = e_i + f_i.

OFF-SLICE OBSTRUCTION (ported).
At eps_i(pi) = k(i) - 1:
    [e_i^{k(i)}, B_i] pi = e_i^{k(i)-1} pi.

MULTI-ORBIT REFINEMENT (substantive new content at B_3):
For i = 3, the short simple, s_3 has TWO non-trivial swap-orbits on positive roots:
    O_3^{(1)} = {e_1 + e_3, e_1 - e_3}   (partner p=1)
    O_3^{(2)} = {e_2 + e_3, e_2 - e_3}   (partner p=2)
Each partner gives a different candidate Aug~_{3,p}.  We test on the slice S_3
whether Aug~_{3,p} agrees with e_3^2.
"""

from collections import defaultdict
from typing import Dict, Tuple, Optional, List

# B_3 positive roots (named symbolically)
# Long minus:
EM12 = 'e1-e2'   # alpha_1
EM13 = 'e1-e3'   # alpha_1 + alpha_2
EM23 = 'e2-e3'   # alpha_2
# Long plus:
EP12 = 'e1+e2'   # alpha_1 + 2 alpha_2 + 2 alpha_3
EP13 = 'e1+e3'   # alpha_1 + alpha_2 + 2 alpha_3
EP23 = 'e2+e3'   # alpha_2 + 2 alpha_3
# Short:
E1   = 'e1'      # alpha_1 + alpha_2 + alpha_3
E2   = 'e2'      # alpha_2 + alpha_3
E3   = 'e3'      # alpha_3

ROOTS = [EM12, EM13, EM23, EP12, EP13, EP23, E1, E2, E3]

# Coefficients in standard basis (e_1, e_2, e_3)
ROOT_VEC = {
    EM12: (1, -1, 0), EM13: (1, 0, -1), EM23: (0, 1, -1),
    EP12: (1, 1, 0),  EP13: (1, 0, 1),  EP23: (0, 1, 1),
    E1:   (1, 0, 0),  E2:   (0, 1, 0),  E3:   (0, 0, 1),
}

# Total content (sum of |coords|, weights heights uniformly).
ROOT_HEIGHT = {r: sum(abs(x) for x in v) for r, v in ROOT_VEC.items()}

KP = Dict[str, int]


# ====================================================================
# Kostant-partition helpers
# ====================================================================

def kp_clean(pi: KP) -> KP:
    return {r: c for r, c in pi.items() if c}


def kp_add(pi: KP, root: str, delta: int) -> KP:
    out = dict(pi)
    out[root] = out.get(root, 0) + delta
    if out[root] == 0:
        del out[root]
    return out


def kp_repr(pi: KP) -> str:
    pi = kp_clean(pi)
    if not pi:
        return '<vacuum>'
    return ' + '.join(f'{c}*{r}' for r, c in sorted(pi.items()))


def kp_key(pi: KP) -> Tuple:
    return tuple(sorted(kp_clean(pi).items()))


def kp_total(pi: KP) -> int:
    """Total 'content' = sum of multiplicities times height-1 in the natural basis."""
    return sum(c for c in pi.values())


# ====================================================================
# Bracketing sequences S_i(pi) for B_3, per CST Def 2.14.
#
# For simple alpha_i, alpha_i-strings partition the positive roots.
# Each string {beta, beta+alpha_i, ...} contributes brackets:
#   * If string has length 2 (long-simple case, k=1):
#       chain-top beta+alpha_i -> ')'^c
#       chain-bottom beta      -> '('^c
#   * If string has length 3 (short-simple case in B_n, k=2):
#       chain-middle beta_0 -> ')'^c and '('^c (one of each)
#       chain-bottom beta_- -> '('^{2c}  (doubled)
#       chain-top beta_+    -> ')'^{2c}  (doubled)
#   * If string is the simple alpha_i singleton:  ')'^c
#   * Non-touching singletons: NO contribution.
#
# Order within S_i: convex order following Bourbaki (matches B_2 pattern):
#   - "closes" come BEFORE "opens" within a chain, so e_i drops chain top to chain bottom.
# ====================================================================

def S_1(pi: KP) -> List[Tuple[str, str]]:
    """Bracketing sequence for alpha_1 = e_1-e_2 in B_3.

    alpha_1-strings on Phi^+:
      Chain {EM23, EM13}: e_2-e_3 -> e_1-e_3.   (long-minus)
      Chain {E2, E1}: e_2 -> e_1.               (short-short)
      Chain {EP23, EP13}: e_2+e_3 -> e_1+e_3.   (long-plus)
      Singleton EM12 = alpha_1 (simple itself).
      Singletons EP12, E3 (alpha_1 doesn't touch).

    CST convention (extrapolated from B_2):
      - Chain-tops contribute ')' in convex order of the tops.
      - Chain-bottoms contribute '(' in convex order of the bottoms.
      - Singleton-simple ')' at end.
      - Non-touching singletons: no contribution.

    Convex order (CST w_0 reduced word): EM12 < EM13 < E1 < EP13 < EP12 < EM23 < E2 < EP23 < E3.
      Tops in convex order: EM13, E1, EP13.
      Bottoms in convex order: EM23, E2, EP23.
    """
    s = []
    # Per-chain blocks in convex order of chain-top:
    #   Chain {EM23 (bot), EM13 (top)}: block ')[EM13] ([EM23]
    for _ in range(pi.get(EM13, 0)):
        s.append((')', EM13))
    for _ in range(pi.get(EM23, 0)):
        s.append(('(', EM23))
    #   Chain {E2 (bot), E1 (top)}: block ')[E1] ([E2]
    for _ in range(pi.get(E1, 0)):
        s.append((')', E1))
    for _ in range(pi.get(E2, 0)):
        s.append(('(', E2))
    #   Chain {EP23 (bot), EP13 (top)}: block ')[EP13] ([EP23]
    for _ in range(pi.get(EP13, 0)):
        s.append((')', EP13))
    for _ in range(pi.get(EP23, 0)):
        s.append(('(', EP23))
    # Singleton simple alpha_1 = EM12 ')' at end:
    for _ in range(pi.get(EM12, 0)):
        s.append((')', EM12))
    return s


def S_2(pi: KP) -> List[Tuple[str, str]]:
    """Bracketing sequence for alpha_2 = e_2 - e_3 in B_3.

    alpha_2-strings on Phi^+:
      Chain {EM12, EM13}: e_1-e_2 -> e_1-e_3.   (long-minus)
      Chain {EP13, EP12}: e_1+e_3 -> e_1+e_2.   (long-plus)
      Chain {E3, E2}: e_3 -> e_2.               (short-short)
      Singleton simple EM23 = alpha_2.
      Singletons E1, EP23 (not touched by alpha_2).

    Convex order: EM12(1) < EM13(2) < E1(3) < EP13(4) < EP12(5) < EM23(6) < E2(7) < EP23(8) < E3(9).
      Tops in convex order: EM13(2), EP12(5), E2(7).
      Bottoms in convex order: EM12(1), EP13(4), E3(9).
    """
    s = []
    # Per-chain blocks in convex order of chain-top:
    #   Chain {EM12 (bot), EM13 (top)}: top EM13 at pos 2.
    for _ in range(pi.get(EM13, 0)):
        s.append((')', EM13))
    for _ in range(pi.get(EM12, 0)):
        s.append(('(', EM12))
    #   Chain {EP13 (bot), EP12 (top)}: top EP12 at pos 5.
    for _ in range(pi.get(EP12, 0)):
        s.append((')', EP12))
    for _ in range(pi.get(EP13, 0)):
        s.append(('(', EP13))
    #   Chain {E3 (bot), E2 (top)}: top E2 at pos 7.
    for _ in range(pi.get(E2, 0)):
        s.append((')', E2))
    for _ in range(pi.get(E3, 0)):
        s.append(('(', E3))
    # Singleton simple alpha_2 = EM23 ')' at end:
    for _ in range(pi.get(EM23, 0)):
        s.append((')', EM23))
    return s


def S_3(pi: KP) -> List[Tuple[str, str]]:
    """Bracketing sequence for alpha_3 = e_3 (short simple, k = 2) in B_3.

    alpha_3-strings on Phi^+:
      Chain A {EM13, E1, EP13}: e_1-e_3 -> e_1 -> e_1+e_3 (length 3).
      Chain B {EM23, E2, EP23}: e_2-e_3 -> e_2 -> e_2+e_3 (length 3).
      Singleton E3 = alpha_3 (simple itself).
      Singletons EM12, EP12 (not touched by alpha_3).

    Per-chain block (matches B_2 S_2 pattern):
        ')'^c_middle  '('^{2 c_bottom}  ')'^{2 c_top}  '('^c_middle

    Chain order = convex order: Chain A spans convex positions 2,3,4; Chain B spans 6,7,8.
    Then singleton simple ')'^c_E3.
    """
    s = []
    # ---- Chain A (positions 2,3,4 in convex order) ----
    # middle E1 ')'
    for _ in range(pi.get(E1, 0)):
        s.append((')', E1))
    # bottom EM13 '(' doubled
    for _ in range(2 * pi.get(EM13, 0)):
        s.append(('(', EM13))
    # top EP13 ')' doubled
    for _ in range(2 * pi.get(EP13, 0)):
        s.append((')', EP13))
    # middle E1 '('
    for _ in range(pi.get(E1, 0)):
        s.append(('(', E1))
    # ---- Chain B (positions 6,7,8 in convex order) ----
    for _ in range(pi.get(E2, 0)):
        s.append((')', E2))
    for _ in range(2 * pi.get(EM23, 0)):
        s.append(('(', EM23))
    for _ in range(2 * pi.get(EP23, 0)):
        s.append((')', EP23))
    for _ in range(pi.get(E2, 0)):
        s.append(('(', E2))
    # ---- Singleton simple alpha_3 = E3 (position 9) ----
    for _ in range(pi.get(E3, 0)):
        s.append((')', E3))
    return s


def S_i(pi: KP, i: int) -> List[Tuple[str, str]]:
    if i == 1: return S_1(pi)
    if i == 2: return S_2(pi)
    if i == 3: return S_3(pi)
    raise ValueError(f"i must be 1, 2, or 3, got {i}")


def cancel(s: list) -> list:
    """Repeatedly cancel adjacent '(', ')' pairs."""
    s = list(s)
    while True:
        for k in range(len(s) - 1):
            if s[k][0] == '(' and s[k + 1][0] == ')':
                del s[k:k + 2]
                break
        else:
            return s


# ====================================================================
# Root arithmetic: beta +/- alpha_i in B_3
# ====================================================================

def simple_root(i: int) -> str:
    return {1: EM12, 2: EM23, 3: E3}[i]


def root_minus_alpha(beta: str, i: int) -> Optional[str]:
    """beta - alpha_i. Returns root name, or None if not in Phi^+ (incl. 0)."""
    if i == 1:
        return {EM12: None, EM13: EM23, EM23: None,
                EP12: None, EP13: EP23, EP23: None,
                E1: E2, E2: None, E3: None}[beta]
    if i == 2:
        return {EM12: None, EM13: EM12, EM23: None,
                EP12: EP13, EP13: None, EP23: None,
                E1: None, E2: E3, E3: None}[beta]
    if i == 3:
        return {EM12: None, EM13: None, EM23: None,
                EP12: None, EP13: E1, EP23: E2,
                E1: EM13, E2: EM23, E3: None}[beta]
    raise ValueError(i)


def root_plus_alpha(beta: str, i: int) -> Optional[str]:
    """beta + alpha_i. Returns root name, or None if not in Phi^+."""
    if i == 1:
        return {EM12: None, EM13: None, EM23: EM13,
                EP12: None, EP13: None, EP23: EP13,
                E1: None, E2: E1, E3: None}[beta]
    if i == 2:
        return {EM12: EM13, EM13: None, EM23: None,
                EP12: None, EP13: EP12, EP23: None,
                E1: None, E2: None, E3: E2}[beta]
    if i == 3:
        return {EM12: None, EM13: E1, EM23: E2,
                EP12: None, EP13: None, EP23: None,
                E1: EP13, E2: EP23, E3: None}[beta]
    raise ValueError(i)


# ====================================================================
# Crystal operators e_i, f_i (CST Def 2.14)
# ====================================================================

def e_i(pi: KP, i: int) -> Optional[KP]:
    """e_i pi: rightmost ')' in S_i^c, beta -> beta - alpha_i."""
    pi = kp_clean(pi)
    sc = cancel(S_i(pi, i))
    rightmost_close = None
    for k in range(len(sc) - 1, -1, -1):
        if sc[k][0] == ')':
            rightmost_close = sc[k]
            break
    if rightmost_close is None:
        return None
    beta = rightmost_close[1]
    new_root = root_minus_alpha(beta, i)
    out = kp_add(pi, beta, -1)
    if new_root is not None:
        out = kp_add(out, new_root, +1)
    return kp_clean(out)


def f_i(pi: KP, i: int) -> KP:
    """f_i pi: leftmost '(' in S_i^c, gamma -> gamma + alpha_i.
    If no '(' in S_i^c, f_i pi = pi + alpha_i (simple root added)."""
    pi = kp_clean(pi)
    sc = cancel(S_i(pi, i))
    leftmost_open = None
    for tok in sc:
        if tok[0] == '(':
            leftmost_open = tok
            break
    if leftmost_open is None:
        return kp_clean(kp_add(pi, simple_root(i), +1))
    gamma = leftmost_open[1]
    new_root = root_plus_alpha(gamma, i)
    out = kp_add(pi, gamma, -1)
    if new_root is not None:
        out = kp_add(out, new_root, +1)
    return kp_clean(out)


def e_i_k(pi: KP, i: int, k: int) -> Optional[KP]:
    cur = pi
    for _ in range(k):
        cur = e_i(cur, i)
        if cur is None:
            return None
    return cur


def f_i_k(pi: KP, i: int, k: int) -> KP:
    cur = pi
    for _ in range(k):
        cur = f_i(cur, i)
    return cur


def eps_i(pi: KP, i: int) -> int:
    sc = cancel(S_i(pi, i))
    return sum(1 for c, _ in sc if c == ')')


def phi_i(pi: KP, i: int) -> int:
    sc = cancel(S_i(pi, i))
    return sum(1 for c, _ in sc if c == '(')


# ====================================================================
# Linear combinations of Kostant partitions
# ====================================================================

class LinComb:
    __slots__ = ('terms',)

    def __init__(self, terms=None):
        self.terms = dict(terms) if terms else {}

    @classmethod
    def zero(cls):
        return cls({})

    @classmethod
    def from_kp(cls, pi, coeff=1):
        if pi is None or coeff == 0:
            return cls.zero()
        p = kp_clean(pi)
        return cls({kp_key(p): (p, coeff)})

    def __add__(self, other):
        out = dict(self.terms)
        for k, (pi, c) in other.terms.items():
            if k in out:
                old_pi, old_c = out[k]
                new_c = old_c + c
                if new_c == 0:
                    del out[k]
                else:
                    out[k] = (old_pi, new_c)
            else:
                out[k] = (pi, c)
        return LinComb(out)

    def __sub__(self, other):
        return self + (-1) * other

    def __rmul__(self, scalar):
        if scalar == 0:
            return LinComb.zero()
        return LinComb({k: (pi, scalar * c) for k, (pi, c) in self.terms.items()})

    def __eq__(self, other):
        return dict(self.terms) == dict(other.terms)

    def is_zero(self):
        return not self.terms

    def num_terms(self):
        return len(self.terms)

    def __repr__(self):
        if not self.terms:
            return '0'
        parts = []
        for k in sorted(self.terms.keys()):
            pi, c = self.terms[k]
            if c == 1:
                parts.append(f'({kp_repr(pi)})')
            elif c == -1:
                parts.append(f'-({kp_repr(pi)})')
            else:
                parts.append(f'{c}*({kp_repr(pi)})')
        return ' + '.join(parts).replace('+ -', '- ')


def apply_e(lc, i):
    out = LinComb.zero()
    for k, (pi, coeff) in lc.terms.items():
        out = out + LinComb.from_kp(e_i(pi, i), coeff)
    return out


def apply_f(lc, i):
    out = LinComb.zero()
    for k, (pi, coeff) in lc.terms.items():
        out = out + LinComb.from_kp(f_i(pi, i), coeff)
    return out


def apply_e_k(lc, i, k):
    cur = lc
    for _ in range(k):
        cur = apply_e(cur, i)
    return cur


def apply_B(lc, i):
    """B_i = e_i + f_i."""
    return apply_e(lc, i) + apply_f(lc, i)


# ====================================================================
# Aug~_i orbit-swap (deterministic forward, e-direction):
# For i = 1, 2 (long simples), each chain {bottom, top} gives a candidate.
#   At B_2, Aug~_1 was the unique short-short swap, but at B_3 we have
#   THREE candidate orbits:
#       short-short:    E2 -> E1   (partner = pure short)
#       long-long (+):  EP23 -> EP13   (partner = +e_3)
#       long-long (-):  EM23 -> EM13   (partner = -e_3)
#   These are different sub-types (the (a, b+, c+, c-) split of aug_tilde_B3_richer).
#   For testing the literal Aug~ = e_i^{k(i)} identification, we test each.
#
# For i = 3 (short simple), the two non-trivial s_3 orbits are:
#       (S, p=1): EP13 <-> EM13   (partner p=1)
#       (S, p=2): EP23 <-> EM23   (partner p=2)
#   Each is a k=2 swap (donor -= 2, receiver += 2? NO — at B_2 it was -=1 +=1
#   because the swap is just a single root replacement; the "k=2" refers to
#   the number of Kashiwara steps it takes via e_i^k, not the orbit-swap multiplicity).
#
# Convention: Aug~_i^{e}: donor -= 1, receiver += 1 (forward direction).
# ====================================================================

def k_i(i):
    return 1 if i in (1, 2) else 2


def aug_e_long(pi, i, subtype):
    """Forward Aug~ for long simple i (long-long or short-short swap).

    subtype = 'a': short-short swap.
        i=1: E2 -> E1 (donor E2, receiver E1).
        i=2: E3 -> E2 (donor E3, receiver E2).
    subtype = 'b+': only meaningful for i where p < i is available; for i=1 no p, for i=2 p=0
        At B_3 we use 1-indexed p ∈ {1, ..., i-1}.
        i=2, p=1: long-long (+) with low partner p=1.
            r = e_1 + e_2 (EP12)? -- we need r' - r = -alpha_2 = -e_2 + e_3.
            Hmm. For long simple alpha_2 = e_2 - e_3, c_i > 0 case:
            (b+, p=1): remove (e_1 + e_2) = EP12, add (e_1 + e_3) = EP13. r'-r = -alpha_2. ✓
            But this REMOVES from the top of an alpha_2-chain.
            Wait — we want forward = "decrease weight by alpha_i" = "raise" in Aug~ sense.
            The B_2 convention: aug_e at i=2 (k=2): donor=G12 (long top), receiver=B11 (long bottom).
                Diff: c_G12 -= 1, c_B11 += 1.  Weight change: B11 - G12 = (e_1-e_2)-(e_1+e_2) = -2 e_2 = -2 alpha_2. ✓
            So aug_e = forward = "weight decreases by k * alpha_i".  Donor = top of chain, receiver = bottom.

            For i=2 at B_3, long simple, chains of length 2:
                Chain A: EM12 -> EM13 (bottom -> top via +alpha_2).
                Chain B: E3 -> E2.
                Chain C: EP13 -> EP12.
            Aug~_2 candidates (each chain gives one): EM13 -> EM12, E2 -> E3, EP12 -> EP13.

    For uniform interface: subtype = 'a' for "short-short" (e_2 -> e_3 for i=2, e_? for i=1),
        subtype = 'L0' for chain "long minus" (EM-chain), 'L+' for EP-chain.
    """
    # We'll keep this generic via explicit (donor, receiver) lookup.
    raise NotImplementedError("Use aug_e_chain instead.")


def aug_e_chain(pi, i, chain_id):
    """Forward Aug~_i swap using a specific chain.

    For i = 1 (alpha_1, k=1), 3 chains in alpha_1-string structure:
        'M' (long-minus): EM23 -> EM13 swap.  donor = EM13, receiver = EM23.
            Wait — forward = weight decreases by alpha_1.  EM23 - EM13 = -alpha_1.
            So donor -> receiver where new_wt - old_wt = -alpha_1:
            donor = EM13, receiver = EM23. ✓
        'P' (long-plus): donor = EP13, receiver = EP23.
        'S' (short-short): donor = E1, receiver = E2.

    For i = 2 (alpha_2, k=1), 3 chains:
        'M' (long-minus): donor = EM13, receiver = EM12.
        'P' (long-plus):  donor = EP12, receiver = EP13.
        'S' (short-short): donor = E2, receiver = E3.

    For i = 3 (alpha_3, k=2), 2 non-trivial chains:
        '1' (partner p=1): donor = EP13, receiver = EM13. (top->bottom of chain A)
            Diff: c_EP13 -=1, c_EM13 +=1. wt diff: EM13 - EP13 = -2 e_3 = -2 alpha_3. ✓
        '2' (partner p=2): donor = EP23, receiver = EM23.
    """
    swaps = {
        (1, 'M'): (EM13, EM23),
        (1, 'P'): (EP13, EP23),
        (1, 'S'): (E1,   E2),
        (2, 'M'): (EM13, EM12),
        (2, 'P'): (EP12, EP13),
        (2, 'S'): (E2,   E3),
        (3, '1'): (EP13, EM13),
        (3, '2'): (EP23, EM23),
    }
    if (i, chain_id) not in swaps:
        raise ValueError(f"No Aug~_chain for i={i}, chain_id={chain_id}")
    donor, receiver = swaps[(i, chain_id)]
    if pi.get(donor, 0) < 1:
        return None
    out = kp_add(pi, donor, -1)
    out = kp_add(out, receiver, +1)
    return kp_clean(out)


def chain_ids_for(i):
    if i in (1, 2):
        return ['M', 'P', 'S']
    if i == 3:
        return ['1', '2']
    raise ValueError(i)


# ====================================================================
# Enumeration
# ====================================================================

def enumerate_partitions(max_total):
    """Enumerate Kostant partitions pi with sum c <= max_total."""
    out = []
    # Iterate over all 9 roots' multiplicities, bounded by max_total.
    n = len(ROOTS)
    # Use a recursive approach for cleanliness.
    def recurse(idx, remaining, partial):
        if idx == n:
            out.append(dict(partial))
            return
        for c in range(remaining + 1):
            partial2 = dict(partial)
            if c > 0:
                partial2[ROOTS[idx]] = c
            recurse(idx + 1, remaining - c, partial2)
    recurse(0, max_total, {})
    return out


# ====================================================================
# TEST 0: Crystal axiom verification (FIRST: don't test downstream if axioms fail)
# ====================================================================

def test_crystal_axioms(max_total=4):
    print("\n=== TEST 0: Crystal axiom sanity check ===")
    print("  Required: e_i f_i = id always; f_i e_i = id when eps_i >= 1.\n")
    all_pass = True
    for i in [1, 2, 3]:
        n_total = 0
        n_ef = 0
        n_fe_slice = 0
        n_fe_slice_ok = 0
        bad_ef = []
        bad_fe = []
        for pi in enumerate_partitions(max_total):
            n_total += 1
            f_pi = f_i(pi, i)
            e_f_pi = e_i(f_pi, i)
            if e_f_pi == kp_clean(pi):
                n_ef += 1
            else:
                bad_ef.append((pi, f_pi, e_f_pi))
            e_pi = e_i(pi, i)
            if e_pi is not None:
                n_fe_slice += 1
                f_e_pi = f_i(e_pi, i)
                if f_e_pi == kp_clean(pi):
                    n_fe_slice_ok += 1
                else:
                    bad_fe.append((pi, e_pi, f_e_pi))
        print(f"  i = {i}:")
        print(f"    e_i f_i = id:           {n_ef}/{n_total}")
        print(f"    f_i e_i = id on slice:  {n_fe_slice_ok}/{n_fe_slice}")
        if bad_ef:
            all_pass = False
            print(f"    *** e_i f_i FAILURES (showing first 5):")
            for pi, f_pi, e_f_pi in bad_ef[:5]:
                print(f"      pi = {kp_repr(pi)} -> f_i pi = {kp_repr(f_pi)} -> e_i f_i pi = {kp_repr(e_f_pi)}")
        if bad_fe:
            all_pass = False
            print(f"    *** f_i e_i FAILURES on slice (showing first 5):")
            for pi, e_pi, f_e_pi in bad_fe[:5]:
                print(f"      pi = {kp_repr(pi)} -> e_i pi = {kp_repr(e_pi)} -> f_i e_i pi = {kp_repr(f_e_pi)}")
    return all_pass


# ====================================================================
# TEST A: On-slice commutativity  [e_i^{k(i)}, B_i] = 0 on S_i = {eps_i >= k}.
# ====================================================================

def test_commutativity_e_k_onslice(max_total=4):
    print("\n=== TEST A: [e_i^{k(i)}, B_i] on the depth-k slice S_i ===\n")
    summary = {}
    for i in [1, 2, 3]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        total = 0
        good = 0
        bad = 0
        bad_examples = []
        for pi in enumerate_partitions(max_total):
            if eps_i(pi, i) < k:
                continue
            total += 1
            pi_lc = LinComb.from_kp(pi)
            ek = apply_e_k(pi_lc, i, k)
            B_ek = apply_B(ek, i)
            B = apply_B(pi_lc, i)
            ek_B = apply_e_k(B, i, k)
            comm = ek_B - B_ek
            if comm.is_zero():
                good += 1
            else:
                bad += 1
                if len(bad_examples) < 5:
                    bad_examples.append((pi, comm))
        print(f"    on-slice partitions tested: {total}")
        print(f"    commutator zero:           {good}")
        print(f"    commutator nonzero:        {bad}")
        if bad_examples:
            print(f"    Sample falsifiers:")
            for pi, comm in bad_examples:
                print(f"      pi = {kp_repr(pi)}: [e^k, B] = {comm}")
        summary[i] = (total, good, bad)
        print()
    return summary


# ====================================================================
# TEST B: Off-slice obstruction.
#   At eps_i = k - 1: [e_i^k, B_i] pi = e_i^{k-1} pi.
#   For i = 1, 2 (k=1): at eps_i = 0: [e_i, B_i] pi = pi.
#   For i = 3 (k=2): at eps_3 = 1: [e_3^2, B_3] pi = e_3 pi.
#   Below eps_i < k - 1: commutator should vanish (since e_i^k pi = e_i^{k-1} pi = 0).
# ====================================================================

def test_offslice(max_total=4):
    print("\n=== TEST B: Off-slice obstruction ===\n")
    summary = {}
    for i in [1, 2, 3]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        for target_eps in range(k):
            print(f"\n    Off-slice locus: eps_{i} = {target_eps}")
            total = 0
            match = 0
            mismatch = 0
            mismatch_examples = []
            for pi in enumerate_partitions(max_total):
                if eps_i(pi, i) != target_eps:
                    continue
                total += 1
                pi_lc = LinComb.from_kp(pi)
                ek = apply_e_k(pi_lc, i, k)
                B_ek = apply_B(ek, i)
                B = apply_B(pi_lc, i)
                ek_B = apply_e_k(B, i, k)
                comm = ek_B - B_ek

                # Predicted obstruction: e_i^{k-1} pi (an actual partition or 0).
                # At eps_i = target_eps: if target_eps == k - 1, e_i^{k-1} pi is well-defined.
                # If target_eps < k - 1, e_i^{k-1} pi = 0.
                if target_eps == k - 1:
                    # Predicted: comm = e_i^{k-1} pi (as a single-term LinComb).
                    expected_pi = e_i_k(pi, i, k - 1) if k - 1 > 0 else kp_clean(pi)
                    expected_lc = LinComb.from_kp(expected_pi) if expected_pi is not None else LinComb.zero()
                else:
                    expected_lc = LinComb.zero()
                if comm == expected_lc:
                    match += 1
                else:
                    mismatch += 1
                    if len(mismatch_examples) < 3:
                        mismatch_examples.append((pi, comm, expected_lc))
            print(f"      tested {total}: match {match}, mismatch {mismatch}")
            if mismatch_examples:
                print(f"      Sample mismatches:")
                for pi, comm, exp in mismatch_examples:
                    print(f"        pi = {kp_repr(pi)}: comm = {comm}, expected = {exp}")
            summary[(i, target_eps)] = (total, match, mismatch)
        print()
    return summary


# ====================================================================
# TEST C: Multi-orbit Aug~ identification on the slice S_i.
# For each chain_id (orbit), check Aug~ = e_i^{k(i)} literally.
# Report match counts per orbit, and define S_i' as the literal-match subset.
# ====================================================================

def test_aug_orbit_identification(max_total=4):
    print("\n=== TEST C: Multi-orbit Aug~ = e_i^{k(i)} identification on Kp(infty) ===\n")
    summary = {}
    for i in [1, 2, 3]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        for chain_id in chain_ids_for(i):
            n_aug_def = 0      # |{pi : aug_e_chain(pi, i, chain_id) != None}|
            n_ek_def  = 0      # |{pi : e_i^k pi != None}|
            n_both    = 0
            n_match   = 0
            mismatches = []
            for pi in enumerate_partitions(max_total):
                aug = aug_e_chain(pi, i, chain_id)
                ek  = e_i_k(pi, i, k)
                if aug is not None: n_aug_def += 1
                if ek  is not None: n_ek_def  += 1
                if aug is not None and ek is not None:
                    n_both += 1
                if aug == ek:
                    n_match += 1
                else:
                    if len(mismatches) < 5:
                        mismatches.append((pi, aug, ek))
            print(f"    chain '{chain_id}': aug_def = {n_aug_def}, ek_def = {n_ek_def}, both_def = {n_both}, full_match = {n_match}/{len(enumerate_partitions(max_total))}")
            if mismatches:
                print(f"      sample disagreements:")
                for pi, aug, ek in mismatches[:3]:
                    a = kp_repr(aug) if aug else '0'
                    e = kp_repr(ek) if ek else '0'
                    print(f"        pi = {kp_repr(pi)}: aug = {a}, e^k = {e}")
            summary[(i, chain_id)] = (n_aug_def, n_ek_def, n_match)
        print()
    return summary


# ====================================================================
# TEST D: Multi-orbit Aug~ on the slice S_i (eps_i >= k), AND restricted
# to "tight sub-slice S_i'" where Aug~_chain = e_i^k literally.
# Report for each orbit how many sub-slice partitions exist.
# ====================================================================

def test_aug_on_slice(max_total=4):
    print("\n=== TEST D: Aug~_{i, chain} vs. e_i^{k(i)} on the slice S_i ===\n")
    summary = {}
    for i in [1, 2, 3]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        n_slice = sum(1 for pi in enumerate_partitions(max_total) if eps_i(pi, i) >= k)
        print(f"    |S_i (max_total={max_total})| = {n_slice}")
        for chain_id in chain_ids_for(i):
            n_aug_def_onslice = 0
            n_ek_match_onslice = 0
            n_subslice = 0  # aug_def AND aug == ek (both nonzero)
            for pi in enumerate_partitions(max_total):
                if eps_i(pi, i) < k:
                    continue
                aug = aug_e_chain(pi, i, chain_id)
                ek = e_i_k(pi, i, k)
                if aug is not None:
                    n_aug_def_onslice += 1
                if aug is not None and ek is not None and aug == ek:
                    n_subslice += 1
                if aug == ek:
                    n_ek_match_onslice += 1
            print(f"    chain '{chain_id}': aug-defined on-slice = {n_aug_def_onslice}, "
                  f"S_i'-tight (aug == ek != 0) = {n_subslice}, "
                  f"full equality (including 0=0) = {n_ek_match_onslice}")
            summary[(i, chain_id)] = (n_aug_def_onslice, n_subslice, n_ek_match_onslice)
        print()
    return summary


# ====================================================================
# TEST E: [Aug~_{i,chain}, B_i] = 0 on the sub-slice S_{i,chain}'.
# This is the orbit-by-orbit version of the coideal commutativity check.
# ====================================================================

def test_aug_commutativity_per_orbit(max_total=4):
    print("\n=== TEST E: [Aug~_{i,chain}, B_i] on sub-slice (Aug~_chain = e_i^k) ===\n")
    summary = {}
    for i in [1, 2, 3]:
        k = k_i(i)
        print(f"  i = {i}, k = {k}")
        for chain_id in chain_ids_for(i):
            n_subslice = 0
            good = 0
            bad = 0
            examples = []
            for pi in enumerate_partitions(max_total):
                aug = aug_e_chain(pi, i, chain_id)
                ek = e_i_k(pi, i, k)
                if aug is None or ek is None:
                    continue
                if aug != ek:
                    continue
                n_subslice += 1
                # Compute [Aug~_{i,chain}, B_i] pi term-by-term.
                pi_lc = LinComb.from_kp(pi)
                aug_pi_lc = LinComb.from_kp(aug)
                B_aug = apply_B(aug_pi_lc, i)
                B = apply_B(pi_lc, i)
                aug_B = LinComb.zero()
                for kk, (term_pi, coeff) in B.terms.items():
                    aug_term = aug_e_chain(term_pi, i, chain_id)
                    aug_B = aug_B + LinComb.from_kp(aug_term, coeff)
                comm = aug_B - B_aug
                if comm.is_zero():
                    good += 1
                else:
                    bad += 1
                    if len(examples) < 3:
                        examples.append((pi, comm))
            print(f"    chain '{chain_id}': sub-slice size = {n_subslice}, [Aug,B] = 0: {good}, != 0: {bad}")
            if examples:
                for pi, comm in examples:
                    print(f"      example: pi = {kp_repr(pi)}, [Aug,B] = {comm}")
            summary[(i, chain_id)] = (n_subslice, good, bad)
        print()
    return summary


# ====================================================================
# TEST F: Multi-orbit classification of S_3 = {eps_3 >= 2} by orbit type.
#
# For i = 3 (short simple, k = 2), the two non-trivial s_3-orbits are
#   O_A = {EP13 <-> EM13}  (partner p=1, "chain A")
#   O_B = {EP23 <-> EM23}  (partner p=2, "chain B")
# Plus singletons E3 (= alpha_3, simple), EM12, EP12, E1, E2.
#
# Classify pi in S_3 by its s_3-orbit support:
#   class "A": pi has chain-A content (EP13 or EM13 > 0) but NO chain-B content.
#   class "B": pi has chain-B content but NO chain-A content.
#   class "AB": pi has both.
#   class "neither": pi has NO chain content (only singletons).
#
# For each class, count: total in slice, how many satisfy Aug~_{3,1} = e_3^2,
# how many satisfy Aug~_{3,2} = e_3^2, how many satisfy AT LEAST one.
# ====================================================================

def orbit_class_for_pi_at_3(pi):
    has_A = pi.get(EP13, 0) > 0 or pi.get(EM13, 0) > 0
    has_B = pi.get(EP23, 0) > 0 or pi.get(EM23, 0) > 0
    if has_A and has_B: return 'AB'
    if has_A: return 'A'
    if has_B: return 'B'
    return 'neither'


def test_aug_multiorbit_classification(max_total=4):
    print("\n=== TEST F: Multi-orbit classification at i=3 (S_3 = {eps_3 >= 2}) ===\n")
    print("  Classes by s_3-orbit support: 'A' = chain-A only, 'B' = chain-B only,")
    print("  'AB' = both, 'neither' = no chain support.\n")
    classes = ['A', 'B', 'AB', 'neither']
    counts = {c: 0 for c in classes}
    match_1 = {c: 0 for c in classes}    # Aug~_{3,1} = e_3^2
    match_2 = {c: 0 for c in classes}    # Aug~_{3,2} = e_3^2
    match_any = {c: 0 for c in classes}
    examples_fail = {c: [] for c in classes}

    for pi in enumerate_partitions(max_total):
        if eps_i(pi, 3) < 2:
            continue
        cls = orbit_class_for_pi_at_3(pi)
        counts[cls] += 1
        aug1 = aug_e_chain(pi, 3, '1')
        aug2 = aug_e_chain(pi, 3, '2')
        ek = e_i_k(pi, 3, 2)
        m1 = (aug1 == ek)
        m2 = (aug2 == ek)
        if m1: match_1[cls] += 1
        if m2: match_2[cls] += 1
        if m1 or m2: match_any[cls] += 1
        if not (m1 or m2) and len(examples_fail[cls]) < 3:
            a1 = kp_repr(aug1) if aug1 else '0'
            a2 = kp_repr(aug2) if aug2 else '0'
            ek_s = kp_repr(ek) if ek else '0'
            examples_fail[cls].append((pi, a1, a2, ek_s))

    for cls in classes:
        n = counts[cls]
        if n == 0:
            print(f"  Class '{cls}': 0 partitions in slice S_3.")
            continue
        print(f"  Class '{cls}': {n} partitions in S_3.")
        print(f"    Aug~_{{3,1}} = e_3^2:  {match_1[cls]}/{n}")
        print(f"    Aug~_{{3,2}} = e_3^2:  {match_2[cls]}/{n}")
        print(f"    Either match:        {match_any[cls]}/{n}")
        if examples_fail[cls]:
            print(f"    Sample partitions where NEITHER orbit identifies (showing first 3):")
            for pi, a1, a2, ek_s in examples_fail[cls]:
                print(f"      pi = {kp_repr(pi)}: aug_1 = {a1}, aug_2 = {a2}, e_3^2 = {ek_s}")
    print()


# ====================================================================
# MAIN
# ====================================================================

if __name__ == '__main__':
    import sys
    print("=" * 75)
    print("B_3 type-AII coideal commutativity verification")
    print("  B_i := e_i + f_i (q=0 image of split type-AII coideal generator)")
    print("  k(1) = k(2) = 1 (long simples); k(3) = 2 (short simple)")
    print("=" * 75)

    MAX = 5

    axioms_ok = test_crystal_axioms(max_total=MAX)
    if not axioms_ok:
        print("\n!!! CRYSTAL AXIOMS FAILED. STOPPING.")
        sys.exit(1)

    test_commutativity_e_k_onslice(max_total=MAX)
    test_offslice(max_total=MAX)
    test_aug_orbit_identification(max_total=MAX - 1)
    test_aug_on_slice(max_total=MAX)
    test_aug_commutativity_per_orbit(max_total=MAX - 1)
    test_aug_multiorbit_classification(max_total=MAX - 1)
