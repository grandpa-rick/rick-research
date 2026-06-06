"""
Computational verification of on-slice coideal commutativity at B_5.

Ports b_i_b4.py from B_4 to B_5.

B_5 setup (1-indexed simple roots):
  alpha_1 = e_1 - e_2  (long)
  alpha_2 = e_2 - e_3  (long)
  alpha_3 = e_3 - e_4  (long)
  alpha_4 = e_4 - e_5  (long)
  alpha_5 = e_5        (short)

Positive roots (25 total):
  Long minus: e_a - e_b for 1 <= a < b <= 5 (10 of them)
  Long plus:  e_a + e_b for 1 <= a < b <= 5 (10 of them)
  Short:      e_a for a=1..5 (5 of them)

Unit factors:
  k(1) = k(2) = k(3) = k(4) = 1   (long simples)
  k(5) = 2                         (short simple at the B_n end)

THEOREM (on-slice commutativity, ported).
For each simple i of B_5, on the depth-k slice
    S_i := { pi in Kp(infty) : eps_i(pi) >= k(i) },
the commutator [e_i^{k(i)}, B_i] = 0,  where B_i = e_i + f_i.

Convex order (Bourbaki, B_5):
  block 1 (e_1 involved): EM12, EM13, EM14, EM15, E1, EP15, EP14, EP13, EP12
  block 2 (e_2 involved): EM23, EM24, EM25, E2, EP25, EP24, EP23
  block 3 (e_3 involved): EM34, EM35, E3, EP35, EP34
  block 4 (e_4 involved): EM45, E4, EP45
  block 5: E5
"""

from collections import defaultdict
from typing import Dict, Tuple, Optional, List

# B_5 positive roots
# Long minus
EM12 = 'e1-e2'
EM13 = 'e1-e3'
EM14 = 'e1-e4'
EM15 = 'e1-e5'
EM23 = 'e2-e3'
EM24 = 'e2-e4'
EM25 = 'e2-e5'
EM34 = 'e3-e4'
EM35 = 'e3-e5'
EM45 = 'e4-e5'
# Long plus
EP12 = 'e1+e2'
EP13 = 'e1+e3'
EP14 = 'e1+e4'
EP15 = 'e1+e5'
EP23 = 'e2+e3'
EP24 = 'e2+e4'
EP25 = 'e2+e5'
EP34 = 'e3+e4'
EP35 = 'e3+e5'
EP45 = 'e4+e5'
# Short
E1 = 'e1'
E2 = 'e2'
E3 = 'e3'
E4 = 'e4'
E5 = 'e5'

# Convex order (Bourbaki w_0 reduced word).
ROOTS_CONVEX = [
    EM12, EM13, EM14, EM15, E1, EP15, EP14, EP13, EP12,   # block 1
    EM23, EM24, EM25, E2, EP25, EP24, EP23,               # block 2
    EM34, EM35, E3, EP35, EP34,                            # block 3
    EM45, E4, EP45,                                         # block 4
    E5,                                                     # block 5
]
ROOTS = ROOTS_CONVEX  # alias for enumeration

# Coefficients in standard basis (e_1, e_2, e_3, e_4, e_5)
ROOT_VEC = {
    EM12: (1,-1, 0, 0, 0), EM13: (1, 0,-1, 0, 0), EM14: (1, 0, 0,-1, 0), EM15: (1, 0, 0, 0,-1),
    EM23: (0, 1,-1, 0, 0), EM24: (0, 1, 0,-1, 0), EM25: (0, 1, 0, 0,-1),
    EM34: (0, 0, 1,-1, 0), EM35: (0, 0, 1, 0,-1),
    EM45: (0, 0, 0, 1,-1),
    EP12: (1, 1, 0, 0, 0), EP13: (1, 0, 1, 0, 0), EP14: (1, 0, 0, 1, 0), EP15: (1, 0, 0, 0, 1),
    EP23: (0, 1, 1, 0, 0), EP24: (0, 1, 0, 1, 0), EP25: (0, 1, 0, 0, 1),
    EP34: (0, 0, 1, 1, 0), EP35: (0, 0, 1, 0, 1),
    EP45: (0, 0, 0, 1, 1),
    E1:   (1, 0, 0, 0, 0), E2:   (0, 1, 0, 0, 0), E3:   (0, 0, 1, 0, 0),
    E4:   (0, 0, 0, 1, 0), E5:   (0, 0, 0, 0, 1),
}

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
    return sum(c for c in pi.values())


# ====================================================================
# Root arithmetic: beta +/- alpha_i in B_5
# Long simples (1, 2, 3, 4): exchange the e_i and e_{i+1} components.
# Short simple (5): e_5 changes sign.
# Result is a positive root or None.
# ====================================================================

SIMPLE_ROOT_NAME = {1: EM12, 2: EM23, 3: EM34, 4: EM45, 5: E5}


def simple_root(i: int) -> str:
    return SIMPLE_ROOT_NAME[i]


_VEC_TO_ROOT = {v: r for r, v in ROOT_VEC.items()}


def _vec_to_root(v: Tuple[int, int, int, int, int]) -> Optional[str]:
    """Look up positive root from coordinate vector, or None if not in Phi^+."""
    return _VEC_TO_ROOT.get(v)


def root_minus_alpha(beta: str, i: int) -> Optional[str]:
    """beta - alpha_i. Returns positive-root name, or None if not in Phi^+ (incl. 0)."""
    v = list(ROOT_VEC[beta])
    if i in (1, 2, 3, 4):
        # alpha_i = e_i - e_{i+1}, so beta - alpha_i: v[i-1] -= 1, v[i] += 1.
        v[i-1] -= 1
        v[i] += 1
    elif i == 5:
        # alpha_5 = e_5
        v[4] -= 1
    else:
        raise ValueError(i)
    return _vec_to_root(tuple(v))


def root_plus_alpha(beta: str, i: int) -> Optional[str]:
    v = list(ROOT_VEC[beta])
    if i in (1, 2, 3, 4):
        v[i-1] += 1
        v[i] -= 1
    elif i == 5:
        v[4] += 1
    else:
        raise ValueError(i)
    return _vec_to_root(tuple(v))


# ====================================================================
# Alpha_i-string structure on Phi^+(B_5).
# Same construction as B_4: length-2 chains for long simples, length-3 chains
# for the short simple alpha_5. See b_i_b4.py for the precise CST Def 2.14
# bracketing rule.
# ====================================================================

def _chains_for_long(i: int) -> List[Tuple[str, str]]:
    """For long simple i in {1,2,3,4}: list of (bot, top) chains in CONVEX
    order of the TOP.
    """
    chains = []
    simple_i_name = simple_root(i)
    for bot in ROOTS_CONVEX:
        if bot == simple_i_name:
            continue
        top = root_plus_alpha(bot, i)
        if top is None:
            continue
        chains.append((bot, top))
    conv_pos = {r: idx for idx, r in enumerate(ROOTS_CONVEX)}
    chains.sort(key=lambda bt: conv_pos[bt[1]])
    return chains


def _chains_for_short() -> List[Tuple[str, str, str]]:
    """For alpha_5 (short): list of (bot, mid, top) chains in convex order of the MID.
    Chains: bot = e_a - e_5, mid = e_a, top = e_a + e_5 for a = 1, 2, 3, 4.
    """
    triples = []
    for a in [1, 2, 3, 4]:
        bot = {1: EM15, 2: EM25, 3: EM35, 4: EM45}[a]
        mid = {1: E1,   2: E2,   3: E3,   4: E4}[a]
        top = {1: EP15, 2: EP25, 3: EP35, 4: EP45}[a]
        triples.append((bot, mid, top))
    conv_pos = {r: idx for idx, r in enumerate(ROOTS_CONVEX)}
    triples.sort(key=lambda bmt: conv_pos[bmt[1]])
    return triples


# Cached:
_LONG_CHAINS = {i: _chains_for_long(i) for i in (1, 2, 3, 4)}
_SHORT_CHAINS = _chains_for_short()


def S_i(pi: KP, i: int) -> List[Tuple[str, str]]:
    """Bracketing sequence for alpha_i in B_5 (CST Def 2.14)."""
    s = []
    if i in (1, 2, 3, 4):
        for (bot, top) in _LONG_CHAINS[i]:
            for _ in range(pi.get(top, 0)):
                s.append((')', top))
            for _ in range(pi.get(bot, 0)):
                s.append(('(', bot))
        simp = simple_root(i)
        for _ in range(pi.get(simp, 0)):
            s.append((')', simp))
        return s
    if i == 5:
        for (bot, mid, top) in _SHORT_CHAINS:
            for _ in range(pi.get(mid, 0)):
                s.append((')', mid))
            for _ in range(2 * pi.get(bot, 0)):
                s.append(('(', bot))
            for _ in range(2 * pi.get(top, 0)):
                s.append((')', top))
            for _ in range(pi.get(mid, 0)):
                s.append(('(', mid))
        for _ in range(pi.get(E5, 0)):
            s.append((')', E5))
        return s
    raise ValueError(f"i must be 1..5, got {i}")


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
# Crystal operators e_i, f_i (CST Def 2.14)
# ====================================================================

def e_i(pi: KP, i: int) -> Optional[KP]:
    """e_i pi: rightmost ')' in S_i^c, beta -> beta - alpha_i (or removed if 0)."""
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
# Enumeration
# ====================================================================

def enumerate_partitions(max_total):
    """Enumerate Kostant partitions pi with sum c <= max_total."""
    out = []
    n = len(ROOTS)
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


def k_i(i):
    return 1 if i in (1, 2, 3, 4) else 2
